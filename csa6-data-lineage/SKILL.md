---
name: csa6-data-lineage
description: Field-level and entity-level data lineage for legacy CSA. Use when Manager invokes Data Lineage analysis.
---

# CSA Data Lineage Skill


## HARD — pack schema is the artifact contract (blocking)

1. Your `artifacts/*.json` **MUST** include a top-level `pack_substance` object.
2. `pack_substance` **MUST** validate 100% against the pack schema(s) in this skill's `pack-schemas/` folder (same as `csa6-pack-schemas/output-schemas/`).
3. Cover **every** `required[]` field, every `minItems` floor, and every ID pattern (`CAP-*`, `CMP-*`, `LIN-*`, `INT-*`, `CTR-*`, `DEBT-*`, `RISK-*`, `GAP-*`, `ASM-*`, `ACT-*`, `REG-*`, `WF-*`, etc.).
4. Do **not** mark done if analysis-only fields are filled but `pack_substance` is missing, thin, or schema-invalid.
5. Markdown rendered later must expose the **same** sections/IDs — if it is not in `pack_substance`, it will not appear in the client MD.
6. Inventing empty placeholders to “pass” is forbidden; use evidenced content or explicit gap rows that still satisfy schema shape/floors where the schema allows gap documentation.

**This agent's pack schema(s):** `pack-schemas/Data_and_Integration.schema.json`

## Schema

Authoritative output/invocation contract: [schema.json](schema.json)

## Shared worker rules

Obey `csa6-specialist-worker` (do not restate). Output: `artifacts/lineage.json` including `entity_catalog`.


## Primary deliverable (pack_substance)

Primary deliverable: rtifacts/lineage.json with required pack_substance matching full pack-schemas/Data_and_Integration.schema.json (stores, entities, LIN-*≥10, DB rules, plus integration sections coordinated with Integration agent).

## Procedure

1. Catalog data sources (DB, files, APIs) from DDL/config/code.
2. Apply `csa6-legacy-stored-procedures` to treat SP/package call sites as transformation nodes (link `{call PKG.PROC}` / TopLink / iBatis to SQL when present).
3. Build `entity_catalog` with key attributes (pk/fk/business_key) for Completeness Data_and_Integration — do not emit a separate entity document.
4. Map primary entity fields source→target with transformation notes.
5. Document validation points and ETL/batch jobs.
6. Prefer table-level completeness for huge schemas; deepen field-level on critical entities only when scoped by Manager.

## Gate

`csa6-gate-data-lineage` — primary entities must have a path; see `quality-rubric.md`.
