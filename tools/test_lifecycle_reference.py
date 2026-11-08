"""Casos de borde reproducibles de la política de incidentes del streamer."""
from dataclasses import replace
from datetime import datetime, timedelta, timezone
import unittest
from lifecycle_reference import (
    Departure, IncidentState, ReturnEvidence, ReturnError, expire, verified_return
)


class DeparturePolicyTests(unittest.TestCase):
    def setUp(self):
        self.start = datetime(2026, 11, 9, 10, tzinfo=timezone.utc)
        self.i = Departure("incident1", "primary", self.start,
                           live_seconds_at_pause=987, economy_ms_at_pause=543210,
                           competition_state="CANCELLED")
        self.good = ReturnEvidence("primary", True, True, True,
                                   frozenset({"CHAT_READ", "LIVE_PRESENCE"}),
                                   "idem-key-000001")

    def test_just_before_seven_days_can_return(self):
        outcome = verified_return(self.i, self.i.cancel_at_utc - timedelta(
            milliseconds=1), self.good)
        self.assertEqual(outcome.state, IncidentState.RESUMED)
        self.assertEqual(outcome.live_seconds_at_pause, 987)
        self.assertEqual(outcome.economy_ms_at_pause, 543210)
        self.assertEqual(outcome.competition_state, "CANCELLED")

    def test_at_exact_deadline_aborted_wins(self):
        at = self.i.cancel_at_utc
        self.assertEqual(expire(self.i, at).state, IncidentState.ABORTED)
        with self.assertRaisesRegex(ReturnError, "ABORT_WINS"):
            verified_return(self.i, at, self.good)

    def test_after_deadline_rejected(self):
        at = self.i.cancel_at_utc + timedelta(seconds=1)
        with self.assertRaises(ReturnError):
            verified_return(self.i, at, self.good)

    def test_stale_expiration_before_deadline_is_noop(self):
        self.assertEqual(expire(self.i, self.i.cancel_at_utc-timedelta(seconds=1)), self.i)

    def test_wrong_account_rejected(self):
        with self.assertRaisesRegex(ReturnError, "PRIMARY_ACCOUNT_MISMATCH"):
            verified_return(self.i, self.start + timedelta(minutes=2),
                            replace(self.good, account_id="other"))

    def test_owner_approval_required(self):
        with self.assertRaisesRegex(ReturnError, "OWNER_APPROVAL_REQUIRED"):
            verified_return(self.i, self.start + timedelta(minutes=2),
                            replace(self.good, owner_approved=False))

    def test_verified_channel_and_capabilities_required(self):
        for evidence in (
            replace(self.good, binding_reverified=False),
            replace(self.good, identity_reverified=False),
            replace(self.good, capabilities=frozenset({"CHAT_READ"})),
        ):
            with self.assertRaises(ReturnError):
                verified_return(self.i, self.start + timedelta(minutes=2), evidence)

    def test_idempotent_retries_do_not_recredit(self):
        at = self.start + timedelta(minutes=1)
        first = verified_return(self.i, at, self.good)
        self.assertEqual(verified_return(first, at, self.good), first)
        with self.assertRaisesRegex(ReturnError, "ALREADY_RESUMED"):
            verified_return(first, at, replace(self.good,
                                              idempotency_key="idem-key-different"))

    def test_abort_is_terminal(self):
        closed = expire(self.i, self.i.cancel_at_utc)
        self.assertEqual(expire(closed, self.i.cancel_at_utc+timedelta(days=10)), closed)
        with self.assertRaisesRegex(ReturnError, "SEASON_ABORTED"):
            verified_return(closed, closed.cancel_at_utc+timedelta(days=1), self.good)

    def test_second_incident_keeps_first_history(self):
        recovered = verified_return(self.i, self.start + timedelta(days=1), self.good)
        second = Departure("incident2", recovered.primary_account_id,
                           self.start+timedelta(days=2))
        self.assertEqual(recovered.state, IncidentState.RESUMED)
        self.assertEqual(second.state, IncidentState.PAUSED)
        self.assertNotEqual(second.incident_id, recovered.incident_id)

    def test_utc_required(self):
        with self.assertRaises(ValueError):
            verified_return(self.i, datetime(2026, 11, 10), self.good)


if __name__ == "__main__":
    unittest.main()
