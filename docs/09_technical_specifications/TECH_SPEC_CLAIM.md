# Claim Specification

**Library volume:** 8 — Technical Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## 1. Purpose

Atomic exclusive edit lock for a page (entry work) or match work unit (`PENDING_FREEZE`: match-claim underspecified in audit — lock policy before coding).

## 2. Claim Record

| Field | Notes |
| --- | --- |
| claimId | UUID |
| pageId | FK |
| claimantUserId | FK |
| claimType | ENTRY | MATCH (`PENDING_FREEZE`) |
| status | ACTIVE | RELEASED | EXPIRED | REASSIGNED |
| claimedAt | timestamptz |
| expiresAt | timestamptz |
| renewedAt | timestamptz |
| version | concurrency |

## 3. Defaults

- TTL: **30 minutes** from last renew/activity (design default).  
- Renew on draft save / heartbeat.  
- Warning UI before expiry.

## 4. Operations

| Op | Behavior |
| --- | --- |
| claim-next | Select eligible → insert active claim uniquely → audit |
| claim specific | Admin/override or allowed path |
| renew | Extend expiresAt if owner + ACTIVE |
| release | Soft release; draft preserved |
| reassign | Admin: release prior, create new, audit |
| expire job | Mark EXPIRED; page returns to queue; draft preserved |

## 5. Invariants

- **One ACTIVE claim per page per claimType.**  
- Expired ≠ delete draft.  
- Stale writes after lost claim → `PAGE_CLAIM_OWNERSHIP_LOST` / `PAGE_CLAIM_EXPIRED`.

## 6. Concurrency

Use transactional `SELECT … FOR UPDATE` on page + unique partial index on `(page_id) WHERE status = 'ACTIVE'`.

## 7. Audit

`PageClaimed` `ClaimRenewed` `ClaimReleased` `ClaimExpired` `ClaimReassigned`

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 2 Queue and Claiming
- Volume 9 `intake_page_claims`
