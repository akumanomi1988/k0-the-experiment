"""La página vigente debe ser resultado de las fuentes, sin escritura en CI."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from sync_docs import sync, load, state, hashes, fill, CURRENT_TEMPLATE

class CurrentDocumentationTests(unittest.TestCase):
    def test_generated_docs_are_current(self):
        self.assertEqual(sync(False), [])

    def test_all_versions_from_pinned_sources(self):
        p = load("data/active_baseline.json")
        rh, ch, manifest = hashes(p)
        self.assertEqual(rh, manifest["rulesetHash"])
        self.assertEqual(ch, manifest["contentHash"])
        values = state(p, manifest)
        self.assertEqual(values["WORKER_SCOPE"], "nation_total")
        self.assertEqual(values["WORKER_ROTATION"], "none")
        self.assertEqual(values["XP_POLICY"], "accepted_effective_work_only")
        self.assertEqual(values["JOIN_PRE"], "authenticated_provider_identity")
        self.assertIn("2.2.0", fill(CURRENT_TEMPLATE, values))

if __name__ == "__main__":
    unittest.main()
