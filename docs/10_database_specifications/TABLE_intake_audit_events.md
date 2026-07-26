# Table: intake_audit_events

**Library volume:** 9 — Database Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## Purpose

Append-only meaningful action log.

## Ownership

People Intake

## Fields

| Column | Type (conceptual) | Null | Notes |
| --- | --- | --- | --- |
| id | uuid | no | PK |
| event_type | text | no | Catalog name |
| actor_user_id | uuid | yes | |
| batch_id | uuid | yes | |
| page_id | uuid | yes | |
| entry_id | uuid | yes | |
| person_id | uuid | yes | |
| request_id | text | yes | |
| summary | text | no | Non-PII |
| payload | jsonb | yes | Redacted |
| created_at | timestamptz | no | |

## Indexes

- idx_audit_created
- idx_audit_type
- idx_audit_page
- idx_audit_actor

## Constraints

- Append-only grants for app role

## Relationships

See ERD / related table specs.

## Lifecycle

Insert only

## Example Row (illustrative, not PII-real)

```json
{ "event_type": "PageClaimed", "summary": "Page claimed for entry" }
```

## Migration Strategy

Partition by time later if volume requires.

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
