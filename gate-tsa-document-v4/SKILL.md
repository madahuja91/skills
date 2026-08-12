---
name: gate-tsa-document-v4
description: Quality gate for TSA human-readable pack and diagrams - validates Target_State_Architecture, Architecture_Views, ADR_Blueprint, diagram catalog consistency.
---

# TSA Document Gate v3

## Role
Validate the client-readable TSA document, architecture views, and diagram pack.

## Validate
- required sections exist
- every major architecture decision is represented
- diagrams exist and are referenced correctly
- diagram labels/components match TSA JSON
- ADR references are valid
- CSA evidence traceability is preserved
- no placeholders or unsupported claims
- Markdown is readable for a client reviewer
- JSON-to-Markdown consistency
- architecture_diagrams.json and tsa_document.json agree with pack files

## Required document set
- src/tsa_pack/Target_State_Architecture.md
- src/tsa_pack/Architecture_Views.md
- src/tsa_pack/ADR_Blueprint.md
- src/tsa_pack/diagrams/*.mmd (sources only; no HTML required)
- Migration_Strategy.md when migration has been generated

## Hard Rules
- Fail if a required diagram is missing.
- Fail if Markdown contradicts authoritative JSON.
- Fail if a diagram contains invented architecture.
- Report exact artifact/section causing failure.

## CHANGE-cycle Validation
Validate that the client-provided ADR and reconciled ADR are reflected in:
- ADR_Blueprint.md
- Target_State_Architecture.md
- Architecture_Views.md
- generated diagram assets

Fail when the client ADR is not traceable, when Markdown contradicts the reconciled JSON, or when diagrams contradict the revised TSA.
