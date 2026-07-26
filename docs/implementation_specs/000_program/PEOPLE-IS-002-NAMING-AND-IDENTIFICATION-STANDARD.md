# PEOPLE-IS-002 — NAMING AND IDENTIFICATION STANDARD

**Document ID:** `PEOPLE-IS-002-NAMING-AND-IDENTIFICATION-STANDARD-1.0`  
**Version:** 1.0  
**Status:** APPROVED  
**Project Root:** `H:\people`  
**Implementation Authorization:** `IMPLEMENTATION NOT AUTHORIZED`  
**Approval:** D-060

---

## Purpose

Define stable identifiers for every governed engineering artifact. Identifiers are permanent once approved. Renaming a display label does not change the canonical identifier.

## Identifier families

| Family | Format | Example |
| --- | --- | --- |
| Document | `PEOPLE-IS-<NUMBER>-<TITLE>-<VERSION>` | PEOPLE-IS-203-UPLOAD-AND-PAGE-MODEL-1.0 |
| Requirement | `REQ-<DOMAIN>-<NUMBER>` | REQ-CLAIM-001 |
| Nonfunctional | `NFR-<DOMAIN>-<NUMBER>` | NFR-SECURITY-001 |
| Acceptance | `AC-<DOMAIN>-<NUMBER>` | AC-CLAIM-001 |
| Entity | `ENTITY-<NAME>` | ENTITY-CLAIM |
| Field | `FIELD-<ENTITY>-<FIELD>` | FIELD-CLAIM-EXPIRES-AT |
| Service | `SERVICE-<DOMAIN>` | SERVICE-CLAIM |
| API endpoint | `API-<DOMAIN>-<NUMBER>` | API-CLAIM-003 |
| State | Catalog 1 keys / `STATE-<RESOURCE>-<STATE>` | STATE-CLAIM-ACTIVE |
| Transition | `TRANSITION-<RESOURCE>-<NUMBER>` | TRANSITION-CLAIM-001 |
| Permission | Catalog 5 keys | PAGE_CLAIM |
| Error | Catalog 2 codes | CLAIM_ALREADY_HELD |
| Audit | Catalog 3 IDs / names | AUDIT-CLAIM-001 / CLAIM_ACQUIRED |
| Notification | Catalog 6 IDs / names | NOTIFY-CLAIM-001 / CLAIM_EXPIRING |
| Job | Catalog 7 IDs / names | JOB-CLAIM-001 / CLAIM_EXPIRATION_CHECK |
| Integration | `INTEGRATION-<DOMAIN>-<NUMBER>` | INTEGRATION-STORAGE-001 |
| Test | `TEST-<TYPE>-<DOMAIN>-<NUMBER>` | TEST-API-CLAIM-001 |
| ADR | `ADR-<NUMBER>` | ADR-001 |
| Decision (minor) | `DECISION-<DOMAIN>-<NUMBER>` | DECISION-GOV-001 |
| Open issue | `ISSUE-<DOMAIN>-<NUMBER>` | ISSUE-STORAGE-001 |
| Risk | `RISK-<DOMAIN>-<NUMBER>` | RISK-AUTH-001 |
| Change | `CHANGE-<YEAR>-<NUMBER>` | CHANGE-2026-001 |
| Build package | `PEOPLE-BUILD-<PHASE>-<NUMBER>-<TITLE>-<VERSION>` | PEOPLE-BUILD-01-001-… |
| Cursor package | `PKG-<phase>.<slice>` | PKG-0.1 |

## Rules

1. Do not invent Catalog 1–8 values; reuse catalog keys.  
2. REQ-* / NFR-* / AC-* may be created in IS docs with Volume/Catalog sources.  
3. Endpoint IDs remain stable across route version transitions.  
4. Directory names: lowercase snake_case (`implementation_specs`).  
5. Filenames may use `PEOPLE-IS-###-TITLE.md` (active convention) or underscore form; Document ID remains authoritative.  

## Functional requirements

| ID | Description |
| --- | --- |
| REQ-GOV-003 | Every requirement must have a stable ID. |

## Acceptance Criteria

AC-GOV-003.

## Revision History

| Version | Date | Change | Approval |
| --- | --- | --- | --- |
| 1.0 | 2026-07-26 | Full identifier families approved | D-060 |
