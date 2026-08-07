---
name: csa7-active-root-hygiene
description: Enforces a single workspace-disk ACTIVE_ROOT with no invented trees, no nested src/src, and all writes only under that root. Use on Manager, Completeness, and every specialist.
---

# Active Root Hygiene

## Schema

[`schema.json`](schema.json)

## HARD — one ACTIVE_ROOT on disk

Prefer workspace-relative **`src/`** — platforms often only allow new files under `src/`.  
Record **`src`** (relative) in `swarm_state.active_root` and `active_root.txt`.  
Do not set ACTIVE_ROOT to an absolute `/app/temp/...` path.

Client pack: **`src/csa_pack/`**. Specialist SSOT: prefer **`src/artifacts/`**.

### Who may write where

| Writer | Allowed under ACTIVE_ROOT |
|--------|---------------------------|
| Specialists | `artifacts/*.json`, `_internal/swarm/*` |
| Completeness (lane) | `artifacts/quality_gate_reports/*`, `_internal/**` |
| Completeness (final) | above + lean `csa_pack/{5 MD, README, arc42-c4/*.html}` only |
| Manager | bootstrap `_internal/swarm/*`, `run_plan.json`, `active_root.txt` |

### Forbidden (blocking)

- Invented absolute trees (`/app/temp/csa-run`, sibling `outputs/` outside ACTIVE_ROOT)
- Nested `src/src/` or duplicate roots
- Chat-only deliverables with no on-disk files
- Specialists writing `csa_pack/` or `deliverables/`
- `csa_pack/machine/`

### Completeness every run

Detect/remove duplicates; fail if pack/artifacts are missing under ACTIVE_ROOT or written outside it.
