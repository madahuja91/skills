---
name: csa5-gate-business-domain
description: Quality gate for CSA domain.json. Use when validating Business Domain specialist output.
---

# Gate: Business Domain

## Schema

Authoritative evaluation contract: [`schema.json`](schema.json)

## Target

- Artifact: `artifacts/domain.json`
- Artifact schema: `skills/agents/csa5-business-domain/schema.json`
- Rubric: `skills/agents/csa5-business-domain/quality-rubric.md`

## Blocking fails

- No domains; critical/high rules missing `implementation_location` without missing-logic flag; schema invalid.

Emit report with `gate_id: gate-business-domain`.
