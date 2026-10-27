# PRJ-DYNAMIC-ADMISSIBILITY-001

Independent incubator project on admissibility-aware state transitions. No universal law is claimed or adopted.

## Start here
- `PROJECT.md` — current state and evidence boundary
- `STRUCTURED-TRANSITION-CONTRACT-001.md` — candidate contract, not a permanent law
- `PROOF-ROADMAP-001.md` — staged formalization/proof obligations
- `LIBRARY-INTAKE-AUDIT-003.md` — latest transfer reconciliation (prepared locally; upload pending)

## Experiments
- EXP-001 — `python experiment.py` → `EXP-001-RESULTS.json`
- EXP-002 — `python experiment_exp002.py` → `EXP-002-RESULTS.json`
- EXP-003 — `python experiment_exp003.py` → `EXP-003-RESULTS.json`

All programs use Python 3 standard library only. These are deterministic toy checks, not MCTS/UCT implementations, formal proofs, or safety certifications.

Recorded results: EXP-001 6/6; EXP-002 2/2; EXP-003 13/13. Passing means only that the specified constructed checks pass. Adapter soundness, universal/dimension-independent validity, real temporal dynamics, and external validity remain unverified.

## Transfer note
The Library baseline was read back and listed as 22 files. Final closure artifacts (registry event 004, intake audit 003, refreshed SHA-256 manifest, and package v0.3.3) are prepared locally but were blocked by the Library upload throttle on 2026-10-16. See `TRANSFER-RESUME-001.md`; transfer is not yet closed.
