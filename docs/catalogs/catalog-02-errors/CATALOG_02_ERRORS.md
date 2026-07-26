# PEOPLE INTAKE SYSTEM

# CATALOG 2 — ERROR CATALOG

**Document ID**

```text
PEOPLE-CATALOG-02-ERRORS-1.0
```

**Catalog Set**

```text
PEOPLE-CATALOG-LIBRARY-1.0
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
CANONICAL ERROR, FAILURE, AND RECOVERY CONTRACT
```

**Build Mode**

```text
DOCUMENTATION ONLY
```

**Prohibited During This Catalog**

* No error classes
* No route handlers
* No logging implementation
* No alerting implementation
* No database migrations
* No API middleware
* No monitoring configuration
* No UI components
* No retry workers
* No dependency installation
* No production error messages

---

# PART I — PURPOSE AND AUTHORITY

## 1. Purpose

The Error Catalog defines every stable failure condition used by the People Intake System.

It establishes:

* canonical error codes
* error categories
* severity
* ownership
* triggering conditions
* safe user messages
* operator explanations
* HTTP mappings
* retryability
* idempotency behavior
* preservation behavior
* recovery actions
* audit requirements
* alert requirements
* logging limits
* related state transitions
* required tests

This catalog answers:

> What failed, how serious is it, what was preserved, what may happen next, and how must the system communicate the failure safely?

---

## 2. Authority

The Error Catalog operationalizes:

* Volume 4 — Security, API, and Engineering
* Volume 5 — Quality, Operations, and Design Freeze
* Volume 8 — Technical Domain Specifications
* Volume 9 — Database Specifications
* Volume 10 — API Specifications
* Volume 11 — User Interface Specifications
* Volume 12 — Component Library and Design System
* Volume 13 — Canonical Platform Standards
* Catalog 1 — State Machine Catalog

No implementation may invent production error codes outside this catalog.

---

# PART II — ERROR DOCTRINE

## 3. Core Error Principles

### `ERROR-PRINCIPLE-001 — Preserve Work`

A failure must not erase user work where preservation is technically possible.

### `ERROR-PRINCIPLE-002 — Explain the Next Step`

Every user-facing error should state what the user may do next.

### `ERROR-PRINCIPLE-003 — Hide Sensitive Internals`

Users must not receive:

* stack traces
* SQL
* provider payloads
* tokens
* secrets
* filesystem paths
* database connection details
* internal hostnames
* unfiltered third-party responses

### `ERROR-PRINCIPLE-004 — Stable Codes, Flexible Messages`

Canonical codes remain stable.

User-facing wording may improve without changing the code’s meaning.

### `ERROR-PRINCIPLE-005 — Failure Is Not Business Rejection`

Technical failure and valid business refusal are distinct.

Examples:

```text
CLAIM_ALREADY_HELD
```

is not a system failure.

```text
UPLOAD_STORAGE_UNAVAILABLE
```

is a technical failure.

### `ERROR-PRINCIPLE-006 — Retry Must Be Safe`

Retry guidance may appear only when the operation is safely retryable.

### `ERROR-PRINCIPLE-007 — Acknowledgment Is Not Resolution`

An operator acknowledging an error does not mean the underlying condition is fixed.

### `ERROR-PRINCIPLE-008 — Error Severity Is Consequence-Based`

Severity depends on business impact, not how alarming the technical exception appears.

### `ERROR-PRINCIPLE-009 — Errors Remain Traceable`

Every significant failure must carry a correlation identifier.

### `ERROR-PRINCIPLE-010 — Unknown Must Not Become No`

Failure or missing data must never convert an unknown preference into a negative answer.

---

# PART III — ERROR RESPONSE CONTRACT

## 4. Standard API Error Envelope

```json
{
  "success": false,
  "error": {
    "code": "CLAIM_ALREADY_HELD",
    "message": "This page was just claimed by another user.",
    "details": [],
    "retryable": false,
    "workPreserved": true
  },
  "correlationId": "generated-correlation-id"
}
```

---

## 5. Required Error Fields

### `code`

Stable canonical machine key.

### `message`

Safe user-facing explanation.

### `details`

Optional structured validation or recovery information.

### `retryable`

Whether repeating the same operation may safely succeed.

### `workPreserved`

Whether user-entered or business data remains preserved.

### `correlationId`

Trace identifier.

---

## 6. Optional Error Fields

```text
field
resourceType
resourceId
currentVersion
expectedVersion
retryAfterSeconds
supportReference
recoveryAction
```

Personal information must not be included merely for convenience.

---

# PART IV — ERROR CATEGORIES

## 7. Canonical Categories

```text
AUTHENTICATION
AUTHORIZATION
SESSION
VALIDATION
NOT_FOUND
CONFLICT
CONCURRENCY
IDEMPOTENCY
UPLOAD
STORAGE
IMAGE
BATCH
PAGE
QUEUE
CLAIM
DRAFT
TRANSCRIPTION
NORMALIZATION
MATCHING
RESOLUTION
PROMOTION
CANONICAL_INTEGRATION
USER_MANAGEMENT
AUDIT
BACKGROUND_JOB
REPORTING
EXPORT
CONFIGURATION
RATE_LIMIT
DEPENDENCY
DATABASE
SECURITY
SYSTEM
```

---

# PART V — SEVERITY MODEL

## 8. Severity Levels

### `INFO`

Expected business condition requiring no operator intervention.

Examples:

* record already completed
* queue currently empty
* page claimed by someone else

### `WARNING`

Recoverable issue that may require user adjustment.

Examples:

* stale version
* upload retry needed
* draft save delayed

### `ERROR`

Operation failed and requires retry, correction, or operator action.

Examples:

* storage unavailable
* normalization failed
* promotion failed

### `CRITICAL`

System integrity, security, or broad workflow availability is threatened.

Examples:

* database unavailable
* audit persistence failure
* canonical duplicate-protection failure
* unauthorized privilege escalation attempt
* source evidence corruption affecting multiple records

---

## 9. Alerting Rule

Severity does not automatically equal alert severity.

An error creates an operator alert only when specified in its catalog entry.

Repeated lower-severity errors may trigger escalation through deduplication policy.

---

# PART VI — HTTP STATUS MAPPING

## 10. Standard Mapping

| HTTP Status | General Meaning                                          |
| ----------- | -------------------------------------------------------- |
| 400         | Invalid request                                          |
| 401         | Authentication required or session invalid               |
| 403         | Authenticated but not authorized                         |
| 404         | Authorized record not found                              |
| 409         | Conflict, stale version, claim, or idempotency collision |
| 410         | Resource intentionally expired or no longer available    |
| 413         | Upload exceeds permitted size                            |
| 415         | Unsupported content type                                 |
| 422         | Semantically invalid operation                           |
| 423         | Resource locked or claimed                               |
| 429         | Rate limited                                             |
| 500         | Unexpected internal failure                              |
| 502         | External dependency returned invalid failure             |
| 503         | Required service unavailable                             |
| 504         | External dependency timed out                            |

The API may use a more precise status only when it remains consistent across the platform.

---

# PART VII — ERROR ENTRY TEMPLATE

## 11. Required Entry Fields

Every error entry contains:

```text
Error ID
Canonical Code
Display Name
Category
Severity
Owning Domain
Trigger
HTTP Status
User Message
Operator Explanation
Retryable
Work Preserved
User Recovery
Operator Recovery
Audit Required
Alert Required
Log Classification
Related States
Related APIs
Required Tests
```

---

# PART VIII — AUTHENTICATION ERRORS

# 12. Authentication Required

**Error ID**

```text
ERROR-AUTH-001
```

**Canonical Code**

```text
AUTH_REQUIRED
```

**Category**

```text
AUTHENTICATION
```

**Severity**

```text
INFO
```

**Trigger**

A protected operation is attempted without a valid authenticated session.

**HTTP Status**

```text
401
```

**User Message**

```text
Please sign in to continue.
```

**Operator Explanation**

No valid authenticated identity was available for the request.

**Retryable**

```text
YES — after authentication
```

**Work Preserved**

```text
YES, where local or durable draft preservation exists
```

**User Recovery**

* sign in
* return to the prior workflow
* recover draft where available

**Audit Required**

Security access event only where policy requires.

**Alert Required**

No.

---

# 13. Invalid Credentials

**Error ID**

```text
ERROR-AUTH-002
```

**Canonical Code**

```text
AUTH_CREDENTIALS_INVALID
```

**HTTP Status**

```text
401
```

**User Message**

```text
We could not verify those sign-in details.
```

**Operator Explanation**

Authentication provider rejected the supplied credentials or proof.

**Retryable**

```text
YES
```

**Work Preserved**

```text
YES
```

**Security Rule**

Do not reveal whether a specific account exists.

---

# 14. Authentication Provider Unavailable

**Error ID**

```text
ERROR-AUTH-003
```

**Canonical Code**

```text
AUTH_PROVIDER_UNAVAILABLE
```

**Severity**

```text
ERROR
```

**HTTP Status**

```text
503
```

**User Message**

```text
Sign-in is temporarily unavailable.

Please try again.
```

**Retryable**

```text
YES
```

**Alert Required**

Yes when threshold is exceeded or multiple users are affected.

---

# 15. Access Invitation Invalid

**Error ID**

```text
ERROR-AUTH-004
```

**Canonical Code**

```text
ACCESS_INVITATION_INVALID
```

**HTTP Status**

```text
422
```

**User Message**

```text
This invitation cannot be used.
```

**Possible Causes**

* malformed invitation
* invitation does not match intended identity
* invitation revoked
* invitation already completed

**Work Preserved**

Not applicable.

---

# 16. Access Invitation Expired

**Error ID**

```text
ERROR-AUTH-005
```

**Canonical Code**

```text
ACCESS_INVITATION_EXPIRED
```

**HTTP Status**

```text
410
```

**User Message**

```text
This invitation has expired.

Ask an administrator for a new invitation.
```

---

