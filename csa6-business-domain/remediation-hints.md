# Business Domain Remediation Hints

| Gap | Fix |
|-----|-----|
| Rules without location | Re-read service/validation/stored-proc files from Discovery code inventory |
| Empty capabilities | Derive from screen menus, use-case packages, batch job names |
| Duplicate domains | Merge via canonical_name; record in normalization_details |
| All inferred | Prefer code paths; demote confidence; list missing_business_logic |
