---
name: tsa-swarm-shared-memory
description: Shared-memory protocol for TSA Orchestrator swarm so parallel specialists sync intake, artifacts, and migration state. Use for Manager bootstrap and every TSA subagent turn.
---

# TSA Swarm Shared Memory

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Paths

```text
ACTIVE_ROOT/
  artifacts/                 # accepted TSA specialist JSON
  quality_gate_reports/
  tsa_pack/                  # Assembler output
  _internal/swarm/
    swarm_state.json
    handoffs.jsonl
    context_memory.md
```

## Rules

1. Manager bootstraps ACTIVE_ROOT + swarm files before workers.
2. Every turn: read swarm_state + latest handoffs before acting.
3. Parallel peers sync only via shared memory + accepted artifact paths.
4. Bump `checkpoint.seq` after writes; emit `swarm_handoff.to[]` for dependents.
5. Completeness updates `loop` only — never rewrites specialist content.
