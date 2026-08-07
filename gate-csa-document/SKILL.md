---
name: gate-csa-document
description: Quality gate for lean 5-doc csa_pack + arc42-c4 HTML. Completeness renders and self-gates in FINAL mode. No machine/, no epic-story, no numbered 00/04-10 packs.
---

# Gate: CSA Document

## Schema

[`schema.json`](schema.json) · policy `csa-rich-content` · ownership `csa-section-boundaries`

Substance contracts (validate content; do not require writing machine JSON):

- `csa-rich-content`
- `csa-section-boundaries`
- `arc42-c4-views`
- `mermaid-diagrams`
- Pack output schemas: `Executive_Summary`, `Business_Architecture`, `Application_Architecture`, `Data_and_Integration`, `Risks_Gaps_and_Traceability`

## Who renders

**Completeness-Validation-Agent** renders and runs this gate in the same FINAL turn. No Document Assembler.

## Pass requires

- `ACTIVE_ROOT=src` preferred; `active-root-hygiene` pass
- Shared memory under `_internal/swarm/`
- Accepted specialist artifacts (schema-complete enough to feed pack)
- On disk under **`src/csa_pack/`**:
  - `Executive_Summary.md`
  - `Business_Architecture.md`
  - `Application_Architecture.md`
  - `Data_and_Integration.md`
  - `Risks_Gaps_and_Traceability.md`
  - `README.md`
  - `arc42-c4/{index,context,containers,components}.html`
- Required Mermaid IDs present
- Pack = legacy codebase evidence only (no workflow meta)

## HARD fail

- Any required pack file missing
- Chat-only / gate-report-only final
- Numbered `00_`/`04_`–`10_` client docs present as primary pack
- `epic_story_seeds/` required or blocking
- `deliverables/` or `csa_pack/machine/` required
- Gate id other than `gate-csa-document`

## Remediation

On fail caused by thin specialist substance, set `target_agent_id` to the owner specialist so Manager re-runs that agent.

Emit `gate_id: gate-csa-document`.
