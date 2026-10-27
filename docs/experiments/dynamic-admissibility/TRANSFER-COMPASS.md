# Dynamic Admissibility v0.3.3 — Transfer Compass

- **Transfer ID:** `SKY-A-DA-XFER-20261027-001`
- **Source:** Library path `/SKY-A/PRJ-DYNAMIC-ADMISSIBILITY-001/`
- **Baseline package:** `Dynamic-Admissibility-Project-Package-v0.3.3.zip`
- **Package SHA-256:** `f8aaa2afb46de038790140f9edc26e8f9a569559d0c0a012e6ee1ab497180fd1`
- **Destination repository:** `Badreddine1982/vanguard-engineering-record`
- **Working branch:** `transfer/dynamic-admissibility-v0.3.3`
- **Status:** `SOURCE RECONCILED — COMPASS ONLY; PROJECT FILES NOT YET TRANSFERRED`

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
- **Three current-root files differ from the package:**
  - `PROJECT.md` — current-root SHA-256: `a80d6d266cdda7a8ca5e6302583d17bdff82679ee69339be962e12182e3a7d9d`
  - `README.md` — current-root SHA-256: `3bce054baae9694a028ca107ec863f169ac698ab7a568187ce5616127e0eb06c`
  - `TRANSFER-RESUME-001.md` — current-root SHA-256: `df0f506683289add2158f09fd8628c527da13b6fca3f1ec3f9d6b191fddfef91`
- **Two current-root records are newer additions not contained in v0.3.3:**
  - `LIBRARY-INTAKE-AUDIT-004.md` — SHA-256: `e8eb5904796d02fd238e7285b1d9563bede228739820c1dfcf5ca16fb893df56`
  - `REGISTRY-EVENT-005.md` — SHA-256: `f48668e00b137fcb12f69e7d57fb8fa49a1806e87c9456bb62696c45977b602d`
- **No package-only payload files remain:** every non-manifest file in the package has a corresponding current-root file.
- The package manifest itself is intact, but its hashes describe the v0.3.3 package contents; they do not automatically describe later current-root revisions.

**Selection rule:** use the 19 exact-matching current-root files as verified byte-identical sources; review and use the current-root versions of the three differing files; include the two newer records as separate chronology/evidence. Do not overwrite current files with older package copies.

## File-level transfer ledger

| Artifact group | Intended repository path | Status | Notes |
|---|---|---|---|
| Project definition and README | `docs/experiments/dynamic-admissibility/` | SOURCE SELECTED AFTER REVIEW | Use current-root versions; preserve incubator / not-adopted state. |
| EXP-001 to EXP-003 protocols and results | `docs/experiments/dynamic-admissibility/` | SOURCE RECONCILED | Keep exact source/result pairing and toy-check limitations. |
| Proof roadmap, kernel-safety lemma, transition contract | `docs/experiments/dynamic-admissibility/` | SOURCE RECONCILED | Candidate research artifacts only; not authoritative adoption. |
| Registry events and intake audits | `docs/experiments/dynamic-admissibility/records/` | SOURCE RECONCILED | Include audit 004 and event 005; preserve chronology. |
| Experiment source files | `experiments/dynamic-admissibility/` | SOURCE RECONCILED | Transfer after documentation and destination comparison. |
| v0.3.3 ZIP and SHA manifest | `artifacts/dynamic-admissibility/` or documented release artifact | DECISION PENDING | Decide whether the ZIP is needed in-repo; avoid redundant copies if individual files are committed. |
| Legacy packages and old transfer-resume record | No active destination by default | ARCHIVED IN LIBRARY | Retain for provenance; do not reintroduce as the current baseline. |

## Transfer gates

1. Compare destination paths and existing content before adding files.
2. Transfer documentation and this ledger before experiment source code.
3. Record each committed file, selected source path/hash, destination path, and commit SHA.
4. Verify destination read-back and recompute source-file hashes for the transferred baseline.
5. Keep the Library source intact until destination verification is complete.
6. Only after verified transfer, record a concise retirement trace in the Library; do not delete the protected Library governance law.
7. Transfer completion does not imply experiment verification, confirmation, or adoption.

## Current boundary

Only this transfer compass has been added to the working branch. No Dynamic Admissibility project file or executable source has been committed yet. The Library source remains intact.
