# EXP-BS-FUN-01 — Black Swan / Fold–Unfold / Nano-MCTS

- **Version:** 0.1.0
- **Record date:** 2026-10-28 (Africa/Algiers, UTC+01:00)
- **Class:** Independent research model + synthetic demonstrator
- **Status:** EXECUTED_SYNTHETIC_DEMONSTRATOR_NOT_VALIDATED
- **Adoption:** NOT ADOPTED
- **Core changes:** None. EULER, Fold/Unfold, and VERITAS-AIXI remain independent.

## 1. Technical definition

This experiment tests whether a bounded search loop combining structural folding, selective unfolding, Nano-MCTS-style candidate selection, bounded novelty, prior research evidence, and independent verification can improve useful search under a fixed per-trial evaluation budget without uncontrolled branch growth.

Black Swan is used as a search-space design principle, not as a claim that rare events can be predicted. The system should preserve a bounded route for unfamiliar but structurally admissible candidates and avoid closing the search space merely because current heuristics assign a low prior score.

**Central hypothesis:** At equal per-trial candidate-evaluation budget, an informed run receiving a traceable research file of verified failures and structural evidence—but no direct disclosure of the target—can improve verified discovery or efficiency relative to a fresh run while keeping representation compact and the loop bounded.

This remains a hypothesis; the synthetic run is preliminary evidence about the toy mechanism only.

## 2. Scope and boundaries

**In scope:** bounded candidate search; compact node representation; selective Fold/Unfold; bounded novelty; evidence-informed repeat trial; independent verifier boundary; cold/informed/fresh-control comparison; metrics and reproducibility.

**Out of scope:** full AIXI or full MCTS implementation; prediction of actual Black Swan events; changes to EULER, Fold/Unfold, or VERITAS-AIXI core; treating a synthetic planted-target check as mathematical proof; automatic architectural adoption.

## 3. Architecture

```text
Large problem -> FOLD -> compact structural seed + provenance
                         |
                  Nano-MCTS selector <--- prior Research File
                         |
                bounded known/novel branches
                         |
                      UNFOLD
                         |
                   local search
                         |
                 independent verifier
                    /           \
             verified fail   verified pass
                    |             |
             failure evidence   evidence record
                    \             /
                    bounded retain / compress / dormant / prune
                                  |
                                RE-FOLD
                                  |
                               bounded LOOP
```

- **BSS:** preserves unknowns/anomalies; does not certify truth.
- **Fold:** compresses active representation while preserving provenance, dependencies, evidence state, and a re-entry path. Semantic losslessness is not assumed.
- **Unfold:** expands only selected regions.
- **Nano-MCTS (research label):** bounded hierarchical selection, not assumed to be a proven MCTS implementation.
- **Novelty:** bounded selection influence, never a truth signal or unlimited branch generator.
- **VERITAS-AIXI-derived logic:** may inform selection/evidence bookkeeping in a later isolated revision; this prototype does not implement AIXI.
- **Verifier:** evaluates correctness independently from search scores.
- **Research File:** preserves explored branches, verified failures, costs, provenance, and uncertainty; it must not leak the answer into a discovery trial.

## 4. Node-retention contract

Record fields where applicable:
`node_id, parent_id, branch_id, representation, provenance, dependencies, evidence_refs, verification_status, uncertainty, novelty, estimated_value, cost, failure_signature, revisit_condition, lifecycle_state`.

Allowed actions:
- `KEEP_ACTIVE`: worth expanding now within budget.
- `FOLD_COMPRESS`: preserve a compact summary and re-entry key.
- `DORMANT`: retain with an explicit revisit trigger.
- `ARCHIVE`: retain a complete audit record outside active search.
- `UNFOLD`: recover detail for a selected branch.
- `PRUNE_FROM_ACTIVE_SET`: stop spending budget on contradicted/redundant/dominated/over-budget branches; do not delete evidence.
- `RETAIN_FAILURE_CONSTRAINT`: preserve why a path failed.

Candidate retention features to test—not a validated scoring law—include verified evidence and provenance, structural connectivity, novelty, information gain, redundancy/dominance, expansion cost, downstream reuse, useful failure constraints, and explicit revisit conditions. The experiment must discover whether these features help rather than assume weights in advance.

## 5. Loop invariants

