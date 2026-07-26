# PEOPLE-IS-004 — DECISION AND OPEN-ISSUE REGISTER

**Document ID:** `PEOPLE-IS-004-DECISION-AND-OPEN-ISSUE-REGISTER-1.0`  
**Version:** 1.0  
**Status:** APPROVED  
**Project Root:** `H:\people`  
**Implementation Authorization:** `IMPLEMENTATION NOT AUTHORIZED`  
**Approval:** D-060

---

## Purpose

Define how decisions, unresolved questions, contradictions, assumptions, and risks are recorded. No blocking issue may remain hidden in prose.

## Registers

| Register | Path |
| --- | --- |
| Decision Log | `docs/00_governance/PEOPLE_INTAKE_DECISION_LOG.md` |
| IS Decision Register | `docs/implementation_specs/decisions/DECISION_REGISTER.md` |
| Open-Issue Register | `docs/implementation_specs/decisions/OPEN_ISSUE_REGISTER.md` |
| Project OD register | `develop_notes/PEOPLE_OPEN_DECISIONS_REGISTER.md` |

## Decision classifications

`ARCHITECTURAL | DATA | SECURITY | PRIVACY | OPERATIONAL | INTEGRATION | USER_EXPERIENCE | TESTING | DEPLOYMENT | GOVERNANCE`

## Decision states

`PROPOSED | UNDER_REVIEW | APPROVED | REJECTED | SUPERSEDED | DEFERRED`

## ADR threshold

ADR required when a decision affects multiple modules, creates a technology dependency, permanent data contract, trust boundary, security/privacy, deployment architecture, integration provider, concurrency/idempotency strategy, long-term ops obligation, or is costly to reverse.

## Initial ADR queue

ADR-001…ADR-020 (framework, database, ORM, auth, storage, jobs, notifications, API style, hosting, validation, tests, observability, audit storage, idempotency, concurrency, canonical person, retention, feature flags, AI review, H-drive enforcement).

## Issue severity / states

Severity: `LOW | MEDIUM | HIGH | CRITICAL`  
States: `OPEN | INVESTIGATING | DECISION_REQUIRED | RESOLVED | DEFERRED | CLOSED`

## Blocking rules

Blocking issues prevent implementation readiness when they affect data integrity, authn/authz, privacy, security, audit completeness, state correctness, idempotency, canonical promotion, deployment safety, backup/recovery, or legal retention.

## Functional requirements

| ID | Description |
| --- | --- |
| REQ-GOV-005 | Blocking decisions must remain visible. |

## Acceptance Criteria

AC-GOV-005.

## Open Decisions

See OPEN_ISSUE_REGISTER.md (ISSUE-PLATFORM-001 through ISSUE-HDRIVE-001).

## Revision History

| Version | Date | Change | Approval |
| --- | --- | --- | --- |
| 1.0 | 2026-07-26 | Decision/issue governance approved | D-060 |
