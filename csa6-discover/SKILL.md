---
name: csa6-discover
description: Technology inventory and artifact classification for legacy CSA discovery. Use when the Manager invokes Discover or when classifying a legacy codebase stack, modules, and dependencies.
---

# CSA Discover Agent Skill


## HARD — pack schema is the artifact contract (blocking)

1. Your `artifacts/*.json` **MUST** include a top-level `pack_substance` object.
2. `pack_substance` **MUST** validate 100% against the pack schema(s) in this skill's `pack-schemas/` folder (same as `csa6-pack-schemas/output-schemas/`).
3. Cover **every** `required[]` field, every `minItems` floor, and every ID pattern (`CAP-*`, `CMP-*`, `LIN-*`, `INT-*`, `CTR-*`, `DEBT-*`, `RISK-*`, `GAP-*`, `ASM-*`, `ACT-*`, `REG-*`, `WF-*`, etc.).
4. Do **not** mark done if analysis-only fields are filled but `pack_substance` is missing, thin, or schema-invalid.
5. Markdown rendered later must expose the **same** sections/IDs — if it is not in `pack_substance`, it will not appear in the client MD.
6. Inventing empty placeholders to “pass” is forbidden; use evidenced content or explicit gap rows that still satisfy schema shape/floors where the schema allows gap documentation.

**This agent's pack schema(s):** `pack-schemas/Executive_Summary.schema.json`

## Schema

Authoritative output/invocation contract: [schema.json](schema.json)

## Shared worker rules

Obey `csa6-specialist-worker` (do not restate).

## Goal

Produce `artifacts/discovery.json` conforming to `schema.json`.


## Primary deliverable (pack_substance)

Primary deliverable: rtifacts/discovery.json with required pack_substance matching pack-schemas/Executive_Summary.schema.json (system_overview, key_metrics_table floors, scorecard seed, findings/risks/effort/strategy/success metrics from inventory evidence). Completeness FINAL may refine Exec from all lanes.

## Procedure

1. Inventory files under `scope.codebase_root` (respect exclusions). Treat the upload as a **complete dump** — source, DDL, packages/procedures, and configs may all live in-tree.
2. Classify into code/data/config/runtime/documentation.
3. Detect languages, frameworks, DBs, infra using descriptors first (`csa6-legacy-framework-heuristics`).
4. Scan for stored procedures / packages / ORM call sites (`csa6-legacy-stored-procedures`) and IBM MQ (`csa6-legacy-ibm-mq`) using heuristics only — never hardcode folder paths or package names.
5. Map internal/external dependencies with risk.
6. Emit `module_map` for Manager scoping; sync via `csa6-swarm-shared-memory`.
7. If DDL/SP/MQ artifacts are absent after a dump-wide heuristic search, flag them as missing — do not invent them.

## Anti-patterns

- Do not assume Spring Boot / microservices on old monoliths.
- Do not invent framework versions; use `"unknown"` + evidence of search.
- Do not skip `evidence` on stack detections.

## Quality bar

See `quality-rubric.md`. Gate: `csa6-gate-discover`.
