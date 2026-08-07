---
name: csa5-gate-integration
description: Quality gate for CSA integration.json. Use when validating Integration specialist output.
---

# Gate: Integration

## Schema

Authoritative evaluation contract: [`schema.json`](schema.json)

## Target

- Artifact: `artifacts/integration.json`
- Artifact schema: `skills/agents/csa5-integration/schema.json`
- Rubric: `skills/agents/csa5-integration/quality-rubric.md`

## Blocking fails

- Discovered external I/O unclassified; missing sync_async/pattern_type; schema invalid.

Emit report with `gate_id: gate-integration`.
