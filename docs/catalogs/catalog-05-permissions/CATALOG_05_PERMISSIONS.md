# PEOPLE INTAKE SYSTEM

# CATALOG 5 — PERMISSIONS & AUTHORIZATION CATALOG

**Document ID**

```text
PEOPLE-CATALOG-05-PERMISSIONS-1.0
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
CANONICAL PERMISSIONS AND AUTHORIZATION CATALOG
```

**Build Mode**

```text
DOCUMENTATION ONLY
```

**Prohibited During This Catalog**

* No application source code
* No authentication or authorization middleware implementation
* No RLS policy SQL or migrations
* No role-assignment UI or handlers
* No dependency installation
* No inventing undocumented production roles, permission keys, or matrix grants outside this catalog and its approved amendments

**Foundation Scope**

This document establishes the governing authorization contract: principles, Version 1 roles, resource types, action model, seeded permission keys, resource scopes, evaluation order, separation of duties, administrative overrides, delegated authority rules, emergency access, audit and test requirements, and locked decisions.

It includes a seeded permission matrix and permission keys. Additional permission keys, matrix cells, and SoD rules must be added through formal catalog amendments under this contract and must not contradict Volumes 0–13 or Catalogs 1–4.

Authentication answers **who you are**. Authorization answers **what you may do**.

---

# PART I — PURPOSE

## 1. Mission

This catalog defines the complete authorization model for the People Intake System.

It answers:

* Who may perform an action?
* On what resource?
* Under what conditions?
* When is approval required?
* When is separation of duties required?
* What must be audited?

No protected action may be authorized outside this catalog.

---

# PART II — AUTHORIZATION PRINCIPLES

## 2. Core Principles

### `AUTHZ-PRINCIPLE-001 — Server Enforcement`

Authorization is always enforced on the server.

### `AUTHZ-PRINCIPLE-002 — UI Is Not Authority`

Hidden buttons are not authorization. Permission is never determined by the client.

### `AUTHZ-PRINCIPLE-003 — Identity Prerequisite`

Every protected action requires an authenticated identity.

### `AUTHZ-PRINCIPLE-004 — Active Account`

Every protected action requires an active account.

### `AUTHZ-PRINCIPLE-005 — Role Assignment`

Every protected action requires an assigned Version 1 role (or System actor context).

### `AUTHZ-PRINCIPLE-006 — Permission Grant`

Every protected action requires the required permission key.

### `AUTHZ-PRINCIPLE-007 — Resource Eligibility`

Every protected action requires resource eligibility within an allowed scope.

### `AUTHZ-PRINCIPLE-008 — State Eligibility`

Every protected action requires state eligibility from Catalog 1.

### `AUTHZ-PRINCIPLE-009 — Separation of Duties`

Protected workflows enforce separation-of-duties rules where cataloged.

### `AUTHZ-PRINCIPLE-010 — Catalog Authority`

No production role, permission key, or authorization grant may exist outside this catalog or an approved amendment.

Authorization prerequisites for every protected action:

* authenticated identity
* active account
* assigned role
* required permission
* resource eligibility
* state eligibility

---

# PART III — ROLE MODEL

## 3. Canonical Version 1 Roles

The canonical Version 1 roles are a closed set:

```text
Owner
Administrator
Reviewer
Data Entry
Uploader
Viewer
System
```

### ROLE-001 — Owner

**Role Key**

```text
Owner
```

May:

* configure the system
* manage administrators
* manage roles
* modify configuration
* archive records
* access all audit history
* perform emergency recovery

Cannot bypass immutable audit history.

### ROLE-002 — Administrator

**Role Key**

```text
Administrator
```

May:

* manage users
* assign approved roles
* manage queues
* release claims
* reopen eligible work
* review operational errors

Cannot:

* remove the final Owner
* alter immutable audit records
* bypass required approvals

### ROLE-003 — Reviewer

**Role Key**

```text
Reviewer
```

May:

* review transcription
* resolve matches
* approve promotions
* return corrections

Cannot:

* manage users
* modify configuration
* assign permissions

### ROLE-004 — Data Entry

**Role Key**

```text
Data Entry
```

May:

* claim pages
* create drafts
* edit active drafts
* submit transcription

Cannot:

* approve work
* resolve matches
* archive records

### ROLE-005 — Uploader

**Role Key**

```text
Uploader
```

May:

* create batches
* upload pages
* replace images
* review image quality

Cannot:

* transcribe
* match
* promote

### ROLE-006 — Viewer

**Role Key**

```text
Viewer
```

Read-only access to authorized resources.

Cannot modify data.

### ROLE-007 — System

**Role Key**

```text
System
```

Reserved for:

* scheduled jobs
* background workers
* migration tasks
* automated retries

Never authenticates through interactive login.

---

# PART IV — RESOURCE TYPES

Authorization applies to:

