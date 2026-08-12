import json, urllib.request, time, sys

PID = "185d83e85fc84e15ab77796c40e22eb4"
pkg = json.load(open(f"/app/project-repos/{PID}/requirements/package.json"))
branches = pkg.get("tree", {}).get("branches", [])
# pick a moderate branch to design
br = next((b for b in branches if b.get("name") == "Reservations"), branches[0])
by_id = {r["req_id"]: r["text"] for r in pkg.get("requirements", [])}
reqs = [by_id[r] for r in br.get("req_ids", []) if r in by_id]
payload = json.dumps({
    "branch": br["name"], "scope": br.get("scope", ""),
    "requirements": reqs,
    "glossary": [{"name": t["name"], "definition": t.get("definition", ""), "kind": t.get("kind", "entity")}
                 for t in pkg.get("glossary", [])],
    "tags": [t["name"] for t in pkg.get("tags", [])],
})
print(f"=== BRANCH: {br['name']} | {len(reqs)} requirements ===\n")

BASE = "http://localhost:7701/v1/chat/completions"


def design(think):
    body = {"model": "architect_aspect_designer",
            "messages": [{"role": "user", "content": payload}],
            "max_tokens": 64000,
            "chat_template_kwargs": {"enable_thinking": think}}
    t = time.time()
    r = json.load(urllib.request.urlopen(urllib.request.Request(
        BASE, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"}, method="POST"), timeout=300))
    dt = time.time() - t
    c = r["choices"][0]["message"]["content"]
    tok = r.get("usage", {}).get("completion_tokens", "?")
    # strip a think block for the "final answer" view
    ans = c.rsplit("</think>", 1)[1] if "</think>" in c else c
    return dt, tok, ans.strip()


for label, think in [("THINK OFF", False), ("THINK ON", True)]:
    dt, tok, ans = design(think)
    print(f"########## {label}  ({dt:.0f}s, {tok} tokens) ##########")
    print(ans)
    print()
