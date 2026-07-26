# PEOPLE INTAKE SYSTEM

# IMPLEMENTATION SPECIFICATION MASTER PLAN

**Document ID**

```text
PEOPLE-IMPLEMENTATION-MASTER-1.0
```

**Program**

```text
PEOPLE-IMPLEMENTATION-SPECIFICATION-LIBRARY-1.0
```

**Status**

```text
SUPERSEDED AS PROGRAM AUTHORITY BY PEOPLE-IMPLEMENTATION-SPECIFICATION-PROGRAM-1.0
RETAINED AS HISTORICAL INVENTORY
```

**Superseded By**

```text
docs/implementation_specs/PEOPLE_IMPLEMENTATION_SPECIFICATION_PROGRAM.md
```

**Document Type**

```text
CANONICAL IMPLEMENTATION SERIES MASTER (FOUNDATION) — HISTORICAL
```

**Build Mode**

```text
DOCUMENTATION ONLY
```

> **Authority note:** Decision **D-059** establishes `PEOPLE-IMPLEMENTATION-SPECIFICATION-PROGRAM-1.0` as the program charter. Use `docs/implementation_specs/` for active IS work. This master remains a useful early IS ID inventory but must not contradict the Program Design.
**Prohibited During This Document**

* No application source code
* No database migrations
* No API handlers or UI implementation
* No dependency installation for production runtime
* No inventing Catalog 10+ IDs outside Catalog 0
* No treating this master as Gate G-10 authorization

**Foundation Scope**

This document establishes the Implementation Specification (IS) series as a **separate documentation series** from the Catalog Library. It inventories phases, document IDs, build order, and traceability rules.

Individual IS-* documents are not fully authored here. They expand via formal amendments under this master and must not contradict Volumes 0–13 or Catalogs 0–9 (when Catalog 9 is complete).

**Relationship to Existing Artifacts**

| Layer | Role |
| --- | --- |
| Volumes 0–13 | Product and engineering design authority already written |
| Catalogs 0–8 (+ 09 Traceability next) | Canonical operational language |
| `PEOPLE-IMPLEMENTATION-MASTER-1.0` | Series map and build order for IS documents |
| `docs/16_implementation_packages/` (PKG-*) | Cursor work units — still BLOCKED until Gate G-10 |
| Catalog 9 Traceability | Closes catalog linkage; IS docs must consume its matrix |

Volumes 8–13 already contain substantial database, API, UI, component, and platform specification content. IS documents **refine and package** that authority for build execution; they do not silently replace volume masters.

---

# PART I — PURPOSE

## 1. Mission

The Implementation Specifications convert approved governance documentation into precise engineering specifications suitable for implementation packaging.

Every implementation document must trace back to one or more approved Volumes and Catalogs.

Implementation documents answer:

* exactly what will be built
* how it will be structured
* where it belongs
* what it depends on
* how it is tested
* how it is deployed

No implementation work should begin without an approved implementation specification **and** Gate G-10 authorization.

---

# PART II — SERIES PRINCIPLES

### `IS-PRINCIPLE-001 — Traceability First`

No IS document may exist without documented Volume and Catalog linkage.

### `IS-PRINCIPLE-002 — Catalog Authority Intact`

IS documents may not invent undocumented states, errors, audit events, config keys, permissions, notifications, jobs, or retention classes.

### `IS-PRINCIPLE-003 — Small Packages`

Prefer small implementation packages (roughly 20–40 pages of governing detail, or equivalent PKG-* slices) that Cursor can complete independently.

### `IS-PRINCIPLE-004 — Volumes Remain Canonical`

Where Volume 8–13 masters already define a domain, IS docs cite and refine them; they do not fork conflicting truth.

### `IS-PRINCIPLE-005 — PKG Mapping Required`

Each IS document must map to one or more planned PKG-* units when executable work is defined.

### `IS-PRINCIPLE-006 — No Code Until Gate G-10`

Design-phase IS authorship does not authorize `src/`, migrations, or production wiring.

### `IS-PRINCIPLE-007 — Catalog 9 Prerequisite for Full Traceability Closure`

Full cross-artifact closure requires `PEOPLE-CATALOG-09-TRACEABILITY-1.0`. IS planning may proceed in documentation parallel, but final IS readiness waits on Catalog 9.

### `IS-PRINCIPLE-008 — Fail Closed on Ambiguity`

Ambiguous build instructions stop for Decision Log resolution rather than inventing behavior during coding.

### `IS-PRINCIPLE-009 — Deterministic Build Order`

Foundational infrastructure precedes services, APIs, UI, integrations, and launch.

### `IS-PRINCIPLE-010 — Master Authority`

No IS-* ID may be invented outside this master or an approved amendment.

---

# PART III — IMPLEMENTATION SERIES INVENTORY

