---
name: gate-tsa-data
description: Quality gate for TSA target_data.json. Use when Completeness Validator evaluates that artifact.
---

# Gate: gate-tsa-data

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Pass requires

- Schema-valid artifact for `target_data.json`
- Stack claims cite ADR; baseline cites CSA
- No invented technologies
- Blocking gaps listed when unresolved ADR decisions block design

Emit report with `gate_id: gate-tsa-data`.
