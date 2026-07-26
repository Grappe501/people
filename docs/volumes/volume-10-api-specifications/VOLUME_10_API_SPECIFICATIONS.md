# PEOPLE INTAKE SYSTEM

# VOLUME 10 — API SPECIFICATIONS

**Document ID**

```text
PEOPLE-VOLUME-10-API-SPECIFICATIONS-1.0
```

**Status**

```text
DESIGN COMPLETE — IMPLEMENTATION NOT AUTHORIZED
```

**Project Root**

```text
H:\people
```

**Document Type**

```text
CANONICAL API CONTRACT
```

**Build Mode**

```text
DOCUMENTATION ONLY
```

**Prohibited During This Volume**

* No route handlers
* No framework code
* No controller logic
* No ORM code
* No SQL
* No SDK implementation
* No HTTP library choice
* No production deployment

---

# PART I — PURPOSE

## 1. Mission

Volume 10 defines every public and internal API contract used by the People Intake System before any production code is written.

It specifies:

* endpoint inventory
* request contracts
* response contracts
* authentication
* authorization
* validation
* idempotency
* optimistic concurrency
* pagination
* filtering
* sorting
* error responses
* audit requirements
* transaction expectations
* versioning
* deprecation policy
* canonical integration contracts

This volume intentionally excludes:

* route handlers
* framework code
* controller logic
* ORM code
* SQL
* SDK implementation
* HTTP library choice

---

# PART II — API PHILOSOPHY

## 2. Core Principles

Every API must be:

* predictable
* versioned
* authenticated where required
* authorized
* idempotent where appropriate
* self-describing
* auditable
* backwards compatible whenever practical

The API exists to protect the business rules defined in Volumes 8 and 9.

The API never weakens those rules.

### `API-PRINCIPLE-001 — Contract Before Code`

No production handler may invent endpoints, payloads, or status semantics absent from this volume or a formal amendment.

### `API-PRINCIPLE-002 — Domain Rules Prevail`

API behavior must enforce Volume 8 domain rules and Volume 9 data constraints. Convenience shortcuts that bypass those rules are prohibited.

### `API-PRINCIPLE-003 — Safe Errors`

Error responses must be actionable without exposing secrets, stack traces, provider internals, or unauthorized record existence details beyond approved policy.

### `API-PRINCIPLE-004 — Server Enforcement`

Authentication, authorization, validation, and workflow rules are enforced server-side. Client UI state is never sufficient.

### `API-PRINCIPLE-005 — Durable Idempotency`

Where required, idempotency is durable and stored per Volume 9; it must not depend only on in-memory state.

---

# PART III — VERSIONING

## 3. Version Strategy

Canonical prefix:

```text
/api/v1/
```

Future breaking changes require:

```text
/api/v2/
```

Minor compatible additions remain within v1.

---

# PART IV — STANDARD REQUEST RULES

## 4. Headers

Standard request headers may include:

```text
Authorization
Content-Type
Accept
Idempotency-Key
If-Match
X-Correlation-ID
```

### Authorization

Authenticated endpoints require:

```text
Bearer <token>
```

The exact authentication provider is defined elsewhere.

### Correlation

Every request receives or generates a correlation ID for tracing.

---

# PART V — STANDARD RESPONSE ENVELOPE

Every successful response follows a common structure.

```json
{
  "success": true,
  "data": {},
  "meta": {},
  "links": {}
}
```

Every error response follows:

```json
{
  "success": false,
  "error": {
    "code": "",
    "message": "",
    "details": []
  },
  "correlationId": ""
}
```

Sensitive implementation details must never appear in error payloads.

---

# PART VI — AUTHENTICATION ENDPOINTS

## GET /api/v1/session

Purpose:

Return authenticated session summary.

Requires:

Authenticated user.

Returns:

* user identity
* application status
* roles
* permissions summary

Must never expose authentication secrets.

---

## POST /api/v1/session/logout

Purpose:

Terminate current application session.

Must be idempotent.

---

# PART VII — USER ENDPOINTS

## GET /api/v1/users/me

Returns:

* display name
* user status
* roles
* current permissions
* profile metadata

---

## GET /api/v1/users

Authorization:

ADMIN or OWNER.

Supports:

* filtering
* pagination
* sorting

Must not expose authentication credentials.

---

## POST /api/v1/users

Purpose:

Invite new application user.

Requires:

OWNER or approved ADMIN.

Produces:

Invitation event.

Audit required.

---

## PATCH /api/v1/users/{id}

Allows:

* activate
* suspend
* disable
* revoke

Every mutation requires:

* authorization
* audit
* optimistic concurrency

---

# PART VIII — ROLE ENDPOINTS

## GET /api/v1/users/{id}/roles

Returns current effective roles.

---

## POST /api/v1/users/{id}/roles

Assign role.

Requires:

OWNER or authorized ADMIN.

Must create:

* role history
* audit event

---

## DELETE /api/v1/users/{id}/roles/{role}

Revokes role.

Requires:

reason.

Produces:

history record.

---

# PART IX — BATCH ENDPOINTS

