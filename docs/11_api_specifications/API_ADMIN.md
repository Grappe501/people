# API — Admin

**Library volume:** 10 — API Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

### GET /api/v1/admin/overview
Counts: queue depth, claims, exceptions, job failures

### GET /api/v1/admin/exceptions
Stuck pages/jobs

### GET /api/v1/admin/audit
Search audit events

### GET /api/v1/admin/claims
Active/expired claims

### POST /api/v1/admin/pages/{pageId}/reopen
Audit: PageReopened

### POST /api/v1/admin/pages/{pageId}/force-complete
Owner/Admin guarded · Audit: PageForceCompleted

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
