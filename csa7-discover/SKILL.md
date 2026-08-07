---
name: csa7-discover
description: Technology inventory and artifact classification for legacy CSA discovery. Use when the Manager invokes Discover or when classifying a legacy codebase stack, modules, and dependencies.
---

# CSA Discover Agent Skill


## HARD — knowledge-first documentation (blocking)

1. Write **architecture knowledge**, not evidence dumps. Answer What / Why / How before citing files.
2. Business rules must be prose (e.g. "Customer cannot be deleted when active orders exist") — never lead with `Class.java:line`.
3. `pack_substance` MUST validate 100% against this skill's `pack-schemas/` (and `csa7-pack-schemas/output-schemas/`).
4. Required narrative fields (overview/purpose/what/why/how, acceptance criteria, DDD, persistence strategy, decision_log, modernization) are blocking.
5. Optional per-field `evidence` may exist for gates; Markdown **must** put `## Evidence Mapping (Appendix)` **last**.
6. Forbidden in client MD: evidence-led tables that dominate the doc; Completeness/gate/workflow meta in Risks docs.
7. Min **200 lines** per client MD; no maxLength anywhere.

**This agent's pack schema(s):** `pack-schemas/Executive_Summary.schema.json`


## Schema

Authoritative output/invocation contract: [schema.json](schema.json)

## Shared worker rules

Obey `csa7-specialist-worker` (do not restate).

## Goal

Produce `artifacts/discovery.json` conforming to `schema.json`.


## Primary deliverable (pack_substance)

Primary deliverable: rtifacts/discovery.json with required pack_substance matching pack-schemas/Executive_Summary.schema.json (system_overview, key_metrics_table floors, scorecard seed, findings/risks/effort/strategy/success metrics from inventory evidence). Completeness FINAL may refine Exec from all lanes.

## Procedure

1. Inventory files under `scope.codebase_root` (respect exclusions). Treat the upload as a **complete dump** — source, DDL, packages/procedures, and configs may all live in-tree.
2. Classify into code/data/config/runtime/documentation.
3. Detect languages, frameworks, DBs, infra using descriptors first (`csa7-legacy-framework-heuristics`).
4. Scan for stored procedures / packages / ORM call sites (`csa7-legacy-stored-procedures`) and IBM MQ (`csa7-legacy-ibm-mq`) using heuristics only — never hardcode folder paths or package names.
5. Map internal/external dependencies with risk.
6. Emit `module_map` for Manager scoping; sync via `csa7-swarm-shared-memory`.
7. If DDL/SP/MQ artifacts are absent after a dump-wide heuristic search, flag them as missing — do not invent them.

## Anti-patterns

- Do not assume Spring Boot / microservices on old monoliths.
- Do not invent framework versions; use `"unknown"` + evidence of search.
- Do not skip `evidence` on stack detections.

## Quality bar

See `quality-rubric.md`. Gate: `csa7-gate-discover`.
