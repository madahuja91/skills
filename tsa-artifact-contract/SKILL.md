---
name: tsa-artifact-contract
description: Shared TSA artifact metadata, CSA/ADR citation rules, and confidence bands. Use when producing or validating any TSA specialist artifact JSON.
---

# TSA Artifact Contract

## Schema

Authoritative contract: [`schema.json`](schema.json)


Every TSA specialist artifact MUST include the shared envelope in `schema.json` plus agent payload fields.

## Required metadata

- `artifact_id`: `{agent}-{yyyyMMddHHmmss}`
- `agent_id`: intake|domain|tech_architecture|data|integration|migration_strategy|document_assembler|completeness_validator
- `csa_refs[]`: paths/IDs from accepted CSA pack (required for design claims)
- `adr_refs[]`: sections/decisions from target ADR/spec (required for stack choices)
- `overall_confidence_score`: 0–100
- `schema_version`: `1.0.0`

## Authority rules

1. **Stack choices** come only from ADR/target spec — never invent DB/MQ/language.
2. **Current-state facts** come only from CSA pack — never re-invent legacy topology.
3. Prefer ADR over CSA when they conflict on *target*; record conflict in gaps.
4. Inferred items: confidence ≤ 40 + `uncertainty_reason`.

## Anti-patterns

- Hardcoding customer names or sample package/queue names
- Treating CSA Discover agents as TSA workers
- Skipping CSA→TSA traceability
