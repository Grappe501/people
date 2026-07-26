# PEOPLE INTAKE SYSTEM

# VOLUME 9 — DATABASE SPECIFICATIONS

**Document ID**

```text
PEOPLE-VOLUME-09-DATABASE-SPECIFICATIONS-1.0
```

**Status**

```text
DESIGN COMPLETE — PENDING CROSS-VOLUME VALIDATION
```

**Project Root**

```text
H:\people
```

**Document Type**

```text
IMPLEMENTATION-GOVERNING DATABASE SPECIFICATION
```

**Build Mode**

```text
DOCUMENTATION ONLY
```

**Prohibited During This Volume**

* No SQL migrations
* No Prisma schema
* No ORM models
* No database provisioning
* No live database connection
* No production credentials
* No schema deployment
* No seed execution
* No destructive data operations

---

# PART I — PURPOSE AND GOVERNANCE

## 1. Purpose

Volume 9 defines the complete database architecture for the People Intake System before implementation begins.

It specifies:

* logical entities
* physical table responsibilities
* fields and data types
* primary keys
* foreign keys
* unique constraints
* check constraints
* indexes
* immutable records
* append-only histories
* record lifecycles
* state storage
* transaction boundaries
* optimistic concurrency
* idempotency
* auditability
* provenance
* retention
* archival
* canonical-person integration
* migration governance
* test-data requirements

This volume answers:

> What information must the People Intake System store, how must that information relate, and what database guarantees are required to preserve trust?

---

## 2. Governing Principles

### `DB-PRINCIPLE-001 — Evidence Before Interpretation`

Source evidence, transcription, normalization, matching, resolution, and canonical promotion must be represented as distinct data layers.

### `DB-PRINCIPLE-002 — History Before Convenience`

Meaningful revisions and decisions must be preserved rather than overwritten.

### `DB-PRINCIPLE-003 — Canonical Separation`

The People Intake database may store references to canonical people but must not become the hidden canonical people database.

### `DB-PRINCIPLE-004 — Constraints Enforce Truth`

Critical invariants must be enforced with database constraints where technically possible.

### `DB-PRINCIPLE-005 — Idempotency Is Durable`

Retry protection must be stored durably and must not depend only on in-memory application state.

### `DB-PRINCIPLE-006 — Authorization Is Not a Table Filter Alone`

Database structure must support authorization, but trusted application logic remains responsible for evaluating permissions unless approved database-level security is later implemented.

### `DB-PRINCIPLE-007 — Archive Is Not Delete`

Archived records remain historically available and retain relationships.

### `DB-PRINCIPLE-008 — Audit Is Independent`

Audit records must not be mixed into mutable business tables.

### `DB-PRINCIPLE-009 — UTC Time`

Persisted event timestamps must use UTC-capable timestamp types.

### `DB-PRINCIPLE-010 — Stable Identifiers`

Database primary keys must be stable and independent from names, email addresses, phone numbers, page numbers, or other mutable business values.

---

# PART II — DATABASE TECHNOLOGY POSTURE

## 3. Logical Technology Assumptions

The design assumes a relational database with capabilities comparable to PostgreSQL.

Required capabilities include:

* transactions
* foreign keys
* unique constraints
* check constraints
* partial indexes or equivalent
* JSON storage for bounded metadata
* timestamp with time zone
* row-level locking
* atomic updates
* generated or computed values where useful
* reliable backup and recovery
* migration support

The exact provider remains deferred.

---

## 4. Identifier Strategy

### 4.1 Primary Keys

All principal business records should use UUID-compatible identifiers.

Preferred conceptual type:

```text
UUID
```

Acceptable implementation options may include:

* UUID version 4
* UUID version 7
* another approved sortable globally unique identifier

The exact generator is deferred.

### 4.2 Human-Readable Display IDs

Selected records may also receive human-readable identifiers.

Examples:

```text
BAT-2026-000001
PAGE-2026-000001
ENT-2026-000001
PRM-2026-000001
```

Display IDs:

* are not primary keys
* must be unique
* must not encode personal information
* may be used in operator communication
* must never be reused

### 4.3 External Identifiers

Identifiers supplied by external systems must be stored separately and scoped by source system.

---

## 5. Timestamp Standard

Use UTC-capable timestamps for:

```text
created_at
updated_at
submitted_at
resolved_at
completed_at
failed_at
expires_at
archived_at
disabled_at
revoked_at
```

Business dates without time may use a date-only type.

Every mutable principal table should normally include:

```text
created_at
updated_at
```

Append-only tables normally require:

```text
created_at
```

but not `updated_at`.

---

## 6. Actor Attribution

Where a record represents a human or system action, store an actor reference.

Conceptual actor fields may include:

```text
created_by_user_id
updated_by_user_id
submitted_by_user_id
resolved_by_user_id
released_by_user_id
system_actor_key
```

A record must not falsely attribute an automated action to a human user.

---

## 7. Optimistic Concurrency

Mutable workflow tables should include a concurrency field.

Preferred conceptual field:

```text
row_version BIGINT
```

or an equivalent mechanism.

Rules:

* starts at a defined initial value
* increments on accepted mutation
* required in stale-write-sensitive updates
* must not be client-controlled
* must not replace transaction locking where locking is required

---

# PART III — DATABASE DOMAIN MAP

## 8. Table Families

The database is organized into these table families:

1. Identity and Access
2. Intake Batches and Pages
3. Source Images and Storage
4. Queue and Claims
5. Drafts and Transcription
6. Normalization
7. Matching
8. Match Resolution
9. Canonical Promotion
10. Person Attribute Contributions
11. Provenance
12. Audit
13. Background Jobs
14. Operational Errors and Alerts
15. Idempotency
16. Configuration References
17. Reporting Support

---

# PART IV — IDENTITY AND ACCESS TABLES

# 9. `application_users`

## 9.1 Purpose

Represents an approved People Intake application user.

## 9.2 Ownership

Owned by the User Access and Approval Domain.

## 9.3 Columns

| Column                  | Conceptual Type | Null | Purpose                             |
| ----------------------- | --------------- | ---: | ----------------------------------- |
| `id`                    | UUID            |   No | Primary key                         |
| `display_id`            | text            |   No | Human-readable stable identifier    |
| `external_auth_subject` | text            |  Yes | Authentication-provider identity    |
| `email_normalized`      | text            |  Yes | Approved user email for recognition |
| `display_name`          | text            |   No | User-facing name                    |
| `status`                | enum/text       |   No | User lifecycle state                |
| `invited_at`            | timestamptz     |  Yes | Invitation time                     |
| `activated_at`          | timestamptz     |  Yes | Activation time                     |
| `suspended_at`          | timestamptz     |  Yes | Suspension time                     |
| `disabled_at`           | timestamptz     |  Yes | Disablement time                    |
| `revoked_at`            | timestamptz     |  Yes | Revocation time                     |
| `last_authenticated_at` | timestamptz     |  Yes | Last verified authentication        |
| `created_by_user_id`    | UUID            |  Yes | Actor creating record               |
| `created_at`            | timestamptz     |   No | Creation time                       |
| `updated_at`            | timestamptz     |   No | Last update                         |
| `row_version`           | bigint          |   No | Optimistic concurrency              |

## 9.4 Allowed Status Values

```text
INVITED
ACTIVE
SUSPENDED
DISABLED
REVOKED
```

## 9.5 Constraints

* Primary key on `id`
* Unique `display_id`
* Unique non-null `external_auth_subject`
* Unique non-null `email_normalized`, unless future policy permits multiple users sharing an email, which is currently prohibited
* Status must use controlled values
* `activated_at` required when status has ever become `ACTIVE`
* Revoked state must not be silently returned to active without a new approval event

## 9.6 Indexes

* unique index on `external_auth_subject`
* unique index on `email_normalized`
* index on `status`
* index on `created_at`

## 9.7 Lifecycle

```text
INVITED → ACTIVE
ACTIVE → SUSPENDED
SUSPENDED → ACTIVE
ACTIVE/SUSPENDED → DISABLED
ACTIVE/SUSPENDED/DISABLED → REVOKED
```

Exact transition enforcement belongs to the State Machine Catalog and service layer.

## 9.8 Deletion

Application users must not be hard-deleted through ordinary operations.

Historical attribution requires the row to remain.

---

# 10. `user_roles`

## 10.1 Purpose

