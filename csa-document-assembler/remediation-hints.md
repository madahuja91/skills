# Document Assembler Remediation Hints

| Gap | Fix |
|-----|-----|
| Missing MD section | Generate from corresponding machine artifact; if data absent, write stub with explicit GAP |
| Missing HTML C4 index | Run `arc42-c4-views`; create `arc42-c4/index.html` + three view pages |
| C4 written as `.md` | Delete `01`/`02`/`03` `.md`; move content into HTML pages |
| Traceability empty | Join BR IDs to CMP/INT/LIN via name/capability links; rewrite `09_*.md` |
| Epic seeds as JSON only | Convert to `functions.md` / `epics.md` / `stories.md` |
| Machine out of sync | Re-copy from artifacts/ accepted versions only |
