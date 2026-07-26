# PEOPLE INTAKE SYSTEM

# CATALOG 1 — STATE MACHINE CATALOG

**Document ID**

```text
PEOPLE-CATALOG-01-STATE-MACHINES-1.0
```

**Document Set**

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

**Build Mode**

```text
DOCUMENTATION ONLY
```

**Prohibited During This Catalog Build**

* No application source code
* No API handlers or route implementations
* No database migrations or ORM models
* No React, JSX, TSX, or CSS implementation
* No undocumented production state keys or transitions

---

# PART I — STATE MACHINE STANDARD

## 9. Purpose

The State Machine Catalog defines every controlled lifecycle in the People Intake System.

A state machine determines:

* where a record begins
* where it may move
* who may move it
* what must be true
* what side effects occur
* what cannot happen
* whether a state is terminal
* how recovery occurs

---

## 10. Universal Transition Rules

Every transition must:

1. start from the current persisted state
2. validate authorization
3. validate transition eligibility
4. validate expected record version
5. execute required database changes atomically
6. create required history
7. create required audit events
8. enqueue required background work
9. return the resulting state
10. reject stale or prohibited transitions

---

## 11. State Categories

States may be:

### Initial

The first valid state.

### Active

Work is permitted or ongoing.

### Waiting

The record awaits another person, system, or condition.

### Blocked

Progress cannot continue without intervention.

### Successful Terminal

The lifecycle completed successfully.

### Unsuccessful Terminal

The lifecycle ended without the intended successful result.

### Archived

The record is inactive but preserved.

---

## 12. Universal Prohibitions

No state machine may:

* erase state history
* silently skip required review
* treat unknown as negative
* overwrite source evidence
* use UI visibility as authorization
* complete before required side effects are durable
* create duplicate canonical people on retry
* move archived records into active work without an explicit restoration transition
* reinterpret failed work as successful

---

# PART II — USER ACCESS STATE MACHINE

# 13. Application User Lifecycle

**Machine ID**

```text
STATE-USER-001
```

## States

```text
INVITED
ACTIVE
SUSPENDED
DISABLED
REVOKED
```

## Initial State

```text
INVITED
```

## Terminal State

```text
REVOKED
```

`DISABLED` is inactive but may be recoverable under policy.

## Allowed Transitions

| From      | To        | Actor                                             |
| --------- | --------- | ------------------------------------------------- |
| None      | INVITED   | Owner or authorized Administrator                 |
| INVITED   | ACTIVE    | Owner, Administrator, or approved activation flow |
| INVITED   | REVOKED   | Owner or Administrator                            |
| ACTIVE    | SUSPENDED | Owner or Administrator                            |
| ACTIVE    | DISABLED  | Owner or Administrator                            |
| ACTIVE    | REVOKED   | Owner or Administrator                            |
| SUSPENDED | ACTIVE    | Owner or Administrator                            |
| SUSPENDED | DISABLED  | Owner or Administrator                            |
| SUSPENDED | REVOKED   | Owner or Administrator                            |
| DISABLED  | ACTIVE    | Owner or authorized Administrator                 |
| DISABLED  | REVOKED   | Owner or Administrator                            |

## Guards

### Activate

Requires:

* approved identity
* accepted access invitation where applicable
* at least one authorized role
* no unresolved security prohibition

### Suspend

Requires:

* reason
* actor authorization
* active claims handled according to policy

### Revoke

Requires:

* explicit confirmation
* reason
* protection against removing the last required Owner
* active sessions invalidated
* role grants ended

## Side Effects

### On Suspension

* block new sessions
* block protected operations
* release or expire claims according to policy
* preserve drafts
* create audit event

### On Revocation

* revoke active roles
* invalidate sessions
* preserve all prior attribution
* prevent automatic reactivation
* create audit event

## Prohibited Transitions

```text
REVOKED → ACTIVE
REVOKED → SUSPENDED
REVOKED → DISABLED
```

A revoked identity requires a new governed user record or formal restoration policy not currently authorized.

---

# PART III — USER ROLE STATE MACHINE

# 14. Role Grant Lifecycle

**Machine ID**

```text
STATE-ROLE-001
```

## States

```text
ACTIVE
EXPIRED
REVOKED
```

## Initial State

```text
ACTIVE
```

## Terminal States

```text
EXPIRED
REVOKED
```

## Transitions

| From   | To      | Actor                             |
| ------ | ------- | --------------------------------- |
| None   | ACTIVE  | Owner or authorized Administrator |
| ACTIVE | EXPIRED | System Actor                      |
| ACTIVE | REVOKED | Owner or authorized Administrator |

## Guards

* user must exist
* role key must be cataloged
* granting actor must have grant authority
* duplicate active role prohibited
* expiration must be future-dated
* final Owner protection must be enforced

---

# PART IV — BATCH STATE MACHINE

# 15. Intake Batch Lifecycle

**Machine ID**

```text
STATE-BATCH-001
```

## States

