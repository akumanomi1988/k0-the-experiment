"""Tests unitarios del cálculo aislado; no equivalen a una temporada simulada."""
import unittest

from worker_math import (
    ActiveWorker, assign_human_weights, effective_worker_units_bp,
    output_milli_for_seconds,
)


class WorkerMathTests(unittest.TestCase):
    def workers(self, count, profession="food"):
        return [ActiveWorker(f"citizen-{i:05d}", profession, i) for i in range(count)]

    def test_quota_boundaries(self):
        for n, expected in [(0, 0), (10, 10_0000), (100, 100_0000),
                            (101, 100_2500), (2500, 700_0000),
                            (2501, 700_0000), (10000, 700_0000)]:
            with self.subTest(n=n):
                weighted = assign_human_weights(self.workers(n))
                self.assertEqual(effective_worker_units_bp(weighted), expected)

    def test_independent_profession_caps(self):
        weighted = assign_human_weights(self.workers(2501, "food")
                                        + self.workers(2501, "research"))
        self.assertEqual(effective_worker_units_bp(weighted), 14_000_000)
        self.assertEqual(sum(x.weight_bp > 0 for x in weighted), 5000)

    def test_stable_order(self):
        workers = [ActiveWorker("z", "food", 1), ActiveWorker("a", "food", 1)]
        self.assertEqual([x.citizen_id for x in assign_human_weights(reversed(workers))],
                         ["a", "z"])

    def test_duplicate_rejected(self):
        with self.assertRaises(ValueError):
            assign_human_weights(self.workers(1) * 2)

    def test_unknown_profession_rejected(self):
        with self.assertRaises(ValueError):
            assign_human_weights([ActiveWorker("x", "unknown", 0)])

    def test_tick_partition_invariance(self):
        # 1 trabajador a 2400 milésimas/minuto: 5s * 12 == 60s.
        remainder = 0
        total = 0
        for _ in range(12):
            part, remainder = output_milli_for_seconds(5 * 10000, 2400,
                                                       remainder=remainder)
            total += part
        once, once_rem = output_milli_for_seconds(60 * 10000, 2400)
        self.assertEqual((total, remainder), (once, once_rem))
        self.assertEqual(total, 2400)

    def test_fractional_worker(self):
        produced, rem = output_milli_for_seconds(60 * 2500, 1800)
        self.assertEqual((produced, rem), (450, 0))

    def test_multipliers(self):
        produced, rem = output_milli_for_seconds(60 * 10000, 2400, (2000,))
        self.assertEqual((produced, rem), (480, 0))

    def test_invalid_remainder(self):
        with self.assertRaises(ValueError):
            output_milli_for_seconds(0, 0, remainder=-1)


if __name__ == "__main__":
    unittest.main()
