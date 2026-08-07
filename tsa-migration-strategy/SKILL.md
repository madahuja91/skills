---
name: tsa-migration-strategy
description: Produce wave-based migration strategy (strangler/coexistence/cutover/rollback) from CSA gaps and TSA designs. Use when Manager invokes TSA Migration Strategy.
---

# TSA Migration Strategy

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Goal

Write `artifacts/migration_strategy.json` aligned to enterprise migration standards.

## Procedure

1. Build 6Rs application disposition matrix for CSA legacy components.
2. Define wave planning with dependencies and estimated durations.
3. Specify coexistence and data sync mechanics (CDC/dual-write/reconciliation).
4. Define testing/verification strategy (shadow/dark/canary/load) and rollback triggers.
5. Build cutover and fallback playbook with go/no-go criteria.
