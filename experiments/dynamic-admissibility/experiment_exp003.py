"""EXP-003: structured-transition interface checks across independent adapters.

Python standard library only. Not MCTS/UCT, not a formal proof, and not a
safety certification. Domain adapters supply relation facts; the kernel gates
selection/activation without interpreting the domains' state coordinates.
"""
from dataclasses import dataclass
import json
from typing import Optional

@dataclass(frozen=True)
class Candidate:
    ident: str
    preference: float
    hard_admissible: Optional[bool]  # TRUE / FALSE / UNKNOWN from the adapter
    capability_present: bool
    activation_authorized: bool
    representation_relation: str  # LOWER / SAME / HIGHER / UNKNOWN from adapter
    proposed_dt: float
    max_admissible_dt: float
    evidence_ref: str
    effective_revalidation_pass: bool = True  # adapter result for the actual effective transition

# Adapter A: a numeric/ranked representation with a domain-specific risk rule.
def numeric_adapter(*, ident, preference, source_level, target_level,
                    current_risk, risk_delta, capability_present=True,
                    activation_authorized=True, proposed_dt=1.0,
                    max_admissible_dt=1.0, evidence_ref="evidence:numeric",
                    effective_revalidation_pass=True, capability_compatible=True):
    limits = {0: 0.30, 1: 0.60, 2: 0.85}
    relation = "SAME" if target_level == source_level else ("LOWER" if target_level < source_level else "HIGHER")
    known_level = target_level in limits and source_level in limits
    admissible = bool(known_level and capability_compatible and current_risk + risk_delta <= limits[target_level])
    return Candidate(ident, preference, admissible, capability_present, activation_authorized,
                     relation, proposed_dt, max_admissible_dt, evidence_ref,
                     effective_revalidation_pass)

# Adapter B: a symbolic state graph. It uses explicit partial-order relations and
# evidence labels, not numeric coordinates. lower_pairs={(a,b)} means a is a
# lower representation of b. Unordered symbolic states return UNKNOWN.
def symbolic_adapter(*, ident, preference, source, target, lower_pairs,
                     evidence_status, capability_present=True,
                     activation_authorized=True, proposed_dt=1.0,
                     max_admissible_dt=1.0, effective_revalidation_pass=True):
    if source == target:
        relation = "SAME"
    elif (target, source) in lower_pairs:
        relation = "LOWER"
    elif (source, target) in lower_pairs:
        relation = "HIGHER"
    else:
        relation = "UNKNOWN"
    status = {"VERIFIED": True, "REJECTED": False, "UNKNOWN": None}.get(evidence_status)
    if evidence_status not in {"VERIFIED", "REJECTED", "UNKNOWN"}:
        raise ValueError("evidence_status must be VERIFIED, REJECTED, or UNKNOWN")
    return Candidate(ident, preference, status, capability_present, activation_authorized,
                     relation, proposed_dt, max_admissible_dt, f"evidence:{evidence_status.lower()}",
                     effective_revalidation_pass)


