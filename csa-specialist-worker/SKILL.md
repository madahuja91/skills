---
name: csa-specialist-worker
description: Shared HARD rules for CSA specialist subagents — artifacts-only writes, ACTIVE_ROOT hygiene, schema floors, swarm sync. Use on Discover/Domain/Tech/Lineage/Integration. Do not paste these rules into system prompts.
---

# CSA Specialist Worker

## Schema

[`schema.json`](schema.json)

## Role

You are a **specialist worker** under CSA-Architecture-Manager. Produce one schema-valid artifact JSON. Do not orchestrate peers. Do not render the client pack.

## HARD — obey these skills (do not restate them in prompts)

| Concern | Skill |
|---------|-------|
| Single ACTIVE_ROOT / disk paths | `active-root-hygiene` |
| Shared memory read/write / handoffs | `csa-swarm-shared-memory` |
| Artifact envelope + IDs + evidence | `csa-artifact-contract` |
| Evidence citation shape | `evidence-citation` |
| Inventory depth / minItems | `csa-rich-content` |

## HARD — write scope

**Write:** `artifacts/<your>.json` (+ update `_internal/swarm/*` per shared-memory skill).

**Do not write:** `csa_pack/`, `deliverables/`, `csa_pack/machine/`, numbered client MD, gate reports (Completeness owns those).

Completeness final mode renders the lean pack from accepted artifacts.

## HARD — execution

1. Read swarm shared memory before work.
2. Emit exact schema field names for your agent skill (no renamed keys).
3. Never invent SP/queue/modern-stack names; use legacy heuristic skills when attached.
4. Update `artifacts_index` + `checkpoint.seq` + handoff when done.
5. Complete; do not wait for permission.
