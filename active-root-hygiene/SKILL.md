---
name: active-root-hygiene
description: Enforces a single workspace-disk ACTIVE_ROOT with no invented /app/temp trees, no nested src/src, and all deliverables written only under that root. Use on every Manager bootstrap and Completeness run for CSA/TSA swarms.
---

# Active Root Hygiene

## Schema

Authoritative contract: [`schema.json`](schema.json)

## HARD rule — workspace disk only

There must be **exactly one** ACTIVE_ROOT for the run. Prefer workspace-relative **`src/`** (create if missing). Record it in `swarm_state.active_root` and `active_root.txt`.

### All deliverables MUST be written on disk under ACTIVE_ROOT only

| Deliverable | Required path (relative to ACTIVE_ROOT) |
|-------------|-------------------------------------------|
| Specialist JSON | `artifacts/*.json` |
| Quality gates | `artifacts/quality_gate_reports/*` |
| CSA/TSA pack | `csa_pack/**` or `tsa_pack/**` |
| Completeness notes | `_internal/completeness_validation/*` |
| Swarm memory | `_internal/swarm/*` |

Agents MUST use `write_file` / shell writes to these **relative** paths under ACTIVE_ROOT so the platform **persists and exports** them with the run workspace.

### Forbidden (blocking)

- Inventing parallel trees such as `/app/temp/csa-run/...`, `/tmp/...`, `~/...`, or any absolute path **outside** the workspace ACTIVE_ROOT
- Writing pack/artifacts to a sibling folder like `outputs/` **outside** ACTIVE_ROOT (e.g. `/app/temp/csa-run/outputs` while ACTIVE_ROOT is `/app/temp/csa-run/active_root`)
- Nested `src/src/` or duplicate ACTIVE_ROOT
- “Memory-only” or chat-only deliverables with no on-disk files under ACTIVE_ROOT
- Declaring done while `csa_pack/` / `artifacts/` do not exist on disk under ACTIVE_ROOT

### Required

1. Manager sets `swarm_state.active_root` once at bootstrap to workspace-relative `src` (or the single workspace root the platform mounts). Prefer **`src`**.
2. If the platform mounts the workspace under `/app/temp/<run-id>/...`, ACTIVE_ROOT must still be **that workspace’s `src`** (or `.`), never a newly invented `/app/temp/csa-run` tree.
3. Every subagent reads `active_root` / `active_root.txt` and writes **only** under it using relative paths (`artifacts/…`, `csa_pack/…`).
4. Completeness Validator **every run**:
   - Fail if any accepted artifact path is outside ACTIVE_ROOT
   - Fail if pack exists only under a parallel `outputs/` tree outside ACTIVE_ROOT
   - Detect nested `src/src` and duplicate pack/swarm trees
   - **Remove duplicates immediately** and log `removed_paths`
   - **Fail blocking** if nesting reappears or agents wrote to multiple roots
5. Assembler MUST create `ACTIVE_ROOT/csa_pack/` (or `tsa_pack/`) on disk before finishing — not only under a custom absolute outputs path.

## Detection heuristics

- Path starts with `/app/temp/csa-run` or other invented absolute sandbox folders not equal to `swarm_state.active_root`
- Pack found under `…/outputs/csa_pack` while ACTIVE_ROOT is `…/active_root` (or `src`) without the same pack under ACTIVE_ROOT
- Path contains `/src/src/`
- Second directory with `_internal/swarm/swarm_state.json` besides `active_root`

## Deliverable formats (remind Completeness)

| Content | Format |
|---------|--------|
| Narrative sections, README | **Markdown only** under `{csa\|tsa}_pack/` |
| arc42 / C4 views | **HTML only** under `{csa\|tsa}_pack/arc42-c4/` |
| Specialist working copies | `artifacts/*.json` / `machine/*.json` (internal) |

Fail document gates if C4 is emitted as `.md` or narrative pack sections as `.html` (except under `arc42-c4/`).
Fail document gates if pack is missing on disk under ACTIVE_ROOT.
