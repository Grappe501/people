# Implementation Specification Program — Index

**Program ID:** PEOPLE-IMPLEMENTATION-SPECIFICATION-PROGRAM-1.0  
**Phase 0:** COMPLETE (D-060)  
**Phase 1:** IS-100…102 APPROVED; IS-103 next

| Document ID | Title | Phase | Status | Owner | Dependencies | Blocking Issues | Readiness |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| PEOPLE-IS-000 | Program Governance | 0 | APPROVED | Program | Program Design | — | 100% |
| PEOPLE-IS-001 | Specification Template | 0 | APPROVED | Program | IS-000 | — | 100% |
| PEOPLE-IS-002 | Naming and Identification Standard | 0 | APPROVED | Program | IS-000 | — | 100% |
| PEOPLE-IS-003 | Traceability Standard | 0 | APPROVED | Program | IS-000 | ISSUE-CATALOG-009 (inventory) | 100% |
| PEOPLE-IS-004 | Decision and Open-Issue Register | 0 | APPROVED | Program | IS-000 | ADR queue open for coding | 100% |
| PEOPLE-IS-005 | Specification Readiness Gate | 0 | APPROVED | Program | IS-000…004 | — | 100% |
| PEOPLE-IS-100 | Repository Architecture | 1 | CLOSED / APPROVED | Program | Phase 0 | ADRs block impl readiness | 100% docs |
| PEOPLE-IS-101 | Technology Decision Specification | 1 | APPROVED | Program | IS-100 + Catalog 09 | ADR-001…020 OPEN | 100% docs |
| PEOPLE-IS-102 | Module Boundary Specification | 1 | APPROVED | Program | IS-100 + IS-101 | ISSUE-MOD-001/002 | 100% docs |
| PEOPLE-IS-103 | Environment Architecture | 1 | APPROVED | Program | IS-102 | open ADRs for env brands | 100% docs |
| PEOPLE-IS-104 | H-Drive Workspace Protocol | 1 | APPROVED | Program | IS-103 | ADR-020 / ISSUE-HDRIVE-001 (guard code) | 100% docs |
| PEOPLE-IS-105 | GitHub and Netlify Architecture | 1 | Next Ready | — | IS-104 | — | 0% |

## Queued Phase 1 siblings

| Document ID | Title | Status |
| --- | --- | --- |
| PEOPLE-IS-104 | H-Drive Workspace Protocol | Queued |
| PEOPLE-IS-105 | GitHub and Netlify Architecture | Queued |

## Shared artifacts

| Artifact | Path |
| --- | --- |
| Requirement matrix | `matrices/REQUIREMENT_TRACEABILITY_MATRIX.md` |
| Module dependency matrix | `matrices/MODULE_DEPENDENCY_MATRIX.md` |
| Module ownership matrix | `matrices/MODULE_OWNERSHIP_MATRIX.md` |
| Boundary validation rules | `matrices/MODULE_BOUNDARY_VALIDATION_RULES.md` |
| Interface contract index | `matrices/MODULE_INTERFACE_CONTRACT_INDEX.md` |
| Decision register | `decisions/DECISION_REGISTER.md` |
| Open-issue register | `decisions/OPEN_ISSUE_REGISTER.md` |
| Progress report | `reports/IMPLEMENTATION_SPECIFICATION_PROGRESS.md` |
| IS-102 completion | `reports/PEOPLE_IS_102_COMPLETION_REPORT.md` |
| ADR index | `docs/adr/_index.md` |
| Spec template | `templates/IMPLEMENTATION_SPECIFICATION_TEMPLATE.md` |
| Orientation | `H:\people\START_HERE.md` |
