# Dynamic Admissibility v0.3.3 — Transfer Compass

- **Transfer ID:** `SKY-A-DA-XFER-20261027-001`
- **Source:** Library path `/SKY-A/PRJ-DYNAMIC-ADMISSIBILITY-001/`
- **Baseline package:** `Dynamic-Admissibility-Project-Package-v0.3.3.zip`
- **Package SHA-256:** `f8aaa2afb46de038790140f9edc26e8f9a569559d0c0a012e6ee1ab497180fd1`
- **Destination repository:** `Badreddine1982/vanguard-engineering-record`
- **Working branch:** `transfer/dynamic-admissibility-v0.3.3`
- **Status:** `RECONCILIATION REQUIRED — COMPASS ONLY; PROJECT FILES NOT YET TRANSFERRED`

## Why this destination

This repository is the engineering record for VANGUARD experiments, evidence, failures, and verified decisions. Dynamic Admissibility remains an experimental incubator, not an adopted VANGUARD law or runtime component. The candidate contract and experiment results must remain clearly labeled as experimental evidence; this transfer does not promote them into authoritative contracts.

## Package integrity check

Read-back of the Library package on 2026-10-27 confirmed:
- ZIP integrity test passed.
- 23 archive entries.
- 22 SHA-256 manifest records recomputed successfully; 22/22 matched.
- The package SHA-256 matches the recorded baseline above.

This verifies the v0.3.3 archive as an intact historical package. It does **not** prove that it is a complete snapshot of the current project folder.

## Source-to-package reconciliation

A byte-level comparison was made between the extracted v0.3.3 package and current files materialized from the Library project root.

- **Exact matches confirmed:** experiment result files and protocols included in the comparison, the kernel-safety lemma, audits 001–003, proof roadmap, registry events 002–004, structured-transition contract, and the two experiment source files included in the comparison.
- **Current root differs from package:** `PROJECT.md`, `README.md`, and `TRANSFER-RESUME-001.md`. The current root versions must be treated as separate candidate source versions and reviewed before transfer; do not silently replace them with package copies.
- **Current root contains post-package records:** `LIBRARY-INTAKE-AUDIT-004.md` and `REGISTRY-EVENT-005.md`, neither of which is in the v0.3.3 archive.
- **Package files not yet included in the byte-level root comparison:** `EXP-002.md`, `REGISTRY-EVENT-001.md`, and `experiment.py`. These must be compared before the source baseline is finalized.
- The package manifest itself matched the current root manifest as a file, but its recorded hashes describe the archive contents, not automatically every later file in the project root.

Therefore the correct next step is a file-level source ledger based on the current root plus archived history, not blind extraction of v0.3.3 over the project.

## File-level transfer ledger

| Artifact group | Intended repository path | Status | Notes |
|---|---|---|---|
| Project definition and README | `docs/experiments/dynamic-admissibility/` | RECONCILE FIRST | Use the current root versions after comparison; preserve incubator / not-adopted state. |
| EXP-001 to EXP-003 protocols and results | `docs/experiments/dynamic-admissibility/` | RECONCILE FIRST | Retain exact source/result pairing and toy-check limitations. |
| Proof roadmap, kernel-safety lemma, transition contract | `docs/experiments/dynamic-admissibility/` | RECONCILE FIRST | Candidate research artifacts only; not authoritative adoption. |
| Registry events and intake audits | `docs/experiments/dynamic-admissibility/records/` | RECONCILE FIRST | Include post-package records and preserve chronology. |
| Experiment source files | `experiments/dynamic-admissibility/` | RECONCILE FIRST | Transfer after documentation and file-level comparison. |
| v0.3.3 ZIP and SHA manifest | `artifacts/dynamic-admissibility/` or documented release artifact | DECISION PENDING | Decide whether the ZIP is needed in-repo; avoid redundant copies if individual files are committed. |
| Legacy packages and old transfer-resume record | No active destination by default | ARCHIVED IN LIBRARY | Retain for provenance; do not reintroduce as the current baseline. |

## Transfer gates

1. Compare destination paths and existing content before adding files.
2. Complete the file-level source ledger, including all current-root files and package-only/legacy files.
3. Transfer documentation and this ledger before experiment source code.
4. Record each committed file, source path, selected source version/hash where available, destination path, and commit SHA.
5. Verify destination read-back and recompute source-file hashes for the transferred baseline.
6. Keep the Library source intact until destination verification is complete.
7. Only after verified transfer, record a concise retirement trace in the Library; do not delete the protected Library governance law.
8. Transfer completion does not imply experiment verification, confirmation, or adoption.

## Current boundary

Only this transfer compass has been added to the working branch. No Dynamic Admissibility project file or executable source has been committed yet. The Library source remains intact.
