#!/usr/bin/env python3
"""EXP-BS-FUN-01 minimal reproducible synthetic demonstrator.

This tests a bounded evidence-informed search loop, not real-world Black Swan
prediction or general MCTS capability. Python standard library only.
"""
import argparse, hashlib, json, random, statistics
from pathlib import Path


def make_problem(seed, width=24):
    rng = random.Random(seed)
    solution = rng.randrange(width)
    branches = []
    for i in range(width):
        branches.append({
            "candidate_id": f"p{seed:03d}-c{i:02d}",
            "branch": f"b{i:02d}",
            "score": round(rng.random(), 6),
            "novelty": round(rng.random(), 6),
            "verified": i == solution,
            "reason": "synthetic independent verifier pass" if i == solution else "synthetic verifier reject",
        })
    return branches, branches[solution]["candidate_id"]


def select_order(candidates, rng, prior=None, novelty_weight=0.22):
    prior = prior or {}
    ranked = []
    for c in candidates:
        state = prior.get(c["candidate_id"], {})
        if state.get("status") == "VERIFIED_PASS":
            bonus = 0.35
        elif state.get("status") == "VERIFIED_FAIL":
            bonus = -0.45
        else:
            bonus = 0.0
        value = c["score"] + novelty_weight*c["novelty"] + bonus + rng.random()*0.08
        ranked.append((value, c))
    ranked.sort(key=lambda item: item[0], reverse=True)
    return [c for _, c in ranked]


def run_trial(problem, budget, seed, prior=None, label="cold"):
    order = select_order(problem, random.Random(seed), prior=prior)
    trace, found = [], None
    for c in order[:budget]:
        status = "VERIFIED_PASS" if c["verified"] else "VERIFIED_FAIL"
        trace.append({"candidate_id": c["candidate_id"], "branch": c["branch"],
                      "status": status, "score": c["score"], "novelty": c["novelty"]})
        if status == "VERIFIED_PASS":
            found = c["candidate_id"]
            break
    return {"label": label, "budget": budget, "evaluated": len(trace),
            "found": found is not None, "solution_id": found, "trace": trace,
            "unique_candidates": len({r["candidate_id"] for r in trace})}


def prior_from_trial(trial):
    # Do not leak successful candidate IDs into the discovery prior.
    return {r["candidate_id"]: {"status": r["status"], "source_trial": trial["label"]}
            for r in trial["trace"] if r["status"] == "VERIFIED_FAIL"}


def run_suite(n=40, width=24, cold_budget=8, informed_budget=8, seed=20261028):
    outcomes = []
    for i in range(n):
        problem, target = make_problem(seed+i, width)
        cold = run_trial(problem, cold_budget, seed+10000+i, label="A_cold")
        prior = prior_from_trial(cold)
        informed = run_trial(problem, informed_budget, seed+20000+i, prior=prior, label="B_informed")
        control = run_trial(problem, informed_budget, seed+30000+i, label="B_control")
        outcomes.append({"problem_id": f"p{seed+i:03d}", "true_solution_id": target,
                         "cold": cold, "informed": informed, "fresh_control": control,
                         "prior_size": len(prior), "prior_contains_solution": target in prior})
    def summary(key):
        trials = [o[key] for o in outcomes]
        return {"trials": len(trials), "successes": sum(t["found"] for t in trials),
                "success_rate": round(sum(t["found"] for t in trials)/len(trials), 4),
                "mean_evaluated_until_stop": round(statistics.mean(t["evaluated"] for t in trials), 4),
                "mean_unique_candidates": round(statistics.mean(t["unique_candidates"] for t in trials), 4)}
    sums = {k: summary(k) for k in ("cold", "informed", "fresh_control")}
    sums["paired_informed_minus_fresh_successes"] = sums["informed"]["successes"]-sums["fresh_control"]["successes"]
    sums["interpretation"] = "Synthetic exploratory result only; no general claim about real MCTS, mathematics, or Black Swan events."
    return {"experiment_id": "EXP-BS-FUN-01", "version": "0.1.0",
            "status": "EXECUTED_SYNTHETIC_DEMONSTRATOR_NOT_VALIDATED",
            "parameters": {"n_problems": n, "width": width, "cold_budget": cold_budget,
                           "informed_budget": informed_budget, "seed": seed,
                           "novelty_weight": 0.22, "language": "Python standard library"},
            "method": "Cold A; informed B receives verified failures only (no pass/target disclosure); equal-budget fresh control.",
            "summary": sums, "runs": outcomes}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=40)
    ap.add_argument("--width", type=int, default=24)
    ap.add_argument("--cold-budget", type=int, default=8)
    ap.add_argument("--informed-budget", type=int, default=8)
    ap.add_argument("--seed", type=int, default=20261028)
    ap.add_argument("--out", default="results.json")
    args = ap.parse_args()
    result = run_suite(args.n, args.width, args.cold_budget, args.informed_budget, args.seed)
    raw = json.dumps(result, indent=2, sort_keys=True)+"\n"
    Path(args.out).write_text(raw, encoding="utf-8")
    print(json.dumps({"experiment_id": result["experiment_id"], "status": result["status"],
                      "summary": result["summary"], "results_path": args.out,
                      "sha256": hashlib.sha256(raw.encode()).hexdigest()}, indent=2))


if __name__ == "__main__":
    main()
