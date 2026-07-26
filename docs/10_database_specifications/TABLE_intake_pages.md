# Table: intake_pages

**Library volume:** 9 — Database Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## Purpose

One photographed sheet; primary queue unit.

## Ownership

People Intake

## Fields

| Column | Type (conceptual) | Null | Notes |
| --- | --- | --- | --- |
| id | uuid | no | PK |
| batch_id | uuid | no | FK |
| page_number | int | no | Unique in batch |
| status | text | no | Page state |
| version | int | no | Optimistic lock |
| blank_page | boolean | no | default false |
| unreadable_page | boolean | no | default false |
| priority | int | yes | Queue boost |
| created_at | timestamptz | no | |
| updated_at | timestamptz | no | |

## Indexes

- idx_pages_queue (status, priority, created_at)
- unique (batch_id, page_number)

## Constraints

- FK batch_id
- page_number >= 1

## Relationships

See ERD / related table specs.

## Lifecycle

UPLOADING → … → COMPLETED/ARCHIVED

## Example Row (illustrative, not PII-real)

```json
{ "id": "…", "page_number": 3, "status": "READY_FOR_ENTRY", "version": 4 }
```

## Migration Strategy

Create with batches; FKs validated.

## Implementation Notes

- Do not create this table until Gate G-10 + migration authorization + shared DB audit.  
- Exact types may adjust to Postgres conventions after audit.

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- DATABASE_SPEC_OVERVIEW.md
- Volume 3 ERD
