---
name: SK-SWARM
description: >-
  REAL SWARM peer protocol for Functional Epic/Story workflows. Use when acting
  as a swarm specialist peer: shared state, handoffs, anti-thrash, default roster.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)


# SK-SWARM — Swarm Peer Protocol

## When to use
Every specialist agent in Current State or Target State phase.

## Checklist (must satisfy)
1. **ACTIVE_ROOT** — Manager/Orchestrator creates it once (`prefer src`). All peers read `WORKSPACE_ROOT/active_root.txt` and write **only** under that root. Never create `src/src` or a second root. Obey `active-root-hygiene`.
2. **Shared working memory** — read/write every turn:
   - `ACTIVE_ROOT/_internal/swarm/swarm_state.json`
   - `ACTIVE_ROOT/_internal/swarm/handoffs.jsonl`
   - `ACTIVE_ROOT/_internal/swarm/context_memory.md`
3. **Autonomous handoffs** — emit `swarm_handoff` every turn
4. **No boss waiting** — you decide next peer(s) from gaps + eligibility
5. **Default roster** — only peers in `run_plan.agents.run`; never call `agents.skip`
6. **Collective context** — load checkpoint before acting; update after acting

## Anti-thrash caps
- Max 8 handoff hops without new `artifacts_index` entries → hand to Quality Reviewer / Traceability Validator or `join_complete`
- No self-handoff loops without `checkpoint.seq` increment and new files
- `fan_out` only for independent specialties

## swarm_state.json shape
```json
{
  "swarm_id": "<run id>",
  "phase": "CurrentState|TargetState|Master",
  "mode": "CREATE|UPDATE",
  "active_root": "<ACTIVE_ROOT>",
  "run_plan_path": "ACTIVE_ROOT/_internal/run_plan.json",
  "roster": {"eligible": [], "completed": [], "in_flight": [], "blocked": []},
  "artifacts_index": [{"agent": "", "paths": [], "status": "PASS|FAIL|HANDED_OFF"}],
  "shared_context": {
    "open_questions": [],
    "decisions": [],
    "capabilities": [],
    "last_handoff": null
  },
  "checkpoint": {"seq": 0, "updated_by": "", "updated_at": ""}
}
```

## Required handoff envelope
```yaml
swarm_handoff:
  action: continue | handoff | fan_out | join_complete | need_user | stop_fail
  to: ["Exact Agent Label", "..."]
  reason: "why these peers"
  context_keys: ["paths or shared_context keys peers must read"]
  checkpoint_seq: <int>
```

### Semantics
- `handoff` — one primary next peer
- `fan_out` — parallel independent peers
- `join_complete` — phase can close (or after quality/trace)
- `need_user` — rare; only when inputs insufficient

## Turn procedure
1. Resolve WORKSPACE_ROOT (dir with `.agents/` / `active_root.txt`). If cwd is already `…/src`, do **not** append another `src`.
2. Read ACTIVE_ROOT from `active_root.txt` (must exist — Manager creates it). Fail if missing or if path contains `src/src`.
3. Read `run_plan.json`, swarm_state, handoffs tail, context_memory
4. Do your specialty work; write JSON/MD SoR **only** under `ACTIVE_ROOT/artifacts/` (never outside ACTIVE_ROOT)
5. Update swarm_state + append handoffs.jsonl + refresh context_memory
6. Emit `swarm_handoff`

## Tone
Enterprise artifacts only.
- **JSON** = system of record
- **Markdown** = required human projection (epics/stories must emit both)
- Prefer tables, ID-linked refs, Given/When/Then, checklists — no narrative filler
