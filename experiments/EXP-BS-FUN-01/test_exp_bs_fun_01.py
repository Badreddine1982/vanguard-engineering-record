import unittest
from exp_bs_fun_01 import make_problem, run_trial, prior_from_trial, run_suite


class ExperimentTests(unittest.TestCase):
    def test_problem_is_deterministic(self):
        a, ta = make_problem(17)
        b, tb = make_problem(17)
        self.assertEqual(a, b)
        self.assertEqual(ta, tb)

    def test_prior_never_discloses_success(self):
        problem, _ = make_problem(5)
        trial = run_trial(problem, 24, 99, label="A_cold")
        prior = prior_from_trial(trial)
        self.assertTrue(all(v["status"] == "VERIFIED_FAIL" for v in prior.values()))

    def test_budget_is_bounded(self):
        problem, _ = make_problem(6)
        trial = run_trial(problem, 5, 101)
        self.assertLessEqual(trial["evaluated"], 5)

    def test_suite_schema_and_repeatability(self):
        a = run_suite(n=5, seed=1234)
        b = run_suite(n=5, seed=1234)
        self.assertEqual(a, b)
        self.assertEqual(a["experiment_id"], "EXP-BS-FUN-01")
        self.assertEqual(len(a["runs"]), 5)


if __name__ == "__main__":
    unittest.main()
