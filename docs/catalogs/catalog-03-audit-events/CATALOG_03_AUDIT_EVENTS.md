# PEOPLE INTAKE SYSTEM

# CATALOG 3 — AUDIT EVENT CATALOG

**Document ID**

```text
PEOPLE-CATALOG-03-AUDIT-EVENTS-1.0
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
CANONICAL AUDIT EVENT CONTRACT AND FOUNDATION
```

**Build Mode**

```text
DOCUMENTATION ONLY
```

**Prohibited During This Catalog**

* No audit persistence implementation
* No database migrations
* No API handlers or middleware
* No logging or alerting implementation
* No UI components
* No dependency installation
* No production audit payloads
* No inventing undocumented production event names outside this catalog and its approved amendments

**Foundation Scope**

This document establishes the governing audit contract: principles, standard fields, naming, domains, entry template, privacy, correlation, retention hooks, testing, and traceability.

It includes seeded example event definitions. Additional event entries must be added through formal catalog amendments under this contract and must not contradict Volumes 0–13, Catalog 1, or Catalog 2.

---

# PART I — PURPOSE

## 1. Mission

The Audit Event Catalog defines every immutable event that may be recorded by the People Intake System.

The audit system exists to answer questions such as:

* Who performed an action?
* What changed?
* When did it occur?
* Why did it occur?
* What object was affected?
* What was the previous state?
* What was the resulting state?
* Was the action successful?
* What evidence supports the action?

Audit history is intended for accountability, traceability, compliance, and operational investigation—not application logic.

---

# PART II — AUDIT PRINCIPLES

## 2. Core Principles

### `AUDIT-PRINCIPLE-001 — Immutability`

Every audit event must be immutable after write.

### `AUDIT-PRINCIPLE-002 — Time-Stamped`

Every audit event must carry an authoritative occurred-at timestamp in UTC.

### `AUDIT-PRINCIPLE-003 — Actor Attribution`

Every audit event must be attributed to an actor (human or system).

### `AUDIT-PRINCIPLE-004 — Correlation`

Every audit event must be correlated to a request or workflow.

### `AUDIT-PRINCIPLE-005 — Resource Linkage`

Every audit event must be linked to the affected resource where applicable.

### `AUDIT-PRINCIPLE-006 — Versioned Contract`

Every audit event type is versioned; released names remain permanent.

### `AUDIT-PRINCIPLE-007 — Searchable`

Audit records must remain searchable for investigation and compliance.

### `AUDIT-PRINCIPLE-008 — Append-Only`

Audit records are append-only and must never be silently modified or deleted.

### `AUDIT-PRINCIPLE-009 — Not Application Logic`

Audit history supports accountability and investigation; it must not be used as the primary business-rule engine.

### `AUDIT-PRINCIPLE-010 — Catalog Authority`

No auditable production action may exist without a corresponding catalog entry or approved amendment.

Every audit event must be:

* Immutable
* Time-stamped
* Attributed to an actor (human or system)
* Correlated to a request or workflow
* Linked to the affected resource
* Versioned
* Searchable
* Never silently modified or deleted

Audit records are append-only.

---

# PART III — STANDARD EVENT CONTRACT

Every audit event contains the following fields:

```text
Event ID
Canonical Event Name
Event Version
Occurred At (UTC)
Correlation ID
Actor Type
Actor ID
Actor Display Name
Resource Type
Resource ID
Previous State
New State
Outcome
Reason Code
Source (UI/API/System)
Related Batch
Related Page
Related Entry
Metadata
```

Optional fields include:

```text
Client Version
IP Address (if policy allows)
Session ID
Job ID
Idempotency Key
```

---

# PART IV — EVENT NAMING

Canonical event names use uppercase snake case.

Examples:

```text
USER_INVITED
USER_ACTIVATED
ROLE_GRANTED
BATCH_CREATED
PAGE_SUBMITTED
CLAIM_ACQUIRED
CLAIM_RELEASED
MATCH_REVIEW_COMPLETED
PROMOTION_SUCCEEDED
AUDIT_WRITE_FAILED
EXPORT_DOWNLOADED
```

Names are permanent once released.

---

# PART V — EVENT DOMAINS

Events are grouped by domain:

```text
AUTHENTICATION
USER_MANAGEMENT
ROLE_MANAGEMENT
BATCH
PAGE
UPLOAD
IMAGE
QUEUE
CLAIM
DRAFT
TRANSCRIPTION
MATCHING
RESOLUTION
PROMOTION
CANONICAL_INTEGRATION
BACKGROUND_JOBS
REPORTING
EXPORT
CONFIGURATION
SECURITY
AUDIT
SYSTEM
```

---

# PART VI — EVENT TEMPLATE

Each event definition contains:

```text
Event ID
Canonical Name
Domain
Description
Trigger
Required Actor
Required Resource
Required Metadata
Required Reason Codes
Related State Transition
Related Error Codes
Privacy Classification
Retention Class
Alert Requirements
Required Tests
```

---

# PART VII — SEEDED EXAMPLE EVENTS

The following entries are canonical seeds under this contract. Further events must follow the same template.

## USER_INVITED

**Event ID**

```text
AUDIT-USER-001
```

**Canonical Name**

```text
USER_INVITED
```

**Domain**

```text
USER_MANAGEMENT
```

**Trigger**

A new user invitation is successfully created.

**Required Metadata**

* invited user identifier
* inviter
* assigned roles
* invitation expiration

---

## CLAIM_ACQUIRED

**Event ID**

```text
AUDIT-CLAIM-001
```

**Canonical Name**

```text
CLAIM_ACQUIRED
```

**Domain**

```text
CLAIM
```

**Trigger**