# PART IX — SESSION ERRORS

# 17. Session Expired

**Error ID**

```text
ERROR-SESSION-001
```

**Canonical Code**

```text
SESSION_EXPIRED
```

**Category**

```text
SESSION
```

**Severity**

```text
WARNING
```

**HTTP Status**

```text
401
```

**User Message**

```text
Your session expired.

Sign in again to continue. Saved work remains available.
```

**Retryable**

```text
YES — after sign-in
```

**Work Preserved**

```text
YES
```

---

# 18. Session Revoked

**Error ID**

```text
ERROR-SESSION-002
```

**Canonical Code**

```text
SESSION_REVOKED
```

**HTTP Status**

```text
401
```

**User Message**

```text
This session is no longer active.

Please sign in again or contact an administrator.
```

**Possible Causes**

* user suspension
* role revocation
* administrative sign-out
* security action

**Audit Required**

Yes.

---

# 19. Session Refresh Failed

**Error ID**

```text
ERROR-SESSION-003
```

**Canonical Code**

```text
SESSION_REFRESH_FAILED
```

**HTTP Status**

```text
503
```

**User Message**

```text
We could not refresh your session.

Your unsaved work is still visible. Sign in again before leaving this page.
```

**Work Preserved**

```text
LOCAL OR DURABLE WORK MUST REMAIN PRESERVED WHERE POSSIBLE
```

---

# PART X — AUTHORIZATION ERRORS

# 20. Access Denied

**Error ID**

```text
ERROR-AUTHZ-001
```

**Canonical Code**

```text
ACCESS_DENIED
```

**Category**

```text
AUTHORIZATION
```

**Severity**

```text
WARNING
```

**HTTP Status**

```text
403
```

**User Message**

```text
You do not have permission to perform this action.
```

**Operator Explanation**

Authenticated user lacks the required permission or resource scope.

**Audit Required**

For high-risk attempted actions or repeated denials.

---

# 21. Role Required

**Error ID**

```text
ERROR-AUTHZ-002
```

**Canonical Code**

```text
ROLE_REQUIRED
```

**HTTP Status**

```text
403
```

**User Message**

```text
Your current role does not allow this action.
```

**Details**

May safely identify the required business capability but should not expose internal authorization architecture.

---

# 22. Resource Scope Denied

**Error ID**

```text
ERROR-AUTHZ-003
```

**Canonical Code**

```text
RESOURCE_SCOPE_DENIED
```

**HTTP Status**

```text
403
```

**User Message**

```text
You do not have access to this record.
```

**Privacy Rule**

Do not confirm the record’s sensitive details.

---

# 23. Administrative Override Not Allowed

**Error ID**

```text
ERROR-AUTHZ-004
```

**Canonical Code**

```text
ADMIN_OVERRIDE_NOT_ALLOWED
```

**HTTP Status**

```text
403
```

**User Message**

```text
This action cannot be overridden with your current authority.
```

**Audit Required**

Yes.

---

# 24. Final Owner Protection

**Error ID**

```text
ERROR-AUTHZ-005
```

**Canonical Code**

```text
FINAL_OWNER_PROTECTED
```

**HTTP Status**

```text
422
```

**User Message**

```text
The final active owner cannot be removed.

Assign another owner before continuing.
```

**Retryable**

Yes, after another owner is established.

---

# PART XI — VALIDATION ERRORS

# 25. Validation Failed

**Error ID**

```text
ERROR-VALIDATION-001
```

**Canonical Code**

```text
VALIDATION_FAILED
```

**Category**

```text
VALIDATION
```

**Severity**

```text
INFO
```

**HTTP Status**

```text
422
```

**User Message**

```text
Review the highlighted information before continuing.
```

**Details**

Field-level errors.

**Work Preserved**

```text
YES
```

---

# 26. Required Field Missing

**Error ID**

```text
ERROR-VALIDATION-002
```

**Canonical Code**

```text
REQUIRED_FIELD_MISSING
```

**HTTP Status**

```text
422
```

**User Message**

```text
Complete this required field.
```

---

# 27. Invalid Field Format

**Error ID**

```text
ERROR-VALIDATION-003
```

**Canonical Code**

```text
FIELD_FORMAT_INVALID
```

**User Message**

```text
Enter this value in the requested format.
```

**Important Rule**

Raw handwritten transcription should not be rejected merely because it does not match a normalized format.

This error applies only where the business field requires a valid application-format value.

---

# 28. Invalid Enumeration Value

**Error ID**

```text
ERROR-VALIDATION-004
```

**Canonical Code**

```text
ENUM_VALUE_INVALID
```

**User Message**

```text
Choose one of the available options.
```

**Operator Explanation**

A request supplied an undocumented or unsupported canonical value.

**Audit Required**

No, unless repeated malformed calls suggest abuse.

---

# 29. Unsupported Filter

**Error ID**

```text
ERROR-VALIDATION-005
```

**Canonical Code**

```text
FILTER_UNSUPPORTED
```

**HTTP Status**

```text
400
```

**User Message**

```text
One or more filters are not supported.
```

---

# 30. Unsupported Sort Field

**Error ID**

```text
ERROR-VALIDATION-006
```

**Canonical Code**

```text
SORT_FIELD_UNSUPPORTED
```

**HTTP Status**

```text
400
```

**User Message**

```text
This list cannot be sorted by that field.
```

---

# 31. Invalid Date Range

**Error ID**

```text
ERROR-VALIDATION-007
```

**Canonical Code**

```text
DATE_RANGE_INVALID
```

**User Message**

```text
Choose a valid starting and ending date.
```

---

# 32. Conflicting Field Condition

**Error ID**

```text
ERROR-VALIDATION-008
```

**Canonical Code**

```text
FIELD_CONDITION_CONFLICT
```

**User Message**

```text
The entered value conflicts with the selected field condition.
```

**Examples**

* value entered while condition is Not Provided
* no value entered while condition is Provided
* negative preference inferred from blank source

---

# 33. Empty Submission

**Error ID**

```text
ERROR-VALIDATION-009
```

**Canonical Code**

```text
SUBMISSION_EMPTY
```

**User Message**

```text
No entries are ready to submit from this page.
```

---

# 34. Duplicate Row Position

**Error ID**

```text
ERROR-VALIDATION-010
```

**Canonical Code**

```text
ROW_POSITION_DUPLICATE
```

**User Message**

```text
Two entries are assigned to the same row position.
```

**Severity**

```text
ERROR
```

**Alert Required**

Only if produced by server-side corruption rather than client validation.

---

# PART XII — NOT FOUND ERRORS

# 35. Record Not Found

**Error ID**

```text
ERROR-NOTFOUND-001
```

**Canonical Code**

```text
NOT_FOUND
```

**HTTP Status**

```text
404
```

**User Message**

```text
This record could not be found.
```

**Privacy Rule**

The response must not distinguish between nonexistent and inaccessible records when doing so could expose protected information.

---

# 36. Batch Not Found

```text
BATCH_NOT_FOUND
```

**Error ID**

```text
ERROR-NOTFOUND-002
```

**User Message**

```text
This batch could not be found.
```

---

# 37. Page Not Found

```text
PAGE_NOT_FOUND
```

**Error ID**

```text
ERROR-NOTFOUND-003
```

---

# 38. Entry Not Found

```text
ENTRY_NOT_FOUND
```

**Error ID**

```text
ERROR-NOTFOUND-004
```

---

# 39. User Not Found

```text
USER_NOT_FOUND
```

**Error ID**

```text
ERROR-NOTFOUND-005
```

**Privacy Rule**

Administrative use only where authorization permits.

---

# 40. Promotion Not Found

```text
PROMOTION_NOT_FOUND
```

**Error ID**

```text
ERROR-NOTFOUND-006
```

---

# PART XIII — CONCURRENCY ERRORS

# 41. Stale Version

**Error ID**

```text
ERROR-CONCURRENCY-001
```

**Canonical Code**

```text
STALE_VERSION
```

**Category**

```text
CONCURRENCY
```

**Severity**

```text
WARNING
```

**HTTP Status**

```text
409
```

**User Message**

```text
This record changed while you were working.

Review the latest version before saving again.
```

**Retryable**

```text
YES — after reload or merge
```

**Work Preserved**

```text
YES, where technically possible
```

**Required Details**

* expected version
* current version
* safe recovery action

---

# 42. Concurrent Transition Conflict

**Error ID**

```text
ERROR-CONCURRENCY-002
```

**Canonical Code**

```text
STATE_TRANSITION_CONFLICT
```

**HTTP Status**

```text
409
```

**User Message**

```text
This record moved to a different stage before your action completed.
```

**Operator Explanation**

Current persisted state does not permit the requested transition.

---

# 43. Duplicate Active Operation

**Error ID**

```text
ERROR-CONCURRENCY-003
```

**Canonical Code**

```text
OPERATION_ALREADY_RUNNING
```

**HTTP Status**

```text
409
```

**User Message**

```text
This operation is already in progress.
```

---

# PART XIV — IDEMPOTENCY ERRORS

# 44. Idempotency Conflict

**Error ID**

```text
ERROR-IDEMPOTENCY-001
```

**Canonical Code**

```text
IDEMPOTENCY_CONFLICT
```

**Category**

```text
IDEMPOTENCY
```

**Severity**

```text
ERROR
```

**HTTP Status**

```text
409
```

**Trigger**

Same idempotency key used with a different request fingerprint.

**User Message**

```text
This request conflicts with an earlier operation.

Refresh the record before trying again.
```

**Audit Required**

Yes for canonical or high-risk operations.

**Alert Required**

Yes if repeated or occurring in promotion workflows.

---

# 45. Idempotency Record In Progress

**Error ID**

```text
ERROR-IDEMPOTENCY-002
```

**Canonical Code**

```text
IDEMPOTENCY_OPERATION_IN_PROGRESS
```

**HTTP Status**

```text
409
```

**User Message**

```text
This operation is still being processed.
```

**Retryable**

