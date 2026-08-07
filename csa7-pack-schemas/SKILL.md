---
name: csa7-pack-schemas
description: Pack substance contracts for Completeness FINAL — five lean Markdown docs + README + arc42-c4 HTML. Use only these schemas; do not invent alternate pack filenames.
---

# CSA Pack Schemas

## Purpose

Completeness FINAL builds **pack substance** JSON and renders Markdown that must satisfy these contracts 100%.

## Allowed client files only

Under `src/csa_pack/`:

| File | Schema |
|------|--------|
| `Executive_Summary.md` | `output-schemas/Executive_Summary.schema.json` |
| `Business_Architecture.md` | `output-schemas/Business_Architecture.schema.json` |
| `Application_Architecture.md` | `output-schemas/Application_Architecture.schema.json` |
| `Data_and_Integration.md` | `output-schemas/Data_and_Integration.schema.json` |
| `Risks_Gaps_and_Traceability.md` | `output-schemas/Risks_Gaps_and_Traceability.schema.json` |
| `README.md` | pack index (links to the five docs + `arc42-c4/index.html`) |
| `arc42-c4/{index,context,containers,components}.html` | `csa7-arc42-c4-views` + `csa7-mermaid-diagrams` |

**No other Markdown under `csa_pack/`.** Extra or alternate filenames = FAIL (`pack_shape_valid`).

## HARD rules

1. Validate pack substance against each schema’s `required[]` before writing MD.
2. Every required field must appear as an explicit heading/table/list in the owner MD.
3. Min **200 lines** per client MD; more is fine; never a max length.
4. Required Mermaid IDs per `csa7-mermaid-diagrams` (blocking).
5. Do **not** write `deliverables/`, `csa_pack/machine/`, or epic-story seeds.
6. Do **not** use Document Assembler — Completeness owns render.

## Bundle

See [`output-schemas/csa-pack-schema-bundle.json`](output-schemas/csa-pack-schema-bundle.json).

## HARD — knowledge-first contracts

These schemas require narrative sections and `evidence_appendix`.
Markdown must follow narrative order; Evidence Mapping appendix last. No maxLength.
