"""Aspect handover tests — GPU-free, fixture-based."""
from architect_agent.aspect_design import AspectDesign
from architect_agent import aspect_handover, mermaid


def _designs():
    return [
        AspectDesign(branch="User & Access Control", scope="auth",
                     components=[{"name": "User", "attributes": [{"name": "email", "type": "String"}]}],
                     interfaces=[{"name": "AuthenticationInterface"}],
                     functions=[{"name": "RegisterUser"}],
                     consumes=[{"concern": "security"}]),
        AspectDesign(branch="Reservations", scope="booking",
                     components=[{"name": "Reservation"}],
                     interfaces=[{"name": "ReservationInterface"}],
                     consumes=[{"concern": "authentication", "why": "owned by User & Access Control"}]),
    ]


PACKAGE = {
    "manifest": {"project_id": "P1", "project_name": "Demo", "architect_ready": True},
    "requirements": [{"req_id": "R1", "text": "..."}, {"req_id": "R2", "text": "..."}],
    "tree": {"nodes": [{"req_id": "R1", "branch": "User & Access Control", "tags": ["authentication"]},
                       {"req_id": "R2", "branch": "Reservations", "tags": ["authentication"]}]},
}


def test_handover_is_aspect_structured_and_req_keyed():
    doc = aspect_handover.build(_designs(), package=PACKAGE)
    assert doc["contract_version"] == "2.0"
    # by_aspect present
    assert "User & Access Control" in doc["by_aspect"]
    assert doc["by_aspect"]["User & Access Control"]["interfaces"][0]["name"] == "AuthenticationInterface"
    # STILL keyed by req_id so the Planner joins unchanged
    assert "R1" in doc["by_requirement"]
    assert doc["by_requirement"]["R1"]["aspect"] == "User & Access Control"
    assert "AuthenticationInterface" in doc["by_requirement"]["R1"]["interfaces"]


def test_components_global_carry_owner_and_module():
    doc = aspect_handover.build(_designs(), package=PACKAGE)
    user = next(c for c in doc["components"] if c["name"] == "User")
    assert user["owner_aspect"] == "User & Access Control"
    assert user["suggested_module"] == "user"


def test_open_issues_propagate():
    doc = aspect_handover.build(_designs(), package=PACKAGE, open_issues=["something for a human"])
    assert doc["open_issues"] == ["something for a human"]


def test_mermaid_emits_one_per_aspect_plus_overview():
    out = mermaid.emit_all(_designs())
    assert "_system_overview.mmd" in out
    assert any("User" in k or "Access" in k for k in out)
    # aspect diagram mentions its interface; overview links consumer->owner
    assert "AuthenticationInterface" in out[next(k for k in out if "Access" in k)]
    assert "flowchart" in out["_system_overview.mmd"]
