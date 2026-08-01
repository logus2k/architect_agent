"""Reranker access — semantic sameness for the built-in design critique.

The house rule: "are these two the same?" goes through the reranker, never string
matching. Scores are sigmoid-scaled so a fixed threshold is meaningful (same convention
as the Analyst and noted-rag).
"""

from __future__ import annotations

import math
import os

import httpx

EMBEDDINGS_URL = os.environ.get("EMBEDDINGS_URL", "http://localhost:8601")
RERANK_MODEL = os.environ.get("RERANK_MODEL_NAME", "bge-reranker")


def _sigmoid(x: float) -> float:
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    e = math.exp(x)
    return e / (1.0 + e)


def rerank(query: str, documents: list[str], timeout: float = 60.0) -> list[float]:
    """One 0-1 relevance score per document, in input order (sigmoid of the raw logit)."""
    if not documents:
        return []
    r = httpx.post(f"{EMBEDDINGS_URL}/v1/rerank",
                   json={"model": RERANK_MODEL, "query": query, "documents": documents},
                   timeout=timeout)
    r.raise_for_status()
    results = r.json().get("results") or r.json().get("data") or []
    scored = [0.0] * len(documents)
    for item in results:
        idx = int(item.get("index", 0))
        raw = item.get("relevance_score", item.get("score", 0.0))
        if 0 <= idx < len(scored):
            scored[idx] = _sigmoid(float(raw))
    return scored