def resolve(candidates: list[Candidate], proposed_id: str) -> dict:
    if not candidates:
        return {"effects": ["TERMINATE"], "proposed_id": proposed_id,
                "selected_id": None, "branch_ids": [], "activated": False,
                "feasible_ids": [], "reason": "empty candidate set"}
    by_id = {c.ident: c for c in candidates}
    if proposed_id not in by_id:
        raise ValueError(f"unknown proposed candidate: {proposed_id}")
    proposed = by_id[proposed_id]
    structurally_admissible = [c for c in candidates if c.hard_admissible is True]
    unknown = [c for c in candidates if c.hard_admissible is None]
    admissible = [c for c in structurally_admissible if c.effective_revalidation_pass]
    rejected_on_revalidation = [c for c in structurally_admissible if not c.effective_revalidation_pass]
    activatable = [c for c in admissible if c.capability_present and c.activation_authorized]

    if not admissible:
        if unknown:
            return {"effects": ["HOLD_UNRESOLVED"], "proposed_id": proposed_id,
                    "selected_id": None, "branch_ids": [], "activated": False,
                    "feasible_ids": [], "unresolved_ids": [c.ident for c in unknown],
                    "reason": "unresolved candidates prevent a claim of proven impossibility"}
        if rejected_on_revalidation:
            return {"effects": ["HOLD_REVALIDATION"], "proposed_id": proposed_id,
                    "selected_id": None, "branch_ids": [], "activated": False,
                    "feasible_ids": [], "revalidation_failed_ids": [c.ident for c in rejected_on_revalidation],
                    "reason": "effective transition failed adapter revalidation"}
        return {"effects": ["TERMINATE"], "proposed_id": proposed_id,
                "selected_id": None, "branch_ids": [], "activated": False,
                "feasible_ids": [], "reason": "no known admissible successor in defined candidate set"}
    if not activatable:
        return {"effects": ["HOLD_DORMANT"], "proposed_id": proposed_id,
                "selected_id": None, "branch_ids": [], "activated": False,
                "feasible_ids": [c.ident for c in admissible],
                "reason": "admissible successors exist but none can be activated"}

    # Proposal preference ranks only candidates that already passed the gates.
    # Never break a top-score tie using an arbitrary identifier: preserve the
    # branch set and defer single-path selection to the proposal/search policy.
    effects = []
    if proposed in activatable:
        selected = proposed
    else:
        top_score = max(c.preference for c in activatable)
        top = [c for c in activatable if c.preference == top_score]
        if len(top) > 1:
            effects = ["REDIRECT", "BRANCH"]
            if unknown:
                effects.append("UNRESOLVED_ALTERNATIVES")
            return {
                "effects": effects, "proposed_id": proposed_id, "selected_id": None,
                "branch_ids": [c.ident for c in activatable],
                "feasible_ids": [c.ident for c in admissible], "activated": False,
                "deferred_tie_ids": [c.ident for c in top],
                "unresolved_ids": [c.ident for c in unknown],
                "reason": "equally preferred admissible alternatives retained; no arbitrary tie-break or activation",
                "preference_overrode_admissibility": False,
            }
        selected = top[0]
    if selected.ident != proposed.ident:
        effects.append("REDIRECT")
    if len(activatable) > 1:
        effects.append("BRANCH")
    effective_dt = min(selected.proposed_dt, selected.max_admissible_dt)
    if effective_dt + 1e-12 < selected.proposed_dt:
        effects.append("SLOWDOWN")
    if selected.representation_relation == "LOWER":
        effects.append("FOLD")
    elif selected.representation_relation == "HIGHER":
        effects.append("UNFOLD")
    effective_revalidated = bool(selected.effective_revalidation_pass and selected.hard_admissible is True and effective_dt > 0)
    activated = bool(effective_revalidated and selected.capability_present and selected.activation_authorized)
    if unknown:
        effects.append("UNRESOLVED_ALTERNATIVES")
    if not effects:
        effects.append("CONTINUE")
    return {
        "effects": effects, "proposed_id": proposed_id, "selected_id": selected.ident,
        "branch_ids": [c.ident for c in activatable],
        "feasible_ids": [c.ident for c in admissible], "activated": activated,
        "proposed_dt": selected.proposed_dt, "effective_dt": effective_dt,
        "effective_transition_revalidated": effective_revalidated,
        "unresolved_ids": [c.ident for c in unknown], "representation_relation": selected.representation_relation,
        "evidence_ref": selected.evidence_ref, "preference_overrode_admissibility": False,
    }


def C(ident, pref=0, ok=True, cap=True, auth=True, rel="SAME", dt=1.0, limit=1.0, ev="evidence:toy", recheck=True):
    return Candidate(ident, pref, ok, cap, auth, rel, dt, limit, ev, recheck)

