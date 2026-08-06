---
name: tsa-swarm-shared-memory
description: Shared-memory protocol for TSA Orchestrator swarm so parallel specialists sync intake, artifacts, and migration state. Use for Manager bootstrap and every TSA subagent turn.
---

# TSA Swarm Shared Memory

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Paths

Exactly **one** ACTIVE_ROOT (prefer workspace `src/`). Never create `src/src` or a second root.

```text
ACTIVE_ROOT/   # e.g. src/  — single root for the whole swarm
  artifacts/                 # accepted TSA specialist JSON
  quality_gate_reports/
  tsa_pack/                  # Assembler output (MD + arc42-c4 HTML)
  _internal/swarm/
    swarm_state.json         # MUST include active_root
    handoffs.jsonl
    context_memory.md
```

## Rules

1. Manager bootstraps **one** ACTIVE_ROOT (prefer `src/`) + swarm files; set `swarm_state.active_root`.
2. Every subagent (sequential or parallel) reads `active_root` and writes **only** there on disk.
3. Every turn: read swarm_state + latest handoffs before acting.
4. Parallel peers sync only via shared memory + accepted artifact paths under `active_root`.
5. Bump `checkpoint.seq` after writes; emit `swarm_handoff.to[]` for dependents.
6. Completeness updates `loop` only — never rewrites specialist content; must run `active-root-hygiene` and delete nested/duplicate roots immediately.
7. Deliverables: Markdown pack sections; arc42/C4 as HTML under `tsa_pack/arc42-c4/` only.
8. **HARD disk rule:** Never invent `/app/temp/csa-run` or sibling `outputs/` outside ACTIVE_ROOT. `tsa_pack/` and `artifacts/` must exist on disk under ACTIVE_ROOT.
