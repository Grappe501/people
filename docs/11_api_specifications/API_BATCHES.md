# API — Batches

**Library volume:** 10 — API Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

### GET /api/v1/batches
List batches for role scope.

### POST /api/v1/batches
Create DRAFT/UPLOADING batch · Idempotency yes · Audit: BatchCreated

### GET /api/v1/batches/{batchId}
Detail + progress summary.

### PATCH /api/v1/batches/{batchId}
Metadata update · Audit: BatchUpdated

### POST /api/v1/batches/{batchId}/complete-upload
Mark upload complete when pages registered · Audit: BatchUploadCompleted · Errors: INVALID_STATE_TRANSITION

### POST /api/v1/batches/{batchId}/archive | reopen
Admin/Owner · Audited

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
