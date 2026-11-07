"""Golden invariants for the conservative free-path model; not engine certification."""
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from reference_simulation import cohort_quarters, run

class ReferenceSimulationTests(unittest.TestCase):
    def test_national_quota_is_independent_of_role_mix(self):
        for mix in ("balanced", "skewed"):
            q100 = cohort_quarters(100, mix)
            q2500 = cohort_quarters(2500, mix)
            q10000 = cohort_quarters(10000, mix)
            self.assertEqual(sum(q100.values()), 400)
            self.assertEqual(sum(q2500.values()), 400 + 2400)
            self.assertEqual(q10000, q2500)
            self.assertEqual(sum(cohort_quarters(0, mix).values()), 0)

    def test_zero_audience_all_milestones(self):
        result = run(viewers=0, live_hours=24, maximum_wall_days=90)
        self.assertEqual(result["endEraIndex"], 13)
        self.assertEqual(result["milestonesAchieved"], 60)
        self.assertEqual(result["technologiesRequiredCompleted"], 12)
        self.assertEqual(result["civicBuildingsCompleted"], 12)
        self.assertEqual(result["goldSpent"], 0)
        self.assertEqual(len(result["eraEntryWallSeconds"]), 13)
        print("REFERENCE_ZERO_AUDIENCE " + json.dumps(result, sort_keys=True))

    def test_replay_same_hash(self):
        a = run(viewers=10, live_hours=24, maximum_wall_days=90)
        b = run(viewers=10, live_hours=24, maximum_wall_days=90)
        self.assertEqual(a["resultHash"], b["resultHash"])
        self.assertEqual(a["milestonesAchieved"], 60)

    def test_partial_live_day_reaches_final_era(self):
        result = run(viewers=0, live_hours=4, maximum_wall_days=90)
        self.assertEqual(result["milestonesAchieved"], 60)
        self.assertLess(result["liveSeconds"], result["wallSeconds"])
        print("REFERENCE_4H_LIVE " + json.dumps(result, sort_keys=True))

if __name__ == "__main__":
    unittest.main()
