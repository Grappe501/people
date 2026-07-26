# PEOPLE INTAKE SYSTEM

# CATALOG 8 — DATA CLASSIFICATION & RETENTION CATALOG

**Document ID**

```text
PEOPLE-CATALOG-08-DATA-RETENTION-1.0
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
CANONICAL DATA CLASSIFICATION AND RETENTION CONTRACT AND FOUNDATION
```

**Build Mode**

```text
DOCUMENTATION ONLY
```

**Prohibited During This Catalog**

* No application source code
* No archival or destruction workers
* No database migrations for retention tables
* No production data deletion
* No dependency installation
* No inventing undocumented production retention rules or classification levels outside this catalog and its approved amendments

**Foundation Scope**

This document establishes the governing data classification and retention contract: principles, classification levels, domains, retention entry template, lifecycle states, archival, legal hold, destruction, recovery, privacy, audit, monitoring, testing, governance, and locked decisions.

It includes seeded domain retention examples. Additional retention rules and exact durations must be added through formal catalog amendments under this contract and must not contradict Volumes 0–13 or Catalogs 1–7. Configurable durations may reference Catalog 4 keys; classification and lifecycle language remain authoritative here.

No persistent data may exist without a documented lifecycle.

---

# PART I — PURPOSE

## 1. Mission

This catalog defines how every category of data in the People Intake System is classified, retained, archived, protected, and ultimately destroyed.

It establishes:

* data classification levels
* ownership
* retention schedules
* archival policies
* destruction requirements
* legal hold procedures
* privacy controls
* recovery expectations
* audit requirements

---

# PART II — DESIGN PRINCIPLES

## 2. Core Principles

### `RETAIN-PRINCIPLE-001 — Classify Before Storage`

Information is classified before durable storage.

### `RETAIN-PRINCIPLE-002 — Retain Only as Necessary`

Data is retained only as long as necessary for operations, compliance, and documented policy.

### `RETAIN-PRINCIPLE-003 — Recoverable When Required`

Eligible data remains recoverable within its documented recovery window.

### `RETAIN-PRINCIPLE-004 — Protect by Sensitivity`

Protections match classification; stronger classes never receive weaker controls by default.

### `RETAIN-PRINCIPLE-005 — Documented Disposal`

Disposal occurs only through documented destruction processes.

### `RETAIN-PRINCIPLE-006 — Traceable Lifecycle`

Lifecycle actions are traceable through Catalog 3 audit records where required.

### `RETAIN-PRINCIPLE-007 — Deterministic Retention`

Retention policies are deterministic and consistently enforced.

### `RETAIN-PRINCIPLE-008 — Legal Hold Suspends Destruction`

Legal hold prohibits destruction and suspends retention timers for affected resources.

### `RETAIN-PRINCIPLE-009 — No Silent Policy Drift`

Existing data must not silently change lifecycle rules without governance approval.

### `RETAIN-PRINCIPLE-010 — Catalog Authority`

No production classification level or retention rule may exist outside this catalog or an approved amendment.

The data lifecycle must ensure that information is:

* classified before storage
* retained only as long as necessary
* recoverable when required
* protected according to sensitivity
* disposed of through documented processes
* traceable through audit records

---

# PART III — DATA CLASSIFICATION LEVELS

Each stored item is assigned one classification.

```text
PUBLIC
INTERNAL
CONFIDENTIAL
RESTRICTED
SYSTEM_SECRET
```

### CLASS-001 — PUBLIC

Information intentionally suitable for public disclosure.

Examples:

* public documentation
* published reports

### CLASS-002 — INTERNAL

Operational information intended for authorized users.

Examples:

* workflow metadata
* queue metrics

### CLASS-003 — CONFIDENTIAL

Business data requiring controlled access.

Examples:

* transcription work
* review notes
* operational history

### CLASS-004 — RESTRICTED

Highly sensitive data requiring the strongest protections.

Examples:

* personally identifiable information
* authentication metadata
* privileged administrative records

### CLASS-005 — SYSTEM_SECRET

Sensitive technical secrets.

Examples:

