# Dynamic Admissibility v0.3.3 — Transfer Compass

- **Transfer ID:** `SKY-A-DA-XFER-20261027-001`
- **Source:** Library path `/SKY-A/PRJ-DYNAMIC-ADMISSIBILITY-001/`
- **Baseline package:** `Dynamic-Admissibility-Project-Package-v0.3.3.zip`
- **Package SHA-256:** `f8aaa2afb46de038790140f9edc26e8f9a569559d0c0a012e6ee1ab497180fd1`
- **Destination repository:** `Badreddine1982/vanguard-engineering-record`
- **Working branch:** `transfer/dynamic-admissibility-v0.3.3`
- **Status:** `PREPARED — COMPASS ONLY; PROJECT FILES NOT YET TRANSFERRED`

## Why this destination

This repository is the engineering record for VANGUARD experiments, evidence, failures, and verified decisions. Dynamic Admissibility remains an experimental incubator, not an adopted VANGUARD law or runtime component. The candidate contract and experiment results must remain clearly labeled as experimental evidence; this transfer does not promote them into authoritative contracts.

## Source integrity check

Read-back of the Library package on 2026-10-27 confirmed:
- ZIP integrity test passed.
- 23 archive entries.
- 22 SHA-256 manifest records recomputed successfully; 22/22 matched.
- The package SHA-256 matches the recorded baseline above.

The Library currently retains the active v0.3.3 package at the project root. Historical packages and the old resume record were moved to archive paths; they were not deleted. The internal Library governance law is outside this transfer.

## File-level transfer ledger

| Artifact group | Intended repository path | Status | Notes |
|---|---|---|---|
| Project definition and README | `docs/experiments/dynamic-admissibility/` | NOT TRANSFERRED | Documentation-first; preserve incubator / not-adopted state. |
| EXP-001 to EXP-003 protocols and results | `docs/experiments/dynamic-admissibility/` | NOT TRANSFERRED | Retain exact source/result pairing and toy-check limitations. |
| Proof roadmap, kernel-safety lemma, transition contract | `docs/experiments/dynamic-admissibility/` | NOT TRANSFERRED | Candidate research artifacts only; not authoritative adoption. |
| Registry events and intake audits | `docs/experiments/dynamic-admissibility/records/` | NOT TRANSFERRED | Preserve provenance and chronological history. |
| Experiment source files | `experiments/dynamic-admissibility/` | NOT TRANSFERRED | Transfer after documentation and file-level comparison. |
| v0.3.3 ZIP and SHA manifest | `artifacts/dynamic-admissibility/` or documented release artifact | NOT TRANSFERRED | Decide whether the ZIP is needed in-repo; avoid redundant copies if individual files are committed. |
| Legacy packages and old transfer-resume record | No active destination by default | ARCHIVED IN LIBRARY | Retain for provenance; do not reintroduce as the current baseline. |

## Transfer gates

1. Compare destination paths and existing content before adding files.
2. Transfer documentation and this ledger before experiment source code.
3. Record each committed file, source path, source version/hash where available, destination path, and commit SHA.
4. Verify destination read-back and recompute source-file hashes for the transferred baseline.
5. Keep the Library source intact until destination verification is complete.
6. Only after verified transfer, record a concise retirement trace in the Library; do not delete the protected Library governance law.
7. Transfer completion does not imply experiment verification, confirmation, or adoption.

## Current boundary

Only this transfer compass has been added to the working branch. No Dynamic Admissibility project file or executable source has been committed yet.
