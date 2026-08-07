---
name: csa5-gate-discover
description: Quality gate for CSA discovery.json. Use when Completeness Validator evaluates Discover output.
---

# Gate: Discover

## Schema

Authoritative evaluation contract: [`schema.json`](schema.json)

Final report must also conform to `skills/shared/csa5-quality-gate-framework/schema.json`.

## Target

- Artifact: `artifacts/discovery.json`
- Artifact schema: `skills/agents/csa5-discover/schema.json`
- Rubric: `skills/agents/csa5-discover/quality-rubric.md`

## Blocking fails

- No language, invented modern framework without descriptor evidence, schema invalid, evidence coverage on stack &lt;70%.

Emit report with `gate_id: gate-discover`.