* encryption keys
* API credentials
* database connection secrets

---

# PART IV — DATA DOMAINS

Retention rules are organized by domain.

```text
Users
Roles
Authentication
Audit
Configuration
Uploads
Images
Batches
Pages
Claims
Drafts
Transcription
Normalization
Matching
Resolution
Promotion
Reports
Exports
Notifications
Jobs
Logs
System Metadata
```

| Domain ID | Domain |
| --- | --- |
| DOMAIN-001 | Users |
| DOMAIN-002 | Roles |
| DOMAIN-003 | Authentication |
| DOMAIN-004 | Audit |
| DOMAIN-005 | Configuration |
| DOMAIN-006 | Uploads |
| DOMAIN-007 | Images |
| DOMAIN-008 | Batches |
| DOMAIN-009 | Pages |
| DOMAIN-010 | Claims |
| DOMAIN-011 | Drafts |
| DOMAIN-012 | Transcription |
| DOMAIN-013 | Normalization |
| DOMAIN-014 | Matching |
| DOMAIN-015 | Resolution |
| DOMAIN-016 | Promotion |
| DOMAIN-017 | Reports |
| DOMAIN-018 | Exports |
| DOMAIN-019 | Notifications |
| DOMAIN-020 | Jobs |
| DOMAIN-021 | Logs |
| DOMAIN-022 | System Metadata |

---

# PART V — RETENTION ENTRY TEMPLATE

Each retention rule documents:

```text
Retention ID
Domain
Data Type
Classification
Owner
Retention Trigger
Retention Period
Archive Required
Archive Location
Legal Hold Eligible
Destruction Method
Recovery Window
Audit Requirements
```

Exact retention periods may use Catalog 4 duration keys (for example `DRAFT_RETENTION_PERIOD`, `LOG_RETENTION_DAYS`, `AUDIT_RETENTION_CLASS`) but must map to cataloged retention entries here.

---

# PART VI — RETENTION STATES

Every retained record progresses through lifecycle states.

```text
ACTIVE
ARCHIVED
LEGAL_HOLD
PENDING_DESTRUCTION
DESTROYED
```

| State ID | State |
| --- | --- |
| RSTATE-001 | ACTIVE |
| RSTATE-002 | ARCHIVED |
| RSTATE-003 | LEGAL_HOLD |
| RSTATE-004 | PENDING_DESTRUCTION |
| RSTATE-005 | DESTROYED |

State transitions must be auditable. Related archival machine language is also governed by Catalog 1 (`STATE-ARCHIVE-001`) where applicable.

---

# PART VII — ARCHIVAL

Archival rules specify:

* when data becomes inactive
* archival storage requirements
* retrieval expectations
* integrity verification
* restoration authorization

Archived data remains protected according to its classification.

---

# PART VIII — LEGAL HOLD

Legal hold suspends normal destruction.

A legal hold records:

* initiating authority
* reason
* start date
* release date
* affected resources

While under legal hold:

* destruction is prohibited
* retention timers are suspended
* all actions remain auditable

---

# PART IX — DESTRUCTION

Destruction policies define:

* eligibility
* approval requirements
* destruction method
* verification
* audit event generation

Destruction must be irreversible when required by policy. Completed retention destruction cannot be overridden by Catalog 5 administrative override.

---

# PART X — RECOVERY

Recovery expectations specify:

* eligible data
* recovery window
* authorization required
* restoration process
* audit requirements

Not all destroyed data is recoverable.

---

# PART XI — DOMAIN EXAMPLES (SEEDED)

Seeded Version 1 retention examples follow. Full per-type inventory and exact durations expand via formal amendment under this contract.

### RETAIN-AUDIT-001 — Audit Records

**Domain**

```text
Audit
```

**Classification**

```text
CONFIDENTIAL
```

**Archive**

Yes.

**Legal Hold**

Eligible.

**Destruction**

Controlled by policy.

---

### RETAIN-DRAFT-001 — Drafts

**Domain**

```text
Drafts
```

**Classification**

```text
CONFIDENTIAL
```

**Archive**

Optional.