Stores current effective roles for application users.

## 10.2 Columns

| Column               | Type        | Null | Purpose             |
| -------------------- | ----------- | ---: | ------------------- |
| `id`                 | UUID        |   No | Primary key         |
| `user_id`            | UUID        |   No | Application user    |
| `role_key`           | text        |   No | Role                |
| `granted_by_user_id` | UUID        |  Yes | Granting actor      |
| `granted_at`         | timestamptz |   No | Grant time          |
| `expires_at`         | timestamptz |  Yes | Optional expiration |
| `revoked_at`         | timestamptz |  Yes | Revocation time     |
| `revoked_by_user_id` | UUID        |  Yes | Revoking actor      |
| `revocation_reason`  | text        |  Yes | Reason              |
| `created_at`         | timestamptz |   No | Creation time       |

## 10.3 Role Values

```text
UPLOADER
DATA_ENTRY
REVIEWER
ADMIN
OWNER
```

## 10.4 Constraints

* Foreign key to `application_users`
* Unique active role per user and role key
* `expires_at` must be later than `granted_at`
* Revoked role must include `revoked_at`
* Revocation actor may be null only for defined system expiration

## 10.5 Indexes

* index on `user_id`
* partial unique index on active `(user_id, role_key)`
* index on active `role_key`
* index on `expires_at`

---

# 11. `user_role_history`

## 11.1 Purpose

Append-only record of role changes.

## 11.2 Columns

```text
id
user_id
role_key
action
effective_at
actor_user_id
reason
source_user_role_id
correlation_id
created_at
```

## 11.3 Actions

```text
GRANTED
REVOKED
EXPIRED
RESTORED
```

## 11.4 Rules

* Append-only
* No updates after creation
* No hard delete
* Every role mutation must produce one history record
* Historical role records do not grant current access

---

# 12. `user_access_events`

## 12.1 Purpose

Stores durable access lifecycle events distinct from general audit events where a dedicated identity timeline is useful.

Possible events:

```text
INVITED
ACTIVATED
SUSPENDED
RESTORED
DISABLED
REVOKED
AUTH_IDENTITY_LINKED
AUTH_IDENTITY_CHANGED
```

This table may later be implemented as a filtered projection from the Audit Event system. Volume 10 and Volume 13 should determine whether a dedicated table remains necessary.

---

# PART V — INTAKE BATCH AND PAGE TABLES

# 13. `intake_batches`

## 13.1 Purpose

Represents a logical collection of source pages received together.

## 13.2 Columns

| Column                | Type        | Null | Purpose                         |
| --------------------- | ----------- | ---: | ------------------------------- |
| `id`                  | UUID        |   No | Primary key                     |
| `display_id`          | text        |   No | Human-readable batch identifier |
| `title`               | text        |   No | Operator label                  |
| `description`         | text        |  Yes | Operational description         |
| `source_description`  | text        |  Yes | Where batch came from           |
| `received_date`       | date        |  Yes | Date received                   |
| `expected_page_count` | integer     |  Yes | Expected pages                  |
| `status`              | text        |   No | Batch state                     |
| `uploads_closed_at`   | timestamptz |  Yes | Time uploads closed             |
| `completed_at`        | timestamptz |  Yes | Completion time                 |
| `archived_at`         | timestamptz |  Yes | Archive time                    |
| `created_by_user_id`  | UUID        |   No | Creator                         |
| `created_at`          | timestamptz |   No | Creation time                   |
| `updated_at`          | timestamptz |   No | Last update                     |
| `row_version`         | bigint      |   No | Concurrency                     |

## 13.3 Suggested Status Values

```text
DRAFT
OPEN
PROCESSING
READY_FOR_COMPLETION
COMPLETED
ARCHIVED
EXCEPTION
```

Final values will be frozen in the State Machine Catalog.

## 13.4 Constraints

* Unique `display_id`
* `expected_page_count >= 0`
* `completed_at` only when status is completed or archived
* `archived_at` only when archived
* Batch title must not be blank after trimming

## 13.5 Indexes

* index on `status`
* index on `received_date`
* index on `created_by_user_id`
* index on `created_at`
* partial index on active non-archived batches

## 13.6 Deletion

No ordinary hard deletion after a page has been attached.

Empty accidental draft batches may be eligible for controlled deletion before evidence is attached, subject to audit policy.

---

# 14. `intake_batch_status_history`

## 14.1 Purpose

Append-only batch state transitions.

Columns:

```text
id
batch_id
from_status
to_status
actor_user_id
system_actor_key
reason
correlation_id
created_at
```

Rules:

* Append-only
* Every batch state change produces one history record
* Initial creation may use null `from_status`

---

# 15. `intake_pages`

## 15.1 Purpose

Represents one physical or captured source sheet within a batch.

## 15.2 Columns

| Column                   | Type        | Null | Purpose                        |
| ------------------------ | ----------- | ---: | ------------------------------ |
| `id`                     | UUID        |   No | Primary key                    |
| `display_id`             | text        |   No | Human-readable page identifier |
| `batch_id`               | UUID        |   No | Parent batch                   |
| `page_sequence`          | integer     |  Yes | Operator-defined order         |
| `page_label`             | text        |  Yes | Optional source label          |
| `status`                 | text        |   No | Workflow state                 |
| `active_source_image_id` | UUID        |  Yes | Current image version          |
| `quality_status`         | text        |   No | Image usability                |
| `entry_count`            | integer     |   No | Derived/cache count            |
| `submitted_at`           | timestamptz |  Yes | Submission time                |
| `completed_at`           | timestamptz |  Yes | Completion time                |
| `archived_at`            | timestamptz |  Yes | Archive time                   |
| `created_by_user_id`     | UUID        |   No | Creator                        |
| `created_at`             | timestamptz |   No | Creation time                  |
| `updated_at`             | timestamptz |   No | Last update                    |
| `row_version`            | bigint      |   No | Concurrency                    |

## 15.3 Quality Values

```text
PENDING_REVIEW
USABLE
BLURRY
CROPPED
WRONG_DOCUMENT
CORRUPT
REPLACEMENT_REQUIRED
```

Final values must align with the State Machine Catalog.

## 15.4 Constraints

* Unique `display_id`
* Foreign key to `intake_batches`
* `page_sequence > 0` where present
* `entry_count >= 0`
* Initial supported entry count must not exceed ten without approved configuration
* Active source image must belong to this page
* A page cannot reference an image from another page
* Completed page must have a usable active image

## 15.5 Unique Rules

Within a batch:

* `page_sequence` should be unique when non-null
* exact duplicate labels may be allowed only with warning; labels are not identity

## 15.6 Indexes

* index on `batch_id`
* index on `(batch_id, page_sequence)`
* index on `status`
* index on `quality_status`
* partial index on queue-eligible pages
* index on `active_source_image_id`

---

# 16. `intake_page_status_history`

Append-only state transition history.

Columns:

```text
id
page_id
from_status
to_status
actor_user_id
system_actor_key
reason
correlation_id
created_at
```

---

# PART VI — SOURCE IMAGE AND STORAGE TABLES

# 17. `storage_objects`

## 17.1 Purpose

Represents one privately stored binary object.

## 17.2 Columns

| Column                  | Type        | Null | Purpose                    |
| ----------------------- | ----------- | ---: | -------------------------- |
| `id`                    | UUID        |   No | Primary key                |
| `provider_key`          | text        |   No | Storage provider class     |
| `bucket_key`            | text        |   No | Logical bucket             |
| `object_key`            | text        |   No | Private object path        |
| `original_filename`     | text        |  Yes | Sanitized display filename |
| `content_type_declared` | text        |  Yes | Client-declared type       |
| `content_type_detected` | text        |  Yes | Server-detected type       |
| `size_bytes`            | bigint      |   No | Object size                |
| `sha256_hash`           | text        |   No | Integrity hash             |
| `storage_status`        | text        |   No | Storage lifecycle          |
| `stored_at`             | timestamptz |  Yes | Successful storage time    |
| `verified_at`           | timestamptz |  Yes | Integrity verification     |
| `quarantined_at`        | timestamptz |  Yes | Quarantine time            |
| `deleted_at`            | timestamptz |  Yes | Controlled destruction     |
| `created_at`            | timestamptz |   No | Creation time              |
| `row_version`           | bigint      |   No | Concurrency                |

