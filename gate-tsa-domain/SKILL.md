---
name: gate-tsa-domain
description: Quality gate for TSA target_domain.json. Use when Completeness Validator evaluates that artifact.
---

# Gate: gate-tsa-domain

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Pass requires

- Schema-valid artifact for `target_domain.json`
- Stack claims cite ADR; baseline cites CSA
- No invented technologies
- Blocking gaps listed when unresolved ADR decisions block design

Emit report with `gate_id: gate-tsa-domain`.
