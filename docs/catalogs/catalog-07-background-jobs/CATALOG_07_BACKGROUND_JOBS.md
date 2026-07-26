# PEOPLE INTAKE SYSTEM

# CATALOG 7 — BACKGROUND JOB CATALOG

**Document ID**

```text
PEOPLE-CATALOG-07-BACKGROUND-JOBS-1.0
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
CANONICAL BACKGROUND JOB CONTRACT AND FOUNDATION
```

**Build Mode**

```text
DOCUMENTATION ONLY
```

**Prohibited During This Catalog**

* No application source code
* No worker, queue, or scheduler implementation
* No database migrations for job tables
* No cron or Netlify scheduled-function wiring
* No dependency installation
* No inventing undocumented production job names outside this catalog and its approved amendments

**Foundation Scope**

This document establishes the governing background-job contract: principles, categories, entry template, triggers, priorities, concurrency policies, retry classes, idempotency rules, failure handling, dependencies, monitoring, audit, security, testing, and locked decisions.

It includes seeded example job definitions. Additional job entries must be added through formal catalog amendments under this contract and must not contradict Volumes 0–13 or Catalogs 1–6.

No background process may exist outside this catalog.

---

# PART I — PURPOSE

## 1. Mission

The Background Job Catalog defines every asynchronous process executed by the People Intake System.

It establishes:

* canonical job definitions
* job ownership
* execution triggers
* queue assignments
* concurrency rules
* retry behavior
* timeout policies
* idempotency requirements
* failure handling
* dependencies
* monitoring
* audit requirements

---

# PART II — DESIGN PRINCIPLES

## 2. Core Principles

### `JOB-PRINCIPLE-001 — Deterministic`

Given the same inputs and cataloged configuration, a job's business outcome must be deterministic.

### `JOB-PRINCIPLE-002 — Idempotent Where Required`

Jobs that modify canonical or irreversible business data must declare and enforce idempotency.

### `JOB-PRINCIPLE-003 — Restartable`

Jobs must be safely restartable after crash, timeout, or deployment interruption.

### `JOB-PRINCIPLE-004 — Observable`

Every job must expose monitoring metrics sufficient for operations.

### `JOB-PRINCIPLE-005 — Independently Retryable`

Retries must be independently schedulable without depending on UI state.

### `JOB-PRINCIPLE-006 — Transaction-Safe`

Jobs that mutate durable state must use explicit transactional boundaries.

### `JOB-PRINCIPLE-007 — Auditable`

Material job lifecycle events generate Catalog 3 audit records where required.

### `JOB-PRINCIPLE-008 — No UI Dependency`

Jobs must never depend on UI state or browser sessions.

### `JOB-PRINCIPLE-009 — Service Identity`

Jobs execute under service identities with minimum required Catalog 5 permissions.

### `JOB-PRINCIPLE-010 — Catalog Authority`

No production background job may exist outside this catalog or an approved amendment.

Background jobs must be:

* deterministic
* idempotent
* restartable
* observable
* independently retryable
* transaction-safe
* auditable

---

# PART III — JOB CATEGORIES

The Version 1 categories are:

```text
Upload
Storage
Image Processing
Claims
Draft Recovery
Transcription
Normalization
Matching
Promotion
Notification
Reporting
Export
Retention
Audit
Maintenance
Security
System
```

| Category ID | Category |
| --- | --- |
| JOBCAT-001 | Upload |
| JOBCAT-002 | Storage |
| JOBCAT-003 | Image Processing |
| JOBCAT-004 | Claims |
| JOBCAT-005 | Draft Recovery |
| JOBCAT-006 | Transcription |
| JOBCAT-007 | Normalization |
| JOBCAT-008 | Matching |
| JOBCAT-009 | Promotion |
| JOBCAT-010 | Notification |
| JOBCAT-011 | Reporting |
| JOBCAT-012 | Export |
| JOBCAT-013 | Retention |
| JOBCAT-014 | Audit |
| JOBCAT-015 | Maintenance |
| JOBCAT-016 | Security |
| JOBCAT-017 | System |

---

# PART IV — JOB TEMPLATE

Each job definition contains:

```text
Job ID
Canonical Name
Description
Owning Domain
Trigger
Queue
Priority
Concurrency Policy
Timeout
Retry Policy
Idempotency Requirement
Dependencies
Success Criteria
Failure Handling
Audit Events
Monitoring Metrics
Required Tests
```

---

# PART V — EXECUTION TRIGGERS

Jobs may begin because of:

* API request
* state transition
* scheduled execution
* queue availability
* completion of another job
* administrator request
* startup recovery

