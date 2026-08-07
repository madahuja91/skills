---
name: csa7-business-domain
description: Extract DDD domains, entities, business rules, and capabilities from legacy code for CSA. Use when Manager invokes Business Domain analysis.
---

# CSA Business Domain Skill


## HARD — knowledge-first documentation (blocking)

1. Write **architecture knowledge**, not evidence dumps. Answer What / Why / How before citing files.
2. Business rules must be prose (e.g. "Customer cannot be deleted when active orders exist") — never lead with `Class.java:line`.
3. `pack_substance` MUST validate 100% against this skill's `pack-schemas/` (and `csa7-pack-schemas/output-schemas/`).
4. Required narrative fields (overview/purpose/what/why/how, acceptance criteria, DDD, persistence strategy, decision_log, modernization) are blocking.
5. Optional per-field `evidence` may exist for gates; Markdown **must** put `## Evidence Mapping (Appendix)` **last**.
6. Forbidden in client MD: evidence-led tables that dominate the doc; Completeness/gate/workflow meta in Risks docs.
7. Min **200 lines** per client MD; no maxLength anywhere.

**This agent's pack schema(s):** `pack-schemas/Business_Architecture.schema.json`


## Schema

Authoritative output/invocation contract: [schema.json](schema.json)

## Shared worker rules

Obey `csa7-specialist-worker` (do not restate). Output: `artifacts/domain.json` with exact schema field names (`business_domains`, `business_capabilities`, `workflows`, `operation_dispatch_rules`, …).


## Primary deliverable (pack_substance)

Primary deliverable: rtifacts/domain.json with required pack_substance matching pack-schemas/Business_Architecture.schema.json (bounded_contexts, CAP-* taxonomy, dictionary, WF-* flows, dispatch, flags, providers, gaps). Analysis fields remain but pack_substance is the gate.

## Procedure

1. Identify bounded contexts / domains from packages, screens, services, tables, and stored procedures.
2. Normalize duplicate names into `canonical_name`.
3. Extract business rules with pseudo-code and `implementation_location` when code-backed; use `csa7-legacy-stored-procedures` for PL/SQL / `{call}` / TopLink / iBatis call sites (never hardcode procedure names).
4. Capture `workflows`, `operation_dispatch_rules`, `feature_flags`, and `provider_selection_rules` when evidenced — do not invent.
5. Map capabilities to domains.
6. Score confidence by source (code > docs > config > inferred).

## Anti-patterns

- Do not create domains without entities or rules.
- Critical/high impact rules without location must be flagged in `uncertainty_reason` / missing logic list.
- Do not emit outline-only stubs to “finish fast”.

## Quality bar

See `quality-rubric.md`. Gate: `csa7-gate-business-domain`.
