---
name: tsa-document-assembler
description: Assembles TSA outputs deterministically from JSON artifacts into ADR and Migration Markdown deliverables.
---

# TSA Document Assembler

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Output format (mandatory)

| Deliverable | Format |
|-------------|--------|
| `ADR_Blueprint.md` | **Markdown** (`.md`) |
| `Migration_Strategy.md` | **Markdown** (`.md`) |
| Specialist copies | `machine/*.json` (internal) |

Do not generate extra narrative packs in this workflow mode.

Write everything under the single `swarm_state.active_root` on disk (no `src/src`). Never invent `/app/temp/csa-run` or a sibling `outputs/` tree outside ACTIVE_ROOT.

## Outputs

```text
ACTIVE_ROOT/tsa_pack/
  ADR_Blueprint.md
  Migration_Strategy.md
  machine/
    adr_blueprint.json
    migration_strategy.json
```

## Rendering rules

1. Render from JSON deterministically (template-style).
2. Do not re-invent facts beyond `artifacts/adr_blueprint.json` and `artifacts/migration_strategy.json`.
3. Keep concise tables, decision bullets, and explicit traceability.
