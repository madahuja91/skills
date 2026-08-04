---
name: gate-tsa-intake
description: Quality gate for TSA intake.json / stack_decisions. Use when Completeness Validator evaluates that artifact.
---

# Gate: gate-tsa-intake

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Pass requires

- Schema-valid artifact for `intake.json / stack_decisions`
- Stack claims cite ADR; baseline cites CSA
- No invented technologies
- Blocking gaps listed when unresolved ADR decisions block design

Emit report with `gate_id: gate-tsa-intake`.