Yes, after delay.

---

# 46. Idempotency Result Unavailable

**Error ID**

```text
ERROR-IDEMPOTENCY-003
```

**Canonical Code**

```text
IDEMPOTENCY_RESULT_UNAVAILABLE
```

**Severity**

```text
CRITICAL
```

**User Message**

```text
We could not safely confirm the result of this operation.

Do not repeat the action until an administrator reviews it.
```

**Alert Required**

Yes, immediate.

**Applies Especially To**

* canonical person creation
* promotion
* user-access revocation
* destructive retention actions

---

# PART XV — BATCH ERRORS

# 47. Batch State Invalid

**Error ID**

```text
ERROR-BATCH-001
```

**Canonical Code**

```text
BATCH_STATE_INVALID
```

**HTTP Status**

```text
422
```

**User Message**

```text
This batch is not in a stage that allows this action.
```

---

# 48. Batch Uploads Closed

**Error ID**

```text
ERROR-BATCH-002
```

**Canonical Code**

```text
BATCH_UPLOADS_CLOSED
```

**User Message**

```text
Uploads are closed for this batch.
```

**Retryable**

Only after authorized reopening.

---

# 49. Batch Completion Blocked

**Error ID**

```text
ERROR-BATCH-003
```

**Canonical Code**

```text
BATCH_COMPLETION_BLOCKED
```

**User Message**

```text
This batch cannot be completed yet.

Resolve the remaining work before continuing.
```

**Details May Include**

* unresolved entries
* active claims
* image issues
* retryable promotions
* open blocking errors

---

# 50. Batch Already Archived

**Error ID**

```text
ERROR-BATCH-004
```

**Canonical Code**

```text
BATCH_ALREADY_ARCHIVED
```

**User Message**

```text
This batch is already archived.
```

---

# PART XVI — PAGE ERRORS

# 51. Page State Invalid

```text
PAGE_STATE_INVALID
```

**Error ID**

```text
ERROR-PAGE-001
```

**User Message**

```text
This page is not in a stage that allows this action.
```

---

# 52. Page Has No Usable Image

```text
PAGE_IMAGE_NOT_USABLE
```

**Error ID**

```text
ERROR-PAGE-002
```

**User Message**

```text
This page needs a usable source image before work can continue.
```

---

# 53. Page Already Submitted

```text
PAGE_ALREADY_SUBMITTED
```

**Error ID**

```text
ERROR-PAGE-003
```

**HTTP Status**

```text
409
```

**User Message**

```text
This page has already been submitted.
```

**Recovery**

Open the immutable submitted version or begin an authorized correction revision.

---

# 54. Page Sequence Conflict

```text
PAGE_SEQUENCE_CONFLICT
```

**Error ID**

```text
ERROR-PAGE-004
```

**User Message**

```text
Another page already uses this sequence number.
```

---

# PART XVII — UPLOAD ERRORS

# 55. Upload Session Invalid

**Error ID**

```text
ERROR-UPLOAD-001
```

**Canonical Code**

```text
UPLOAD_SESSION_INVALID
```

**Category**

```text
UPLOAD
```

**HTTP Status**

```text
422
```

**User Message**

```text
This upload session cannot be used.
```

---

# 56. Upload Session Expired

**Error ID**

```text
ERROR-UPLOAD-002
```

**Canonical Code**

```text
UPLOAD_SESSION_EXPIRED
```

**HTTP Status**

```text
410
```

**User Message**

```text
This upload session expired.

Start the upload again.
```

---

# 57. Upload File Too Large

**Error ID**

```text
ERROR-UPLOAD-003
```

**Canonical Code**

```text
UPLOAD_FILE_TOO_LARGE
```

**HTTP Status**

```text
413
```

**User Message**

```text
This file is larger than the allowed upload size.
```

**Details**

May include the permitted maximum.

---

# 58. Upload Type Unsupported

**Error ID**

```text
ERROR-UPLOAD-004
```

**Canonical Code**

```text
UPLOAD_TYPE_UNSUPPORTED
```

**HTTP Status**

```text
415
```

**User Message**

```text
This file type is not supported.
```

---

# 59. Upload File Corrupt

**Error ID**

```text
ERROR-UPLOAD-005
```

**Canonical Code**

```text
UPLOAD_FILE_CORRUPT
```

**HTTP Status**

```text
422
```

**User Message**

```text
This file could not be read.

Choose a different copy of the image.
```

---

# 60. Upload Integrity Check Failed

**Error ID**

```text
ERROR-UPLOAD-006
```

**Canonical Code**

```text
UPLOAD_INTEGRITY_FAILED
```

**Severity**

```text
ERROR
```

**User Message**

```text
The uploaded file could not be verified.

Please upload it again.
```

**Alert Required**

If repeated or broad.

---

# 61. Upload Duplicate Suspected

**Error ID**

```text
ERROR-UPLOAD-007
```

**Canonical Code**

```text
UPLOAD_DUPLICATE_SUSPECTED
```

**Severity**

```text
INFO
```

**HTTP Status**

```text
409
```

**User Message**

```text
This image appears similar to one already in the batch.
```

**Important Rule**

This is a review condition, not necessarily a rejection.

---

# 62. Upload Completion Failed

**Error ID**

```text
ERROR-UPLOAD-008
```

**Canonical Code**

```text
UPLOAD_COMPLETION_FAILED
```

**Severity**

```text
ERROR
```

**User Message**

```text
The file uploaded, but the page could not be finalized.

Your upload remains preserved for review.
```

**Work Preserved**

```text
YES
```

**Alert Required**

Yes when the page relationship cannot be completed automatically.

---

# PART XVIII — STORAGE ERRORS

# 63. Storage Unavailable

**Error ID**

```text
ERROR-STORAGE-001
```

**Canonical Code**

```text
STORAGE_UNAVAILABLE
```

**Category**

```text
STORAGE
```

**Severity**

```text
ERROR
```

**HTTP Status**

```text
503
```

**User Message**

```text
File storage is temporarily unavailable.

Please try again.
```

**Alert Required**

Yes when threshold exceeded.

---

# 64. Storage Object Missing

**Error ID**

```text
ERROR-STORAGE-002
```

**Canonical Code**

```text
STORAGE_OBJECT_MISSING
```

**Severity**

```text
CRITICAL
```

**HTTP Status**

```text
500
```

**User Message**

```text
The source file could not be found.

An administrator has been notified.
```

**Work Preserved**

Structured records remain preserved; source evidence status must move to exception.

**Alert Required**

Immediate.

---

# 65. Storage Verification Failed

**Error ID**

```text
ERROR-STORAGE-003
```

**Canonical Code**

```text
STORAGE_VERIFICATION_FAILED
```

**User Message**

```text
The stored file could not be verified.
```

**Alert Required**

Yes.

---

# 66. Storage Access Denied

**Error ID**

```text
ERROR-STORAGE-004
```

**Canonical Code**

```text
STORAGE_ACCESS_DENIED
```

**HTTP Status**

```text
403
```

**User Message**

```text
You do not have permission to access this source file.
```

**Audit Required**

Yes for repeated or suspicious requests.

---

# 67. Storage Access Link Expired

**Error ID**

```text
ERROR-STORAGE-005
```

**Canonical Code**

```text
STORAGE_ACCESS_EXPIRED
```

**HTTP Status**

```text
410
```

**User Message**

```text
This image-access link expired.

Refresh the page to continue.
```

---

# PART XIX — IMAGE ERRORS

# 68. Image Replacement Required

```text
IMAGE_REPLACEMENT_REQUIRED
```

**Error ID**

```text
ERROR-IMAGE-001
```

**Severity**

```text
WARNING
```

**User Message**

```text
This page needs a clearer replacement image.
```

---

# 69. Image Version Conflict

```text
IMAGE_VERSION_CONFLICT
```

**Error ID**

```text
ERROR-IMAGE-002
```

**HTTP Status**

```text
409
```

**User Message**

```text
A newer image version is available.

Reload the page before continuing.
```

---

# 70. Image Rotation Failed

```text
IMAGE_DISPLAY_TRANSFORM_FAILED
```

**Error ID**

```text
ERROR-IMAGE-003
```

**Severity**

```text
WARNING
```

**User Message**

```text
The image view could not be adjusted.

The original file remains unchanged.
```

---

# PART XX — QUEUE ERRORS

# 71. Queue Empty

**Error ID**

```text
ERROR-QUEUE-001
```

**Canonical Code**

```text
QUEUE_EMPTY
```

**Category**

```text
QUEUE
```

**Severity**

```text
INFO
```

**HTTP Status**

```text
404
```

or successful empty collection according to endpoint semantics.

**User Message**

```text
No eligible work is available right now.
```

**Important Rule**

Queue empty is normally an ordinary state, not a failure.

---

# 72. Queue Item No Longer Eligible

**Error ID**

```text
ERROR-QUEUE-002
```

**Canonical Code**

```text
QUEUE_ITEM_NOT_ELIGIBLE
```

**HTTP Status**

```text
409
```

**User Message**

```text
This item is no longer available for this type of work.
```

---

# 73. Queue Projection Stale

**Error ID**

```text
ERROR-QUEUE-003
```

**Canonical Code**

```text
QUEUE_PROJECTION_STALE
```

**Severity**

```text
WARNING
```

**User Message**

```text
The queue changed before your action completed.

Refresh the list and try again.
```

**Alert Required**

Only if repeated beyond expected concurrency.

---

# PART XXI — CLAIM ERRORS

# 74. Claim Already Held

**Error ID**

```text
ERROR-CLAIM-001
```

**Canonical Code**

```text
CLAIM_ALREADY_HELD
```

**Category**

```text
CLAIM
```

**Severity**

```text
INFO
```

**HTTP Status**

```text
423
```

**User Message**

```text
This page was just claimed by another user.

Choose another available page.
```

**Work Preserved**

Not applicable.

---

# 75. Claim Not Owned

**Error ID**

