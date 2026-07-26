# PEOPLE INTAKE SYSTEM

# CATALOG 9 — CROSS-VOLUME TRACEABILITY MATRIX

**Document ID**

```text
PEOPLE-CATALOG-09-TRACEABILITY-1.0
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
CANONICAL CROSS-VOLUME TRACEABILITY CONTRACT AND FOUNDATION
```

**Build Mode**

```text
DOCUMENTATION ONLY
```

**Prohibited During This Catalog**

* No application source code
* No inventing undocumented production catalog keys to “fill” matrix cells
* No claiming system-wide FULLY_MAPPED / VERIFIED for unseeded domains
* No database migrations or runtime enforcement engines
* No dependency installation for application scaffolding
* No silent contradiction of Volumes 0–13 or Catalogs 0–8

**Foundation Scope**

This document establishes the governing Cross-Volume Traceability Matrix contract: principles, linkage chain, required matrix fields, status vocabulary, orphan rules, amendment rules, seeded matrix rows, and locked decisions.

It includes seeded linkage examples drawn from already-approved governance and catalog artifacts. Full cross-volume inventory expansion requires formal catalog amendments under this contract and progressive PEOPLE-IS-* authorship. Incomplete cells MUST use `PENDING`, `PARTIALLY_MAPPED`, `BLOCKED`, or `NOT_APPLICABLE` with rationale — never fabricated IDs.

Companion surfaces (not substitutes for this catalog):

* `docs/traceability/DESIGN_SOURCE_MAP.md` (DOC-0 authority / domain path map)
* `docs/implementation_specs/matrices/REQUIREMENT_TRACEABILITY_MATRIX.md` (IS program RTM)
* `docs/implementation_specs/000_program/PEOPLE-IS-003-TRACEABILITY-STANDARD.md` (IS writing standard)

Catalog 9 is the **authoritative catalog** for the Catalog Library linkage model. IS-003 remains the Implementation Specification writing standard; both MUST remain consistent.

---

# PART I — PURPOSE

## 1. Mission

Prove that every approved business rule and requirement is represented — in both directions — across governing volumes, catalogs, engineering design, verification, and (later) implementation packages.

It establishes:

* the canonical linkage chain
* required matrix fields
* mapping statuses
* orphan prohibitions
* seeded verified / mapped examples
* rules for expanding the matrix without inventing keys

---

# PART II — DESIGN PRINCIPLES

## 2. Core Principles

### `TRACE-PRINCIPLE-001 — Bidirectional Traceability`

Every mapped requirement MUST be navigable from governance to implementation planning and from implementation artifacts back to governance.

### `TRACE-PRINCIPLE-002 — Stable Identifiers`

Every requirement and linked artifact MUST use a stable identifier conforming to PEOPLE-IS-002 and the owning catalog.

### `TRACE-PRINCIPLE-003 — No Silent Orphans`

Critical orphans listed in this catalog are prohibited. Gaps MUST be explicit (`UNMAPPED`, `PARTIALLY_MAPPED`, `BLOCKED`, or `NOT_APPLICABLE` with reason).

### `TRACE-PRINCIPLE-004 — Catalog Authority`

Cataloged operational language (states, errors, permissions, audit events, config keys, notifications, jobs, retention) remains owned by Catalogs 1–8. This matrix links; it does not redefine those catalogs.

### `TRACE-PRINCIPLE-005 — Honesty Over Completeness`

A partial but honest matrix is preferred to a complete matrix that invents undocumented production values.

### `TRACE-PRINCIPLE-006 — Source Required`

Every requirement row MUST identify a governing source document and section or equivalent authority reference.

### `TRACE-PRINCIPLE-007 — Tests Are Mandatory for Implementation Readiness`

A requirement cannot reach implementation readiness without one or more mapped tests (or an explicit deferred-test plan recorded as `BLOCKED` with owner).

### `TRACE-PRINCIPLE-008 — Privileged Actions Require Permissions`

Privileged operations MUST map to Catalog 5 permission keys.

### `TRACE-PRINCIPLE-009 — State Mutations Require Audit Decisions`

State mutations MUST map to a Catalog 3 audit event or an explicit documented audit-decision exception.

### `TRACE-PRINCIPLE-010 — Catalog Library Locked at 0–9`

