---
name: csa7-data-lineage
description: Field-level and entity-level data lineage for legacy CSA. Use when Manager invokes Data Lineage analysis.
---

# CSA Data Lineage Skill


## HARD — knowledge-first documentation (blocking)

1. Write **architecture knowledge**, not evidence dumps. Answer What / Why / How before citing files.
2. Business rules must be prose (e.g. "Customer cannot be deleted when active orders exist") — never lead with `Class.java:line`.
3. `pack_substance` MUST validate 100% against this skill's `pack-schemas/` (and `csa7-pack-schemas/output-schemas/`).
4. Required narrative fields (overview/purpose/what/why/how, acceptance criteria, DDD, persistence strategy, decision_log, modernization) are blocking.
5. Optional per-field `evidence` may exist for gates; Markdown **must** put `## Evidence Mapping (Appendix)` **last**.
6. Forbidden in client MD: evidence-led tables that dominate the doc; Completeness/gate/workflow meta in Risks docs.
7. Min **200 lines** per client MD; no maxLength anywhere.

**This agent's pack schema(s):** `pack-schemas/Data_and_Integration.schema.json`


## Schema

Authoritative output/invocation contract: [schema.json](schema.json)

## Shared worker rules

Obey `csa7-specialist-worker` (do not restate). Output: `artifacts/lineage.json` including `entity_catalog`.


## Primary deliverable (pack_substance)

Primary deliverable: rtifacts/lineage.json with required pack_substance matching full pack-schemas/Data_and_Integration.schema.json (stores, entities, LIN-*≥10, DB rules, plus integration sections coordinated with Integration agent).

## Procedure

1. Catalog data sources (DB, files, APIs) from DDL/config/code.
2. Apply `csa7-legacy-stored-procedures` to treat SP/package call sites as transformation nodes (link `{call PKG.PROC}` / TopLink / iBatis to SQL when present).
3. Build `entity_catalog` with key attributes (pk/fk/business_key) for Completeness Data_and_Integration — do not emit a separate entity document.
4. Map primary entity fields source→target with transformation notes.
5. Document validation points and ETL/batch jobs.
6. Prefer table-level completeness for huge schemas; deepen field-level on critical entities only when scoped by Manager.

## Gate

`csa7-gate-data-lineage` — primary entities must have a path; see `quality-rubric.md`.