```text
DRAFT
OPEN
PROCESSING
READY_FOR_COMPLETION
COMPLETED
EXCEPTION
ARCHIVED
```

## Initial State

```text
DRAFT
```

## Terminal State

```text
ARCHIVED
```

## State Meanings

### DRAFT

Batch exists but is not yet open for ordinary uploads.

### OPEN

Pages may be uploaded and prepared.

### PROCESSING

One or more pages are moving through transcription, review, matching, or promotion.

### READY_FOR_COMPLETION

All required pages and entries have reached completion criteria.

### COMPLETED

Batch processing is complete.

### EXCEPTION

Batch cannot progress because of an unresolved operational condition.

### ARCHIVED

Batch is inactive and historically preserved.

## Allowed Transitions

| From                 | To                   |
| -------------------- | -------------------- |
| DRAFT                | OPEN                 |
| DRAFT                | ARCHIVED             |
| OPEN                 | PROCESSING           |
| OPEN                 | READY_FOR_COMPLETION |
| OPEN                 | EXCEPTION            |
| OPEN                 | ARCHIVED             |
| PROCESSING           | READY_FOR_COMPLETION |
| PROCESSING           | EXCEPTION            |
| EXCEPTION            | OPEN                 |
| EXCEPTION            | PROCESSING           |
| EXCEPTION            | READY_FOR_COMPLETION |
| READY_FOR_COMPLETION | PROCESSING           |
| READY_FOR_COMPLETION | COMPLETED            |
| READY_FOR_COMPLETION | EXCEPTION            |
| COMPLETED            | ARCHIVED             |

## Completion Guards

To enter `READY_FOR_COMPLETION`:

* uploads are closed
* every retained page has a usable active image or an approved terminal disposition
* no page remains in active transcription
* no required entry remains unresolved
* no required promotion remains pending or retryable
* no blocking error remains open

To enter `COMPLETED`:

* completion summary validated
* no active claims
* no active drafts requiring action
* required reports or completion checks generated
* completion audit event recorded

## Prohibited Transitions

```text
ARCHIVED → OPEN
ARCHIVED → PROCESSING
COMPLETED → OPEN
```

Restoration requires a future formal restoration state and is not authorized in Version 1.

---

# PART V — PAGE STATE MACHINE

# 16. Intake Page Lifecycle

**Machine ID**

```text
STATE-PAGE-001
```

## States

```text
UPLOADING
VERIFYING
NEEDS_IMAGE_REVIEW
REPLACEMENT_REQUIRED
READY_FOR_TRANSCRIPTION
CLAIMED_FOR_TRANSCRIPTION
TRANSCRIPTION_IN_PROGRESS
SUBMITTED
TRANSCRIPTION_REVIEW
RETURNED_FOR_CORRECTION
READY_FOR_MATCHING
MATCHING_IN_PROGRESS
MATCH_REVIEW
RESOLVED
COMPLETED
EXCEPTION
ARCHIVED
```

## Initial State

```text
UPLOADING
```

## Successful Terminal States

```text
COMPLETED
ARCHIVED
```

## Core Transitions

| From                      | To                          |
| ------------------------- | --------------------------- |
| UPLOADING                 | VERIFYING                   |
| UPLOADING                 | EXCEPTION                   |
| VERIFYING                 | NEEDS_IMAGE_REVIEW          |
| VERIFYING                 | EXCEPTION                   |
| NEEDS_IMAGE_REVIEW        | READY_FOR_TRANSCRIPTION     |
| NEEDS_IMAGE_REVIEW        | REPLACEMENT_REQUIRED        |
| REPLACEMENT_REQUIRED      | VERIFYING                   |
| READY_FOR_TRANSCRIPTION   | CLAIMED_FOR_TRANSCRIPTION   |
| CLAIMED_FOR_TRANSCRIPTION | TRANSCRIPTION_IN_PROGRESS   |
| CLAIMED_FOR_TRANSCRIPTION | READY_FOR_TRANSCRIPTION     |
| TRANSCRIPTION_IN_PROGRESS | SUBMITTED                   |
| TRANSCRIPTION_IN_PROGRESS | READY_FOR_TRANSCRIPTION     |
| SUBMITTED                 | TRANSCRIPTION_REVIEW        |
| TRANSCRIPTION_REVIEW      | READY_FOR_MATCHING          |
| TRANSCRIPTION_REVIEW      | RETURNED_FOR_CORRECTION     |
| RETURNED_FOR_CORRECTION   | CLAIMED_FOR_TRANSCRIPTION   |
| READY_FOR_MATCHING        | MATCHING_IN_PROGRESS        |
| MATCHING_IN_PROGRESS      | MATCH_REVIEW                |
| MATCHING_IN_PROGRESS      | EXCEPTION                   |
| MATCH_REVIEW              | RESOLVED                    |
| MATCH_REVIEW              | EXCEPTION                   |
| RESOLVED                  | COMPLETED                   |
| EXCEPTION                 | approved prior active state |
| COMPLETED                 | ARCHIVED                    |

