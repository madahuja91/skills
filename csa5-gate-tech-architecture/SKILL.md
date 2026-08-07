---
name: csa5-gate-tech-architecture
description: Quality gate for CSA architecture.json. Use when validating Tech Architecture specialist output.
---

# Gate: Tech Architecture

## Schema

Authoritative evaluation contract: [`schema.json`](schema.json)

## Target

- Artifact: `artifacts/architecture.json`
- Artifact schema: `skills/agents/csa5-tech-architecture/schema.json`
- Rubric: `skills/agents/csa5-tech-architecture/quality-rubric.md`

## Blocking fails

- Fewer than required layers without monolith justification; runtime claimed without evidence; schema invalid; component evidence &lt;70%.

Emit report with `gate_id: gate-tech-architecture`.
