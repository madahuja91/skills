# TSA Document Gate v2

## Role
Validate the client-readable TSA document and architecture views.

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

## Required document set
- Target_State_Architecture.md
- Architecture_Views.md
- ADR_Blueprint.md
- Migration_Strategy.md when migration has been generated

## Hard Rules
- Fail if a required diagram is missing.
- Fail if Markdown contradicts authoritative JSON.
- Fail if a diagram contains invented architecture.
- Report exact artifact/section causing failure.


## CHANGE-cycle Validation (v8+)
Validate that the client-provided ADR and reconciled ADR are reflected in:
- ADR_Blueprint.md
- Target_State_Architecture.md
- Architecture_Views.md
- generated diagram assets

Fail when the client ADR is not traceable, when Markdown contradicts the reconciled JSON, or when diagrams contradict the revised TSA.
