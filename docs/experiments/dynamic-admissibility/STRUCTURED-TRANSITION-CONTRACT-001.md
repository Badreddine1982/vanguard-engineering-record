# STRUCTURED-TRANSITION-CONTRACT-001 — Candidate Research Contract

- **Contract ID:** STC-001
- **Version:** 0.1
- **Status:** RESEARCH CANDIDATE — NOT A LAW — NOT ADOPTED
- **Project:** PRJ-DYNAMIC-ADMISSIBILITY-001
- **Purpose:** Prepare a falsifiable formalization of a unified admissibility-aware transition law.

## 1. Core question

Can one domain-neutral transition interface constrain state evolution while leaving proposal/search free to explore, and derive operational consequences from relations rather than independent per-mode rules or a fixed list of semantic coordinates?

## 2. Separation of responsibilities

1. **Proposal policy (future MCTS/UCT adapter):** ranks or proposes candidate transitions. Its score is not evidence of validity and conveys no activation authority.
2. **Domain relation adapter:** supplies explicit facts about a proposed transition: hard-constraint result, representation relation, and admissible dynamic extent/time horizon. The adapter may be implemented differently by different domains.
3. **Transition kernel:** filters proposals using the supplied relation contract, retains all admissible alternatives for search, and computes the effective dynamic extent. It must not infer validity from preference.
4. **Activation gate:** permits activation only when the candidate is admissible, capability exists, and activation is authorized. Validity alone never activates a capability.
5. **Outcome observations:** REDIRECT, BRANCH, SLOWDOWN, FOLD, UNFOLD, CONTINUE, HOLD_DORMANT, and TERMINATE are diagnostic consequences of the resulting relation set, not mutually exclusive commands hard-coded into candidate generation.

## 3. Abstract contract

Let `S` be a set of states; no coordinates are presumed. Let `P(s,t)` be the proposal set at state `s` and time `t`. A candidate transition is `τ = (s, s', Δt, e)` where `e` is relevant evidence/context.

A domain adapter supplies:

- `A(s, τ, e, t)`: a three-valued admissibility assessment (`TRUE`, `FALSE`, `UNKNOWN`);
- `R(s, s')`: an abstract representation relation, e.g. lower / equivalent / higher (the comparator is domain supplied; the core need not know representation coordinates);
- `H(s, s', e, t)`: a checked maximum admissible evolution horizon/extent for this transition;
- `Cap(s')` and `Auth(τ,t)`: capability existence and activation authorization.

The transition kernel may compute an effective horizon `Δt* = min(Δt, H)` only when the domain adapter guarantees that the shortened transition is meaningful and it re-evaluates hard constraints for the resulting transition. Otherwise it must reject or defer rather than assume shortening makes it safe.

An activation is allowed only if:

`A(s, τ*, e, t) ∧ Cap(s') ∧ Auth(τ*,t)`

where `τ*` is the actual transition at the effective horizon. Proposal score is deliberately absent from this predicate.

## 4. Outcome semantics (observations, not separate validity laws)

- **REDIRECT:** the preferred proposal is not activatable/admissible, while another admissible and activatable successor exists.
- **BRANCH:** more than one admissible, activatable successor remains available for exploration.
- **SLOWDOWN:** the proposed evolution horizon exceeds the checked admissible horizon and the shortened transition passes re-evaluation.
- **FOLD / UNFOLD:** the representation comparator reports a lower / higher representation relation for the selected transition.
- **CONTINUE:** a valid transition proceeds without another reported outcome.
- **HOLD_DORMANT:** admissible transitions exist, but no capability can be activated under current authorization/capability state.
- **HOLD_UNRESOLVED:** at least one candidate has UNKNOWN admissibility and no known admissible activatable successor was selected; the kernel must not claim proven impossibility. Unknown candidates never activate.
- **HOLD_REVALIDATION:** the effective transition failed revalidation; it must not activate merely because the original proposal passed.
- **TERMINATE:** no admissible successor exists in the defined candidate set and no unresolved candidate prevents that scoped conclusion. This is scoped to the present state, evidence, horizon, and proposal set—not a claim of global impossibility.

More than one outcome observation may apply to a transition. The kernel must not force a false single-label priority order. If equally preferred admissible branches remain and the proposer has not selected one, the kernel must preserve the branch set rather than break the tie by arbitrary identifiers or a hidden central preference.

## 5. Invariants required of every implementation

- Proposal preference cannot override hard admissibility.
- Equal-scored valid alternatives are not resolved by arbitrary ID ordering; they remain available for further search.
- Capability existence, activation, and validity remain distinct.
- A failed candidate does not silently mutate state or erase evidence.
- Every shortened/modified transition is re-evaluated.
- Representation relations are supplied by an adapter; the core does not assume a universal coordinate system.
- Empty known-admissible successor sets yield a scoped no-continuation result; unresolved candidates yield HOLD_UNRESOLVED rather than a false global-impossibility claim.
- Results preserve source state, proposed transition, effective transition, evidence, time/horizon, and all applicable outcome observations.

## 6. Research limits

This contract is a candidate specification. It is not a theorem, a universal law, proof of dimension independence, a safety certification, or evidence of actual MCTS/UCT integration. Domain adapters can encode mistaken constraints; formal soundness depends on their definitions and evidence.

## 7. Falsification gates

The candidate must be revised or rejected if any implementation allows preference to override constraints, activates a dormant/unauthorized capability or UNKNOWN candidate, breaks an equal-preference tie using arbitrary identifiers, shortens a transition without successful revalidation, loses valid alternatives, is sensitive to irrelevant state renaming, or cannot reproduce the required outcome observations across independently designed representations.

Next: EXP-003 tests this contract at interface level. Passing EXP-003 would support implementation consistency only. A mathematical proof requires explicit assumptions, definitions, lemmas, and a proof that the stated invariants follow from them.