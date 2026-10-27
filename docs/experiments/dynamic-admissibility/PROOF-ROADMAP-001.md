# PROOF-ROADMAP-001 — From Toy Interface to a Mathematical Transition Law

- **Roadmap ID:** PROOF-ROADMAP-001
- **Version:** 0.1
- **Status:** RESEARCH PLAN — OPEN — NO THEOREM ESTABLISHED
- **Project:** PRJ-DYNAMIC-ADMISSIBILITY-001
- **Basis:** EXP-001 through EXP-003 and STRUCTURED-TRANSITION-CONTRACT-001

## Purpose
Prepare a disciplined route toward proving a unified transition law without mistaking passing toy tests for proof, fixing semantic coordinates in advance, or assigning admissibility authority to MCTS.

## Candidate formal skeleton
Let `S` be an abstract state set and `P(s,t,e)` a set of proposed transitions available at state `s`, time `t`, and evidence/context `e`. A transition is not accepted because a search policy gives it a high score.

A domain theory supplies:
- a three-valued admissibility assessment: `TRUE`, `FALSE`, or `UNKNOWN`;
- a dynamic viability/horizon relation for the actual transition;
- a representation relation between source and target descriptions;
- separate capability-presence and activation-authorization predicates.

The kernel returns (i) known admissible successors, (ii) unresolved candidates, (iii) effective transition/horizon after domain-approved adjustment and revalidation, (iv) activation decision, and (v) derived outcome observations. It must preserve multiple valid successors rather than imposing a single preferred direction by definition.

## First conditional lemma (kernel-level, not a universal law)

`KERNEL-SAFETY-LEMMA-001.md` states the first proof target: by the definition of the kernel's activatable set, an activated candidate must satisfy the adapter-supplied TRUE admissibility result for the effective transition, pass effective-transition revalidation, possess the capability, have activation authorization, and have a positive effective horizon. This follows from the kernel guard **assuming the adapter facts are sound**. It is not proof that the adapters correctly model a real system, nor proof that a universal admissibility law exists.

## Proof obligations (separate gates)

### P0 — Definitions and assumptions
Specify state, transition, evidence, time, admissibility, dynamic viability, representation relation, capability, activation, and what counts as an observation. State which facts come from a domain adapter and which are proved by the kernel.

### P1 — Safety of the kernel (conditional theorem)
Prove that every activated transition passed the admissibility predicate for the *effective* transition, has an existing capability, and has explicit activation authorization. Prove that preference scores cannot bypass those checks. This theorem is conditional on the soundness of the supplied predicates.

### P2 — Unknown-state discipline
Prove that `UNKNOWN` never activates and is never silently converted to either `TRUE` or a claim of global impossibility. Demonstrate that an unresolved novel candidate does not suppress known valid alternatives or get mistaken for a proven safe branch.

### P3 — Dynamic step validity
Define when reducing `Δt`/extent preserves the meaning of a transition. Prove the kernel activates only after revalidation of the actual shortened transition. Do not assume a smaller step is automatically safe.

### P4 — Representation/fold-unfold preservation
Define abstraction/refinement maps between representation levels. State and prove which properties must be preserved under fold/unfold (for example, specified observations or invariants). Ordering a representation as “lower” or “higher” alone does not prove semantic preservation.

### P5 — Conditional viability and liveness
Separate safety (never take a forbidden transition) from liveness (eventually take a valid transition when one exists). State the additional assumptions needed for fair search, bounded delay, and nonempty viable successors. MCTS/UCT does not supply these guarantees by itself.

### P6 — Representation independence
Define the intended meaning of “no fixed semantic coordinates.” The first claim to test is invariance under isomorphic relabeling and equivalence-preserving adapters. A stronger claim across arbitrary state representations requires a formal theorem; success on two examples is not enough.

### P7 — Adversarial and implementation testing
Test conflicting constraints, stale evidence, false or missing adapter results, changing time horizons, cyclic/redundant representations, all-invalid successors, unknown candidates, equal-score alternatives, and alternative valid branches. Then compare independent implementations and integrate actual MCTS/UCT as a proposal mechanism only.

## Acceptance gates
- **Gate A:** definitions and assumptions explicit; examples no longer rely on hidden semantics.
- **Gate B:** conditional safety properties proved on paper and tested against counterexamples.
- **Gate C:** representation and dynamic invariants stated and tested across independent adapters.
- **Gate D:** actual MCTS/UCT experiments show it cannot override validity; search quality is evaluated separately.
- **Gate E:** independent review/reproduction; only then consider `VERIFIED` or `CONFIRMED` status.
- **Adoption:** requires a separate explicit decision; it is never inferred from tests or proof artifacts alone.

## Non-goals and warnings
This roadmap does not claim that the law is possible in the desired strong form. The candidate may be narrowed or rejected by counterexamples. Mathematical correctness of the adapter predicates is a separate obligation; a generic interface cannot make an incorrect domain model sound. The quantum-entanglement analogy remains illustrative only and carries no physical claim.