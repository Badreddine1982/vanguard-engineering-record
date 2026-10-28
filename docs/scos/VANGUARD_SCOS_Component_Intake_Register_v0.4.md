# Component Intake Register — VANGUARD / SCOS / AGI ARC

- **Record ID:** LIB-INTAKE-VSC-REG-001
- **Revision:** 0.4
- **Updated:** 2026-10-28
- **Status:** `SOURCE IDENTITY CAPTURED / T0 ISOLATED REPRODUCTION VERIFIED / T1–T12 NOT RUN / NOT ADOPTED`
- **Rule:** Each row remains a separate knowledge object until an explicit reconciliation decision authorizes a relationship or merge.

| Intake ID | Candidate | Source / provenance | Proposed role | Evidence known | Intake decision | Next action |
|---|---|---|---|---|---|---|
| VSC-C01 | VANGUARD knowledge/autonomy contract v0.2 | `VANGUARD_AI_v0.2_Knowledge_Autonomy_Contract.md` | Lifecycle, state separation, controlled evolution | Contract exists; not proof of full implementation | Reference baseline | Reconcile with Master Page |
| VSC-C02 | Harness Adapter v0.3 | `VANGUARD_AI_v0.3_Harness_Adapter_Contract.md` | Provider-neutral execution boundary | Implementation/tests require independent check | Reference baseline | Inspect implementation/tests |
| VSC-C03 | MCTS architecture v0.4 | `VANGUARD_AI_v0.4_MCTS_System_Architecture.md` | System-wide search abstraction | Contract exists; tests not run here | Experimental candidate | Reproduce acceptance tests |
| VSC-C04 | VERITAS-AIXI verMCTS / reversible search | `VERITAS_AIXI_v0.2_CONTRACTS.md`; `VERITAS-AIXI_EXP-001_MCTS-Fold-Seed-Unfold.md` | Verification-aware search and reversible speculative state | Bounded proof-of-concept only | Retain experiment | Expand benchmark |
| VSC-C05 | SCOS / Sovereign Mind pulse/domains | Conversation drafts; canonical source unresolved | Adaptive scheduling/decomposition | No verified integrated implementation established | Preserve candidate | Identify source; define timing; baseline test |
| VSC-C06 | CTM / CLIO | AGI ARC / SCOS drafts | State update / optimization | Draft-level | Experimental | Define equations, invariants, unit tests |
| VSC-C07 | DGM / self-programming | Multiple drafts | Candidate patch search | No permission to mutate protected core | Sandbox-only | Propose-test-verify-rollback |
| VSC-C08 | eQMARL / multi-agent mixing | Multiple drafts | Optional coordination | Classical weighted mixing is not quantum entanglement | Experimental adapter | Compare with simple baselines |
| VSC-C09 | TripleEvaluator | SCOS draft | Evidence/utility evaluator | Suspected unreachable norm-delta condition requires source-level test | Not accepted | Specify signed metric and edge cases |
| VSC-C10 | Quorum | AGI ARC draft | Independent evidence aggregation | Random voting is not valid evidence | Reject current mechanism; retain idea | Define independence/fault model |
| VSC-C11 | RSI-Isolated E0 | `RSI_Isolated_Project_E0.md` | Independent RSI research | Useful performance gate failed | `NOT ADOPTED`; retain negative evidence | New experiment only with justified change |
| VSC-C12 | Damage-resilient nucleus | `damage_resilient_nucleus.py` | Fault detection/recovery candidate | Full behavior/tests not assessed here | Separate experiment | Inspect source; define fault model/tests |
| VSC-C13 | Epistemology V9.0 / AdvancedAGI | `/VANGUARD-SCOS-INTAKE/Epistemology_V9.0_Source.docx`; audit `LIB-AUDIT-VSC-V9-001` | Possible framework/candidate interfaces | Source SHA-256 recorded; T0 isolated reproduction passed in limited scope; submitted program not executed | Preserve source; no wholesale merge; `NOT VERIFIED / NOT ADOPTED` | Resolve dependencies; define runnable isolated candidates and runtime tests |

## Status vocabulary
- `LOCKED`: intake identity/source captured; no adoption.
- `VERIFIED`: claim passed its defined verification procedure.
- `CONFIRMED`: independent/repeated confirmation satisfied the contract.
- `ADOPTED`: explicit decision after reconciliation and evidence.
- `NOT ADOPTED`: preserved but not approved for integration.
- `GAP`: required information/evidence missing.
- `OBSERVED IN SOURCE`: visible in reviewed artifact, not necessarily operationally validated.

## No-assumption rule
Library storage does not prove implementation completeness, test success, integration, security, or adoption.

## Revision 0.4 change log
- Recorded the v0.3 T0 dependency defect and corrected it in package v0.3.1.
- T0 passed twice from a clean extraction without v0.2; result hashes matched.
- T1–T12 remain `NOT RUN`; no component promoted to `VERIFIED`, `CONFIRMED`, or `ADOPTED`.
