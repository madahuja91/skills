---
name: csa-rich-content
description: Enforces concise, schema-driven CSA outputs with zero redundancy. Use for every specialist output, Document Assembler, and gate-csa-document validation.
---

# CSA Output Quality (schema-first)

## Schema

Depth and structure contract: [`schema.json`](schema.json)

## Core policy

1. **Schema over verbosity**: completeness is measured by required schema fields and evidence coverage, not by word count.
2. **SSOT**: tabular data appears once in its owning section. Never restate table rows as narrative paragraphs.
3. **Concise prose**: insights are bullet points (1–2 sentences), only for interpretation, risk, and implications.
4. **No fluff**: fail boilerplate, repeated summaries, and repeated evidence baselines.

## Specialist JSON quality

Specialist artifacts must be schema-valid, evidence-backed, and non-empty in required arrays.  
Use `unknown` with evidence trail instead of invented values.

## Pack quality rules (`csa_pack/`)

- Required Markdown files: `00`, `04`–`10`, `README.md`
- Required HTML files: `arc42-c4/index.html`, `context.html`, `containers.html`, `components.html`
- No epic/story seed outputs
- No C4 Markdown files

### Redundancy controls

- Do not duplicate full inventory tables across multiple Markdown files.
- Do not duplicate the same risk register in more than one section.
- Do not duplicate full domain catalogs outside `04`.
- Do not duplicate full integration catalogs outside `07`.
- Do not duplicate full lineage matrices outside `06` / `09`.

### `index.html` policy

`index.html` is the consolidated hub and may summarize all concerns.  
Markdown files remain section-specific deep dives and must cross-link to owner sections when needed.

## Completeness enforcement

For `gate-csa-document`, Completeness must fail when:

1. Required files are missing (`required_files_present`)
2. Required schemas are invalid (`schema_conformance`)
3. Section ownership is violated (`section_ownership_violation`)
4. Markdown siblings are overly similar (`section_anti_redundancy`)
5. Tables are repeated as prose (`table_prose_duplication`)
6. Pack shape is wrong (mega-pack/report-only substitute)
