# PEOPLE-IS-304 — READ MODEL SPECIFICATIONS

**Title:** Read Model Specifications  
**Document ID:** `PEOPLE-IS-304-READ-MODEL-SPECIFICATIONS-1.0`  
**Version:** 1.0  
**Status:** APPROVED  
**Phase:** PHASE 3 — DATABASE ARCHITECTURE  
**Project Root:** `H:\people`  
**Owner:** People Intake System Program  
**Approval Authority:** Decision Log D-076  
**Created Date:** 2026-07-26  
**Last Updated:** 2026-07-26  
**Governing Documents:** IS-300; IS-301; IS-302; IS-303; IS-200…202; Catalogs 01/05/08  
**Dependencies:** PEOPLE-IS-303 APPROVED (D-075)  
**Implementation Authorization:** `IMPLEMENTATION NOT AUTHORIZED`

```text
DESIGN COMPLETE
APPROVED FOR DOCUMENTATION GOVERNANCE
CANONICAL LOGICAL READ-MODEL CATALOG
READ MODELS PROJECT TRUTH — THEY DO NOT CREATE TRUTH
NO SQL / VIEWS AS EXECUTABLE ARTIFACTS / MATERIALIZED TABLES / PRISMA / MIGRATIONS
APPLICATION IMPLEMENTATION NOT AUTHORIZED
```

---

## 1. Purpose

Define every **logical read model** required for efficient presentation to users and systems **without redefining the source of truth**. Write-model ownership remains in LT-*/REL-*/CON-*; read models only **project** governed state for consumption.

## 2. Scope

Read-model admission questionnaire; complete `RM-*` cards; projection boundaries; technology-neutral refresh/consistency expectations; filter/sort/pagination; aggregations and derived fields; security trimming; Catalog 08 sensitivity; audit visibility; retention; ownership; traceability; future package ownership.

## 3. Out of Scope

```text
FORBIDDEN:
  CREATE VIEW / MATERIALIZED VIEW / indexed projection DDL
  Prisma read replicas, CQRS frameworks as executable code
  Caching, Redis, Elasticsearch, or query-engine choices
  Inventing business states, entities, or relationships in projections
  Dual-write “reporting tables” that become alternate truth
```

Physical view/table/index choices → IS-305 / authorized packages after Gate G-10.  
Migration sequencing → **IS-305**.

## 4. Standing doctrine (locked)

```text
Read models exist for consumption,
not ownership.

Read models project truth.
They do not create truth.

A read model may derive information.
It may never redefine an approved business concept.

Read models are disposable.
The governed domain is authoritative.
```

### 4.1 Extension tree

```text
Need a new query/presentation surface?
  → Existing RM-* in this catalog?
      YES → Reuse / amend card
      NO  → Does LT-*/REL-*/CON-* already supply the facts?
              YES → Amend IS-304 (projection only)
              NO  → Does domain need a new concept?
                      YES → Update IS-200…303 first, then amend IS-304
                      NO  → Reject
                            → Only then may packages implement the projection
```

### 4.2 Consistency vocabulary (business, not tech)

| Term | Meaning in this IS |
| --- | --- |
| `IMMEDIATE` | Consumer must see write-model outcome on next successful read of that concern (e.g. active claim holder after acquire) |
| `BOUNDED` | Stale window acceptable within a named business bound (e.g. ops counters within minutes) |
| `EVENTUAL` | Eventually consistent is acceptable; must not invent interim business states |

These are **business expectations**, not mandates for sync replication, CDC, or materialized views.

## 5. Mandatory read-model questionnaire