1. Search != Verification != Adoption.
2. Search score, novelty, probability, and selection preference are not proof.
3. Every expansion consumes finite budget; every loop has a stop condition.
4. Novelty remains inside a budget and structural admissibility boundary.
5. Fold cannot silently erase provenance, dependencies, failures, contradictions, or re-entry capability.
6. VERIFIED_FAIL differs from UNTESTED.
7. Trial B's prior must not directly reveal the target; this prototype carries forward verified failures only.
8. Results must be reproducible from code, parameters, seed, and output.
9. No result automatically modifies a parent project's core or grants adoption.

## 6. Experimental design

- **Trial A — Cold:** no prior research file; fixed evaluation budget.
- **Trial B — Informed:** receives Trial A's verified-failure trace only. Successful candidate IDs are excluded from the prior.
- **Fresh control:** same per-trial budget, no prior, separate deterministic random stream.

This is a synthetic proof-of-mechanism, not a faithful MCTS simulation. A ranked candidate list uses heuristic score, novelty, and bounded jitter. A synthetic verifier marks exactly one planted candidate per instance as correct.

Recorded parameters: 40 problems; 24 candidates/problem; budget 8 per condition; master seed 20261028; novelty weight 0.22; Python standard library; one synthetic verification-cost unit per candidate.

Metrics: discovery rate, mean evaluations until stop, unique candidates evaluated, informed-vs-fresh success difference, prior leakage check, repeatability, artifact hashes. A full validation must additionally measure active-node count, folded representation size, semantic preservation, Fold/Unfold cost, runtime, repeated-failure rate, novelty yield, verifier cost, and confidence intervals across independent seeds.

## 7. Results

| Condition | Problems | Discoveries | Rate | Mean evaluations until stop |
|---|---:|---:|---:|---:|
| Trial A — Cold | 40 | 15 | 37.5% | 6.40 |
| Trial B — Informed | 40 | 25 | 62.5% | 4.80 |
| Fresh equal-budget control | 40 | 15 | 37.5% | 6.725 |

In this fixed synthetic setup, informed search found 10 more targets than the fresh control (+25 percentage points).

**Interpretation limit:** this does not establish that real Nano-MCTS, AIXI, Fold/Unfold, EULER, or a Black Swan system improves similarly. The generator is simple, the target is planted, and only one fixed-seed suite is recorded. The prior comes from the same instance's earlier failed candidates. This is a runnable sanity check, not a general performance result. Independent implementations, multiple seed suites, non-synthetic tasks, paired analysis, and a real structural Fold/Unfold benchmark are required.

## 8. Acceptance gates

- **G0 Provenance:** PASS for this synthetic run.
- **G1 Bounded loop execution:** PASS for this synthetic run.
- **G2 No direct target leakage:** PASS by implementation rule; automated tests included.
- **G3 Independent correctness:** PASS only within the toy verifier; real-domain verification NOT TESTED.
- **G4 Structural Fold/Unfold preservation:** NOT TESTED; not implemented in this prototype.
- **G5 Generalization:** NOT TESTED.
- **G6 Independent review:** PENDING.
- **G7 Adoption:** NOT APPROVED.

Overall: **PRELIMINARY / NOT VALIDATED / NOT ADOPTED**.

## 9. Reproduction

```bash
python exp_bs_fun_01.py --out results.json
python -m unittest -v
python -m py_compile exp_bs_fun_01.py test_exp_bs_fun_01.py
sha256sum README.md exp_bs_fun_01.py test_exp_bs_fun_01.py results.json
```

## 10. Prior work and separation

- `BSS-RECOVERY-001`: partial recovered concept record, not a complete original package.
- `TRIAD-INTERACTION-HYPOTHESIS-001`: proposed separation of Black Swan unknown-space, EULER reasoning, and Zettelkasten relation integrity; untested/not adopted.
- VERITAS-AIXI's earlier Fold/Seed/Unfold experiment has a newer revision marked INCONCLUSIVE because its search-quality gate failed. Do not generalize its earlier proof-of-concept wording.
- EULER remains independent. No dependency or integration is established here.

## 11. Change control and conclusion

This is an isolated research artifact. Future revisions preserve raw outputs, parameters, code hashes, and reasons for protocol changes. Proposal, implementation, execution, verification, review, and adoption remain separate states.

A bounded evidence-informed demonstrator was executed on 40 synthetic problems. It improved over the fresh control in this particular run, but the result is narrow and benchmark-specific. The hypothesis remains OPEN until actual reversible node folding, semantic preservation, stronger baselines, independent seeds, and external review are tested.
