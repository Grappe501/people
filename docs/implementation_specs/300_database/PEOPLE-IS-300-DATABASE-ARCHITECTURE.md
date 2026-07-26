# PEOPLE-IS-300 — DATABASE ARCHITECTURE

**Title:** Database Architecture  
**Document ID:** `PEOPLE-IS-300-DATABASE-ARCHITECTURE-1.0`  
**Version:** 1.0  
**Status:** APPROVED  
**Phase:** PHASE 3 — DATABASE ARCHITECTURE  
**Project Root:** `H:\people`  
**Owner:** People Intake System Program  
**Approval Authority:** Decision Log D-072  
**Created Date:** 2026-07-26  
**Last Updated:** 2026-07-26  
**Governing Documents:** IS-100; IS-102; IS-200; IS-201; IS-202; Catalogs 01/03/08; Volume 9 (subordinate depth); D-018/D-029…032  
**Dependencies:** PEOPLE-IS-202 APPROVED (D-071); ADR-002/003 remain OPEN (provider/ORM brands)  
**Implementation Authorization:** `IMPLEMENTATION NOT AUTHORIZED`

```text
DESIGN COMPLETE
APPROVED FOR DOCUMENTATION GOVERNANCE
PHASE 3 STARTED
DATABASE IS A PROJECTION OF THE DOMAIN — NOT ITS SOURCE
NO MIGRATIONS / SQL / PRISMA / SEEDS / INDEXES / TRIGGERS IN THIS PACKAGE
APPLICATION IMPLEMENTATION NOT AUTHORIZED
```

**Guiding principle (locked):**

> The database is an implementation of the domain—not the source of the domain.

**Subordinate companions:** `docs/04_data/PEOPLE_INTAKE_DATABASE_ARCHITECTURE.md`; Volume 9; `docs/10_database_specifications/*` (bootstrap drafts). Where they conflict with IS-200…202 or this IS, **IS-200…300 win**.

---

## 1. Purpose

Define the persistence architecture so that future tables, constraints, and migrations are a **faithful map** of approved entities (IS-201) and fields/value objects (IS-202)—never an independent invention surface.

## 2. Scope

Persistence philosophy; aggregate-to-table mapping strategy; identity / PK / FK policy; ownership boundaries; normalization; write vs read model philosophy; soft-delete and archival; audit persistence; concurrency/versioning; sensitive-data segregation; naming; schema organization; migration governance (docs only); scaling/partition considerations; traceability to IS-200…202; persistence extension doctrine.

## 3. Out of Scope (hard forbid for this package)

```text
FORBIDDEN IN PEOPLE-IS-300:
  migrations/ or SQL files
  Prisma schema or generated models
  seed data / fixtures with real PII
  live indexes, triggers, functions, extensions applied to a database
  database provisioning or credentials
  destructive data operations
  inventing tables/columns without IS-201/IS-202 admission
```

Physical column-level catalogs and constraint DDL language deepen in **IS-301+** still as documentation until Gate G-10 / `migrationsAuthorized`.

## 4. Governing References

IS-200 domain; IS-201 entities; IS-202 fields/VOs; Catalog 01 states; Catalog 03 audit; Catalog 08 classification; IS-102 module ownership; IS-100 `database/` home; ADR-002/003 OPEN.

## 5. Definitions

| Term | Meaning |
| --- | --- |
| Write model | Tables optimized for transactional integrity of aggregates |
| Read model | Query/projection structures that must not become a second write authority |
| Table seed name | Conceptual name (e.g. `intake_batches`) — not deployed schema |
| Persistence rule | Architectural rule in this IS governing how domain maps to storage |
| Additive migration | Future change that expands without silent destructive rewrite (when authorized) |

## 6. Assumptions

* Hosted PostgreSQL recommended (IS-101 / ADR-002 OPEN).  
* ORM (Prisma recommended) behind adapters (ADR-003 OPEN).  
* Shared DB compatibility audit required before real migrations (Volume 9 / prior docs).  
* Canonical person tables are **outside** intake ownership.  

## 7. Functional Requirements