## Guards

### Ready for Transcription

Requires:

* verified active source image
* usable image-quality state
* batch permits transcription
* no duplicate active page workflow

### Submitted

Requires:

* durable saved draft
* valid submission revision
* zero structural validation errors
* claim ownership or approved recovery authority
* submission idempotency record
* claim completion

### Ready for Matching

Requires:

* transcription review approved
* current submission revision
* normalization complete or approved exception

### Resolved

Requires:

* every active entry has an effective resolution
* no blocking entry conflict
* review authorization

### Completed

Requires:

* every required entry promotion succeeded or has an approved no-change terminal outcome
* no retryable promotion remains
* no blocking operational error

---

# PART VI — PAGE IMAGE QUALITY STATE MACHINE

# 17. Image Quality Lifecycle

**Machine ID**

```text
STATE-IMAGE-QUALITY-001
```

## States

```text
PENDING_REVIEW
USABLE
BLURRY
CROPPED
WRONG_DOCUMENT
CORRUPT
REPLACEMENT_REQUIRED
SUPERSEDED
```

## Initial State

```text
PENDING_REVIEW
```

## Transitions

| From                 | To                   |
| -------------------- | -------------------- |
| PENDING_REVIEW       | USABLE               |
| PENDING_REVIEW       | BLURRY               |
| PENDING_REVIEW       | CROPPED              |
| PENDING_REVIEW       | WRONG_DOCUMENT       |
| PENDING_REVIEW       | CORRUPT              |
| BLURRY               | REPLACEMENT_REQUIRED |
| CROPPED              | REPLACEMENT_REQUIRED |
| WRONG_DOCUMENT       | REPLACEMENT_REQUIRED |
| CORRUPT              | REPLACEMENT_REQUIRED |
| USABLE               | SUPERSEDED           |
| REPLACEMENT_REQUIRED | SUPERSEDED           |

A replacement image begins a new quality lifecycle at `PENDING_REVIEW`.

## Rule

A page may enter transcription only when its active image is `USABLE`.

---

# PART VII — STORAGE OBJECT STATE MACHINE

# 18. Storage Object Lifecycle

**Machine ID**

```text
STATE-STORAGE-001
```

## States

```text
PENDING
UPLOADING
STORED
VERIFIED
QUARANTINED
MISSING
FAILED
DELETION_PENDING
DELETED
```

## Initial State

```text
PENDING
```

## Transitions

| From             | To               |
| ---------------- | ---------------- |
| PENDING          | UPLOADING        |
| PENDING          | FAILED           |
| UPLOADING        | STORED           |
| UPLOADING        | FAILED           |
| STORED           | VERIFIED         |
| STORED           | QUARANTINED      |
| STORED           | MISSING          |
| VERIFIED         | QUARANTINED      |
| VERIFIED         | MISSING          |
| QUARANTINED      | VERIFIED         |
| QUARANTINED      | DELETION_PENDING |
| MISSING          | VERIFIED         |
| MISSING          | FAILED           |
| FAILED           | PENDING          |
| VERIFIED         | DELETION_PENDING |
| DELETION_PENDING | DELETED          |
| DELETION_PENDING | VERIFIED         |

## Terminal State

```text
DELETED
```

Deletion requires approved retention policy.

Ordinary image replacement never deletes the prior storage object.

---

# PART VIII — UPLOAD SESSION STATE MACHINE

# 19. Upload Lifecycle

**Machine ID**

```text
STATE-UPLOAD-001
```

## States

```text
CREATED
READY
UPLOADING
VERIFYING
COMPLETED
FAILED_RETRYABLE
FAILED_FINAL
EXPIRED
CANCELLED
```

## Initial State

```text
CREATED
```

## Transitions

| From             | To               |
| ---------------- | ---------------- |
| CREATED          | READY            |
| CREATED          | CANCELLED        |
| READY            | UPLOADING        |
| READY            | EXPIRED          |
| READY            | CANCELLED        |
| UPLOADING        | VERIFYING        |
| UPLOADING        | FAILED_RETRYABLE |
| UPLOADING        | FAILED_FINAL     |
| VERIFYING        | COMPLETED        |
| VERIFYING        | FAILED_RETRYABLE |
| VERIFYING        | FAILED_FINAL     |
| FAILED_RETRYABLE | READY            |
| FAILED_RETRYABLE | CANCELLED        |

## Terminal States

```text
COMPLETED
FAILED_FINAL
EXPIRED
CANCELLED
```

## Completion Guards

* object stored
* integrity hash verified
* content type accepted
* size accepted
* upload session idempotency validated
* intended page relationship valid

---

# PART IX — QUEUE ITEM STATE MACHINE

# 20. Queue Item Lifecycle

**Machine ID**

```text
STATE-QUEUE-001
```

## States

```text
PENDING
AVAILABLE
CLAIMED
BLOCKED
COMPLETED
REMOVED
CANCELLED
```

## Initial State

```text
PENDING
```