```text
ERROR-CLAIM-002
```

**Canonical Code**

```text
CLAIM_NOT_OWNED
```

**HTTP Status**

```text
403
```

**User Message**

```text
This work is not currently reserved for you.
```

---

# 76. Claim Expired

**Error ID**

```text
ERROR-CLAIM-003
```

**Canonical Code**

```text
CLAIM_EXPIRED
```

**HTTP Status**

```text
409
```

**User Message**

```text
Your reservation expired.

Your saved draft remains available.
```

**Work Preserved**

```text
YES
```

---

# 77. Claim Renewal Denied

**Error ID**

```text
ERROR-CLAIM-004
```

**Canonical Code**

```text
CLAIM_RENEWAL_DENIED
```

**User Message**

```text
This reservation could not be extended.
```

**Possible Causes**

* claim already expired
* work no longer eligible
* administrative release
* replacement claim exists

---

# 78. Claim Release Failed

**Error ID**

```text
ERROR-CLAIM-005
```

**Canonical Code**

```text
CLAIM_RELEASE_FAILED
```

**User Message**

```text
The reservation could not be released.

Your saved work remains preserved.
```

---

# 79. Active Claim Required

**Error ID**

```text
ERROR-CLAIM-006
```

**Canonical Code**

```text
ACTIVE_CLAIM_REQUIRED
```

**HTTP Status**

```text
423
```

**User Message**

```text
Claim this work before making changes.
```

---

# PART XXII — DRAFT ERRORS

# 80. Draft Save Failed

**Error ID**

```text
ERROR-DRAFT-001
```

**Canonical Code**

```text
DRAFT_SAVE_FAILED
```

**Category**

```text
DRAFT
```

**Severity**

```text
ERROR
```

**User Message**

```text
Your draft could not be saved.

Your entries are still visible. Try again before leaving this page.
```

**Retryable**

```text
YES
```

**Work Preserved**

```text
LOCAL WORK SHOULD REMAIN PRESERVED
```

---

# 81. Draft Not Found

**Error ID**

```text
ERROR-DRAFT-002
```

**Canonical Code**

```text
DRAFT_NOT_FOUND
```

**HTTP Status**

```text
404
```

**User Message**

```text
No recoverable draft was found for this page.
```

---

# 82. Draft Recovery Denied

**Error ID**

```text
ERROR-DRAFT-003
```

**Canonical Code**

```text
DRAFT_RECOVERY_DENIED
```

**HTTP Status**

```text
403
```

**User Message**

```text
You do not have permission to recover this draft.
```

---

# 83. Draft Already Submitted

**Error ID**

```text
ERROR-DRAFT-004
```

**Canonical Code**

```text
DRAFT_ALREADY_SUBMITTED
```

**HTTP Status**

```text
409
```

**User Message**

```text
This draft has already been submitted.
```

---

# 84. Draft Revision Conflict

**Error ID**

```text
ERROR-DRAFT-005
```

**Canonical Code**

```text
DRAFT_REVISION_CONFLICT
```

**User Message**

```text
A newer draft revision exists.

Review the latest version before saving.
```

---

# PART XXIII — TRANSCRIPTION ERRORS

# 85. Transcription Submission Failed

**Error ID**

```text
ERROR-TRANSCRIPTION-001
```

**Canonical Code**

```text
TRANSCRIPTION_SUBMISSION_FAILED
```

**Category**

```text
TRANSCRIPTION
```

**Severity**

```text
ERROR
```

**User Message**

```text
The page could not be submitted.

Your saved draft remains available.
```

**Retryable**

Yes.

---

# 86. Transcription Structural Validation Failed

**Error ID**

```text
ERROR-TRANSCRIPTION-002
```

**Canonical Code**

```text
TRANSCRIPTION_STRUCTURE_INVALID
```

**User Message**

```text
Review the page entries before submitting.
```

**Examples**

* duplicate row positions
* invalid field conditions
* unsaved changes
* missing active image
* stale claim

---

# 87. Transcription Revision Superseded

**Error ID**

```text
ERROR-TRANSCRIPTION-003
```

**Canonical Code**

```text
TRANSCRIPTION_REVISION_SUPERSEDED
```

**HTTP Status**

```text
409
```

**User Message**

```text
A newer transcription revision is now current.
```

---

# 88. Correction Request Invalid

**Error ID**

```text
ERROR-TRANSCRIPTION-004
```

**Canonical Code**

```text
CORRECTION_REQUEST_INVALID
```

**User Message**

```text
The correction request is incomplete or no longer applies.
```

---

# 89. Correction Already Resolved

**Error ID**

```text
ERROR-TRANSCRIPTION-005
```

**Canonical Code**

```text
CORRECTION_ALREADY_RESOLVED
```

**User Message**

```text
This correction request has already been resolved.
```

---

# PART XXIV — NORMALIZATION ERRORS

# 90. Normalization Failed

**Error ID**

```text
ERROR-NORMALIZATION-001
```

**Canonical Code**

```text
NORMALIZATION_FAILED
```

**Category**

```text
NORMALIZATION
```

**Severity**

```text
ERROR
```

**User Message**

```text
This entry could not be prepared for matching.

The original transcription remains unchanged.
```

**Retryable**

Depends on cause.

**Work Preserved**

```text
YES
```

---

# 91. Normalization Version Unsupported

**Error ID**

```text
ERROR-NORMALIZATION-002
```

**Canonical Code**

```text
NORMALIZATION_VERSION_UNSUPPORTED
```

**Severity**

```text
CRITICAL
```

**Alert Required**

Yes.

---

# 92. Normalized Value Conflict

**Error ID**

```text
ERROR-NORMALIZATION-003
```

**Canonical Code**

```text
NORMALIZED_VALUE_CONFLICT
```

**User Message**

```text
The system found conflicting normalized values for this field.
```

**Recovery**

Human review.

---

# PART XXV — MATCHING ERRORS

# 93. Match Evaluation Failed

**Error ID**

```text
ERROR-MATCH-001
```

**Canonical Code**

```text
MATCH_EVALUATION_FAILED
```

**Category**

```text
MATCHING
```

**Severity**

```text
ERROR
```

**User Message**

```text
Matching could not be completed.

The entry remains available for retry or review.
```

---

# 94. Match Candidates Unavailable

**Error ID**

```text
ERROR-MATCH-002
```

**Canonical Code**

```text
MATCH_CANDIDATES_UNAVAILABLE
```

**User Message**

```text
Candidate records are temporarily unavailable.
```

**Retryable**

Yes.

---

# 95. Match Conflict

**Error ID**

```text
ERROR-MATCH-003
```

**Canonical Code**

```text
MATCH_CONFLICT
```

**Severity**

```text
WARNING
```

**HTTP Status**

```text
422
```

**User Message**

```text
The available identity evidence conflicts.

A reviewer must resolve the conflict before continuing.
```

**Important Rule**

This is a business-review condition, not necessarily a technical failure.

---

# 96. Match Evaluation Superseded

**Error ID**

```text
ERROR-MATCH-004
```

**Canonical Code**

```text
MATCH_EVALUATION_SUPERSEDED
```

**User Message**

```text
A newer match evaluation is available.
```

---

# 97. Match Algorithm Version Missing

**Error ID**

```text
ERROR-MATCH-005
```

**Canonical Code**

```text
MATCH_ALGORITHM_VERSION_MISSING
```

**Severity**

```text
CRITICAL
```

**Alert Required**

Immediate.

**Reason**

A completed evaluation cannot be trusted without its algorithm version.

---

# 98. Match Explanation Missing

**Error ID**

```text
ERROR-MATCH-006
```

**Canonical Code**

```text
MATCH_EXPLANATION_MISSING
```

**Severity**

```text
ERROR
```

**User Message**

```text
The system could not explain this candidate result.

Do not finalize the match until the evaluation is complete.
```

---

# PART XXVI — RESOLUTION ERRORS

# 99. Resolution Outcome Invalid

**Error ID**

```text
ERROR-RESOLUTION-001
```

**Canonical Code**

```text
RESOLUTION_OUTCOME_INVALID
```

**Category**

```text
RESOLUTION
```

**User Message**

```text
Choose a valid resolution outcome.
```

---

# 100. Resolution Candidate Required

**Error ID**

```text
ERROR-RESOLUTION-002
```

**Canonical Code**

```text
RESOLUTION_CANDIDATE_REQUIRED
```

**User Message**

```text
Select the existing person this entry should match.
```

---

# 101. Resolution Reason Required

**Error ID**

```text
ERROR-RESOLUTION-003
```

**Canonical Code**

```text
RESOLUTION_REASON_REQUIRED
```

**User Message**

```text
Add a reason before finalizing this decision.
```

---

# 102. Resolution Conflict Not Acknowledged

**Error ID**

```text
ERROR-RESOLUTION-004
```

**Canonical Code**

```text
RESOLUTION_CONFLICT_NOT_ACKNOWLEDGED
```

**User Message**

```text
Review and acknowledge the conflicting evidence before finalizing.
```

---

# 103. Resolution Already Finalized

**Error ID**

```text
ERROR-RESOLUTION-005
```

**Canonical Code**

```text
RESOLUTION_ALREADY_FINALIZED
```

**HTTP Status**

```text
409
```

**User Message**

```text
This resolution has already been finalized.
```

---

# 104. Resolution Reopen Not Allowed

**Error ID**

```text
ERROR-RESOLUTION-006
```

**Canonical Code**

```text
RESOLUTION_REOPEN_NOT_ALLOWED
```

**User Message**

```text
This resolution cannot be reopened under the current policy.
```

**Audit Required**

Yes for attempted administrative override.

---

# 105. Duplicate Entry Target Required

**Error ID**

```text
ERROR-RESOLUTION-007
```

**Canonical Code**

```text
DUPLICATE_ENTRY_TARGET_REQUIRED
```

**User Message**

```text
Select the primary intake entry before marking this entry as a duplicate.
```

---

# PART XXVII — PROMOTION ERRORS

