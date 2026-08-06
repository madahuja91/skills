---
name: tsa-intake
description: Ingest CSA pack only; emit intake.json and provisional stack_decisions.json from CSA evidence. Use when Manager invokes TSA Intake.
---

# TSA Intake

## Schema

Authoritative contract: [`schema.json`](schema.json)

## Goal

Write `artifacts/intake.json` and `artifacts/stack_decisions.json` from the CSA pack only. No separate TargetSpec is required.

## Procedure

1. Inventory CSA pack sections + machine JSON from the uploaded CSA pack zip.
2. Summarize current-state domains/capabilities/components/integrations/risks as baseline.
3. Derive provisional stack decisions only from CSA evidence; mark inferred items and unknowns clearly.
4. Flag missing CSA evidence that blocks synthesis.
5. Sync shared memory.
