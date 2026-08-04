---
name: gate-tsa-migration
description: Quality gate for TSA migration_strategy.json. Use when Completeness Validator evaluates that artifact.
---

# Gate: gate-tsa-migration

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Pass requires

- Schema-valid artifact for `migration_strategy.json`
- Stack claims cite ADR; baseline cites CSA
- No invented technologies
- Blocking gaps listed when unresolved ADR decisions block design

Emit report with `gate_id: gate-tsa-migration`.
