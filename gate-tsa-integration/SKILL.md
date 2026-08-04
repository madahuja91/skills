---
name: gate-tsa-integration
description: Quality gate for TSA target_integration.json. Use when Completeness Validator evaluates that artifact.
---

# Gate: gate-tsa-integration

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Pass requires

- Schema-valid artifact for `target_integration.json`
- Stack claims cite ADR; baseline cites CSA
- No invented technologies
- Blocking gaps listed when unresolved ADR decisions block design

Emit report with `gate_id: gate-tsa-integration`.
