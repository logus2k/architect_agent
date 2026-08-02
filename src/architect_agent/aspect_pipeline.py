"""The Architect pipeline — per-aspect, no SysML.

    Analyst package -> design per aspect -> built-in refine loop -> emit
                    -> handover (aspect-structured, req_id-keyed) + Mermaid diagrams + artifacts

Replaces the old per-requirement + SysML-jar path. No JVM: diagrams are Mermaid source,
rendered client-side by reqoach. Correctness comes from the built-in critique/refine loop
(reranker near-dup, ownership, consumed-but-unowned), not a SysML validator.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path

from . import aspect_handover, mermaid, refine
from .aspect_design import AspectDesign
from .client import AgentClient

PUBLISH_ROOT = Path(os.environ.get("ARCHITECT_DATA_DIR", "data")) / "architecture"


@dataclass
class Result:
    package_dir: Path
    designs: list[AspectDesign]
    handover: dict
    open_issues: list[str] = field(default_factory=list)
    rounds: int = 0


def _artifacts_md(designs: list[AspectDesign], handover: dict) -> dict[str, str]:
    lines = ["# Architecture — by Aspect\n"]
    for d in designs:
        lines.append(f"## {d.branch}\n\n_{d.scope}_\n")
        lines.append("**Components:** " + (", ".join(c["name"] for c in d.components) or "—"))
        lines.append("\n**Interfaces:** " + (", ".join(i["name"] for i in d.interfaces) or "—"))
        lines.append("\n**Consumes:** " + (", ".join(c.get("concern", "") for c in d.consumes) or "—") + "\n")
    add = "\n".join(lines)
    issues = "# Open Issues\n\n" + ("\n".join(f"- {i}" for i in handover["open_issues"]) or "_None._")
    return {"architecture.md": add, "open_issues.md": issues}


#: When set, the Architect publishes into the per-project git repo instead of its private
#: data dir, and asks reqoach to commit (reqoach owns git — the Architect just writes files).
REPOS_ROOT = os.environ.get("PROJECT_REPOS_ROOT")
REQOACH_URL = os.environ.get("REQOACH_URL", "http://localhost:7802").rstrip("/")


def publish_to_repo(pid: str, out_dir: str | Path, *, repos_root: str | None = None,
                    reqoach_url: str | None = None) -> dict:
    """Copy an architecture output dir into the project repo's `architecture/` area and ask
    reqoach to commit it (reqoach owns git). Returns reqoach's commit result."""
    import shutil
    import httpx
    repos_root = repos_root or REPOS_ROOT
    reqoach_url = (reqoach_url or REQOACH_URL).rstrip("/")
    if not repos_root:
        raise ValueError("PROJECT_REPOS_ROOT is not set — nowhere to publish")
    dest = Path(repos_root) / pid / "architecture"
    dest.mkdir(parents=True, exist_ok=True)
    # Clear prior contents (keep .gitkeep) so renamed/removed artifacts from an earlier run do
    # not linger — the commit then reflects exactly this run's output.
    for item in dest.iterdir():
        if item.name == ".gitkeep":
            continue
        shutil.rmtree(item) if item.is_dir() else item.unlink()
    for item in Path(out_dir).iterdir():
        target = dest / item.name
        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            shutil.copy2(item, target)
    r = httpx.post(f"{reqoach_url}/repos/{pid}/commit",
                   json={"area": "architecture", "agent": "architect",
                         "message": "Architect: publish architecture package"}, timeout=60)
    r.raise_for_status()
    return r.json()


def run(package: dict | str | Path, out_dir: str | Path | None = None,
        client: AgentClient | None = None, to_repo: bool = False) -> Result:
    """Execute the per-aspect pipeline and publish the package. When `to_repo` is set (and
    PROJECT_REPOS_ROOT is configured), also copy the output into the project repo's
    `architecture/` area and ask reqoach to commit it."""
    if not isinstance(package, dict):
        package = json.loads(Path(package).read_text())
    client = client or AgentClient()

    ref = refine.refine(package, client)
    designs = ref.designs

    handover = aspect_handover.build(designs, package=package, open_issues=ref.open_issues)

    pid = package.get("manifest", {}).get("project_id") or "unknown"
    if out_dir:
        out_dir = Path(out_dir)
    elif to_repo:
        # Publish from a FRESH dir so stale files from a previous (e.g. SysML-era) run in
        # PUBLISH_ROOT/<pid> are never copied into the repo.
        import tempfile
        out_dir = Path(tempfile.mkdtemp(prefix=f"arch_{pid[:8]}_"))
    else:
        out_dir = PUBLISH_ROOT / pid
    (out_dir / "diagrams").mkdir(parents=True, exist_ok=True)
    (out_dir / "artifacts").mkdir(parents=True, exist_ok=True)

    aspect_handover.write(handover, out_dir)
    for fname, src in mermaid.emit_all(designs).items():
        (out_dir / "diagrams" / fname).write_text(src)
    for fname, text in _artifacts_md(designs, handover).items():
        (out_dir / "artifacts" / fname).write_text(text)

    if to_repo:
        publish_to_repo(pid, out_dir)

    return Result(package_dir=out_dir, designs=designs, handover=handover,
                  open_issues=ref.open_issues, rounds=ref.rounds)


def export_diagrams(designs, fmt: str = "mermaid") -> dict[str, str]:
    """Export the aspect diagrams in the chosen format. Mermaid is the browser default;
    draw.io is the editable-export alternative. Same design data either way."""
    from . import mermaid, drawio
    if fmt == "drawio":
        return drawio.emit_all(designs)
    if fmt == "mermaid":
        return mermaid.emit_all(designs)
    raise ValueError(f"unknown diagram format: {fmt!r} (mermaid|drawio)")


def load_package(source: str, *, analyst_url: str | None = None) -> dict:
    """Resolve a package from either a local file or the Analyst service.

    `source` is a local `package.json` path if it exists on disk, otherwise it is
    treated as an Analyst project id and fetched from
    `GET {analyst_url}/projects/{source}/package`.
    """
    p = Path(source)
    if p.exists():
        return json.loads(p.read_text())
    import httpx
    base = (analyst_url or os.environ.get("ANALYST_URL", "http://analyst-agent:7803")).rstrip("/")
    r = httpx.get(f"{base}/projects/{source}/package", timeout=120)
    r.raise_for_status()
    return r.json()


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(
        description="Architect (per-aspect): Analyst package -> design+refine -> "
                    "handover 2.0 + Mermaid diagrams. No SysML.")
    ap.add_argument("package",
                    help="local package.json path, OR an Analyst project id to fetch")
    ap.add_argument("-o", "--out", default=None,
                    help="output dir (default: $ARCHITECT_DATA_DIR/architecture/<pid>)")
    ap.add_argument("--analyst-url", default=None,
                    help="Analyst base URL when PACKAGE is a project id "
                         "(default $ANALYST_URL or http://analyst-agent:7803)")
    ap.add_argument("--repo", action="store_true",
                    help="also publish into the project git repo's architecture/ area and ask "
                         "reqoach to commit (needs $PROJECT_REPOS_ROOT + $REQOACH_URL)")
    args = ap.parse_args()

    package = load_package(args.package, analyst_url=args.analyst_url)
    result = run(package, out_dir=args.out, to_repo=args.repo)
    print(f"published: {result.package_dir}")
    print(f"aspects: {len(result.designs)}  refine_rounds: {result.rounds}  "
          f"open_issues: {len(result.open_issues)}")
    for issue in result.open_issues:
        print(f"  - {issue}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