| # | Area | Questions |
| --- | --- | --- |
| M1 | Identity | Stable `RM-*` ID |
| M2 | Identity | Canonical name |
| M3 | Purpose | Business purpose |
| M4 | Consumers | Primary consumers (UI / API / reporting / export / workflow / ops) |
| M5 | Sources | Source logical tables (`LT-*`) |
| M6 | Sources | Source relationships (`REL-*`) |
| M7 | Sources | Source constraints (`CON-*`) |
| M8 | Boundary | Projection boundary (what is included / excluded) |
| M9 | Refresh | Refresh/update expectation (technology-neutral) |
| M10 | Consistency | Consistency expectation (`IMMEDIATE` / `BOUNDED` / `EVENTUAL`) |
| M11 | Query | Filter expectations |
| M12 | Query | Search expectations |
| M13 | Query | Sort expectations |
| M14 | Query | Pagination expectations |
| M15 | Derive | Aggregation responsibilities |
| M16 | Derive | Derived fields (must cite formula / source; no new business meaning) |
| M17 | Security | Security trimming (Catalog 05) |
| M18 | Sens | Sensitivity propagation (Catalog 08) |
| M19 | Audit | Audit visibility |
| M20 | Retention | Retention behavior |
| M21 | Ownership | Owning module / builder (never claim/resolution write owners) |
| M22 | Trace | Traceability to IS-200…303 |
| M23 | Package | Future implementation package ownership |
| M24 | Forbid | Explicit forbidden writes / forbidden invented fields |

---

## 6. Functional Requirements

| ID | Description |
| --- | --- |
| REQ-RM-001 | Every governed presentation/query surface MUST have an `RM-*` card before physical projection. |
| REQ-RM-002 | Read models MUST NOT accept authoritative writes for claims, resolutions, promotions, or Catalog 01 state. |
| REQ-RM-003 | Read models MUST NOT redefine Catalog 01 states, entities, fields, relationships, or constraints. |
| REQ-RM-004 | Derived fields MUST cite source LT/REL/CON facts and MUST NOT invent domain meaning. |
| REQ-RM-005 | Queue and worklist projections MUST remain non-owners (CON-OWN-QUEUE-READONLY). |
| REQ-RM-006 | Security trimming MUST apply before sensitive projection (Cat 05/08). |
| REQ-RM-007 | New read models require IS-304 amendment or ADR — and upstream IS if new facts are needed. |
| REQ-RM-008 | This package MUST NOT create SQL views, materialized tables, Prisma, migrations, or caches. |

---

## 7. Read model catalog

### RM-QUEUE-WORKLIST — Transcription / work queue

| Field | Value |
| --- | --- |
| M1–M3 | `RM-QUEUE-WORKLIST` / QueueWorklist / Shared worklist of pages available or held for transcription (and related work types) |
| M4 | UI queue; queue API; workflow assignment surfaces |
| M5 | LT-PAGE, LT-BATCH, LT-CLAIM (overlay), LT-QUEUE (logical), LT-IMAGE (active ref display meta only) |
| M6 | REL-QUEUE-PAGE, REL-QUEUE-CLAIM, REL-BATCH-PAGE, REL-PAGE-CLAIM-ACTIVE, REL-PAGE-IMAGE-ACTIVE |
| M7 | CON-OWN-QUEUE-READONLY, CON-UNQ-CLAIM-ACTIVE, CON-REQ-STATE-CAT01, CON-LIFE-CAT01-ONLY |
| M8 | **Includes:** page id, batch context, Cat 01 page/claim presentation codes, active claim holder/expiry if any, priority, ordinal hints. **Excludes:** claim create/update, draft body PII unless authorized screen, resolution/promotion writes |
| M9 | Rebuild/project from write model on read or via disposable projection; claim overlay must track claim service outcomes |
| M10 | `IMMEDIATE` for active claim holder/availability; `BOUNDED` acceptable for secondary counters |
| M11–M14 | Filter by state/work type/priority/batch; search by page/batch codes (non-PII); sort priority then age/ordinal; cursor/offset pagination |
| M15–M16 | Optional derived `is_available`, `claim_remaining` from claim expiry + Cat 01 — must not invent new states |
| M17–M18 | Trim by queue/view permissions (Cat 05); CLASS-002 floor; no public image URLs |
| M19–M20 | Does not own audits; underlying page/claim audits; disposable with write-model retention |
| M21 | Queue projection builder / MOD-QUEUE — **never** claim service |
| M22–M23 | ENT-QUEUE-ITEM; IS-301 LT-QUEUE; queue read-model pkg |
| M24 | **Forbid** claim writes; **forbid** alternate Catalog 01 vocabulary |

### RM-BATCH-LIST — Batch administration list

