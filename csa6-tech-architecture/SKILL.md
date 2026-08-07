---
name: csa6-tech-architecture
description: Runtime-aware technical architecture, C4 layers, components, and tech debt for CSA. Use when Manager invokes Technology Architecture analysis.
---

# CSA Tech Architecture Skill


## HARD — pack schema is the artifact contract (blocking)

1. Your `artifacts/*.json` **MUST** include a top-level `pack_substance` object.
2. `pack_substance` **MUST** validate 100% against the pack schema(s) in this skill's `pack-schemas/` folder (same as `csa6-pack-schemas/output-schemas/`).
3. Cover **every** `required[]` field, every `minItems` floor, and every ID pattern (`CAP-*`, `CMP-*`, `LIN-*`, `INT-*`, `CTR-*`, `DEBT-*`, `RISK-*`, `GAP-*`, `ASM-*`, `ACT-*`, `REG-*`, `WF-*`, etc.).
4. Do **not** mark done if analysis-only fields are filled but `pack_substance` is missing, thin, or schema-invalid.
5. Markdown rendered later must expose the **same** sections/IDs — if it is not in `pack_substance`, it will not appear in the client MD.
6. Inventing empty placeholders to “pass” is forbidden; use evidenced content or explicit gap rows that still satisfy schema shape/floors where the schema allows gap documentation.

**This agent's pack schema(s):** `pack-schemas/Application_Architecture.schema.json`

## Schema

Authoritative output/invocation contract: [schema.json](schema.json)

## Shared worker rules

Obey `csa6-specialist-worker` (do not restate). Output: `artifacts/architecture.json` including `deployment_topology`, `security_controls`, `cross_cutting_concerns`, `build_and_runtime`.


## Primary deliverable (pack_substance)

Primary deliverable: rtifacts/architecture.json with required pack_substance matching pack-schemas/Application_Architecture.schema.json (5 layers, CMP-*, build/runtime, deploy, security, cross-cutting, runtime evidence, DEBT-*, ops_gaps).

## Procedure

1. Map presentation/business/data/integration/infrastructure layers from code + configs.
2. Register components with `CMP-*` IDs and evidence; include `interfaces` when evidenced.
3. Fill `deployment_topology`, `security_controls`, `cross_cutting_concerns`, and `build_and_runtime` (feeds Application Architecture — no separate tech-stack doc).
4. Compare static structure vs runtime (logs/APM) when available; else mark `analysis_scope: static`.
5. Score technical debt; list dead/orphan candidates honestly.
6. Fill C4 context/containers/critical components for Completeness Mermaid (`mermaid-diagrams` + `arc42-c4-views`).

## Anti-patterns

- Do not claim runtime validation without logs/traces.
- Do not invent microservices topology for a monolith WAR/EAR.
- Do not emit outline-only stubs to “finish fast”.

## Gate

`csa6-gate-tech-architecture` — see `quality-rubric.md`.
