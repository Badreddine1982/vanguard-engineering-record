# Runtime Execution v1 — Initial Vertical Slice

## State

PROPOSED / EVIDENCE PENDING

## Sources

- `vanguard-contracts`: `contracts/runtime/execution.v1.yaml`
- `vanguard-contracts`: `contracts/runtime/execution.v1.schema.yaml`
- `vanguard-runtime`: `src/execution.py`
- `vanguard-runtime`: `tests/test_execution.py`
- `vanguard-runtime`: `contracts.lock`
- `vanguard-runtime`: `scripts/verify_contract_lock.py`

## Evidence currently available

- Contract definition exists and is versioned.
- Runtime request/result types exist.
- Deterministic validation paths are implemented.
- GitHub Actions previously exposed a concrete CI environment failure: pytest was not provisioned.
- Corrective CI provisioning was applied and a subsequent workflow completed successfully before Contract Lock was introduced (run `35717683211`).
- Runtime now pins `runtime.execution@1.0.0` to immutable source commit `775c9850d6a2231cc619b3d64570ca9f08429635`.
- The workflow now verifies the pinned contract from its immutable GitHub source before running runtime tests.
- The new Contract Lock verification workflow run is currently in progress; final evidence is pending.

## Interpretation

The Contract Lock establishes an explicit, reproducible relationship between the runtime implementation and one exact version of the contract repository. It does not by itself establish that the runtime satisfies the contract.

That distinction is deliberate: identity and compatibility claims require execution evidence.

## Corrective action history

1. CI failed because pytest was not provisioned.
2. The workflow was amended to provision Python 3.11 and pytest.
3. GitHub subsequently recorded a successful runtime test run.
4. Contract Lock was then introduced to pin the contract source by immutable commit.
5. A new workflow run was triggered to verify the lock and then execute the tests.

## Confirmation status

Not confirmed as an adopted system contract. The lock relationship is implemented, but final adoption remains evidence-gated until the new lock verification run completes successfully and the resulting evidence is recorded.

## Governing rule

Probability may enter the loop, but it does not leave the loop as truth without confirmation.
