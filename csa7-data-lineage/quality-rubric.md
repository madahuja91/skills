# Data Lineage Quality Rubric

| Metric | Pass threshold | Blocking |
|--------|----------------|----------|
| Schema conformance | 100% | yes |
| ≥1 data source | required | yes |
| Primary entities (from domain/DDL) have lineage path | ≥80% | yes |
| field_lineage or documented table-level with justification | required | yes |
| Evidence on lineage entries | ≥60% non-inferred | yes |
| lineage_scope matches depth delivered | required | warn |
