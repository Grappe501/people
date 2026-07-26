# Table: intake_promotion_requests

**Library volume:** 9 — Database Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## Purpose

Controlled promotion to canonical domain.

## Ownership

People Intake

## Fields

| Column | Type (conceptual) | Null | Notes |
| --- | --- | --- | --- |
| id | uuid | no | PK |
| entry_id | uuid | no | |
| resolution_id | uuid | no | |
| action | text | no | CREATE/LINK/UPDATE |
| status | text | no | PENDING/SUCCEEDED/FAILED |
| idempotency_key | text | no | Unique in scope |
| request_payload | jsonb | no | Redacted/minimized |
| result_payload | jsonb | yes | |
| attempts | int | no | |
| created_at | timestamptz | no | |
| updated_at | timestamptz | no | |

## Indexes

- unique idempotency_key
- idx_promo_status

## Constraints

- FK to resolution

## Relationships

See ERD / related table specs.

## Lifecycle

PENDING → SUCCEEDED/FAILED → retry

## Example Row (illustrative, not PII-real)

```json
{ "action": "CREATE", "status": "PENDING" }
```

## Migration Strategy

Coordinate with canonical schema audit.

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