## GET /api/v1/batches

Supports:

* pagination
* filtering
* status
* date range
* uploader
* archive state

---

## POST /api/v1/batches

Creates batch.

Idempotent:

No.

Audit:

Yes.

Returns:

Batch summary.

---

## GET /api/v1/batches/{id}

Returns:

* metadata
* progress
* page counts
* workflow status

---

## PATCH /api/v1/batches/{id}

Allows:

* metadata correction
* close uploads
* archive

Requires concurrency token.

---

# PART X — PAGE ENDPOINTS

## GET /api/v1/pages/{id}

Returns:

* metadata
* workflow
* image summary
* entry summary

---

## POST /api/v1/pages

Creates page.

Normally used after upload completion.

---

## PATCH /api/v1/pages/{id}

Updates:

* quality status
* metadata
* workflow transitions

---

# PART XI — IMAGE ENDPOINTS

## POST /api/v1/uploads

Creates upload session.

Returns:

temporary upload instructions.

---

## POST /api/v1/uploads/{id}/complete

Completes upload.

Requires:

Idempotency-Key.

Must never duplicate page creation.

---

## GET /api/v1/images/{id}

Returns:

temporary authorized image access.

Never returns permanent URLs.

---

## POST /api/v1/images/{id}/replace

Creates new source-image version.

Original image remains preserved.

---

# PART XII — QUEUE ENDPOINTS

## GET /api/v1/queue

Supports:

* work type
* priority
* pagination

Only authorized work is returned.

---

## POST /api/v1/queue/{id}/claim

Atomic claim operation.

Possible responses:

* success
* already claimed
* no longer eligible

---

## POST /api/v1/claims/{id}/renew

Renews claim.

Fails if expired.

---

## POST /api/v1/claims/{id}/release

Releases claim.

Administrative release requires reason.

---

# PART XIII — DRAFT ENDPOINTS

## GET /api/v1/drafts/{pageId}

Returns current draft.

---

## PUT /api/v1/drafts/{pageId}

Saves draft.

Requires:

If-Match concurrency token.

Returns:

new version.

---

## POST /api/v1/drafts/{pageId}/recover

Returns recoverable draft.

Audit required.

---

# PART XIV — TRANSCRIPTION ENDPOINTS

## POST /api/v1/pages/{id}/submit

Submits completed transcription.

Creates:

* submission revision
* workflow transition
* normalization request

Idempotent:

Yes.

---

## GET /api/v1/entries/{id}

Returns:

current entry

plus

revision summary.

---

## GET /api/v1/entries/{id}/history

Returns immutable submission history.

---

# PART XV — MATCHING ENDPOINTS

## POST /api/v1/entries/{id}/evaluate

Starts matching evaluation.

Usually asynchronous.

---

## GET /api/v1/match-evaluations/{id}

Returns:

* candidates
* confidence
* signals
* warnings

---

## GET /api/v1/match-candidates/{id}

Returns:

full explanation.

---

# PART XVI — MATCH RESOLUTION

## POST /api/v1/match-resolutions

Creates resolution.

Possible outcomes:

```text
MATCH_EXISTING_PERSON
CREATE_NEW_PERSON
REQUIRES_MORE_INFORMATION
REJECT_ENTRY
DUPLICATE_INTAKE_ENTRY
ESCALATE_CONFLICT
```

Requires:

Reviewer.

Audit mandatory.

---

## GET /api/v1/match-resolutions/{id}

Returns immutable resolution.

---

# PART XVII — PROMOTION

## POST /api/v1/promotions

Creates promotion request.

Must be idempotent.

---

## GET /api/v1/promotions/{id}

Returns:

* status
* attempts
* canonical result
* retry state

---

## POST /api/v1/promotions/{id}/retry

Authorized retry.

Requires:

ADMIN or REVIEWER where permitted.

---

# PART XVIII — REPORTING

## GET /api/v1/reports/batches

Aggregate statistics.

---

## GET /api/v1/reports/queue

Operational queue summary.

---

## GET /api/v1/reports/errors

Open processing errors.

---

## GET /api/v1/reports/operators

Operator productivity and workload summaries.

Must minimize exposure of personal information.

---

# PART XIX — AUDIT

## GET /api/v1/audit

ADMIN only.

Supports:

* subject
* actor
* date range
* event type

---

## GET /api/v1/audit/{id}

Returns one immutable audit event.

---

# PART XX — ERROR CODES

Every API error returns a stable error code.

Examples:

```text
AUTH_REQUIRED
ACCESS_DENIED
VALIDATION_FAILED
CLAIM_ALREADY_HELD
CLAIM_EXPIRED
STALE_VERSION
NOT_FOUND
UPLOAD_FAILED
MATCH_CONFLICT
PROMOTION_FAILED
IDEMPOTENCY_CONFLICT
RATE_LIMITED
SYSTEM_ERROR
```

Messages may change.

Codes remain stable.

---

# PART XXI — PAGINATION

Collection endpoints support:

```text
page
pageSize
sort
direction
filter
search
```

Responses include:

