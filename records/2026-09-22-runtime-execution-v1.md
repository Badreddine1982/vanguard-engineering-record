# Runtime Execution v1 — Initial Vertical Slice

## State

VERIFIED / COMPATIBILITY EVIDENCE IN PROGRESS

## Sources

- `vanguard-contracts`: `contracts/runtime/execution.v1.yaml`
- `vanguard-contracts`: `contracts/runtime/execution.v1.schema.yaml`
- `vanguard-runtime`: `src/execution.py`
- `vanguard-runtime`: `tests/test_execution.py`
- `vanguard-runtime`: `contracts.lock`
- `vanguard-runtime`: `scripts/verify_contract_lock.py`
- `vanguard-runtime`: `verification/contract-lifecycle.yaml`
- `vanguard-runtime`: `verification/lifecycle-proof.yaml`
- `vanguard-runtime`: `scripts/test_contract_lifecycle.py`

## Evidence currently available

- Contract definition exists and is versioned.
- Runtime request/result types exist.
- Deterministic validation paths are implemented.
- GitHub Actions previously exposed a concrete CI environment failure: pytest was not provisioned.
- Corrective CI provisioning was applied and a subsequent workflow completed successfully before Contract Lock was introduced (run `35717683211`).
- Runtime pins `runtime.execution@1.0.0` to immutable source commit `775c9850d6a2231cc619b3d64570ca9f08429635`.
- GitHub Actions run `35841837937` (run #21) completed successfully on runtime commit `9ed82687afe24615ad41894934efa78baf07b89b`.
- Run #21 passed lifecycle definition verification, the strengthened transition-guard mechanism proof, Contract Lock verification, runtime execution tests, and the explicit adoption gate.
- The lifecycle fixture proved `LOCKED -> VERIFIED -> CONFIRMED -> ADOPTED` while explicitly recording `real_contract_state_changed: false`.

## Interpretation

The first lifecycle step is now closed at the **mechanism level**.

This proves that the lifecycle can enforce its declared transition guards and that automatic adoption is blocked. It does not mean that the real `runtime.execution` contract has been adopted.

The next step is therefore Compatibility Evidence: a machine-readable record tying the exact source contract, exact runtime commit, exact verification run, and observed test results together.

## Compatibility Evidence — in progress

Record:
`records/compatibility/runtime-execution-v1.yaml`

Current source:
- component: `vanguard-contracts`
- contract: `runtime.execution@1.0.0`
- source commit: `775c9850d6a2231cc619b3d64570ca9f08429635`

Current target:
- component: `vanguard-runtime`
- target commit: `9ed82687afe24615ad41894934efa78baf07b89b`

Evidence anchor:
- workflow: `Runtime Contract Test`
- run: `35841837937`
- run number: `21`
- conclusion: `success`

The current record is deliberately marked `in_progress`: the successful workflow establishes a strong first evidence package, but the compatibility claim is not yet promoted to final confirmation or adoption.

## Corrective action history

1. CI failed because pytest was not provisioned.
2. The workflow was amended to provision Python 3.11 and pytest.
3. GitHub subsequently recorded a successful runtime test run.
4. Contract Lock was introduced to pin the contract source by immutable commit.
5. The lifecycle mechanism was added and initially proved with an isolated fixture.
6. The lifecycle test was strengthened to exercise actual transition guards and reject invalid transitions.
7. Run #21 completed successfully with all lifecycle, lock, runtime-test, and explicit-adoption-gate steps passing.
8. Compatibility Evidence has now been opened as a separate machine-readable record.

## Confirmation status

The lifecycle **mechanism** is verified and confirmed by GitHub execution evidence.

The real `runtime.execution` contract remains **not adopted**. Compatibility Evidence is in progress; confirmation and adoption remain evidence-gated and require explicit approval.

## Governing rule

Probability may enter the loop, but it does not leave the loop as truth without confirmation.
