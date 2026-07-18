"""Symbol registry — the single source of truth for element names.

The problem this solves: the Architect Agent generates artifacts through many
independent, stateless LLM calls (batch=1, `memory_policy: "none"`). A component
named in `interfaces.md` must be the *identical* identifier in `allocations.md`
and in `model.sysml`. Independent calls will not agree on naming by themselves,
and unlike duplicate detection this cannot be recovered after the fact by a
reranker — there is nothing to compare against once divergent names are written.

So names are never left to the model. A name is *minted* once, deterministically,
by this registry; every later prompt receives the authoritative names as input and
is instructed to use them verbatim.

The registry is plain Python. It holds no model state and makes no LLM calls.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field, asdict
from enum import Enum
from pathlib import Path


class Kind(str, Enum):
    """SysML v2 construct a symbol maps to. Mirrors the classification taxonomy
    in implementation.md §2.1.1 — a kind exists because it renders differently."""

    PART_DEF = "part def"
    PART_USAGE = "part"
    ACTION_DEF = "action def"
    ACTION_USAGE = "action"
    PORT_DEF = "port def"
    INTERFACE_DEF = "interface def"
    STATE_DEF = "state def"
    CONSTRAINT_DEF = "constraint def"
    ATTRIBUTE = "attribute"


#: SysML v2 reserved words that cannot be used as identifiers. Learned the hard
#: way: `attribute state : String` fails with "no viable alternative at input
#: 'state'". This list is deliberately conservative — a false positive costs a
#: suffixed name, a false negative costs a failed build at the Step 5 gate.
RESERVED = frozenset({
    "about", "abstract", "accept", "action", "actor", "after", "alias", "all",
    "allocate", "allocation", "analysis", "and", "as", "assert", "assign", "assoc",
    "assume", "at", "attribute", "bind", "binding", "by", "calc", "case", "comment",
    "concern", "connect", "connection", "constraint", "decide", "def", "default",
    "defined", "dependency", "derived", "do", "doc", "else", "end", "entry", "enum",
    "event", "exhibit", "exit", "expose", "false", "filter", "first", "flow", "for",
    "fork", "frame", "from", "hastype", "if", "implies", "import", "in", "include",
    "individual", "inout", "interface", "istype", "item", "join", "language",
    "library", "locale", "loop", "merge", "message", "meta", "metadata", "nonunique",
    "not", "null", "objective", "occurrence", "of", "or", "ordered", "out", "package",
    "parallel", "part", "perform", "port", "private", "protected", "public", "redefines",
    "ref", "references", "render", "rendering", "rep", "require", "requirement",
    "return", "satisfy", "send", "snapshot", "specializes", "stakeholder", "standard",
    "state", "subject", "subsets", "succession", "then", "timeslice", "to", "transition",
    "true", "until", "use", "variant", "variation", "verification", "verify", "via",
    "view", "viewpoint", "when", "while", "xor",
})

_NON_ALNUM = re.compile(r"[^0-9a-zA-Z]+")


class SymbolError(RuntimeError):
    """Raised on a naming conflict the registry cannot resolve silently."""


@dataclass
class Symbol:
    """One named element. `name` is authoritative and never regenerated."""

    name: str
    kind: Kind
    #: req_ids this symbol was minted for. Multiple requirements can drive one
    #: element; all of them are retained for the ADD traceability section.
    req_ids: list[str] = field(default_factory=list)
    #: Free-text intent, carried into prompts so the model knows what the name means.
    description: str = ""
    #: Owning symbol name, for nested usages (a part inside a part).
    parent: str | None = None
    #: Normalised intent this symbol was minted from. Persisted because the
    #: intent→name index cannot be rebuilt from the name alone: minting is
    #: lossy ("gpu clusters" → "GPUCluster"). Without it, a reloaded registry
    #: forks a duplicate on the next equivalent mint.
    intent_key: str = ""

    def to_dict(self) -> dict:
        d = asdict(self)
        d["kind"] = self.kind.value
        return d


def _pascal(raw: str) -> str:
    """'GPU cluster manager' -> 'GPUClusterManager'. Preserves existing internal
    capitalisation so acronyms survive: 'GPU' does not become 'Gpu'."""
    parts = [p for p in _NON_ALNUM.split(raw) if p]
    out = []
    for p in parts:
        out.append(p if (p.isupper() or (p[:1].isupper() and any(c.isupper() for c in p[1:])))
                   else p[:1].upper() + p[1:])
    return "".join(out) or "Unnamed"


def _camel(raw: str) -> str:
    """'GPU cluster' -> 'gpuCluster'. Leading acronym is lowercased whole, so we
    get 'gpuCluster' rather than the unreadable 'gPUCluster'."""
    p = _pascal(raw)
    m = re.match(r"^([A-Z]+)(?=[A-Z][a-z]|$)", p)
    if m:
        return m.group(1).lower() + p[m.end():]
    return p[:1].lower() + p[1:]


#: Definitions are PascalCase, usages camelCase — matching the SysML v2 standard
#: library's own convention and the examples in implementation.md §2.3.
_STYLE = {
    Kind.PART_DEF: _pascal, Kind.ACTION_DEF: _pascal, Kind.PORT_DEF: _pascal,
    Kind.INTERFACE_DEF: _pascal, Kind.STATE_DEF: _pascal, Kind.CONSTRAINT_DEF: _pascal,
    Kind.PART_USAGE: _camel, Kind.ACTION_USAGE: _camel, Kind.ATTRIBUTE: _camel,
}


class SymbolRegistry:
    """Mints and stores element names. Deterministic: the same inputs in the same
    order always produce the same names, so a rerun diffs cleanly."""

    def __init__(self) -> None:
        self._symbols: dict[str, Symbol] = {}
        #: Maps (kind, intent) -> name so asking twice for the same thing returns
        #: the same symbol rather than minting a near-duplicate.
        self._by_intent: dict[tuple[str, str], str] = {}

    # -- minting ---------------------------------------------------------------

    def mint(self, intent: str, kind: Kind, req_id: str | None = None,
             description: str = "", parent: str | None = None) -> Symbol:
        """Return the symbol for `intent`, creating it if new.

        `intent` is the natural-language concept ("GPU cluster"), not a name. The
        registry owns the transformation to an identifier so that two callers who
        describe the same concept converge on one symbol.
        """
        key = (kind.value, self._normalise_intent(intent))
        if key in self._by_intent:
            sym = self._symbols[self._by_intent[key]]
            if req_id and req_id not in sym.req_ids:
                sym.req_ids.append(req_id)
            if description and not sym.description:
                sym.description = description
            return sym

        name = self._unique(_STYLE[kind](intent))
        sym = Symbol(name=name, kind=kind, description=description, parent=parent,
                     req_ids=[req_id] if req_id else [], intent_key=key[1])
        self._symbols[name] = sym
        self._by_intent[key] = name
        return sym

    @staticmethod
    def _normalise_intent(intent: str) -> str:
        """'GPU Cluster', 'gpu cluster', 'GPU  clusters' all collapse to one key.
        Crude singularisation only — 'ies'/'s' — because over-eager stemming would
        merge genuinely distinct concepts, which is the worse failure."""
        # Split camelCase/PascalCase first. Agents are inconsistent about this:
        # one stage returns "enforce per user GPU quota", another returns the same
        # concept as "EnforcePerUserGPUQuota". Without splitting, the second has no
        # word boundaries and mints a duplicate symbol — observed in a real run.
        # The two alternatives handle acronym runs ("GPUQuota" -> "GPU Quota") and
        # ordinary boundaries ("perUser" -> "per User").
        spaced = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])|(?<=[a-z0-9])(?=[A-Z])", " ", intent)
        s = _NON_ALNUM.sub(" ", spaced).strip().lower()
        words = []
        for w in s.split():
            if len(w) > 3 and w.endswith("ies"):
                w = w[:-3] + "y"
            elif len(w) > 3 and w.endswith("s") and not w.endswith("ss"):
                w = w[:-1]
            words.append(w)
        return " ".join(words)

    def _unique(self, base: str) -> str:
        """Avoid reserved words and collisions. A reserved word gets a kind-neutral
        suffix rather than a rename, so the intent stays legible."""
        cand = base
        if cand.lower() in RESERVED:
            cand = base + "Element"
        if cand not in self._symbols:
            return cand
        n = 2
        while f"{cand}{n}" in self._symbols:
            n += 1
        return f"{cand}{n}"

    # -- lookup ----------------------------------------------------------------

    def get(self, name: str) -> Symbol | None:
        return self._symbols.get(name)

    def names(self, kind: Kind | None = None) -> list[str]:
        return sorted(n for n, s in self._symbols.items() if kind is None or s.kind == kind)

    def __len__(self) -> int:
        return len(self._symbols)

    def __contains__(self, name: object) -> bool:
        return name in self._symbols

    # -- prompt surface --------------------------------------------------------

    def as_prompt_block(self, kinds: list[Kind] | None = None, limit: int | None = None) -> str:
        """Render the authoritative names for injection into a generation prompt.

        This is the mechanism that keeps stateless calls consistent: every prompt
        after the logical-architecture stage carries this block and is told to use
        these identifiers verbatim, inventing none.
        """
        syms = [s for s in self._symbols.values() if kinds is None or s.kind in kinds]
        syms.sort(key=lambda s: (s.kind.value, s.name))
        if limit is not None and len(syms) > limit:
            # Truncation is visible, never silent — an unbounded block is the
            # documented overflow path (see implementation.md §5.1).
            shown, dropped = syms[:limit], len(syms) - limit
            body = "\n".join(f"- {s.kind.value} {s.name}"
                             + (f" — {s.description}" if s.description else "")
                             for s in shown)
            return body + f"\n- ... and {dropped} more (truncated)"
        return "\n".join(f"- {s.kind.value} {s.name}"
                         + (f" — {s.description}" if s.description else "")
                         for s in syms)

    # -- persistence -----------------------------------------------------------

    def to_json(self) -> str:
        return json.dumps({"symbols": [s.to_dict() for s in
                                       sorted(self._symbols.values(), key=lambda s: s.name)]},
                          indent=2)

    def save(self, path: str | Path) -> None:
        Path(path).write_text(self.to_json())

    @classmethod
    def load(cls, path: str | Path) -> "SymbolRegistry":
        reg = cls()
        data = json.loads(Path(path).read_text())
        for d in data["symbols"]:
            sym = Symbol(name=d["name"], kind=Kind(d["kind"]), req_ids=d.get("req_ids", []),
                         description=d.get("description", ""), parent=d.get("parent"),
                         intent_key=d.get("intent_key", ""))
            reg._symbols[sym.name] = sym
            if sym.intent_key:
                reg._by_intent[(sym.kind.value, sym.intent_key)] = sym.name
        return reg

    # -- verification ----------------------------------------------------------

    def validate_text(self, text: str, kinds: list[Kind] | None = None) -> list[str]:
        """Return registry names that `text` fails to use — i.e. elements the model
        was told about but silently renamed or dropped. Used to catch drift before
        the artifact is written."""
        return [n for n in self.names() if
                (kinds is None or self._symbols[n].kind in kinds) and
                not re.search(rf"\b{re.escape(n)}\b", text)]