## Transitions

| From            | To        |
| --------------- | --------- |
| PENDING         | AVAILABLE |
| PENDING         | BLOCKED   |
| AVAILABLE       | CLAIMED   |
| AVAILABLE       | BLOCKED   |
| AVAILABLE       | REMOVED   |
| CLAIMED         | AVAILABLE |
| CLAIMED         | COMPLETED |
| CLAIMED         | BLOCKED   |
| BLOCKED         | AVAILABLE |
| BLOCKED         | REMOVED   |
| COMPLETED       | REMOVED   |
| any nonterminal | CANCELLED |

## Rules

Queue items are projections of workflow eligibility.

If the underlying subject is no longer eligible, the queue item must move to:

```text
REMOVED
```

or:

```text
CANCELLED
```

It must not remain claimable.

---

# PART X — CLAIM STATE MACHINE

# 21. Work Claim Lifecycle

**Machine ID**

```text
STATE-CLAIM-001
```

## States

```text
ACTIVE
EXPIRING
EXPIRED
RELEASED
COMPLETED
CANCELLED
```

## Initial State

```text
ACTIVE
```

## Transitions

| From     | To        |
| -------- | --------- |
| ACTIVE   | EXPIRING  |
| ACTIVE   | RELEASED  |
| ACTIVE   | COMPLETED |
| ACTIVE   | CANCELLED |
| EXPIRING | ACTIVE    |
| EXPIRING | EXPIRED   |
| EXPIRING | RELEASED  |
| EXPIRING | COMPLETED |

## Terminal States

```text
EXPIRED
RELEASED
COMPLETED
CANCELLED
```

## Guards

### Renew

* claim belongs to current user or authorized administrator
* claim has not expired
* subject remains eligible
* no replacement claim exists

### Complete

* associated workflow transaction succeeded
* draft or resolution is durable
* required audit event is durable

## Side Effects

### Expiration

* queue item may return to available
* saved draft remains
* claimant attribution remains
* claim-history event created

### Release

* reason required for administrative release
* unsaved-work warning handled in UI
* durable draft preserved

---

# PART XI — PAGE DRAFT STATE MACHINE

# 22. Draft Lifecycle

**Machine ID**

```text
STATE-DRAFT-001
```

## States

```text
ACTIVE
RECOVERABLE
RECOVERED
SUBMITTED
SUPERSEDED
ABANDONED
```

## Initial State

```text
ACTIVE
```

## Transitions

| From        | To          |
| ----------- | ----------- |
| ACTIVE      | RECOVERABLE |
| ACTIVE      | SUBMITTED   |
| ACTIVE      | ABANDONED   |
| RECOVERABLE | RECOVERED   |
| RECOVERABLE | SUPERSEDED  |
| RECOVERABLE | ABANDONED   |
| RECOVERED   | ACTIVE      |
| RECOVERED   | SUBMITTED   |
| SUBMITTED   | SUPERSEDED  |

## Rules

* claim expiration may move active draft to recoverable
* draft recovery never changes prior revision attribution
* submission preserves all draft revisions
* submitted drafts are not edited directly

---

# PART XII — ENTRY STATE MACHINE

# 23. Intake Entry Lifecycle

**Machine ID**

```text
STATE-ENTRY-001
```

## States

```text
DRAFT
SUBMITTED
TRANSCRIPTION_REVIEW
RETURNED_FOR_CORRECTION
APPROVED_FOR_MATCHING
NORMALIZING
READY_FOR_MATCHING
MATCHING
MATCH_REVIEW
REQUIRES_MORE_INFORMATION
CONFLICT_ESCALATED
RESOLVED_MATCH_EXISTING
RESOLVED_CREATE_NEW
RESOLVED_REJECTED
RESOLVED_DUPLICATE
PROMOTION_PENDING
PROMOTION_IN_PROGRESS
PROMOTION_RETRY_NEEDED
PROMOTION_REVIEW_REQUIRED
COMPLETED
ARCHIVED
```

## Initial State

```text
DRAFT
```

## Terminal Operational States

```text
COMPLETED
ARCHIVED
RESOLVED_REJECTED
RESOLVED_DUPLICATE
```

`RESOLVED_REJECTED` and `RESOLVED_DUPLICATE` may lead to `COMPLETED` through a no-canonical-change promotion or finalization operation.

## Main Transitions

```text
DRAFT
→ SUBMITTED
→ TRANSCRIPTION_REVIEW
→ APPROVED_FOR_MATCHING
→ NORMALIZING
→ READY_FOR_MATCHING
→ MATCHING
→ MATCH_REVIEW
```

Possible review outcomes:

```text
MATCH_REVIEW → RESOLVED_MATCH_EXISTING
MATCH_REVIEW → RESOLVED_CREATE_NEW
MATCH_REVIEW → REQUIRES_MORE_INFORMATION
MATCH_REVIEW → CONFLICT_ESCALATED
MATCH_REVIEW → RESOLVED_REJECTED
MATCH_REVIEW → RESOLVED_DUPLICATE
```