| ID | Description |
| --- | --- |
| REQ-DBA-001 | Every persisted table/column MUST trace to an IS-201 entity and/or IS-202 field/VO (or explicit EXTERNAL boundary). |
| REQ-DBA-002 | No persistence artifact MAY invent business concepts absent from IS-200…202. |
| REQ-DBA-003 | Primary keys MUST be opaque UUIDs (or equivalent); never email/phone/name as PK. |
| REQ-DBA-004 | Human-readable codes MAY exist as secondary unique attributes (non-PII). |
| REQ-DBA-005 | Foreign keys MUST respect aggregate/module ownership; consumers do not own parent rows. |
| REQ-DBA-006 | Lifecycle/state columns MUST store Catalog 01 values only (`VO-CAT01-STATE`). |
| REQ-DBA-007 | Raw and normalized values MUST remain separate columns where IS-202 requires. |
| REQ-DBA-008 | Match resolution persistence MUST NOT write canonical person master tables. |
| REQ-DBA-009 | Promotion persistence is the intake path that records canonical create/link outcomes via ports. |
| REQ-DBA-010 | Audit events MUST be append-only. |
| REQ-DBA-011 | One active claim per page/work type MUST be enforceable (unique partial index intent). |
| REQ-DBA-012 | `(batch_id, page_number)` and `(page_id, row_number)` uniqueness MUST be enforceable. |
| REQ-DBA-013 | Idempotency keys for promotion (and similar) MUST be uniquely constrained in scope. |
| REQ-DBA-014 | Soft-delete/archive MUST align with Catalog 01 archival machines and Catalog 08 retention—not ad hoc flags that bypass state machines. |
| REQ-DBA-015 | Sensitive columns MUST map to Catalog 08 classifications; secrets never in DB docs as values. |
| REQ-DBA-016 | Future migrations (when authorized) MUST be additive-first and Decision-Log/package governed. |
| REQ-DBA-017 | This package MUST NOT create migrations, SQL, Prisma, seeds, or live schema objects. |

## 8. Nonfunctional Requirements

| ID | Description |
| --- | --- |
| NFR-DBA-HONEST-001 | Do not assume conceptual tables already exist in any shared database. |
| NFR-DBA-SCALE-001 | Partition/sharding notes are future considerations, not deployment orders. |
| NFR-DBA-SEC-001 | Least privilege DB roles planned for app vs migration vs read replicas (ops later). |

## 9. Architecture

### 9.1 Persistence philosophy

```text
Business Domain (IS-200)
  → Entities (IS-201)
    → Fields / VOs (IS-202)
      → Persistence Architecture (IS-300)   ← this document
        → Logical table catalog (IS-301+)
          → Authorized migrations / ORM (Gate G-10 + package)
```

Authority is **one-directional**. Schema changes that invent domain concepts are rejected.

### 9.2 Persistence extension doctrine (locked)

```text
New persistence requirement?
  → Existing Entity? (IS-201)
      → Existing Field? (IS-202)
          → Existing Value Object?
              → Existing Persistence Rule? (this IS / IS-301+)
                  YES → Reuse
                  NO  → Update IS-300/IS-301+ or create ADR
                        → Only then may future packages create tables/schemas/migrations
```

### 9.3 Aggregate-to-table mapping strategy

| Strategy | When |
| --- | --- |
| **One aggregate root ≈ one primary table** | Batch, Page, Claim, Resolution, Promotion Request, User |
| **Child rows in related tables** | Candidates under evaluation; image versions under image; corrections under entry |
| **Projection / read tables** | Queue item may be view or derived table — **no claim writes** |
| **EXTERNAL schemas** | Canonical person/attributes — not owned by intake migrations |
| **Append-only tables** | Audit events; selected histories |

Do not flatten Match Resolution into Promotion tables. Do not store canonical master attributes on `intake_entries` beyond linkage IDs after successful promotion.

### 9.4 Conceptual table map (seeds — not DDL)

