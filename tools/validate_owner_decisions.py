#!/usr/bin/env python3
"""Guardrails de las veinte decisiones explícitas del propietario.

No certifica motores, permisos LIVE, cumplimiento legal ni arte realmente producido.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def load(path: str):
    return json.loads(read(path))


def validate() -> list[str]:
    rules = load("data/ruleset.json")
    schema = load("contracts/ruleset.schema.json")
    art = load("data/art_spec.json")
    money = load("data/monetization_rules.json")
    man = load("data/content_manifest.json")
    master = read("docs/ESPECIFICACION.md")
    identity = load("contracts/multistreamer.schema.json")

    require(rules["schemaVersion"] == schema["properties"]["schemaVersion"]["const"],
            "Ruleset/schema version diverged")
    require(man["schemaVersion"] == rules["schemaVersion"],
            "Manifest/ruleset version diverged")
    require("docs/ESPECIFICACION.md" == rules["sourcePriority"][1],
            "Master is not the single current source of truth")

    # Every owner decision is a row in the SAME master file.
    owner_rows = re.findall(r"^\| (\d{2}) \|", master, re.MULTILINE)
    require(sorted(set(owner_rows)) == [f"{i:02d}" for i in range(1, 21)],
            "Master must contain decisions 01..20 exactly")
    require(len(owner_rows) == 20, "Missing or duplicated owner decision row")

    def rule(section: str, key: str, value) -> None:
        block = rules[section]
        require(block.get(key) == value, f"{section}.{key} disagrees with owner decision")
        section_schema = schema["properties"][section]
        require(key in section_schema["required"], f"Schema must require {section}.{key}")
        require(section_schema["properties"][key].get("const") == value,
                f"Schema const disagrees with {section}.{key}")

    # First delivery, mode, platform and season duration.
    rule("release", "firstDelivery", "TWELVE_PLAYABLE_ERAS_ENGINE_COMPLETE_BEFORE_PLATFORM_INTEGRATION")
    rule("release", "firstLaunchMode", "SINGLE_OPERATOR_THREE_CHANNELS")
    rule("release", "firstRealPlatform", "youtube")
    rule("release", "requiresAuthorizedProviderEvidence", True)
    rule("progression", "targetSeasonWallDaysMin", 45)
    rule("progression", "targetSeasonWallDaysMax", 90)
    rule("progression", "averageEraTargetDays", 5.5)
    require(rules["progression"]["finalEraIndex"] == 13
            and rules["progression"]["finalEraGameplayEnabled"] is False,
            "12 eras playable + 13 terminal must remain")
    rule("nations", "unequalLiveSchedulesAllowed", True)
    rule("nations", "unequalLiveHoursCompensation", False)
    rule("nations", "multistreamerStartCondition",
         "three_authorized_bindings_no_simultaneous_live_required")
    rule("season", "startCondition", "THREE_AUTHORIZED_CHANNELS_NOT_THREE_SIMULTANEOUS_LIVES")
    rule("season", "showAccumulatedLiveHoursByNation", True)
    rule("season", "streamerAbandonmentPolicy",
         "CONFIRMED_EXIT_GLOBAL_PAUSE_ABORT_AFTER_7_WALL_DAYS")
    rule("season", "streamerAbandonmentCancelAfterDays", 7)
    rule("season", "streamerReturnPolicy",
         "SAME_PRIMARY_REVERIFIED_OWNER_APPROVED_BEFORE_DEADLINE")
    rule("season", "streamerReturnDeadline",
         "STRICT_BEFORE_7_DAY_UTC_DEADLINE_ABORT_AT_EQUALITY")
    rule("season", "streamerReturnPauseClockPolicy",
         "NO_RETROACTIVE_ECONOMY_OR_LIVE_CATCHUP")
    rule("season", "streamerReturnCancelledCompetitionPolicy",
         "NEVER_REOPEN_CANCELLED")
    rule("season", "streamerReturnMultipleIncidents",
         "AUDIT_EACH_INCIDENT_ONE_ACTIVE_PER_SEASON")
    rule("tournaments", "maxPausedTournamentWallHours", 72)
    rule("tournaments", "pausedTournamentTimeoutPolicy", "CANCEL_WITHOUT_PENALTY")

    # One worker quota for the *entire* nation and one nation for each K0 account.
    rule("citizens", "activeHumanWorkersSoftCapScope", "PER_NATION_TOTAL")
    rule("citizens", "humanQuotaAssignment", "deterministic_hash_rotation_nation_live_600s")
    rule("citizens", "accountAllegiance", "ONE_K0_ACCOUNT_ONE_NATION_PER_SEASON")
    rule("citizens", "chatIdentityFlow",
         "AUTO_PROVISION_K0_ACCOUNT_FROM_VERIFIED_PROVIDER_IDENTITY")
    rule("citizens", "crossProviderUniqueness",
         "REQUIRES_EXPLICIT_VERIFIED_ACCOUNT_LINK")
    rule("citizens", "displayIdentityPolicy", "GENERATED_PSEUDONYM_ALIAS_OPT_IN")
    curve = rules["citizens"]["humanContributionCurve"]
    require((curve["first"], curve["firstBp"], curve["last"],
             curve["lastBp"], curve["afterLastBp"]) ==
            (100, 10000, 2500, 2500, 0), "National quota band boundaries differ")
    rule("citizens", "humanWorkXpEligibility", "accepted_effective_work_only")
    commands = {x["id"]: x for x in load("data/commands.json")["commands"]}
    require(commands["join"]["precondition"] == "authenticated_provider_identity"
            and commands["work"]["precondition"] == "registered_citizen",
            "Chat-only join / registered work identity semantics drifted")

    # Initial business/art/narration/safety and money budget.
    rule("release", "monetizationGate", "AFTER_GAME_VALIDATED_AND_PLATFORM_LEGAL_APPROVED")
    rule("release", "ownShowFirst", True)
    rule("release", "saasDeferred", True)
    rule("release", "publicLaunchMarket", "ES_EU_GENERAL_AUDIENCE")
    rule("release", "minorSafeguardsRequired", True)
    rule("release", "maxMonthlyInfraBudgetEur", 100)
    rule("operator", "maxMonthlyInfrastructureBudgetEur", 100)
    rule("operator", "narrationMode", "GENERATIVE_LLM_REALTIME_DYNAMIC_TTS")
    rule("operator", "narrationAuthority", "CONFIRMED_FACTS_ONLY_NO_GAME_MUTATIONS")
    rule("operator", "narrationFallback", "APPROVED_TEMPLATES_AND_SUBTITLES")
    rule("presentation", "pilotLocales", ["es-ES"])
    rule("presentation", "pilotLayouts", ["VERTICAL_360_640", "HORIZONTAL_640_360"])
    rule("presentation", "allPlayableEraArtRequiredBeforeFirstPilot", True)
    rule("presentation", "requiredPlayableEraArtCount", 12)
    rule("presentation", "terminalEpilogueArtRequiredBeforeFirstPilot", True)
    require(art["requireAllPlayableEraArtBeforeFirstPilot"]
            and art["requiredPlayableEraCount"] == 12
            and art["terminalEpilogueArtRequired"],
            "Art catalog contradicts owner's pilot scope")
    require(money["liveMonetizationEnabled"] is False
            and money["initialPublicLaunchEnabled"] is False
            and money["firstBusinessModel"] == "OWN_LIVE_SHOW",
            "Early monetization or wrong business goal")
    rule("privacy", "operationalDataRetentionDays", 30)
    rule("privacy", "publicNamePolicy", "PSEUDONYM_BY_DEFAULT_ALIAS_ONLY_WITH_CONSENT")
    rule("privacy", "minorProtection",
         "EU_GENERAL_AUDIENCE_MINIMIZATION_NO_TARGETED_MONETIZATION")
    # The old v2.2 worker scope and Council payment state are forbidden in
    # active normative/SQL artifacts, not merely discouraged in prose.
    blueprint = read("docs/67_BLUEPRINT_IMPLEMENTACION_Y_PRUEBAS.md")
    require("cap por profesión" not in blueprint,
            "Implementation blueprint still assumes per-profession human cap")
    require("Twitch/YouTube (los que demuestren permisos)" not in blueprint,
            "Implementation blueprint has not prioritised YouTube")
    base_sql = read("architecture/001_schema.sql")
    require("'PAYMENT_BLOCKED'" not in base_sql,
            "SQL still allows a Council state that implies gold blocking")
    return_schema = identity["$defs"].get("PrimaryBroadcasterReturn")
    require(return_schema is not None and
            "ownerApprovalUtc" in return_schema["required"] and
            "verifiedCapabilities" in return_schema["required"],
            "Broadcaster return DTO requires verified same-primary OWNER approval")
    api = read("contracts/openapi.yaml")
    require("/api/v2/operator/seasons/{seasonId}/primary-return:" in api and
            "operatorJwt: [owner]" in api,
            "Missing OWNER-only primary-return API")
    require("ux_one_active_primary_departure_per_season" in
            read("architecture/003_multistreamer_diseno.sql"),
            "Repeated departure audit needs one-active-incident partial unique index")
    require("ck_departure_resolution" in read("architecture/003_multistreamer_diseno.sql"),
            "SQL must check return-before-deadline, same primary and abort time")
    check_sql = read("architecture/003_multistreamer_diseno.sql")
    require("UNIQUE" in check_sql and "ux_citizen_one_nation_per_k0_account_season" in check_sql
            and "viewer_provider_account_links" in check_sql
            and "viewer_display_consents" in check_sql,
            "SQL design lacks account/nation/consent uniqueness")
    require("ViewerAccountAllegiance" in identity["$defs"],
            "Identity JSON contract lacks verified account binding")

    # Guard against reintroducing the previous incompatible quota and identity.
    descriptions = {
        "docs/ESPECIFICACION.md": [
            "primeros 100 activos por oficio", "por profesión y por nación",
            "puede tener ciudadanos distintos si interactúa", "PAYMENT_BLOCKED",
        ],
        "docs/04_ECONOMIA_Y_BALANCE.md": ["Primeros 100 activos por oficio"],
        "docs/06_PROFESIONES_HABILIDADES_Y_XP.md": [
            "100 plazas de contribución plena por profesión",
            "un ciudadano por nación/temporada",
        ],
        "docs/02_CANALES_CUENTAS_Y_NACIONES.md": [
            "sí puede crear ciudadanos distintos en naciones diferentes",
        ],
    }
    for file, forbidden in descriptions.items():
        doc = read(file).lower()
        for phrase in forbidden:
            require(phrase.lower() not in doc,
                    f"{file} still contains superseded semantics: {phrase}")

    # Real provider fixtures are topology examples, NOT permissions or API sessions.
    from uuid import UUID
    binding_schema = load("contracts/channel_binding.schema.json")
    for fixture in [
        "data/channel_bindings.example.json",
        "data/channel_presets/mixed.json",
        "data/channel_presets/three_youtube.json",
        "data/channel_presets/three_tiktok.json",
        "data/channel_presets/three_simulated.json",
    ]:
        preset = load(fixture)
        require(preset["schemaVersion"] ==
                binding_schema["properties"]["schemaVersion"]["const"],
                f"{fixture}: fixture and schema version disagree")
        try:
            UUID(preset["seasonId"])
        except (ValueError, TypeError):
            ERRORS.append(f"{fixture}: seasonId must be UUID")
        require(preset["status"] == "TOPOLOGY_EXAMPLE_ONLY_NOT_AUTHORIZED",
                f"{fixture}: must not represent authorized platform accounts")
        require(len(preset["assignments"]) == 3,
                f"{fixture}: exactly three distinct nations required")
        ids = set()
        slugs = set()
        for assignment in preset["assignments"]:
            try:
                UUID(assignment["nationId"])
            except (ValueError, TypeError):
                ERRORS.append(f"{fixture}: nationId must be UUID")
            ids.add(assignment["nationId"])
            slugs.add(assignment.get("factionId"))
            for binding in assignment["bindings"]:
                require(binding["monetizationEnabled"] is False,
                        f"{fixture}: fixture must not monetize")
                if binding["provider"] != "simulated":
                    require(binding["enabled"] is False,
                            f"{fixture}: real provider capability cannot be pre-authorized")
        require(len(ids) == 3 and slugs == {"micelios","runicos","ferrinos"},
                f"{fixture}: 3 unique nations and faction slugs required")

    return ERRORS


if __name__ == "__main__":
    for problem in validate():
        print("FAIL:", problem)
    if ERRORS:
        raise SystemExit(1)
    print("PASS: all 20 owner decisions consistent with the canonical rules/contract/schema")
    print("NOTE: design assertions are not engine/provider/art/budget acceptance tests")
