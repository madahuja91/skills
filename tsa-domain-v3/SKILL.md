# TSA Domain and ADR v2

## Role
Derive architecture decisions from the accepted target-state architecture and domain model.

## Output
Write machine-readable ADR content under:
src/artifacts/adr_blueprint.json

Provide the source material for the human-readable ADR section rendered by Completeness.

## ADR Requirements
Each decision should include:
- ID
- title
- context
- problem
- decision drivers
- options considered
- selected option
- rationale
- trade-offs
- consequences
- risks
- dependencies
- CSA evidence
- TSA references
- migration impact

## Hard Rules
- Do not invent decisions unrelated to the TSA.
- Preserve accepted decisions during review rework unless explicitly changed by human review.
- Update only impacted ADRs when possible.
- JSON is authoritative.


## Client ADR Reconciliation (v8+)
During POST_REVIEW_CHANGE, the client may provide a modified ADR.

Required inputs:
- `src/artifacts/adr_blueprint.json`
- `src/artifacts/tsa_specification.json`
- mandatory client ADR
- Human Review feedback

Rules:
- Preserve the generated ADR as the baseline for traceability.
- Treat the client ADR as authoritative for explicitly changed decisions.
- Identify conflicts between generated and client ADRs.
- Reconcile only impacted decisions.
- Produce `src/artifacts/reconciled_adr_blueprint.json`.
- Include traceability from each reconciled decision to the client ADR and affected TSA decisions.
- Do not invent new architecture decisions beyond the client ADR, accepted TSA, or CSA evidence.
