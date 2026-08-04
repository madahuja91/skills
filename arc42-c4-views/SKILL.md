---
name: arc42-c4-views
description: Builds arc42-aligned C4 Context/Container/Component views as an HTML index site with mandatory Mermaid diagrams. Use when assembling architecture visualization outputs.
---

# arc42 + C4 Views (HTML index)

## Schema

HTML pack manifest contract: [schema.json](schema.json)

Also obey: `skills/standards/mermaid-diagrams/SKILL.md`

## Output format (mandatory)

C4 / arc42 building-block views are **HTML only** — never Markdown.

```text
csa_pack/arc42-c4/
  index.html           # entry index — nav + summary + links to all views
  context.html         # C4 Level 1 System Context + Mermaid diag-c4-context
  containers.html      # C4 Level 2 Containers + Mermaid diag-c4-containers
  components.html      # C4 Level 3 critical Components + Mermaid diag-c4-components
```

`index.html` is the **single entry point** humans open. It must include:

1. Title + system name
2. Short current-state summary (1–2 paragraphs)
3. Navigation links to `context.html`, `containers.html`, `components.html`
4. Optional arc42 section anchors / notes (context & scope, building blocks)
5. Evidence/confidence footnotes where useful

## Page content rules

| File | Must show | Required Mermaid |
|------|-----------|------------------|
| `context.html` | People/actors, system boundary, external systems | `diag-c4-context` (`C4Context` or `flowchart`) |
| `containers.html` | Deployables (WAR/EAR/services/batch); one container for monolith unless proven distributed | `diag-c4-containers` (`C4Container` or `flowchart`) |
| `components.html` | Critical `CMP-*` only; link IDs to capabilities | `diag-c4-components` (`C4Component` or `flowchart`) |

## Mermaid rendering in HTML (mandatory)

Follow `mermaid-diagrams`:

- Each of `context.html`, `containers.html`, `components.html` MUST contain at least one `<pre class="mermaid">...</pre>` block.
- Each of those pages MUST load Mermaid runtime (CDN ESM) and initialize it.
- Diagram content must come from accepted artifacts only — never invent externals/containers.

## HTML conventions

- Self-contained page chrome (inline CSS preferred).
- Relative links only (`./context.html`, etc.).
- Semantic headings (`h1`–`h3`), tables or definition lists for structured facts.
- Mermaid CDN is required for browser diagram rendering (see `mermaid-diagrams`).
- Do not emit `01_system_context_c4.md` / `02_*.md` / `03_*.md`.

## Sources

Build from accepted `architecture.c4_views` + discovery + integration (+ domain for actors). Do not invent externals/containers.

## arc42 alignment (selected)

- Context & scope → `index.html` summary + `context.html`
- Building block view → `containers.html` / `components.html`
- Runtime / risks remain in Markdown pack sections `08` / `10` (not HTML)
