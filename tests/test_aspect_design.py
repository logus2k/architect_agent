"""aspect_design + refine tests — GPU-free via a mock AgentClient."""
from architect_agent import aspect_design, refine, critique
from architect_agent.aspect_design import AspectDesign


class MockClient:
    """Returns canned JSON per agent. `designs` maps branch->design dict; `owner` is the
    adjudicator's answer."""
    def __init__(self, designs, owner=None):
        self._designs = designs
        self._owner = owner
    def complete_json(self, agent, content):
        import json
        payload = json.loads(content)
        if agent == aspect_design.DESIGNER_AGENT:
            return self._designs[payload["branch"]]
        if agent == refine.ADJUDICATOR_AGENT:
            return {"owner": self._owner, "reason": "test"}
        return {}


PACKAGE = {
    "manifest": {"project_id": "P1"},
    "requirements": [{"req_id": "R1", "text": "a"}, {"req_id": "R2", "text": "b"}],
    "glossary": [{"name": "Order", "definition": "an order"}],
    "tags": [{"name": "payment"}],
    "tree": {"branches": [{"name": "Sales", "scope": "s", "req_ids": ["R1"]},
                          {"name": "Fulfilment", "scope": "f", "req_ids": ["R2"]}],
             "nodes": [{"req_id": "R1", "branch": "Sales", "tags": ["payment"]},
                       {"req_id": "R2", "branch": "Fulfilment", "tags": []}]},
}


def test_design_branch_parses_and_adapts():
    designs = {"Sales": {"components": [{"name": "Order"}], "functions": [{"name": "PlaceOrder"}],
                         "interfaces": [{"name": "SalesInterface"}], "consumes": [{"concern": "payment"}]},
               "Fulfilment": {"components": [], "functions": [], "interfaces": [], "consumes": []}}
    c = MockClient(designs)
    out = aspect_design.design_aspects(PACKAGE, c)
    assert {d.branch for d in out} == {"Sales", "Fulfilment"}
    sales = next(d for d in out if d.branch == "Sales")
    assert aspect_design.interfaces_by_aspect(out)["Sales"] == ["SalesInterface"]
    assert aspect_design.consumes_by_aspect(out)["Sales"] == ["payment"]


def test_refine_reconciles_ownership():
    """Both aspects claim 'Order'; the adjudicator picks Sales; Fulfilment must drop it and
    consume it instead, leaving zero ownership violations."""
    designs = {"Sales": {"components": [{"name": "Order"}], "functions": [], "interfaces": [], "consumes": []},
               "Fulfilment": {"components": [{"name": "Order"}], "functions": [], "interfaces": [], "consumes": []}}
    c = MockClient(designs, owner="Sales")
    res = refine.refine(PACKAGE, c, max_rounds=2)
    cb = aspect_design.components_by_aspect(res.designs)
    owners = [a for a, cs in cb.items() if "Order" in cs]
    assert owners == ["Sales"]
    ful = next(d for d in res.designs if d.branch == "Fulfilment")
    assert any(x.get("concern") == "Order" for x in ful.consumes)
    assert res.critique.clean


def test_misassignment_check_runs():
    """Exercise the previously-untested check: a node tagged with a concern owned elsewhere."""
    nodes = [{"req_id": "R1", "branch": "Reservations", "tags": ["authentication"]}]
    findings = critique.misassignment(nodes, {"authentication": "User & Access Control"})
    assert findings and findings[0].kind == "cross_cutting_placement"
    assert findings[0].severity == "warning"
    # a node in its own concern's branch is fine
    assert critique.misassignment([{"req_id": "R2", "branch": "User & Access Control",
                                    "tags": ["authentication"]}],
                                  {"authentication": "User & Access Control"}) == []
