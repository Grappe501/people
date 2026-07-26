# Table: intake_match_candidates

**Library volume:** 9 — Database Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## Purpose

Scored possible canonical matches for an entry.

## Ownership

People Intake

## Fields

| Column | Type (conceptual) | Null | Notes |
| --- | --- | --- | --- |
| id | uuid | no | PK |
| entry_id | uuid | no | FK |
| match_run_id | uuid | yes | FK |
| person_id | uuid | no | Canonical ref |
| tier | text | no | EXACT/POSSIBLE/CONFLICT |
| score | numeric | yes | |
| reasons | jsonb | no | Explainability |
| rank | int | no | |
| status | text | no | OPEN/SELECTED/REJECTED |

## Indexes

- idx_candidates_entry_rank
- idx_candidates_person

## Constraints

- tier in allowed set

## Relationships

See ERD / related table specs.

## Lifecycle

Created by match job; resolved with resolution

## Example Row (illustrative, not PII-real)

```json
{ "tier": "POSSIBLE", "rank": 1, "reasons": ["normalized_phone"] }
```

## Migration Strategy

Retain after resolution for audit.

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
