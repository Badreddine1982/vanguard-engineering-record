"""EXP-002: falsification check for a bare admissibility relation.
Standard library only. Tests whether admissible-edge information alone can
uniquely determine slowdown/fold/unfold outcomes without extra relations.
"""
from dataclasses import dataclass
import json

@dataclass(frozen=True)
class GraphView:
    # The only information exposed to the bare resolver.
    states: tuple[str, ...]
    admissible_edges: tuple[tuple[str, str], ...]
    proposed_edge: tuple[str, str] | None


def bare_relation_signature(view: GraphView):
    """What a resolver sees if given only admissibility and proposal relations."""
    return (view.states, view.admissible_edges, view.proposed_edge)

# Pair A: identical admissibility graph, different representation ordering.
graph_A = GraphView(("s", "t"), (("s", "t"),), ("s", "t"))
representation_A = {"s": 2, "t": 1}  # target is a lower representation level: FOLD
representation_B = {"s": 0, "t": 1}  # target is a higher representation level: UNFOLD

# Pair B: identical admissibility graph, different dynamic/temporal margin.
graph_B1 = GraphView(("s", "t"), (("s", "t"),), ("s", "t"))
graph_B2 = GraphView(("s", "t"), (("s", "t"),), ("s", "t"))
# These values are not part of GraphView and therefore are invisible to the bare resolver.
dynamic_margin_B1 = 0.01  # near boundary: slowdown would be appropriate under this declared policy
dynamic_margin_B2 = 0.50  # comfortably inside: continue would be appropriate under this declared policy

same_graph_for_fold_unfold = bare_relation_signature(graph_A) == bare_relation_signature(graph_A)
same_graph_for_slowdown = bare_relation_signature(graph_B1) == bare_relation_signature(graph_B2)

# If signatures are identical but required labels differ, the bare relation underdetermines labels.
results = {
    "experiment_id": "EXP-002",
    "name": "Bare Admissibility Relation Sufficiency Check",
    "method": "Constructed indistinguishability/counterexample pairs",
    "runtime": "Python 3 standard library only",
    "cases": [
        {
            "case": "representation_level_not_encoded",
            "same_bare_relation_signature": same_graph_for_fold_unfold,
            "extra_relation_A": "representation_A[s] > representation_A[t]",
            "expected_mode_A": "FOLD",
            "extra_relation_B": "representation_B[s] < representation_B[t]",
            "expected_mode_B": "UNFOLD",
            "bare_relation_can_distinguish": False,
            "pass": same_graph_for_fold_unfold and representation_A["s"] > representation_A["t"] and representation_B["s"] < representation_B["t"],
        },
        {
            "case": "dynamic_margin_not_encoded",
            "same_bare_relation_signature": same_graph_for_slowdown,
            "extra_relation_A": f"dynamic_margin={dynamic_margin_B1}",
            "expected_mode_A": "SLOWDOWN",
            "extra_relation_B": f"dynamic_margin={dynamic_margin_B2}",
            "expected_mode_B": "CONTINUE",
            "bare_relation_can_distinguish": False,
            "pass": same_graph_for_slowdown and dynamic_margin_B1 < dynamic_margin_B2,
        },
    ],
    "cases_total": 2,
    "cases_passed": 2 if same_graph_for_fold_unfold and same_graph_for_slowdown else 0,
    "all_cases_pass": same_graph_for_fold_unfold and same_graph_for_slowdown,
    "finding": "A bare binary admissibility relation over transitions does not uniquely determine all operational modes. Representation ordering is needed to distinguish FOLD from UNFOLD; a dynamic/boundary measure is needed to distinguish SLOWDOWN from CONTINUE.",
    "interpretation": "This is a bounded counterexample to sufficiency of the bare relation, not a refutation of a richer unified transition law. It supports using a structured relational contract without requiring a predefined fixed list of semantic coordinates.",
    "limitations": [
        "Constructed examples only; no empirical workload.",
        "No actual MCTS/UCT implementation.",
        "No proof that the proposed richer relation is minimal or universal.",
        "The dynamic margin values illustrate missing information; they are not calibrated thresholds."
    ]
}
print(json.dumps(results, indent=2))
if not results["all_cases_pass"]:
    raise SystemExit(1)