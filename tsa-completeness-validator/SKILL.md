---
name: tsa-completeness-validator
description: Validates TSA specialist artifacts against schemas and gate rubrics; emits pass/fail reports. Use after every TSA specialist as Manager subagent.
---

# TSA Completeness Validator

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Role

Evaluate only — never invent architecture.

## Procedure

1. Load target artifact + gate skill schema.
2. Validate JSON Schema + ADR/CSA citation rules.
3. Emit `_internal/completeness_validation/*` and `artifacts/quality_gate_reports/*`.
4. Update shared memory `loop` only.