## 17.3 Storage Status Values

```text
PENDING
UPLOADING
STORED
VERIFIED
QUARANTINED
MISSING
DELETION_PENDING
DELETED
FAILED
```

## 17.4 Constraints

* Unique `(provider_key, bucket_key, object_key)`
* `size_bytes >= 0`
* Hash format validated
* Deleted object must have `deleted_at`
* Verified object must have `verified_at`
* Storage object path must never contain raw personal fields

## 17.5 Indexes

* unique object locator index
* index on `sha256_hash`
* index on `storage_status`
* index on `created_at`
* partial index on incomplete objects
* partial index on missing or failed objects

---

# 18. `source_images`

## 18.1 Purpose

Represents one version of source evidence attached to a page.

## 18.2 Columns

```text
id
page_id
storage_object_id
version_number
is_original_upload
is_active
rotation_metadata
width_pixels
height_pixels
image_quality_notes
uploaded_by_user_id
replaces_source_image_id
created_at
```

## 18.3 Constraints

* Foreign key to `intake_pages`
* Foreign key to `storage_objects`
* Unique `(page_id, version_number)`
* One active image per page
* `version_number >= 1`
* Replacement image must refer to an image belonging to the same page
* Original upload cannot be deleted through replacement

## 18.4 Indexes

* index on `page_id`
* partial unique index on active image per page
* index on `storage_object_id`
* index on `replaces_source_image_id`

## 18.5 Immutability

The following should be immutable after acceptance:

* page association
* storage object
* version number
* uploader
* creation time

Changing active status is allowed through controlled replacement.

---

# 19. `image_access_events`

## 19.1 Purpose

Records sensitive image access where policy requires durable history.

Columns:

```text
id
source_image_id
user_id
access_purpose
access_result
request_correlation_id
client_context_summary
created_at
```

Do not store:

* signed URL
* token
* raw image data
* unnecessary IP data unless approved security policy requires it

This table may later be merged into the general Audit Event table if the audit model sufficiently supports high-volume access events.

---

# PART VII — UPLOAD TABLES

# 20. `upload_sessions`

## 20.1 Purpose

Represents an upload lifecycle from initiation through completion.

## 20.2 Columns

```text
id
display_id
batch_id
intended_page_id
initiated_by_user_id
idempotency_key
status
declared_filename
declared_content_type
declared_size_bytes
storage_object_id
failure_code
failure_detail_safe
expires_at
completed_at
created_at
updated_at
row_version
```

## 20.3 Constraints

* Unique `display_id`
* Unique scoped idempotency key
* `declared_size_bytes >= 0`
* Completed status requires storage object
* Expiration must be later than creation
* One completed upload session cannot attach to multiple pages

## 20.4 Indexes

* index on `batch_id`
* index on `intended_page_id`
* index on `status`
* index on `expires_at`
* unique idempotency index
* partial index on incomplete active uploads

---

# 21. `upload_attempts`

Append-only attempt history.

Columns:

```text
id
upload_session_id
attempt_number
started_at
completed_at
result
failure_code
storage_reference_safe
created_at
```

Unique:

```text
(upload_session_id, attempt_number)
```

---

# PART VIII — QUEUE AND CLAIM TABLES

# 22. `work_queue_items`

## 22.1 Purpose

Represents derived work eligibility when a durable queue table is used.

## 22.2 Design Decision

Queue truth remains workflow state.

This table is an operational projection, not the ultimate source of business truth.

## 22.3 Columns

```text
id
work_type
subject_type
subject_id
priority
eligibility_status
available_at
not_before
removed_at
removal_reason
created_at
updated_at
row_version
```

## 22.4 Work Types

```text
TRANSCRIPTION
TRANSCRIPTION_REVIEW
MATCH_REVIEW
PROMOTION_RETRY
OPERATIONAL_EXCEPTION
```

## 22.5 Constraints

* Subject type and ID required
* One active queue item per work type and subject
* Priority within approved range
* Removed queue item must have `removed_at`
* Queue item does not remain active when subject is no longer eligible

## 22.6 Indexes

* partial index on active eligible items
* index on `(work_type, priority, available_at)`
* index on `(subject_type, subject_id)`
* partial unique active queue identity

---

# 23. `work_claims`

## 23.1 Purpose

Represents temporary ownership of a queue work item.

## 23.2 Columns

| Column                | Type        | Null | Purpose              |
| --------------------- | ----------- | ---: | -------------------- |
| `id`                  | UUID        |   No | Primary key          |
| `queue_item_id`       | UUID        |   No | Work item            |
| `claim_type`          | text        |   No | Claim classification |
| `claimed_by_user_id`  | UUID        |   No | Claim holder         |
| `status`              | text        |   No | Claim state          |
| `claimed_at`          | timestamptz |   No | Claim time           |
| `expires_at`          | timestamptz |   No | Expiration           |
| `renewed_at`          | timestamptz |  Yes | Last renewal         |
| `released_at`         | timestamptz |  Yes | Release time         |
| `released_by_user_id` | UUID        |  Yes | Actor                |
| `release_reason`      | text        |  Yes | Reason               |
| `row_version`         | bigint      |   No | Concurrency          |
| `created_at`          | timestamptz |   No | Creation             |

## 23.3 Status Values

```text
ACTIVE
EXPIRED
RELEASED
COMPLETED
CANCELLED
```

## 23.4 Constraints

* One active claim per queue item and claim type
* `expires_at > claimed_at`
* Released claim requires release time
* Administrative release requires reason
* Completed claim must correspond to completed workflow action
* Claim holder immutable

## 23.5 Indexes

* partial unique index on active claim
* index on `claimed_by_user_id`
* index on `expires_at`
* index on `status`
* index on `queue_item_id`

---

# 24. `claim_history`

Append-only record of claim events.

Events:

```text
CLAIMED
RENEWED
EXPIRED
RELEASED
COMPLETED
CANCELLED
ADMIN_RELEASED
```

Columns:

```text
id
claim_id
event_type
actor_user_id
system_actor_key
previous_expires_at
new_expires_at
reason
correlation_id
created_at
```

---

# PART IX — DRAFT AND TRANSCRIPTION TABLES

# 25. `page_drafts`

## 25.1 Purpose

Represents the current recoverable draft state for a page transcription workspace.

## 25.2 Columns

```text
id
page_id
owner_user_id
source_claim_id
current_revision_number
status
last_saved_at
submitted_at
created_at
updated_at
row_version
```

## 25.3 Status Values

```text
ACTIVE
SUPERSEDED
SUBMITTED
ABANDONED
RECOVERED
```

## 25.4 Constraints

* One current active draft per page transcription workflow
* Current revision number nonnegative
* Submitted draft must have `submitted_at`
* Draft owner does not imply permanent page ownership

---

# 26. `page_draft_revisions`

## 26.1 Purpose

Append-only snapshots of draft data.

## 26.2 Columns

```text
id
page_draft_id
revision_number
saved_by_user_id
source_claim_id
payload_json
payload_schema_version
change_summary
created_at
```

## 26.3 Constraints

* Unique `(page_draft_id, revision_number)`
* Revision numbers strictly increase
* Payload conforms to approved schema
* Saved actor required
* No mutation after creation

## 26.4 JSON Use

JSON is acceptable here for a bounded draft snapshot because:

* draft structure is versioned
* snapshot recovery is valuable
* canonical query behavior should rely on normalized relational tables after submission

Draft JSON must not replace relational submitted-entry storage.

---

# 27. `intake_entries`

## 27.1 Purpose

Represents one independently tracked handwritten person row.

## 27.2 Columns

| Column                           | Type        | Null | Purpose                      |
| -------------------------------- | ----------- | ---: | ---------------------------- |
| `id`                             | UUID        |   No | Primary key                  |
| `display_id`                     | text        |   No | Human-readable entry ID      |
| `page_id`                        | UUID        |   No | Source page                  |
| `row_position`                   | integer     |   No | Physical row                 |
| `status`                         | text        |   No | Entry workflow state         |
| `current_submission_revision_id` | UUID        |  Yes | Current effective submission |
| `effective_match_resolution_id`  | UUID        |  Yes | Current resolution           |
| `canonical_person_link_id`       | UUID        |  Yes | Effective canonical link     |
| `rejection_reason_code`          | text        |  Yes | Rejection reason             |
| `archived_at`                    | timestamptz |  Yes | Archive                      |
| `created_at`                     | timestamptz |   No | Creation                     |
| `updated_at`                     | timestamptz |   No | Update                       |
| `row_version`                    | bigint      |   No | Concurrency                  |

