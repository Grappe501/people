# Table: intake_entries

**Library volume:** 9 — Database Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## Purpose

One person line on a page.

## Ownership

People Intake

## Fields

| Column | Type (conceptual) | Null | Notes |
| --- | --- | --- | --- |
| id | uuid | no | PK |
| page_id | uuid | no | FK |
| row_number | int | no | 1–10 |
| status | text | no | Entry state |
| first_name_raw | text | yes | |
| last_name_raw | text | yes | |
| phone_raw | text | yes | |
| email_raw | text | yes | |
| zip_raw | text | yes | |
| volunteer_status | text | yes | YES/NO/UNKNOWN |
| email_list_status | text | yes | YES/NO/UNKNOWN |
| *_normalized | text | yes | Parallel cols |
| field_conditions | jsonb | yes | Per-field flags |
| canonical_person_id | uuid | yes | After promotion |
| version | int | no | |
| created_at | timestamptz | no | |
| updated_at | timestamptz | no | |

## Indexes

- unique (page_id, row_number)
- idx_entries_match_status
- idx_entries_norm_email / phone

## Constraints

- row_number between 1 and 10
- volunteer_status in (YES,NO,UNKNOWN) when set

## Relationships

See ERD / related table specs.

## Lifecycle

DRAFT → TRANSCRIBED → matching → completed

## Example Row (illustrative, not PII-real)

```json
{ "row_number": 1, "volunteer_status": "UNKNOWN", "status": "DRAFT" }
```

## Migration Strategy

Additive columns preferred for new fields.

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