| Domain aggregate / entity | Table seed (conceptual) | Owner module |
| --- | --- | --- |
| Batch | `intake_batches` | MOD-BATCHES |
| Page | `intake_pages` | MOD-PAGES |
| Entry | `intake_entries` | MOD-DRAFTS / MOD-TRANSCRIPTIONS (ISSUE-MOD-001) |
| Entry corrections (if separate) | `intake_entry_corrections` | MOD-TRANSCRIPTIONS |
| Claim | `intake_page_claims` | MOD-CLAIMS |
| Queue projection | view/table TBD | MOD-QUEUES |
| Source image | `intake_source_images` | MOD-UPLOADS |
| Upload attempt | `intake_upload_attempts` | MOD-UPLOADS |
| Image versions | `intake_image_versions` | MOD-UPLOADS |
| Match evaluation run | `intake_match_runs` | MOD-MATCHING |
| Match candidate | `intake_match_candidates` | MOD-MATCHING |
| Match resolution | `intake_match_resolutions` | MOD-RESOLUTION |
| Promotion request | `intake_promotion_requests` | MOD-PROMOTION |
| Promotion result (if split) | `intake_promotion_results` | MOD-PROMOTION |
| Audit event | `intake_audit_events` | MOD-AUDIT |
| Processing error | `intake_processing_errors` | MOD-OPERATIONS |
| Application user | `app_users` | MOD-USERS |
| Canonical person* | EXTERNAL | Canonical domain |

\*Names TBD after shared-DB audit; intake stores linkage only.

### 9.5 Identity strategy

| Kind | Rule |
| --- | --- |
| Surrogate PK | UUID (or equivalent opaque ID) — `VO-UUID` |
| Natural keys | Forbidden as PK (email, phone, name+ZIP) |
| Operational codes | Secondary unique (`batch_code`, `page_code`, `entry_code`) — non-PII |
| External IDs | Canonical person IDs stored as linkage columns only after promotion success |
| Public sequential IDs | Avoid (volume leakage) |

### 9.6 Primary key policy

* Every intake-owned table has exactly one surrogate PK.  
* PKs immutable.  
* Composite PKs discouraged; use surrogate PK + unique constraints for natural uniqueness.  

### 9.7 Foreign key policy

* FKs express IS-200 relationships (Batch→Page→Entry, etc.).  
* ON DELETE: prefer restrict/protect for business parents; cascade only where aggregate deletion rules explicitly allow (future IS-301).  
* Cross-module FK reads allowed; **writes** only by owning module.  
* No FK from intake into RedDirt operational tables for routine intake.  
* Canonical person references are logical/external — physical FK only if shared-DB audit approves.

### 9.8 Ownership boundaries in persistence

| May persist under intake | Must not |
| --- | --- |
| intake_* write models; app_users; intake audit/errors | Canonical master person/attribute/merge tables as intake-owned |
| Promotion request/result rows | Match resolution writing person attributes |
| Private image **keys/refs** | Public object URLs as identity; secrets in columns documented as samples |

Module ownership (IS-102) governs which service may INSERT/UPDATE which tables.

### 9.9 Normalization strategy

* **Logical 3NF-oriented write model** for intake core.  
* Do not collapse raw/normalized/condition into one overloaded column.  
* Do not duplicate resolution outcome onto promotion as a second authority — promotion references `resolution_id`.  
* Controlled denormalization only for explicit read models with refresh rules (IS-301+ / reports ISSUE-MOD-002).  

### 9.10 Write model vs read model

| Model | Role | Rules |
| --- | --- | --- |
| Write | Source of truth for aggregates | Enforce Catalog 01, uniqueness, invariants |
| Read | Query convenience (queue, reports) | No bypass of write invariants; no dual claim store |

CQRS-lite is allowed; event sourcing is **not** required for V1.

### 9.11 Soft-delete and archival philosophy

* Prefer Catalog 01 archival/destruction machines (`STATE-ARCHIVE-001` etc.) over anonymous `is_deleted` that bypasses lifecycle.  
* Soft-delete flags, if used, MUST map to defined states and retention classes.  
* Legal hold / destruction: Catalog 08 — no silent hard delete of RESTRICTED evidence without policy.  

### 9.12 Audit persistence strategy

