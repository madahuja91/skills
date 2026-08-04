---
name: gate-tsa-document
description: Quality gate for TSA tsa_pack Markdown + HTML + Mermaid. Use when Completeness Validator evaluates that artifact.
---

# Gate: gate-tsa-document

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Pass requires

- Schema-valid artifact for `tsa_pack Markdown + HTML + Mermaid`
- Stack claims cite ADR; baseline cites CSA
- No invented technologies
- Blocking gaps listed when unresolved ADR decisions block design

Emit report with `gate_id: gate-tsa-document`.
