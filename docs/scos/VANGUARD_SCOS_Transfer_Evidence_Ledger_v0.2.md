# VANGUARD–SCOS Transfer Evidence Ledger — 2026-10-19

- **Record ID:** VSC-TRANSFER-EVIDENCE-001
- **Revision:** 0.2
- **Intake status:** `SOURCE IDENTITY CAPTURED / T0 ISOLATED REPRODUCTION PASS (LIMITED) / TRANSFER OPEN / T1–T12 NOT RUN / NOT ADOPTED`
- **Authority:** Evidence record only; does not change Master State or grant adoption.

## Source identity
- Library path: `/VANGUARD-SCOS-INTAKE/Epistemology_V9.0_Source.docx`
- Bytes: `22423`
- SHA-256: `e3087ac7a077da0bd3ef924838f177496b3f2b44025b7da981dff481534ce316`
- Container check: DOCX ZIP and `word/document.xml` parsed successfully.

## Existing package baseline
- Path: `/VANGUARD-SCOS-INTAKE/VANGUARD_SCOS_Intake_Completion_Package_v0.2.zip`
- Bytes: `6266`
- SHA-256: `9d41397fbfd94c3f94f8f33d51131e844335f7a31c278fb217170a705300c6f2`
- ZIP integrity: pass. Members: `Epistemology_V9_Static_Intake_Audit_v0.1.md`, `VANGUARD_SCOS_Component_Intake_Register_v0.2.md`, `VANGUARD_SCOS_Acceptance_Test_Execution_Ledger_v0.1.md`.
- Finding: existing package does not contain the source DOCX or test script/results; it is an intake-record package, not a source-complete execution package.

## Evidence produced in this continuation
- `VSC_T0_Smoke_Test_Results_v0.1.json`: T0 limited pass; source identity, container integrity, and static markers.
- `run_vscos_t0.py`: deterministic read-only test script.
- Repeatability: two runs produced identical result JSON SHA-256 `bd5973894a1a5374359e5f9a5060fb765c240c8961119aedc94dbf3b4009978f`.
- Scope: no source import or execution; runtime tests T1–T12 remain NOT RUN.

## Transfer boundary
Local package creation and Library upload/read-back are distinct operations. This ledger must not be treated as proof that newly generated artifacts have been uploaded. Transfer closure requires successful Library writes and read-back of exact paths, sizes, and hashes.

## Correction and independent extraction evidence — 2026-10-28
- Original v0.3 package SHA-256: `fa72060038021f453f750ae17081b9d6c7040dc2e9024be907eaaee681f2df9c` (35,471 bytes); ZIP integrity passed, 9 members.
- Reproducible defect: `run_vscos_t0.py` hard-coded `VANGUARD_SCOS_Intake_Completion_Package_v0.2.zip`, which was absent from the v0.3 archive. This invalidated the claim that T0 was self-contained; it did not erase the earlier environment-specific result.
- Corrected release candidate: `VANGUARD_SCOS_Intake_Completion_Package_v0.3.1.zip`. T0 now anchors paths to the script directory and verifies required payloads against the included SHA-256 manifest; it does not open or require v0.2.
- Verification procedure: extracted v0.3.1 into a clean directory; confirmed v0.2 was absent; ran `python run_vscos_t0.py` twice; both exit codes were 0; both overall statuses were PASS; output JSON SHA-256 was identical across runs.
- Package ZIP integrity and all manifest-listed hashes were verified after final build. See `VSC_T0_Smoke_Test_Results_v0.2.json` and `VANGUARD_SCOS_PACKAGE_SHA256_MANIFEST_v0.2.txt`.
- T1–T12 remain `NOT RUN`; submitted AGI source remains unimported/unexecuted.
- Library upload/read-back and GitHub transfer are separate gates. This record alone does not claim either has completed.
