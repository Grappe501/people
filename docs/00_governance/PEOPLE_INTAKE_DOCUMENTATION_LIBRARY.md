# People Intake — Documentation Library

**Status:** draft_complete  
**Version:** 2.0  
**Authority:** Defines the cohesive volume numbering for the engineering manual  
**Supreme document:** Volume 0 — Project Constitution

---

## Library Map

| Volume | Title | Primary contents | Typical paths |
| --- | --- | --- | --- |
| **0** | Project Constitution | Preamble, articles, universal principles, Cursor oath | `docs/00_governance/PEOPLE_INTAKE_PROJECT_CONSTITUTION.md` |
| **1** | Governance Foundation | Master plan, charter, scope, protocols, decisions | `docs/00_governance/` · `docs/01_product/` |
| **2** | Workflow & User Experience | Roles, workflows, queue, UX, a11y | `docs/02_workflows/` · `docs/03_ux/` |
| **3** | Data, Matching & Storage | Domain, ERD, matching, provenance, storage/privacy | `docs/04_data/` · selected storage docs |
| **4** | Security, API & Engineering Contracts | Auth, threat model, API/service contracts | `docs/05_security/` · `docs/06_engineering/` |
| **5** | Quality, Operations & Design Freeze | Tests, deployment, runbooks, freeze package | `docs/07_quality/` |
| **6** | Architecture Audit & Design Validation | Findings, risks, open decisions, freeze report | `reports/` · freeze report |
| **7** | Master Cursor Build Orchestration | Phases 0–12, gates, ledgers, Cursor controls | `docs/08_implementation/` |
| **8** | Technical Specifications | Domain engineering specs (auth → jobs) | `docs/09_technical_specifications/` |
| **9** | Database Specifications | Table-level design (no migrations yet) | `docs/10_database_specifications/` |
| **10** | API Specifications | Full endpoint contracts | `docs/11_api_specifications/` |
| **11** | UI Specifications | Screen engineering specs | `docs/12_ui_specifications/` |
| **12** | Component Library | Reusable component contracts | `docs/13_component_library/` |
| **13** | Canonical Platform Standards | Cross-app platform standards | `docs/15_platform_standards/` |
| **EC** | Engineering Catalogs | State / error / event / config catalogs | `docs/14_engineering_catalogs/` |
| **IP** | Implementation Packages | Executable Cursor packages | `docs/16_implementation_packages/` |

---

## Reading Order

### Every session

1. **Volume 0** — Constitution (mandatory)  
2. `contracts/governance/active-build.json`  

### Before any coding slice (after Gate G-10)

3. Volume 7 orchestration (active phase)  
4. Volume 8 domain tech spec(s)  
5. Volume 9 tables touched  
6. Volume 10 endpoints touched  
7. Volume 11–12 UI/components if UI  
8. EC catalogs for states/errors/events  
9. Matching IP package for the slice  

### Platform / multi-app work

10. Volume 13 Canonical Platform Standards  

---

## Path Stability Note

Historical folder names are retained for Git stability. **Library volume numbers** in this document and `documentation-index.json` are authoritative for reading order.

---

## Implementation rule

Cursor must not invent tables, endpoints, states, errors, events, or components absent from Volumes 8–13 and the Engineering Catalogs.
