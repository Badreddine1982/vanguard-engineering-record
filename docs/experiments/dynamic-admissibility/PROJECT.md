# PRJ-DYNAMIC-ADMISSIBILITY-001 — Dynamic Admissibility and State Transitions

- **Project ID:** PRJ-DYNAMIC-ADMISSIBILITY-001
- **Version:** 0.3.3 (research/evidence + transfer reconciliation)
- **Type:** Mathematical / AI-systems research
- **Status:** INCUBATOR — EXP-001/002 ARTIFACTS PRESENT IN LIBRARY — EXP-003 13/13 TOY CHECKS PASS LOCALLY; FILE TRANSFER PENDING — UNIFIED LAW UNPROVEN — NOT ADOPTED
- **Last reconciled:** 2026-10-16
- **Provenance:** Research discussion on admissibility, MCTS-like exploration, representation fold/unfold, time-dependent transition behavior, and distributed dormant capabilities; tests are isolated and reproducible using Python 3 standard library only.

## Technical Definition
Independent research project studying whether a structured admissibility-aware transition relation can constrain valid evolution while preserving proposal freedom, distributed capabilities, and derived fold/unfold dynamics—without requiring a fixed list of semantic coordinates or separate authority rules inside every node.

## Research Question
Can one structured transition law separate proposal preference, admissibility, dynamic viability, representation relations, capability existence, activation authorization, and validity—and derive operational outcomes without allowing search preference to override mathematical constraints?

## Candidate Principles — Hypotheses, Not Laws
1. MCTS/UCT may propose and explore transitions but does not define their admissibility.
2. Validity is independent of proposal preference.
3. Capability existence, activation, and validity are distinct.
4. Fold/unfold are representation-level transitions, not automatic changes in truth or authority.
5. Time/horizon can be a genuine dynamic variable where the modeled system requires it.
6. Unknown admissibility must neither grant activation nor be misreported as proven impossibility.
7. Distributed capabilities may remain dormant until a governed activation transition; this is a toy interface property, not yet a neural-network result.
8. A shared transition interface is not proof of one universal mathematical law.

## Evidence State
- **EXP-001:** re-run on 2026-10-15; 6/6 constructed cases passed. Deterministic utility ranking, not MCTS/UCT; outcome labels are partly hand-authored conditions. Source and result are separately present in the Library.
- **EXP-002:** re-run on 2026-10-15; 2/2 constructed indistinguishability checks passed. A bare binary admissibility graph lacks information needed to distinguish some operational modes. Protocol, source and result are separately present in the Library.
- **EXP-003:** re-run locally on 2026-10-15; 13/13 constructed interface checks passed using numeric/risk and symbolic/evidence partial-order adapters. Includes relabeling invariance, activation separation, failed effective-transition revalidation, UNKNOWN handling, and preservation of equally preferred branches without identifier-based tie-breaking. It remains a deterministic toy kernel, not MCTS/UCT. **EXP-003 source/result and associated contract/roadmap were not transferred into the Library in this operation due to the upload quota; see `TRANSFER-RESUME-001.md`; the refreshed closure package is v0.3.3.**
- **Not verified:** formal generality; adapter soundness; dimension/representation independence beyond bounded relabeling; minimality; temporal dynamics in a real evolving system; empirical utility; external validity.
- **Architecture adoption:** NOT ADOPTED.

## Current Library Transfer State
A fresh Library listing returned 22 files with no pagination cursor or warnings. Read-back verified the current project/README, EXP-003 protocol and result, structured transition contract, proof roadmap, transfer-resume record, audit 002, and registry event 003. The EXP-003 source and results are present in the current Library baseline; the experiment remains a 13/13 deterministic toy check, not a proof.

The final closure artifacts `REGISTRY-EVENT-004.md`, `LIBRARY-INTAKE-AUDIT-003.md`, regenerated `PACKAGE-MANIFEST-SHA256.txt`, and `Dynamic-Admissibility-Project-Package-v0.3.3.zip` were prepared locally. Their upload attempt was blocked by the service throttle on 2026-10-16. They are not yet confirmed in the Library. The transfer remains OPEN until upload and read-back verification of all four artifacts.

## Relations
Conceptually related to `/VERITAS-AIXI/Experiments/EXP-001_MCTS-Fold-Seed-Unfold/` and other MCTS/Fold/Unfold records. Relation does not imply dependency, merge, shared implementation, or adoption. No core project has been modified.

## Next Gate
Resume file-level transfer after the service permits uploads and verify each exact path. Then review the structured contract and proof roadmap: formalize definitions and assumptions, prove kernel safety conditionally on sound adapters, specify unknown-state and dynamic-step guarantees, define fold/unfold preservation, separate safety from liveness/fair exploration, and test against additional independent representations. Actual MCTS/UCT integration is a later experiment; no result automatically promotes the project beyond incubator status.
