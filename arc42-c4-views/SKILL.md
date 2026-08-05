---
name: arc42-c4-views
description: Builds a rich arc42-aligned HTML CSA/TSA architecture site — comprehensive index.html hub plus C4 Context/Container/Component pages with Mermaid. Use when assembling architecture visualization outputs.
---

# arc42 + C4 Views (HTML index)

## Schema

HTML pack manifest contract: [schema.json](schema.json)

Also obey: `skills/standards/mermaid-diagrams/SKILL.md` and `csa-rich-content` (HTML depth floors).

## Output format (mandatory)

C4 / arc42 building-block views are **HTML only** — never Markdown.

```text
csa_pack/arc42-c4/   (or tsa_pack/arc42-c4/)
  index.html           # PRIMARY deliverable — rich single-page architecture hub
  context.html         # C4 Level 1 System Context + Mermaid diag-c4-context
  containers.html      # C4 Level 2 Containers + Mermaid diag-c4-containers
  components.html      # C4 Level 3 critical Components + Mermaid diag-c4-components
```

## HARD: `index.html` is the rich hub (not a stub nav page)

Humans open **`index.html` first**. It must be a **long, self-contained documentation page** (reference quality like a full architecture site: meta stats strip, sticky section nav, many tables, embedded Mermaid, prose).  
A short “summary + three links” page **FAILS** Completeness.

### Do include (CSA — current state)

Anchor IDs required (nav must link to these):

| Anchor id | Section | Content (evidence-backed only) |
|-----------|---------|--------------------------------|
| `#overview` | Current-state overview | System name, purpose, scope, confidence, analysis_scope |
| `#inventory` | Discovery inventory | Counts by type (Java/JSP/WAR/EAR/SQL/packages/configs/MQ/CORBA/etc.), module table, top evidence paths |
| `#stack` | Technology stack | Languages, app server, persistence (iBatis/TopLink/JDBC/Oracle), messaging, integration tech — as **observed**, not target |
| `#architecture` | Architecture diagrams | Mermaid: exec overview + C4 context (and containers if space); legend |
| `#domains` | Domains & capabilities | Domains, entities, capabilities tables; ubiquitous language notes |
| `#data` | Data & lineage | Data sources, packages/SPs, critical field lineage, transformation chains |
| `#integrations` | Integration landscape | Catalog table (MQ/SOAP/HTTP/CORBA/files), inbound/outbound, reliability gaps |
| `#c4` | C4 building blocks | Summary tables for actors/externals, containers, critical `CMP-*`; links to detail pages |
| `#runtime` | Runtime / ops / debt | Packaging, runtime evidence or unknowns, tech-debt register |
| `#risks` | Gaps / risks / assumptions | Ranked risks, missing evidence, assumptions |
| `#traceability` | Traceability | Capability↔component↔integration↔lineage matrix (HTML table) |
| `#pack` | Pack links | Links to Markdown sections `../00_…` … `../10_…` and `./context.html` etc. |

### Do NOT copy TSA/migration content into CSA index

Skip or omit for **CSA** (those belong in TSA packs):

- Target microservices decomposition / Fargate / schema-per-service target design
- Migration effort estimates / timelines / team sizing
- “Legacy → cloud migration” as the primary framing
- Target OpenAPI/Swagger of future services (unless the **legacy** codebase already has API specs — then document as-is APIs only)

CSA framing = **as-is / current state**. You may include a short “modernization readiness scorecard” (dimensions + scores from evidence) under `#overview` or `#risks` — not a full migration strategy.

### Depth floors for `index.html`

See `csa-rich-content`: **≥5000 words** of real HTML text (strip tags for counting), **≥8 HTML tables**, **≥2 Mermaid diagrams** embedded with runtime init, **all required anchors** present with non-empty sections.

### UI polish (match reference richness, not stub chrome)

- Single-page layout with header, meta-stat cards (counts), horizontal/sticky nav to anchors
- Inline CSS (self-contained); readable typography; tables with headers
- Optional cards/grids for domains/capabilities — content density matters more than decoration
- Mermaid CDN ESM init on `index.html` (and on C4 detail pages)

## Detail pages (`context` / `containers` / `components`)

Still required. Each must be substantial (≥800 words) with its required Mermaid diagram — they deepen C4; they do **not** replace the rich index.

| File | Must show | Required Mermaid |
|------|-----------|------------------|
| `context.html` | People/actors, system boundary, external systems | `diag-c4-context` |
| `containers.html` | Deployables (WAR/EAR/services/batch) | `diag-c4-containers` |
| `components.html` | Critical `CMP-*`; link to capabilities | `diag-c4-components` |

## Mermaid rendering in HTML (mandatory)

Follow `mermaid-diagrams`:

- `index.html` MUST contain ≥2 `<pre class="mermaid">` blocks and Mermaid runtime init.
- Each of `context.html`, `containers.html`, `components.html` MUST contain ≥1 Mermaid block + runtime init.
- Diagram content from accepted artifacts only — never invent externals/containers.

## HTML conventions

- Self-contained page chrome (inline CSS preferred).
- Relative links only.
- Semantic headings (`h1`–`h3`), tables for structured facts.
- Do not emit `01_system_context_c4.md` / `02_*.md` / `03_*.md`.

## Sources

Build from accepted `architecture.c4_views` + discovery + domain + lineage + integration (+ quality gaps). Expand inventories into tables — do not invent.

## arc42 alignment

- Context & scope → `#overview` + `context.html`
- Building block view → `#architecture` / `#c4` + containers/components pages
- Runtime / risks → `#runtime` / `#risks` (also Markdown `08` / `10`)
