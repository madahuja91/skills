---
name: csa7-arc42-c4-views
description: Builds arc42-aligned HTML CSA architecture hub with full anchors, Mermaid diagrams, and C4 detail pages. Incomplete index or missing diagrams = Completeness FAIL.
---

# arc42 + C4 Views (HTML)

## Schema

[`schema.json`](schema.json) · also `csa7-mermaid-diagrams`

## Output (mandatory)

```text
csa_pack/arc42-c4/
  index.html           # PRIMARY hub — full anchors + ≥2 Mermaid diagrams
  context.html         # C4 L1 + diag-c4-context
  containers.html      # C4 L2 + diag-c4-containers
  components.html      # C4 L3 + diag-c4-components
```

HTML only — never Markdown C4 pages.

## HARD: `index.html` is a full hub (not a stub)

A short summary + three links **FAILS**. Humans open `index.html` first.

### Required anchors (all 12 — nav must link each)

| Anchor | Content |
|--------|---------|
| `#overview` | System name, purpose, scope, confidence |
| `#inventory` | Discovery counts + module/evidence table |
| `#stack` | Observed languages, app server, DB, messaging |
| `#architecture` | ≥1 Mermaid (exec overview); legend |
| `#domains` | Domains / capabilities table |
| `#data` | Stores, packages/SPs, critical lineage |
| `#integrations` | Integration catalog (MQ/SOAP/HTTP/CORBA/…) |
| `#c4` | Actors/externals/containers/CMP-* tables + links to detail pages |
| `#runtime` | Packaging, runtime evidence, debt highlights |
| `#risks` | Ranked risks / gaps / assumptions |
| `#traceability` | Capability↔component↔integration↔lineage table |
| `#pack` | Links to the 5 named MD docs + `./context.html` etc. |

### Mermaid on index (blocking)

- ≥2 `<pre class="mermaid">` blocks (e.g. exec overview + C4 context or containers)
- Classic Mermaid runtime (`mermaid.min.js` + `mermaid.run`) — **not** ESM-only
- Still emit diagram source if CDN 401 — do not drop diagrams

### Detail pages (blocking)

| File | Required Mermaid |
|------|------------------|
| `context.html` | `diag-c4-context` |
| `containers.html` | `diag-c4-containers` |
| `components.html` | `diag-c4-components` |

Each page: ≥1 Mermaid block + classic runtime.

## Sources

`architecture.c4_views` + discovery + domain + lineage + integration. Empty `c4_views` → Completeness FAIL with `target_agent_id: tech_architecture` for Manager re-run.

## Fail → Manager re-run

| Gap | `target_agent_id` |
|-----|-------------------|
| Empty/thin `c4_views` | `tech_architecture` |
| Thin domain for `#domains` | `business_domain` |
| Thin lineage for `#data` | `data_lineage` |
| Thin integrations for `#integrations` | `integration` |
| Artifacts rich but index/diagrams not rendered | `completeness_validator` (re-run FINAL) |

## Anti-patterns

- Stub index (overview + links only)
- Missing required anchors
- No Mermaid / ESM-only init that never paints
- Extra Markdown under `csa_pack/` as a C4 substitute (C4 lives in `arc42-c4/*.html` only)
- TSA migration framing as primary content