```text
Users
Roles
Batches
Pages
Entries
Claims
Drafts
Uploads
Images
Queues
Matches
Resolutions
Promotions
Exports
Reports
Configuration
Audit
Background Jobs
```

| Resource ID | Resource Type |
| --- | --- |
| RES-001 | Users |
| RES-002 | Roles |
| RES-003 | Batches |
| RES-004 | Pages |
| RES-005 | Entries |
| RES-006 | Claims |
| RES-007 | Drafts |
| RES-008 | Uploads |
| RES-009 | Images |
| RES-010 | Queues |
| RES-011 | Matches |
| RES-012 | Resolutions |
| RES-013 | Promotions |
| RES-014 | Exports |
| RES-015 | Reports |
| RES-016 | Configuration |
| RES-017 | Audit |
| RES-018 | Background Jobs |

---

# PART V — ACTION MODEL

Every protected action is cataloged. Seeded Version 1 actions:

```text
READ
CREATE
UPDATE
DELETE
CLAIM
RELEASE
SUBMIT
APPROVE
RETURN
MATCH
RESOLVE
PROMOTE
EXPORT
ARCHIVE
RESTORE
CONFIGURE
```

| Action ID | Action |
| --- | --- |
| ACTION-001 | READ |
| ACTION-002 | CREATE |
| ACTION-003 | UPDATE |
| ACTION-004 | DELETE |
| ACTION-005 | CLAIM |
| ACTION-006 | RELEASE |
| ACTION-007 | SUBMIT |
| ACTION-008 | APPROVE |
| ACTION-009 | RETURN |
| ACTION-010 | MATCH |
| ACTION-011 | RESOLVE |
| ACTION-012 | PROMOTE |
| ACTION-013 | EXPORT |
| ACTION-014 | ARCHIVE |
| ACTION-015 | RESTORE |
| ACTION-016 | CONFIGURE |

Additional actions require formal catalog amendment.

---

# PART VI — PERMISSION KEYS

Permission keys are permanent identifiers.

Every permission entry includes:

```text
Permission ID
Permission Key
Display Name
Resource Type
Action
Default Scopes
Granted Roles
Separation of Duties
Audit Required
Related Catalogs
```

## 6. Seeded Permission Keys

### PERM-USER-001

```text
USER_READ
```

### PERM-USER-002

```text
USER_CREATE
```

### PERM-USER-003

```text
USER_UPDATE
```

### PERM-USER-004

```text
USER_DISABLE
```

### PERM-ROLE-001

```text
ROLE_ASSIGN
```

### PERM-BATCH-001

```text
BATCH_CREATE
```

### PERM-BATCH-002

```text
BATCH_COMPLETE
```

### PERM-PAGE-001

```text
PAGE_UPLOAD
```

### PERM-PAGE-002

```text
PAGE_REPLACE_IMAGE
```

### PERM-PAGE-003

```text
PAGE_CLAIM
```

### PERM-PAGE-004

```text
PAGE_SUBMIT
```

### PERM-MATCH-001

```text
MATCH_REVIEW
```

### PERM-MATCH-002

```text
MATCH_FINALIZE
```

### PERM-PROMOTION-001

```text
PROMOTION_APPROVE
```

### PERM-EXPORT-001

```text
EXPORT_RUN
```

### PERM-CONFIG-001

```text
CONFIGURATION_EDIT
```

### PERM-AUDIT-001

```text
AUDIT_VIEW
```

### PERM-SYSTEM-001

```text
SYSTEM_JOB_EXECUTE
```

Additional permission keys require formal catalog amendment under this contract.

---

# PART VII — RESOURCE SCOPES

Each permission applies within one or more scopes.

Scopes include:

```text
Own Resource
Assigned Work
Department
Organization
Entire System
```

| Scope ID | Scope |
| --- | --- |
| SCOPE-001 | Own Resource |
| SCOPE-002 | Assigned Work |
| SCOPE-003 | Department |
| SCOPE-004 | Organization |
| SCOPE-005 | Entire System |

Examples:

A Data Entry user may edit:

```text
Assigned Work
```

An Administrator may release:

```text
Entire System
```

---

# PART VIII — PERMISSION MATRIX

Seeded Version 1 matrix (display rows map to permission keys above). Full cell-level expansion for every key continues via amendment under this contract.

| Permission | Owner | Admin | Reviewer | Data Entry | Uploader | Viewer | System |
| --- | :---: | :---: | :------: | :--------: | :------: | :----: | :----: |
| View Users | ✓ | ✓ | | | | | |
| Create Users | ✓ | ✓ | | | | | |
| Assign Roles | ✓ | ✓ | | | | | |
| Create Batch | ✓ | ✓ | | | ✓ | | |
| Upload Pages | ✓ | ✓ | | | ✓ | | |
| Claim Work | ✓ | ✓ | | ✓ | | | |
| Submit Transcription | ✓ | ✓ | | ✓ | | | |
| Review Transcription | ✓ | ✓ | ✓ | | | | |
| Finalize Match | ✓ | ✓ | ✓ | | | | |
| Promote Identity | ✓ | ✓ | ✓ | | | | |
| View Audit | ✓ | ✓ | Limited | | | | |
| Change Configuration | ✓ | | | | | | |
| Execute Jobs | | | | | | | ✓ |