## Phase 0 — Repository & Development Foundation

| IS ID | Title | Primary Catalog / Volume Links |
| --- | --- | --- |
| IS-000 | Repository Layout | Volume 13; PKG-0.1 |
| IS-001 | Development Environment | Volume 13; Catalog 4 |
| IS-002 | Configuration Implementation | Catalog 4 |

## Phase 1 — Data Layer

| IS ID | Title | Primary Catalog / Volume Links |
| --- | --- | --- |
| IS-100 | Database Architecture | Volume 9; Catalog 1; Catalog 8 |
| IS-101 | Entity Specifications | Volume 9; Catalog 1; Catalog 5 |
| IS-102 | Database Migrations | Volume 9 (docs only until authorized) |
| IS-103 | Repository Layer | Volume 8–9; Catalog 1 |

## Phase 2 — Business Services

| IS ID | Title | Primary Catalog / Volume Links |
| --- | --- | --- |
| IS-200 | Service Architecture | Volume 8 |
| IS-201 | Authentication Service | Catalog 5; Volume 8 |
| IS-202 | Authorization Service | Catalog 5 |
| IS-203 | Batch Service | Catalog 1; Volume 8 |
| IS-204 | Upload Service | Catalog 1; Catalog 7 |
| IS-205 | Claim Service | Catalog 1; Catalog 7 |
| IS-206 | Draft Service | Catalog 1; Catalog 8 |
| IS-207 | Matching Service | Catalog 1; Volume 8 |
| IS-208 | Promotion Service | Catalog 1; Catalog 7 |
| IS-209 | Notification Service | Catalog 6 |
| IS-210 | Audit Service | Catalog 3 |

## Phase 3 — API Layer

| IS ID | Title | Primary Catalog / Volume Links |
| --- | --- | --- |
| IS-300 | REST Architecture | Volume 10; Catalog 2 |
| IS-301 | Endpoint Specifications | Volume 10; Catalog 5 |
| IS-302 | Request Contracts | Volume 10 |
| IS-303 | Response Contracts | Volume 10 |
| IS-304 | Error Mapping | Catalog 2 |
| IS-305 | Pagination | Catalog 4; Volume 10 |

## Phase 4 — Background Processing

| IS ID | Title | Primary Catalog / Volume Links |
| --- | --- | --- |
| IS-400 | Job Framework | Catalog 7 |
| IS-401 | Queue Processing | Catalog 7 |
| IS-402 | Scheduling | Catalog 7 |
| IS-403 | Retry Engine | Catalog 7; Catalog 4 |
| IS-404 | Recovery | Catalog 7; Catalog 8 |

## Phase 5 — User Interface

| IS ID | Title | Primary Catalog / Volume Links |
| --- | --- | --- |
| IS-500 | Design System | Volume 12 |
| IS-501 | Navigation | Volume 11 |
| IS-502 | Authentication Screens | Volume 11; Catalog 5 |
| IS-503 | Dashboard | Volume 11 |
| IS-504 | Uploader | Volume 11 |
| IS-505 | Review Workspace | Volume 11 |
| IS-506 | Matching Workspace | Volume 11 |
| IS-507 | Administration | Volume 11; Catalog 5 |
| IS-508 | Settings | Volume 11; Catalog 4 |
| IS-509 | Accessibility | Volume 11–12 |

## Phase 6 — Security

| IS ID | Title | Primary Catalog / Volume Links |
| --- | --- | --- |
| IS-600 | Authentication Implementation | Catalog 5 |
| IS-601 | Authorization Middleware | Catalog 5 |
| IS-602 | Secrets | Catalog 4; Catalog 8 |
| IS-603 | Rate Limiting | Catalog 4 |
| IS-604 | Audit Enforcement | Catalog 3 |

## Phase 7 — Integrations

| IS ID | Title | Primary Catalog / Volume Links |
| --- | --- | --- |
| IS-700 | Identity Provider | Catalog 4 (`AUTH_PROVIDER`); Catalog 5 |
| IS-701 | Storage | Catalog 4 (`STORAGE_PROVIDER`) |
| IS-702 | Email | Catalog 6 |
| IS-703 | AI Integration | Volume 8; Catalog 3 |
| IS-704 | Future Government APIs | Catalog 8; Decision Log required before adoption |

## Phase 8 — Operations

| IS ID | Title | Primary Catalog / Volume Links |
| --- | --- | --- |
| IS-800 | Logging | Catalog 4; Catalog 3 |
| IS-801 | Monitoring | Catalog 4 |
| IS-802 | Metrics | Catalog 7 |
| IS-803 | Dashboards | Volume 11 (admin) |
| IS-804 | Deployment | Volume 13 |
| IS-805 | Recovery | Catalog 8; Catalog 7 |

## Phase 9 — Testing

