---
name: gate-tsa-tech
description: Quality gate for TSA target_architecture.json. Use when Completeness Validator evaluates that artifact.
---

# Gate: gate-tsa-tech

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Pass requires

- Schema-valid artifact for `target_architecture.json`
- Stack claims cite ADR; baseline cites CSA
- No invented technologies
- Blocking gaps listed when unresolved ADR decisions block design

Emit report with `gate_id: gate-tsa-tech`.
