#!/usr/bin/env python3
"""Coverage matrix for *conservative reference* economics, not a live-game benchmark."""
import argparse
import json
from pathlib import Path
from reference_simulation import run

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("evidence/reference_matrix_v2.2.json"))
    args = parser.parse_args()
    cases = []
    for live_hours in (4, 24):
        for mix in ("balanced", "skewed"):
            for viewers in (0, 10, 100, 1000, 10000):
                report = run(viewers=viewers, mix=mix, live_hours=live_hours,
                             maximum_wall_days=90, seed="baseline-cosmetic-seed")
                assert report["milestonesAchieved"] == 60
                assert report["endEraIndex"] == 13
                assert report["goldSpent"] == 0
                cases.append(report)
                print(f"CASE_OK live={live_hours}h viewers={viewers} mix={mix} "
                      f"wallDays={report['wallSeconds']/86400:.2f} "
                      f"blockedMilli={report['blockedProductionMilli']}")
    # A different seed changes the report identity but is deliberately not
    # economic input: every nation uses the same logical buildable map.
    output = {
        "model": "CONSERVATIVE_FREE_PATH_NOT_AUTHORITATIVE",
        "limitations": [
            "No real chat commands, votes, XP, perks, extra buildings, map or combat.",
            "No database transactions/replay or external provider events.",
            "Simulation seeds are cosmetic-only; not independent balance samples.",
            "Profiles model continuously active synthetic humans renewed hourly."
        ],
        "caseCount": len(cases),
        "cases": cases,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(f"MATRIX_PASS cases={len(cases)} allReachedEra=13 allRealMilestones=60")

if __name__ == "__main__":
    main()
