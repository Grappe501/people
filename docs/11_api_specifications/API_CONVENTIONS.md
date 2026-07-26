# API Conventions

**Library volume:** 10 — API Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## Envelope

Success: `{ "ok": true, "data": {}, "meta": { "requestId": "…" } }`  
Error: `{ "ok": false, "error": { "code", "message", "retryable" }, "meta": { "requestId" } }`

## Requirements per operation

Operation ID · method · path · purpose · roles · record authz · request schema · response schema · state prerequisites · transition · transaction boundary · idempotency · audit events · error codes · retry · privacy classification

## Auth

All routes authenticated except approved sign-in bootstrap.

## Idempotency

Header `Idempotency-Key` required on claim-next, submit, resolve-match, promotion-request, upload-complete.

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 4 API contracts
- ERROR_CATALOG.md
