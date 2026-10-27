# SNOWBALL — Independent Research Project

**Project ID:** SNOWBALL-INDEP-001  
**Status:** LOCKED / RESEARCH INCUBATOR  
**Lifecycle:** Candidate → Evidence → Verification → Confirmation → Adoption  
**Scope:** Independent, portable project; no authority to alter VANGUARD, Library governance, or protected core systems.

## Technical Definition

SNOWBALL is an independent research project for studying staged operational maturation: a system begins with deliberately limited capabilities and permissions, then may earn additional operational rights only after demonstrating safe, verifiable competence within its current scope.

**State:** Architectural candidate under experimental validation.  
**Provenance:** Derived from the VOL architecture work and VOL Architecture Review 001.  
**Scope:** Permission governance, staged qualification, evidence-driven progression, rollback, monitoring, and memory of authorization history.  
**Evidence status:** Architectural; empirical qualification remains pending.

## Core Principle

> The system does not advance because a new level exists; it earns additional operational rights after proving that it can safely and verifiably handle the rights already granted.

## Fundamental Distinctions

- Capability ≠ Permission
- Permission ≠ Qualification
- Qualification → Permission expansion
- Evidence ≠ Verification
- Verification ≠ Adoption
- KMA records the authorization journey; it does not grant authority.

## VOL Model

A VOL is a maturity stage containing:

1. Laws
2. Capabilities
3. Permissions
4. Evidence requirements
5. Verification requirements
6. Promotion gate
7. Monitoring
8. Rollback rules
9. KMA record

Later VOLs inherit previously qualified scope unless explicitly constrained by stronger governance.

## VOL-1 — Current Experimental Baseline

VOL-1 is deliberately low-risk and sandboxed. It demonstrates a complete learning/development loop without granting authority over protected system state.

### Permitted candidate activities

- Read authorized state and knowledge.
- Create bounded experiments.
- Create or modify code/tools inside a sandbox.
- Run tests and benchmarks.
- Analyze failures.
- Preserve evidence, failures, and lessons.
- Propose changes for later qualification.
- Conduct bounded web research when WEB_RESEARCH is explicitly enabled.

### Protected / prohibited

- No modification of the core kernel.
- No modification of VOL laws or promotion gates.
- No modification of verification authority.
- No deletion or rewriting of evidence.
- No self-promotion.
- No self-granting of permissions.
- No unrestricted external action.

## WEB_RESEARCH Permission

WEB_RESEARCH is a scoped research permission, not unrestricted internet execution.

Its intended scope may include reliable-source discovery, primary research, advanced research, comparison, claim verification, and provenance capture.

Retrieved information is a candidate input to the evidence pipeline; it does not become authority merely because it was retrieved.

## External GPT / Model Access

External model access is a later candidate permission, not a core dependency. If enabled in a future stage, its purpose, scope, provider, inputs/outputs, provenance, cost, verification, monitoring, and rollback must be defined before qualification.

## Evidence and Promotion Chain

Search / Learning → Candidate → Evidence → Verification → Qualification → Gate → Permission expansion → KMA record

Search mechanisms, external models, or experiments cannot self-certify or directly grant authority.

## Rollback Principle

Failure must not erase evidence. Operational authority may be suspended or rolled back to the last qualified state while the evidence remains intact.

## VOL-2 Derivation Rule

VOL-2 must not be invented merely as a stronger level. It should be derived from demonstrated limits of VOL-1:

1. Identify a real operational need.
2. Demonstrate that VOL-1 cannot satisfy it within current permissions.
3. Define the smallest additional permission that resolves the need.
4. Analyze its new risk.
5. Define its governing law and evidence requirements.
6. Verify qualification conditions.
7. Only then propose VOL-2 adoption.

## Independence / Portability

SNOWBALL is self-contained and portable. Its package can be copied into another project without transferring authority from the source project. The receiving project must independently evaluate compatibility, provenance, scope, and evidence status.

## Current Disposition

- Project existence: **proposed for Library intake**
- VOL-1 architecture: **reviewed; empirical qualification pending**
- WEB_RESEARCH: **candidate scoped permission**
- External GPT/model access: **future candidate permission**
- VOL-2: **intentionally open**
- Automatic adoption into VANGUARD: **not permitted**

## Governing Research Rule

No architectural claim becomes permanent knowledge merely because it is plausible. Experiments, successful or failed, are retained in the project archive with their evidence status.