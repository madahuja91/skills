---
name: gate-tsa-document
description: Quality gate for TSA final Markdown deliverables (ADR blueprint and migration strategy).
---

# Gate: gate-tsa-document

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Pass requires

- Schema-valid `tsa_pack` under single `active_root` (no `src/src`)
- Required docs present: `tsa_pack/ADR_Blueprint.md`, `tsa_pack/Migration_Strategy.md`
- Markdown rendered deterministically from `artifacts/adr_blueprint.json` and `artifacts/migration_strategy.json`
- Stack claims cite ADR; baseline cites CSA
- No invented technologies
- Blocking gaps listed when unresolved ADR decisions block design
- `active-root-hygiene` pass (duplicates removed; no remaining nested roots)

Emit report with `gate_id: gate-tsa-document`.
