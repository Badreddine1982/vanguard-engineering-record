# KMA Transfer Compass — KMA-TRANSFER-001

- **Project:** KMA — Knowledge Memory Architecture
- **Version:** 0.1
- **Updated:** 2026-10-27
- **State:** FIRST DOCUMENT COPIED TO GITHUB; EXACT READ-BACK VERIFIED
- **Adoption:** NOT ADOPTED. The source remains an architectural draft; this transfer does not approve implementation or adoption.
- **Library source:** `Knowledge_Memory_Architecture_v0.1.md` — Library file ID `libfile_b792256cd6dc8191b521e0d6510d29a7`.
- **GitHub destination:** `Badreddine1982/vanguard-engineering-record/docs/kma/Knowledge_Memory_Architecture_v0.1.md`, branch `main`.
- **Transfer commit:** `f4ebb17b5d48dfb28eda9a387ce87135f4465c6c`.
- **GitHub blob SHA (read-back):** `6c331b9e59944ab77e02787876976b32075371e6`.
- **Read-back check:** PASS — retrieved content exactly matches the Library source text available for this operation.
- **Source handling:** Copy only. The Library source has not been deleted or modified.

## Repository roles (working convention)

| Repository | KMA-related content |
|---|---|
| `vanguard-engineering-record` | Architecture drafts, provenance, decisions, evidence, transfer compass and status history |
| `vanguard-contracts` | Formal KMA record schemas, interfaces, lifecycle and compatibility contracts, once identified and reviewed |
| `vanguard-runtime` | Executable storage/retrieval/router implementations and tests, after the contract boundary is clear |
| `vanguard-ai` | System-level integration and entry points, only where an actual integration reference is needed |

These roles are practical routing guidance, not a claim that all such components already exist.

## File-level register

| Source artifact | Destination | Status | Notes |
|---|---|---|---|
| `Knowledge_Memory_Architecture_v0.1.md` | `vanguard-engineering-record/docs/kma/Knowledge_Memory_Architecture_v0.1.md` | **TRANSFERRED — READ-BACK VERIFIED** | Exact text comparison passed. Source status remains `ARCHITECTURAL DRAFT`. |
| Exact KMA record schemas | `vanguard-contracts/contracts/kma/` (proposed) | **NOT LOCATED / PENDING INVENTORY** | Do not invent or derive a canonical schema from the draft's field list without review. |
| Retrieval scoring, consolidation, retention thresholds, promotion evidence, indexing, archive representation | To be assigned after source inventory | **OPEN DESIGN GATES** | These are explicitly listed as pre-implementation design gates in v0.1. |
| KMA implementation and tests | `vanguard-runtime` (proposed) | **NOT TRANSFERRED** | Documentation-first; do not imply code exists or is tested. |

## Resume procedure

1. Read this compass and the transferred architecture draft first.
2. Inventory all other Library documents referring to KMA, Storage Map, memory routing, evidence retention, or promotion lifecycle; record exact source IDs and paths.
3. Inspect the current `main` trees before selecting destinations. Keep architecture/evidence records in engineering-record, formal interfaces in contracts, and executable code/tests in runtime.
4. For each copied file, record source identity, destination path, branch, commit SHA, GitHub blob SHA, and exact read-back comparison result.
5. Use `TRANSFERRED — READ-BACK VERIFIED` only after the destination is fetched and compared. This status verifies copying, not semantic correctness, testing, integration, or adoption.
6. Preserve the Library source as the reference copy until a separate lifecycle decision explicitly changes that policy.

## Current boundary

Only the architecture draft listed above has been copied in this KMA pass. No KMA code, canonical schema, or integration has been transferred or validated by this operation.
