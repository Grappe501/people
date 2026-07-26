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
| Commit/Push/Deploy Protocol | `docs/00_governance/PEOPLE_PROTOCOL_COMMIT_PUSH_DEPLOY.md` |
| ADR index | `docs/adr/_index.md` |
| Next build note | `develop_notes/NEXT_CURSOR_BUILD.md` |
| Active build | `contracts/governance/active-build.json` |

## Current next-ready work

1. `PEOPLE-IS-105-GITHUB-AND-NETLIFY-ARCHITECTURE-1.0`  
2. Parallel: `PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0`

H-drive workspace standard: IS-104 (D-067). Closeout: D-065. Implementation not authorized.

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
