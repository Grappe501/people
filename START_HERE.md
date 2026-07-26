# START HERE — People Intake System

**Canonical project root:** `H:\people`  
**Read this before changing anything.**

## Current authorization

```text
DOCUMENTATION AND SPECIFICATION WORK: AUTHORIZED
APPLICATION IMPLEMENTATION: NOT AUTHORIZED
DATABASE MIGRATIONS: NOT AUTHORIZED
DEPLOYMENT: NOT AUTHORIZED
PACKAGE INSTALLATION FOR APPLICATION RUNTIME: NOT AUTHORIZED
```

Gate **G-10** remains **CLOSED**. `applicationCodeAuthorized` remains **false**.

## Boundaries

* All project-controlled work MUST stay under `H:\people`.  
* Do not intentionally write project artifacts to `C:\`.  
* Production secrets MUST NOT appear in docs, Git, logs, or fixtures.  
* Catalog Library is locked at **Catalogs 0–9** (not 10–13).

## Governing entry points

| Priority | Path |
| --- | --- |
| Constitution | `docs/00_governance/PEOPLE_INTAKE_PROJECT_CONSTITUTION.md` |
| Decision Log | `docs/00_governance/PEOPLE_INTAKE_DECISION_LOG.md` |
| Catalog Master | `docs/catalogs/catalog-00-master-registry/` |
| IS Program | `docs/implementation_specs/PEOPLE_IMPLEMENTATION_SPECIFICATION_PROGRAM.md` |
| IS Index | `docs/implementation_specs/_index.md` |
| Repository Architecture | `docs/implementation_specs/100_platform/PEOPLE-IS-100-REPOSITORY-ARCHITECTURE.md` |
| Technology Decisions | `docs/implementation_specs/100_platform/PEOPLE-IS-101-TECHNOLOGY-DECISION-SPECIFICATION.md` |
| Module Boundaries | `docs/implementation_specs/100_platform/PEOPLE-IS-102-MODULE-BOUNDARY-SPECIFICATION.md` |
| Environment Architecture | `docs/implementation_specs/100_platform/PEOPLE-IS-103-ENVIRONMENT-ARCHITECTURE.md` |
| H-Drive Workspace Protocol | `docs/implementation_specs/100_platform/PEOPLE-IS-104-H-DRIVE-WORKSPACE-PROTOCOL.md` |
| GitHub and Netlify Architecture | `docs/implementation_specs/100_platform/PEOPLE-IS-105-GITHUB-AND-NETLIFY-ARCHITECTURE.md` |
| Domain Model | `docs/implementation_specs/200_domain/PEOPLE-IS-200-DOMAIN-MODEL.md` |
| Entity Specifications | `docs/implementation_specs/200_domain/PEOPLE-IS-201-ENTITY-SPECIFICATIONS.md` |
| Field and Value Objects | `docs/implementation_specs/200_domain/PEOPLE-IS-202-FIELD-AND-VALUE-OBJECT-SPECIFICATIONS.md` |
| Database Architecture | `docs/implementation_specs/300_database/PEOPLE-IS-300-DATABASE-ARCHITECTURE.md` |
| Logical Table Catalog | `docs/implementation_specs/300_database/PEOPLE-IS-301-LOGICAL-TABLE-CATALOG.md` |
| Logical Relationships | `docs/implementation_specs/300_database/PEOPLE-IS-302-LOGICAL-RELATIONSHIP-SPECIFICATIONS.md` |
| Logical Constraints & Integrity | `docs/implementation_specs/300_database/PEOPLE-IS-303-LOGICAL-CONSTRAINTS-AND-INTEGRITY.md` |
| Read Model Specifications | `docs/implementation_specs/300_database/PEOPLE-IS-304-READ-MODEL-SPECIFICATIONS.md` |
| Migration Governance | `docs/implementation_specs/300_database/PEOPLE-IS-305-MIGRATION-GOVERNANCE.md` |
| Commit/Push/Deploy Protocol | `docs/00_governance/PEOPLE_PROTOCOL_COMMIT_PUSH_DEPLOY.md` |
| Cursor Execution Protocol | `docs/08_implementation/PEOPLE_INTAKE_CURSOR_EXECUTION_PROTOCOL.md` |
| Audit / Freeze lane | `docs/00_governance/lanes/PEOPLE_AUDIT_REMEDIATION_AND_QUALITY_OPS_FREEZE.md` |
| Latest audit findings | `reports/PEOPLE_AUDIT_SLICE_010_FINDINGS.md` |
| Gate G-10 readiness | `reports/PEOPLE_GATE_G10_READINESS_ASSESSMENT.md` |
| G-10 remediation plan | `docs/00_governance/PEOPLE_GATE_G10_REMEDIATION_PLAN.md` |
| Locked operating posture | `docs/00_governance/PEOPLE_LOCKED_OPERATING_POSTURE.md` |
| Steve G-10 decision dashboard | `reports/PEOPLE_STEVE_G10_DECISION_DASHBOARD.md` |
| G-10 blocker master register | `reports/PEOPLE_GATE_G10_BLOCKER_MASTER_REGISTER.md` |
| ADR decision packet index | `reports/PEOPLE_BLOCKING_ADR_DECISION_PACKET_INDEX.md` |
| ADR index | `docs/adr/_index.md` |
| Next build note | `develop_notes/NEXT_CURSOR_BUILD.md` |
| Active build | `contracts/governance/active-build.json` |

## Current next-ready work

1. **Steve ADR decision pass** — `reports/PEOPLE_STEVE_G10_DECISION_DASHBOARD.md`  
2. `PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0` continues  
3. Gate G-10: **REMAIN CLOSED** — reassessment D-079+ only after material evidence changes  

Phase 3 docs complete. Design freeze **DENIED**. **Implementation not authorized.**  
G-10 blocker remediation packets prepared (decisions pending).

## Allowed now

* Markdown / indexes / registers / matrices / progress reports  
* Non-executable documentation schemas and validation instructions  
* Documentation-only Cursor instructions  

## Prohibited now

* Application source under `src` / `app`  
* Database migrations  
* Netlify functions / live providers  
* Production configuration / secrets  
* Dependency installs for application scaffolding  
* Deployments  

## Repository map (target)

See PEOPLE-IS-100 for full ownership of `docs`, `contracts`, `src`, `database`, `tests`, `scripts`, `deployment`, `generated`, `local`, `tmp`, `logs`, and related roots. Many implementation directories are **placeholders** until an authorized package creates them.

## Validation

Prefer:

```text
npm run governance:validate
```

with caches/temp under `H:\people` (e.g. `.npm-cache`, `.tmp` until ADR-020 formalizes paths).