| Field | Value |
| --- | --- |
| M1–M3 | `RM-BATCH-LIST` / BatchList / Ops list of batches with summary counts |
| M4 | Admin UI; batch API list |
| M5 | LT-BATCH; derived counts from LT-PAGE / LT-ENTRY |
| M6 | REL-BATCH-PAGE; REL-PAGE-ENTRY |
| M7 | CON-ID-BATCH-CODE, CON-REQ-STATE-CAT01, CON-CARD-ENTRIES-MAX10 (indirect) |
| M8 | Batch identity, Cat 01 batch state, priority, source type, page/entry **counts** — not full page payloads |
| M9 | Counts may be maintained as disposable aggregates or computed |
| M10 | `BOUNDED` for counts; `IMMEDIATE` for batch identity/state after batch writes |
| M11–M14 | Filter state/priority/source; search batch_code; sort created/priority; paginate |
| M15–M16 | `page_count`, `entry_count` derived — must match write-model cardinality, not invent entries |
| M17–M18 | Admin roles; CLASS-002 |
| M19–M20 | Batch lifecycle audits elsewhere; retention with batch |
| M21 | MOD-BATCHES read surfaces |
| M22–M23 | IS-201 ENT-BATCH; batch pkg |
| M24 | Must not store people; must not invent batch states |

### RM-BATCH-DETAIL — Batch detail with page index

| Field | Value |
| --- | --- |
| M1–M3 | `RM-BATCH-DETAIL` / BatchDetail / Single batch + ordered page index |
| M4 | Admin/capture UI; batch detail API |
| M5 | LT-BATCH, LT-PAGE |
| M6 | REL-BATCH-PAGE |
| M7 | CON-UNQ-PAGE-NUMBER, CON-REQ-PAGE-BATCH |
| M8 | Batch header + pages ordered by `page_number`; no full entry PII dump unless authorized child view |
| M9–M10 | `IMMEDIATE` after page add/reorder; |
| M11–M14 | Page filter by page state; sort by page_number; paginate large batches |
| M15–M16 | Optional completion ratio from Cat 01 page states — formula only |
| M17–M18 | Batch view permissions; CLASS-002 |
| M21–M24 | MOD-BATCHES/PAGES; forbid page move inventing transfer rules not in domain |

### RM-PAGE-TRANSCRIPTION — Transcription workspace projection

| Field | Value |
| --- | --- |
| M1–M3 | `RM-PAGE-TRANSCRIPTION` / PageTranscriptionWorkspace / Page + entries + active image meta for transcription |
| M4 | Transcription UI; page/entry APIs (read) |
| M5 | LT-PAGE, LT-ENTRY, LT-IMAGE, LT-IMAGE-VERSION, LT-CLAIM, LT-ENTRY-CORRECTION (history panel) |
| M6 | REL-PAGE-ENTRY, REL-PAGE-IMAGE-ACTIVE, REL-IMAGE-VERSION, REL-PAGE-CLAIM-ACTIVE, REL-ENTRY-CORRECTION |
| M7 | CON-CARD-ENTRIES-MAX10, CON-UNQ-ENTRY-ROW, CON-REF-PAGE-IMAGE-ACTIVE, CON-IMM-SUBMITTED-REVISION, CON-UNQ-CLAIM-ACTIVE, CON-SENS-NO-PUBLIC-IMAGE |
| M8 | **Includes:** page state, ≤10 entries with raw/normalized/condition layers, active image private ref/meta, claim overlay for holder. **Excludes:** writing claims via this RM; inventing 11th entry; public CDN identity |
| M9–M10 | `IMMEDIATE` for entries/claim/image active ref after successful writes |
| M11–M14 | Entry sort by row_number; no cross-page search in this RM |
| M15–M16 | `entry_count`, blank-row gaps as **absence** of entities — never fabricate entry rows |
| M17–M18 | Transcription permissions; CLASS-003–004 on entry/image; trim fields by role |
| M19–M20 | Transcription/correction audits via audit RM; retention with evidence |
| M21 | Transcription read surfaces; claim writes remain claim service |
| M22–M23 | IS-201 page/entry/image; transcription UI pkg |
| M24 | **Forbid** claim writes; **forbid** UNKNOWN→NO coercion in projection |

### RM-ENTRY-MATCHING — Matching workspace projection