## 27.3 Constraints

* Unique `display_id`
* Unique `(page_id, row_position)`
* `row_position` between 1 and configured maximum, initially 10
* Current submission must belong to entry
* Effective resolution must belong to entry
* Canonical link must belong to entry
* Rejection reason required for rejected state
* Blank physical rows must not have entries

## 27.4 Indexes

* index on `page_id`
* unique row-position index
* index on `status`
* index on `current_submission_revision_id`
* index on `effective_match_resolution_id`
* index on `canonical_person_link_id`
* partial index on entries awaiting review

---

# 28. `entry_submission_revisions`

## 28.1 Purpose

Stores each immutable submitted version of an entry.

## 28.2 Columns

```text
id
entry_id
revision_number
submitted_by_user_id
source_page_draft_revision_id
submission_status
submitted_at
supersedes_submission_revision_id
correction_reason
created_at
```

## 28.3 Constraints

* Unique `(entry_id, revision_number)`
* Append-only
* Superseded revision must belong to same entry
* Revision number strictly increases
* Correction requires a reason
* Current effective revision is referenced from `intake_entries`

---

# 29. `intake_entry_fields`

## 29.1 Purpose

Stores field values for a submitted entry revision.

## 29.2 Columns

```text
id
submission_revision_id
field_key
raw_value
field_condition
operator_note
created_at
```

## 29.3 Field Keys

```text
LAST_NAME
FIRST_NAME
EMAIL
PHONE
ZIP
VOLUNTEER
EMAIL_LIST
```

## 29.4 Field Conditions

```text
PROVIDED
NOT_PROVIDED
UNREADABLE
AMBIGUOUS
CORRECTED
```

## 29.5 Constraints

* Unique `(submission_revision_id, field_key)`
* Controlled field key
* Controlled field condition
* Volunteer and Email List raw semantic values limited to:

  * YES
  * NO
  * UNKNOWN
* `NOT_PROVIDED` preference values must resolve to `UNKNOWN`
* Empty raw value with `PROVIDED` generally invalid unless field type supports meaningful blank, which current fields do not
* `CORRECTED` must belong to a correction revision or contain correction lineage

## 29.6 Indexes

* index on `submission_revision_id`
* index on `field_key`
* limited indexes on raw values should be avoided due to privacy and poor query semantics

---

# 30. `entry_field_revision_history`

## 30.1 Purpose

Optional granular append-only field history.

This may be unnecessary if complete immutable submission revisions provide sufficient history.

Volume 10 and implementation design should determine whether:

* submission revisions alone are sufficient, or
* granular field history materially improves review and audit.

If retained, columns include:

```text
id
entry_id
field_key
old_submission_revision_id
new_submission_revision_id
change_type
changed_by_user_id
reason
created_at
```

---

# PART X — NORMALIZATION TABLES

# 31. `normalization_runs`

## 31.1 Purpose

Represents one normalization execution for an entry submission revision.

## 31.2 Columns

```text
id
submission_revision_id
normalization_version
status
started_at
completed_at
failure_code
created_at
```

## 31.3 Constraints

* Unique effective run per submission revision and normalization version
* Completed run requires completion time
* Version required
* Run is immutable after terminal state except controlled recovery metadata

---

# 32. `normalized_entry_fields`

## 32.1 Purpose

Stores normalized comparison values.

## 32.2 Columns

```text
id
normalization_run_id
field_key
normalized_value
normalization_status
warning_codes_json
created_at
```

## 32.3 Normalization Status

```text
NORMALIZED
UNCHANGED
INVALID
INCOMPLETE
AMBIGUOUS
NOT_APPLICABLE
```

## 32.4 Constraints

* Unique `(normalization_run_id, field_key)`
* Controlled field key and status
* Normalized value may be null when invalid, incomplete, or not applicable
* Raw value must not be copied unnecessarily

## 32.5 Sensitive Index Strategy

Potential indexes:

* hashed normalized email
* hashed normalized phone
* normalized ZIP
* name comparison key

The exact privacy-preserving index design is deferred.

Direct broad indexing of raw personal fields is discouraged.

---

# PART XI — MATCHING TABLES

# 33. `match_evaluations`

## 33.1 Purpose

Represents one versioned matching evaluation of one submitted entry revision.

## 33.2 Columns

```text
id
entry_id
submission_revision_id
normalization_run_id
algorithm_version
status
confidence_class
candidate_count
initiated_by_user_id
system_actor_key
started_at
completed_at
failure_code
supersedes_match_evaluation_id
created_at
```

## 33.3 Status Values

```text
PENDING
RUNNING
COMPLETED
FAILED
SUPERSEDED
CANCELLED
```

## 33.4 Confidence Values

```text
EXACT
HIGH
POSSIBLE
LOW
NO_MATCH
CONFLICT
```

## 33.5 Constraints

* Submission revision must belong to entry
* Normalization run must belong to submission revision
* Algorithm version required
* Completed evaluation requires confidence class and completion time
* Superseded evaluation must belong to same entry
* Candidate count nonnegative

## 33.6 Indexes

* index on `entry_id`
* index on `submission_revision_id`
* index on `status`
* index on `confidence_class`
* index on `created_at`
* partial index on pending or failed evaluations

---

# 34. `match_candidates`

## 34.1 Purpose

Represents one canonical-person candidate within an evaluation.

## 34.2 Columns

```text
id
match_evaluation_id
canonical_system_key
canonical_person_external_id
rank
confidence_class
score_numeric
display_summary_json
supporting_signal_count
conflicting_signal_count
created_at
```

## 34.3 Constraints

* Unique candidate per evaluation and canonical person reference
* Rank positive
* Rank unique within evaluation
* Score bounded by documented scale
* Display summary contains only approved minimized fields
* Candidate is immutable within evaluation

## 34.4 Indexes

* index on `match_evaluation_id`
* unique candidate identity within evaluation
* index on canonical person reference
* index on confidence class

---

# 35. `match_signals`

## 35.1 Purpose

Stores explainable evidence for or against a candidate.

## 35.2 Columns

```text
id
match_candidate_id
signal_key
signal_direction
signal_strength
source_field_key
canonical_attribute_type
comparison_summary
score_contribution
created_at
```

## 35.3 Signal Direction

```text
SUPPORTS
WEAKENS
CONFLICTS
NEUTRAL
```

## 35.4 Constraints

* Signal key controlled
* Direction controlled
* Strength bounded
* Comparison summary must not contain unnecessary raw PII
* Signal immutable after evaluation completion

---

# 36. `match_evaluation_warnings`

## 36.1 Purpose

Stores evaluation-level warnings not tied to one candidate.

Examples:

* insufficient data
* shared household contact
* conflicting strong identifiers
* canonical service partial result
* low-quality source field
* possible duplicate intake entry

Columns:

```text
id
match_evaluation_id
warning_code
severity
safe_message
created_at
```

---

# PART XII — MATCH RESOLUTION TABLES

# 37. `match_resolutions`

## 37.1 Purpose

Stores authorized human identity decisions.

## 37.2 Columns

| Column                                  | Type        | Null | Purpose                   |
| --------------------------------------- | ----------- | ---: | ------------------------- |
| `id`                                    | UUID        |   No | Primary key               |
| `entry_id`                              | UUID        |   No | Intake entry              |
| `match_evaluation_id`                   | UUID        |  Yes | Evaluation reviewed       |
| `resolution_version`                    | integer     |   No | Resolution sequence       |
| `outcome`                               | text        |   No | Decision                  |
| `selected_match_candidate_id`           | UUID        |  Yes | Existing person candidate |
| `selected_canonical_system_key`         | text        |  Yes | Canonical system          |
| `selected_canonical_person_external_id` | text        |  Yes | Canonical person          |
| `resolved_by_user_id`                   | UUID        |   No | Reviewer                  |
| `resolution_reason`                     | text        |   No | Human explanation         |
| `evidence_context_json`                 | JSON        |  Yes | Safe decision context     |
| `supersedes_resolution_id`              | UUID        |  Yes | Prior resolution          |
| `resolved_at`                           | timestamptz |   No | Resolution time           |
| `created_at`                            | timestamptz |   No | Creation                  |