checks = []
def check(name, result, predicate, expected):
    checks.append({"case": name, "pass": bool(predicate(result)), "expected": expected, "result": result})

# Numeric/ranked adapter: hard admissibility is computed from the numeric toy rule.
a1 = [
    numeric_adapter(ident="risky", preference=100, source_level=1, target_level=2, current_risk=0.50, risk_delta=0.40),
    numeric_adapter(ident="safe", preference=5, source_level=1, target_level=1, current_risk=0.50, risk_delta=0.02),
]
r = resolve(a1, "risky")
check("inadmissible_preference_cannot_override_law", r,
      lambda x: x["selected_id"] == "safe" and "REDIRECT" in x["effects"] and x["activated"] and not x["preference_overrode_admissibility"],
      "select authorized admissible alternative; never activate preferred invalid candidate")

branch = [
    numeric_adapter(ident="a", preference=5, source_level=1, target_level=1, current_risk=0.20, risk_delta=0.05),
    numeric_adapter(ident="b", preference=4, source_level=1, target_level=1, current_risk=0.20, risk_delta=0.10),
]
r = resolve(branch, "a")
check("all_valid_alternatives_preserved", r,
      lambda x: set(x["branch_ids"]) == {"a", "b"} and "BRANCH" in x["effects"],
      "retain both admissible authorized successors")

slow = numeric_adapter(ident="slow-path", preference=9, source_level=1, target_level=1,
                       current_risk=0.2, risk_delta=0.05, proposed_dt=1.0, max_admissible_dt=0.25)
r = resolve([slow], "slow-path")
check("dynamic_horizon_reduces_step", r,
      lambda x: x["effective_dt"] == 0.25 and "SLOWDOWN" in x["effects"] and x["effective_transition_revalidated"],
      "reduce proposed horizon only with successful effective-transition revalidation")

fold = numeric_adapter(ident="folded", preference=2, source_level=2, target_level=1, current_risk=0.2, risk_delta=0.1)
r = resolve([fold], "folded")
check("representation_order_yields_fold_observation", r,
      lambda x: "FOLD" in x["effects"], "numeric representation comparator yields FOLD")
unfold = numeric_adapter(ident="expanded", preference=2, source_level=0, target_level=1, current_risk=0.1, risk_delta=0.1)
r = resolve([unfold], "expanded")
check("representation_order_yields_unfold_observation", r,
      lambda x: "UNFOLD" in x["effects"], "numeric representation comparator yields UNFOLD")

blocked = numeric_adapter(ident="blocked", preference=99, source_level=2, target_level=2,
                          current_risk=0.80, risk_delta=0.10)
r = resolve([blocked], "blocked")
check("no_admissible_successor_terminates", r,
      lambda x: x["effects"] == ["TERMINATE"] and not x["activated"],
      "no exception when all known successors violate the numeric toy constraint")

r = resolve([C("dormant", 9, ok=True, cap=True, auth=False)], "dormant")
check("validity_does_not_imply_activation", r,
      lambda x: "HOLD_DORMANT" in x["effects"] and not x["activated"] and x["feasible_ids"] == ["dormant"],
      "valid transition remains dormant without activation authorization")

# Symbolic adapter: evidence status determines admissibility; a partial order
# supplies representation direction. No numeric semantic coordinates are used.
lower_pairs = {("symbolic-blue", "expanded-root"), ("renamed-y", "renamed-root")}
b1 = [
    symbolic_adapter(ident="symbolic-red", preference=100, source="expanded-root", target="symbolic-red",
                    lower_pairs=lower_pairs, evidence_status="REJECTED"),
    symbolic_adapter(ident="symbolic-blue", preference=3, source="expanded-root", target="symbolic-blue",
                    lower_pairs=lower_pairs, evidence_status="VERIFIED"),
]
r_b = resolve(b1, "symbolic-red")
check("symbolic_adapter_uses_same_kernel", r_b,
      lambda x: x["selected_id"] == "symbolic-blue" and "REDIRECT" in x["effects"] and "FOLD" in x["effects"],
      "same generic kernel handles symbolic evidence plus partial-order relations")

