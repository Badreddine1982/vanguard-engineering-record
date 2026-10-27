# KERNEL-SAFETY-LEMMA-001 — Activation Soundness Under Adapter Assumptions

- **Lemma ID:** KERNEL-SAFETY-LEMMA-001
- **Version:** 0.1
- **Status:** PRELIMINARY CONDITIONAL LEMMA — PROOF SKETCH — NOT EXTERNALLY VERIFIED
- **Project:** PRJ-DYNAMIC-ADMISSIBILITY-001
- **Depends on:** `STRUCTURED-TRANSITION-CONTRACT-001.md`, `experiment_exp003.py`

## Definitions
For a candidate transition `c`, let:
- `A(c) ∈ {TRUE, FALSE, UNKNOWN}` be the domain adapter's hard admissibility result;
- `V(c) ∈ {TRUE, FALSE}` be the adapter's revalidation result for the actual effective transition after any dynamic-horizon adjustment;
- `K(c)` mean the required capability exists;
- `U(c)` mean activation is explicitly authorized;
- `h*(c) = min(h_proposed(c), h_max(c))` be the effective horizon, with domain semantics supplied by the adapter.

The kernel may activate `c` only if:

`A(c) = TRUE ∧ V(c) = TRUE ∧ K(c) ∧ U(c) ∧ h*(c) > 0`.

The adapter-produced booleans are assumptions/inputs for this lemma; the kernel does not prove their domain-level soundness.

## Lemma 1 — Activation soundness (conditional)

**Claim.** If the kernel returns `activated(c) = TRUE`, then `A(c) = TRUE`, `V(c) = TRUE`, `K(c) = TRUE`, `U(c) = TRUE`, and `h*(c) > 0`.

**Proof sketch.** The kernel's activation assignment is the conjunction of effective-transition revalidation, a TRUE hard-admissibility result, positive effective horizon, capability presence, and activation authorization. Therefore a true activation result implies every conjunct. This is a direct implementation invariant, conditional on the meaning and correctness of the supplied adapter results.

## Lemma 2 — Proposal preference has no validity authority (conditional)

**Claim.** A candidate with `A(c) ≠ TRUE` or `V(c) = FALSE` cannot become activated solely because its preference score is higher than those of other candidates.

**Proof sketch.** The kernel forms the activatable candidate set only from candidates whose hard admissibility is TRUE and whose effective transition passed revalidation, and then applies capability/authorization gates. Preference is considered only within that set. Thus ranking cannot add a candidate to the set or bypass the activation conjunction.

## Lemma 3 — Unknown-state fail-closed behavior (interface property)

**Claim.** A candidate with `A(c) = UNKNOWN` cannot be activated, and if no known admissible successor exists while unresolved candidates remain, the kernel reports `HOLD_UNRESOLVED`, not `TERMINATE`.

**Proof sketch.** UNKNOWN candidates are excluded from the known-admissible set. The empty-known-set branch checks for unresolved candidates before producing the scoped termination label; activation only uses known-admissible candidates. This prevents the interface from treating lack of knowledge as proof of impossibility.

## What these lemmas do not prove

They do not prove that a domain adapter has correctly computed admissibility, that the state model covers reality, that `h_max` is safe, that fold/unfold preserves semantics, that MCTS/UCT will explore fairly, or that one universal law exists across arbitrary systems. Those are separate obligations in `PROOF-ROADMAP-001.md`.

The lemmas have not been machine-checked in Lean or another proof assistant. They are precise proof targets with informal derivations from the current kernel design.