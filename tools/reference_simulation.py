#!/usr/bin/env python3
"""Conservative, deterministic FREE-path reference simulation for K0 v2.2.

Covers five REAL milestones per playable era, ordinary stock/capacity, food upkeep,
mandatory technology, civic building, storage, UTC missions and LIVE-only era advance.
Not the authoritative game engine: excludes optional buildings, player XP/perks,
elections, strategic votes, war, map placement, NPC growth, event injection and DB.
No monetization is present. Results are *model evidence*, not production proof.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROLES = ("food", "wood", "mine", "build", "research")
RESOURCES = ("food", "wood", "stone", "ore", "knowledge")
DENOMINATOR = 60 * 4 * 10000


def load(name: str):
    return json.loads((ROOT / "data" / name).read_text(encoding="utf-8"))


@dataclass
class ReferenceState:
    tick: int = 0
    era_index: int = 1
    stock: dict[str, int] = field(default_factory=dict)
    caps: dict[str, int] = field(default_factory=dict)
    remainder: dict[str, int] = field(default_factory=dict)
    produced_era: dict[str, int] = field(default_factory=dict)
    produced_day: dict[str, int] = field(default_factory=dict)
    work_remainder: int = 0
    work_done: int = 0
    active_construction: dict | None = None
    complete_buildings: set[str] = field(default_factory=set)
    tech_done: set[str] = field(default_factory=set)
    claimed_missions: set[tuple[str, int]] = field(default_factory=set)
    completed_milestones: set[str] = field(default_factory=set)
    mission_completed_era: bool = False
    day_index: int = -1
    week_index: int = -1
    weekly_buildings_completed: int = 0
    weekly_effective_worker_numerator: int = 0
    storage_built_by_era: dict[int, int] = field(default_factory=dict)
    total_milestones: int = 0
    era_entered_at: dict[str, int] = field(default_factory=dict)
    shortage_seconds: int = 0
    blocked_milli: int = 0
    live_seconds: int = 0
    state_hash: str = ""


def cohort_quarters(total: int, mix: str = "balanced", scope: str = "nation_total") -> dict[str, int]:
    """Synthetic always-active roster sorted by (activeSinceUtc, citizenId).

    First 100 people full (4 quarters), next 2400 quarter (1), rest zero.
    Under nation_total the thresholds apply across ALL professions, not per role.
    Viewer fixtures renew activity hourly; not a live chat integration.
    """
    if scope != "nation_total":
        raise ValueError("Unsupported worker scope")
    if total < 0 or total > 100000:
        raise ValueError("Viewers outside documented limit")
    out = dict.fromkeys(ROLES, 0)
    for i in range(min(total, 2500)):
        role = ROLES[i % 5] if mix == "balanced" else (
            "food" if i % 10 < 7 else ROLES[1 + ((i % 10 - 7) % 4)]
        )
        out[role] += 4 if i < 100 else 1
    return out


def run(
    viewers: int = 0,
    mix: str = "balanced",
    live_hours: int = 24,
    maximum_wall_days: int = 90,
    seed: str = "reference-v22",
    finish_at_era: int = 13,
) -> dict:
    """Run exact five-second integer steps under a deliberately limited model."""
    if not 0 < live_hours <= 24:
        raise ValueError("At least some LIVE time is needed to advance eras")
    if not 1 < finish_at_era <= 13:
        raise ValueError("Invalid requested terminal era")
    rules = load("ruleset.v2.json")
    eras = load("eras.v2.json")["eras"]
    all_milestones = load("milestones.v2.json")["milestones"]
    techs = {t["id"]: t for t in load("technologies.v2.json")["technologies"]}
    buildings = {v["id"]: v for v in load("buildings.v2.json")["buildingCatalog"]}
    missions = load("missions.v2.json")["missions"]
    npc = rules["citizens"]["initialNpcAllocation"]
    human = cohort_quarters(viewers, mix, rules["citizens"]["activeHumanWorkersScope"])
    s = ReferenceState()
    s.stock = {name: 0 for name in RESOURCES}
    s.caps = {name: int(rules["resources"]["capacityInitial"][name]) * 1000 for name in RESOURCES}
    s.remainder = {name: 0 for name in RESOURCES}
    s.produced_era = {name: 0 for name in RESOURCES}
    s.produced_day = {name: 0 for name in RESOURCES}
    s.era_entered_at[eras[0]["id"]] = 0
    upkeep_remainder = 0
    current_day = 0
    current_week = 0
    building_civic = lambda: buildings[eras[s.era_index - 1]["signatureBuildingId"]]

    def can_pay(b: dict) -> bool:
        return all(s.stock.get(name, 0) >= val * 1000
                   for name, val in b["cost"].items() if name in RESOURCES)

    def start(b: dict):
        for name, val in b["cost"].items():
            if name in RESOURCES:
                s.stock[name] -= val * 1000
                assert s.stock[name] >= 0
        s.active_construction = b
        s.work_done = 0
        s.work_remainder = 0

    def end_mission(m: dict, period: int):
        s.claimed_missions.add((m["id"], period))
        for name, value in m["reward"].items():
            s.stock[name] = min(s.caps[name], s.stock[name] + value * 1000)
        # Only a mission completed during this era can credit its milestone.
        if m["id"] in eligible_missions:
            s.mission_completed_era = True

    for tick in range(maximum_wall_days * 86400 // 5):
        s.tick = tick + 1
        t0 = tick * 5
        live = t0 % 86400 < live_hours * 3600
        s.live_seconds += 5 if live else 0
        economy_bp = (rules["simulation"]["liveEconomyBp"]
                      if live else rules["simulation"]["offlineEconomyBp"])
        if t0 // 86400 != current_day:
            current_day = t0 // 86400
            s.produced_day = dict.fromkeys(RESOURCES, 0)
        if t0 // (7 * 86400) != current_week:
            current_week = t0 // (7 * 86400)
            s.weekly_buildings_completed = 0
            s.weekly_effective_worker_numerator = 0
        s.weekly_effective_worker_numerator += (
            (sum(npc.values()) * 4 + sum(human.values())) * 5 * economy_bp
        )

        # Eat first, and record any shortage before productivity.
        human_quarters = sum(human.values())
        accountable_quarters = min(human_quarters, 4 * rules["resources"]["maxHumanFoodUpkeepEquivalentWorkers"])
        upkeep_quarters = sum(npc.values()) * 4 + accountable_quarters
        upkeep_num = (rules["resources"]["foodConsumedPerNpcUnitPerMinuteMilli"]
                      * upkeep_quarters * 5 * economy_bp)
        upkeep, upkeep_remainder = divmod(upkeep_remainder + upkeep_num, DENOMINATOR)
        shortage = upkeep > s.stock["food"]
        s.stock["food"] = max(0, s.stock["food"] - upkeep)
        if shortage:
            s.shortage_seconds += 5
        starvation_bp = rules["resources"]["foodShortageProductionBp"] if shortage else 10000

        # With an identical seed and fixture, all operations are deterministic
        # integer arithmetic. Building boosts are deliberately omitted.
        for role, names in (
            ("food", (("food", 10000),)),
            ("wood", (("wood", 10000),)),
            ("mine", (("stone", 10000),) if s.era_index < 3
             else (("stone", 7500), ("ore", 2500))),
            ("research", (("knowledge", 10000),)),
        ):
            quarters = npc[role] * 4 + human[role]
            for name, share_bp in names:
                rate = rules["baseOutputMilliPerWorkerMinute"][name]
                numerator = rate * quarters * 5 * economy_bp * starvation_bp * share_bp
                # Preserve fractions by using a fixed, explicit denominator.
                # DENOMINATOR (per minute, quarters, economy BP) × two bonuses.
                divisor = DENOMINATOR * 10000 * 10000
                whole, rest = divmod(
                    s.remainder[name] + numerator, divisor
                )
                s.remainder[name] = rest
                accepted = min(max(0, s.caps[name] - s.stock[name]), whole)
                s.blocked_milli += whole - accepted
                s.stock[name] += accepted
                s.produced_era[name] += accepted
                s.produced_day[name] += accepted

        era = eras[s.era_index - 1]
        eligible_missions = next(
            m["eligibleMissionIds"] for m in all_milestones
            if m["eraId"] == era["id"] and m["triggerKind"] == "mission_completed"
        )

        # Automatic free mandatory research: never consumes gold.
        current_tech = techs[era["researchTrackId"]]
        if current_tech["id"] not in s.tech_done and all(
            req in s.tech_done for req in current_tech["requires"]
        ) and s.stock["knowledge"] >= current_tech["costKnowledge"] * 1000:
            s.stock["knowledge"] -= current_tech["costKnowledge"] * 1000
            s.tech_done.add(current_tech["id"])

        # One civic per era; storage is built when any ordinary stock crosses 75%.
        if s.active_construction is None:
            civic = building_civic()
            storage = buildings[f"{era['id']}_storage"]
            storage_count = s.storage_built_by_era.get(s.era_index, 0)
            storage_pressure = any(
                s.stock[name] * 4 >= s.caps[name] * 3 for name in RESOURCES
            )
            if civic["id"] not in s.complete_buildings and can_pay(civic):
                start(civic)
            elif storage_pressure and storage_count < storage["maxInstancesPerNation"] and can_pay(storage):
                start(storage)
                s.storage_built_by_era[s.era_index] = storage_count + 1

        if s.active_construction is not None:
            quarters = npc["build"] * 4 + human["build"]
            rate = rules["baseOutputMilliPerWorkerMinute"]["buildWork"]
            numerator = rate * quarters * 5 * economy_bp * starvation_bp
            # work amount in milli units, same integer fraction convention.
            divisor = DENOMINATOR * 10000
            work, s.work_remainder = divmod(s.work_remainder + numerator, divisor)
            s.work_done += work
            b = s.active_construction
            if s.work_done >= b["buildWorkUnits"] * 1000:
                s.complete_buildings.add(b["id"])
                s.weekly_buildings_completed += 1
                if b["family"] == "storage":
                    gain = b["effects"]["capacityAddEachResource"] * 1000
                    for name in RESOURCES:
                        s.caps[name] += gain
                s.active_construction = None
                s.work_done = 0

        # Mission window: per mission, per calendar period; rewards are not production.
        for mission in missions:
            if mission["period"] == "DAY_UTC":
                period = t0 // 86400
            else:
                period = t0 // (7 * 86400)
            if (mission["id"], period) in s.claimed_missions:
                continue
            goal = mission["goal"]
            kind = goal["kind"]
            met = (
                (kind == "produce_food" and s.produced_day["food"] >= goal["units"] * 1000)
                or (kind == "produce_wood" and s.produced_day["wood"] >= goal["units"] * 1000)
                or (kind == "produce_knowledge" and s.produced_day["knowledge"] >= goal["units"] * 1000)
                or (kind == "complete_basic_buildings"
                    and s.weekly_buildings_completed >= goal["count"])
                or (kind == "effective_worker_minutes"
                    and s.weekly_effective_worker_numerator >= goal["units"] * DENOMINATOR)
            )
            if met:
                end_mission(mission, period)

        # Evaluate the actual five configured milestones, not a synthetic score.
        for m in all_milestones:
            if m["eraId"] != era["id"] or m["id"] in s.completed_milestones:
                continue
            kind = m["triggerKind"]
            ok = False
            if kind == "food_production":
                ok = s.produced_era["food"] >= m["targetProductionUnits"] * 1000
            elif kind == "materials_production":
                ok = all(s.produced_era[name] >= value * 1000
                         for name, value in m["targetProductionByResourceUnits"].items())
            elif kind == "knowledge_production":
                ok = (s.produced_era["knowledge"] >= m["targetProductionUnits"] * 1000
                      and m["requiresTechnologyId"] in s.tech_done)
            elif kind == "signature_basic_building_completed":
                ok = m["targetBuildingId"] in s.complete_buildings
            elif kind == "mission_completed":
                ok = s.mission_completed_era
            if ok:
                s.completed_milestones.add(m["id"])
                s.total_milestones += 1

        points = sum(m["points"] for m in all_milestones
                     if m["eraId"] == era["id"] and m["id"] in s.completed_milestones)
        if points == 100 and live:
            s.era_index += 1
            next_era = eras[s.era_index - 1]["id"]
            s.era_entered_at[next_era] = (tick + 1) * 5
            if s.era_index >= finish_at_era:
                break
            s.produced_era = dict.fromkeys(RESOURCES, 0)
            s.mission_completed_era = False
        assert all(x >= 0 for x in s.stock.values())
    else:
        raise RuntimeError(
            f"Reference model stalled at era {s.era_index} after {maximum_wall_days} days; "
            f"milestones={len(s.completed_milestones)} stock={s.stock}"
        )

    assert s.era_index == finish_at_era
    assert s.total_milestones == (finish_at_era - 1) * 5
    assert all(t in s.tech_done for t in (f"tech_{e['id']}" for e in eras[:finish_at_era - 1]))
    assert all(f"{e['id']}_civic" in s.complete_buildings for e in eras[:finish_at_era - 1])
    result = {
        "model": "FREE_PATH_REFERENCE_NOT_AUTHORITATIVE",
        "rulesetHash": hashlib.sha256((ROOT / "data/ruleset.v2.json").read_bytes()).hexdigest(),
        "seed": seed,  # map/competition RNG not exercised by this conservative route
        "viewers": viewers, "mix": mix, "liveHoursDaily": live_hours,
        "endEraIndex": s.era_index, "milestonesAchieved": s.total_milestones,
        "technologiesRequiredCompleted": finish_at_era - 1,
        "civicBuildingsCompleted": finish_at_era - 1,
        "wallSeconds": s.tick * 5, "liveSeconds": s.live_seconds,
        "eraEntryWallSeconds": s.era_entered_at,
        "foodShortageSeconds": s.shortage_seconds,
        "blockedProductionMilli": s.blocked_milli, "goldSpent": 0,
    }
    result["resultHash"] = hashlib.sha256(json.dumps(result, sort_keys=True).encode()).hexdigest()
    return result


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--viewers", type=int, default=0)
    p.add_argument("--mix", choices=("balanced", "skewed"), default="balanced")
    p.add_argument("--live-hours", type=int, default=24)
    p.add_argument("--max-days", type=int, default=90)
    args = p.parse_args()
    print(json.dumps(run(args.viewers, args.mix, args.live_hours, args.max_days),
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
