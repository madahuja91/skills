# Discover Remediation Hints

| Gap pattern | Fix |
|-------------|-----|
| No framework | Re-scan `WEB-INF`, `ejb-jar.xml`, `application.xml`, `web.config`, `*.vbproj`, `Makefile`, `build.xml`, `*.ear`/`*.war` layouts |
| Version unknown | Read manifest/MANIFEST.MF, pom without parent resolve, assembly info, vendor readme; keep `unknown` if still unclear |
| Low classification | Expand extension map for `.cob`, `.cbl`, `.cls`, `.bas`, `.asp`, `.aspx`, `.cfm`, `.pc`, `.sqb` |
| Empty module_map | Group by top-level dirs / packages / projects |
| Invented modern stack | Strip modern assumptions; re-derive from descriptors only |