Promotion path:

```text
RESOLVED_MATCH_EXISTING
→ PROMOTION_PENDING
→ PROMOTION_IN_PROGRESS
→ COMPLETED
```

```text
RESOLVED_CREATE_NEW
→ PROMOTION_PENDING
→ PROMOTION_IN_PROGRESS
→ COMPLETED
```

Failure paths:

```text
PROMOTION_IN_PROGRESS → PROMOTION_RETRY_NEEDED
PROMOTION_IN_PROGRESS → PROMOTION_REVIEW_REQUIRED
PROMOTION_RETRY_NEEDED → PROMOTION_IN_PROGRESS
PROMOTION_REVIEW_REQUIRED → PROMOTION_PENDING
```

Correction path:

```text
TRANSCRIPTION_REVIEW
→ RETURNED_FOR_CORRECTION
→ DRAFT
→ SUBMITTED
```

## Rules

* every submitted revision is immutable
* return for correction creates a new revision
* matching always targets the current approved submission revision
* prior evaluations remain preserved
* prior resolutions remain preserved
* one effective resolution exists at a time
* canonical completion requires provenance

---

# PART XIII — NORMALIZATION STATE MACHINE

# 24. Normalization Run Lifecycle

**Machine ID**

```text
STATE-NORMALIZATION-001
```

## States

```text
PENDING
RUNNING
COMPLETED
COMPLETED_WITH_WARNINGS
FAILED_RETRYABLE
FAILED_FINAL
CANCELLED
SUPERSEDED
```

## Transitions

| From                | To                      |
| ------------------- | ----------------------- |
| PENDING             | RUNNING                 |
| PENDING             | CANCELLED               |
| RUNNING             | COMPLETED               |
| RUNNING             | COMPLETED_WITH_WARNINGS |
| RUNNING             | FAILED_RETRYABLE        |
| RUNNING             | FAILED_FINAL            |
| FAILED_RETRYABLE    | PENDING                 |
| any completed state | SUPERSEDED              |

## Rule

Normalization failure must never alter raw transcription.

---

# PART XIV — MATCH EVALUATION STATE MACHINE

# 25. Match Evaluation Lifecycle

**Machine ID**

```text
STATE-MATCH-EVAL-001
```

## States

```text
PENDING
RUNNING
COMPLETED
COMPLETED_WITH_WARNINGS
FAILED_RETRYABLE
FAILED_FINAL
CANCELLED
SUPERSEDED
```

## Transitions

| From                    | To                      |
| ----------------------- | ----------------------- |
| PENDING                 | RUNNING                 |
| PENDING                 | CANCELLED               |
| RUNNING                 | COMPLETED               |
| RUNNING                 | COMPLETED_WITH_WARNINGS |
| RUNNING                 | FAILED_RETRYABLE        |
| RUNNING                 | FAILED_FINAL            |
| FAILED_RETRYABLE        | PENDING                 |
| COMPLETED               | SUPERSEDED              |
| COMPLETED_WITH_WARNINGS | SUPERSEDED              |

## Completion Requirements

* algorithm version
* candidate count
* confidence class
* signal explanations
* warning records
* immutable evaluation data

---

# PART XV — MATCH RESOLUTION STATE MACHINE

# 26. Match Resolution Workflow

**Machine ID**

```text
STATE-MATCH-RESOLUTION-001
```

## States

```text
DRAFT
READY_TO_FINALIZE
FINALIZED
SUPERSEDED
REOPENED
CANCELLED
```

## Initial State

```text
DRAFT
```

## Transitions

| From              | To                |
| ----------------- | ----------------- |
| DRAFT             | READY_TO_FINALIZE |
| DRAFT             | CANCELLED         |
| READY_TO_FINALIZE | DRAFT             |
| READY_TO_FINALIZE | FINALIZED         |
| FINALIZED         | SUPERSEDED        |
| FINALIZED         | REOPENED          |
| REOPENED          | READY_TO_FINALIZE |
| REOPENED          | CANCELLED         |

## Finalized Outcomes

```text
MATCH_EXISTING_PERSON
CREATE_NEW_PERSON
REQUIRES_MORE_INFORMATION
REJECT_ENTRY
DUPLICATE_INTAKE_ENTRY
ESCALATE_CONFLICT
```

## Finalization Guards

* authorized Reviewer
* current match evaluation
* selected outcome
* required candidate or duplicate target
* reason
* conflict acknowledgment
* expected entry version
* confirmation
* audit event within transaction

## Rule

Reopening never edits the finalized resolution.

It creates a new resolution version.

---

# PART XVI — PROMOTION STATE MACHINE

# 27. Promotion Request Lifecycle

**Machine ID**

```text
STATE-PROMOTION-001
```

## States

```text
PENDING
RUNNING
SUCCEEDED
FAILED_RETRYABLE
FAILED_FINAL
REQUIRES_REVIEW
CANCELLED
SUPERSEDED
```

