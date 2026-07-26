# Page Specification

**Library volume:** 8 — Technical Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## 1. Purpose

Primary queue work unit: one source image + 0–10 entries.

## 2. Identity

- `pageId` UUID  
- `pageNumber` unique within batch  
- Human code may include batch + page ordinal

## 3. Core Fields

| Field | Notes |
| --- | --- |
| batchId | required FK |
| pageNumber | 1..N within batch |
| status | page state machine |
| version | optimistic concurrency integer |
| imageQualityStatus | pending/pass/fail/`PENDING_FREEZE` labels |
| blankPage | boolean exception path |
| unreadablePage | boolean exception path |

## 4. Lifecycle

See Engineering Catalog — Page state machine. UX labels must not expose raw enum names to routine users.

## 5. Invariants

- At most one active original image version.  
- At most one active claim.  
- Entry count ≤ 10.  
- Page not `COMPLETED` while any entry has pending promotion (`PENDING_FREEZE` alignment with UX vocabulary — OD-B*).  
- Submit requires active claim (or audited override).

## 6. Exception Paths

- Upload failure → retryable page state  
- Unreadable → return path without inventing people  
- Blank page → documented zero-entry submit (`PENDING_FREEZE` vs API 1–10 — OD-B*)

## 7. Audit

`PageRegistered` `PageUploaded` `PageStatusChanged` `PageSubmitted` `PageReturned` `PageReopened` `PageForceCompleted`

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 2 workflows
- Volume 9 `intake_pages`
- Volume 10 page endpoints
