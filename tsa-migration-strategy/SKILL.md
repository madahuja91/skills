---
name: tsa-migration-strategy
description: Produce wave-based migration strategy (strangler/coexistence/cutover/rollback) from CSA gaps and TSA designs. Use when Manager invokes TSA Migration Strategy.
---

# TSA Migration Strategy

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Goal

Write `artifacts/migration_strategy.json` and feed `migration-strategy-pack`.

## Procedure

1. Choose pattern with justification (CSA risk + ADR constraints).
2. Define waves tied to capabilities/components/data units.
3. Cutover, rollback, exit criteria.
4. Required Mermaid: `diag-migration-waves`.
