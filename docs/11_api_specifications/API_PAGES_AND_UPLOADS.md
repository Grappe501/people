# API — Pages & Uploads

**Library volume:** 10 — API Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

### POST /api/v1/batches/{batchId}/pages
Register page slot · Audit: PageRegistered

### POST /api/v1/pages/{pageId}/upload-intent
Returns storage upload instructions · Authz page · Audit: UploadIntentCreated

### POST /api/v1/pages/{pageId}/upload-complete
Verify object · activate image · Idempotency yes · Errors: UPLOAD_* · Audit: ImageUploaded

### POST /api/v1/pages/{pageId}/replace-image
New version · Audit: ImageReplaced

### GET /api/v1/pages/{pageId}
Page detail + entry summaries as authorized

### GET /api/v1/pages/{pageId}/image-access
Signed URL · short TTL · Audit metadata only · Errors: IMAGE_ACCESS_DENIED

### POST /api/v1/pages/{pageId}/image-quality
Pass/fail quality review · state transition

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
