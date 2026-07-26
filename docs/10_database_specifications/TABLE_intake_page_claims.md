# Table: intake_page_claims

**Library volume:** 9 — Database Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## Purpose

Exclusive work lock on a page.

## Ownership

People Intake

## Fields

| Column | Type (conceptual) | Null | Notes |
| --- | --- | --- | --- |
| id | uuid | no | PK |
| page_id | uuid | no | FK |
| claimant_user_id | uuid | no | FK |
| claim_type | text | no | ENTRY / MATCH PENDING_FREEZE |
| status | text | no | ACTIVE/RELEASED/EXPIRED/REASSIGNED |
| claimed_at | timestamptz | no | |
| expires_at | timestamptz | no | |
| renewed_at | timestamptz | yes | |

## Indexes

- **partial unique** (page_id) WHERE status='ACTIVE' (and claim_type when multi-type)
- idx_claims_expiry

## Constraints

- One active claim rule enforced in DB

## Relationships

See ERD / related table specs.

## Lifecycle

Unclaimed → Active → Released/Expired/Reassigned

## Example Row (illustrative, not PII-real)

```json
{ "status": "ACTIVE", "claim_type": "ENTRY" }
```

## Migration Strategy

Critical concurrency index — test before prod.

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
