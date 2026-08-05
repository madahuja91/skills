---
name: csa-tech-architecture
description: Runtime-aware technical architecture, C4 layers, components, and tech debt for CSA. Use when Manager invokes Technology Architecture analysis.
---

# CSA Tech Architecture Skill

## Schema

Authoritative output/invocation contract: [schema.json](schema.json)


## Goal

Write `artifacts/architecture.json` per `schema.json`. Populate `c4_views` for Assembler.

## Procedure

1. Map presentation/business/data/integration/infrastructure layers from code + configs.
2. Register components with `CMP-*` IDs and evidence.
3. Compare static structure vs runtime (logs/APM) when available; else mark `analysis_scope: static`.
4. Score technical debt; list dead/orphan candidates honestly.
5. Fill C4 context/containers/critical components for Assembler Mermaid (`mermaid-diagrams` + `arc42-c4-views`).

## HARD: Depth (`csa-rich-content`)

Emit dense layers/components/C4 elements with evidence. Tiny 3-component stubs fail Completeness.

## Anti-patterns

- Do not claim runtime validation without logs/traces.
- Do not invent microservices topology for a monolith WAR/EAR.
- Do not emit outline-only stubs to “finish fast”.

## Gate

`gate-tech-architecture` — see `quality-rubric.md`.
