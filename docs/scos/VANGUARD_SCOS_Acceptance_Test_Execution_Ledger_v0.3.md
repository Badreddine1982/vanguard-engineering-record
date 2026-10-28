# Acceptance Test Execution Ledger — VANGUARD / SCOS Intake

- **Record ID:** LIB-TEST-LEDGER-VSC-001
- **Revision:** 0.3
- **Updated:** 2026-10-28
- **Status:** `T0 ISOLATED REPRODUCTION PASS (LIMITED) / T1–T12 NOT RUN`
- **Related plan:** `VANGUARD_SCOS_Acceptance_Test_Plan_v0.1.md`
- **Source:** `/VANGUARD-SCOS-INTAKE/Epistemology_V9.0_Source.docx`
- **Source SHA-256:** `e3087ac7a077da0bd3ef924838f177496b3f2b44025b7da981dff481534ce316`

| Test ID | Area | Status | Evidence | Notes |
|---|---|---|---|---|
| T0 | Source/build identity | `PASS — LIMITED` | `VSC_T0_Smoke_Test_Results_v0.2.json`; source hash above | DOCX exists, SHA-256 recorded, ZIP/XML parse passed; manifest-listed package payloads verified from clean extraction. No build/dependency lock or runnable build identity exists. |
| T0-SMOKE | Repeatable static source check | `PASS — STATIC ONLY` | `run_vscos_t0.py`; result JSON SHA-256 `ba89c75eec4acc128449955369e43eb428f5e7ef16daec606fc061e9039b0886` | Two runs from a clean extraction without v0.2 produced identical result bytes. Source was not imported/executed. |
| T1 | Policy denial | `NOT RUN` | None | Must demonstrate no adapter call after denial. |
| T2 | Adapter normalization | `NOT RUN` | None | Runtime behavior not exercised. |
| T3 | Search correctness | `NOT RUN` | None | No deterministic MCTS toy implementation tested. |
| T4 | Verification boundary | `NOT RUN` | None | No runtime promotion gate tested. |
| T5 | State separation | `NOT RUN` | None | No state mutation controls tested. |
| T6 | Internalization lifecycle | `NOT RUN` | None | Lifecycle behavior not executed. |
| T7 | Self-modification containment | `NOT RUN` | None | No sandbox/patch test. |
| T8 | Rollback/recovery | `NOT RUN` | None | No runtime rollback test. |
| T9 | RSI claim discipline | `NOT RUN` | None | No baseline benchmark. |
| T10 | Pulse-controller value | `NOT RUN` | None | No controlled benchmark. |
| T11 | Multi-agent/quorum evidence | `NOT RUN` | None | No independent evaluator/fault-model test. |
| T12 | Capability/provider swap | `NOT RUN` | None | No adapter swap test. |

## T0 raw observations
- Source bytes: 22,423
- Source SHA-256: `e3087ac7a077da0bd3ef924838f177496b3f2b44025b7da981dff481534ce316`
- DOCX ZIP integrity: PASS; `word/document.xml` parsed; 608 non-empty paragraphs observed.
- v0.3 defect: T0 attempted to open a v0.2 ZIP absent from the v0.3 archive.
- v0.3.1 correction: script roots paths at its own directory and validates manifest-listed payloads; it does not require v0.2.
- Isolated rerun: two exit codes 0, two PASS results, identical result JSON SHA-256.

## Scope limitation
T0 verifies source identity/container integrity and selected static markers only. It does not prove the submitted program imports, initializes, runs, is secure, performs as advertised, uses quantum hardware, or is ready for integration.

## Promotion rule
No component is `VERIFIED` until its specified tests pass with retained evidence. No component is `CONFIRMED` without required independent/repeated confirmation. No component is `ADOPTED` without explicit decision and dependency/conflict reconciliation.
