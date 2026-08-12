---
name: active-root-hygiene-v2
description: Enforces a single workspace-disk ACTIVE_ROOT (prefer src/) with no invented absolute trees, no nested src/src, and all deliverables written only under that root. Use on every Manager/Orchestrator bootstrap and Quality run.
---

# Active Root Hygiene

## HARD - one ACTIVE_ROOT on disk

Prefer workspace-relative **src/**.
Record **src** (relative) in swarm shared memory / active_root.txt.
Do not set ACTIVE_ROOT to an absolute `/app/temp/...` path.
Never create or write under nested **src/src**.

## TSA writes
- Specialist SSOT: `src/artifacts/`
- Client pack: `src/tsa_pack/`
- Diagrams: `src/tsa_pack/diagrams/`

## Rules
- All new files must be under ACTIVE_ROOT
- Delete accidental `src/src` duplicates immediately
- Do not invent absolute trees outside the workspace root
