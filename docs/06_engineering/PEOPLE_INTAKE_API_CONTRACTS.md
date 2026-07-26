# People Intake — API Contracts

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-SECURITY-API-ENGINEERING-DESIGN-1.0  
**Base path:** `/api/v1/` (conceptual)

---

## Principles

Versioned · authenticated · schema-validated · role-aware · state-aware · idempotent where required · transactional where required · audited where required · consistent errors.

No endpoint implemented without a completed per-operation contract including: Operation ID, method, path, purpose, roles, record authz, request/response schemas, state prerequisites/transition, transaction boundary, idempotency, audit, error codes, retry, rate limit, privacy classification.

---

## Response Envelope

Success:

```json
{ "ok": true, "data": {}, "meta": { "requestId": "..." } }
```

Error:

```json
{
  "ok": false,
  "error": { "code": "PAGE_CLAIM_CONFLICT", "message": "This page is no longer available.", "retryable": false },
  "meta": { "requestId": "..." }
}
```

Never include stack traces, SQL, credentials, tokens, or full PII in error metadata.

---

## Endpoint Inventory

### Session and User

```text
GET    /api/v1/session
GET    /api/v1/me
POST   /api/v1/sign-out
GET    /api/v1/users
POST   /api/v1/users/invite
PATCH  /api/v1/users/{userId}
POST   /api/v1/users/{userId}/disable
POST   /api/v1/users/{userId}/enable
```

### Batches

```text
GET    /api/v1/batches
POST   /api/v1/batches
GET    /api/v1/batches/{batchId}
PATCH  /api/v1/batches/{batchId}
POST   /api/v1/batches/{batchId}/complete-upload
POST   /api/v1/batches/{batchId}/archive
POST   /api/v1/batches/{batchId}/reopen
```

### Pages and Uploads

```text
POST   /api/v1/batches/{batchId}/pages
POST   /api/v1/pages/{pageId}/upload-intent
POST   /api/v1/pages/{pageId}/upload-complete
POST   /api/v1/pages/{pageId}/replace-image
GET    /api/v1/pages/{pageId}
GET    /api/v1/pages/{pageId}/image-access
POST   /api/v1/pages/{pageId}/image-quality
```

### Queue and Claims

```text
GET    /api/v1/queues/entry
POST   /api/v1/queues/entry/claim-next
POST   /api/v1/pages/{pageId}/claim
POST   /api/v1/pages/{pageId}/claim/renew
POST   /api/v1/pages/{pageId}/claim/release
POST   /api/v1/pages/{pageId}/claim/reassign
```

### Transcription

```text
GET    /api/v1/pages/{pageId}/draft
PUT    /api/v1/pages/{pageId}/draft
POST   /api/v1/pages/{pageId}/submit
POST   /api/v1/pages/{pageId}/return-unreadable
POST   /api/v1/pages/{pageId}/corrections
```

### Matching

```text
GET    /api/v1/matching/queue
POST   /api/v1/matching/claim-next
GET    /api/v1/entries/{entryId}/match-review
POST   /api/v1/entries/{entryId}/resolve-match
POST   /api/v1/entries/{entryId}/defer-match
POST   /api/v1/entries/{entryId}/return-correction
```

### Promotion

```text
GET    /api/v1/promotion/{promotionId}
POST   /api/v1/entries/{entryId}/promotion-request
POST   /api/v1/promotion/{promotionId}/retry
```

Browsers must not call raw canonical-person mutation endpoints.

### Administration

```text
GET    /api/v1/admin/overview
GET    /api/v1/admin/exceptions
GET    /api/v1/admin/audit
GET    /api/v1/admin/claims
POST   /api/v1/admin/pages/{pageId}/reopen
POST   /api/v1/admin/pages/{pageId}/force-complete
```

---

## Example: Claim Next Page

```text
Operation ID: claimNextEntryPage
POST /api/v1/queues/entry/claim-next
Roles: DATA_ENTRY, ADMIN, OWNER
Behavior: auth → authz → check active claim → select by priority/age → lock → create claim → update state → audit → return
Idempotency: required within request scope
Success: 200
Errors: AUTH_REQUIRED, ROLE_NOT_ALLOWED, ACTIVE_CLAIM_EXISTS, NO_PAGE_AVAILABLE, DATABASE_UNAVAILABLE, INTERNAL_ERROR
```

## Example: Submit Page

```text
Operation ID: submitIntakePage
POST /api/v1/pages/{pageId}/submit
Roles: DATA_ENTRY, ADMIN, OWNER
Requires: active claim (or override), valid state, matching version, 1–10 entries unless blank exception
Transaction: lock → validate claim → persist entries/conditions → normalize → status → release claim → audit → matching job → commit
Idempotency: required
Success: 200 or 202
Errors: PAGE_NOT_FOUND, PAGE_CLAIM_OWNERSHIP_LOST, PAGE_CLAIM_EXPIRED, STALE_WRITE, ENTRY_LIMIT_EXCEEDED, INVALID_STATE_TRANSITION, VALIDATION_FAILED, IDEMPOTENCY_CONFLICT
```

## Example: Resolve Match

```text
Operation ID: resolveEntryMatch
POST /api/v1/entries/{entryId}/resolve-match
Roles: REVIEWER, ADMIN, OWNER
Options: LINK_EXISTING | CREATE_NEW | RETURN_FOR_CORRECTION | DEFER | NO_ACTION
Transaction: lock → save resolution → update candidates → promotion request if needed → entry status → audit → commit
Idempotency: required
Errors: ENTRY_NOT_FOUND, MATCH_ALREADY_RESOLVED, REVIEW_CLAIM_LOST, INVALID_CANDIDATE, INVALID_FIELD_DECISION, STALE_WRITE
```

---

## HTTP Status Guidance

200/201/202/204 · 400/401/403/404/409/413/415/422/429 · 500/502/503  

Do not leak record existence via differentiated unauthorized responses when privacy requires uniformity.

Machine registry: `contracts/schemas/api-endpoint-registry.json`