* `intake_audit_events` append-only.  
* Event names = Catalog 03 only.  
* Payload: structured facts; **no secrets**; classify per Catalog 08.  
* Correlation IDs: batch/page/entry/promotion/claim as applicable.  

### 9.13 Concurrency / versioning philosophy

* Optimistic concurrency via `version` / `VO-OPT-LOCK` on mutable aggregates (pages, entries, claims as designed).  
* Conflict → fail closed (`STALE_VERSION` posture per ADR-015 OPEN).  
* Submitted transcription revisions immutable; corrections via formal correction records/history.  
* Match evaluation immutable after completion; supersede via new run row.  

### 9.14 Sensitive-data segregation

| Class (Cat 08) | Persistence note |
| --- | --- |
| CLASS-002 INTERNAL | Standard intake metadata |
| CLASS-003 CONFIDENTIAL | Names, locations, preferences |
| CLASS-004 RESTRICTED | Email/phone raw+norm; image storage keys |
| CLASS-005 SYSTEM_SECRET | **Not** in business tables; env/secret stores only |

Encryption-at-rest / column encryption brands: PENDING provider ADRs — document requirement, do not invent vendor config here.

### 9.15 Naming conventions

| Object | Convention |
| --- | --- |
| Intake tables | `intake_<plural_snake>` |
| App/auth tables | `app_<plural_snake>` |
| PK column | `id` (UUID) |
| FK column | `<entity>_id` |
| State column | `lifecycle_state` (Catalog 01) |
| Timestamps | `*_at` UTC |
| Raw/norm/condition | `<field>_raw` / `<field>_normalized` / `<field>_condition` |
| Indexes (future) | `ix_<table>_<cols>`; unique `uq_<table>_<cols>` |

### 9.16 Schema organization

| Area | Content |
| --- | --- |
| Intake schema/search_path | intake_* write models |
| App schema | users/roles (or public with prefix — finalize IS-301) |
| Canonical | Separate ownership; integration by port |
| Migrations home (future) | `database/migrations` per IS-100 — **not created now** |

### 9.17 Migration governance (documentation only)

When Gate G-10 / `migrationsAuthorized` opens:

1. Shared DB compatibility audit report first.  
2. Additive migrations preferred; expand/contract for renames.  
3. Separate migration credentials from app runtime.  
4. Each migration cites package ID + IS-201/202 trace + rollback notes.  
5. No undocumented production tables.  
6. Prisma/SQL artifacts only inside authorized packages.  

IS-300 does **not** authorize starting that sequence.

### 9.18 Partitioning / scaling (future)

* Consider time/batch-based partitioning for audit and large image metadata later.  
* Do not pre-partition in V1 docs as mandatory.  
* Read replicas: ops IS later; write authority remains primary.  

### 9.19 Indexing intent (not DDL)

Documented intent only (implement in authorized packages):

* Unique: `(batch_id, page_number)`, `(page_id, row_number)`, active claim partial unique, idempotency keys  
* Lookup: `lifecycle_state`, FK columns, normalized email/phone for match (careful with PII indexes)  
* Hash: `sha256_hash` for dedupe  

Exact index DDL → IS-301+ / migration packages.

### 9.20 Transaction boundary intent

Align with Volume 8 / IS-200:

* Claim acquire atomic  
* Draft save vs submit revision boundaries  
* Promotion request durable before async canonical call  
* Resolution finalize does not include canonical write  

## 10. Data Contracts

Logical only. Column catalogs → IS-301. Types map from IS-202 VOs (UUID, enums as Cat01/text+check, timestamps timestamptz, etc.) — physical types chosen when ADR-002 accepted.

## 11. Interface Contracts

Persistence accessed only through owning module repositories/adapters — never UI→SQL. Canonical integration via promotion port (ISSUE-CANONICAL-001).

## 12–16. State / Permission / Error / Audit / Jobs

* State columns = Catalog 01.  
* DB roles ≠ Catalog 5 page permissions (separate concerns).  
* Migration failures = ops/errors Catalog 2 when implemented.  
* Schema change audit recommended in ops packages.  
* Background jobs never create ad hoc tables.  

