---
name: csa5-tech-architecture
description: Runtime-aware technical architecture, C4 layers, components, and tech debt for CSA. Use when Manager invokes Technology Architecture analysis.
---

# CSA Tech Architecture Skill

## Schema

Authoritative output/invocation contract: [schema.json](schema.json)

## Shared worker rules

Obey `csa5-specialist-worker` (do not restate). Output: `artifacts/architecture.json` including `deployment_topology`, `security_controls`, `cross_cutting_concerns`, `build_and_runtime`.

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

`csa5-gate-tech-architecture` — see `quality-rubric.md`.
