# People Intake — Documentation Master Index

**Build:** PEOPLE-DOC-FOUNDATION-AND-INVENTORY-1.0  
**Machine inventory:** `data/documentation/document_inventory.json`

## 1. Purpose

Provide the single navigation and status map for the People Intake documentation library.

## 2. Authority Hierarchy

1. Volume 0 — Project Constitution  
2. Volumes 1–5 design (Volume 5 incomplete)  
3. Volume 6 Architecture Audit  
4. Volume 7 Build Orchestration  
5. Approved change records (Decision Log)  
6. Specification volumes 8–13 / catalogs (formal DOC-1…12; bootstrap is DRAFT)  

Lower layers may not silently override higher layers.

## 3. Volume Library

| Vol | Canonical Title | Canonical path (content home) | Status | Authority | Summary | Contradictions | Open decisions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Project Constitution | `docs/00_governance/PEOPLE_INTAKE_PROJECT_CONSTITUTION.md` | APPROVED | 1 | Standing orders | — | — |
| 1 | Governance Foundation | `docs/00_governance/`, `docs/01_product/` | APPROVED | 2 | Mission, scope, protocols | X-07/X-14 (master plan notes) | — |
| 2 | Workflow & UX | `docs/02_workflows/`, `docs/03_ux/` | APPROVED | 2 | Capture/transcribe/match UX | X-01,X-06,X-07,X-09,X-12,X-13 | OD-B04,07,08,09 |
| 3 | Data, Matching & Storage | `docs/04_data/` + storage/privacy | APPROVED | 2 | Domain, matching, images | X-01–X-05,X-08 | OD-B01–03,05,10,11 |
| 4 | Security, API & Engineering | `docs/05_security/`, `docs/06_engineering/` | APPROVED | 2 | Authz, API, jobs | X-09–X-11,X-13 | OD-B06,08 |
| 5 | Quality, Ops & Freeze | `docs/07_quality/` | **PARTIAL / MISSING** | 2 | Tests, ops, freeze package | X-15 | **OD-B12** |
| 6 | Architecture Audit | `reports/` + freeze report | APPROVED (freeze DENIED) | 3 | Findings, risks, OD register | all open X-* | OD-B01–12 |
| 7 | Build Orchestration | `docs/08_implementation/` | APPROVED (coding dormant) | 3 | Phases 0–12 playbook | — | Gate G-10 closed |
| 8 | Technical Specifications | `docs/09_technical_specifications/` | DRAFT bootstrap | 5 | Domain specs | inherits OD/X | DOC-1 pending |
| 9 | Database Specifications | `docs/10_database_specifications/` | DRAFT bootstrap | 5 | Table specs | OD-B05 | DOC-2 pending |
| 10 | API Specifications | `docs/11_api_specifications/` | DRAFT bootstrap | 5 | Endpoint contracts | X-09 | DOC-3 pending |
| 11 | UI Specifications | `docs/12_ui_specifications/` | DRAFT bootstrap | 5 | Screens | X-01 | DOC-4 pending |
| 12 | Component Library | `docs/volumes/volume-12-component-library/` (+ `docs/13_component_library/` pointer/bootstrap) | DESIGN COMPLETE (impl not authorized) | 5 | Components/tokens | — | `COMP-DEC-001`…`025`; DOC-5 formalization |
| 13 | Platform Standards | `docs/volumes/volume-13-platform-standards/` (+ `docs/15_platform_standards/` pointer/bootstrap) | DESIGN COMPLETE (impl not authorized) | 5 | Engineering doctrine | — | Next: State Machine Catalog; DOC-6 formalization |

`docs/volumes/volume-XX-*/README.md` pointers map to the content homes above. **No silent volume fabrication.**

## 4. Catalogs

| Catalog | Path | Status |
| --- | --- | --- |
| Terminology | `docs/catalogs/terminology/` | Foundation complete (DOC-0) |
| Identifiers | `docs/catalogs/identifiers/` | Foundation complete (DOC-0) |
| 0 Master Registry | `docs/catalogs/catalog-00-master-registry/` | DESIGN COMPLETE (impl not authorized) |
| 1 State machines | `docs/catalogs/catalog-01-state-machines/` | DESIGN COMPLETE (impl not authorized) |
| 2 Errors | `docs/catalogs/catalog-02-errors/` | DESIGN COMPLETE (impl not authorized) |
| 3 Audit events | `docs/catalogs/catalog-03-audit-events/` | DESIGN COMPLETE foundation (impl not authorized) |
| 4 Configuration | `docs/catalogs/catalog-04-configuration/` | DESIGN COMPLETE foundation (impl not authorized) |
| 5 Permissions | `docs/catalogs/catalog-05-permissions/` | DESIGN COMPLETE foundation (impl not authorized) |
| 6 Notifications | `docs/catalogs/catalog-06-notifications/` | DESIGN COMPLETE foundation (impl not authorized) |
| 7 Background jobs | `docs/catalogs/catalog-07-background-jobs/` | DESIGN COMPLETE foundation (impl not authorized) |
| 8 Data retention | `docs/catalogs/catalog-08-data-retention/` | DESIGN COMPLETE foundation (impl not authorized) |
| 9 Traceability | Planned `PEOPLE-CATALOG-09-TRACEABILITY-1.0` | Next |

## 5. Registers

| Register | Path |
| --- | --- |
| Open decisions | `develop_notes/PEOPLE_OPEN_DECISIONS_REGISTER.md` (+ `reports/…`) |
| Contradictions | `develop_notes/PEOPLE_CONTRADICTION_REGISTER.md` (+ `reports/…`) |
| Decision log | `docs/00_governance/PEOPLE_INTAKE_DECISION_LOG.md` |
| Risks | `reports/PEOPLE_RISK_REGISTER.md` |

## 6. Traceability

| Artifact | Path | Status |
| --- | --- | --- |
| Design source map | `docs/traceability/DESIGN_SOURCE_MAP.md` | DOC-0 complete |
| Cross-volume matrices | — | Planned DOC-10 |

## 7. Implementation Packages

| Path | Status |
| --- | --- |
| `docs/implementation_specs/` | PEOPLE-IMPLEMENTATION-SPECIFICATION-PROGRAM-1.0 + Phase 0 |
| `docs/implementation-specifications/` | Historical IS Master (superseded as authority) |
| `docs/implementation-packages/` | Placeholder |
| `docs/16_implementation_packages/` | Bootstrap PKG framework + master pointer |
| Formal DOC-11 | Phase 0 started under D-059 |

## 8. Validation

```powershell
Set-Location H:\people
npm run docs:foundation:validate
```

## 9. Current Build Status

**DOC-0 — Documentation Foundation and Inventory:** COMPLETE (pending git commit/push in this pass)  
**Design freeze:** DENIED  
**Application code:** PROHIBITED  
**Catalogs 0–8:** DESIGN COMPLETE (foundation)  
**IS Master:** DESIGN PHASE foundation (D-058)

## 10. Next Approved Slice

```text
PEOPLE-CATALOG-09-TRACEABILITY-1.0
```

Then continue audit remediation / freeze path. IS-* authorship remains documentation-only and blocked from coding until Gate G-10.

Volume 8 may proceed as documentation, marking OD-B*/PENDING_FREEZE items as proposed — not frozen. Critical ownership/evidence contradictions do not block starting DOC-1 if they remain explicitly open.