# 106. Promotion Failed

**Error ID**

```text
ERROR-PROMOTION-001
```

**Canonical Code**

```text
PROMOTION_FAILED
```

**Category**

```text
PROMOTION
```

**Severity**

```text
ERROR
```

**User Message**

```text
The approved identity decision could not be promoted.

The resolution remains preserved.
```

**Work Preserved**

```text
YES
```

---

# 107. Promotion Retry Not Allowed

**Error ID**

```text
ERROR-PROMOTION-002
```

**Canonical Code**

```text
PROMOTION_RETRY_NOT_ALLOWED
```

**User Message**

```text
This promotion cannot be retried in its current state.
```

---

# 108. Promotion Already Running

**Error ID**

```text
ERROR-PROMOTION-003
```

**Canonical Code**

```text
PROMOTION_ALREADY_RUNNING
```

**HTTP Status**

```text
409
```

**User Message**

```text
This promotion is already being processed.
```

---

# 109. Promotion Already Succeeded

**Error ID**

```text
ERROR-PROMOTION-004
```

**Canonical Code**

```text
PROMOTION_ALREADY_SUCCEEDED
```

**User Message**

```text
This promotion has already completed successfully.
```

---

# 110. Promotion Idempotency Missing

**Error ID**

```text
ERROR-PROMOTION-005
```

**Canonical Code**

```text
PROMOTION_IDEMPOTENCY_MISSING
```

**Severity**

```text
CRITICAL
```

**User Message**

```text
This promotion cannot proceed safely.

An administrator has been notified.
```

**Alert Required**

Immediate.

---

# 111. Promotion Canonical Result Missing

**Error ID**

```text
ERROR-PROMOTION-006
```

**Canonical Code**

```text
PROMOTION_CANONICAL_RESULT_MISSING
```

**Severity**

```text
CRITICAL
```

**Trigger**

External canonical operation appears successful, but the required canonical identifier or durable response is absent.

**User Message**

```text
The promotion result could not be safely confirmed.

Do not retry until an administrator reviews it.
```

**Alert Required**

Immediate.

---

# 112. Promotion Provenance Failed

**Error ID**

```text
ERROR-PROMOTION-007
```

**Canonical Code**

```text
PROMOTION_PROVENANCE_FAILED
```

**Severity**

```text
CRITICAL
```

**User Message**

```text
The canonical update could not be completed with its required history.

An administrator has been notified.
```

**Important Rule**

Promotion must not be considered fully successful without provenance.

---

# PART XXVIII — CANONICAL INTEGRATION ERRORS

# 113. Canonical Service Unavailable

**Error ID**

```text
ERROR-CANONICAL-001
```

**Canonical Code**

```text
CANONICAL_SERVICE_UNAVAILABLE
```

**HTTP Status**

```text
503
```

**User Message**

```text
The canonical people system is temporarily unavailable.

The approved resolution remains preserved.
```

**Retryable**

Yes.

---

# 114. Canonical Service Timeout

**Error ID**

```text
ERROR-CANONICAL-002
```

**Canonical Code**

```text
CANONICAL_SERVICE_TIMEOUT
```

**HTTP Status**

```text
504
```

**User Message**

```text
The canonical people system did not respond in time.

The result will be reviewed before any retry.
```

**Important Rule**

Timeout after a create request requires idempotent result verification before retry.

---

# 115. Canonical Person Not Found

**Error ID**

```text
ERROR-CANONICAL-003
```

**Canonical Code**

```text
CANONICAL_PERSON_NOT_FOUND
```

**User Message**

```text
The selected canonical person is no longer available.
```

---

# 116. Canonical Duplicate Risk

**Error ID**

```text
ERROR-CANONICAL-004
```

**Canonical Code**

```text
CANONICAL_DUPLICATE_RISK
```

**Severity**

```text
CRITICAL
```

**User Message**

```text
This operation may create or link a duplicate person.

A reviewer must resolve the conflict before continuing.
```

**Alert Required**

Yes.

---

# 117. Canonical Contract Invalid

**Error ID**

```text
ERROR-CANONICAL-005
```

**Canonical Code**

```text
CANONICAL_CONTRACT_INVALID
```

**Severity**

```text
CRITICAL
```

**Trigger**

Canonical system response does not satisfy the approved integration contract.

**Alert Required**

Immediate.

---

# 118. Canonical Attribute Conflict

**Error ID**

```text
ERROR-CANONICAL-006
```

**Canonical Code**

```text
CANONICAL_ATTRIBUTE_CONFLICT
```

**User Message**

```text
The intake value conflicts with existing canonical information.

A reviewer must decide how to proceed.
```

---

# PART XXIX — USER MANAGEMENT ERRORS

# 119. User Already Exists

```text
USER_ALREADY_EXISTS
```

**Error ID**

```text
ERROR-USER-001
```

**User Message**

```text
A user with this identity already exists.
```

---

# 120. User State Invalid

```text
USER_STATE_INVALID
```

**Error ID**

```text
ERROR-USER-002
```

**User Message**

```text
This user is not in a state that allows this action.
```

---

# 121. Role Already Assigned

```text
ROLE_ALREADY_ASSIGNED
```

**Error ID**

```text
ERROR-USER-003
```

**User Message**

```text
This role is already assigned.
```

---

# 122. Role Not Assigned

```text
ROLE_NOT_ASSIGNED
```

**Error ID**

```text
ERROR-USER-004
```

**User Message**

```text
This user does not currently have that role.
```

---

# 123. Active Work Blocks User Change

```text
USER_CHANGE_BLOCKED_BY_ACTIVE_WORK
```

**Error ID**

```text
ERROR-USER-005
```

**User Message**

```text
This user has active work that must be handled before continuing.
```

---

# PART XXX — AUDIT ERRORS

# 124. Audit Write Failed

**Error ID**

```text
ERROR-AUDIT-001
```

**Canonical Code**

```text
AUDIT_WRITE_FAILED
```

**Category**

```text
AUDIT
```

**Severity**

```text
CRITICAL
```

**User Message**

```text
This action could not be completed safely.

An administrator has been notified.
```

**Required Behavior**

For actions requiring atomic audit:

* rollback the business transaction
* do not report success
* create emergency operational signal outside the failed audit channel where possible

**Alert Required**

Immediate.

---

# 125. Audit Event Invalid

**Error ID**

```text
ERROR-AUDIT-002
```

**Canonical Code**

```text
AUDIT_EVENT_INVALID
```

**Severity**

```text
CRITICAL
```

**Trigger**

Audit payload fails required contract validation.

---

# 126. Audit Record Modification Attempted

**Error ID**

```text
ERROR-AUDIT-003
```

**Canonical Code**

```text
AUDIT_RECORD_IMMUTABLE
```

**HTTP Status**

```text
403
```

**User Message**

```text
Audit history cannot be changed.
```

**Audit Required**

A security event must record the attempted modification through an approved immutable path.

---

# PART XXXI — BACKGROUND JOB ERRORS

# 127. Background Job Failed

**Error ID**

```text
ERROR-JOB-001
```

**Canonical Code**

```text
BACKGROUND_JOB_FAILED
```

**Category**

```text
BACKGROUND_JOB
```

**User Message**

```text
A background operation could not be completed.
```

**Operator Message**

Job details, attempt count, safe failure summary, and recovery action.

---

# 128. Job Retry Exhausted

**Error ID**

```text
ERROR-JOB-002
```

**Canonical Code**

```text
JOB_RETRY_EXHAUSTED
```

**Severity**

```text
ERROR
```

**Alert Required**

Yes.

---

# 129. Job Payload Invalid

**Error ID**

```text
ERROR-JOB-003
```

**Canonical Code**

```text
JOB_PAYLOAD_INVALID
```

**Severity**

```text
CRITICAL
```

**Alert Required**

Yes.

---

# 130. Job Lock Lost

**Error ID**

```text
ERROR-JOB-004
```

**Canonical Code**

```text
JOB_LOCK_LOST
```

**User Message**

Normally not user-facing.

**Operator Explanation**

Worker no longer owns the job lease and must stop side effects.

---

# 131. Job Dependency Missing

**Error ID**

```text
ERROR-JOB-005
```

**Canonical Code**

```text
JOB_DEPENDENCY_MISSING
```

**User Message**

```text
This operation is waiting for required earlier work.
```

---

# PART XXXII — REPORTING ERRORS

# 132. Report Generation Failed

```text
REPORT_GENERATION_FAILED
```

**Error ID**

```text
ERROR-REPORT-001
```

**User Message**

```text
This report could not be generated.

Please try again.
```

---

# 133. Report Scope Invalid

```text
REPORT_SCOPE_INVALID
```

**Error ID**

```text
ERROR-REPORT-002
```

**User Message**

```text
Choose a valid report scope.
```

---

# 134. Report Data Incomplete

```text
REPORT_DATA_INCOMPLETE
```

**Error ID**

```text
ERROR-REPORT-003
```

**Severity**

```text
WARNING
```

**User Message**

```text
This report is available, but some data is incomplete.
```

**Rule**

The report must visibly disclose incomplete coverage.

---

# PART XXXIII — EXPORT ERRORS

# 135. Export Not Authorized

```text
EXPORT_NOT_AUTHORIZED
```

**Error ID**

```text
ERROR-EXPORT-001
```

**HTTP Status**

```text
403
```

**User Message**

```text
You do not have permission to export this information.
```

---

# 136. Export Request Invalid

```text
EXPORT_REQUEST_INVALID
```

**Error ID**

```text
ERROR-EXPORT-002
```

**User Message**

```text
Review the export scope before continuing.
```

---

# 137. Export Generation Failed

```text
EXPORT_GENERATION_FAILED
```

**Error ID**

```text
ERROR-EXPORT-003
```

**User Message**

```text
The export could not be generated.
```

---

# 138. Export Expired

```text
EXPORT_EXPIRED
```

**Error ID**

```text
ERROR-EXPORT-004
```