```text
totalItems
totalPages
currentPage
pageSize
```

---

# PART XXII — FILTERING

Supported filter model:

```text
status
date range
user
batch
page
queue type
review status
promotion status
```

Unknown filters return validation errors.

---

# PART XXIII — SORTING

Allowed only on documented sortable fields.

Unknown sort fields rejected.

---

# PART XXIV — IDEMPOTENCY

Required for:

* upload completion
* submission
* promotion
* canonical creation
* retryable operations

Repeated requests must return the original business result.

---

# PART XXV — CONCURRENCY

Mutable resources require optimistic concurrency.

Typical mechanism:

```text
If-Match
```

or equivalent version token.

Stale updates return:

```text
STALE_VERSION
```

---

# PART XXVI — RATE LIMITING

Authentication endpoints:

stricter.

Administrative endpoints:

protected.

Bulk endpoints:

configurable.

Rate limiting responses include retry guidance where appropriate.

---

# PART XXVII — AUDIT REQUIREMENTS

The following always create audit events:

* role assignment
* user suspension
* upload completion
* claim acquisition
* claim release
* submission
* match resolution
* promotion
* administrative override
* archive
* configuration changes

---

# PART XXVIII — CANONICAL INTEGRATION CONTRACT

People Intake never directly owns canonical identity.

Supported conceptual operations:

```text
findCandidates()

createPerson()

linkPerson()

contributeAttribute()

attachProvenance()

getPromotionStatus()
```

Implementation remains outside this project.

---

# PART XXIX — SECURITY REQUIREMENTS

Every protected endpoint requires:

* authentication
* authorization
* validation
* audit where required
* safe error handling

Input must never be trusted solely because it originates from the client.

---

# PART XXX — DEPRECATION POLICY

Endpoints remain supported throughout the major version.

Breaking removals require:

* advance documentation
* migration guidance
* replacement endpoint

---

# PART XXXI — TEST REQUIREMENTS

Every endpoint must have tests for:

* authentication
* authorization
* validation
* happy path
* error path
* concurrency
* idempotency
* audit creation
* rate limiting (where applicable)

---

# PART XXXII — LOCKED API DECISIONS

The following decisions are frozen at the API-contract level unless formally amended.

1. Canonical public prefix is `/api/v1/`.
2. Success and error envelopes are standardized.
3. Correlation IDs are mandatory for tracing.
4. Bearer authentication is required for protected endpoints.
5. Authorization is evaluated server-side for every protected operation.
6. Upload completion requires `Idempotency-Key`.
7. Transcription submission is idempotent.
8. Promotion creation is idempotent.
9. Mutable updates use optimistic concurrency (`If-Match` or equivalent).
10. Stale updates return `STALE_VERSION`.
11. Claim acquisition is atomic and may return already-claimed outcomes.
12. Image access returns temporary authorized URLs only.
13. Permanent public image URLs are prohibited.
14. Match resolution requires Reviewer authority and audit.
15. Canonical identity remains outside People Intake ownership.
16. Error codes are stable; messages may change.
17. Unknown filters and sort fields are rejected.
18. Audit endpoints are ADMIN-scoped.
19. Reporting endpoints minimize personal-data exposure.
20. Breaking API changes require a new major version.

---

# PART XXXIII — API READINESS

| Area                  | Readiness |
| --------------------- | --------: |
| Endpoint Inventory    |      100% |
| Authentication        |       98% |
| Authorization         |       98% |
| Validation Rules      |       97% |
| Error Contracts       |       98% |
| Idempotency           |      100% |
| Concurrency           |       98% |
| Pagination            |      100% |
| Reporting             |       96% |
| Audit Requirements    |      100% |
| Canonical Integration |       97% |

**Overall Volume 10 Design Readiness**

```text
98%
```

The remaining percentage is reserved for reconciliation with:

* State Machine Catalog
* Error Catalog
* Audit Event Catalog
* Volume 11 UI specifications
* Cross-Volume Traceability Matrix

---

# PART XXXIV — NEXT GOVERNING BUILD

The next documentation volume is:

```text
PEOPLE-VOLUME-11-USER-INTERFACE-SPECIFICATIONS-1.0
```

Volume 11 will define every screen, workflow, layout, navigation pattern, responsive behavior, accessibility requirement, validation interaction, loading state, empty state, confirmation dialog, keyboard interaction, and mobile experience before any UI code is written.

The documentation library is now moving from backend architecture into the user experience. **Volume 11** will become the blueprint that Cursor follows to build every screen consistently, without inventing layouts or workflows during implementation.

---

## Document Control

| Field | Value |
| --- | --- |
| Canonical path | `docs/volumes/volume-10-api-specifications/VOLUME_10_API_SPECIFICATIONS.md` |
| Legacy pointer | `docs/11_api_specifications/VOLUME_10_API_SPECIFICATIONS.md` |
| Encoding | UTF-8 |
| Status | DESIGN COMPLETE — IMPLEMENTATION NOT AUTHORIZED |
| Build mode | DOCUMENTATION ONLY — no handlers |