| Field | Value |
| --- | --- |
| M1–M3 | `RM-ENTRY-MATCHING` / EntryMatchingWorkspace / Entry + match runs/candidates + current resolution projection |
| M4 | Matching UI; matching API reads |
| M5 | LT-ENTRY, LT-MATCH-RUN, LT-MATCH-CANDIDATE, LT-MATCH-RESOLUTION |
| M6 | REL-ENTRY-MATCH-RUN, REL-MATCH-RUN-CANDIDATE, REL-CANDIDATE-PERSON, REL-ENTRY-RESOLUTION |
| M7 | CON-XAGG-MATCH-NE-PROMO, CON-XAGG-RESOLUTION-NO-PERSON-WRITE, CON-XAGG-SHARED-CONTACT-NE-IDENTITY, CON-IMM-MATCH-RUN, CON-CARD-ACTIVE-RESOLUTION, CON-EXT-CANONICAL-SOFT-REF |
| M8 | Shows candidates and resolution **outcomes**; displays external person ids as soft refs; **does not** write person masters or perform promotion |
| M9–M10 | `IMMEDIATE` after match run/resolution writes |
| M11–M14 | Filter candidates by score band; sort score desc; paginate candidate lists |
| M15–M16 | Display scores/reasons from write model; must not invent identity certainty |
| M17–M18 | Matching permissions; CLASS-003 |
| M21 | Matching read surfaces — resolution writes stay resolution service |
| M22–M23 | Matching/resolution pkgs |
| M24 | **Forbid** promotion actions as if they were match; **forbid** person master writes |

### RM-PROMOTION-STATUS — Promotion request status projection

| Field | Value |
| --- | --- |
| M1–M3 | `RM-PROMOTION-STATUS` / PromotionStatusView / Promotion requests/results for an entry or queue of promotions |
| M4 | Promotion UI; promotion API; ops exception workflows |
| M5 | LT-PROMOTION, LT-PROMOTION-RESULT, LT-ENTRY, LT-MATCH-RESOLUTION |
| M6 | REL-RESOLUTION-PROMOTION, REL-PROMOTION-ENTRY, REL-PROMOTION-RESULT, REL-PROMOTION-PERSON, REL-ENTRY-PERSON-LINK |
| M7 | CON-XAGG-MATCH-NE-PROMO, CON-TEMP-MATCH-BEFORE-PROMOTE, CON-UNQ-PROMO-IDEMPOTENCY, CON-XAGG-LINKED-PERSON-VIA-PROMO, CON-EXT-CANONICAL-SOFT-REF |
| M8 | Promotion Cat 01 state, idempotency identity, result history, linked person soft ref after success — **does not** redefine match outcome |
| M9–M10 | `IMMEDIATE` after promotion service writes; external person confirmation may be `BOUNDED` pending port (ISSUE-CANONICAL-001) |
| M11–M14 | Filter by promotion state; sort updated_at; paginate |
| M15–M16 | Latest result derived from append-only results |
| M17–M18 | Promotion permissions; CLASS-003–004 |
| M21 | MOD-PROMOTION read surfaces |
| M22–M23 | Promotion pkg; ISSUE-CANONICAL-001 visible |
| M24 | **Forbid** rewriting resolution via this RM |

### RM-AUDIT-TIMELINE — Audit correlation timeline

| Field | Value |
| --- | --- |
| M1–M3 | `RM-AUDIT-TIMELINE` / AuditTimeline / Chronological audit events for a subject (batch/page/entry/claim/promotion) |
| M4 | Audit UI component; admin forensics API |
| M5 | LT-AUDIT |
| M6 | REL-AUDIT-CORRELATION |
| M7 | CON-APP-AUDIT, CON-RET-AUDIT-HOLD, CON-SENS-CLASS-PROPAGATE |
| M8 | Append-only event projection; may redact payload fields by role; **never** mutates audit rows |
| M9–M10 | `IMMEDIATE` after audit append for that subject correlation |
| M11–M14 | Filter by domain/event type/time; sort time asc/desc; paginate |
| M15–M16 | None that invent events |
| M17–M18 | Elevated audit permissions; payload class trimming |
| M19–M20 | Is the audit view; retention per Cat 08 / holds |
| M21 | Audit read surfaces |
| M22–M23 | Audit pkg |
| M24 | **Forbid** update/delete through RM |

