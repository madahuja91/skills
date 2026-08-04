---
name: tsa-completeness-validator
description: Validates TSA specialist artifacts against schemas and gate rubrics; enforces single ACTIVE_ROOT (no src/src); emits pass/fail reports. Use after every TSA specialist as Manager subagent.
---

# TSA Completeness Validator

## Schema

Authoritative contract: [`schema.json`](schema.json)

Also apply: `skills/shared/active-root-hygiene/schema.json`

## Role

Evaluate only — never invent architecture. Also enforce **workspace hygiene**.

## HARD: Single ACTIVE_ROOT (every Completeness run)

1. Read `ACTIVE_ROOT` from `_internal/swarm/swarm_state.json` → `active_root` (canonical single root; typically `src`).
2. Scan for **forbidden** nested roots: `src/src`, or any `active_root/<same-root-name>/`.
3. Scan for **duplicate** swarm/pack trees outside `active_root`.
4. **Delete duplicates / nested roots immediately**; record `removed_paths` in the gate report (`active_root_hygiene` section).
5. If violations remain → **blocking fail** (`result=fail`) and tell Manager to re-run the offending agent with writes only under `active_root`.
6. All sequential and parallel subagents must use the **same** `active_root` — fail if artifacts landed in more than one root this attempt.

## Procedure

1. Run **active-root-hygiene** checks (above) before/with artifact checks.
2. Load target artifact + gate skill schema.
3. Validate JSON Schema + ADR/CSA citation rules.
4. Emit `_internal/completeness_validation/*` and `artifacts/quality_gate_reports/*` under **only** `active_root`.
5. Update shared memory `loop` only.

## Deliverable format checks (document gates)

- Narrative TSA sections + epic seeds: **Markdown only**
- arc42/C4: **HTML index** under `tsa_pack/arc42-c4/` only — never C4 `.md`
- Fail if narrative content is HTML outside `arc42-c4/`
