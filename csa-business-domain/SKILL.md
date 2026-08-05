---
name: csa-business-domain
description: Extract DDD domains, entities, business rules, and capabilities from legacy code for CSA. Use when Manager invokes Business Domain analysis.
---

# CSA Business Domain Skill

## Schema

Authoritative output/invocation contract: [schema.json](schema.json)


## Goal

Write `artifacts/domain.json` per `schema.json` using Discovery inventory.

## Procedure

1. Identify bounded contexts / domains from packages, screens, services, tables, and stored procedures.
2. Normalize duplicate names into `canonical_name`.
3. Extract business rules with pseudo-code and `implementation_location` when code-backed; use `legacy-stored-procedures` for PL/SQL / `{call}` / TopLink / iBatis call sites (never hardcode procedure names).
4. Map capabilities to domains for Function epic seeds.
5. Score confidence by source (code > docs > config > inferred).
6. Sync via `csa-swarm-shared-memory`.

## HARD: Depth (`csa-rich-content`)

Produce a **dense** `domain.json`: many evidenced domains/entities/rules/capabilities with multi-sentence descriptions and evidence paths. A handful of shallow rows is a Completeness fail.

## Anti-patterns

- Do not create domains without entities or rules.
- Critical/high impact rules without location must be flagged in `uncertainty_reason` / missing logic list.
- Do not emit outline-only stubs to “finish fast”.

## Quality bar

See `quality-rubric.md`. Gate: `gate-business-domain`.