## Initial State

```text
PENDING
```

## Transitions

| From             | To               |
| ---------------- | ---------------- |
| PENDING          | RUNNING          |
| PENDING          | CANCELLED        |
| RUNNING          | SUCCEEDED        |
| RUNNING          | FAILED_RETRYABLE |
| RUNNING          | FAILED_FINAL     |
| RUNNING          | REQUIRES_REVIEW  |
| FAILED_RETRYABLE | PENDING          |
| FAILED_RETRYABLE | CANCELLED        |
| REQUIRES_REVIEW  | PENDING          |
| REQUIRES_REVIEW  | FAILED_FINAL     |
| REQUIRES_REVIEW  | CANCELLED        |
| SUCCEEDED        | SUPERSEDED       |

## Success Guards

* canonical operation acknowledged
* canonical person external ID present when required
* canonical link created
* contributions recorded
* provenance recorded
* idempotency record completed
* audit event recorded

## Retry Rule

Every retry must reuse the original canonical idempotency identity.

---

# PART XVII — CANONICAL LINK STATE MACHINE

# 28. Canonical Person Link Lifecycle

**Machine ID**

```text
STATE-CANONICAL-LINK-001
```

## States

```text
ACTIVE
DISPUTED
SUPERSEDED
REVOKED_BY_CANONICAL_AUTHORITY
```

## Initial State

```text
ACTIVE
```

## Transitions

| From     | To                             |
| -------- | ------------------------------ |
| ACTIVE   | DISPUTED                       |
| ACTIVE   | SUPERSEDED                     |
| ACTIVE   | REVOKED_BY_CANONICAL_AUTHORITY |
| DISPUTED | ACTIVE                         |
| DISPUTED | SUPERSEDED                     |
| DISPUTED | REVOKED_BY_CANONICAL_AUTHORITY |

## Rule

Historical links remain preserved.

---

# PART XVIII — BACKGROUND JOB STATE MACHINE

# 29. Background Job Lifecycle

**Machine ID**

```text
STATE-JOB-001
```

## States

```text
PENDING
AVAILABLE
RUNNING
SUCCEEDED
FAILED_RETRYABLE
FAILED_FINAL
CANCELLED
DEAD_LETTER
```

## Initial State

```text
PENDING
```

## Transitions

| From             | To               |
| ---------------- | ---------------- |
| PENDING          | AVAILABLE        |
| PENDING          | CANCELLED        |
| AVAILABLE        | RUNNING          |
| RUNNING          | SUCCEEDED        |
| RUNNING          | FAILED_RETRYABLE |
| RUNNING          | FAILED_FINAL     |
| RUNNING          | AVAILABLE        |
| FAILED_RETRYABLE | AVAILABLE        |
| FAILED_RETRYABLE | DEAD_LETTER      |
| FAILED_FINAL     | DEAD_LETTER      |

## Rules

* stale worker lock may return running job to available
* attempt count increments atomically
* max attempts enforced
* terminal failure creates processing error
* no duplicated side effect on retry

---

# PART XIX — PROCESSING ERROR STATE MACHINE

# 30. Processing Error Lifecycle

**Machine ID**

```text
STATE-ERROR-001
```

## States

```text
OPEN
ACKNOWLEDGED
RETRYING
RESOLVED
IGNORED_WITH_REASON
ESCALATED
```

## Initial State

```text
OPEN
```

## Transitions

| From         | To                  |
| ------------ | ------------------- |
| OPEN         | ACKNOWLEDGED        |
| OPEN         | RETRYING            |
| OPEN         | RESOLVED            |
| OPEN         | ESCALATED           |
| OPEN         | IGNORED_WITH_REASON |
| ACKNOWLEDGED | RETRYING            |
| ACKNOWLEDGED | RESOLVED            |
| ACKNOWLEDGED | ESCALATED           |
| ACKNOWLEDGED | IGNORED_WITH_REASON |
| RETRYING     | RESOLVED            |
| RETRYING     | OPEN                |
| RETRYING     | ESCALATED           |
| ESCALATED    | RETRYING            |
| ESCALATED    | RESOLVED            |
| ESCALATED    | IGNORED_WITH_REASON |

## Rules

* acknowledgment is not resolution
* ignore requires reason
* resolution requires summary
* recurring error may reopen or create a linked new occurrence according to deduplication policy

---

# PART XX — OPERATOR ALERT STATE MACHINE

# 31. Alert Lifecycle

**Machine ID**

```text
STATE-ALERT-001
```

## States

```text
OPEN
ACKNOWLEDGED
IN_PROGRESS
RESOLVED
DISMISSED_WITH_REASON
ESCALATED
```

## Initial State

```text
OPEN
```

## Transitions

```text
OPEN → ACKNOWLEDGED
OPEN → IN_PROGRESS
OPEN → ESCALATED
OPEN → RESOLVED
ACKNOWLEDGED → IN_PROGRESS
ACKNOWLEDGED → ESCALATED
ACKNOWLEDGED → RESOLVED
IN_PROGRESS → RESOLVED
IN_PROGRESS → ESCALATED
ESCALATED → IN_PROGRESS
ESCALATED → RESOLVED
any nonterminal → DISMISSED_WITH_REASON
```