Matrix legend:

* ✓ — granted at cataloged scope for the role
* Limited — Reviewer may view audit related to assigned review work only
* blank — not granted

---

# PART IX — SEPARATION OF DUTIES

Certain actions must be performed by different people.

### SOD-001 — Submit and Approve

The same user may not both submit transcription and approve that submission.

### SOD-002 — Match Resolve and Dual Review

The same user may not both resolve a match and approve an exception requiring dual review (when dual review is enabled).

### SOD-003 — Self Elevation

The same user may not approve their own administrative elevation.

These rules prevent conflicts of interest. Additional SoD rules require formal catalog amendment.

---

# PART X — ADMINISTRATIVE OVERRIDES

Administrative overrides are allowed only where explicitly authorized.

Every override requires:

* reason
* actor
* timestamp
* audit event

Some actions cannot be overridden.

Examples:

* immutable audit history
* final Owner protection
* completed retention destruction

---

# PART XI — PERMISSION EVALUATION ORDER

Authorization evaluates in this order:

1. Authenticated?
2. Active account?
3. Role assigned?
4. Permission granted?
5. Resource exists?
6. Resource scope valid?
7. State allows action?
8. Separation-of-duties satisfied?
9. Additional policy satisfied?

Only then is the action executed.

Denial at any step fails closed. Protected denials generate audit events per Part XIV.

---

# PART XII — DELEGATED AUTHORITY

Future versions may support delegated administration.

Delegations must include:

* scope
* expiration
* delegating actor
* delegated permissions

Delegation never exceeds the delegator's authority.

Delegation is not enabled in Version 1 interactive product surfaces until a formal amendment unlocks it.

---

# PART XIII — EMERGENCY ACCESS

Emergency access is limited.

Requirements:

* Owner approval or approved emergency policy
* mandatory audit
* mandatory reason
* automatic expiration
* post-event review

Emergency access cannot rewrite immutable audit history.

---

# PART XIV — AUDIT REQUIREMENTS

The following always generate audit events:

* role assignment
* role removal
* permission denial on protected actions
* administrative override
* emergency access
* configuration changes
* user suspension
* user reactivation

Audit event shapes and names are governed by Catalog 3. Authorization must not invent undocumented audit event names.

---

# PART XV — TEST REQUIREMENTS

Every permission requires tests for:

* authorized user
* unauthorized user
* wrong role
* inactive account
* wrong resource scope
* invalid state
* separation-of-duties violation
* audit generation

Tests are documentation requirements until implementation is authorized.

---

# PART XVI — LOCKED AUTHORIZATION DECISIONS

## Locked Decisions

1. Authorization is server enforced.
2. Roles grant permissions.
3. Permissions apply to resources.
4. Resources have scopes.
5. States may block otherwise valid permissions.
6. Hidden UI never grants authorization.
7. Owners cannot be accidentally removed.
8. Audit history is always protected.
9. Administrative overrides are auditable.
10. Separation of duties is enforced for protected workflows.
11. Version 1 roles are a closed set unless formally amended.
12. Permission keys are permanent identifiers.
13. System never authenticates through interactive login.
14. Delegation never exceeds the delegator's authority.
15. Additional roles, permission keys, and matrix grants require catalog amendment.

---

# PART XVII — READINESS

| Area | Readiness |
| --- | --------: |
| Role Model | 100% |
| Permission Keys | 100% |
| Resource Scopes | 100% |
| Permission Matrix | 99% |
| Separation of Duties | 100% |
| Audit Integration | 100% |
| Authorization Rules | 100% |
| Seeded Keys | 100% |
| Full Key Inventory Expansion | Deferred to amendment |

**Overall Catalog 5 Readiness**

```text
99%
```

The remaining percentage is reserved for full permission-key inventory expansion, Notification Catalog linkage, and Cross-Volume Traceability.

---

# PART XVIII — NEXT CATALOG

## Next Catalog

```text
PEOPLE-CATALOG-06-NOTIFICATIONS-1.0
```

This catalog will define every notification type, delivery channel, priority, recipient rules, expiration policy, acknowledgment behavior, deduplication policy, and the exact events that trigger notifications throughout the system.

With Catalogs 1–5 in place, the project now has governing specifications for **workflow states, errors, audit events, configuration, and authorization**. The next major governance layer is the **Notification Catalog**.

No application code is authorized during the catalog sequence.
