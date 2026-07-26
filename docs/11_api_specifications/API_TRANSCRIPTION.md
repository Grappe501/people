# API — Transcription

**Library volume:** 10 — API Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

### GET /api/v1/pages/{pageId}/draft
Requires claim ownership (or admin) · Returns entries + version

### PUT /api/v1/pages/{pageId}/draft
Autosave · version check · Errors: STALE_WRITE, PAGE_CLAIM_* · Audit: EntryDraftSaved (throttled policy OK)

### POST /api/v1/pages/{pageId}/submit
Validate 0–10/`PENDING_FREEZE` · normalize · release claim · enqueue match · Idempotency yes · Transactional  
Errors: ENTRY_LIMIT_EXCEEDED, VALIDATION_FAILED, INVALID_STATE_TRANSITION, STALE_WRITE  
Audit: PageSubmitted

### POST /api/v1/pages/{pageId}/return-unreadable
Exception path · Audit: PageReturned

### POST /api/v1/pages/{pageId}/corrections
Formal correction after return · Audit: EntryCorrected

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