The governed Catalog Library remains Catalogs 0–9. Draft material labeled Catalogs 10–13 is Volume or Implementation Specification supporting content — not catalog authority.

---

# PART III — CANONICAL LINKAGE CHAIN

## 3. Catalog 0 Chain (required)

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

## 4. Extended Engineering Chain (IS-003 aligned)

Not every requirement uses every node. Applicable nodes MUST be recorded.

```text
Master Objective
→ Volume Requirement
→ Catalog Rule
→ Implementation Requirement
→ Entity
→ Service
→ API
→ UI
→ Background Job
→ Integration
→ Permission
→ State Transition
→ Error
→ Audit Event
→ Notification
→ Retention Rule
→ Test
→ Implementation Package
→ Verification Evidence
```

## 5. Link Node IDs

| Node ID | Meaning |
| --- | --- |
| LINK-BUSINESS-RULE | Governing business / volume rule |
| LINK-STATE | Catalog 1 state or machine |
| LINK-DATABASE | Entity / table / field |
| LINK-API | API endpoint or contract |
| LINK-SCREEN | UI screen / surface |
| LINK-COMPONENT | UI component |
| LINK-PERMISSION | Catalog 5 permission key |
| LINK-AUDIT | Catalog 3 audit event |
| LINK-ERROR | Catalog 2 error code |
| LINK-TEST | Test ID |
| LINK-PACKAGE | Implementation package ID |
| LINK-JOB | Catalog 7 job |
| LINK-NOTIFICATION | Catalog 6 notification |
| LINK-RETENTION | Catalog 8 retention rule |
| LINK-CONFIG | Catalog 4 configuration key |
| LINK-INTEGRATION | External integration boundary |

---

# PART IV — MATRIX FIELD CONTRACT

## 6. Required fields

Every matrix row MUST support the following fields (blank only when `NOT_APPLICABLE` with reason, or `PENDING` during foundation expansion):

```text
Trace Row ID
Requirement ID
Requirement Title
Requirement Type
Priority
Source Document
Source Section
Governing Catalog
Entity
Field
Service
API
UI Screen
Component
Job
Integration
Permission
State
Transition
Error
Audit Event
Notification
Retention Rule
Config Key
Test IDs
Implementation Package
Status
Notes
```

## 7. Status vocabulary

```text
UNMAPPED
PARTIALLY_MAPPED
FULLY_MAPPED
VERIFIED
BLOCKED
NOT_APPLICABLE
```

`NOT_APPLICABLE` REQUIRES an explanation in Notes.

`VERIFIED` REQUIRES documented review evidence (Phase review, gate review, or named validation).

---

# PART V — ORPHAN RULES

## 8. Prohibited orphans

The following are prohibited for implementation-ready work:

* a requirement with no source
* an entity with no requirement
* an API with no service
* a state transition with no audit decision
* a privileged operation with no permission
* a production error with no Catalog 2 entry
* a notification with no trigger
* a job with no owner
* a test with no requirement
* an implementation package with no approved specification

Foundation documentation MAY record known orphans as `BLOCKED` or `PARTIALLY_MAPPED` until resolved.

---

# PART VI — ROW TEMPLATE

## 9. Traceability row template

```text
Trace Row ID:
Requirement ID:
Title:
Type:
Priority:
Source Document:
Source Section:
Governing Catalog:
Entity:
Field:
Service:
API:
UI Screen:
Component:
Job:
Integration:
Permission:
State:
Transition:
Error:
Audit Event:
Notification:
Retention Rule:
Config Key:
Test IDs:
Implementation Package:
Status:
Notes:
```

---

# PART VII — SEEDED MATRIX ROWS

## 10. Seed inventory

This foundation seeds **ten** authoritative starting rows. Additional rows expand only by formal amendment or by PEOPLE-IS documents that update this catalog’s registry through approved process.

### `TRACE-SEED-001`

| Field | Value |
| --- | --- |
| Requirement ID | REQ-GOV-001 |
| Title | Documentation must precede implementation |
| Type | Governance |
| Priority | CRITICAL |
| Source | PEOPLE-IS-000 / Master Program |
| Status | VERIFIED |
| Test IDs | Phase 0 review |
| Package | PKG-0.0 |
| Notes | Locked by D-060 / D-061 posture |

### `TRACE-SEED-002`

