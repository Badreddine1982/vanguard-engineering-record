# VANGUARD–SCOS v0.3.1 — Transfer Compass

- Transfer ID: `VSC-XFER-20261028-001`
- Source: `/VANGUARD-SCOS-INTAKE/`
- Source document: `Epistemology_V9.0_Source.docx`
- Source SHA-256: `e3087ac7a077da0bd3ef924838f177496b3f2b44025b7da981dff481534ce316`
- Corrected package: `VANGUARD_SCOS_Intake_Completion_Package_v0.3.1.zip`
- Package size: 37,215 bytes
- Package SHA-256: `917583cd5b643107b7e14f2f39539f58637fa43bd89b7a5a81f4ace3fb5cd5a0`
- Library destination: `/VANGUARD-SCOS-INTAKE/VANGUARD_SCOS_Intake_Completion_Package_v0.3.1.zip`
- GitHub repository: `Badreddine1982/vanguard-engineering-record`
- Working branch: `transfer/vanguard-scos-v0.3.1`
- State: `PACKAGE BUILT / LIBRARY READ-BACK VERIFIED / T0 ISOLATED PASS / GITHUB EVIDENCE MERGED / BINARY GITHUB PUBLICATION OPEN`

## Defect and correction

The v0.3 T0 script attempted to open `VANGUARD_SCOS_Intake_Completion_Package_v0.2.zip`, which is not included in the v0.3 archive. That dependency made T0 fail from an independent extraction.

v0.3.1 replaces the legacy-package check with required-payload and SHA-256 manifest checks rooted at the script directory. It does not require or open v0.2.

## Verification evidence

- v0.3.1 archive integrity check: PASS; 9 members.
- All manifest-listed payload hashes recomputed and matched.
- Fresh extraction contained no v0.2 archive.
- `python run_vscos_t0.py` executed twice from that extraction; both exit codes were 0 and both overall statuses were PASS.
- Both runs produced result JSON SHA-256: `ba89c75eec4acc128449955369e43eb428f5e7ef16daec606fc061e9039b0886`.
- T0 scope remains limited to source identity, DOCX container/XML integrity, manifest hashes, and deterministic static markers. The submitted AGI source was not imported or executed.

## GitHub artifact boundary

This PR transfers the auditable text records, manifest, T0 result record, and T0 script into GitHub. The binary ZIP v0.3.1 is currently stored in the Library and has been read back byte-for-byte; it is **not included as a binary file in this PR**. Therefore this PR does not claim that the ZIP itself has been published as a GitHub repository/release asset.

## File-level status

| Artifact | State |
|---|---|
| Epistemology V9.0 source DOCX | Preserved unchanged; hash recorded |
| Static audit and acceptance plan | Included as evidence, not adoption |
| Component intake register v0.4 | Included |
| Acceptance execution ledger v0.3 | Included |
| Transfer evidence ledger v0.2 | Included |
| T0 script and v0.2 result JSON | Included; independent repeat passed |
| SHA-256 manifest v0.2 | Included; payload hashes verified |
| T1–T12 | `NOT RUN` |
| Component adoption | `NOT ADOPTED` |

## Transfer gates still open

1. The evidence/documentation PR is merged to `main` (PR #3; merge commit `fbe98f7f5d41e7babd3fdd71a12a4742d0a64a00`).
2. The v0.3.1 ZIP is in the Library and was read back byte-for-byte; size and SHA-256 match the recorded values.
3. The binary ZIP itself is not included in GitHub; publishing it as a GitHub release/repository asset remains open.
4. Keep the older v0.3 package as historical evidence; do not silently overwrite or delete it.
5. Do not mark T1–T12 as passed or promote any component based on this correction.

The protected Library governance law is outside this transfer. Library retirement/deletion is not authorized by this record.