### RM-ERROR-OPS — Processing error / exception list

| Field | Value |
| --- | --- |
| M1–M3 | `RM-ERROR-OPS` / ProcessingErrorOpsList / Operator-facing processing errors |
| M4 | Exception workflows UI; ops API |
| M5 | LT-ERROR; optional subject joins to LT-PAGE/LT-ENTRY |
| M6 | REL-ERROR-SUBJECT |
| M7 | CON-REQ-STATE-CAT01 where error has lifecycle; soft refs preferred |
| M8 | Error identity, classification placeholders (Cat 02), subject soft refs, remediation flags — not a second queue of claims |
| M9–M10 | `IMMEDIATE` after error write; |
| M11–M14 | Filter open/closed/type; sort severity/time; paginate |
| M17–M18 | Ops roles; avoid leaking CLASS-004 in list cards |
| M21 | Ops/error read surfaces |
| M22–M23 | Ops pkg |
| M24 | Must not become claim writer |

### RM-OPS-SUMMARY — Operations summary counters

| Field | Value |
| --- | --- |
| M1–M3 | `RM-OPS-SUMMARY` / OpsSummaryCounters / High-level counts by Catalog 01 states for dashboards |
| M4 | Ops dashboard UI; reporting API (internal) |
| M5 | Aggregates over LT-BATCH, LT-PAGE, LT-CLAIM, LT-PROMOTION (counts only) |
| M6 | Uses REL-* only for join keys as needed |
| M7 | CON-LIFE-CAT01-ONLY — counters keyed **only** by Catalog 01 codes |
| M8 | Counts and ratios; **no** PII entry payloads; **no** invented “dashboard states” |
| M9–M10 | `BOUNDED` / `EVENTUAL` acceptable |
| M11–M14 | Filter time window/batch; limited sort; single-page or coarse pagination |
| M15–M16 | Counts by Cat 01 state; completion ratios — formulas only |
| M17–M18 | Ops admin; CLASS-002 aggregates |
| M21 | Ops reporting builder (disposable) |
| M22–M23 | Reporting pkg; **ISSUE-MOD-002** may add further report RMs via amendment |
| M24 | **Forbid** using summary as write authority; **forbid** non-Cat-01 status buckets |

### RM-USER-ADMIN — User and role grant projection

| Field | Value |
| --- | --- |
| M1–M3 | `RM-USER-ADMIN` / UserAdminList / Users and role grants for administration |
| M4 | Admin UI; session/user API reads |
| M5 | LT-USER, LT-ROLE-GRANT |
| M6 | REL-USER-ROLE |
| M7 | CON-UNQ-USER-EMAIL (provider-dependent ADR-004), CON-REF-ROLE-USER |
| M8 | User identity, roles, status — not auth secrets |
| M9–M10 | `IMMEDIATE` after role grant changes |
| M11–M14 | Filter role/active; search email; sort name/email; paginate |
| M17–M18 | User-admin permissions; CLASS-004 email handling |
| M21 | MOD-USERS read surfaces |
| M22–M23 | Authz pkg |
| M24 | Must not project secrets/tokens |

### RM-CLAIM-ACTIVE-OVERLAY — Active claim overlay (shared fragment)

| Field | Value |
| --- | --- |
| M1–M3 | `RM-CLAIM-ACTIVE-OVERLAY` / ActiveClaimOverlay / Reusable projection of active claim for a page/work type |
| M4 | Embedded in queue/transcription UIs; not a standalone write API |
| M5 | LT-CLAIM, LT-USER (display name only) |
| M6 | REL-PAGE-CLAIM-ACTIVE, REL-CLAIM-USER |
| M7 | CON-UNQ-CLAIM-ACTIVE, CON-REQ-CLAIM-USER, CON-TEMP-CLAIM-EXPIRY, CON-OWN-CLAIM-SERVICE |
| M8 | Holder, work type, expiry, Cat 01 claim state |
| M9–M10 | `IMMEDIATE` |
| M21 | Built only from claim write model; queue may **consume**, never **write** |
| M24 | **Forbid** acquire/release through this RM |

