# Table: intake_match_resolutions

**Library volume:** 9 — Database Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## Purpose

Final human/system determination for an entry.

## Ownership

People Intake

## Fields

| Column | Type (conceptual) | Null | Notes |
| --- | --- | --- | --- |
| id | uuid | no | PK |
| entry_id | uuid | no | FK |
| resolution | text | no | LINK_EXISTING/CREATE_NEW/DEFER/RETURN_FOR_CORRECTION/NO_ACTION |
| selected_person_id | uuid | yes | |
| selected_candidate_id | uuid | yes | |
| decided_by | uuid | no | |
| decided_at | timestamptz | no | |
| notes | text | yes | |
| entry_version | int | no | |

## Indexes

- unique final resolution per entry version
- idx_resolutions_entry

## Constraints

- One final per entry version

## Relationships

See ERD / related table specs.

## Lifecycle

Written in resolve transaction with promotion request when needed

## Example Row (illustrative, not PII-real)

```json
{ "resolution": "CREATE_NEW" }
```

## Migration Strategy

Immutable after write except formal void by admin policy.

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
