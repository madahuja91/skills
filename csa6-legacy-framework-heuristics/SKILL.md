---
name: csa6-legacy-framework-heuristics
description: Detection heuristics for 20+ year legacy stacks (J2EE, .NET Framework, VB, COBOL, classic ASP, ESB, batch). Use during Discover and when validating stack claims.
---

# Legacy Framework Heuristics

## Schema

Structured findings: [schema.json](schema.json)

Emit findings into Discover/tech analysis; do not hardcode customer names.

## Prefer descriptors over guesses

| Signal | Likely stack |
|--------|--------------|
| `WEB-INF/web.xml`, `ejb-jar.xml`, `application.xml` | Java EE / J2EE |
| `struts-config.xml`, `tiles-defs.xml` | Apache Struts 1.x |
| `faces-config.xml` | JSF |
| `hibernate.cfg.xml` / `*.hbm.xml` | Hibernate classic |
| `web.config` + `.aspx` / `.asmx` | ASP.NET |
| `.vbproj` / `.csproj` ToolsVersion ≤ 3.5 | .NET Framework legacy |
| `.asp` + `global.asa` | Classic ASP |
| `.cob` / `.cbl` / JCL | COBOL mainframe |
| `build.xml` + `*.ear`/`*.war` | Ant enterprise packaging |
| `*.wsdl` + Axis/CXF jars | SOAP legacy |
| MQ / JMS config without Kafka | Enterprise messaging legacy |
| Control-M / Autosys / `.ctl` | Batch integration |

## Related enterprise legacy (also detect)

| Signal | Likely stack |
|--------|--------------|
| `javax.ejb.*`, `*Home`, `*EJB`, `ejb-jar.xml` | EJB |
| `weblogic.xml`, WebLogic JNDI lookups | WebLogic app server |
| `org.omg.CORBA`, `*POA*`, `*_Helper`/`*_Holder` | CORBA |
| TopLink / EclipseLink `StoredProcedureCall` | ORM SP calls — see `csa6-legacy-stored-procedures` |
| iBatis/MyBatis `<procedure>` / `{call ...}` | SQL maps SP — see `csa6-legacy-stored-procedures` |
| `com.ibm.mq.*` / `mq.*` properties | IBM MQ — see `csa6-legacy-ibm-mq` |

## Rules

1. Never upgrade version without manifest/pom/assembly evidence.
2. Monolith WAR/EAR ⇒ single container in C4 unless proven otherwise.
3. Stored procedures count as business rules + lineage sources — load `csa6-legacy-stored-procedures`.
4. IBM MQ put/get is a first-class integration — load `csa6-legacy-ibm-mq`.
5. File drop / FTP is a first-class integration pattern_type `legacy` or `data`.
6. If only bytecode/binaries present, mark confidence low and list missing source as critical gap.
7. Never hardcode customer package, queue, or schema names; extract from the uploaded codebase only.