## 37.3 Outcomes

```text
MATCH_EXISTING_PERSON
CREATE_NEW_PERSON
REQUIRES_MORE_INFORMATION
REJECT_ENTRY
DUPLICATE_INTAKE_ENTRY
ESCALATE_CONFLICT
```

## 37.4 Constraints

* Unique `(entry_id, resolution_version)`
* Reviewer required
* Reason required
* Existing-person outcome requires selected canonical person
* Create-new outcome must not include selected existing person
* Duplicate-entry outcome should reference duplicate target through a separate relation
* Superseding resolution must belong to same entry
* Append-only

## 37.5 Indexes

* index on `entry_id`
* index on `outcome`
* index on `resolved_by_user_id`
* index on selected canonical person
* index on `resolved_at`

---

# 38. `duplicate_entry_links`

## 38.1 Purpose

Represents a reviewed determination that one intake entry duplicates another intake entry.

Columns:

```text
id
duplicate_entry_id
primary_entry_id
match_resolution_id
reason
created_at
```

Constraints:

* Entries must differ
* Unique effective duplicate relation
* Resolution must have duplicate-entry outcome
* Does not delete either entry

---

# 39. `resolution_status_history`

Optional append-only operational history for resolution workflow transitions such as:

```text
DRAFTED
FINALIZED
SUPERSEDED
REOPENED
```

The actual identity decision remains in immutable `match_resolutions`.

---

# PART XIII — CANONICAL PROMOTION TABLES

# 40. `promotion_requests`

## 40.1 Purpose

Stores a durable idempotent request to apply an approved resolution to the canonical people domain.

## 40.2 Columns

```text
id
display_id
entry_id
match_resolution_id
operation_type
canonical_system_key
idempotency_key
status
requested_by_user_id
requested_at
completed_at
failed_at
failure_code
latest_attempt_number
canonical_result_type
canonical_person_external_id
row_version
created_at
updated_at
```

## 40.3 Operation Types

```text
LINK_EXISTING_PERSON
CREATE_NEW_PERSON
CONTRIBUTE_ATTRIBUTES
NO_CANONICAL_CHANGE
```

A single promotion request may orchestrate more than one canonical operation only if the transaction contract is explicitly documented.

## 40.4 Status Values

```text
PENDING
RUNNING
SUCCEEDED
FAILED_RETRYABLE
FAILED_FINAL
REQUIRES_REVIEW
CANCELLED
```

## 40.5 Constraints

* Unique `display_id`
* Unique idempotency key within canonical system
* Resolution must belong to entry
* Resolution must authorize operation type
* Success requires result type
* Existing-person link success requires canonical person ID
* New-person creation success requires canonical person ID
* Terminal failure requires failure code

## 40.6 Indexes

* index on `entry_id`
* index on `match_resolution_id`
* index on `status`
* unique idempotency index
* index on canonical person reference
* partial index on retryable requests

---

# 41. `promotion_attempts`

## 41.1 Purpose

Append-only attempt records for canonical promotion.

Columns:

```text
id
promotion_request_id
attempt_number
started_at
completed_at
result
failure_code
http_status_safe
provider_request_reference
provider_response_reference
retry_after
created_at
```

Constraints:

* Unique `(promotion_request_id, attempt_number)`
* Attempt number positive
* No secrets or full provider payloads
* Provider references must be safe opaque identifiers

---

# 42. `canonical_person_links`

## 42.1 Purpose

Stores the durable relationship between an intake entry and a canonical person.

## 42.2 Columns

```text
id
entry_id
canonical_system_key
canonical_person_external_id
promotion_request_id
link_status
linked_at
superseded_at
superseded_by_link_id
created_at
```

## 42.3 Constraints

* One current effective canonical link per entry
* Canonical person reference required
* Promotion request required
* Superseding link must belong to same entry
* Historical links remain preserved

## 42.4 Link Status

```text
ACTIVE
SUPERSEDED
DISPUTED
REVOKED_BY_CANONICAL_AUTHORITY
```

Revocation does not erase history.

---

# 43. `canonical_attribute_contributions`

## 43.1 Purpose

Records each attribute contribution sent to or acknowledged by the canonical domain.

## 43.2 Columns

```text
id
promotion_request_id
entry_id
field_key
attribute_type
raw_value_reference_id
normalized_value_reference_id
contribution_value_safe
preference_value
source_confidence
canonical_result_status
canonical_attribute_external_id
conflict_status
created_at
```

## 43.3 Rules

* Contribution must trace to entry and promotion
* Preference values restricted to `YES`, `NO`, `UNKNOWN`
* Unknown must not be translated to No
* Canonical result status records whether accepted, ignored, conflicted, or deferred
* Raw personal values should be referenced rather than duplicated where practical

---

# PART XIV — PROVENANCE TABLES

# 44. `provenance_records`

## 44.1 Purpose

Represents one provenance statement linking source, transformation, decision, or destination.

## 44.2 Columns

```text
id
provenance_type
subject_type
subject_id
source_system_key
source_record_type
source_record_id
source_image_id
actor_user_id
system_actor_key
transformation_key
transformation_version
review_reference_type
review_reference_id
destination_system_key
destination_record_type
destination_record_id
correlation_id
created_at
```

## 44.3 Provenance Types

```text
SOURCE
TRANSCRIPTION
NORMALIZATION
MATCH_EVALUATION
HUMAN_RESOLUTION
PROMOTION
CANONICAL_CONTRIBUTION
CORRECTION
ARCHIVAL
```

## 44.4 Constraints

* Subject required
* Source or actor context required as appropriate
* Human and system actors mutually distinguishable
* Destination required for promotion or canonical contribution
* Append-only
* No ordinary update or deletion

## 44.5 Indexes

* index on `(subject_type, subject_id)`
* index on source record
* index on destination record
* index on `source_image_id`
* index on `correlation_id`
* index on `created_at`

---

# 45. `provenance_links`

Optional generalized graph links when one provenance record depends on another.

Columns:

```text
parent_provenance_id
child_provenance_id
relationship_type
created_at
```

Use only if direct fields in `provenance_records` are insufficient. Avoid unnecessary graph complexity.

---

# PART XV — AUDIT TABLES

# 46. `audit_events`

## 46.1 Purpose

Stores immutable business audit events.

## 46.2 Columns

| Column             | Type        | Null | Purpose                  |
| ------------------ | ----------- | ---: | ------------------------ |
| `id`               | UUID        |   No | Primary key              |
| `event_name`       | text        |   No | Stable catalog event     |
| `event_version`    | integer     |   No | Payload version          |
| `domain_key`       | text        |   No | Owning domain            |
| `actor_type`       | text        |   No | Human/system             |
| `actor_user_id`    | UUID        |  Yes | Human actor              |
| `system_actor_key` | text        |  Yes | System actor             |
| `subject_type`     | text        |   No | Primary business subject |
| `subject_id`       | UUID/text   |   No | Subject identity         |
| `object_type`      | text        |  Yes | Secondary object         |
| `object_id`        | UUID/text   |  Yes | Secondary object ID      |
| `result`           | text        |   No | Outcome                  |
| `reason_code`      | text        |  Yes | Controlled reason        |
| `payload_json`     | JSON        |  Yes | Safe structured details  |
| `correlation_id`   | text/UUID   |   No | Operation correlation    |
| `occurred_at`      | timestamptz |   No | Business event time      |
| `recorded_at`      | timestamptz |   No | Audit write time         |

## 46.3 Actor Constraints

Exactly one of:

* `actor_user_id`
* `system_actor_key`

should normally be present.

Approved anonymous security events may be exceptions.

## 46.4 Result Values

```text
SUCCEEDED
FAILED
DENIED
PARTIAL
CANCELLED
```

## 46.5 Rules

* Append-only
* No secrets
* No signed URLs
* No passwords or tokens
* Raw PII minimized
* Event name must exist in Audit Event Catalog
* Payload must conform to event version
* Audit failure must block designated high-risk transactions

## 46.6 Indexes

* index on `event_name`
* index on `(subject_type, subject_id)`
* index on `actor_user_id`
* index on `system_actor_key`
* index on `correlation_id`
* index on `occurred_at`
* index on `result`
* partitioning may be considered later at scale

---

# PART XVI — BACKGROUND JOB TABLES

