---
name: tsa-tech-architecture
description: Design target technical architecture and C4 views using ADR stack decisions and CSA baseline. Use when Manager invokes TSA Tech Architecture.
---

# TSA Tech Architecture

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Goal

Write `artifacts/target_architecture.json` with C4 views for Assembler + `arc42-c4-views` / `mermaid-diagrams`.

## HARD

Use only stack from `stack_decisions.json`. One container topology consistent with ADR (e.g. services vs modular monolith).