A user successfully claims work from the queue.

**Metadata**

* queue item
* claim duration
* page identifier

---

## PAGE_SUBMITTED

**Event ID**

```text
AUDIT-PAGE-001
```

**Canonical Name**

```text
PAGE_SUBMITTED
```

**Domain**

```text
PAGE
```

**Trigger**

A transcription revision is submitted.

**Metadata**

* revision number
* entry count
* claim owner
* submission version

---

## MATCH_RESOLUTION_FINALIZED

**Event ID**

```text
AUDIT-MATCH-001
```

**Canonical Name**

```text
MATCH_RESOLUTION_FINALIZED
```

**Domain**

```text
RESOLUTION
```

**Trigger**

A reviewer finalizes a match decision.

**Metadata**

* selected outcome
* reviewer
* confidence summary
* candidate reference (if applicable)

---

## PROMOTION_SUCCEEDED

**Event ID**

```text
AUDIT-PROMOTION-001
```

**Canonical Name**

```text
PROMOTION_SUCCEEDED
```

**Domain**

```text
PROMOTION
```

**Trigger**

A promotion completes successfully.

**Metadata**

* promotion identifier
* canonical person identifier
* provenance reference
* idempotency key

---

## SECURITY_ACCESS_DENIED

**Event ID**

```text
AUDIT-SECURITY-001
```

**Canonical Name**

```text
SECURITY_ACCESS_DENIED
```

**Domain**

```text
SECURITY
```

**Trigger**

A protected action is denied because of insufficient authorization.

**Metadata**

* requested action
* required permission
* resource type

---

# PART VIII — REASON CODES

Reason codes are cataloged separately but referenced by audit events.

Examples include:

```text
USER_REQUEST
ADMIN_ACTION
SECURITY_POLICY
CLAIM_EXPIRED
WORK_COMPLETED
IMAGE_REPLACED
RETURNED_FOR_CORRECTION
MATCH_CONFLICT
PROMOTION_RETRY
SYSTEM_RECOVERY
```

Detailed reason-code expansion remains aligned with Catalog 1 reason families and Catalog 2 error recovery language.

---

# PART IX — PRIVACY

Audit events must never store:

* passwords
* authentication tokens
* session secrets
* full uploaded images
* raw document scans
* unredacted sensitive values unless explicitly required by policy

Audit metadata should contain references rather than copies whenever possible.

---

# PART X — CORRELATION

Every audit event must support:

* Correlation ID
* Parent workflow identifier (when applicable)
* Request identifier
* Background job identifier (when applicable)

This enables reconstruction of an entire workflow across multiple services.

---

# PART XI — RETENTION

Each event is assigned a retention class by the Data Retention Catalog.

Example classes:

```text
Operational
Compliance
Security
Legal Hold Eligible
Permanent
```

---

# PART XII — REQUIRED TESTS

Every audit event definition requires tests verifying:

* Event is generated when expected
* Event is not generated when prohibited
* Required metadata is present
* Correlation ID is attached
* Immutable storage behavior
* Privacy rules are enforced
* Correct state transition linkage
* Correct actor attribution
* Correct timestamp generation

---

# PART XIII — TRACEABILITY

Every event maps to:

* State Machine
* API Endpoint
* Database Entity
* UI Workflow
* Permission
* Error Code
* Test Suite

No auditable action may exist without a corresponding catalog entry.

---

# PART XIV — LOCKED AUDIT DECISIONS

## Locked Decisions

1. Audit records are append-only.
2. Released canonical event names are permanent.
3. Every significant auditable action requires a cataloged event.
4. Audit is for accountability and investigation, not primary business logic.
5. Every event carries a correlation identifier.
6. Every event is attributed to a human or system actor.
7. Secrets and tokens never appear in audit payloads.
8. Full source images never appear in audit payloads.
9. Metadata prefers references over copies of personal data.
10. Event types are versioned.
11. Privacy classification is required on each event definition.
12. Retention class is assigned via the Retention Catalog.
13. Seeded example events in this catalog are authoritative.
14. Additional events require formal catalog amendment under this contract.
15. No audit implementation may invent undocumented production event names.

---

# PART XV — READINESS

| Area             | Readiness |
| ---------------- | --------: |
| Event Contract   |      100% |
| Naming Standard  |      100% |
| Domains          |      100% |
| Privacy Rules    |      100% |
| Correlation      |      100% |
| Retention Hooks  |       95% |
| Traceability     |       95% |
| Required Testing |      100% |
| Seeded Examples  |      100% |
| Full Event Inventory Expansion | Foundation ready — entries via amendment |

**Overall Catalog 3 Foundation Readiness**

```text
98%
```

The remaining percentage is reserved for:

* full event inventory expansion under this contract
* Configuration Catalog thresholds and related settings
* Permission Catalog actor/permission linkage
* Data Retention Catalog class finalization
* Cross-Volume Traceability Matrix

---

# PART XVI — NEXT CATALOG

## Next Catalog

```text
PEOPLE-CATALOG-04-CONFIGURATION-1.0
```

This catalog will define every environment variable, feature flag, timeout, retry policy, upload limit, secret classification, and runtime configuration used anywhere in the platform.

At this point, the documentation library consists of:

1. Master Build Plan
2. Volumes 0–13
3. Catalog 0 – Master Registry
4. Catalog 1 – State Machines
5. Catalog 2 – Error Catalog
6. Catalog 3 – Audit Event Catalog (foundation)

The next logical document is **Catalog 4 – Configuration**, which becomes the single source of truth for every environment variable, feature flag, storage setting, timeout, retry policy, upload limit, and deployment configuration used throughout the system.

No application code is authorized during the catalog sequence.