# 47. `background_jobs`

## 47.1 Purpose

Represents durable asynchronous work.

## 47.2 Columns

```text
id
job_type
subject_type
subject_id
deduplication_key
status
priority
available_at
locked_at
locked_by_worker
heartbeat_at
attempt_count
max_attempts
completed_at
failed_at
failure_code
payload_json
payload_schema_version
created_at
updated_at
row_version
```

## 47.3 Constraints

* Unique active deduplication key where applicable
* Attempt count nonnegative
* Max attempts positive
* Completed job requires completed time
* Final failure requires failure time and code
* Payload contains no secrets and minimal PII

## 47.4 Indexes

* index on `(status, available_at, priority)`
* index on job type
* index on subject
* unique deduplication key where appropriate
* index on stale running jobs using heartbeat

---

# 48. `background_job_attempts`

Append-only attempt history.

Columns:

```text
id
background_job_id
attempt_number
worker_key
started_at
heartbeat_last_at
completed_at
result
failure_code
safe_error_summary
created_at
```

Unique:

```text
(background_job_id, attempt_number)
```

---

# PART XVII — PROCESSING ERROR AND ALERT TABLES

# 49. `processing_errors`

## 49.1 Purpose

Stores durable operational errors requiring investigation or workflow handling.

## 49.2 Columns

```text
id
error_code
error_category
severity
subject_type
subject_id
operation_key
correlation_id
retryable
status
safe_user_message
safe_operator_summary
first_occurred_at
last_occurred_at
occurrence_count
resolved_at
resolved_by_user_id
resolution_summary
created_at
updated_at
row_version
```

## 49.3 Status Values

```text
OPEN
ACKNOWLEDGED
RETRYING
RESOLVED
IGNORED_WITH_REASON
ESCALATED
```

## 49.4 Constraints

* Error code must exist in Error Catalog
* Occurrence count positive
* Resolution requires actor or approved system resolution
* Ignored status requires reason
* No raw secrets or provider payloads

---

# 50. `operator_alerts`

## 50.1 Purpose

Represents actionable operator-facing conditions.

## 50.2 Columns

```text
id
alert_type
severity
subject_type
subject_id
source_error_id
status
title
safe_summary
recommended_action
deduplication_key
first_detected_at
last_detected_at
acknowledged_at
acknowledged_by_user_id
resolved_at
resolved_by_user_id
resolution_summary
created_at
updated_at
row_version
```

## 50.3 Constraints

* Active deduplication where appropriate
* Acknowledgment does not require resolution
* Resolution requires summary
* No unnecessary PII

---

# PART XVIII — IDEMPOTENCY TABLES

# 51. `idempotency_records`

## 51.1 Purpose

Prevents repeated requests from creating duplicate business outcomes.

## 51.2 Columns

```text
id
scope_key
operation_key
idempotency_key
request_fingerprint
status
subject_type
subject_id
response_reference_type
response_reference_id
locked_at
completed_at
expires_at
created_at
updated_at
row_version
```

## 51.3 Status Values

```text
IN_PROGRESS
COMPLETED
FAILED_RETRYABLE
FAILED_FINAL
EXPIRED
```

## 51.4 Constraints

* Unique `(scope_key, operation_key, idempotency_key)`
* Same key with different request fingerprint must produce conflict
* Completed record must reference resulting business outcome
* Expiration policy must not allow duplicate creation for operations requiring permanent deduplication
* Canonical person creation keys may require indefinite retention

## 51.5 Indexes

* unique key scope index
* index on status
* index on expires at
* index on subject

---

# PART XIX — CONFIGURATION REFERENCE TABLES

# 52. `application_configuration`

## 52.1 Purpose

Stores non-secret runtime configuration when database-backed configuration is approved.

## 52.2 Columns

```text
id
configuration_key
value_json
value_type
environment_scope
status
effective_from
effective_until
updated_by_user_id
created_at
updated_at
row_version
```

## 52.3 Rules

* No secrets
* Configuration key unique within environment and effective range
* Changes audited
* Values validated by configuration catalog
* Sensitive credentials remain in secret management, not this table

This table is optional and should not be implemented unless runtime database-backed configuration is actually needed.

---

# PART XX — REPORTING SUPPORT

# 53. Reporting Views

Prefer database views or materialized views for aggregate reporting rather than duplicating business data.

Potential views:

```text
batch_progress_summary
page_workflow_summary
queue_depth_summary
claim_expiration_summary
transcription_throughput_summary
match_outcome_summary
promotion_status_summary
open_error_summary
operator_work_summary
```

## 53.1 Rules

* Views must derive from authoritative tables
* Views must respect authorization through application access controls
* Materialized views must document refresh behavior
* Reporting views must not expose unnecessary raw PII
* Counts must define state criteria precisely

---

# PART XXI — DATA CLASSIFICATION

# 54. Classification Levels

## `PUBLIC`

Information safe for unrestricted disclosure.

Very little People Intake operational data is public.

## `INTERNAL`

Operational information that does not contain personal data.

Examples:

* queue counts
* system status
* configuration names without values

## `CONFIDENTIAL`

Personal or operational information requiring authorized access.

Examples:

* names
* email addresses
* phone numbers
* ZIP codes
* user activity
* batch source descriptions

## `RESTRICTED`

Highly sensitive operational evidence or security information.

Examples:

* source images
* authentication identity mappings
* signed access artifacts
* security events
* detailed candidate comparisons
* bulk exports

## `SECRET`

Credentials and cryptographic secrets.

These must not be stored in ordinary application tables.

---

# 55. Table Classification Matrix

| Table                               | Classification        |
| ----------------------------------- | --------------------- |
| `application_users`                 | Confidential          |
| `user_roles`                        | Confidential          |
| `intake_batches`                    | Internal/Confidential |
| `intake_pages`                      | Confidential          |
| `storage_objects`                   | Restricted            |
| `source_images`                     | Restricted            |
| `upload_sessions`                   | Confidential          |
| `work_queue_items`                  | Confidential          |
| `work_claims`                       | Confidential          |
| `page_drafts`                       | Restricted            |
| `page_draft_revisions`              | Restricted            |
| `intake_entries`                    | Confidential          |
| `entry_submission_revisions`        | Restricted            |
| `intake_entry_fields`               | Restricted            |
| `normalized_entry_fields`           | Restricted            |
| `match_evaluations`                 | Restricted            |
| `match_candidates`                  | Restricted            |
| `match_signals`                     | Restricted            |
| `match_resolutions`                 | Restricted            |
| `promotion_requests`                | Restricted            |
| `canonical_person_links`            | Restricted            |
| `canonical_attribute_contributions` | Restricted            |
| `provenance_records`                | Restricted            |
| `audit_events`                      | Restricted            |
| `background_jobs`                   | Internal/Confidential |
| `processing_errors`                 | Confidential          |
| `operator_alerts`                   | Confidential          |
| `idempotency_records`               | Internal/Restricted   |

---

# PART XXII — REFERENTIAL ACTIONS

# 56. Foreign-Key Policy

Preferred default:

```text
ON DELETE RESTRICT
```

Use cascading delete only where the child has no independent historical value and deletion is permitted.

Because this system preserves evidence and history, cascade deletion should be rare.

---

# 57. Referential Action Matrix

| Parent              | Child               | Delete Behavior            |
| ------------------- | ------------------- | -------------------------- |
| User                | Role                | Restrict                   |
| User                | Audit Event         | Restrict                   |
| Batch               | Page                | Restrict                   |
| Page                | Source Image        | Restrict                   |
| Page                | Entry               | Restrict                   |
| Page                | Claim               | Restrict                   |
| Entry               | Submission Revision | Restrict                   |
| Submission Revision | Entry Field         | Restrict                   |
| Entry               | Match Evaluation    | Restrict                   |
| Match Evaluation    | Candidate           | Restrict                   |
| Candidate           | Signal              | Restrict                   |
| Entry               | Match Resolution    | Restrict                   |
| Resolution          | Promotion Request   | Restrict                   |
| Promotion Request   | Attempt             | Restrict                   |
| Entry               | Canonical Link      | Restrict                   |
| Any business record | Provenance          | Restrict                   |
| Any business record | Audit Event         | No direct cascading delete |

Archival should replace deletion for most parent records.

---

# PART XXIII — INDEX STRATEGY

# 58. Index Principles

