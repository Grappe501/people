# People Intake — Source-of-Truth Registry

**Status:** draft_complete  
**Version:** 1.3  
**Build:** PEOPLE-PROJECT-CONSTITUTION-3.0

---

## Mandatory First Read

Before every build session, read:

```text
docs/00_governance/PEOPLE_INTAKE_PROJECT_CONSTITUTION.md
```

**PEOPLE INTAKE SYSTEM — VOLUME 0 — PROJECT CONSTITUTION** is the highest-authority standing-orders document. Detailed volumes remain authoritative for depth; they may not silently weaken Volume 0 principles.

Documentation library map:

```text
docs/00_governance/PEOPLE_INTAKE_DOCUMENTATION_LIBRARY.md
```

| Volume | Title |
| --- | --- |
| 0 | Project Constitution |
| 1 | Governance Foundation |
| 2 | Workflow & User Experience |
| 3 | Data, Matching & Storage |
| 4 | Security, API & Engineering Contracts |
| 5 | Quality, Operations & Design Freeze |
| 6 | Architecture Audit & Design Validation |
| 7 | Master Cursor Build Orchestration |

---

## Hierarchy

```text
0. Project Constitution (Volume 0) — standing orders; read first
1. Approved master documents / Decision Log (accepted)
2. Approved domain contracts
3. Approved state machines
4. Approved database design
5. Approved API contracts
6. Approved UX specifications
7. Implementation code
8. Generated documentation
```

Lower layers may not silently redefine higher layers.  
If Volume 0 conflicts with draft prose, stop and resolve via Decision Log.

---

## Canonical Files by Governance Area

| Area | Canonical file |
| --- | --- |
| Project constitution (Volume 0) | `docs/00_governance/PEOPLE_INTAKE_PROJECT_CONSTITUTION.md` |
| Documentation library map | `docs/00_governance/PEOPLE_INTAKE_DOCUMENTATION_LIBRARY.md` |
| Technical specifications (Vol 8) | `docs/09_technical_specifications/` |
| Database specifications (Vol 9) | `docs/10_database_specifications/` |
| API specifications (Vol 10) | `docs/11_api_specifications/` |
| UI specifications (Vol 11) | `docs/12_ui_specifications/` |
| Component library (Vol 12) | `docs/13_component_library/` |
| Engineering catalogs | `docs/14_engineering_catalogs/` |
| Platform standards (Vol 13) | `docs/15_platform_standards/` |
| Implementation packages | `docs/16_implementation_packages/` |
| Master plan | `docs/00_governance/PEOPLE_INTAKE_MASTER_BUILD_PLAN.md` |
| Product charter | `docs/01_product/PEOPLE_INTAKE_PRODUCT_CHARTER.md` |
| Scope and boundaries | `docs/00_governance/PEOPLE_INTAKE_SCOPE_AND_BOUNDARIES.md` |
| H-drive protocol | `docs/00_governance/PEOPLE_INTAKE_H_DRIVE_PROTOCOL.md` |
| Design-before-code | `docs/00_governance/PEOPLE_INTAKE_DESIGN_BEFORE_CODE_PROTOCOL.md` |
| Source-of-truth registry | `docs/00_governance/PEOPLE_INTAKE_SOURCE_OF_TRUTH_REGISTRY.md` |
| Decision log | `docs/00_governance/PEOPLE_INTAKE_DECISION_LOG.md` |
| Glossary | `docs/00_governance/PEOPLE_INTAKE_GLOSSARY.md` |
| Cursor build orchestration | `docs/08_implementation/PEOPLE_INTAKE_CURSOR_BUILD_ORCHESTRATION.md` |
| Implementation phase map | `docs/08_implementation/PEOPLE_INTAKE_IMPLEMENTATION_PHASE_MAP.md` |
| Implementation ledger | `docs/08_implementation/PEOPLE_INTAKE_IMPLEMENTATION_LEDGER.md` |
| Cursor execution | `docs/08_implementation/PEOPLE_INTAKE_CURSOR_EXECUTION_PROTOCOL.md` |
| Build gates | `docs/08_implementation/PEOPLE_INTAKE_BUILD_GATES.md` |
| Progress ledger | `docs/08_implementation/PEOPLE_INTAKE_PROGRESS_LEDGER.md` |
| Design freeze report | `docs/08_implementation/PEOPLE_INTAKE_DESIGN_FREEZE_REPORT.md` |
| Active build contract | `contracts/governance/active-build.json` |
| Implementation ledger contract | `contracts/governance/implementation-ledger.json` |
| Documentation index | `contracts/documentation/documentation-index.json` |
| Build phase registry | `contracts/governance/build-phase-registry.json` |

---

## Planned Canonical Files (Later Volumes)

Volumes through security/engineering (DOC-030–DOC-043 and related) are `draft_complete`. Remaining focus:

| Area | Planned canonical file |
| --- | --- |
| Test master plan | `docs/07_quality/PEOPLE_INTAKE_TEST_MASTER_PLAN.md` |
| Test case catalog | `docs/07_quality/PEOPLE_INTAKE_TEST_CASE_CATALOG.md` |
| Deployment architecture | `docs/07_quality/PEOPLE_INTAKE_DEPLOYMENT_ARCHITECTURE.md` |
| Netlify / DB / storage runbooks | `docs/07_quality/PEOPLE_INTAKE_*_RUNBOOK.md` |
| Operator manual / launch checklist | `docs/07_quality/` |
| Final implementation handoff | `docs/08_implementation/PEOPLE_INTAKE_FINAL_IMPLEMENTATION_HANDOFF.md` |

Full planned inventory lives in:

```text
contracts/documentation/documentation-index.json
```

---

## Conflict Resolution Rule

If documents disagree:

1. Prefer the higher hierarchy layer.
2. Prefer an `accepted` Decision Log entry over draft prose.
3. Prefer machine-readable contracts for enum and schema values once approved.
4. Record the conflict and resolve via Decision Log before implementation.
