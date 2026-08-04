---
name: csa-completeness-validator
description: Validates CSA specialist artifacts against JSON Schema and gate rubrics; emits pass/fail gate reports with remediation briefs. Use after every specialist run as Manager subagent.
---

# Completeness Validation Agent Skill

## Schema

Authoritative output/invocation contract: [schema.json](schema.json)


## Role

Subagent invoked by CSA Architecture Manager **after every specialist** (and Assembler). Never invent architecture content; only evaluate.

## Inputs

```json
{
  "artifact_path": "artifacts/discovery.json",
  "gate_id": "gate-discover",
  "attempt": 1,
  "max_reruns": 2,
  "prior_context": "optional notes from Manager"
}
```

## Procedure

1. Load agent skill schema + `quality-rubric.md` for the gate.
2. Validate JSON Schema; score `schema_conformance`.
3. Apply rubric metrics for evidence, completeness, confidence.
4. Build `blocking_gaps` (critical/high that block acceptance) and `warnings`.
5. If fail: write `remediation_brief` using agent `remediation-hints.md`.
6. Write report to `artifacts/quality_gate_reports/{gate_id}-{artifact_stem}.json`.
7. Return report JSON to Manager.

## Mapping gate → skill

| gate_id | artifact | rubric source |
|---------|----------|---------------|
| gate-discover | discovery.json | agents/csa-discover |
| gate-business-domain | domain.json | agents/csa-business-domain |
| gate-tech-architecture | architecture.json | agents/csa-tech-architecture |
| gate-data-lineage | lineage.json | agents/csa-data-lineage |
| gate-integration | integration.json | agents/csa-integration |
| gate-csa-document | csa_pack/ (MD + arc42-c4 HTML + required Mermaid) | agents/csa-document-assembler |
| gate-epic-story-readiness | epic_story_seeds/*.md | standards/epic-story-mapping |

## Rules

- Do not soft-pass invented stacks or missing evidence on critical claims.
- `max_reruns` is always 2 (Manager-enforced).
- Prefer concrete `files_to_revisit` over vague advice.

## Self quality bar

See `quality-rubric.md`.
