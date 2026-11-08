"""Modelo de referencia sin I/O de la política de retorno del streamer.

NO es el motor autoritativo. El handler .NET debe implementar este contrato en
transacción serializable con locks, writerEpoch, Idempotency-Key y Outbox.
"""
from dataclasses import dataclass, replace
from datetime import datetime, timedelta, timezone
from enum import Enum


class IncidentState(str, Enum):
    PAUSED = "PAUSED"
    RESUMED = "RESUMED"
    ABORTED = "ABORTED"


class ReturnError(ValueError):
    pass


@dataclass(frozen=True)
class Departure:
    incident_id: str
    primary_account_id: str
    confirmed_at_utc: datetime
    state: IncidentState = IncidentState.PAUSED
    resolved_at_utc: datetime | None = None
    completed_idempotency_key: str | None = None
    live_seconds_at_pause: int = 0
    economy_ms_at_pause: int = 0
    competition_state: str = "PAUSED"

    @property
    def cancel_at_utc(self) -> datetime:
        _utc(self.confirmed_at_utc)
        return self.confirmed_at_utc + timedelta(days=7)


@dataclass(frozen=True)
class ReturnEvidence:
    account_id: str
    owner_approved: bool
    identity_reverified: bool
    binding_reverified: bool
    capabilities: frozenset[str]
    idempotency_key: str


def _utc(t: datetime) -> None:
    if t.tzinfo is None or t.utcoffset() != timedelta():
        raise ValueError("UTC-aware datetime required")


def expire(incident: Departure, at_utc: datetime) -> Departure:
    """ABORTED at exact boundary; settled incidents are immutable."""
    _utc(at_utc)
    if incident.state != IncidentState.PAUSED:
        return incident
    if at_utc < incident.cancel_at_utc:
        return incident
    return replace(incident, state=IncidentState.ABORTED,
                   resolved_at_utc=at_utc)


def verified_return(incident: Departure, at_utc: datetime,
                    evidence: ReturnEvidence) -> Departure:
    """Exactly the same K0 primary, OWNER and two capabilities, strictly <7d.

    The returned dataclass preserves all clocks and cancelled competitions;
    wall-clock gaps are not credited. Terminal states cannot be resurrected.
    """
    _utc(at_utc)
    if incident.state == IncidentState.RESUMED:
        if evidence.idempotency_key == incident.completed_idempotency_key:
            return incident
        raise ReturnError("ALREADY_RESUMED")
    if incident.state == IncidentState.ABORTED:
        raise ReturnError("SEASON_ABORTED")
    if at_utc >= incident.cancel_at_utc:
        raise ReturnError("RETURN_DEADLINE_EXPIRED_ABORT_WINS")
    if at_utc < incident.confirmed_at_utc:
        raise ReturnError("RETURN_BEFORE_DEPARTURE")
    if not evidence.idempotency_key or len(evidence.idempotency_key) < 12:
        raise ReturnError("IDEMPOTENCY_REQUIRED")
    if evidence.account_id != incident.primary_account_id:
        raise ReturnError("PRIMARY_ACCOUNT_MISMATCH")
    if not evidence.owner_approved:
        raise ReturnError("OWNER_APPROVAL_REQUIRED")
    if not evidence.identity_reverified or not evidence.binding_reverified:
        raise ReturnError("CHANNEL_REVERIFICATION_REQUIRED")
    if not {"CHAT_READ", "LIVE_PRESENCE"} <= evidence.capabilities:
        raise ReturnError("LIVE_CAPABILITY_NOT_VERIFIED")
    return replace(incident, state=IncidentState.RESUMED,
                   resolved_at_utc=at_utc,
                   completed_idempotency_key=evidence.idempotency_key)