**HTTP Status**

```text
410
```

**User Message**

```text
This export is no longer available.

Create a new export if it is still needed.
```

---

# 139. Export Download Limit Reached

```text
EXPORT_DOWNLOAD_LIMIT_REACHED
```

**Error ID**

```text
ERROR-EXPORT-005
```

**User Message**

```text
This export is no longer available for download.
```

---

# PART XXXIV — CONFIGURATION ERRORS

# 140. Configuration Missing

**Error ID**

```text
ERROR-CONFIG-001
```

**Canonical Code**

```text
CONFIGURATION_MISSING
```

**Category**

```text
CONFIGURATION
```

**Severity**

```text
CRITICAL
```

**User Message**

```text
This feature is not currently available.
```

**Operator Explanation**

Required nonsecret or secret configuration is absent.

**Alert Required**

Yes in staging or production.

---

# 141. Configuration Invalid

```text
CONFIGURATION_INVALID
```

**Error ID**

```text
ERROR-CONFIG-002
```

**Severity**

```text
CRITICAL
```

**Alert Required**

Yes.

---

# 142. Feature Disabled

```text
FEATURE_DISABLED
```

**Error ID**

```text
ERROR-CONFIG-003
```

**Severity**

```text
INFO
```

**HTTP Status**

```text
404
```

or:

```text
403
```

according to disclosure policy.

**User Message**

```text
This feature is not currently available.
```

---

# 143. Unsafe Environment Detected

```text
UNSAFE_ENVIRONMENT_CONFIGURATION
```

**Error ID**

```text
ERROR-CONFIG-004
```

**Severity**

```text
CRITICAL
```

**Trigger Examples**

* production using test credentials
* production storage pointing to development
* canonical integration targeting an unapproved environment
* project path policy violated
* client bundle contains a server secret

**Required Behavior**

Block startup or high-risk operation.

---

# PART XXXV — RATE LIMIT ERRORS

# 144. Rate Limited

**Error ID**

```text
ERROR-RATE-001
```

**Canonical Code**

```text
RATE_LIMITED
```

**Category**

```text
RATE_LIMIT
```

**HTTP Status**

```text
429
```

**User Message**

```text
Too many requests were made in a short period.

Please try again shortly.
```

**Details**

May include retry guidance.

---

# 145. Upload Rate Limited

```text
UPLOAD_RATE_LIMITED
```

**Error ID**

```text
ERROR-RATE-002
```

---

# 146. Authentication Rate Limited

```text
AUTH_RATE_LIMITED
```

**Error ID**

```text
ERROR-RATE-003
```

**Security Rule**

Do not reveal account-existence information.

---

# PART XXXVI — DATABASE ERRORS

# 147. Database Unavailable

**Error ID**

```text
ERROR-DATABASE-001
```

**Canonical Code**

```text
DATABASE_UNAVAILABLE
```

**Category**

```text
DATABASE
```

**Severity**

```text
CRITICAL
```

**HTTP Status**

```text
503
```

**User Message**

```text
The system is temporarily unavailable.

Your unsaved work should remain visible where possible.
```

**Alert Required**

Immediate.

---

# 148. Database Transaction Failed

```text
DATABASE_TRANSACTION_FAILED
```

**Error ID**

```text
ERROR-DATABASE-002
```

**Severity**

```text
ERROR
```

**User Message**

```text
The action could not be completed.

No partial changes were saved.
```

**Work Preserved**

Depends on workflow, but partial transaction changes must not persist.

---

# 149. Database Constraint Violation

```text
DATABASE_CONSTRAINT_VIOLATION
```

**Error ID**

```text
ERROR-DATABASE-003
```

**User Message**

Use a domain-specific safe error when possible.

Generic fallback:

```text
The requested change conflicts with existing information.
```

---

# 150. Database Migration Mismatch

```text
DATABASE_MIGRATION_MISMATCH
```

**Error ID**

```text
ERROR-DATABASE-004
```

**Severity**

```text
CRITICAL
```

**Required Behavior**

Block incompatible application startup or affected feature.

---

# 151. Database Read Replica Stale

```text
DATABASE_READ_STALE
```

**Error ID**

```text
ERROR-DATABASE-005
```

**Severity**

```text
WARNING
```

**User Message**

```text
The latest update is still being synchronized.

Refresh the record before continuing.
```

---

# PART XXXVII — SECURITY ERRORS

# 152. Security Validation Failed

**Error ID**

```text
ERROR-SECURITY-001
```

**Canonical Code**

```text
SECURITY_VALIDATION_FAILED
```

**Category**

```text
SECURITY
```

**Severity**

```text
ERROR
```

**User Message**

```text
This request could not be completed.
```

**Audit Required**

Yes.

---

# 153. CSRF Validation Failed

```text
CSRF_VALIDATION_FAILED
```

**Error ID**

```text
ERROR-SECURITY-002
```

**HTTP Status**

```text
403
```

**User Message**

```text
Your session could not verify this request.

Refresh the page and try again.
```

---

# 154. Malicious Upload Suspected

```text
MALICIOUS_UPLOAD_SUSPECTED
```

**Error ID**

```text
ERROR-SECURITY-003
```

**Severity**

```text
CRITICAL
```

**User Message**

```text
This file could not be accepted.
```

**Audit Required**

Yes.

**Alert Required**

Yes.

---

# 155. Unauthorized Data Access Attempt

```text
UNAUTHORIZED_DATA_ACCESS_ATTEMPT
```

**Error ID**

```text
ERROR-SECURITY-004
```

**Severity**

```text
CRITICAL
```

**User Message**

```text
You do not have permission to access this information.
```

**Audit Required**

Immediate security audit event.

---

# 156. Secret Exposure Detected

```text
SECRET_EXPOSURE_DETECTED
```

**Error ID**

```text
ERROR-SECURITY-005
```

**Severity**

```text
CRITICAL
```

**Required Behavior**

* stop affected operation
* suppress secret from output
* alert operator
* initiate credential-rotation procedure
* preserve forensic evidence safely

---

# 157. Privilege Escalation Attempt

```text
PRIVILEGE_ESCALATION_ATTEMPT
```

**Error ID**

```text
ERROR-SECURITY-006
```

**Severity**

```text
CRITICAL
```

**Audit Required**

Yes.

**Alert Required**

Immediate.

---

# PART XXXVIII — DEPENDENCY ERRORS

# 158. External Dependency Unavailable

**Error ID**

```text
ERROR-DEPENDENCY-001
```

**Canonical Code**

```text
DEPENDENCY_UNAVAILABLE
```

**HTTP Status**

```text
503
```

**User Message**

```text
A required service is temporarily unavailable.
```

---

# 159. External Dependency Timeout

```text
DEPENDENCY_TIMEOUT
```

**Error ID**

```text
ERROR-DEPENDENCY-002
```

**HTTP Status**

```text
504
```

---

# 160. External Dependency Response Invalid

```text
DEPENDENCY_RESPONSE_INVALID
```

**Error ID**

```text
ERROR-DEPENDENCY-003
```

**Severity**

```text
ERROR
```

**Alert Required**

When contract-breaking or repeated.

---

# 161. External Dependency Authentication Failed

```text
DEPENDENCY_AUTHENTICATION_FAILED
```

**Error ID**

```text
ERROR-DEPENDENCY-004
```

**Severity**

```text
CRITICAL
```

**User Message**

```text
A required service connection is unavailable.
```

**Alert Required**

Yes.

---

# PART XXXIX — SYSTEM ERRORS

# 162. System Error

**Error ID**

```text
ERROR-SYSTEM-001
```

**Canonical Code**

```text
SYSTEM_ERROR
```

**Category**

```text
SYSTEM
```

**Severity**

```text
ERROR
```

**HTTP Status**

```text
500
```

**User Message**

```text
Something went wrong.

Your work remains preserved where possible. Use the reference below if you need assistance.
```

**Required Fields**

* correlation ID
* work-preservation status

---

# 163. System Temporarily Unavailable

```text
SYSTEM_UNAVAILABLE
```

**Error ID**

```text
ERROR-SYSTEM-002
```

**HTTP Status**

```text
503
```

**User Message**

```text
The system is temporarily unavailable.

Please try again.
```

---

# 164. Unsupported Operation

```text
OPERATION_UNSUPPORTED
```

**Error ID**

```text
ERROR-SYSTEM-003
```

**HTTP Status**

```text
422
```

**User Message**

```text
This operation is not supported.
```

---

# 165. Contract Version Unsupported

```text
CONTRACT_VERSION_UNSUPPORTED
```

**Error ID**

```text
ERROR-SYSTEM-004
```

**Severity**

```text
ERROR
```

**User Message**

```text
This request uses an unsupported system version.
```

---

# PART XL — ERROR PRESERVATION MATRIX

## 166. Preservation Rules

| Error Family          | Expected Preservation                       |
| --------------------- | ------------------------------------------- |
| Authentication        | Durable drafts preserved                    |
| Authorization         | No mutation occurs                          |
| Validation            | All entered values preserved                |
| Concurrency           | Local unsaved work preserved where possible |
| Claim                 | Durable draft preserved                     |
| Upload                | Successfully stored files preserved         |
| Storage               | Structured records preserved                |
| Transcription         | Draft preserved                             |
| Normalization         | Raw transcription preserved                 |
| Matching              | Entry and prior evaluations preserved       |
| Resolution            | Prior finalized versions preserved          |
| Promotion             | Approved resolution preserved               |
| Canonical integration | Idempotency and attempt history preserved   |
| Audit failure         | Business transaction rolled back            |
| Background job        | Attempt history preserved                   |
| Export                | Source records unaffected                   |
| Database transaction  | No partial committed changes                |
| System error          | Preserve work where technically possible    |

---

# PART XLI — RETRY CLASSIFICATION

## 167. Retry Classes

### `RETRY-NONE`

Do not repeat without changed input, permission, or state.

Examples:

* access denied
* invalid resolution outcome
* final owner protected

