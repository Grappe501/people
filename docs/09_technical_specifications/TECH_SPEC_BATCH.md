# Batch Specification

**Library volume:** 8 — Technical Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## 1. Purpose

Group pages from one capture effort with shared metadata.

## 2. Identity

- `batchId` UUID internal  
- Optional human code `PI-YYYYMMDD-#####`

## 3. Metadata Fields

| Field | Required | Notes |
| --- | --- | --- |
| title / label | optional | Operator-friendly |
| eventName | optional | |
| county | optional | |
| city | optional | |
| collectionDate | recommended | |
| collectedBy | optional | |
| notes | optional | |
| createdBy | system | uploader userId |
| status | system | see state machine |

## 4. Lifecycle

`DRAFT → UPLOADING → READY → IN_PROGRESS → NEEDS_ATTENTION → COMPLETED → ARCHIVED`

Completion requires all pages resolved (see Engineering Catalog / state machines).

## 5. Invariants

- Batch contains pages, not people.  
- Deleting a batch with pages is Admin-only and must preserve evidence or soft-delete.  
- Progress metrics derived from page states, not stored as sole truth.

## 6. Operations

Create · Patch metadata · Complete upload · Archive · Reopen (Admin)

## 7. Audit

`BatchCreated` `BatchUpdated` `BatchUploadCompleted` `BatchArchived` `BatchReopened`

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 3 domain model
- Volume 9 `intake_batches`
- Volume 10 batch endpoints