| Field | Value |
| --- | --- |
| Requirement ID | REQ-GOV-007 |
| Title | All project work must remain under H:\people |
| Type | Governance |
| Priority | CRITICAL |
| Source | PEOPLE-IS-000 |
| Status | VERIFIED |
| Test IDs | Boundary review / governance:validate |
| Notes | Aligns with REQ-REPO-001 |

### `TRACE-SEED-003`

| Field | Value |
| --- | --- |
| Requirement ID | REQ-GOV-008 |
| Title | Nothing may intentionally write to C:\ |
| Type | Governance |
| Priority | CRITICAL |
| Source | PEOPLE-IS-000 |
| Status | VERIFIED |
| Test IDs | Boundary review |
| Notes | OS-unrelated writes distinguished in IS-100 |

### `TRACE-SEED-004`

| Field | Value |
| --- | --- |
| Requirement ID | REQ-GOV-009 |
| Title | Approval does not automatically authorize implementation |
| Type | Governance |
| Priority | CRITICAL |
| Source | PEOPLE-IS-000 |
| Status | VERIFIED |
| Test IDs | Governance review |
| Notes | Gate G-10 remains CLOSED |

### `TRACE-SEED-005`

| Field | Value |
| --- | --- |
| Requirement ID | REQ-GOV-010 |
| Title | Production secrets must not appear in documentation |
| Type | Governance / Security |
| Priority | CRITICAL |
| Source | PEOPLE-IS-000 |
| Status | VERIFIED |
| Test IDs | Security review |
| Retention Rule | RETAIN-SECRET-001 (related class) |
| Notes | Catalog 8 secret retention example linked by class, not as a runtime job |

### `TRACE-SEED-006`

| Field | Value |
| --- | --- |
| Requirement ID | REQ-REPO-001 |
| Title | Canonical project root H:\people |
| Type | Repository |
| Priority | CRITICAL |
| Source | PEOPLE-IS-100 |
| Status | FULLY_MAPPED |
| Test IDs | Root validation test (future) |
| Package | Future repository-guard package |
| Notes | Design-mapped; guard code not authorized |

### `TRACE-SEED-007`

| Field | Value |
| --- | --- |
| Requirement ID | REQ-REPO-005 |
| Title | Dependency direction Presentation→Application→Domain |
| Type | Repository |
| Priority | HIGH |
| Source | PEOPLE-IS-100 |
| Status | FULLY_MAPPED |
| Test IDs | Import-boundary tests (future) |
| Notes | Blocks coding until ADRs + packages |

### `TRACE-SEED-008`

| Field | Value |
| --- | --- |
| Requirement ID | REQ-REPO-015 |
| Title | Canonical START_HERE orientation document |
| Type | Repository |
| Priority | HIGH |
| Source | PEOPLE-IS-100 |
| Status | FULLY_MAPPED |
| Test IDs | Orientation review |
| Notes | `START_HERE.md` present at repository root |

### `TRACE-SEED-009`

| Field | Value |
| --- | --- |
| Requirement ID | REQ-CLAIM-ACQUIRE (seed placeholder for claim acquire rule) |
| Title | Page claim acquire must enforce exclusive hold semantics |
| Type | Workflow |
| Priority | HIGH |
| Source | Volume 2 / Catalog 1 / Catalog 5 |
| Permission | PAGE_CLAIM |
| Error | CLAIM_ALREADY_HELD |
| Audit Event | AUDIT-CLAIM-001 / CLAIM_ACQUIRED |
| Status | PARTIALLY_MAPPED |
| Test IDs | PENDING |
| Package | PENDING |
| Notes | Uses only Catalog 2/3/5 seeded/canonical keys. Full entity/API/UI/job mapping expands via IS phases — do not invent routes or tables here. |

### `TRACE-SEED-010`

| Field | Value |
| --- | --- |
| Requirement ID | REQ-GOV-CATALOG-LOCK |
| Title | Catalog Library remains locked at Catalogs 0–9 |
| Type | Governance |
| Priority | CRITICAL |
| Source | Catalog 0 / D-059 / D-060 / D-061 |
| Status | VERIFIED |
| Test IDs | Catalog library validation |
| Notes | Catalogs 10–13 labels are non-canonical |

---

# PART VIII — RELATIONSHIP TO OTHER ARTIFACTS

## 11. DOC-0 Design Source Map

