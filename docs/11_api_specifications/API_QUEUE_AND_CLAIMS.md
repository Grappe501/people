# API — Queue & Claims

**Library volume:** 10 — API Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

### GET /api/v1/queues/entry
List eligible pages (non-authoritative vs claim).

### POST /api/v1/queues/entry/claim-next
**Critical path.** Atomic claim · Idempotency required · Transaction: select+lock+insert claim+audit  
Errors: ACTIVE_CLAIM_EXISTS, NO_PAGE_AVAILABLE, PAGE_ALREADY_CLAIMED, DATABASE_UNAVAILABLE  
Audit: PageClaimed  
Response: pageId, claimId, expiresAt, image access bootstrap

### POST /api/v1/pages/{pageId}/claim
Claim specific page when allowed.

### POST /api/v1/pages/{pageId}/claim/renew
Owner only · extends TTL · Audit: ClaimRenewed

### POST /api/v1/pages/{pageId}/claim/release
Owner or admin · Audit: ClaimReleased

### POST /api/v1/pages/{pageId}/claim/reassign
Admin · Audit: ClaimReassigned

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- API_CONVENTIONS.md
- api-endpoint-registry.json
