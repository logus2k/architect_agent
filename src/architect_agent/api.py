"""Architect HTTP service — mirrors the Analyst's job pattern.

The Architect was a batch job (`aspect_pipeline` CLI). This thin server exposes the same run
as an async job so reqoach can trigger it and poll progress, exactly like the Analyst's
`structure:run`:

  POST /projects/{pid}/architect:run   -> start a run, returns {job_id}
  GET  /jobs/{job_id}                  -> status snapshot (status, stage, progress, error)
  GET  /health

A run: fetch the Analyst package -> per-aspect design + refine -> emit handover + Mermaid
diagrams -> publish into the project repo's architecture/ area and ask reqoach to commit.
Each run executes in a worker thread (the design makes many LLM calls); the JobManager keeps
a snapshot the UI polls. No socket.io — polling is enough and matches the Overview's poller.
"""

from __future__ import annotations

import threading
import time
import uuid
from dataclasses import dataclass, field

from fastapi import FastAPI, HTTPException

from . import aspect_pipeline

__version__ = "0.1.0"


@dataclass
class Job:
    job_id: str
    project_id: str
    status: str = "queued"                 # queued | running | done | error
    stage: str | None = None
    progress: dict = field(default_factory=dict)
    error: str | None = None
    result: dict | None = None
    started_at: float | None = None

    def snapshot(self) -> dict:
        return {"job_id": self.job_id, "project_id": self.project_id, "kind": "architect",
                "status": self.status, "stage": self.stage, "progress": self.progress,
                "error": self.error, "result": self.result,
                "elapsed_s": round(time.time() - self.started_at) if self.started_at else None}


class JobManager:
    """Owns architect jobs; runs each in a worker thread. Polling-only (no socket.io)."""

    def __init__(self) -> None:
        self.jobs: dict[str, Job] = {}

    def _run_architect(self, job: Job) -> None:
        job.status = "running"
        job.started_at = time.time()
        try:
            job.stage = "fetch"
            job.progress = {"stage": "fetch", "status": "progress"}
            package = aspect_pipeline.load_package(job.project_id)

            job.stage = "design"
            job.progress = {"stage": "design", "status": "progress"}
            result = aspect_pipeline.run(package, to_repo=True)

            job.status = "done"
            job.stage = "done"
            job.result = {
                "aspects": len(result.designs),
                "open_issues": len(result.open_issues),
                "refine_rounds": result.rounds,
                "package_dir": str(result.package_dir),
            }
            job.progress = {"stage": "done", "status": "done", **job.result}
        except Exception as e:  # noqa: BLE001 — surface any pipeline failure to the client
            job.status = "error"
            job.error = f"{type(e).__name__}: {e}"

    def create_architect_run(self, pid: str) -> Job:
        job = Job(job_id=uuid.uuid4().hex, project_id=pid)
        self.jobs[job.job_id] = job
        threading.Thread(target=self._run_architect, args=(job,), daemon=True).start()
        return job


api = FastAPI(title="architect-agent", version=__version__)
jm = JobManager()


@api.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "architect-agent", "version": __version__,
            "jobs": len(jm.jobs)}


@api.post("/projects/{pid}/architect:run")
def architect_run(pid: str) -> dict:
    """Start an architecture run for a project. Returns the job id to poll."""
    job = jm.create_architect_run(pid)
    return {"job_id": job.job_id, "project_id": pid, "status": job.status}


@api.get("/jobs/{job_id}")
def job_status(job_id: str) -> dict:
    job = jm.jobs.get(job_id)
    if not job:
        raise HTTPException(404, "unknown job")
    return job.snapshot()