**Recovery**

Supported during configured recovery window.

---

### RETAIN-IMAGE-001 — Uploaded Images

**Domain**

```text
Images
```

**Classification**

```text
CONFIDENTIAL
```

**Archive**

Yes.

**Integrity**

Integrity verification required before restoration.

---

### RETAIN-SECRET-001 — Authentication Secrets

**Domain**

```text
Authentication
```

**Classification**

```text
SYSTEM_SECRET
```

**Archive**

No.

**Destruction**

Destruction follows secure secret rotation procedures.

---

# PART XII — PRIVACY

Sensitive information must receive protections appropriate to its classification.

Examples include:

* access restrictions
* encryption where applicable
* least-privilege access
* secure handling during export
* secure destruction

Authorization remains governed by Catalog 5. Classification does not grant access by itself.

---

# PART XIII — AUDIT

The following lifecycle events generate audit records:

* archive
* restore
* legal hold applied
* legal hold released
* destruction requested
* destruction approved
* destruction completed
* recovery performed

Audit event shapes and names are governed by Catalog 3. This catalog must not invent undocumented audit event names.

---

# PART XIV — MONITORING

Operational metrics include:

* archived record counts
* pending destruction counts
* legal hold inventory
* recovery requests
* destruction failures
* retention exceptions

Background retention execution is governed by Catalog 7 (`RETENTION_EXPIRATION`).

---

# PART XV — TEST REQUIREMENTS

Each retention rule requires tests verifying:

* correct classification
* correct retention state transitions
* archival behavior
* legal hold suspension
* destruction eligibility
* recovery authorization
* audit generation
* monitoring metrics

Tests are documentation requirements until implementation is authorized.

---

# PART XVI — GOVERNANCE

Changes to retention policy require:

* documented approval
* version update
* audit record
* review of affected systems

Existing data must not silently change lifecycle rules.

---

# PART XVII — LOCKED RETENTION DECISIONS

## Locked Decisions

1. No persistent data may exist without a documented lifecycle.
2. Information is classified before durable storage.
3. Retention policies are deterministic and consistently enforced.
4. Legal hold prohibits destruction and suspends retention timers.
5. Destruction must be irreversible when required by policy.
6. Not all destroyed data is recoverable.
7. Archived data remains protected according to its classification.
8. Existing data must not silently change lifecycle rules.
9. SYSTEM_SECRET data is not archived into ordinary archival stores.
10. Seeded retention examples in this catalog are authoritative starting points for amendment.
11. Exact durations may use Catalog 4 keys but must map to cataloged retention entries.
12. Classification does not grant access; Catalog 5 remains authoritative for authorization.
13. Completed retention destruction cannot be overridden administratively.
14. Material lifecycle events require Catalog 3 audit linkage where required.
15. Additional classification levels and retention rules require catalog amendment under this contract.

---

# PART XVIII — READINESS

| Area | Readiness |
| --- | --------: |
| Classification Model | 100% |
| Retention Framework | 100% |
| Archival Rules | 100% |
| Legal Hold | 100% |
| Destruction Policy | 100% |
| Recovery Framework | 100% |
| Audit Integration | 100% |
| Seeded Domain Examples | 100% |
| Full Rule Inventory / Exact Durations | Deferred to amendment |

**Overall Catalog 8 Readiness**

```text
99%
```

The remaining percentage is reserved for full retention-rule inventory, exact duration tables, regulatory mapping detail, and Cross-Volume Traceability.

---

# PART XIX — NEXT CATALOG

## Next Catalog

```text
PEOPLE-CATALOG-09-TRACEABILITY-1.0
```

This catalog will define the Cross-Volume Traceability Matrix that maps requirements, volumes, catalogs, APIs, state machines, permissions, audit events, configuration, notifications, jobs, and retention rules into a single authoritative linkage model.

With Catalogs 1–8 in place, the project now has governing specifications for **workflow states, errors, audit events, configuration, authorization, notifications, background jobs, and data retention**. The final catalog in the locked library sequence is **Traceability**.

No application code is authorized during the catalog sequence.
