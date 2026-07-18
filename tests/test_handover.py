"""Planner handover tests — the contract in sdk/how_to.md.

The join key is `req_id`; if that breaks, nothing downstream can attach.
"""

from architect_agent import handover
from architect_agent.generate import Requirement, StageOutput
from architect_agent.judge import Verdict
from architect_agent.symbols import Kind, SymbolRegistry


def _fixture():
    reg = SymbolRegistry()
    svc = reg.mint("matching service", Kind.PART_DEF, req_id="REQ-0013",
                   description="computes match scores")
    reg.mint("matching service", Kind.PART_USAGE, req_id="REQ-0013")
    reg.mint("data management service", Kind.PART_USAGE, req_id="REQ-0013")
    fn = reg.mint("match job seekers to postings", Kind.ACTION_DEF, req_id="REQ-0013")

    logical = StageOutput(records=[{"req_id": "REQ-0013", "def": svc.name,
                                    "usage": "matchingService",
                                    "attributes": [{"name": "matchScore", "type": "Real"}],
                                    "description": "computes match scores"}])
    functions = StageOutput(records=[{"req_id": "REQ-0013", "name": fn.name,
                                      "description": "match"}])
    ifaces = StageOutput(records=[{"req_id": "REQ-0013", "name": "MatchingResultInterface",
                                   "port": "MatchingResultPort", "attributes": [],
                                   "ends": [{"role": "supplier", "element": "matchingService"},
                                            {"role": "consumer", "element": "dataManagementService"}],
                                   "description": "results"}])
    cons = StageOutput(records=[{"req_id": "REQ-0013", "name": "MatchLatency",
                                 "expression": "latencyMs <= 200", "parameters": [],
                                 "category": "performance", "description": "bound"}],
                       unresolved=["REQ-0030: states no measurable bound (C7=2)"])
    allocs = StageOutput(records=[{"req_id": "REQ-0013", "function": fn.name,
                                   "component": svc.name, "rationale": "owner"}])
    reqs = [Requirement(req_id="REQ-0013", text="..."),
            Requirement(req_id="REQ-0030", text="...")]
    return reqs, reg, logical, functions, ifaces, cons, allocs


def _build(**over):
    reqs, reg, logical, functions, ifaces, cons, allocs = _fixture()
    kwargs = dict(reqs=reqs, reg=reg, manifest={"project_id": "P1", "architect_ready": False},
                  logical_out=logical, functions_out=functions, interfaces_out=ifaces,
                  constraints_out=cons, allocs_out=allocs)
    kwargs.update(over)
    return handover.build(**kwargs)


def test_keyed_by_req_id():
    """The join key. The Planner already carries req ids in `traces_to`."""
    doc = _build()
    assert "REQ-0013" in doc["by_requirement"]
    entry = doc["by_requirement"]["REQ-0013"]
    assert entry["components"][0]["name"] == "MatchingService"
    assert entry["functions"][0]["name"] == "MatchJobSeekersToPostings"
    assert entry["constraints"][0]["expression"] == "latencyMs <= 200"
    assert entry["allocations"][0]["component"] == "MatchingService"


def test_component_index_gives_stable_module_names():
    """Kills the .py/.js inconsistency: one name per component, everywhere."""
    doc = _build()
    comp = next(c for c in doc["components"] if c["name"] == "MatchingService")
    assert comp["suggested_module"] == "matching_service"
    assert comp["req_ids"] == ["REQ-0013"]


def test_depends_on_derived_from_interfaces_only():
    doc = _build()
    assert doc["depends_on"] == [{"from": "dataManagementService",
                                  "to": "matchingService",
                                  "via": "MatchingResultInterface"}]


def test_unquantified_constraints_surface_as_open_issues():
    doc = _build()
    kinds = {i["kind"] for i in doc["open_issues"]}
    assert "unquantified_constraint" in kinds
    issue = next(i for i in doc["open_issues"] if i["kind"] == "unquantified_constraint")
    assert issue["req_id"] == "REQ-0030"


def test_judge_defects_reach_the_planner():
    """A semantic defect must not arrive looking clean."""
    doc = _build(verdicts=[
        Verdict(element="UserAccountLifecycle", req_id="REQ-0006", kind="behavior",
                verdict="wrong", reason="transition may be inverted",
                suggested_fix="review transitions"),
        Verdict(element="Fine", req_id="REQ-0001", kind="constraint", verdict="ok"),
    ])
    defects = [i for i in doc["open_issues"] if i["kind"] == "semantic_defect"]
    assert len(defects) == 1
    assert defects[0]["element"] == "UserAccountLifecycle"
    assert not any(i.get("element") == "Fine" for i in doc["open_issues"])


def test_architect_ready_is_mirrored_not_invented():
    doc = _build(manifest={"project_id": "P1", "architect_ready": False,
                           "release_status": "draft"})
    assert doc["source_package"]["architect_ready"] is False
    assert doc["source_package"]["release_status"] == "draft"


def test_requirement_with_no_elements_is_simply_absent():
    doc = _build()
    assert "REQ-0030" not in doc["by_requirement"]
    assert doc["source_package"]["requirements_received"] == 2
    assert doc["source_package"]["requirements_modelled"] == 1


def test_classes_are_published_with_provenance():
    """The Analyst documents `classes[]` as never empty, but packages without a
    `classify:run` carry it empty throughout (386/386 observed, independently
    reported by the Planner). The Architect's fallback fills them, so routing has
    a signal either way — but the source must be visible, because analyst labels
    and our fallback are not equivalent evidence."""
    reqs, reg, logical, functions, ifaces, cons, allocs = _fixture()
    reqs[0].classes = ["functional", "interface"]
    reqs[0].classified_by = "architect"
    reqs[1].classes = ["constraint"]
    reqs[1].classified_by = "analyst"
    doc = handover.build(reqs=reqs, reg=reg, manifest={}, logical_out=logical,
                         functions_out=functions, interfaces_out=ifaces,
                         constraints_out=cons, allocs_out=allocs)
    assert doc["by_requirement"]["REQ-0013"]["classes"] == ["functional", "interface"]
    assert doc["by_requirement"]["REQ-0013"]["classified_by"] == "architect"
    assert doc["by_requirement"]["REQ-0030"]["classified_by"] == "analyst"
    assert doc["classification"] == {"from_analyst": 1, "from_architect_fallback": 1,
                                     "unclassified": 0}
