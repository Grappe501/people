# People Intake — Error Contract

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-SECURITY-API-ENGINEERING-DESIGN-1.0

---

## Categories

```text
AUTHENTICATION
AUTHORIZATION
VALIDATION
NOT_FOUND
CONFLICT
STATE
CLAIM
UPLOAD
STORAGE
MATCHING
PROMOTION
DATABASE
RATE_LIMIT
DEPENDENCY
INTERNAL
```

---

## Example Codes

```text
AUTH_REQUIRED
ACCESS_NOT_APPROVED
ACCOUNT_DISABLED
ROLE_NOT_ALLOWED
RECORD_ACCESS_DENIED
BATCH_NOT_FOUND
PAGE_NOT_FOUND
PAGE_ALREADY_CLAIMED
PAGE_CLAIM_EXPIRED
PAGE_CLAIM_OWNERSHIP_LOST
STALE_WRITE
INVALID_STATE_TRANSITION
ENTRY_LIMIT_EXCEEDED
UPLOAD_TYPE_NOT_ALLOWED
UPLOAD_TOO_LARGE
UPLOAD_CONFIRMATION_FAILED
IMAGE_ACCESS_DENIED
MATCH_ALREADY_RESOLVED
PROMOTION_ALREADY_COMPLETED
CANONICAL_SERVICE_UNAVAILABLE
IDEMPOTENCY_CONFLICT
RATE_LIMITED
INTERNAL_ERROR
ACTIVE_CLAIM_EXISTS
NO_PAGE_AVAILABLE
DATABASE_UNAVAILABLE
VALIDATION_FAILED
INVALID_CANDIDATE
INVALID_FIELD_DECISION
REVIEW_CLAIM_LOST
ENTRY_NOT_FOUND
```

Each error defines: code, user-safe message, HTTP status, retryable, operator action, logging severity, audit requirement.

---

## User Message Style

Plain language:

```text
This page is now assigned to another user. Your saved draft has been preserved.
```

Avoid exposing internal concurrency jargon.

---

## Severity

```text
INFO | WARNING | ERROR | CRITICAL
```

Critical examples: audit failure during privileged action; canonical duplication control failure; public image exposure; secret leakage; unauthorized schema modification.

---

## Failure Isolation Messages (Intent)

| Failure | User experience |
| --- | --- |
| Database | Could not save; draft remains available — never fake success |
| Storage | Upload incomplete; page-specific retry |
| Matching | Retryable processing; transcription preserved |
| Promotion | Resolution saved; pending promotion; page not falsely complete |
| Audit (high-risk) | Block completion |

---

## Degradation

| Dependency down | Allowed | Paused |
| --- | --- | --- |
| Canonical domain | Capture, upload, transcription, drafts | Candidate lookup; final resolution needing canonical; promotion |
| Object storage | Non-image admin views; queue metadata | New upload; image view; transcription needing image |
| Auth provider | Existing sessions per approved policy | New sign-in may be unavailable |

Machine registry: `contracts/schemas/error-code-registry.json`
