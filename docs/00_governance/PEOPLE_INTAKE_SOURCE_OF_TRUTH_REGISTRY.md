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

Workflow, UX, and data/storage volumes through DOC-029 / DOC-032 / DOC-033 are now `draft_complete`.

| Area | Planned canonical file |
| --- | --- |
| Auth architecture | `docs/05_security/PEOPLE_INTAKE_AUTH_ARCHITECTURE.md` |
| Authorization matrix | `docs/05_security/PEOPLE_INTAKE_AUTHORIZATION_MATRIX.md` |
| Threat model | `docs/05_security/PEOPLE_INTAKE_THREAT_MODEL.md` |
| API contracts | `docs/06_engineering/PEOPLE_INTAKE_API_CONTRACTS.md` |
| Service contracts | `docs/06_engineering/PEOPLE_INTAKE_SERVICE_CONTRACTS.md` |
| Test master plan | `docs/07_quality/PEOPLE_INTAKE_TEST_MASTER_PLAN.md` |
| Deployment architecture | `docs/07_quality/PEOPLE_INTAKE_DEPLOYMENT_ARCHITECTURE.md` |
| Design freeze report | `docs/08_implementation/PEOPLE_INTAKE_DESIGN_FREEZE_REPORT.md` |

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
