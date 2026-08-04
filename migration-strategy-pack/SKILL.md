---
name: migration-strategy-pack
description: Standard structure for TSA migration strategy Markdown — waves, strangler/coexistence, cutover, rollback. Use during Migration Strategy agent and Assembler.
---

# Migration Strategy Pack

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Section outline (`08_migration_strategy_roadmap.md`)

1. Strategy pattern (strangler / coexistence / big-bang — justify from CSA+ADR)
2. Wave plan (capabilities/components per wave)
3. Data migration & cutover approach
4. Integration coexistence (legacy MQ/API bridges)
5. Rollback & risk controls
6. Exit criteria per wave

## Required Mermaid

`diag-migration-waves` — flowchart of waves and dependencies.