---

# PART XXI — IDEMPOTENCY STATE MACHINE

# 32. Idempotency Record Lifecycle

**Machine ID**

```text
STATE-IDEMPOTENCY-001
```

## States

```text
IN_PROGRESS
COMPLETED
FAILED_RETRYABLE
FAILED_FINAL
EXPIRED
```

## Initial State

```text
IN_PROGRESS
```

## Transitions

| From             | To               |
| ---------------- | ---------------- |
| IN_PROGRESS      | COMPLETED        |
| IN_PROGRESS      | FAILED_RETRYABLE |
| IN_PROGRESS      | FAILED_FINAL     |
| FAILED_RETRYABLE | IN_PROGRESS      |
| FAILED_RETRYABLE | EXPIRED          |
| FAILED_FINAL     | EXPIRED          |
| COMPLETED        | EXPIRED          |

## Rules

* same key plus different request fingerprint produces conflict
* completed operation returns original business result
* canonical creation idempotency may never expire
* expiration policy depends on operation class

---

# PART XXII — NOTIFICATION STATE MACHINE

# 33. In-App Notification Lifecycle

**Machine ID**

```text
STATE-NOTIFICATION-001
```

## States

```text
PENDING
DELIVERED
READ
ACKNOWLEDGED
DISMISSED
EXPIRED
FAILED
```

## Initial State

```text
PENDING
```

## Transitions

```text
PENDING → DELIVERED
PENDING → FAILED
DELIVERED → READ
DELIVERED → ACKNOWLEDGED
DELIVERED → DISMISSED
DELIVERED → EXPIRED
READ → ACKNOWLEDGED
READ → DISMISSED
READ → EXPIRED
```

A notification requiring action must not be treated as resolved merely because it was read.

---

# PART XXIII — EXPORT STATE MACHINE

# 34. Data Export Lifecycle

**Machine ID**

```text
STATE-EXPORT-001
```

## States

```text
REQUESTED
AUTHORIZATION_REVIEW
APPROVED
REJECTED
GENERATING
READY
DOWNLOADED
EXPIRED
FAILED
CANCELLED
```

## Initial State

```text
REQUESTED
```

## Transitions

```text
REQUESTED → AUTHORIZATION_REVIEW
REQUESTED → CANCELLED
AUTHORIZATION_REVIEW → APPROVED
AUTHORIZATION_REVIEW → REJECTED
APPROVED → GENERATING
GENERATING → READY
GENERATING → FAILED
READY → DOWNLOADED
READY → EXPIRED
```

## Rules

* export scope must be explicit
* privacy classification shown
* authorization checked
* export access expires
* export action audited
* generated file remains beneath approved project or provider-controlled storage boundary

---

# PART XXIV — ARCHIVAL STATE MACHINE

# 35. Archival Lifecycle

**Machine ID**

```text
STATE-ARCHIVE-001
```

## States

```text
ACTIVE
ARCHIVE_REQUESTED
ARCHIVED
RESTORATION_REQUESTED
RESTORED
DESTRUCTION_REVIEW
DESTRUCTION_APPROVED
DESTROYED
LEGAL_HOLD
```

## Version 1 Authorization

Authorized transitions:

```text
ACTIVE → ARCHIVE_REQUESTED
ARCHIVE_REQUESTED → ARCHIVED
ACTIVE → LEGAL_HOLD
ARCHIVED → LEGAL_HOLD
```

The following remain designed but disabled until the retention catalog authorizes them:

```text
ARCHIVED → RESTORATION_REQUESTED
RESTORATION_REQUESTED → RESTORED
ARCHIVED → DESTRUCTION_REVIEW
DESTRUCTION_REVIEW → DESTRUCTION_APPROVED
DESTRUCTION_APPROVED → DESTROYED
```

## Rule

Legal hold blocks destruction.

---

# PART XXV — STATE TRANSITION REASON CODES

# 36. Shared Reason Code Families

Detailed values will be finalized in the Error and Audit catalogs.

Required families include:

```text
USER_REQUEST
ADMINISTRATIVE_ACTION
SECURITY_ACTION
CLAIM_EXPIRED
WORK_COMPLETED
RETURNED_FOR_CORRECTION
IMAGE_UNUSABLE
UPLOAD_FAILED
VALIDATION_FAILED
MATCH_CONFLICT
INSUFFICIENT_INFORMATION
CANONICAL_SERVICE_FAILURE
DUPLICATE_INTAKE
ARCHIVAL_POLICY
LEGAL_HOLD
SYSTEM_RECOVERY
SUPERSEDED_BY_NEW_VERSION
```

---

# PART XXVI — REQUIRED STATE HISTORY

# 37. History Requirements

Dedicated history is mandatory for:

* user status
* role grants
* batch status
* page status
* claim lifecycle
* draft revisions
* entry submissions
* match resolutions
* promotion attempts
* canonical links
* background job attempts
* errors
* alerts
* archive actions

History entries must include:

```text
Record
Prior State
New State
Actor
Reason
Correlation ID
Occurred At
```

---

# PART XXVII — TRANSITION AUDIT REQUIREMENTS

# 38. Always-Audited Transitions

The following transitions always require an audit event:

* user invited
* user activated
* user suspended
* user disabled
* user revoked
* role granted
* role revoked
* batch completed
* batch archived
* image replaced
* claim administratively released
* draft recovered by another user
* page submitted
* transcription returned for correction
* transcription approved
* match resolution finalized
* match resolution reopened
* promotion requested
* promotion retried manually
* promotion succeeded
* promotion failed finally
* canonical link disputed
* export requested
* export downloaded
* legal hold applied
* destruction approved
* configuration changed

---

# PART XXVIII — STATE MACHINE TEST STANDARD

# 39. Required Tests Per Machine

Every state machine requires tests for:

1. valid initial creation
2. every allowed transition
3. every prohibited transition
4. authorization
5. missing guard
6. stale version
7. audit creation
8. history creation
9. transaction rollback
10. idempotent retry
11. concurrent transition attempt
12. terminal-state protection
13. recovery path
14. archived behavior

---

# PART XXIX — LOCKED STATE DECISIONS

# 40. Locked Decisions

1. State transitions are server-enforced.
2. Every state uses a cataloged canonical key.
3. State history is preserved.
4. State transitions are concurrency-protected.
5. UI labels may differ from machine keys but not from their meaning.
6. Claim expiration does not erase drafts.
7. Source-image replacement does not erase original images.
8. Submission creates an immutable revision.
9. Corrections create new revisions.
10. Match evaluations are immutable after completion.
11. Match resolutions are versioned.
12. Candidate selection is not finalization.
13. Promotions are independently stateful from resolutions.
14. Promotion retries reuse idempotency identity.
15. Canonical links retain history.
16. Acknowledgment is not resolution.
17. Read notification is not acknowledgment.
18. Archive is not deletion.
19. Legal hold blocks destruction.
20. Terminal failure cannot be displayed as success.
21. No state transition may silently skip audit when audit is required.
22. No undocumented state may appear in production.

---

# PART XXX — OPEN STATE DECISIONS

# 41. Deferred Decisions

### `STATE-DEC-001`

Exact claim duration.

### `STATE-DEC-002`

Exact claim-expiration warning threshold.

### `STATE-DEC-003`

Whether transcription review is page-level, entry-level, or hybrid at launch.

### `STATE-DEC-004`

Whether batch `PROCESSING` is persisted or derived.

### `STATE-DEC-005`

Whether page status is persisted as one status or projected from subdomain states.

### `STATE-DEC-006`

Exact restoration policy for archived records.

### `STATE-DEC-007`

Exact destruction lifecycle activation.

### `STATE-DEC-008`

Whether notifications expire automatically.

### `STATE-DEC-009`

Exact export-approval requirements.

### `STATE-DEC-010`

Whether role expiration is included in Version 1.

These decisions must be resolved before implementation packages that depend on them.

---

# PART XXXI — STATE CATALOG READINESS

# 42. Readiness Score

| Area                  | Readiness |
| --------------------- | --------: |
| User states           |      100% |
| Role states           |      100% |
| Batch states          |       99% |
| Page states           |       98% |
| Image states          |      100% |
| Upload states         |      100% |
| Queue states          |      100% |
| Claim states          |      100% |
| Draft states          |      100% |
| Entry states          |       99% |
| Normalization states  |      100% |
| Matching states       |      100% |
| Resolution states     |      100% |
| Promotion states      |      100% |
| Canonical-link states |      100% |
| Background-job states |      100% |
| Error states          |      100% |
| Alert states          |      100% |
| Idempotency states    |      100% |
| Notification states   |       98% |
| Export states         |       98% |
| Archive states        |       96% |
| Audit requirements    |      100% |
| Test requirements     |      100% |

**Overall Catalog 1 Readiness**

```text
99%
```

The remaining percentage is reserved for reconciliation with:

* Error Catalog
* Audit Event Catalog
* Configuration Catalog
* Permission Catalog
* Retention Catalog
* Cross-Volume Traceability Matrix

---

# 43. Next Catalog Build

The next catalog is:

```text
PEOPLE-CATALOG-02-ERRORS-1.0
```

It will define every stable error code, including:

* category
* severity
* triggering condition
* safe user message
* operator explanation
* HTTP status
* retryability
* preservation behavior
* recovery action
* audit requirements
* alert requirements
* owning domain
* related state transition
* required tests

The **Master Catalog Registry** and **State Machine Catalog** are now established. The next build is the **Error Catalog**, followed by Audit Events, Configuration, Permissions, Notifications, Jobs, Retention, and the final Traceability Matrix.
