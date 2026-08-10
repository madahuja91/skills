# TSA Migration Strategy v2

## Role
Generate the migration strategy only after explicit Human Review approval of the TSA.

## Preconditions
Required:
- approved TSA specification
- approved diagrams
- approved ADR blueprint
- successful TSA quality gate
- Human Review decision = APPROVE

## Output
Produce:
- src/artifacts/migration_strategy.json
- source material for Completeness to render Migration_Strategy.md

## Coverage
- migration scope
- application/workload inventory
- 6R disposition
- migration waves
- sequencing
- dependencies
- coexistence
- data migration
- CDC where applicable
- testing strategy
- cutover
- rollback/fallback
- readiness criteria
- risks
- governance
- post-migration validation

## Hard Rules
- Never run before Human Review APPROVE.
- Never modify the approved TSA.
- Never invent ADR decisions.
- Reference accepted architecture and ADR artifacts.
- JSON is authoritative.
- Use ACTIVE_ROOT only.
