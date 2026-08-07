---
name: csa6-swarm-shared-memory
description: Shared-memory protocol for CSA Orchestrator swarm — swarm_state, handoffs, context_memory, and artifact index so parallel specialists sync outputs. Use for Manager bootstrap and every subagent turn.
---

# CSA Swarm Shared Memory

## Schema

Authoritative `swarm_state.json` contract: [`schema.json`](schema.json)

Also maintain `handoffs.jsonl` (append-only JSON lines) and `context_memory.md` (Markdown digest).

## Why

Parallel swarm agents must **not** sync only through chat. They share one on-disk checkpoint so peers and Completeness Validator see the same truth.

## HARD: Bootstrap before any worker (blocking)

Manager MUST create these files **before** Discover or any specialist runs. Completeness fails the run if any are missing:

1. `ACTIVE_ROOT/_internal/swarm/swarm_state.json` (full minimum shape below)
2. `ACTIVE_ROOT/_internal/swarm/handoffs.jsonl` (may start empty)
3. `ACTIVE_ROOT/_internal/swarm/context_memory.md` (seed digest)
4. `ACTIVE_ROOT/_internal/run_plan.json`

## HARD: Fast parallel control loop

1. Bootstrap shared memory (above).
2. Discover → Completeness (Discover only). On fail → Manager re-runs Discover (≤2).
3. **Fan-out** Domain + Tech + Lineage + Integration **in parallel**.
4. Completeness per lane as each finishes. On fail → Manager re-runs **that owner** (≤2) using `target_agent_id` + `schema_fields_missing`.
5. On **join_complete**, Completeness FINAL renders lean `csa_pack/` (5 MD + README + arc42 HTML) and self-gates `gate-csa-document`.
6. On FINAL fail naming an owner → Manager re-runs that specialist, then FINAL again.

Do **not** invoke Document Assembler. Do **not** run epic-story readiness.

## ACTIVE_ROOT layout

Manager bootstraps **exactly one** ACTIVE_ROOT — prefer workspace-relative **`src/`**. Set `swarm_state.active_root` once. All agents write **only** under that path.

```text
ACTIVE_ROOT/                          # e.g. src/
  artifacts/                          # specialist JSON SSOT
    discovery.json
    domain.json
    architecture.json
    lineage.json
    integration.json
    quality_gate_reports/
  csa_pack/                           # Completeness FINAL lean pack (5 MD + README + arc42-c4)
  _internal/
    run_plan.json
    swarm/
      swarm_state.json
      handoffs.jsonl
      context_memory.md
    completeness_validation/
    agent_execution_log.json
```

## swarm_state.json minimum shape

```json
{
  "swarm_id": "<run-id>",
  "pattern": "orchestrator-swarm",
  "manager": "CSA-Architecture-Manager",
  "active_root": "<ACTIVE_ROOT>",
  "run_plan_path": "_internal/run_plan.json",
  "phase": "discover|swarm_parallel|final_pack|done",
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

1. **Before work:** read `swarm_state.json`, tail of `handoffs.jsonl`, `context_memory.md`, and `run_plan.json`.
2. **During work:** read peer artifacts listed as `accepted` in `artifacts_index`.
3. **After work:** write your artifact; update `artifacts_index`, `roster`, `shared_context`, bump `checkpoint.seq`, append `handoffs.jsonl`, refresh `context_memory.md`.

## Completeness + shared memory

- Completeness writes under `_internal/completeness_validation/` and updates `loop.completeness`.
- On `FAIL_INCOMPLETE`: Manager re-invokes the **same** owning agent named in `target_agent_id` (not a different specialty).
- Phase `final_pack` = Completeness FINAL render + gate. Phase `done` only after required pack files exist on disk.
