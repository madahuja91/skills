---
name: active-root-hygiene
description: Enforces a single ACTIVE_ROOT (typically one src/) with no nested src/src or duplicate roots; Completeness must fail or auto-remove duplicates. Use on every Manager bootstrap and Completeness run for CSA/TSA swarms.
---

# Active Root Hygiene

## Schema

Authoritative contract: [`schema.json`](schema.json)

## HARD rule

There must be **exactly one** ACTIVE_ROOT for the run. Prefer workspace `src/` (or the path recorded in `swarm_state.active_root`).

### Forbidden

- Nested `src/src/` (or `ACTIVE_ROOT/src/` when ACTIVE_ROOT is already `src`)
- Parallel duplicate roots writing the same pack (`src/` and `src2/`, twin `csa_pack/` / `tsa_pack/` trees outside ACTIVE_ROOT)
- Subagents inventing a new root while peers use another

### Required

1. Manager sets `swarm_state.active_root` once at bootstrap (absolute or workspace-relative canonical path).
2. Every subagent (sequential or parallel) reads `active_root` and writes **only** under it.
3. Completeness Validator **every run**:
   - Detect nested `src/src` (and equivalent double-root patterns)
   - Detect duplicate pack/artifact trees outside `active_root`
   - **Remove duplicates immediately** (delete nested/extra trees) and log paths in the gate report
   - **Fail blocking** if nesting reappears after cleanup or if agents wrote to multiple roots in the same attempt
4. After cleanup, all subsequent work continues only under the single `active_root`.

## Detection heuristics

- Path contains `/src/src/` or ends with nested repeated root segment
- Second directory that also contains `_internal/swarm/swarm_state.json` besides `active_root`
- Pack output (`csa_pack/` / `tsa_pack/`) found both under `active_root` and a sibling/nested root

## Deliverable formats (remind Completeness)

| Content | Format |
|---------|--------|
| Narrative sections, migration, epic/story seeds, README | **Markdown only** |
| arc42 / C4 views | **HTML only** under `{csa\|tsa}_pack/arc42-c4/` (`index.html` + pages) |
| Specialist working copies | `artifacts/*.json` / `machine/*.json` (internal) |

Fail document gates if C4 is emitted as `.md` or narrative pack sections as `.html` (except under `arc42-c4/`).