Indexes should support:

* queue acquisition
* claim expiration
* page and batch navigation
* entry workflow lookup
* match review
* promotion retries
* audit reconstruction
* job execution
* error monitoring
* canonical link lookup

Indexes must not be added indiscriminately.

Every production index should document:

* query supported
* expected selectivity
* write cost
* privacy implications
* uniqueness purpose
* whether partial
* whether covering

---

# 59. Priority Indexes

High-priority indexes include:

```text
intake_pages(batch_id, page_sequence)
intake_pages(status)
intake_entries(page_id, row_position)
intake_entries(status)
work_queue_items(work_type, priority, available_at)
work_claims(expires_at) WHERE status = 'ACTIVE'
match_evaluations(entry_id, created_at)
match_resolutions(entry_id, resolution_version)
promotion_requests(status)
promotion_requests(canonical_system_key, idempotency_key)
background_jobs(status, available_at, priority)
audit_events(subject_type, subject_id, occurred_at)
provenance_records(subject_type, subject_id)
processing_errors(status, severity)
operator_alerts(status, severity)
```

---

# 60. Personal Data Indexing

Direct indexing of raw email, phone, and name values should be minimized.

Preferred matching techniques may include:

* normalized comparison columns
* salted or keyed hashes
* tokenized search keys
* restricted comparison indexes
* canonical service candidate lookup

Exact implementation will be defined later.

---

# PART XXIV — TRANSACTION SPECIFICATIONS

# 61. Claim Acquisition Transaction

Must:

1. identify eligible queue item
2. lock or atomically reserve it
3. confirm no active claim
4. create claim
5. update queue projection if needed
6. record claim history
7. record audit event where required
8. commit as one transaction

Failure must produce no active claim.

---

# 62. Draft Save Transaction

Must:

1. verify user authorization
2. verify expected draft version
3. insert immutable draft revision
4. update current draft pointer
5. increment row version
6. optionally record audit or operational event
7. commit

A stale version must not partially save.

---

# 63. Submission Transaction

Must:

1. verify current claim or authorized recovery context
2. verify expected draft revision
3. create immutable entry records as needed
4. create immutable submission revisions
5. create field records
6. update current submission pointers
7. transition entry and page state
8. release or complete claim
9. create normalization job
10. record audit event
11. commit

If any required step fails, submission must not appear complete.

---

# 64. Match Resolution Transaction

Must:

1. lock or version-check entry
2. verify reviewer authorization
3. verify current evaluation
4. insert new immutable resolution
5. supersede prior effective resolution if applicable
6. update entry effective resolution pointer
7. create promotion request or next workflow item where appropriate
8. record audit event
9. commit

---

# 65. Promotion Request Creation Transaction

Must:

1. verify effective resolution
2. compute stable idempotency identity
3. create or retrieve existing request
4. create background job if needed
5. record audit event
6. commit

External canonical operation should occur after durable local commit.

---

# 66. Promotion Completion Transaction

Must:

1. verify attempt and idempotency
2. record canonical result
3. create canonical person link if applicable
4. record attribute contributions
5. create provenance records
6. update promotion status
7. update entry status
8. record audit event
9. commit

---

# PART XXV — APPEND-ONLY POLICY

# 67. Required Append-Only Tables

The following are append-only or effectively append-only:

* `user_role_history`
* `user_access_events`
* `intake_batch_status_history`
* `intake_page_status_history`
* `upload_attempts`
* `claim_history`
* `page_draft_revisions`
* `entry_submission_revisions`
* `match_signals`
* `match_resolutions`
* `promotion_attempts`
* `canonical_attribute_contributions`
* `provenance_records`
* `audit_events`
* `background_job_attempts`

Corrections require new records rather than rewriting history.

---

# 68. Mutable Operational Tables

These may be updated under controlled concurrency:

* `application_users`
* `user_roles`
* `intake_batches`
* `intake_pages`
* `storage_objects`
* `upload_sessions`
* `work_queue_items`
* `work_claims`
* `page_drafts`
* `intake_entries`
* `normalization_runs`
* `match_evaluations`
* `promotion_requests`
* `background_jobs`
* `processing_errors`
* `operator_alerts`
* `idempotency_records`

Mutability must not erase durable history.

---

# PART XXVI — ARCHIVE AND DELETE STRATEGY

# 69. Archive Strategy

Archival should:

* remove records from active queues
* preserve relationships
* preserve audit
* preserve provenance
* preserve canonical links
* restrict ordinary editing
* remain searchable by authorized administrators
* retain required source evidence

---

# 70. Hard Delete Eligibility

Hard deletion may be considered only for:

* empty accidental draft records
* uncompleted upload placeholders with no stored evidence
* expired transient idempotency records where retention is not required
* test data in non-production environments
* legally approved destruction under formal retention policy

Hard deletion must never be used to:

* hide mistakes
* remove unfavorable audit history
* erase a resolved identity decision
* erase source evidence while canonical contributions remain
* remove user attribution

---

# PART XXVII — MIGRATION GOVERNANCE

# 71. Migration Principles

Every migration must be:

* additive where practical
* reviewed
* reversible or accompanied by recovery plan
* tested against representative data
* documented
* ordered
* environment-aware
* safe for existing records

---

# 72. Migration Package Requirements

Every future migration package must document:

```text
Migration ID
Purpose
Affected tables
Affected columns
Preconditions
Forward steps
Data transformation
Validation queries
Rollback strategy
Backup requirement
Expected locks
Expected duration
Deployment order
Application compatibility
Operator approval
```

---

# 73. Expand-and-Contract Pattern

For breaking schema changes:

1. add new structure
2. deploy compatible application logic
3. backfill
4. validate
5. switch reads
6. switch writes
7. monitor
8. remove old structure in a later approved migration

Do not combine destructive removal with the first introduction of replacement behavior.

---

# 74. Data Backfills

Backfills must be:

* restartable
* idempotent
* observable
* bounded
* auditable where business meaning changes
* capable of reporting progress
* safe under concurrent application usage

---

# PART XXVIII — SEED AND TEST DATA

# 75. Seed Data

Production seed data should be limited to approved static reference values such as:

* role keys
* status definitions if lookup tables are used
* field keys
* error categories
* audit-event catalog references

Do not seed real people.

---

# 76. Test Fixtures

Test fixtures must include:

* clean entry
* partial entry
* unreadable field
* ambiguous field
* unknown preference
* shared phone household
* duplicate email risk
* conflicting identifiers
* claim collision
* stale draft
* promotion retry
* canonical conflict
* archived batch
* disabled user
* missing image
* corrupted upload

Use fictional data only.

---

# PART XXIX — DATABASE SECURITY

# 77. Runtime Database Role

The application runtime should use a least-privilege role.

It must not have permission to:

* alter schema
* create extensions
* drop tables
* manage users
* bypass audit protections
* read unrelated databases

---

# 78. Migration Role

Schema migrations should use a separate privileged role.

Migration credentials must not be exposed to normal runtime processes.

---

# 79. Read-Only Reporting Role

A separate reporting role may be created for approved aggregate access.

It must not automatically access:

* raw source images
* raw personal fields
* authentication mappings
* secret configuration
* unrestricted audit payloads

---

# 80. Row-Level Security

Row-level security may be considered if supported by the selected platform.

It must not be assumed until explicitly designed.

If adopted, it supplements rather than replaces:

* service authorization
* role checks
* audit
* workflow validation

---

# PART XXX — DATABASE VALIDATION REQUIREMENTS

# 81. Schema Validation

Before implementation is approved, the future schema must prove:

* every table has a primary key
* every foreign key has an explicit delete action
* every enum-like field has controlled values
* every append-only table is protected
* every mutable table has concurrency strategy
* every sensitive table has classification
* every idempotent operation has durable key storage
* every current-pointer relation points to a valid owned record
* every queue item maps to authoritative workflow state
* every canonical link retains provenance

---

# 82. Integrity Test Cases

Required database-level tests include:

1. Cannot create two active claims for one queue item.
2. Cannot create two entries in the same page row.
3. Cannot mark unknown preference as no through a default.
4. Cannot attach an image from another page as active image.
5. Cannot create a match resolution for another entry’s candidate.
6. Cannot create a promotion request from an unresolved conflict.
7. Cannot duplicate canonical person creation with same idempotency key.
8. Cannot remove an entry that has provenance.
9. Cannot update an immutable submission revision.
10. Cannot create a corrected revision without lineage.
11. Cannot create active role duplicates.
12. Cannot create completed promotion without result.
13. Cannot set completed page with unusable image.
14. Cannot create canonical contribution without source entry.
15. Cannot create an audit event with both human and system actors unless explicitly supported.

