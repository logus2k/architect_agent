"""Semantic review — judge first, escalate to a human when unresolved.

The Step 5 validator proves the model *parses and resolves*. It cannot tell you the
model says the wrong thing. A constraint asserting `requested > quota` for a rule
that should reject over-quota requests is perfectly valid SysML and precisely
backwards; that case was observed in a real run.

So generated elements that carry logic are judged against their source requirement.
The judge is not a gate — it is a triage step. Anything it flags `wrong`, or cannot
decide, is escalated for human sign-off rather than silently accepted or silently
discarded.
"""

from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field

from .client import AgentClient, LLMError
from .generate import WORKERS, Requirement, StageOutput

JUDGE_AGENT = "architect_judge"

#: Only elements whose meaning can be *wrong* are worth judging. A part definition
#: is a naming choice; a constraint expression is a claim that can be inverted.
JUDGEABLE = ("constraint", "allocation", "behavior")


@dataclass
class Verdict:
    element: str
    req_id: str
    kind: str
    verdict: str          # ok | wrong | uncertain
    reason: str = ""
    suggested_fix: str | None = None

    @property
    def needs_human(self) -> bool:
        """`wrong` is a defect; `uncertain` means the judge abstained. Both reach a
        human — treating abstention as approval is how a review step becomes
        decorative."""
        return self.verdict in ("wrong", "uncertain")

    def as_open_issue(self) -> str:
        label = "DEFECT" if self.verdict == "wrong" else "NEEDS REVIEW"
        fix = f" Suggested: {self.suggested_fix}" if self.suggested_fix else ""
        return f"[{label}] {self.kind} {self.element} ({self.req_id}): {self.reason}{fix}"


def _req_text(reqs: list[Requirement], req_id: str) -> str:
    for r in reqs:
        if r.req_id == req_id:
            return r.text
    return ""


def _claims(constraints_out: StageOutput, allocs_out: StageOutput,
            behavior_out: StageOutput | None) -> list[tuple[str, str, str, str]]:
    """Flatten the judgeable elements into (kind, element, req_id, rendering)."""
    items: list[tuple[str, str, str, str]] = []
    for rec in constraints_out.records:
        expr = rec.get("expression") or "(no expression)"
        items.append(("constraint", rec["name"], rec["req_id"],
                      f"constraint {rec['name']}: {expr}"))
    for rec in allocs_out.records:
        items.append(("allocation", f"{rec['function']}->{rec['component']}", rec["req_id"],
                      f"function {rec['function']} is performed by component {rec['component']}"))
    for rec in (behavior_out.records if behavior_out else []):
        trs = "; ".join(f"{t['from']} then {t['to']}" for t in rec.get("transitions") or [])
        items.append(("behavior", rec["name"], rec["req_id"],
                      f"state machine {rec['name']} states=[{', '.join(rec.get('states') or [])}] "
                      f"transitions=[{trs}]"))
    return items


def review(reqs: list[Requirement], *, constraints_out: StageOutput,
           allocs_out: StageOutput, behavior_out: StageOutput | None,
           client: AgentClient, workers: int = WORKERS) -> list[Verdict]:
    """Judge every logic-bearing element. Never raises on a judgement — a judge
    that fails is itself escalated, not silently skipped."""
    items = _claims(constraints_out, allocs_out, behavior_out)
    if not items:
        return []

    def one(item) -> Verdict:
        kind, element, req_id, rendering = item
        payload = json.dumps({
            "requirement": _req_text(reqs, req_id),
            "req_id": req_id,
            "generated_element": rendering,
            "element_kind": kind,
        })
        try:
            data = client.complete_json(JUDGE_AGENT, payload)
        except LLMError as e:
            # An unavailable judge must not read as approval.
            return Verdict(element=element, req_id=req_id, kind=kind,
                           verdict="uncertain",
                           reason=f"judge unavailable: {e}")
        verdict = str(data.get("verdict", "uncertain")).lower()
        if verdict not in ("ok", "wrong", "uncertain"):
            verdict = "uncertain"
        return Verdict(element=element, req_id=req_id, kind=kind, verdict=verdict,
                       reason=str(data.get("reason", "")),
                       suggested_fix=data.get("suggested_fix") or None)

    with ThreadPoolExecutor(max_workers=workers) as ex:
        return list(ex.map(one, items))


def escalations(verdicts: list[Verdict]) -> list[str]:
    """Open-issue lines for everything a human must look at."""
    return [v.as_open_issue() for v in verdicts if v.needs_human]


def summary(verdicts: list[Verdict]) -> dict[str, int]:
    out = {"ok": 0, "wrong": 0, "uncertain": 0}
    for v in verdicts:
        out[v.verdict] = out.get(v.verdict, 0) + 1
    return out
