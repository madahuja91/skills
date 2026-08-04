---
name: tsa-intake
description: Ingest CSA pack + ADR/target spec; emit intake.json and stack_decisions.json. Use when Manager invokes TSA Intake.
---

# TSA Intake

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Goal

Write `artifacts/intake.json` and `artifacts/stack_decisions.json` (via `target-stack-contract`).

## Procedure

1. Inventory CSA pack sections + machine JSON.
2. Parse ADR/target spec for stack decisions — unresolved if missing.
3. List reusable CSA domains/capabilities/components/integrations as baseline.
4. Flag conflicts and missing inputs.
5. Sync shared memory.
