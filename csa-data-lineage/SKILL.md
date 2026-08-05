---
name: csa-data-lineage
description: Field-level and entity-level data lineage for legacy CSA. Use when Manager invokes Data Lineage analysis.
---

# CSA Data Lineage Skill

## Schema

Authoritative output/invocation contract: [schema.json](schema.json)


## Goal

Write `artifacts/lineage.json` per `schema.json`.

## Procedure

1. Catalog data sources (DB, files, APIs) from DDL/config/code.
2. Apply `legacy-stored-procedures` to treat SP/package call sites as transformation nodes (link `{call PKG.PROC}` / TopLink / iBatis to SQL when present).
3. Map primary entity fields source→target with transformation notes.
4. Document validation points and ETL/batch jobs.
5. Prefer table-level completeness for huge schemas; deepen field-level on critical entities only when scoped by Manager.
6. Sync via `csa-swarm-shared-memory`.

## HARD: Depth (`csa-rich-content`)

Prefer many evidenced field_lineage / transformation rows (SP call chains, table hops). A handful of placeholder lineage rows fails Completeness when discovery shows substantial SQL/packages.

## Gate

`gate-data-lineage` — primary entities must have a path; see `quality-rubric.md`.