b2 = [
    symbolic_adapter(ident="renamed-x", preference=100, source="renamed-root", target="renamed-x",
                    lower_pairs=lower_pairs, evidence_status="REJECTED"),
    symbolic_adapter(ident="renamed-y", preference=3, source="renamed-root", target="renamed-y",
                    lower_pairs=lower_pairs, evidence_status="VERIFIED"),
]
r_b2 = resolve(b2, "renamed-x")
check("irrelevant_symbol_renaming_invariance", r_b2,
      lambda x: x["effects"] == r_b["effects"] and x["activated"] == r_b["activated"] and x["effective_dt"] == r_b["effective_dt"],
      "renaming symbolic identifiers without changing relations preserves behavior")

revalidation_fail = numeric_adapter(ident="shortened-but-invalid", preference=100, source_level=1, target_level=1,
                                    current_risk=0.2, risk_delta=0.05, proposed_dt=1.0, max_admissible_dt=0.2,
                                    effective_revalidation_pass=False)
r = resolve([revalidation_fail], "shortened-but-invalid")
check("failed_effective_revalidation_blocks_activation", r,
      lambda x: "HOLD_REVALIDATION" in x["effects"] and not x["activated"],
      "a shortened proposal is not activated when effective-transition revalidation fails")

unknown = symbolic_adapter(ident="black-swan-unknown", preference=100, source="unknown-root", target="novel-state",
                           lower_pairs=set(), evidence_status="UNKNOWN")
r = resolve([unknown], "black-swan-unknown")
check("unknown_candidate_fails_closed_without_false_termination", r,
      lambda x: "HOLD_UNRESOLVED" in x["effects"] and not x["activated"] and "TERMINATE" not in x["effects"],
      "unknown candidate cannot activate and is not misreported as proven impossibility")


# Equal best-score alternatives must not be resolved by lexicographic IDs.
tied = [
    C("alpha", 5, ok=True),
    C("zeta", 5, ok=True),
    C("invalid-proposal", 99, ok=False),
]
r = resolve(tied, "invalid-proposal")
check("equal_preference_tie_preserves_freedom", r,
      lambda x: x["selected_id"] is None and not x["activated"] and set(x["branch_ids"]) == {"alpha", "zeta"} and "BRANCH" in x["effects"],
      "equal valid alternatives are preserved without arbitrary identifier-based selection or activation")

r = resolve([C("missing-capability", 50, ok=True, cap=False, auth=True)], "missing-capability")
check("capability_absence_blocks_activation", r,
      lambda x: not x["activated"] and "HOLD_DORMANT" in x["effects"],
      "admissibility cannot grant a missing capability")

summary = {
    "experiment_id": "EXP-003",
    "name": "Structured Transition Contract Across Numeric and Symbolic Adapters",
    "implementation": "shared deterministic toy kernel with numeric/risk and symbolic/evidence partial-order adapters; no real MCTS/UCT",
    "checks_total": len(checks), "checks_passed": sum(c["pass"] for c in checks),
    "all_checks_pass": all(c["pass"] for c in checks), "checks": checks,
    "interpretation": "Passing supports interface consistency for the constructed cases only. It does not prove a universal or dimension-independent law, minimality of the contract, or soundness of arbitrary domain adapters.",
    "known_limitations": [
        "The hard-constraint and effective-revalidation results are supplied by domain adapters; correctness of those facts is not proved by the kernel.",
        "The dynamic horizon is a toy bound, not an empirically calibrated time-evolution model.",
        "No actual MCTS/UCT, formal proof, empirical workload, or external validation is included."
    ]
}
print(json.dumps(summary, indent=2))
if not summary["all_checks_pass"]:
    raise SystemExit(1)