| IS ID | Title | Primary Catalog / Volume Links |
| --- | --- | --- |
| IS-900 | Unit Testing | Catalog 1–8 test sections |
| IS-901 | Integration Testing | Catalog 7; Volume 10 |
| IS-902 | Workflow Testing | Catalog 1 |
| IS-903 | Performance Testing | Catalog 4 |
| IS-904 | Security Testing | Catalog 5 |
| IS-905 | Accessibility Testing | Volume 11–12 |
| IS-906 | Production Readiness | Gate G-10; freeze report |

## Phase 10 — Launch

| IS ID | Title | Primary Catalog / Volume Links |
| --- | --- | --- |
| IS-1000 | Release Checklist | Gate G-10 |
| IS-1001 | Migration Checklist | Volume 9 (authorized only after freeze) |
| IS-1002 | Rollback Procedures | Volume 9; Volume 13 |
| IS-1003 | Launch Verification | Operations IS-800+ |
| IS-1004 | Post-Launch Validation | Catalog 3; Catalog 7 |

**Seeded IS ID count:** 55 documents inventoried (not fully authored).

---

# PART IV — TRACEABILITY REQUIREMENTS

Every implementation specification must reference:

* Master Build Plan
* Governing Volume(s)
* Governing Catalog(s)
* Related ADRs / Decision Log entries
* Related APIs (Volume 10)
* Related State Machines (Catalog 1)
* Related Permissions (Catalog 5)
* Related Audit Events (Catalog 3)
* Related Tests
* Related PKG-* units (when executable)

No implementation document should exist without documented traceability.

---

# PART V — RECOMMENDED BUILD ORDER

1. Repository & Development Foundation (IS-000…002)
2. Database Architecture (IS-100)
3. Entity Specifications (IS-101)
4. Configuration Implementation (IS-002 / Catalog 4)
5. Authentication & Authorization (IS-201/202, IS-600/601)
6. Core Services (IS-203…210)
7. API Layer (IS-300…305)
8. Background Processing (IS-400…404)
9. User Interface (IS-500…509)
10. Integrations (IS-700…704)
11. Operations (IS-800…805)
12. Testing (IS-900…906)
13. Launch Readiness (IS-1000…1004)

This order minimizes rework by building foundational infrastructure before higher-level services and user interfaces.

---

# PART VI — PACKAGE SIZING RULE

Instead of monolithic IS documents, break work into **small implementation packages** that Cursor can complete independently:

* reviewable in isolation
* traceable to governing catalogs and volumes
* mappable to PKG-* index entries
* blocked from coding until Gate G-10

Existing PKG-* rows in `docs/16_implementation_packages/PACKAGE_INDEX.md` remain the executable packaging surface unless formally amended.

---

# PART VII — LOCKED DECISIONS

1. Implementation Specifications are a separate series from the Catalog Library.
2. Catalog IDs 10+ are not created by this master.
3. Volumes 8–13 remain canonical for already-authored domain specs.
4. Catalogs remain the sole authority for states, errors, audit, config, permissions, notifications, jobs, and retention language.
5. No IS document may invent undocumented catalog values.
6. No application code is authorized by authorship of this master.
7. Gate G-10 remains closed until design freeze and audit remediation requirements are met.
8. Catalog 9 Traceability remains the next Catalog Library build.
9. Small packages are preferred over monolithic IS documents.
10. PKG-* units remain BLOCKED until Gate G-10.
11. Seeded IS IDs in this master are authoritative inventory; full content expands via amendment.
12. IS-704 government integrations require Decision Log approval before adoption.
13. Migration and production deletion work remain unauthorized until explicitly unlocked.
14. Ambiguity fails closed to Decision Log resolution.
15. Implementation begins only after approved IS content **and** Gate G-10 authorization.

---

# PART VIII — READINESS

| Area | Readiness |
| --- | --------: |
| Series Structure | 100% |
| Phase Inventory | 100% |
| Traceability Rules | 100% |
| Build Order | 100% |
| Volume / Catalog Mapping | 98% |
| Individual IS Authorship | Deferred |
| Catalog 9 Linkage Closure | Pending Catalog 9 |
| Gate G-10 Authorization | Closed |

**Overall Master Readiness**

```text
95%
```

The remaining percentage is reserved for Catalog 9 Traceability closure, per-IS authorship, and PKG-* reconciliation detail.

---

# PART IX — NEXT ACTIONS

## Catalog Library (primary)

```text
PEOPLE-CATALOG-09-TRACEABILITY-1.0
```

## Parallel (still required for freeze)

```text
PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0
```

## Implementation series (documentation planning only)

Expand IS documents under this master in small packages after Catalog 9 closes, or in parallel as **documentation-only** drafts that remain blocked from coding.

No application code is authorized.
