---
name: csa6-business-domain
description: Extract DDD domains, entities, business rules, and capabilities from legacy code for CSA. Use when Manager invokes Business Domain analysis.
---

# CSA Business Domain Skill


## HARD — pack schema is the artifact contract (blocking)

1. Your `artifacts/*.json` **MUST** include a top-level `pack_substance` object.
2. `pack_substance` **MUST** validate 100% against the pack schema(s) in this skill's `pack-schemas/` folder (same as `csa6-pack-schemas/output-schemas/`).
3. Cover **every** `required[]` field, every `minItems` floor, and every ID pattern (`CAP-*`, `CMP-*`, `LIN-*`, `INT-*`, `CTR-*`, `DEBT-*`, `RISK-*`, `GAP-*`, `ASM-*`, `ACT-*`, `REG-*`, `WF-*`, etc.).
4. Do **not** mark done if analysis-only fields are filled but `pack_substance` is missing, thin, or schema-invalid.
5. Markdown rendered later must expose the **same** sections/IDs — if it is not in `pack_substance`, it will not appear in the client MD.
6. Inventing empty placeholders to “pass” is forbidden; use evidenced content or explicit gap rows that still satisfy schema shape/floors where the schema allows gap documentation.

**This agent's pack schema(s):** `pack-schemas/Business_Architecture.schema.json`

## Schema

Authoritative output/invocation contract: [schema.json](schema.json)

## Shared worker rules

Obey `csa6-specialist-worker` (do not restate). Output: `artifacts/domain.json` with exact schema field names (`business_domains`, `business_capabilities`, `workflows`, `operation_dispatch_rules`, …).


## Primary deliverable (pack_substance)

Primary deliverable: rtifacts/domain.json with required pack_substance matching pack-schemas/Business_Architecture.schema.json (bounded_contexts, CAP-* taxonomy, dictionary, WF-* flows, dispatch, flags, providers, gaps). Analysis fields remain but pack_substance is the gate.

## Procedure

1. Identify bounded contexts / domains from packages, screens, services, tables, and stored procedures.
2. Normalize duplicate names into `canonical_name`.
3. Extract business rules with pseudo-code and `implementation_location` when code-backed; use `csa6-legacy-stored-procedures` for PL/SQL / `{call}` / TopLink / iBatis call sites (never hardcode procedure names).
4. Capture `workflows`, `operation_dispatch_rules`, `feature_flags`, and `provider_selection_rules` when evidenced — do not invent.
5. Map capabilities to domains.
6. Score confidence by source (code > docs > config > inferred).

## Anti-patterns

- Do not create domains without entities or rules.
- Critical/high impact rules without location must be flagged in `uncertainty_reason` / missing logic list.
- Do not emit outline-only stubs to “finish fast”.

## Quality bar

See `quality-rubric.md`. Gate: `csa6-gate-business-domain`.
