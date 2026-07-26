# Event Catalog

**Library volume:** Engineering Catalogs  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## Rule

Every meaningful mutation emits a catalogued audit event.

| Event | When |
| --- | --- |
| UserSignedIn | Successful auth (no secrets) |
| UserSignedOut | Sign-out |
| UserInvited | Admin invite |
| UserUpdated | Role/profile change |
| UserDisabled | Disable |
| UserEnabled | Enable |
| BatchCreated | New batch |
| BatchUpdated | Metadata change |
| BatchUploadCompleted | Upload complete |
| BatchArchived | Archive |
| BatchReopened | Reopen |
| PageRegistered | Page slot created |
| PageUploaded | Image activated |
| PageStatusChanged | Status transition |
| PageClaimed | Claim acquired |
| ClaimRenewed | TTL extended |
| ClaimReleased | Voluntary release |
| ClaimExpired | Expiry job |
| ClaimReassigned | Admin reassign |
| EntryDraftSaved | Draft persist |
| PageSubmitted | Submit success |
| PageReturned | Unreadable/return |
| EntryCorrected | Correction saved |
| ImageReplaced | New image version |
| UploadIntentCreated | Intent issued |
| ImageAccessGranted | Signed URL issued (meta only) |
| MatchRunStarted | Job start |
| MatchCandidatesGenerated | Candidates stored |
| MatchResolved | Resolution saved |
| MatchDeferred | Defer |
| MatchReturnedForCorrection | Return |
| PromotionRequested | Request created |
| PromotionSucceeded | Canonical OK |
| PromotionFailed | Canonical fail |
| PromotionRetried | Retry |
| PageReopened | Admin |
| PageForceCompleted | Admin |
| JobFailed | Dead/fail visible |

Payloads: references + redacted summaries only.

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- TECH_SPEC_AUDIT.md
