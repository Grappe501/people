# Table: intake_batches

**Library volume:** 9 — Database Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## Purpose

Collection of pages from one capture effort.

## Ownership

People Intake

## Fields

| Column | Type (conceptual) | Null | Notes |
| --- | --- | --- | --- |
| id | uuid | no | PK |
| public_code | text | yes | Human code |
| title | text | yes | |
| event_name | text | yes | |
| county | text | yes | |
| city | text | yes | |
| collection_date | date | yes | |
| collected_by | text | yes | |
| notes | text | yes | |
| status | text | no | Batch state enum |
| created_by | uuid | no | FK app_users |
| created_at | timestamptz | no | |
| updated_at | timestamptz | no | |

## Indexes

- idx_batches_status_created
- idx_batches_created_by

## Constraints

- PK id
- status in allowed enum set

## Relationships

See ERD / related table specs.

## Lifecycle

DRAFT → … → ARCHIVED per state catalog

## Example Row (illustrative, not PII-real)

```json
{ "id": "…", "status": "READY", "county": "Pulaski" }
```

## Migration Strategy

Create after audit; additive only.

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
