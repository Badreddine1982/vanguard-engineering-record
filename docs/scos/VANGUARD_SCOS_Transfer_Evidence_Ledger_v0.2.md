# VANGUARD–SCOS Transfer Evidence Ledger — v0.2

- Record ID: `VSC-TRANSFER-EVIDENCE-001`
- Updated: 2026-10-28
- State: `SOURCE IDENTITY CAPTURED / T0 ISOLATED REPRODUCTION PASS (LIMITED) / TRANSFER REVIEW OPEN / T1–T12 NOT RUN / NOT ADOPTED`
- Authority: evidence record only; no adoption authority.

## Source identity

- Library source: `/VANGUARD-SCOS-INTAKE/Epistemology_V9.0_Source.docx`
- Bytes: 22,423
- SHA-256: `e3087ac7a077da0bd3ef924838f177496b3f2b44025b7da981dff481534ce316`

## v0.3 defect

The original v0.3 package was a valid ZIP with 9 entries and SHA-256 `fa72060038021f453f750ae17081b9d6c7040dc2e9024be907eaaee681f2df9c`. However, its T0 script referenced `VANGUARD_SCOS_Intake_Completion_Package_v0.2.zip`, which was not present in the archive. This reproduced failure prevented treating v0.3 as self-contained.

## Corrected v0.3.1 evidence

- Package path: `/VANGUARD-SCOS-INTAKE/VANGUARD_SCOS_Intake_Completion_Package_v0.3.1.zip`
- Bytes: 37,215
- SHA-256: `917583cd5b643107b7e14f2f39539f58637fa43bd89b7a5a81f4ace3fb5cd5a0`
- ZIP integrity: PASS; 9 entries.
- Manifest: all six listed payload hashes recomputed and matched.
- Isolated test: clean extraction; v0.2 absent; T0 executed twice.
- Exit codes: 0 and 0.
- Result JSON SHA-256 on both runs: `ba89c75eec4acc128449955369e43eb428f5e7ef16daec606fc061e9039b0886`.
- T0 overall: PASS, limited to identity/container/manifest/static-marker checks.

## Remaining boundaries

- T1–T12: `NOT RUN`.
- Submitted AGI source: not imported or executed.
- GitHub transfer: branch-level evidence is not equivalent to PR merge.
- Library transfer: package upload succeeded; read-back verification remains required.
- No source deletion, Library retirement, core integration, confirmation, or adoption is authorized by this record.