### `RETRY-USER`

User may safely retry after correction or refresh.

Examples:

* validation failed
* stale version
* expired access link
* upload failed

### `RETRY-AUTOMATIC`

Background system may retry safely under policy.

Examples:

* dependency unavailable
* promotion service unavailable
* background job transient failure

### `RETRY-OPERATOR`

Administrator review is required before retry.

Examples:

* uncertain canonical result
* missing idempotency record
* provenance failure
* duplicate risk

### `RETRY-FORBIDDEN`

Repeating the operation may cause duplicate or unsafe side effects.

Examples:

* unknown canonical create result without idempotency confirmation
* completed destructive operation
* unresolved audit persistence failure

---

# PART XLII — ALERT CREATION RULES

## 168. Mandatory Alert Errors

The following always create alerts:

```text
IDEMPOTENCY_RESULT_UNAVAILABLE
STORAGE_OBJECT_MISSING
MATCH_ALGORITHM_VERSION_MISSING
PROMOTION_IDEMPOTENCY_MISSING
PROMOTION_CANONICAL_RESULT_MISSING
PROMOTION_PROVENANCE_FAILED
CANONICAL_DUPLICATE_RISK
CANONICAL_CONTRACT_INVALID
AUDIT_WRITE_FAILED
AUDIT_EVENT_INVALID
JOB_PAYLOAD_INVALID
CONFIGURATION_MISSING
CONFIGURATION_INVALID
UNSAFE_ENVIRONMENT_CONFIGURATION
DATABASE_UNAVAILABLE
DATABASE_MIGRATION_MISMATCH
MALICIOUS_UPLOAD_SUSPECTED
SECRET_EXPOSURE_DETECTED
PRIVILEGE_ESCALATION_ATTEMPT
DEPENDENCY_AUTHENTICATION_FAILED
```

---

## 169. Threshold-Based Alerts

The following create alerts after configured recurrence or duration thresholds:

```text
AUTH_PROVIDER_UNAVAILABLE
STORAGE_UNAVAILABLE
UPLOAD_INTEGRITY_FAILED
QUEUE_PROJECTION_STALE
DRAFT_SAVE_FAILED
MATCH_EVALUATION_FAILED
PROMOTION_FAILED
BACKGROUND_JOB_FAILED
REPORT_GENERATION_FAILED
DEPENDENCY_TIMEOUT
SYSTEM_ERROR
```

Threshold values belong to the Configuration Catalog.

---

# PART XLIII — AUDIT REQUIREMENTS

## 170. Errors Requiring Audit Events

Audit is mandatory for:

* authorization denial on high-risk action
* administrative override denial
* session revocation
* idempotency conflict on high-risk operations
* promotion uncertainty
* canonical duplicate risk
* audit write failure
* attempted audit modification
* export denial
* malicious upload suspicion
* unauthorized data access
* secret exposure
* privilege escalation attempt
* unsafe environment detection
* manual retry after failure
* operator dismissal or ignore-with-reason
* final error resolution

The Audit Event Catalog will define exact event names and payloads.

---

# PART XLIV — LOGGING CLASSIFICATION

## 171. Log Levels

### Debug

Development and test diagnostics only.

Must not contain PII or secrets.

### Info

Expected lifecycle events and ordinary business conditions.

### Warn

Recoverable anomalies.

### Error

Failed operation requiring retry or review.

### Critical

Integrity, security, or broad service-impacting failure.

---

## 172. Prohibited Log Content

Never log:

* passwords
* access tokens
* refresh tokens
* session cookies
* secret keys
* full source images
* signed storage URLs
* full handwritten page content
* raw email or phone unless explicitly approved and masked
* database connection strings
* private provider payloads
* full exported datasets

---

# PART XLV — USER MESSAGE STANDARD

## 173. Message Structure

A complete user-facing error may include:

```text
What happened
What was preserved
What to do next
Reference identifier
```

Example:

```text
Your draft could not be saved.

Your entries are still visible on this device. Try again before leaving this page.

Reference: 72F1-A90C
```

---

## 174. Message Tone

Messages should be:

* calm
* direct
* nonblaming
* specific
* brief
* honest

Avoid:

```text
Fatal error
Illegal operation
User error
Unknown exception
Something catastrophic happened
```

unless describing a protected operator-only condition.

---

# PART XLVI — ERROR DISPLAY RULES

## 175. Inline Errors

Use for:

* invalid field
* missing field
* conflicting field condition
* unsupported selection

---

## 176. Banner Errors

Use for:

* save failure
* stale record
* expired claim
* image issue
* retryable promotion failure
* incomplete report

---

## 177. Full-Page Error States

Use for:

* access denied
* record not found
* system unavailable
* maintenance
* unrecoverable session failure

---

## 178. Dialog Errors

Use only where the error directly interrupts a modal or high-risk confirmation flow.

Do not place routine validation inside generic dialogs.

---

# PART XLVII — ERROR DEDUPLICATION

## 179. Deduplication Identity

Processing errors may be grouped by:

```text
error code
subject type
subject ID
operation
dependency
environment
```

Repeated errors should increment occurrence count rather than create uncontrolled duplicates when the business condition is identical.

---

## 180. Non-Deduplicable Errors

The following require separate records:

* security access attempts
* audit write failures
* destructive action failures
* promotion attempts
* canonical create uncertainty
* export downloads
* user-access changes

---

# PART XLVIII — RECOVERY ACTION CATALOG

## 181. Standard Recovery Actions

```text
SIGN_IN
REFRESH_RECORD
RETRY_OPERATION
RELOAD_LATEST
RECOVER_DRAFT
CLAIM_ANOTHER
REQUEST_NEW_INVITATION
UPLOAD_REPLACEMENT
RETURN_FOR_CORRECTION
REVIEW_MATCH_CONFLICT
REVIEW_CANONICAL_RESULT
CONTACT_ADMINISTRATOR
ACKNOWLEDGE_ERROR
RETRY_JOB
ESCALATE
NO_ACTION_REQUIRED
```

Each error must map to one or more recovery actions.

---

# PART XLIX — ERROR-TO-STATE ALIGNMENT

## 182. State Transition Outcomes

Errors may produce one of these state effects:

```text
NO_STATE_CHANGE
ROLLBACK_TRANSACTION
MOVE_TO_EXCEPTION
MOVE_TO_RETRYABLE_FAILURE
MOVE_TO_FINAL_FAILURE
MOVE_TO_REQUIRES_REVIEW
RETURN_TO_AVAILABLE
PRESERVE_CURRENT_STATE
```

Examples:

```text
CLAIM_ALREADY_HELD
→ NO_STATE_CHANGE
```

```text
PROMOTION_FAILED
→ MOVE_TO_RETRYABLE_FAILURE or MOVE_TO_FINAL_FAILURE
```

```text
AUDIT_WRITE_FAILED
→ ROLLBACK_TRANSACTION
```

```text
STORAGE_OBJECT_MISSING
→ MOVE_TO_EXCEPTION
```

---

# PART L — REQUIRED ERROR TESTS

## 183. Test Requirements Per Error

Every cataloged error must be tested for:

1. triggering condition
2. canonical code
3. HTTP status
4. user-safe message
5. retryable value
6. work-preserved value
7. no secret leakage
8. correlation ID
9. state effect
10. transaction rollback where required
11. audit event where required
12. alert creation where required
13. deduplication behavior
14. authorization behavior
15. responsive UI presentation where user-facing
16. screen-reader announcement where applicable

---

# PART LI — ERROR REGISTRY

## 184. Canonical Error Families

### Authentication

```text
AUTH_REQUIRED
AUTH_CREDENTIALS_INVALID
AUTH_PROVIDER_UNAVAILABLE
ACCESS_INVITATION_INVALID
ACCESS_INVITATION_EXPIRED
```

### Session

```text
SESSION_EXPIRED
SESSION_REVOKED
SESSION_REFRESH_FAILED
```

### Authorization

```text
ACCESS_DENIED
ROLE_REQUIRED
RESOURCE_SCOPE_DENIED
ADMIN_OVERRIDE_NOT_ALLOWED
FINAL_OWNER_PROTECTED
```

### Validation

```text
VALIDATION_FAILED
REQUIRED_FIELD_MISSING
FIELD_FORMAT_INVALID
ENUM_VALUE_INVALID
FILTER_UNSUPPORTED
SORT_FIELD_UNSUPPORTED
DATE_RANGE_INVALID
FIELD_CONDITION_CONFLICT
SUBMISSION_EMPTY
ROW_POSITION_DUPLICATE
```

### Not Found

```text
NOT_FOUND
BATCH_NOT_FOUND
PAGE_NOT_FOUND
ENTRY_NOT_FOUND
USER_NOT_FOUND
PROMOTION_NOT_FOUND
```

### Concurrency

```text
STALE_VERSION
STATE_TRANSITION_CONFLICT
OPERATION_ALREADY_RUNNING
```

### Idempotency

```text
IDEMPOTENCY_CONFLICT
IDEMPOTENCY_OPERATION_IN_PROGRESS
IDEMPOTENCY_RESULT_UNAVAILABLE
```

### Batch

```text
BATCH_STATE_INVALID
BATCH_UPLOADS_CLOSED
BATCH_COMPLETION_BLOCKED
BATCH_ALREADY_ARCHIVED
```

### Page

```text
PAGE_STATE_INVALID
PAGE_IMAGE_NOT_USABLE
PAGE_ALREADY_SUBMITTED
PAGE_SEQUENCE_CONFLICT
```

### Upload

```text
UPLOAD_SESSION_INVALID
UPLOAD_SESSION_EXPIRED
UPLOAD_FILE_TOO_LARGE
UPLOAD_TYPE_UNSUPPORTED
UPLOAD_FILE_CORRUPT
UPLOAD_INTEGRITY_FAILED
UPLOAD_DUPLICATE_SUSPECTED
UPLOAD_COMPLETION_FAILED
```

### Storage

