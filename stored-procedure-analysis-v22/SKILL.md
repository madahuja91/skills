---
name: stored-procedure-analysis-v22
description: >-
  Extract complete stored-procedure business logic into schema-complete JSON so backlog artifacts can inline real rules, data operations, and migration behavior instead of references.
---

# Stored Procedure Analysis

Authoritative skill definition (identical to `skill.yaml` / `schema.json`):

```yaml
skill:
  id: stored-procedure-analysis
  name: Stored Procedure Analysis
  version: 2.0.0
  purpose: Extract complete stored-procedure business logic into schema-complete JSON so backlog artifacts can inline real rules, data operations, and migration behavior instead of references.
  responsibility:
    owns:
    - SP metadata, parameters, tables, control flow, and data transformations
    - numbered business rules extracted from SP logic, fully written (not cited)
    - error handling, transactions, and SP-to-SP dependencies
    does_not_own:
    - Epic/Feature titles
    - UI/BFF LLD
  inputs:
    required:
    - codebase
    optional:
    - csa_output
  output:
    schema: stored_procedure
    required_fields:
    - id
    - procedure_name
    - schema_name
    - purpose
    - parameters
    - tables_accessed
    - functions_called
    - control_flow
    - business_rules
    - data_transformations
    - error_handling
    - transactions
    - dependencies
    - current_behavior
    - target_intent
    - migration_considerations
    - traceability
  content_rules:
    must:
    - Document every parameter with name, type, direction, default, and usage.
    - List every table with operation (SELECT/INSERT/UPDATE/DELETE/MERGE) and key columns.
    - Write each business rule as condition + action + exception (no BR/ADR/migration pointers).
    - Describe control flow as readable steps (IF/ELSE, loops, TRY/CATCH) with real predicates.
    - Inline migration/coexistence/cutover/rollback behavior that this SP implies; do not cite a migration document.
    must_not:
    - Write see SP, see ADR, see migration_strategy, refer BR-###, as documented in.
    - Skip dynamic SQL, transactions, or error paths.
    - Use empty arrays for mandatory content when evidence exists.
  schema_completeness_gate:
    rule: STRICT schema compliance — All output.required_fields must be present and non-empty prose (not references) before status=complete
  dual_write:
    json_root: src/artifacts/canonical/backlog/
    markdown_root: src/artifacts/projections/backlog/
    when: parallel_same_stage_via_markdown_renderer
    governance_pass_required: false
  workspace_disk:
    read_roots:
    - uploaded codebase path
    - extracted/
    - ../files/
    write_paths:
    - src/artifacts/packages/stored-procedure-evidence.json
    - src/artifacts/packages/stored-procedures/
    forbid:
    - /app/temp as write root
    - inventing absolute temp trees
    rule: Read SQL from workspace disk; write evidence only under src/artifacts/. Cite workspace-relative paths, never /app/temp as stored location.
```
