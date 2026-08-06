---
name: csa-discover
description: Technology inventory and artifact classification for legacy CSA discovery. Use when the Manager invokes Discover or when classifying a legacy codebase stack, modules, and dependencies.
---

# CSA Discover Agent Skill

## Schema

Authoritative output/invocation contract: [schema.json](schema.json)

## Shared worker rules

Obey `csa-specialist-worker` (do not restate).

## Goal

Produce `artifacts/discovery.json` conforming to `schema.json`.

## Procedure

1. Inventory files under `scope.codebase_root` (respect exclusions). Treat the upload as a **complete dump** — source, DDL, packages/procedures, and configs may all live in-tree.
2. Classify into code/data/config/runtime/documentation.
3. Detect languages, frameworks, DBs, infra using descriptors first (`legacy-framework-heuristics`).
4. Scan for stored procedures / packages / ORM call sites (`legacy-stored-procedures`) and IBM MQ (`legacy-ibm-mq`) using heuristics only — never hardcode folder paths or package names.
5. Map internal/external dependencies with risk.
6. Emit `module_map` for Manager scoping; sync via `csa-swarm-shared-memory`.
7. If DDL/SP/MQ artifacts are absent after a dump-wide heuristic search, flag them as missing — do not invent them.

## Anti-patterns

- Do not assume Spring Boot / microservices on old monoliths.
- Do not invent framework versions; use `"unknown"` + evidence of search.
- Do not skip `evidence` on stack detections.

## Quality bar

See `quality-rubric.md`. Gate: `gate-discover`.