## 17. Security and Privacy

* No production credentials in repo.  
* No real PII in seeds/docs.  
* Private image binary outside Postgres; DB holds refs/hashes.  

## 18. Retention

Catalog 08 classes drive purge/archive jobs later; schema must not prevent retention enforcement.

## 19. Observability

Slow-query and migration logs in ops IS; correlate by entity IDs.

## 20. Testing (future packages)

* Uniqueness/invariant tests  
* Illegal state writes rejected  
* Append-only audit  
* No canonical write from resolution paths  
* Migration dry-run when authorized  

## 21. Acceptance Criteria

| ID | Criterion | Met? |
| --- | --- | --- |
| AC-DBA-001 | Guiding principle locked (DB projects domain) | Yes |
| AC-DBA-002 | Aggregate→table strategy documented | Yes |
| AC-DBA-003 | PK/FK/identity/uniqueness policies documented | Yes |
| AC-DBA-004 | Write vs read, audit, concurrency, soft-delete/archive documented | Yes |
| AC-DBA-005 | Sensitive-data segregation via Catalog 08 documented | Yes |
| AC-DBA-006 | Naming + schema organization + migration governance documented | Yes |
| AC-DBA-007 | Traceability to IS-200…202 stated | Yes |
| AC-DBA-008 | Persistence extension doctrine locked | Yes |
| AC-DBA-009 | No migrations/SQL/Prisma/seeds created by this package | Yes |

## 22. Open Decisions

| ID | Notes |
| --- | --- |
| ADR-002 / ISSUE-DATABASE-001 | Hosted Postgres brand / shared DB facts |
| ADR-003 | ORM packaging |
| ISSUE-MOD-001 | Entry table writer split / correction table shape |
| ISSUE-CANONICAL-001 | Whether physical FK to canonical is possible |
| ISSUE-MOD-002 | Reports read-model tables |
| STATE-DEC-* | Derived vs persisted counters/states |
| Exact schemas/search_path | IS-301 |

## 23. Risks

| ID | Risk | Mitigation |
| --- | --- | --- |
| RISK-DBA-001 | Schema invents domain | REQ-DBA-001/002; doctrine §9.2 |
| RISK-DBA-002 | Draft UX statuses stored | REQ-DBA-006 |
| RISK-DBA-003 | Resolution writes persons | REQ-DBA-008 |
| RISK-DBA-004 | Creating migrations “to be helpful” | REQ-DBA-017 |
| RISK-DBA-005 | Assuming tables exist in shared DB | NFR-DBA-HONEST-001 |

## 24. Dependencies

IS-200…202; Catalogs 01/03/08; open ADRs for provider/ORM; shared DB audit before migrate.

## 25. Traceability

| From | To |
| --- | --- |
| ENT-* / FLD-* / VO-* | Table seeds + column intent |
| Catalog 01 | `lifecycle_state` columns |
| Catalog 03 | audit table event_name |
| Catalog 08 | sensitivity / retention |
| IS-102 | table write ownership |

Status: FULLY_MAPPED (architecture); physical DDL PARTIALLY_MAPPED → IS-301+.

## 26. Implementation Boundary

**Authorized:** this specification; indexes/registers; subordinate banners; empty `300_database/` docs folder.  
**Forbidden:** any executable schema artifact listed in §3.

## 27. Revision History

| Version | Date | Change | Approval |
| --- | --- | --- | --- |
| 1.0 | 2026-07-26 | Phase 3 persistence architecture (docs only) | D-072 |

## Next primary

```text
PEOPLE-IS-301-LOGICAL-TABLE-CATALOG-1.0
```

## Independent lane

```text
PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0
(continue Critical ADR visibility; do not block IS-301 absent a true gate)
```

## Final status

```text
PEOPLE-IS-300 DATABASE ARCHITECTURE: APPROVED (DOCUMENTATION)
PHASE 3: STARTED
MIGRATIONS / SQL / PRISMA: NOT CREATED — NOT AUTHORIZED
APPLICATION IMPLEMENTATION: NOT AUTHORIZED
```
