---
name: csa5-business-domain
description: Extract DDD domains, entities, business rules, and capabilities from legacy code for CSA. Use when Manager invokes Business Domain analysis.
---

# CSA Business Domain Skill

## Schema

Authoritative output/invocation contract: [schema.json](schema.json)

## Shared worker rules

Obey `csa5-specialist-worker` (do not restate). Output: `artifacts/domain.json` with exact schema field names (`business_domains`, `business_capabilities`, `workflows`, `operation_dispatch_rules`, …).

## Procedure

1. Identify bounded contexts / domains from packages, screens, services, tables, and stored procedures.
2. Normalize duplicate names into `canonical_name`.
3. Extract business rules with pseudo-code and `implementation_location` when code-backed; use `csa5-legacy-stored-procedures` for PL/SQL / `{call}` / TopLink / iBatis call sites (never hardcode procedure names).
4. Capture `workflows`, `operation_dispatch_rules`, `feature_flags`, and `provider_selection_rules` when evidenced — do not invent.
5. Map capabilities to domains.
6. Score confidence by source (code > docs > config > inferred).

## Anti-patterns

- Do not create domains without entities or rules.
- Critical/high impact rules without location must be flagged in `uncertainty_reason` / missing logic list.
- Do not emit outline-only stubs to “finish fast”.

## Quality bar

See `quality-rubric.md`. Gate: `csa5-gate-business-domain`.
