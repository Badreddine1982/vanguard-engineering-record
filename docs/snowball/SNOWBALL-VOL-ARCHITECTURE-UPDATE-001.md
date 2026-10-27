# SNOWBALL — VOL Architecture Update 001

**Status:** ARCHITECTURAL UPDATE / PROPOSED  
**Date:** 2026-10-04  
**Scope:** Snowball staged operational-authorization architecture  
**Change Type:** ADD / REFRAME  
**Promotion:** Not yet permanent law; requires later verification/confirmation before adoption

## 1. Purpose

This update establishes the VOL framework as a staged operational-authorization system for Snowball.

VOL stages are not game levels, intelligence scores, or rewards for “winning”. A stage represents a maturity boundary at which the system may qualify for additional operational permissions after demonstrating competence with the permissions and constraints already available to it.

> The system gradually earns the operational right to perform actions that were previously prohibited, after demonstrating that it can handle the preceding permissions safely and verifiably.

## 2. Fundamental Distinctions

```text
Capability ≠ Permission
Permission ≠ Qualification

Capability
    ↓
Evidence
    ↓
Verification
    ↓
Qualification
    ↓
Permission
```

Technical capability alone never authorizes an action. Reward/value signals may measure progress and guide learning, but they do not independently grant permissions.

## 3. VOL as a Maturity Stage

```text
VOL-n
├── Laws
├── Permissions
├── Evidence Requirements
├── Verification
├── Promotion Gate
├── Rollback
└── KMA Record
```

A later VOL inherits applicable laws and permissions of earlier stages and adds only additional operational rights that have a justified architectural need.

## 4. VOL-1 — Initial Integrated Development Stage

VOL-1 is intentionally low-risk. Its purpose is to establish the complete self-development loop under containment.

Permitted activities include:

- inspect authorized system/runtime state;
- read and use authorized knowledge;
- create bounded experiments;
- create and modify code/tools inside an isolated sandbox;
- execute tests and benchmarks inside the permitted environment;
- analyze failures and record reusable failure evidence;
- retain successful and unsuccessful experiment records;
- acquire bounded capabilities through controlled experiments;
- propose changes for later stages without directly granting them;
- use bounded external research when `WEB_RESEARCH` is explicitly granted.

VOL-1 does not authorize:

- direct protected core/kernel modification;
- modification of VOL laws or promotion gates during ordinary operation;
- rewriting, deleting, or falsifying evidence to obtain qualification;
- self-promotion or self-granting permissions;
- silent alteration of Master State or protected contracts;
- turning search/reward results into architectural authority.

## 5. Scoped Internet Research Permission

Candidate permission: `WEB_RESEARCH`

Purpose:

- reliable sources;
- primary sources and research papers;
- advanced technical research;
- comparison of approaches;
- claim verification and knowledge-gap resolution;
- evidence collection for bounded research objectives.

The permission is purpose-scoped and provenance-aware. It does not imply unrestricted web execution or unrestricted external action. External information remains untrusted until it passes the applicable verification path.

## 6. External Model / GPT Permission

Access to GPT or another external advanced model is treated as a separate operational permission rather than a mandatory dependency.

It may be opened in a later VOL after the system demonstrates the required competence under earlier permissions.

The permission should define:

- allowed purpose;
- model/provider boundary;
- input/output scope;
- provenance requirements;
- cost/resource limits where applicable;
- verification requirements;
- rollback/revocation conditions.

The external model remains an adapter/capability provider and does not receive Snowball’s architectural authority through access.

## 7. Permission Design Rule

Every newly opened permission must have:

1. a reason it is needed;
2. an explicit scope;
3. a known risk class;
4. governing laws/constraints;
5. evidence requirements;
6. a verification path;
7. monitoring/audit requirements;
8. a rollback or suspension path.

> Use the smallest permission that demonstrates the largest useful part of the intended architecture.

Verification cost should increase with the risk and power of the newly opened permission.

## 8. VOL-2 and Later Stages

No final VOL-2 permission set is fixed by this update.

VOL-2 must be derived from demonstrated needs arising from VOL-1 and must answer:

- What can VOL-2 do that VOL-1 cannot?
- Why is the additional authority necessary?
- What new risk does it introduce?
- Which law governs it?
- What evidence proves readiness?
- What verification is sufficient?
- What happens on failure?

The same method applies recursively to later stages.

## 9. Promotion Authority

```text
Search / Learning
       ↓
Candidate behavior
       ↓
Evidence
       ↓
Verification
       ↓
Qualification
       ↓
Promotion Gate
       ↓
Permission expansion
```

MCTS, AIXI-style priors, reward functions, agents, or external models may contribute evidence or search efficiency, but none may self-certify or directly grant authorization.

## 10. Persistence of Granted Permissions

A qualified permission becomes an operational right within its defined scope. Persistence does not mean unrestricted use: scope, policy, monitoring, resource limits, and suspension/rollback conditions remain active.

A permission can therefore be durable without becoming absolute.

## 11. KMA Relationship

KMA records the authorization journey without becoming the authorization authority itself.

Relevant records should preserve:

```text
VOL
permission
qualification evidence
verification result
provenance
scope
conditions
promotion decision
rollback history
failure evidence
```

This preserves:

`Storage ≠ Verification ≠ Adoption`

and keeps context, provenance, verification state, and applicability boundaries attached to evidence.

## 12. Rollback / Failure Principle

```text
Attempt
  ↓
Failure / insufficient evidence
  ↓
Rollback to last authorized state
  ↓
Preserve evidence + failure record
  ↓
Remain in current VOL
  ↓
Reopen only with new evidence / justified experiment
```

Failure is retained as reusable negative knowledge rather than erased.

## 13. Architectural Boundary

This update does not:

- declare all future VOL laws final;
- grant Snowball unrestricted Internet access;
- grant GPT/external models automatic authority;
- make MCTS the permission controller;
- modify VERITAS-AIXI core;
- claim that Snowball has already demonstrated qualifications required for future permissions.

## 14. Resulting Snowball Model

```text
                         SNOWBALL
                            │
                    VOL Maturity Framework
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
       Laws            Permissions          Evidence
        │                   │                   │
        └───────────────────┼───────────────────┘
                            ↓
                       Verification
                            ↓
                       Qualification
                            ↓
                      Promotion Gate
                            ↓
                 New Operational Rights
                            ↓
                    KMA / Evidence Record
                            │
                       Failure / Rollback
                            └────→ current authorized state
```

## 15. Current Disposition

- **This update:** ARCHITECTURAL / PROPOSED
- **VOL-1 framework:** defined as the initial low-risk integrated stage.
- **WEB_RESEARCH:** defined as a candidate scoped permission; not unrestricted Internet authority.
- **External GPT/model access:** defined as a later candidate permission; not a core dependency.
- **VOL-2+:** intentionally open for evidence-driven derivation.
- **Adoption:** not claimed by this update alone.

## 16. Governing Principle

> Snowball does not grow its authority because it can perform an action. It grows its authority only when evidence demonstrates that granting that action is justified within a defined scope and verification boundary.