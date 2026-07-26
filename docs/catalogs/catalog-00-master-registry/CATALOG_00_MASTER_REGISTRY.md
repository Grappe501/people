# PEOPLE INTAKE SYSTEM

# CATALOG 0 — MASTER CATALOG REGISTRY

**Document ID**

```text
PEOPLE-CATALOG-00-MASTER-REGISTRY-1.0
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
* No undocumented enum, status, error, permission, audit, config, or job values in production code

---

## 1. Purpose

The Master Catalog Registry defines every controlled catalog required before implementation begins.

The catalogs convert the broad rules in Volumes 0–13 into exact operational values that software may safely enforce.

The catalog library prevents Cursor, developers, APIs, database migrations, background workers, and user-interface components from inventing:

* states
* transitions
* errors
* permissions
* audit events
* configuration keys
* notification types
* job types
* retention rules
* severity levels
* reason codes
* recovery actions

---

## 2. Catalog Authority

The catalog hierarchy is:

```text
Project Constitution
        ↓
Volumes 0–13
        ↓
Canonical Catalogs
        ↓
Traceability Matrix
        ↓
Implementation Packages
        ↓
Code and Infrastructure
```

Catalogs interpret and operationalize the volumes.

Catalogs may not contradict the volumes.

Where a catalog exposes a contradiction, implementation stops until the governing documentation is reconciled.

---

## 3. Required Catalog Set

### `PEOPLE-CATALOG-00-MASTER-REGISTRY-1.0`

Defines:

* catalog inventory
* catalog ownership
* catalog formatting
* identifiers
* lifecycle
* versioning
* amendment procedures

### `PEOPLE-CATALOG-01-STATE-MACHINES-1.0`

Defines:

* every record lifecycle
* allowed states
* initial states
* terminal states
* transitions
* actors
* guards
* side effects
* prohibited transitions
* recovery transitions

### `PEOPLE-CATALOG-02-ERRORS-1.0`

Defines:

* error codes
* categories
* severity
* HTTP mapping
* safe user messages
* operator messages
* retryability
* recovery
* audit requirements

### `PEOPLE-CATALOG-03-AUDIT-EVENTS-1.0`

Defines:

* event names
* event versions
* domains
* actors
* subjects
* payloads
* results
* required audit transactions
* retention

### `PEOPLE-CATALOG-04-CONFIGURATION-1.0`

Defines:

* environment variables
* runtime settings
* feature flags
* limits
* timeouts
* retries
* secret classification
* defaults
* environment availability

### `PEOPLE-CATALOG-05-PERMISSIONS-1.0`

Defines:

* roles
* permissions
* resource scopes
* action scopes
* administrative overrides
* separation of duties
* denied combinations

### `PEOPLE-CATALOG-06-NOTIFICATIONS-1.0`

Defines:

* notification types
* recipients
* channels
* severity
* triggers
* deduplication
* acknowledgment behavior
* privacy limits

### `PEOPLE-CATALOG-07-BACKGROUND-JOBS-1.0`

Defines:

* job types
* payload contracts
* retry rules
* idempotency
* concurrency
* timeouts
* terminal failure behavior
* operator recovery

### `PEOPLE-CATALOG-08-DATA-RETENTION-1.0`

Defines:

* data classifications
* retention classes
* archive periods
* legal hold
* destruction eligibility
* export controls
* evidence-preservation rules

### `PEOPLE-CATALOG-09-TRACEABILITY-1.0`

Maps:

```text
Business Rule
→ State
→ Database
→ API
→ Screen
→ Component
→ Permission
→ Audit Event
→ Error
→ Test
→ Implementation Package
```

---

## 4. Catalog Entry Standard

Every catalog item must include, where applicable:

```text
Catalog Item ID
Canonical Key
Display Name
Description
Owning Domain
Source Volume
Status
Version
Allowed Actors
Preconditions
Behavior
Side Effects
Audit Event
Error Codes
Recovery
Tests
Traceability
```

---

## 5. Identifier Standard

Catalog identifiers use:

```text
<CATALOG>-<DOMAIN>-<NUMBER>
```

Examples:

```text
STATE-BATCH-001
ERROR-CLAIM-004
AUDIT-USER-007
CONFIG-UPLOAD-003
PERM-MATCH-005
JOB-PROMOTION-002
```

Canonical machine keys use uppercase snake case.

Examples:

```text
READY_FOR_TRANSCRIPTION
CLAIM_ALREADY_HELD
MATCH_RESOLUTION_FINALIZED
UPLOAD_MAX_FILE_SIZE_BYTES
```

---

## 6. Catalog Versioning

Compatible additions:

```text
1.0 → 1.1
```

Breaking changes:

```text
1.x → 2.0
```

A breaking change includes:

* removing a canonical key
* changing established meaning
* changing a terminal state into a nonterminal state
* weakening a permission
* changing retry safety
* changing audit requirements
* changing retained evidence behavior

---

## 7. Catalog Change Record

Every catalog amendment must record:

```text
Change ID
Date
Catalog
Previous Version
New Version
Reason
Affected Entries
Affected Volumes
Affected Implementation
Migration Required
Approved By
```

---

## 8. Canonical Value Rule

Implementation may not create undocumented enum values, status values, reason codes, error codes, role keys, permission keys, audit-event names, configuration keys, or job types.

Temporary experimental values must:

* be explicitly marked experimental
* remain outside production
* have an owner
* have an expiration date
* be removed or formally cataloged before release

---

## 9. Catalog Library Sequence

Build order:

```text
CATALOG-0  Master Catalog Registry
CATALOG-1  State Machine Catalog
CATALOG-2  Error Catalog
CATALOG-3  Audit Event Catalog
CATALOG-4  Configuration Catalog
CATALOG-5  Permission and Authorization Catalog
CATALOG-6  Notification Catalog
CATALOG-7  Background Job Catalog
CATALOG-8  Data Classification and Retention Catalog
CATALOG-9  Cross-Volume Traceability Matrix
```

## 10. Current Status

| Catalog ID | Title | Status |
| --- | --- | --- |
| PEOPLE-CATALOG-00-MASTER-REGISTRY-1.0 | Master Catalog Registry | DESIGN COMPLETE |
| PEOPLE-CATALOG-01-STATE-MACHINES-1.0 | State Machine Catalog | DESIGN COMPLETE |
| PEOPLE-CATALOG-02-ERRORS-1.0 | Error Catalog | DESIGN COMPLETE |
| PEOPLE-CATALOG-03-AUDIT-EVENTS-1.0 | Audit Event Catalog | DESIGN COMPLETE (foundation) |
| PEOPLE-CATALOG-04-CONFIGURATION-1.0 | Configuration Catalog | DESIGN COMPLETE (foundation) |
| PEOPLE-CATALOG-05-PERMISSIONS-1.0 | Permission and Authorization Catalog | DESIGN COMPLETE (foundation) |
| PEOPLE-CATALOG-06-NOTIFICATIONS-1.0 | Notification Catalog | DESIGN COMPLETE (foundation) |
| PEOPLE-CATALOG-07-BACKGROUND-JOBS-1.0 | Background Job Catalog | DESIGN COMPLETE (foundation) |
| PEOPLE-CATALOG-08-DATA-RETENTION-1.0 | Data Classification and Retention Catalog | DESIGN COMPLETE (foundation) |
| PEOPLE-CATALOG-09-TRACEABILITY-1.0 | Cross-Volume Traceability Matrix | DESIGN COMPLETE (foundation) |

The locked Catalog Library sequence (0–9) is complete at foundation/design level:

```text
PEOPLE-CATALOG-LIBRARY-COMPLETE
```

The next governed engineering specification build is:

```text
PEOPLE-IS-101-TECHNOLOGY-DECISION-SPECIFICATION-1.0
```

No application code is authorized by Catalog Library completion.
