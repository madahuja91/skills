---
name: active-root-hygiene
description: >-
  Enforces a single workspace-disk ACTIVE_ROOT (prefer src/) with no invented
  absolute trees, no nested src/src, and all epic/story deliverables written only
  under that root. Use on every Manager/Orchestrator bootstrap and 
  
  Quality run.
---

# Active Root Hygiene

## Schema

Authoritative contract: [`schema.json`](schema.json)

## HARD rule — one ACTIVE_ROOT on workspace disk

There must be **exactly one** ACTIVE_ROOT for the run. Prefer workspace-relative **`src/`** (create if missing). Record it in:

- `WORKSPACE_ROOT/active_root.txt` (single line: `src`)
- `swarm_state.active_root`

### Manager / Orchestrator (must create)

1. Resolve WORKSPACE_ROOT = directory containing `.agents/` or `skills/` (if cwd is already `…/src`, use parent — do **not** create another `src` under cwd).
2. Create `WORKSPACE_ROOT/src` if missing.
3. Write `WORKSPACE_ROOT/active_root.txt` with content `src` (or the single chosen relative path).
4. Create `ACTIVE_ROOT/_internal/swarm/` and bootstrap swarm files.
5. Set `swarm_state.active_root` once. Never invent a second root.

### All agents (must follow)

| Deliverable | Path under ACTIVE_ROOT |
|-------------|------------------------|
| CS/TS JSON + nested MD | `artifacts/cs/**`, `artifacts/ts/**` |
| Gates | `artifacts/gates/**` |
| Traceability | `artifacts/traceability/**` |
| Package | `artifacts/package/**` |
| Swarm memory | `_internal/swarm/*` |

Use relative writes under ACTIVE_ROOT only so the platform persists/exports them.

### Forbidden (blocking)

- Nested **`src/src/`** or duplicate ACTIVE_ROOT
- Invented parallel trees (`/app/temp/...`, `/tmp/...`, sibling `outputs/` outside ACTIVE_ROOT)
- Writing packs/artifacts outside ACTIVE_ROOT
- Chat-only deliverables with no on-disk files under ACTIVE_ROOT
- Resolving ACTIVE_ROOT by appending `src` when cwd is already ACTIVE_ROOT

### Detection heuristics

- Path contains `/src/src/` or `\\src\\src\\`
- Second directory with `_internal/swarm/swarm_state.json` besides active_root
- Artifact paths outside `active_root.txt` value

### Quality / Completeness

Every Quality Reviewer turn:

1. Read `active_root.txt` + `swarm_state.active_root` (must match)
2. Fail if nested `src/src` or multi-root writes
3. Remove duplicate nested roots when safe; log `removed_paths`
4. Fail blocking if nesting reappears
