# Queue Specification

**Library volume:** 8 — Technical Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## 1. Purpose

Shared multi-user work lists for entry and matching.

## 2. Queues

| Queue | Consumer roles | Eligibility |
| --- | --- | --- |
| Entry queue | DATA_ENTRY, ADMIN, OWNER | Pages ready for entry, unclaimed or expired claim |
| Match queue | REVIEWER, ADMIN, OWNER | Entries/pages needing human match review |
| Correction queue | DATA_ENTRY (+admin) | Pages returned for correction |
| Exception queue | ADMIN, OWNER | Failures, stuck states |

## 3. Ordering

Default: priority (if set) then oldest first (created/ready timestamp). Admin may boost priority.

## 4. Listing vs Claim

- `GET` lists are eventually consistent views.  
- `claim-next` is the atomic assignment path — never “select then claim” in two non-atomic client steps as the only path.

## 5. Filters

Batch, county, status, assignee (admin), age — server-side only.

## 6. Invariants

- Claim-next must not return a page already actively claimed.  
- Concurrent claim-next must serialize via DB lock / unique active claim constraint.

## 7. Tests

- Two concurrent claim-next → distinct pages or one `NO_PAGE_AVAILABLE`  
- Expired claim returns to queue  

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 2 Queue and Claiming
- TECH_SPEC_CLAIM.md