`docs/traceability/DESIGN_SOURCE_MAP.md` defines authority hierarchy and domain→path ownership. It does **not** replace this matrix. Catalog 9 rows SHOULD cite Volume/path sources consistent with that map.

## 12. Implementation Specification RTM

`docs/implementation_specs/matrices/REQUIREMENT_TRACEABILITY_MATRIX.md` tracks IS-program requirements. Catalog 9 is the Catalog Library authority for cross-volume linkage. When both exist for the same Requirement ID, they MUST not contradict; conflicts become open issues.

## 13. PEOPLE-IS-003

IS-003 defines how PEOPLE-IS documents write and gate traceability. Catalog 9 defines the catalog-level matrix contract. Field names and statuses are intentionally aligned.

---

# PART IX — AMENDMENT AND EXPANSION

## 14. Adding rows

New rows REQUIRE:

* stable Requirement ID and Trace Row ID
* source citation
* honest status
* no invented Catalog 1–8 keys
* registry and SHA update through governed build scripts
* Decision Log or CHANGE-* when material

## 15. Changing mapped keys

Changing a mapped catalog key REQUIRES impact analysis per PEOPLE-IS-003 (entities, services, APIs, screens, jobs, permissions, states, errors, audit, notifications, tests, packages).

---

# PART X — GOVERNANCE

## 16. Review points

Traceability MUST be reviewed:

* when a specification becomes structurally complete
* before technical approval
* before implementation readiness
* after any breaking change
* before release
* after a major incident affecting governed behavior

## 17. Completion standard for TRACEABILITY_COMPLETE (specs)

A PEOPLE-IS specification cannot reach `TRACEABILITY_COMPLETE` unless the PEOPLE-IS-003 minimum standard is met. Catalog 9 foundation completion does **not** auto-complete every future IS document.

---

# PART XI — LOCKED TRACEABILITY DECISIONS

## Locked Decisions

1. Traceability is bidirectional.
2. Stable identifiers are mandatory.
3. Critical orphans are prohibited for implementation-ready work.
4. Catalogs 1–8 own operational language; Catalog 9 links them.
5. Honesty over invented completeness.
6. Every requirement row requires a source.
7. Implementation readiness requires mapped tests (or explicit BLOCKED test plan).
8. Privileged actions require Catalog 5 permissions.
9. State mutations require Catalog 3 audit decisions or documented exceptions.
10. Catalog Library remains locked at Catalogs 0–9.
11. Seeded TRACE-SEED-* rows are authoritative starting points for amendment.
12. DOC-0 Design Source Map and IS RTM are companions, not substitutes.
13. `NOT_APPLICABLE` requires a written reason.
14. Fabricating undocumented production keys to fill matrix cells is prohibited.
15. Additional matrix rows and full inventories expand only via formal amendment or governed IS updates under this contract.

---

# PART XII — READINESS

| Area | Readiness |
| --- | --------: |
| Linkage Chain Model | 100% |
| Field Contract | 100% |
| Status Vocabulary | 100% |
| Orphan Rules | 100% |
| Seeded Matrix Rows | 100% |
| Alignment with IS-003 | 100% |
| Full Cross-Volume Inventory | Deferred to amendment / IS phases |
| Runtime Traceability Tooling | Not authorized |

**Overall Catalog 9 Readiness**

```text
98%
```

The remaining percentage is reserved for full cross-volume row inventory, complete claim/workflow mappings, and verification evidence expansion.

---

# PART XIII — LIBRARY CLOSURE

## Catalog Library status

With Catalogs 0–9 complete at foundation/design level, the locked Catalog Library sequence is **closed**.

```text
PEOPLE-CATALOG-LIBRARY-COMPLETE
PEOPLE-CATALOG-LIBRARY-1.0 — DESIGN COMPLETE (FOUNDATION)
APPLICATION IMPLEMENTATION — NOT AUTHORIZED
```

## Next governed build (after this catalog)

```text
PEOPLE-IS-101-TECHNOLOGY-DECISION-SPECIFICATION-1.0
```

`nextCatalogId` for the Catalog 0 / Catalog 9 registries is:

```text
PEOPLE-CATALOG-LIBRARY-COMPLETE
```

Catalog 09 closes first so technology decisions in IS-101 can map cleanly to requirements, ADRs, risks, tests, and later packages.

Parallel freeze work remains required:

```text
PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0
```

No application code is authorized by Catalog Library completion.
