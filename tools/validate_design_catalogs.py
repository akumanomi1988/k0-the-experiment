#!/usr/bin/env python3
"""Static design baseline validation; DOES NOT simulate the game or certify LIVE."""
from __future__ import annotations
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FAILURES: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        FAILURES.append(message)


def load(path: str):
    file = ROOT / path
    check(file.is_file(), f"Missing {path}")
    if not file.is_file():
        return {}
    try:
        return json.loads(file.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeError) as e:
        FAILURES.append(f"Invalid JSON {path}: {e}")
        return {}


def main() -> int:
    manifest = load("data/content_manifest.v2.3.json")
    catalog_paths = [item.get("path", "") for item in manifest.get("files", [])]
    check(manifest.get("status") == "DESIGN_CANDIDATE_NOT_HASHED_OR_RELEASED",
          "Manifest must not pretend it has been released")
    check(len(catalog_paths) == len(set(catalog_paths)) and len(catalog_paths) >= 15,
          "Manifest paths must be unique and cover canonical catalogs")
    for entry in manifest.get("files", []):
        check((ROOT / entry.get("path", "")).is_file(),
              f"Manifest references missing file {entry.get('path')}")
    check("data/era_missions.v2.3.json" in catalog_paths,
          "Manifest missing era mission catalog")
    rules = load("data/ruleset.v2.json")
    eras = load("data/eras.v2.json").get("eras", [])
    milestones = load("data/milestones.v2.json").get("milestones", [])
    techs = load("data/technologies.v2.json").get("technologies", [])
    buildings = load("data/buildings.v2.json").get("buildingCatalog", [])
    strategic = load("data/strategic_projects.v2.json")
    era_missions = load("data/era_missions.v2.3.json").get("missions", [])
    skills = load("data/skills.v2.json").get("choices", [])
    professions = load("data/professions.v2.json").get("professions", [])
    units = load("data/combat_units.v2.2.json").get("units", [])
    for p in (
        "contracts/normalized_event.schema.json",
        "contracts/channel_binding.schema.json",
        "contracts/nation_delta.schema.json",
        "contracts/multistreamer.v2.3.schema.json",
    ):
        doc = load(p)
        check(bool(doc.get("$schema")), f"{p}: must declare $schema")
        if p != "contracts/multistreamer.v2.3.schema.json":
            check((doc.get("properties", {}).get("nationId", {}).get("format") == "uuid" or
                   doc.get("properties", {}).get("assignments", {}).get("items", {}).get("properties", {}).get("nationId", {}).get("format") == "uuid"),
                  f"{p}: nationId must be uuid")
            check("factionId" in doc.get("properties", {}) or
                  "factionId" in doc.get("properties", {}).get("assignments", {}).get("items", {}).get("properties", {}),
                  f"{p}: missing factionId")

    era_ids = [e.get("id") for e in eras]
    check(len(eras) == 13 and len(set(era_ids)) == 13, "13 unique eras required")
    check([e.get("order") for e in eras] == list(range(1, 14)), "Era order 1..13 required")
    for e in eras:
        check(e.get("gameplayAvailable") is (e.get("eraIndex") <= 12), f"Era {e.get('id')} playable flag")
    check(len(professions) == 5, "five profession families required")
    check(len(skills) == 30, "30 skills required")
    check(len(units) == 39, "39 unit roles required")

    tech_ids = {t.get("id") for t in techs}
    check(len(techs) == 39 and len(tech_ids) == 39, "39 unique technologies required")
    required_tech_ids = set()
    check(len(milestones) == 65, "5 milestones × 13 eras (final epilogue catalog)")
    check(Counter(m.get("eraIndex") for m in milestones) == Counter({i: 5 for i in range(1, 14)}),
          "five milestones per era")
    for m in milestones:
        check(m.get("points") == 20 and m.get("requiresGold") is False,
              f"Milestone {m.get('id')} must have 20 points and no gold")
        req = m.get("requiresTechnologyId")
        if req:
            if m.get("eraIndex", 13) <= 12:
                required_tech_ids.add(req)
            check(req in tech_ids, f"Milestone {m.get('id')} missing tech {req}")
        if m.get("triggerKind") == "mission_completed" and m.get("eraIndex") <= 12:
            check(m.get("eligibleMissionIds") == [f"era_mission_{m.get('eraId')}"],
                  f"Milestone {m.get('id')} must use era mission")
    for t in techs:
        check(bool(t.get("isRequiredForMilestone")) is (t.get("id") in required_tech_ids),
              f"Technology milestone flag drift: {t.get('id')}")
        check(t.get("costGold") == 0, f"Technology paid for by gold {t.get('id')}")

    check(len(era_missions) == 12 and len({x.get("eraId") for x in era_missions}) == 12,
          "12 unique era missions required")
    for x in era_missions:
        check(x.get("id") == f"era_mission_{x.get('eraId')}", f"Era mission ID mismatch {x}")
        check(x.get("npcCanComplete") is True and x.get("goldRequired") is False,
              f"Era mission must be free and completable by NPC {x.get('id')}")
        check(x.get("goal", {}).get("kind") == "productive_effective_worker_minutes"
              and x.get("goal", {}).get("units", 0) > 0, f"Era mission needs actual work {x.get('id')}")

    check(len(buildings) == 130, "130 basic buildings required")
    check(Counter(x.get("eraIndex") for x in buildings) == Counter({i: 10 for i in range(1, 14)}),
          "10 building families each era")
    for b in buildings:
        check(b.get("cost", {}).get("gold", 0) == 0, f"Building cannot require gold: {b.get('id')}")
        req = b.get("requiresTechId")
        if req:
            check(req in tech_ids, f"Building has unknown tech {b.get('id')} -> {req}")
        if b.get("family") in ("workshop", "research"):
            check(req == f"tech_{b.get('eraId')}", f"Workshop/research tech missing {b.get('id')}")

    projects, wonders = strategic.get("projects", []), strategic.get("wonders", [])
    check(len(projects) == 39 and len(wonders) == 13, "39 council projects and 13 wonders")
    check(Counter(x.get("eraIndex") for x in projects) == Counter({i: 3 for i in range(1,14)}),
          "3 council alternatives per era")
    for p in projects + wonders:
        check(p.get("cost", {}).get("gold") == 0, f"Gold forbidden in projects/wonders {p.get('id')}")
        check(p.get("gameplayAvailable") is (p.get("eraIndex") <= 12),
              f"Epilogue gating mismatch {p.get('id')}")
    check("no gold means no vote" not in strategic.get("candidatePool", "").lower(),
          "Legacy gold-vote description is still present")
    check(rules.get("status") == "DESIGN_BASELINE_CANDIDATE_NOT_IMPLEMENTED",
          "Ruleset is design candidate, not implemented")
    check(rules.get("simulation", {}).get("economyFactorAppliedOnce") is True,
          "Offline multiplier must be applied once")
    check(rules.get("strategic", {}).get("oneCouncilPerNationPerPlayableEra") is True,
          "Council one per playable era")
    check(rules.get("progression", {}).get("finalEraGameplayEnabled") is False,
          "Interestellar must be terminal")
    check(rules.get("citizens", {}).get("activeHumanWorkersSoftCapScope") ==
          "PER_PROFESSION_PER_NATION_DESIGN_CANDIDATE", "Human cap scope is ambiguous")

    sql = (ROOT / "architecture/001_schema_v2.sql").read_text(encoding="utf-8")
    check("'PAUSED'" in sql and "'COSMETIC_SPEND'" in sql,
          "Design DDL lacks paused votes / cosmetic gold entry")
    for p in ("docs/CURRENT_SPEC.md",
              "docs/63_ARQUITECTURA_MULTISTREAMER_v2.3.md",
              "docs/64_RELOJES_EVENTOS_Y_CONTRATOS_v2.3.md",
              "docs/65_DISENO_STREAMER_OVERLAYS_Y_ARTE_v2.3.md",
              "docs/66_INTEGRACIONES_SEGURIDAD_Y_OPERACION_v2.3.md",
              "docs/67_BLUEPRINT_IMPLEMENTACION_Y_PRUEBAS_v2.3.md"):
        check((ROOT / p).is_file(), f"Missing spec {p}")

    if FAILURES:
        print(f"FAILED: {len(FAILURES)} static design checks")
        for error in FAILURES:
            print(" -", error)
        return 1
    print("PASS: static K0 v2.3 catalogs/contracts design consistency")
    print("NOTE: no runtime, balance, migrations, OBS, legal or LIVE provider tests executed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
