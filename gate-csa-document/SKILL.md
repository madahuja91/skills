---
name: gate-csa-document
description: Quality gate for lean csa_pack (5 Markdown docs + arc42 HTML + machine section JSON). Use after Document Assembler.
---

# Gate: CSA Document

## Schema

[`schema.json`](schema.json) · pack manifest `csa-document-assembler/schema.json` · policy `csa-rich-content`

## Pass requires

- Single `active_root`; `active-root-hygiene` pass
- **Shared memory present:** `_internal/swarm/{swarm_state.json,handoffs.jsonl,context_memory.md}`
- Machine section JSON for all 5 docs, schema-valid
- Markdown: `Executive_Summary.md`, `Business_Architecture.md`, `Application_Architecture.md`, `Data_and_Integration.md`, `Risks_Gaps_and_Traceability.md`, `README.md`
- HTML: `arc42-c4/{index,context,containers,components}.html`
- **Forbidden:** numbered `00`/`04`–`10` MD, C4-as-MD, mega-pack-only, epic/story seeds as required pack
- Mermaid required diagrams present
- section_min_rows + SSOT + anti-redundancy (Jaccard > 0.32 fails)

Emit `gate_id: gate-csa-document`.
