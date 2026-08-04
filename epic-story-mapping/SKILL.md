---
name: epic-story-mapping
description: Maps CSA capabilities and traceability into Function, Epic, and Story seeds as Markdown for modernization backlog generation. Use during Document Assembler and epic-story readiness gate.
---

# Epic / Story Mapping

## Schema

Markdown seed contract: [schema.json](schema.json)

## Hierarchy

| Level | Definition | Primary CSA source |
|-------|------------|--------------------|
| Function | Business capability / bounded context slice | `business_capabilities`, domains |
| Epic | Cohesive delivery slice with data + integration ownership | capability + related INT/LIN/CMP |
| Story | Implementable change with AC hooks | BR / flow / screen / API |

## Output format (mandatory)

Write **Markdown** (not JSON) deliverables:

- `csa_pack/epic_story_seeds/functions.md`
- `csa_pack/epic_story_seeds/epics.md`
- `csa_pack/epic_story_seeds/stories.md`

Optional: keep structured copies under `csa_pack/machine/epic_story_seeds/` only if a downstream tool requires JSON — human pack remains Markdown.

## Markdown templates

### functions.md

```markdown
# Functions

## FN-<slug> — <Name>
- Description: ...
- Capability IDs: CAP-...
- Domain IDs: DOM-...
- CSA refs: `csa_pack/05_business_capabilities.md`, ...
```

### epics.md

```markdown
# Epics

## EP-<slug> — <Name>
- Function: FN-...
- Description: ...
- Data ownership: ...
- Integration IDs: INT-...
- Priority hint: high|medium|...
- CSA refs: `csa_pack/04_domain_model_ddd.md`, `csa_pack/arc42-c4/index.html`, ...
```

### stories.md

```markdown
# Stories

## US-<slug> — <Title>
- Epic: EP-...
- Capability: CAP-...
- Narrative: ...
- Trace IDs: BR-..., CMP-...
- Acceptance criteria hooks:
  - ...
- CSA refs: `csa_pack/09_traceability_matrix.md`, ...
```

## Rules

1. Every Function → ≥1 Epic.
2. Every Epic → CSA refs including Markdown section paths and/or `arc42-c4/*.html` and machine IDs.
3. Every Story → capability_id, ≥1 trace ID (BR-/CMP-/INT-/LIN-), and acceptance criteria hooks.
4. Do not invent capabilities not present in domain artifact; if needed, mark derived with reason.
5. Prefer modernization-oriented story phrasing without prescribing target tech unless in CSA.