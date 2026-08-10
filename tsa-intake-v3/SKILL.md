# TSA Intake v2

## Role
Convert the CSA pack into a machine-readable TSA intake baseline.

## Output
Write only:
- src/artifacts/intake.json
- required shared-memory handoff under ACTIVE_ROOT

## Content
Capture:
- scope and business context
- current-state applications/components
- domains and bounded contexts
- data and persistence
- integrations and APIs
- infrastructure/cloud
- security
- deployment/runtime
- observability
- NFRs
- constraints
- assumptions
- risks
- gaps
- evidence references

## Hard Rules
- JSON only for the intake artifact.
- Do not create client-facing Markdown.
- Do not design target architecture.
- Every material fact must be traceable to CSA evidence.
- Never invent missing information.
- Use ACTIVE_ROOT only.