```text
STORAGE_UNAVAILABLE
STORAGE_OBJECT_MISSING
STORAGE_VERIFICATION_FAILED
STORAGE_ACCESS_DENIED
STORAGE_ACCESS_EXPIRED
```

### Image

```text
IMAGE_REPLACEMENT_REQUIRED
IMAGE_VERSION_CONFLICT
IMAGE_DISPLAY_TRANSFORM_FAILED
```

### Queue

```text
QUEUE_EMPTY
QUEUE_ITEM_NOT_ELIGIBLE
QUEUE_PROJECTION_STALE
```

### Claim

```text
CLAIM_ALREADY_HELD
CLAIM_NOT_OWNED
CLAIM_EXPIRED
CLAIM_RENEWAL_DENIED
CLAIM_RELEASE_FAILED
ACTIVE_CLAIM_REQUIRED
```

### Draft

```text
DRAFT_SAVE_FAILED
DRAFT_NOT_FOUND
DRAFT_RECOVERY_DENIED
DRAFT_ALREADY_SUBMITTED
DRAFT_REVISION_CONFLICT
```

### Transcription

```text
TRANSCRIPTION_SUBMISSION_FAILED
TRANSCRIPTION_STRUCTURE_INVALID
TRANSCRIPTION_REVISION_SUPERSEDED
CORRECTION_REQUEST_INVALID
CORRECTION_ALREADY_RESOLVED
```

### Normalization

```text
NORMALIZATION_FAILED
NORMALIZATION_VERSION_UNSUPPORTED
NORMALIZED_VALUE_CONFLICT
```

### Matching

```text
MATCH_EVALUATION_FAILED
MATCH_CANDIDATES_UNAVAILABLE
MATCH_CONFLICT
MATCH_EVALUATION_SUPERSEDED
MATCH_ALGORITHM_VERSION_MISSING
MATCH_EXPLANATION_MISSING
```

### Resolution

```text
RESOLUTION_OUTCOME_INVALID
RESOLUTION_CANDIDATE_REQUIRED
RESOLUTION_REASON_REQUIRED
RESOLUTION_CONFLICT_NOT_ACKNOWLEDGED
RESOLUTION_ALREADY_FINALIZED
RESOLUTION_REOPEN_NOT_ALLOWED
DUPLICATE_ENTRY_TARGET_REQUIRED
```

### Promotion

```text
PROMOTION_FAILED
PROMOTION_RETRY_NOT_ALLOWED
PROMOTION_ALREADY_RUNNING
PROMOTION_ALREADY_SUCCEEDED
PROMOTION_IDEMPOTENCY_MISSING
PROMOTION_CANONICAL_RESULT_MISSING
PROMOTION_PROVENANCE_FAILED
```

### Canonical Integration

```text
CANONICAL_SERVICE_UNAVAILABLE
CANONICAL_SERVICE_TIMEOUT
CANONICAL_PERSON_NOT_FOUND
CANONICAL_DUPLICATE_RISK
CANONICAL_CONTRACT_INVALID
CANONICAL_ATTRIBUTE_CONFLICT
```

### User Management

```text
USER_ALREADY_EXISTS
USER_STATE_INVALID
ROLE_ALREADY_ASSIGNED
ROLE_NOT_ASSIGNED
USER_CHANGE_BLOCKED_BY_ACTIVE_WORK
```

### Audit

```text
AUDIT_WRITE_FAILED
AUDIT_EVENT_INVALID
AUDIT_RECORD_IMMUTABLE
```

### Jobs

```text
BACKGROUND_JOB_FAILED
JOB_RETRY_EXHAUSTED
JOB_PAYLOAD_INVALID
JOB_LOCK_LOST
JOB_DEPENDENCY_MISSING
```

### Reporting

```text
REPORT_GENERATION_FAILED
REPORT_SCOPE_INVALID
REPORT_DATA_INCOMPLETE
```

### Export

```text
EXPORT_NOT_AUTHORIZED
EXPORT_REQUEST_INVALID
EXPORT_GENERATION_FAILED
EXPORT_EXPIRED
EXPORT_DOWNLOAD_LIMIT_REACHED
```

### Configuration

```text
CONFIGURATION_MISSING
CONFIGURATION_INVALID
FEATURE_DISABLED
UNSAFE_ENVIRONMENT_CONFIGURATION
```

### Rate Limit

```text
RATE_LIMITED
UPLOAD_RATE_LIMITED
AUTH_RATE_LIMITED
```

### Database

```text
DATABASE_UNAVAILABLE
DATABASE_TRANSACTION_FAILED
DATABASE_CONSTRAINT_VIOLATION
DATABASE_MIGRATION_MISMATCH
DATABASE_READ_STALE
```

### Security

```text
SECURITY_VALIDATION_FAILED
CSRF_VALIDATION_FAILED
MALICIOUS_UPLOAD_SUSPECTED
UNAUTHORIZED_DATA_ACCESS_ATTEMPT
SECRET_EXPOSURE_DETECTED
PRIVILEGE_ESCALATION_ATTEMPT
```

### Dependency

```text
DEPENDENCY_UNAVAILABLE
DEPENDENCY_TIMEOUT
DEPENDENCY_RESPONSE_INVALID
DEPENDENCY_AUTHENTICATION_FAILED
```

### System

```text
SYSTEM_ERROR
SYSTEM_UNAVAILABLE
OPERATION_UNSUPPORTED
CONTRACT_VERSION_UNSUPPORTED
```

---

# PART LII — LOCKED ERROR DECISIONS

## 185. Locked Decisions

1. Production errors use cataloged stable codes.
2. User messages never expose secrets or stack traces.
3. Every significant error includes a correlation ID.
4. Validation errors preserve user input.
5. Claim expiration preserves drafts.
6. Draft save failure must not clear visible entries.
7. Normalization failure never changes raw transcription.
8. Match failure preserves prior evaluations.
9. Resolution failure preserves finalized history.
10. Promotion failure preserves the approved resolution.
11. Canonical uncertainty blocks unsafe retry.
12. Idempotency-result uncertainty requires operator review.
13. Audit failure rolls back any action requiring atomic audit.
14. Acknowledging an error does not resolve it.
15. A read notification does not resolve an error.
16. Retry guidance appears only when retry is safe.
17. Technical failures remain distinct from valid business conditions.
18. Queue empty is not treated as a system failure.
19. Claim collision is not treated as a system failure.
20. Unknown data is never converted to No because of an error.
21. Personal information is minimized in logs.
22. Source images are never logged.
23. Alerts are created according to catalog policy.
24. Critical integrity errors cannot be shown as success.
25. Error handling must be tested.
26. The UI must tell users whether their work was preserved.
27. Unsupported machine values are rejected.
28. Repeated errors follow deduplication policy.
29. Security errors always use safe, minimal user messages.
30. No undocumented production error code is allowed.

---

# PART LIII — DEFERRED ERROR DECISIONS

## 186. Open Decisions

### `ERROR-DEC-001`

Exact retry delay schedule.

### `ERROR-DEC-002`

Exact threshold for repeated error alerts.

### `ERROR-DEC-003`

Exact correlation-ID display format.

### `ERROR-DEC-004`

Whether HTTP 423 is used consistently for claim locks.

### `ERROR-DEC-005`

Whether empty queue endpoints return 200 with an empty collection or a specialized no-work result.

### `ERROR-DEC-006`

Exact local unsaved-work persistence method.

### `ERROR-DEC-007`

Exact operator escalation levels.

### `ERROR-DEC-008`

Exact error-deduplication time window.

### `ERROR-DEC-009`

Exact support workflow associated with reference IDs.

### `ERROR-DEC-010`

Exact treatment of external dependency partial success.

### `ERROR-DEC-011`

Exact user wording after production usability testing.

### `ERROR-DEC-012`

Exact error retention duration.

These decisions will be resolved through the Configuration, Notification, Background Job, Retention, and Traceability catalogs.

---

# PART LIV — ERROR CATALOG READINESS

## 187. Readiness Score

| Area                    | Readiness |
| ----------------------- | --------: |
| Error doctrine          |      100% |
| Response contract       |      100% |
| Categories              |      100% |
| Severity model          |      100% |
| HTTP mapping            |       99% |
| Authentication errors   |      100% |
| Authorization errors    |      100% |
| Validation errors       |      100% |
| Concurrency errors      |      100% |
| Idempotency errors      |      100% |
| Upload and storage      |      100% |
| Queue and claims        |      100% |
| Draft and transcription |      100% |
| Normalization           |      100% |
| Matching                |      100% |
| Resolution              |      100% |
| Promotion               |      100% |
| Canonical integration   |      100% |
| User management         |      100% |
| Audit failures          |      100% |
| Jobs                    |      100% |
| Reporting and export    |       99% |
| Configuration           |      100% |
| Database                |      100% |
| Security                |      100% |
| System errors           |      100% |
| Preservation rules      |      100% |
| Retry rules             |       99% |
| Alert rules             |       98% |
| Test requirements       |      100% |

**Overall Catalog 2 Readiness**

```text
99%
```

The remaining percentage is reserved for reconciliation with:

* Audit Event Catalog
* Configuration Catalog
* Permission Catalog
* Notification Catalog
* Background Job Catalog
* Data Retention Catalog
* Cross-Volume Traceability Matrix

---

# PART LV — NEXT CATALOG BUILD

## 188. Next Catalog

The next governing catalog is:

```text
PEOPLE-CATALOG-03-AUDIT-EVENTS-1.0
```

It will define:

* canonical event names
* event versions
* actors
* subjects
* objects
* results
* reason codes
* required payloads
* privacy restrictions
* correlation rules
* transaction boundaries
* retention classification
* which events are mandatory
* which failures require security events
* exact traceability to states, APIs, permissions, and errors

The catalog library now has complete lifecycle and error foundations. The next piece is the **Audit Event Catalog**, which will define the immutable event language connecting every sensitive action, state transition, retry, denial, and failure.
