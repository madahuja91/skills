---
name: csa5-gate-data-lineage
description: Quality gate for CSA lineage.json. Use when validating Data Lineage specialist output.
---

# Gate: Data Lineage

## Schema

Authoritative evaluation contract: [`schema.json`](schema.json)

## Target

- Artifact: `artifacts/lineage.json`
- Artifact schema: `skills/agents/csa5-data-lineage/schema.json`
- Rubric: `skills/agents/csa5-data-lineage/quality-rubric.md`

## Blocking fails

- No data sources; &lt;80% primary entities lack path; schema invalid.

Emit report with `gate_id: gate-data-lineage`.