---

# PART XXXI — OPEN DATABASE DECISIONS

# 83. Deferred Decisions

The following remain intentionally open for later resolution:

### `DB-DEC-001`

Exact database provider.

### `DB-DEC-002`

Exact UUID version.

### `DB-DEC-003`

Use of native database enums versus validated text or lookup tables.

### `DB-DEC-004`

Whether `user_access_events` remains separate from `audit_events`.

### `DB-DEC-005`

Whether `image_access_events` remains separate from `audit_events`.

### `DB-DEC-006`

Whether granular `entry_field_revision_history` is needed beyond immutable submission revisions.

### `DB-DEC-007`

Whether work queue items are persisted or generated dynamically.

### `DB-DEC-008`

Whether reporting uses ordinary views or materialized views.

### `DB-DEC-009`

Exact privacy-preserving matching indexes.

### `DB-DEC-010`

Exact database partitioning thresholds.

### `DB-DEC-011`

Exact retention duration for idempotency records.

### `DB-DEC-012`

Whether configuration is database-backed.

### `DB-DEC-013`

Whether row-level security is adopted.

### `DB-DEC-014`

Exact strategy for immutable-table enforcement.

### `DB-DEC-015`

Exact audit event payload validation mechanism.

These are not blockers to architectural completion.

---

# PART XXXII — LOCKED DATABASE DECISIONS

# 84. Locked Decisions

1. Relational database architecture is required.
2. Stable non-personal primary keys are required.
3. Batch, Page, and Entry are separate tables.
4. One Entry represents one physical handwritten row.
5. Page row position is unique within a page.
6. Source Images are versioned.
7. One source-image version is active per page.
8. Storage object identity is separate from source-image business identity.
9. Claims are durable records.
10. One active claim exists per work item and claim type.
11. Claim history is append-only.
12. Draft revisions are append-only.
13. Submitted entry revisions are immutable.
14. Raw fields and normalized fields are stored separately.
15. Field condition is stored independently from field value.
16. `YES`, `NO`, and `UNKNOWN` are distinct preference values.
17. No default may convert missing preference to `NO`.
18. Match Evaluations are versioned.
19. Match Candidates belong to one evaluation.
20. Match Signals are explainable and retained.
21. Match Resolutions are immutable and versioned.
22. One current effective resolution exists per entry.
23. Promotion Requests are durable and idempotent.
24. Promotion Attempts are append-only.
25. Canonical Person links are references, not locally owned identities.
26. Canonical contributions require provenance.
27. Provenance is append-only.
28. Audit Events are append-only.
29. Background Jobs and attempts are separate.
30. Operational errors and alerts are distinct concepts.
31. Archive is different from delete.
32. Critical foreign keys default to restrictive deletion.
33. Runtime and migration database roles are separate.
34. UTC-capable timestamps are required.
35. Mutable workflow records require concurrency protection.
36. Business retries require durable idempotency.
37. Raw source images are never stored directly in ordinary relational columns.
38. Secret values are not stored in normal configuration tables.
39. Reporting structures must derive from authoritative data.
40. Migrations must preserve backward compatibility where practical.

---

# PART XXXIII — TABLE REGISTRY

# 85. Canonical Table Registry

## Identity and Access

```text
application_users
user_roles
user_role_history
user_access_events
```

## Intake

```text
intake_batches
intake_batch_status_history
intake_pages
intake_page_status_history
intake_entries
entry_submission_revisions
intake_entry_fields
entry_field_revision_history
```

## Images and Uploads

```text
storage_objects
source_images
image_access_events
upload_sessions
upload_attempts
```

## Queue and Claims

```text
work_queue_items
work_claims
claim_history
```

## Drafts

```text
page_drafts
page_draft_revisions
```

## Normalization

```text
normalization_runs
normalized_entry_fields
```

## Matching

```text
match_evaluations
match_candidates
match_signals
match_evaluation_warnings
match_resolutions
duplicate_entry_links
resolution_status_history
```

## Canonical Integration

```text
promotion_requests
promotion_attempts
canonical_person_links
canonical_attribute_contributions
```

## Provenance and Audit

```text
provenance_records
provenance_links
audit_events
```

## Operations

```text
background_jobs
background_job_attempts
processing_errors
operator_alerts
idempotency_records
application_configuration
```

Some optional tables may be removed during later reconciliation if their purpose is fully covered by another approved structure.

---

# PART XXXIV — LOGICAL ENTITY RELATIONSHIP MAP

# 86. Core Relationship Flow

```text
application_users
    ├── user_roles
    ├── work_claims
    ├── page_draft_revisions
    ├── entry_submission_revisions
    ├── match_resolutions
    └── audit_events

intake_batches
    └── intake_pages
            ├── source_images
            │       └── storage_objects
            ├── work_queue_items
            │       └── work_claims
            ├── page_drafts
            │       └── page_draft_revisions
            └── intake_entries
                    ├── entry_submission_revisions
                    │       └── intake_entry_fields
                    ├── normalization_runs
                    │       └── normalized_entry_fields
                    ├── match_evaluations
                    │       ├── match_candidates
                    │       │       └── match_signals
                    │       └── match_evaluation_warnings
                    ├── match_resolutions
                    │       └── promotion_requests
                    │               ├── promotion_attempts
                    │               ├── canonical_person_links
                    │               └── canonical_attribute_contributions
                    └── provenance_records

audit_events
    └── references every meaningful business subject
```

---

# PART XXXV — VOLUME 9 READINESS

# 87. Completion Checklist

Volume 9 is complete when:

* every major domain has a database home
* source evidence remains distinct from interpretation
* immutable history is preserved
* mutable workflow state is identified
* concurrency controls are defined
* idempotency storage is defined
* canonical identity remains external
* provenance is mandatory
* audit is independent
* archive and deletion rules are explicit
* sensitive data classifications are documented
* transaction boundaries are documented
* migration governance is documented
* test fixture needs are documented
* open implementation decisions are separated from locked architecture

---

# 88. Readiness Score

| Area                    | Readiness |
| ----------------------- | --------: |
| Logical entity coverage |      100% |
| Table ownership         |       98% |
| Key strategy            |       98% |
| Relationship design     |       98% |
| Constraint design       |       96% |
| Index strategy          |       94% |
| Append-only history     |      100% |
| Concurrency             |       98% |
| Idempotency             |      100% |
| Canonical boundaries    |      100% |
| Provenance              |      100% |
| Audit                   |      100% |
| Privacy classification  |       98% |
| Retention and archive   |       96% |
| Migration governance    |       98% |
| Reporting support       |       92% |

**Overall Volume 9 Design Readiness**

```text
98%
```

The remaining percentage is reserved for reconciliation with:

* Volume 10 — API Specifications
* State Machine Catalog
* Error Catalog
* Audit Event Catalog
* Configuration Catalog
* Cross-Volume Traceability Matrix

---

# 89. Next Governing Build

The next documentation build is:

```text
PEOPLE-VOLUME-10-API-SPECIFICATIONS-1.0
```

Volume 10 will define:

* every endpoint
* request contracts
* response contracts
* authentication requirements
* authorization requirements
* validation rules
* error codes
* idempotency
* transaction behavior
* concurrency tokens
* audit events
* rate limits
* pagination
* retry behavior
* example payloads
* versioning and deprecation

No API handlers or production implementation should be created during Volume 10.

The next build is **Volume 10 — API Specifications**. It will convert these tables and domain rules into exact contracts so Cursor will never need to invent endpoint behavior during implementation.

---

## Document Control

| Field | Value |
| --- | --- |
| Canonical path | `docs/volumes/volume-09-database-specifications/VOLUME_09_DATABASE_SPECIFICATIONS.md` |
| Legacy pointer | `docs/10_database_specifications/VOLUME_09_DATABASE_SPECIFICATIONS.md` |
| Encoding | UTF-8 |
| Status | DESIGN COMPLETE — PENDING CROSS-VOLUME VALIDATION |
| Build mode | DOCUMENTATION ONLY — no SQL migrations |
