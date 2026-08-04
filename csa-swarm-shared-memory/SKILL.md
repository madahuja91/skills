---
name: csa-swarm-shared-memory
description: Shared-memory protocol for CSA Orchestrator swarm — swarm_state, handoffs, context_memory, and artifact index so parallel specialists sync outputs. Use for Manager bootstrap and every subagent turn.
---

# CSA Swarm Shared Memory

## Schema

Authoritative `swarm_state.json` contract: [`schema.json`](schema.json)

Also maintain `handoffs.jsonl` (append-only JSON lines) and `context_memory.md` (Markdown digest).

## Why

Parallel swarm agents must **not** sync only through chat. They share one on-disk checkpoint so peers and Completeness Validator see the same truth.

## ACTIVE_ROOT layout

Manager bootstraps **exactly one** ACTIVE_ROOT (prefer workspace `src/`). **Never** create nested `src/src` or a second active root. Set `swarm_state.active_root` once. All sequential/parallel subagents write only under that path (see `active-root-hygiene`).

```text
ACTIVE_ROOT/                          # e.g. src/ — single root for the whole swarm
  artifacts/                          # accepted specialist JSON (public machine)
    discovery.json
    domain.json
    architecture.json
    lineage.json
    integration.json
  quality_gate_reports/
  csa_pack/                           # Assembler output (MD + arc42-c4 HTML)
  _internal/
    run_plan.json
    swarm/
      swarm_state.json                # MUST include active_root
      handoffs.jsonl                  # append-only handoff log
      context_memory.md               # short rolling digest
    completeness_validation/          # Completeness Validator only
    agent_execution_log.json
```

Write `active_root.txt` (one relative line) at workspace root when platform expects it.

## swarm_state.json minimum shape

```json
{
  "swarm_id": "<run-id>",
  "pattern": "orchestrator-swarm",
  "manager": "CSA-Architecture-Manager",
  "active_root": "<ACTIVE_ROOT>",
  "run_plan_path": "_internal/run_plan.json",
  "phase": "discover|swarm_parallel|assemble|done",
  "roster": {
    "running": [],
    "accepted": [],
    "failed": [],
    "blocked": []
  },
  "artifacts_index": {
    "discovery": { "path": "artifacts/discovery.json", "status": "pending|accepted|failed", "gate": null },
    "domain": { "path": "artifacts/domain.json", "status": "pending", "gate": null },
    "architecture": { "path": "artifacts/architecture.json", "status": "pending", "gate": null },
    "lineage": { "path": "artifacts/lineage.json", "status": "pending", "gate": null },
    "integration": { "path": "artifacts/integration.json", "status": "pending", "gate": null }
  },
  "shared_context": {
    "codebase_root": "",
    "module_scope": [],
    "stack_signals": [],
    "open_questions": [],
    "decisions": [],
    "id_registry": {}
  },
  "loop": {
    "last_design_agent": "",
    "completeness": "PASS_COMPLETE|FAIL_INCOMPLETE|PENDING",
    "attempt": 1,
    "max_reruns": 2
  },
  "checkpoint": { "seq": 0, "updated_by": "", "updated_at": "" }
}
```

## Every agent turn (mandatory)

1. **Before work:** `read_file` `swarm_state.json`, tail of `handoffs.jsonl`, `context_memory.md`, and `run_plan.json`.
2. **During work:** read peer artifacts listed as `accepted` in `artifacts_index` (never invent IDs that conflict with `shared_context.id_registry`).
3. **After work:** write your artifact path; update `artifacts_index`, `roster`, `shared_context`, bump `checkpoint.seq`, append `handoffs.jsonl`, refresh `context_memory.md`.
4. Emit `swarm_handoff` in the handoff log:

```json
{
  "at": "ISO-8601",
  "from": "<agent>",
  "type": "handoff|fan_out|join_complete|rework",
  "to": ["<next-agent-or-agents>"],
  "proposed_next": "<optional>",
  "artifact_paths": [],
  "notes": ""
}
```

## Parallel swarm sync rules

- After Discover is `accepted`, Manager may **fan_out** BusinessDomain, TechArchitecture, DataLineage, Integration in parallel.
- Parallel peers must:
  - load the same Discover artifact from shared memory
  - register new IDs into `shared_context.id_registry` (DOM-/ENT-/BR-/CMP-/INT-/LIN-)
  - never overwrite another peer’s artifact path
- Manager waits for **join_complete** (all parallel agents accepted or escalated) before Assembler.

## Completeness + shared memory

- Completeness Validator writes only under `_internal/completeness_validation/` and updates `loop.completeness`.
- On `FAIL_INCOMPLETE`: Manager re-invokes **same** owning agent (not a different specialty); do not honor `to[]` until `PASS_COMPLETE`.

## Anti-patterns

- Passing large artifact bodies only in chat
- Private unsynced copies of discovery/domain
- Declaring phase done while `artifacts_index` still pending
- Skipping checkpoint.seq bump
