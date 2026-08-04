# Claims Legacy Module Fixture

Minimal Java EE Servlet 2.5 + JDBC + SOAP-style client module for CSA Orchestrator pilot.

**Expected Discover findings**
- Language: Java
- Framework: Java EE Servlet (from `WEB-INF/web.xml`), NOT Spring Boot
- Database: Oracle (from DDL/JDBC SQL)
- Module: claims

**Expected Domain**
- DOM-claims, ENT-claim, BR-claim-status-transition

**Expected Integration**
- INT-* Policy SOAP outbound sync
