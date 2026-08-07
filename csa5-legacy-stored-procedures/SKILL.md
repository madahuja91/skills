---
name: csa5-legacy-stored-procedures
description: Detection and documentation heuristics for legacy stored procedures, packages, and ORM call sites (PL/SQL, TopLink, iBatis/MyBatis, JDBC CallableStatement). Use during Discover, Domain, Data Lineage, and Completeness validation. Do not hardcode customer package names.
---

# Legacy Stored Procedures Skill

## Schema

Findings contract: [schema.json](schema.json)

## Goal

Discover and document **database-resident logic** and **application call sites** so CSA lineage and business rules include SP/packages — without assuming a specific product name.

## Scan order (generic)

1. Inventory dirs/files: `**/database*/**`, `**/*PROCEDURE*/**`, `**/*PACKAGE*/**`, `**/*DDL*/**`, `**/*.{sql,pls,pkb,pks,plb}`.
2. Grep SQL text for:
   - `(?i)CREATE\s+(OR\s+REPLACE\s+)?(PROCEDURE|FUNCTION|PACKAGE(\s+BODY)?)`
   - nested `PROCEDURE\s+\w+` inside package bodies
3. Grep app maps/code for call sites:
   - JDBC escape `{call Schema.Proc(...)}` / `{?=call ...}`
   - iBatis/MyBatis: `<procedure>`, `statementType="CALLABLE"`
   - TopLink/EclipseLink: `StoredProcedureCall`, `setProcedureName`, `addNamedArgument`
   - JDBC: `CallableStatement`, `prepareCall`, `registerOutParameter`
4. Link **callee name** from Java/XML to SQL object / filename when possible; else mark `unresolved_callee`.

## Emit into CSA artifacts

### Discover

- Classify SQL packages/procedures under `artifact_inventory.classified_artifacts.data`
- Note ORM/map technologies under frameworks (e.g. TopLink, iBatis) with evidence
- List missing DDL/SP dumps in `missing_artifacts` when call sites exist but SQL absent

### Business Domain

- Treat SP bodies as **business_rules** / workflow when they encode validation, status, calculations
- `extraction_source`: `code` if body found; else `inferred` with uncertainty
- Prefer `implementation_location.file_path` pointing at `.sql` or map XML

### Data Lineage

- Model SP as transformation steps: in-params → out-params/cursors → tables
- Capture `{call PKG.PROC}` as lineage edge even when body unavailable (lower confidence)

## Anti-patterns

- Do not invent package/procedure names not present in files.
- Do not assume PostgreSQL vs Oracle vs SQL Server — use driver URL / DDL dialect evidence.
- Do not skip SP just because Java layer looks like CRUD.