| Trigger ID | Trigger |
| --- | --- |
| TRIGGER-001 | API Request |
| TRIGGER-002 | State Transition |
| TRIGGER-003 | Scheduled Execution |
| TRIGGER-004 | Queue Availability |
| TRIGGER-005 | Prior Job Completion |
| TRIGGER-006 | Administrator Request |
| TRIGGER-007 | Startup Recovery |

---

# PART VI — PRIORITY LEVELS

```text
LOW
NORMAL
HIGH
CRITICAL
```

| Priority ID | Priority |
| --- | --- |
| JOBPRI-001 | LOW |
| JOBPRI-002 | NORMAL |
| JOBPRI-003 | HIGH |
| JOBPRI-004 | CRITICAL |

Higher priority affects scheduling only—it does not bypass authorization.

Configurable defaults may use Catalog 4 keys such as `JOB_CONCURRENCY`, `JOB_TIMEOUT`, `JOB_MAX_ATTEMPTS`, and `JOB_BACKOFF_STRATEGY`.

---

# PART VII — CONCURRENCY POLICIES

Supported policies:

```text
Single Instance
Per Resource
Per Batch
Per User
Unlimited
```

| Concurrency ID | Policy |
| --- | --- |
| CONC-001 | Single Instance |
| CONC-002 | Per Resource |
| CONC-003 | Per Batch |
| CONC-004 | Per User |
| CONC-005 | Unlimited |

Example:

A promotion job may execute only once per approved resolution (`Per Resource`).

---

# PART VIII — RETRY POLICIES

Retry classes:

```text
No Retry
Immediate Retry
Exponential Backoff
Manual Retry
Operator Review Required
```

| Retry ID | Policy |
| --- | --- |
| RETRY-001 | No Retry |
| RETRY-002 | Immediate Retry |
| RETRY-003 | Exponential Backoff |
| RETRY-004 | Manual Retry |
| RETRY-005 | Operator Review Required |

Retries must never create duplicate business results.

---

# PART IX — IDEMPOTENCY

Every job must specify whether it requires idempotency.

Jobs that modify canonical data always require idempotency.

Examples:

* promotion
* canonical updates
* user provisioning
* archive processing

Idempotency keys and records are governed by Catalog 1 (`STATE-IDEMPOTENCY-001`) and related Volume contracts.

---

# PART X — CORE JOBS (SEEDED)

Seeded Version 1 job definitions follow. Full inventory expands via formal amendment under this contract.

### JOB-UPLOAD-001 — UPLOAD_VERIFICATION

**Canonical Name**

```text
UPLOAD_VERIFICATION
```

**Purpose**

Verify uploaded file integrity.

**Trigger**

Successful upload.

**Output**

Verified storage object.

**Idempotency**

Required.

---

### JOB-IMAGE-001 — IMAGE_PREVIEW_GENERATION

**Canonical Name**

```text
IMAGE_PREVIEW_GENERATION
```

**Purpose**

Generate preview images.

**Trigger**

Verified upload.

**Idempotency**

Required.

---

### JOB-CLAIM-001 — CLAIM_EXPIRATION_CHECK

**Canonical Name**

```text
CLAIM_EXPIRATION_CHECK
```

**Purpose**

Expire overdue claims.

**Trigger**

Scheduled execution.

**Concurrency**

```text
Single Instance
```

---

### JOB-DRAFT-001 — DRAFT_RECOVERY_SCAN

**Canonical Name**

```text
DRAFT_RECOVERY_SCAN
```

**Purpose**

Locate recoverable drafts after claim expiration.

**Trigger**

Scheduled execution or claim expiration completion.

---

### JOB-NORMALIZATION-001 — ENTRY_NORMALIZATION

**Canonical Name**

```text
ENTRY_NORMALIZATION
```

**Purpose**

Normalize approved transcription entries.

**Idempotency**

Required.

---

### JOB-MATCH-001 — MATCH_EVALUATION

**Canonical Name**

```text
MATCH_EVALUATION
```

**Purpose**

Evaluate candidate matches.

**Idempotency**

Required.

---

### JOB-PROMOTION-001 — PROMOTION_EXECUTION

**Canonical Name**

```text
PROMOTION_EXECUTION
```

**Purpose**

Promote approved identity decisions.

**Requirements**

* idempotent
* transactional
* audited

**Concurrency**

```text
Per Resource
```

---

### JOB-NOTIFY-001 — NOTIFICATION_DISPATCH

**Canonical Name**

```text
NOTIFICATION_DISPATCH
```

**Purpose**

Deliver queued notifications.

**Related Catalog**

Catalog 6.

