# Dynamic Admissibility v0.3.3 — Transfer Compass

- **Transfer ID:** `SKY-A-DA-XFER-20261027-001`
- **Source:** Library path `/SKY-A/PRJ-DYNAMIC-ADMISSIBILITY-001/`
- **Baseline package:** `Dynamic-Admissibility-Project-Package-v0.3.3.zip`
- **Package SHA-256:** `f8aaa2afb46de038790140f9edc26e8f9a569559d0c0a012e6ee1ab497180fd1`
- **Destination repository:** `Badreddine1982/vanguard-engineering-record`
- **Working branch:** `transfer/dynamic-admissibility-v0.3.3`
- **Status:** `BRANCH TRANSFER READ-BACK VERIFIED — DRAFT PR #2 OPEN; NOT MERGED`

## Why this destination

This repository is the engineering record for VANGUARD experiments, evidence, failures, and verified decisions. Dynamic Admissibility remains an experimental incubator, not an adopted VANGUARD law or runtime component. Candidate contracts and experiment results must remain clearly labeled as experimental evidence; this transfer does not promote them into authoritative contracts.

## Package integrity check

Read-back of the Library package on 2026-10-27 confirmed:
- ZIP integrity test passed.
- 23 archive entries.
- 22 SHA-256 manifest records recomputed successfully; 22/22 matched.
- The package SHA-256 matches the recorded baseline above.

## Source-to-package reconciliation

A byte-level comparison was completed for all 22 payload files listed in the v0.3.3 manifest against the current Library project root.

- **19/22 payload files match exactly.**
- **Three current-root files differ from the package:** `PROJECT.md`, `README.md`, and `TRANSFER-RESUME-001.md`.
- **Two current-root records are later additions not contained in v0.3.3:** `LIBRARY-INTAKE-AUDIT-004.md` and `REGISTRY-EVENT-005.md`.
- **No package-only payload files remain:** every non-manifest file in the package has a corresponding current-root file.

The three differences were content-reviewed, not treated as evidence that the root copy is newer:
- Package `PROJECT.md` declares version **0.3.3**; the differing current-root copy declares **0.3.2**. The package version is the newer project-definition baseline.
- Both README and transfer-resume variants contain pending-transfer wording that is superseded by the later closure records.
- `LIBRARY-INTAKE-AUDIT-004.md` and `REGISTRY-EVENT-005.md` explicitly confirm that Library transfer closed on 2026-10-17 and that package integrity passed. They govern the later operational status.
- The package manifest is intact; its hashes describe the v0.3.3 archive and do not automatically describe later files.

**Selection rule:** preserve v0.3.3 package contents as the versioned baseline; add audit 004 and registry event 005 as later closure evidence; do not replace the package's versioned files with differing current-root copies merely because their path names match. Keep the historical pending-transfer wording as provenance, and make the later closure state clear through the subsequent records.

## File-level transfer ledger

| Artifact group | Intended repository path | Status | Notes |
|---|---|---|---|
| Project definition and README | `docs/experiments/dynamic-admissibility/` | SOURCE SELECTED | Use v0.3.3 package versions; cross-reference later closure records. |
| EXP-001 to EXP-003 protocols and results | `docs/experiments/dynamic-admissibility/` | SOURCE RECONCILED | Keep exact source/result pairing and toy-check limitations. |
| Proof roadmap, kernel-safety lemma, transition contract | `docs/experiments/dynamic-admissibility/` | SOURCE RECONCILED | Candidate research artifacts only; not authoritative adoption. |
| Registry events and intake audits | `docs/experiments/dynamic-admissibility/records/` | SOURCE RECONCILED | Include audit 004 and event 005; preserve chronology. |
| Experiment source files | `experiments/dynamic-admissibility/` | SOURCE RECONCILED | Transfer after documentation and destination comparison. |
| v0.3.3 ZIP and SHA manifest | `artifacts/dynamic-admissibility/` or documented release artifact | DECISION PENDING | Avoid a redundant binary copy if individual files and hashes are recorded. |
| Legacy packages and old transfer-resume record | No active destination by default | ARCHIVED IN LIBRARY | Retain for provenance; do not reintroduce as the current baseline. |

## Transfer gates

1. Compare destination paths and existing content before adding files.
2. Transfer documentation and this ledger before experiment source code.
3. Record each committed file, selected source version/hash, destination path, and commit SHA.
4. Verify destination read-back and recompute source-file hashes for the transferred baseline.
5. Keep the Library source intact until destination verification is complete.
6. Only after verified external transfer, record a concise retirement trace in the Library; do not delete the protected Library governance law.
7. Transfer completion does not imply experiment verification, confirmation, or adoption.

## Current boundary

The branch contains 26 transferred payload artifacts: 20 files from the v0.3.3 package baseline, the two later Library closure records, this transfer compass, and all three experiment source files. The additional `GITHUB-TRANSFER-VERIFY-001.md` record makes **27 changed files in draft PR #2**. The experiment sources were committed after the documentation-first stage.

Direct destination read-back matched all 17 package documentation files sourced from Library records and all three experiment source files; the two later closure records also matched their Library versions. The package-only versions of `PROJECT.md`, `README.md`, and `TRANSFER-RESUME-001.md` were additionally checked by comparing their Git blob SHAs against the exact extracted package bytes. The compass itself was read back from the destination.

Local reproduction from the hash-verified v0.3.3 package completed successfully:
- EXP-001: 6/6 constructed checks passed.
- EXP-002: 2/2 constructed checks passed.
- EXP-003: 13/13 constructed interface checks passed.

These are toy checks only; they do not prove the candidate law, adapter soundness, actual MCTS/UCT integration, or system safety.

**Transfer scope:** the branch-level copy and read-back are verified. Draft pull request #2 is open for review; the changes are not merged into `main`. Internal Library sources remain intact. No Library retirement/deletion operation has been performed, and the protected Library governance law remains outside this transfer.
