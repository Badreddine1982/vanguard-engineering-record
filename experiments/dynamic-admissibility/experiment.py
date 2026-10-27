"""Toy experiment for a unified admissibility-aware transition resolver.
Standard-library only. This is a logic/interface consistency test, not real MCTS.
"""
from dataclasses import dataclass, asdict
import json

@dataclass(frozen=True)
class State:
    level: int
    risk: float
    capability: str
    activated: bool = False

@dataclass(frozen=True)
class Action:
    name: str
    target_level: int
    risk_delta: float
    utility: float
    capability: str

# Explicit toy constraint: maximum risk depends on representation level.
def risk_limit(level: int) -> float:
    return {0: 0.30, 1: 0.60, 2: 0.85}.get(level, 0.0)

def admissible(state: State, action: Action) -> bool:
    return (action.target_level in (0, 1, 2)
            and action.capability == state.capability
            and state.risk + action.risk_delta <= risk_limit(action.target_level))

def propose(state: State, actions: list[Action]) -> Action:
    # A deterministic utility preference stands in for a proposal policy; not MCTS/UCT.
    return max(actions, key=lambda a: (a.utility, a.name))

def resolve(state: State, actions: list[Action]) -> dict:
    proposed = propose(state, actions)
    feasible = [a for a in actions if admissible(state, a)]
    proposed_is_feasible = admissible(state, proposed)
    if not feasible:
        mode = "TERMINATE"
        selected = None
    else:
        selected = max(feasible, key=lambda a: (a.utility, a.name))
        redirected = not proposed_is_feasible
        margin = risk_limit(selected.target_level) - (state.risk + selected.risk_delta)
        if redirected:
            mode = "REDIRECT"
        elif len(feasible) > 1:
            mode = "BRANCH"
        elif selected.target_level < state.level:
            mode = "FOLD"
        elif selected.target_level > state.level:
            mode = "UNFOLD"
        elif margin <= 0.05:
            mode = "SLOWDOWN"
        else:
            mode = "CONTINUE"
    # Activation is granted only to the selected admissible transition.
    activated = selected is not None and admissible(state, selected)
    return {
        "mode": mode,
        "proposed_action": proposed.name,
        "proposed_admissible": proposed_is_feasible,
        "feasible_actions": [a.name for a in feasible],
        "selected_action": selected.name if selected else None,
        "activated": activated,
        "validity_separate_from_activation": selected is None or admissible(state, selected),
    }

def run_case(name, state, actions, expected):
    result = resolve(state, actions)
    result["case"] = name
    result["expected_mode"] = expected
    result["pass"] = result["mode"] == expected
    return result

cases = [
    run_case("inadmissible_preference_redirected_to_feasible_alternative",
        State(1, 0.50, "research"),
        [Action("risky_unfold", 2, 0.40, 10, "research"), Action("safe_continue", 1, 0.02, 5, "research")], "REDIRECT"),
    run_case("multiple_feasible_successors_branch",
        State(1, 0.20, "research"),
        [Action("continue_a", 1, 0.05, 5, "research"), Action("continue_b", 1, 0.10, 4, "research")], "BRANCH"),
    run_case("near_boundary_slowdown",
        State(1, 0.50, "research"),
        [Action("near_limit_continue", 1, 0.09, 5, "research")], "SLOWDOWN"),
    run_case("lower_representation_fold",
        State(2, 0.20, "research"),
        [Action("fold", 1, 0.10, 5, "research")], "FOLD"),
    run_case("higher_representation_unfold",
        State(0, 0.10, "research"),
        [Action("unfold", 1, 0.10, 5, "research")], "UNFOLD"),
    run_case("no_admissible_successor_terminate",
        State(2, 0.80, "research"),
        [Action("too_risky", 2, 0.10, 10, "research"), Action("wrong_capability", 1, 0.0, 2, "execute")], "TERMINATE"),
]
summary = {
    "experiment_id": "EXP-001",
    "experiment_name": "Unified State Transition Law — Toy Model",
    "implementation_type": "deterministic toy resolver; not MCTS/UCT",
    "cases_total": len(cases),
    "cases_passed": sum(c["pass"] for c in cases),
    "all_cases_pass": all(c["pass"] for c in cases),
    "results": cases,
    "interpretation": "Passing cases establish only internal consistency for these hand-authored toy rules. They do not establish a dimension-independent mathematical law or general system validity."
}
print(json.dumps(summary, indent=2))
if not summary["all_cases_pass"]:
    raise SystemExit(1)