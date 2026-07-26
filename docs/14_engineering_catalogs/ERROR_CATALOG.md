# Error Catalog

**Library volume:** Engineering Catalogs  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## Registry

Machine file: `contracts/schemas/error-code-registry.json` (expand to match this catalog before coding).

| Code | HTTP | Retryable | User-safe intent |
| --- | --- | --- | --- |
| AUTH_REQUIRED | 401 | no | Sign in required |
| ACCESS_NOT_APPROVED | 403 | no | Account not approved |
| ACCOUNT_DISABLED | 403 | no | Account disabled |
| ROLE_NOT_ALLOWED | 403 | no | Not permitted |
| RECORD_ACCESS_DENIED | 403 | no | Not permitted |
| BATCH_NOT_FOUND | 404 | no | Not found |
| PAGE_NOT_FOUND | 404 | no | Not found |
| ENTRY_NOT_FOUND | 404 | no | Not found |
| PAGE_ALREADY_CLAIMED | 409 | no | Assigned to another user |
| PAGE_CLAIM_EXPIRED | 409 | no | Claim expired; draft preserved |
| PAGE_CLAIM_OWNERSHIP_LOST | 409 | no | No longer your claim |
| ACTIVE_CLAIM_EXISTS | 409 | no | Finish or release current claim |
| NO_PAGE_AVAILABLE | 200/404 | no | Queue empty (product choice of empty UX) |
| STALE_WRITE | 409 | yes | Refresh and retry |
| INVALID_STATE_TRANSITION | 409 | no | Action not available now |
| ENTRY_LIMIT_EXCEEDED | 422 | no | Max 10 people |
| VALIDATION_FAILED | 422 | no | Fix highlighted fields |
| UPLOAD_TYPE_NOT_ALLOWED | 415 | no | Unsupported file type |
| UPLOAD_TOO_LARGE | 413 | no | File too large |
| UPLOAD_CONFIRMATION_FAILED | 409 | yes | Retry upload confirm |
| IMAGE_ACCESS_DENIED | 403 | no | Cannot view image |
| MATCH_ALREADY_RESOLVED | 409 | no | Already resolved |
| INVALID_CANDIDATE | 422 | no | Invalid candidate |
| INVALID_FIELD_DECISION | 422 | no | Complete field decisions |
| REVIEW_CLAIM_LOST | 409 | no | Review claim lost |
| PROMOTION_PENDING | 409 | yes | Waiting on promotion |
| PROMOTION_ALREADY_COMPLETED | 409 | no | Already promoted |
| CANONICAL_SERVICE_UNAVAILABLE | 503 | yes | Try again later |
| IDEMPOTENCY_CONFLICT | 409 | no | Conflicting replay |
| RATE_LIMITED | 429 | yes | Slow down |
| DATABASE_UNAVAILABLE | 503 | yes | Could not save |
| DEPENDENCY_UNAVAILABLE | 503 | yes | Service unavailable |
| INTERNAL_ERROR | 500 | maybe | Something went wrong |

Each code must define operator action + log severity before production.

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 4 Error contract
