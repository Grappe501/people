# PEOPLE-IS-000 — PROGRAM GOVERNANCE

**Document ID:** `PEOPLE-IS-000-PROGRAM-GOVERNANCE-1.0`  
**Version:** 1.0  
**Status:** APPROVED  
**Project Root:** `H:\people`  
**Owner:** Program  
**Technical Reviewer:** Program  
**Governance Reviewer:** Program  
**Traceability Reviewer:** Program  
**Approval Authority:** Decision Log D-060  
**Created:** 2026-07-26  
**Last Updated:** 2026-07-26  
**Governing Documents:** PEOPLE-IMPLEMENTATION-SPECIFICATION-PROGRAM-1.0; Volume 0–1; Catalog 00  
**Dependencies:** None  
**Implementation Authorization:** `IMPLEMENTATION NOT AUTHORIZED`

---

## 1. Purpose

Govern the entire Implementation Specification Program: authority, scope, hierarchy, approval, implementation restrictions, change control, ownership, conflict resolution, and implementation authorization.

Phase 0 does not design application features or authorize application code.

## 2. Scope

Included: IS series rules, status model, approvals, H-drive boundary, change control.  
Out of scope: Application features, schemas, APIs, UI, deployments.

## 3. Out of Scope

Executable application logic; migrations; Netlify functions; production secrets; live providers; package installs for application runtime.

## 4. Governing References

* Master Build Plan  
* Volumes 0–13  
* Catalogs 00–08 (foundation complete); Catalog 09 Traceability (next)  
* PEOPLE-IMPLEMENTATION-SPECIFICATION-PROGRAM-1.0  
* Gate G-10 (closed)  
* Decision Log D-058, D-059, D-060  

**Note:** Catalog Library is locked at **0–9**. Draft material labeled Catalogs 10–13 is not governing catalog authority.

## 5. Definitions

| Term | Meaning |
| --- | --- |
| Documentation approval | Spec accepted as governing documentation |
| Implementation authorization | Explicit permission to code within named scope |
| IS document | PEOPLE-IS-* engineering specification |

## 6. Assumptions

Catalog 09 will complete for full matrix closure. ADR-001…020 remain open and block coding.

## 7. Functional Requirements

| ID | Description |
| --- | --- |
| REQ-GOV-001 | Documentation must precede implementation. |
| REQ-GOV-007 | All project work must remain under H:\people. |
| REQ-GOV-008 | Nothing may intentionally write to C:\. |
| REQ-GOV-009 | Approval does not automatically authorize implementation. |
| REQ-GOV-010 | Production secrets must not appear in documentation. |

## 8. Nonfunctional Requirements

| ID | Description |
| --- | --- |
| NFR-GOV-001 | Governance docs must be discoverable via `_index.md`. |
| NFR-GOV-002 | Change history must be auditable via Decision Log / CHANGE-* IDs. |

## 9. Architecture

### Document hierarchy

```text
1. Master Build Outline
2. Approved Volumes
3. Approved Catalogs (00–09)
4. Approved Protocols
5. Approved ADRs / Decision Log
6. Approved Implementation Specifications
7. Approved Implementation Packages (PKG-*)
8. Application Implementation
9. Verification Evidence
10. Operational Runbooks
```

### Program phases

Phase 0 Governance → 1 Platform → 2 Domain → 3 Database → 4 Services → 5 API → 6 UX → 7 Jobs → 8 Integrations → 9 Security → 10 Ops → 11 Testing → 12 Deployment → 13 Package Design → 14 Authorization Gate.

## 10–28. Cross-cutting

State / permission / API / job sections: **NOT_APPLICABLE** (program governance, not a runtime feature). Failures: conflict resolution procedure in §000.10 style — record ISSUE, escalate to Decision Log, do not silently pick a side.

### Status model

```text
NOT_STARTED | DRAFT | INTERNAL_REVIEW | REVISION_REQUIRED
STRUCTURALLY_COMPLETE | TECHNICALLY_REVIEWED | TRACEABILITY_COMPLETE
APPROVED | IMPLEMENTATION_READY | SUPERSEDED | DEPRECATED | ARCHIVED
```

### Implementation authorization states

```text
IMPLEMENTATION NOT AUTHORIZED
IMPLEMENTATION AUTHORIZED FOR NAMED DOCUMENTATION TOOLING ONLY
IMPLEMENTATION AUTHORIZED FOR SPECIFIED PACKAGE
IMPLEMENTATION AUTHORIZED FOR SPECIFIED PHASE
FULL IMPLEMENTATION AUTHORIZED
```

### Locked governance decisions

1. Documentation precedes implementation.  
2. Application code prohibited until explicitly authorized.  
3. H:\people is the canonical project root.  
4. Nothing may intentionally write to C:\.  
5. No specification may silently contradict an approved catalog or volume.  
6. Every requirement must have a stable identifier.  
7. Every critical decision must have an ADR or decision record.  
8. Every unresolved issue must be visible in the open-issue register.  
9. Every implementation-ready specification must have complete traceability.  
10. Approval and implementation authorization are separate actions.  
11. Exact paths must be defined before coding begins.  
12. Forbidden paths must be declared for each implementation package.  
13. Production secrets may never be stored in documentation.  
14. Every implementation package must define validation and rollback.  
15. No undocumented feature may enter production.  
16. Catalog Library remains 0–9.  

## Acceptance Criteria

AC-GOV-001, AC-GOV-006, AC-GOV-007 (see Phase 0 package).

## Open Decisions

ADR-001…020 open; Catalog 09 incomplete (IS-ISSUE / ISSUE-PLATFORM-* register).

## Traceability

See `matrices/REQUIREMENT_TRACEABILITY_MATRIX.md` rows REQ-GOV-001, 007–010.

## Implementation Boundary

**Allowed:** markdown, indexes, registers, matrices, non-executable schemas.  
**Forbidden:** `src/`, migrations, live config, deployments, dependency installs for app runtime.

## Revision History

| Version | Date | Change | Approval |
| --- | --- | --- | --- |
| 1.0 | 2026-07-26 | Phase 0 package elevate to APPROVED | D-060 |
