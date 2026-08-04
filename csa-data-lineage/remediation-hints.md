# Data Lineage Remediation Hints

| Gap | Fix |
|-----|-----|
| No sources | Parse JDBC URLs, hibernate/cfg, *.sql, DTS/SSIS, control-M/batch scripts |
| Missing field paths | Start from primary keys of core tables; trace DAO/SQL |
| Over-claiming field-level | Switch lineage_scope to table_level and document |
