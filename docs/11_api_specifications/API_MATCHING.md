# API — Matching

**Library volume:** 10 — API Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

### GET /api/v1/matching/queue
Reviewer queue listing

### POST /api/v1/matching/claim-next
`PENDING_FREEZE` match-claim policy · Audit when locked

### GET /api/v1/entries/{entryId}/match-review
Candidates + entry + image access

### POST /api/v1/entries/{entryId}/resolve-match
Body: resolution + candidate/person + field decisions · Idempotency yes · May create promotion  
Errors: MATCH_ALREADY_RESOLVED, INVALID_CANDIDATE, REVIEW_CLAIM_LOST, STALE_WRITE  
Audit: MatchResolved

### POST /api/v1/entries/{entryId}/defer-match
Audit: MatchDeferred

### POST /api/v1/entries/{entryId}/return-correction
Audit: MatchReturnedForCorrection

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