---

## 8. Read model index

```text
RM-QUEUE-WORKLIST
RM-BATCH-LIST
RM-BATCH-DETAIL
RM-PAGE-TRANSCRIPTION
RM-ENTRY-MATCHING
RM-PROMOTION-STATUS
RM-AUDIT-TIMELINE
RM-ERROR-OPS
RM-OPS-SUMMARY
RM-USER-ADMIN
RM-CLAIM-ACTIVE-OVERLAY
```

## 9. Physical shape guidance (non-binding, non-SQL)

| Guidance | Note |
| --- | --- |
| Prefer disposable projections | Views, query joins, or rebuildable read stores — all must remain disposable |
| Queue VIEW vs table | Business constraint locked (read-only); physical choice deferred to IS-305 / packages |
| No dual-write reporting tables as truth | If a physical table is used for RM-*, it is still a projection under this IS |
| Indexes | Optimization only; must not encode new invariants (CON-* remain authority) |

## 10. Surfaced open items (not silently closed)

| ID | Topic | Disposition |
| --- | --- | --- |
| ISSUE-MOD-002 | Additional report READ_MODEL tables | Further RM-* via IS-304 amendment when justified |
| ISSUE-CANONICAL-001 | Canonical person DTO / confirmation latency | RM-PROMOTION-STATUS / matching soft refs; `BOUNDED` external confirmation |
| ISSUE-AUDIT-001 | Draft status vocabularies in old docs | RMs must use Cat 01 only (CON-LIFE-CAT01-ONLY) |
| Queue physical shape | VIEW vs table | Deferred to IS-305; CON-OWN-QUEUE-READONLY / REQ-RM-005 hold |

## 11. Acceptance Criteria

| ID | Criterion | Met? |
| --- | --- | --- |
| AC-RM-001 | Questionnaire M1–M24 defined | Yes |
| AC-RM-002 | Core consumer surfaces carded (queue, batch, transcription, matching, promotion, audit, ops, users) | Yes |
| AC-RM-003 | Read-model doctrine locked | Yes |
| AC-RM-004 | Non-ownership / non-truth rules locked | Yes |
| AC-RM-005 | Catalog 01 / Match≠Promotion / soft-ref preserved in RMs | Yes |
| AC-RM-006 | No SQL/views/Prisma/migrations/caches created | Yes |

## 12. Risks

| ID | Risk | Mitigation |
| --- | --- | --- |
| RISK-RM-001 | UI projection becomes alternate state authority | REQ-RM-002/003; doctrine §4 |
| RISK-RM-002 | Queue writes claims | REQ-RM-005; CON-OWN-QUEUE-READONLY |
| RISK-RM-003 | Dashboard invents status buckets | RM-OPS-SUMMARY M24; CON-LIFE-CAT01-ONLY |
| RISK-RM-004 | Reporting dual-write drifts from domain | Disposable RM rule; IS-305 governance |

## 13. Dependencies

IS-301; IS-302; IS-303; Catalog 01/05/08; open issues in §10.

## 14. Traceability

`RM-*` ↔ `LT-*` / `REL-*` / `CON-*` ↔ ENT-* — FULLY_MAPPED (logical).  
Physical projection artifacts → IS-305 / authorized packages.

## 15. Implementation Boundary

**Authorized:** this read-model catalog; governance; audit verification.  
**Forbidden:** executable views, materialized stores, Prisma, migrations, caches as project artifacts.

## 16. Revision History

| Version | Date | Change | Approval |
| --- | --- | --- | --- |
| 1.0 | 2026-07-26 | Logical read-model catalog | D-076 |

## Next primary

```text
PEOPLE-IS-305-MIGRATION-GOVERNANCE-1.0
```

## Independent lane

```text
PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0
```

## Final status

```text
PEOPLE-IS-304 READ MODEL SPECIFICATIONS: APPROVED (DOCUMENTATION)
READ MODELS PROJECT TRUTH — DO NOT CREATE TRUTH
READ MODELS ARE DISPOSABLE — DOMAIN IS AUTHORITATIVE
SQL / VIEWS / PRISMA / MIGRATIONS: NOT AUTHORIZED
```
