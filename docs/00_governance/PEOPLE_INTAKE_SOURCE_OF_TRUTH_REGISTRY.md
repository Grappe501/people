# People Intake — Source-of-Truth Registry

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-GOVERNANCE-FOUNDATION-1.0

---

## Hierarchy

```text
1. Approved master documents
2. Approved domain contracts
3. Approved state machines
4. Approved database design
5. Approved API contracts
6. Approved UX specifications
7. Implementation code
8. Generated documentation
```

Lower layers may not silently redefine higher layers.

---

## Canonical Files by Governance Area

| Area | Canonical file |
| --- | --- |
| Master plan | `docs/00_governance/PEOPLE_INTAKE_MASTER_BUILD_PLAN.md` |
| Product charter | `docs/01_product/PEOPLE_INTAKE_PRODUCT_CHARTER.md` |
| Scope and boundaries | `docs/00_governance/PEOPLE_INTAKE_SCOPE_AND_BOUNDARIES.md` |
| H-drive protocol | `docs/00_governance/PEOPLE_INTAKE_H_DRIVE_PROTOCOL.md` |
| Design-before-code | `docs/00_governance/PEOPLE_INTAKE_DESIGN_BEFORE_CODE_PROTOCOL.md` |
| Source-of-truth registry | `docs/00_governance/PEOPLE_INTAKE_SOURCE_OF_TRUTH_REGISTRY.md` |
| Decision log | `docs/00_governance/PEOPLE_INTAKE_DECISION_LOG.md` |
| Glossary | `docs/00_governance/PEOPLE_INTAKE_GLOSSARY.md` |
| Cursor execution | `docs/08_implementation/PEOPLE_INTAKE_CURSOR_EXECUTION_PROTOCOL.md` |
| Build gates | `docs/08_implementation/PEOPLE_INTAKE_BUILD_GATES.md` |
| Progress ledger | `docs/08_implementation/PEOPLE_INTAKE_PROGRESS_LEDGER.md` |
| Active build contract | `contracts/governance/active-build.json` |
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
| Design freeze report | `docs/08_implementation/PEOPLE_INTAKE_DESIGN_FREEZE_REPORT.md` |
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
