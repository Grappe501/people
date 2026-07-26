# PEOPLE-IS-001 — SPECIFICATION TEMPLATE

**Document ID:** `PEOPLE-IS-001-SPECIFICATION-TEMPLATE-1.0`  
**Version:** 1.0  
**Status:** APPROVED  
**Project Root:** `H:\people`  
**Implementation Authorization:** `IMPLEMENTATION NOT AUTHORIZED`  
**Approval:** D-060

---

## Purpose

Define the mandatory structure of every PEOPLE-IS specification.

## Mandatory header fields

```text
Title, Document ID, Version, Status, Project Root,
Owner, Technical Reviewer, Governance Reviewer, Traceability Reviewer,
Approval Authority, Created Date, Last Updated,
Governing Documents, Dependencies, Implementation Authorization
```

## Mandatory sections (1–28)

1. Purpose  
2. Scope  
3. Out of Scope  
4. Governing References  
5. Definitions  
6. Assumptions  
7. Functional Requirements  
8. Nonfunctional Requirements  
9. Architecture  
10. Data Contracts  
11. Interface Contracts  
12. State Behavior  
13. Permission Behavior  
14. Error and Recovery Behavior  
15. Audit Requirements  
16. Notification Requirements  
17. Background Processing  
18. Security and Privacy  
19. Data Classification and Retention  
20. Observability  
21. Testing  
22. Acceptance Criteria  
23. Open Decisions  
24. Risks  
25. Dependencies  
26. Traceability Matrix  
27. Implementation Boundary  
28. Revision History  

Sections that do not apply must be marked `NOT_APPLICABLE` with justification.

## Requirement writing standard

Use MUST / MUST NOT / REQUIRED / SHALL / SHALL NOT / MAY / OPTIONAL. Avoid undefined adjectives (fast, secure, reasonable) unless measurable.

### Requirement template

```text
Requirement ID | Title | Type | Priority | Description | Trigger |
Preconditions | Required Behavior | Failure Behavior |
Related State | Permission | Error | Audit | Notification | Test | Source
```

### Acceptance criterion template

```text
Acceptance ID | Related Requirement | Given | When | Then | Evidence Required | Blocking
```

### Open-decision / Risk / Revision templates

See `docs/implementation_specs/templates/IMPLEMENTATION_SPECIFICATION_TEMPLATE.md`.

## Functional requirements

| ID | Description |
| --- | --- |
| REQ-GOV-002 | Every specification must use the canonical template. |

## Acceptance Criteria

AC-GOV-002.

## Implementation Boundary

Documentation only. Copyable skeleton: `templates/IMPLEMENTATION_SPECIFICATION_TEMPLATE.md`.

## Revision History

| Version | Date | Change | Approval |
| --- | --- | --- | --- |
| 1.0 | 2026-07-26 | Full 28-section template approved | D-060 |
