# PEOPLE-IS-005 — SPECIFICATION READINESS GATE

**Document ID:** `PEOPLE-IS-005-SPECIFICATION-READINESS-GATE-1.0`  
**Version:** 1.0  
**Status:** APPROVED  
**Project Root:** `H:\people`  
**Implementation Authorization:** `IMPLEMENTATION NOT AUTHORIZED`  
**Approval:** D-060

---

## Purpose

Define evidence required for an implementation specification to advance through each readiness state. A percentage alone cannot establish readiness.

## Gates

| Gate | Result status | Required evidence (summary) |
| --- | --- | --- |
| 1 Draft | DRAFT | ID, title, owner, purpose, preliminary scope, governing refs |
| 2 Structure | STRUCTURALLY_COMPLETE | All mandatory sections; requirements; open decisions; risks; acceptance; revision history |
| 3 Technical | TECHNICALLY_REVIEWED | Architecture, ownership, dependencies, contracts, failures, security/ops implications, boundaries |
| 4 Traceability | TRACEABILITY_COMPLETE | Full mapping per PEOPLE-IS-003 minimum standard |
| 5 Approval | APPROVED | No critical contradiction; sign-offs; version fixed; effective date |
| 6 Impl Ready | IMPLEMENTATION_READY | Blocking deps/ADRs/issues cleared; allowed/forbidden paths; package; validation; rollback; tests; no secrets; auth status explicit |

## Critical rule

```text
IMPLEMENTATION_READY ≠ APPLICATION CODE AUTHORIZED
```

Coding requires a separate Gate G-10 / active-build authorization declaration.

## Automatic rejection conditions

Conflicts with approved catalog; missing test strategy; missing permission mapping for protected behavior; missing audit mapping for state changes; undocumented errors/jobs; unresolved critical security or data-loss questions; missing rollback/recovery; unapproved provider; permits writes outside H:\people; contains production secrets; ambiguous implementation scope.

## Implementation package gate fields

Package ID, Purpose, Approved Specifications, Dependencies, Allowed Paths, Forbidden Paths, Files to Create/Modify, Schema/API/UI/Job/Config/Security Changes, Tests, Validation Commands, Rollback, Documentation Updates, Commit/Deployment Instructions, Completion Report Format.

## Completion scoring (supplemental)

Structure 10% · Requirements 15% · Architecture 15% · Data/Interfaces 15% · Security/Privacy 10% · Failure/Recovery 10% · Traceability 15% · Testing 10%. A 100% score does not override a blocking issue.

## Functional requirements

| ID | Description |
| --- | --- |
| REQ-GOV-006 | Readiness requires objective evidence. |

## Acceptance Criteria

AC-GOV-006, AC-GOV-008.

## Revision History

| Version | Date | Change | Approval |
| --- | --- | --- | --- |
| 1.0 | 2026-07-26 | Readiness gates approved | D-060 |
