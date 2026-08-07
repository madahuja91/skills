---
name: csa7-tech-architecture
description: Runtime-aware technical architecture, C4 layers, components, and tech debt for CSA. Use when Manager invokes Technology Architecture analysis.
---

# CSA Tech Architecture Skill


## HARD — knowledge-first documentation (blocking)

1. Write **architecture knowledge**, not evidence dumps. Answer What / Why / How before citing files.
2. Business rules must be prose (e.g. "Customer cannot be deleted when active orders exist") — never lead with `Class.java:line`.
3. `pack_substance` MUST validate 100% against this skill's `pack-schemas/` (and `csa7-pack-schemas/output-schemas/`).
4. Required narrative fields (overview/purpose/what/why/how, acceptance criteria, DDD, persistence strategy, decision_log, modernization) are blocking.
5. Optional per-field `evidence` may exist for gates; Markdown **must** put `## Evidence Mapping (Appendix)` **last**.
6. Forbidden in client MD: evidence-led tables that dominate the doc; Completeness/gate/workflow meta in Risks docs.
7. Min **200 lines** per client MD; no maxLength anywhere.

**This agent's pack schema(s):** `pack-schemas/Application_Architecture.schema.json`


## Schema

Authoritative output/invocation contract: [schema.json](schema.json)

## Shared worker rules

Obey `csa7-specialist-worker` (do not restate). Output: `artifacts/architecture.json` including `deployment_topology`, `security_controls`, `cross_cutting_concerns`, `build_and_runtime`.


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

`csa7-gate-tech-architecture` — see `quality-rubric.md`.