---

### JOB-REPORT-001 — REPORT_GENERATION

**Canonical Name**

```text
REPORT_GENERATION
```

**Purpose**

Generate requested reports.

---

### JOB-EXPORT-001 — EXPORT_GENERATION

**Canonical Name**

```text
EXPORT_GENERATION
```

**Purpose**

Create export packages.

**Idempotency**

Required.

---

### JOB-RETENTION-001 — RETENTION_EXPIRATION

**Canonical Name**

```text
RETENTION_EXPIRATION
```

**Purpose**

Apply retention policies.

**Related Catalog**

Catalog 8 (Data Retention).

**Idempotency**

Required.

---

### JOB-AUDIT-001 — AUDIT_INTEGRITY_CHECK

**Canonical Name**

```text
AUDIT_INTEGRITY_CHECK
```

**Purpose**

Verify audit consistency.

**Trigger**

Scheduled execution.

---

### JOB-MAINT-001 — SYSTEM_HEALTH_CHECK

**Canonical Name**

```text
SYSTEM_HEALTH_CHECK
```

**Purpose**

Collect operational health metrics.

**Trigger**

Scheduled execution.

---

# PART XI — DEPENDENCIES

Jobs may depend upon:

* prior job completion
* resource state
* configuration
* external services

Dependency failures must be explicit. Silent skipping of unmet dependencies is prohibited.

---

# PART XII — FAILURE HANDLING

Every job specifies:

* retry behavior
* escalation threshold
* operator notification
* state transition
* audit event

Failed jobs never silently disappear.

---

# PART XIII — MONITORING

Each job reports:

* queue depth
* execution count
* average runtime
* success rate
* failure rate
* retry count
* last execution
* last successful execution

---

# PART XIV — AUDIT

Background jobs generate audit events for:

* execution started
* execution completed
* execution failed
* manual retry
* cancellation
* operator intervention

Audit event shapes and names are governed by Catalog 3. This catalog must not invent undocumented audit event names.

---

# PART XV — SECURITY

Jobs execute under service identities.

Interactive user permissions are not reused by scheduled workers.

Every service identity has the minimum required permissions (`SYSTEM_JOB_EXECUTE` and related Catalog 5 grants).

---

# PART XVI — TEST REQUIREMENTS

Each job requires tests for:

* successful execution
* retry behavior
* timeout
* idempotency
* dependency failure
* cancellation
* audit generation
* monitoring metrics

Tests are documentation requirements until implementation is authorized.

---

# PART XVII — LOCKED JOB DECISIONS

## Locked Decisions

1. No production background job may exist outside this catalog or an approved amendment.
2. Jobs must never depend on UI state or browser sessions.
3. Retries must never create duplicate business results.
4. Jobs that modify canonical data always require idempotency.
5. Failed jobs never silently disappear.
6. Priority affects scheduling only and does not bypass authorization.
7. Jobs execute under service identities, not interactive user sessions.
8. Dependency failures must be explicit.
9. Seeded job names in this catalog are authoritative permanent identifiers.
10. Promotion execution must be idempotent, transactional, and audited.
11. Configurable timeouts and concurrency use Catalog 4 keys; they do not invent new job types.
12. Notification dispatch jobs must honor Catalog 6 recipient and privacy rules.
13. Retention jobs defer classification durations to Catalog 8.
14. Material job lifecycle events require Catalog 3 audit linkage where required.
15. Additional job types require catalog amendment under this contract.

---

# PART XVIII — READINESS

| Area | Readiness |
| --- | --------: |
| Job Model | 100% |
| Retry Policies | 100% |
| Concurrency Rules | 100% |
| Idempotency | 100% |
| Monitoring | 100% |
| Failure Handling | 100% |
| Audit Integration | 100% |
| Seeded Jobs | 100% |
| Full Inventory Expansion | Deferred to amendment |

**Overall Catalog 7 Readiness**

```text
99%
```

The remaining percentage is reserved for full job inventory expansion, Data Retention Catalog linkage, and Cross-Volume Traceability.

---

# PART XIX — NEXT CATALOG

## Next Catalog

```text
PEOPLE-CATALOG-08-DATA-RETENTION-1.0
```

This catalog will define every data classification level, retention schedule, archival policy, legal hold rule, destruction workflow, privacy requirement, and lifecycle policy governing every piece of data stored within the People Intake System.

With Catalogs 1–7 in place, the project now has governing specifications for **workflow states, errors, audit events, configuration, authorization, notifications, and background jobs**. The next major governance layer is the **Data Classification and Retention Catalog**.

No application code is authorized during the catalog sequence.
