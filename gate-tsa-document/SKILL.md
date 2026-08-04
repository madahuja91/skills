---
name: gate-tsa-document
description: Quality gate for TSA tsa_pack Markdown + HTML + Mermaid. Use when Completeness Validator evaluates that artifact.
---

# Gate: gate-tsa-document

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Pass requires

- Schema-valid `tsa_pack` under single `active_root` (no `src/src`)
- Narrative sections + epic seeds: **Markdown only**
- arc42/C4: **HTML** under `tsa_pack/arc42-c4/` only (never C4 `.md`)
- Required Mermaid present (MD fences + HTML `pre.mermaid`)
- Stack claims cite ADR; baseline cites CSA
- No invented technologies
- Blocking gaps listed when unresolved ADR decisions block design
- `active-root-hygiene` pass (duplicates removed; no remaining nested roots)

Emit report with `gate_id: gate-tsa-document`.
