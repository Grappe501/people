# Decision Register

**Program:** PEOPLE-IMPLEMENTATION-SPECIFICATION-PROGRAM-1.0  
**Companion Decision Log:** `docs/00_governance/PEOPLE_INTAKE_DECISION_LOG.md`  
**ADR index:** `docs/adr/_index.md`

## Accepted program decisions (Decision Log)

| ID | Summary |
| --- | --- |
| D-058 | PEOPLE-IMPLEMENTATION-MASTER-1.0 foundation |
| D-059 | PEOPLE-IMPLEMENTATION-SPECIFICATION-PROGRAM-1.0 + Phase 0 start |
| D-060 | PEOPLE-IS-PHASE-0-GOVERNANCE-1.0 complete; IS-000…005 APPROVED |
| D-061 | PEOPLE-IS-100-REPOSITORY-ARCHITECTURE-1.0 CLOSED |
| D-062 | PEOPLE-CATALOG-09-TRACEABILITY-1.0; Catalog Library COMPLETE |
| D-063 | PEOPLE-IS-101-TECHNOLOGY-DECISION-SPECIFICATION-1.0 APPROVED |
| D-064 | PEOPLE-IS-102-MODULE-BOUNDARY-SPECIFICATION-1.0 APPROVED |
| D-065 | Standing commit/push/deploy protocol restored |
| D-066 | PEOPLE-IS-103-ENVIRONMENT-ARCHITECTURE-1.0 APPROVED |
| D-067 | PEOPLE-IS-104-H-DRIVE-WORKSPACE-PROTOCOL-1.0 APPROVED |
| D-068 | PEOPLE-IS-105-GITHUB-AND-NETLIFY-ARCHITECTURE-1.0 APPROVED; Phase 1 platform docs COMPLETE; Burt execution authority locked |
| D-069 | PEOPLE-IS-200-DOMAIN-MODEL-1.0 APPROVED; audit/freeze independent lane chartered; Phase 2 started |
| D-070 | PEOPLE-IS-201-ENTITY-SPECIFICATIONS-1.0 APPROVED; entity admission questionnaire locked; AUDIT-SLICE-001 recorded |
| D-071 | PEOPLE-IS-202-FIELD-AND-VALUE-OBJECT-SPECIFICATIONS-1.0 APPROVED; field doctrine locked; AUDIT-SLICE-002 banners |
| D-072 | PEOPLE-IS-300-DATABASE-ARCHITECTURE-1.0 APPROVED; Phase 3 started; no migrations; AUDIT-SLICE-003 |
| D-073 | PEOPLE-IS-301-LOGICAL-TABLE-CATALOG-1.0 APPROVED; logical ≠ physical; AUDIT-SLICE-004 |

## Phase 0 approved decisions

| Decision ID | Decision | Status |
| --- | --- | --- |
| DECISION-GOV-001 | Use a separate PEOPLE-IS document family | Approved |
| DECISION-GOV-002 | Require stable IDs for requirements and engineering artifacts | Approved |
| DECISION-GOV-003 | Separate approval from implementation authorization | Approved |
| DECISION-GOV-004 | Require bidirectional traceability | Approved |
| DECISION-GOV-005 | Use H:\people as the exclusive project root | Approved |
| DECISION-GOV-006 | Prefer large coherent implementation packages over micro-edits | Approved |
| DECISION-GOV-007 | Require allowed and forbidden path declarations | Approved |
| DECISION-GOV-008 | Require validation and rollback for every build package | Approved |
| DECISION-GOV-009 | Catalog Library remains locked at 0–9 | Approved |

## Required ADRs (recommendations in IS-101; acceptance pending)

| ADR | Topic | Recommendation (summary) | Status |
| --- | --- | --- | --- |
| ADR-001 | Application Framework | Next.js + React + TypeScript | OPEN / PROPOSED |
| ADR-002 | Database Provider | Hosted PostgreSQL (brand TBD) | OPEN / PROPOSED |
| ADR-003 | ORM or Data Access Strategy | Prisma behind adapters | OPEN / PROPOSED |
| ADR-004 | Authentication Provider | Supabase Auth; method unresolved | OPEN / PROPOSED |
| ADR-005 | Object Storage Provider | Private object storage adapter | OPEN / PROPOSED |
| ADR-006 | Background Job Runtime | Dedicated queue/worker | OPEN / PROPOSED |
| ADR-007 | Notification Provider | Email adapter; vendor TBD | OPEN / PROPOSED |
| ADR-008 | API Style and Versioning | REST JSON `/api/v1` | OPEN / PROPOSED |
| ADR-009 | Hosting and Deployment | Dedicated Netlify site (D-018) | OPEN / PROPOSED |
| ADR-010 | Schema Validation Library | Zod and/or Ajv | OPEN / PROPOSED |
| ADR-011 | Test Framework | Vitest + Playwright class | OPEN / PROPOSED |
| ADR-012 | Observability Provider | Structured logs; OTel TBD | OPEN / PROPOSED |
| ADR-013 | Audit Storage Strategy | Postgres audit tables | OPEN / PROPOSED |
| ADR-014 | Idempotency Strategy | Keys + constraints + checks | OPEN / PROPOSED |
| ADR-015 | Optimistic Concurrency Strategy | Version columns | OPEN / PROPOSED |
| ADR-016 | Canonical Person Integration Boundary | Anti-corruption DTOs | OPEN / PROPOSED |
| ADR-017 | Data Retention Enforcement Strategy | Policy + scheduled jobs | OPEN / PROPOSED |
| ADR-018 | Feature Flag Strategy | Catalog 4 flags first | OPEN / PROPOSED |
| ADR-019 | AI Provider and Human Review Boundary | Assistive; human review required | OPEN / PROPOSED |
| ADR-020 | H-Drive Development Enforcement | Guard + cache redirects | OPEN / PROPOSED |
