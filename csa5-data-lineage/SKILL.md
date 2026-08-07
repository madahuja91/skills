---
name: csa5-data-lineage
description: Field-level and entity-level data lineage for legacy CSA. Use when Manager invokes Data Lineage analysis.
---

# CSA Data Lineage Skill

## Schema

Authoritative output/invocation contract: [schema.json](schema.json)

## Shared worker rules

Obey `csa5-specialist-worker` (do not restate). Output: `artifacts/lineage.json` including `entity_catalog`.

## Procedure

1. Catalog data sources (DB, files, APIs) from DDL/config/code.
2. Apply `csa5-legacy-stored-procedures` to treat SP/package call sites as transformation nodes (link `{call PKG.PROC}` / TopLink / iBatis to SQL when present).
3. Build `entity_catalog` with key attributes (pk/fk/business_key) for Completeness Data_and_Integration — do not emit a separate entity document.
4. Map primary entity fields source→target with transformation notes.
5. Document validation points and ETL/batch jobs.
6. Prefer table-level completeness for huge schemas; deepen field-level on critical entities only when scoped by Manager.

## Gate

`csa5-gate-data-lineage` — primary entities must have a path; see `quality-rubric.md`.
