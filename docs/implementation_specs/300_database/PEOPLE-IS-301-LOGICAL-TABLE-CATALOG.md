# PEOPLE-IS-301 — LOGICAL TABLE CATALOG

**Title:** Logical Table Catalog  
**Document ID:** `PEOPLE-IS-301-LOGICAL-TABLE-CATALOG-1.0`  
**Version:** 1.0  
**Status:** APPROVED  
**Phase:** PHASE 3 — DATABASE ARCHITECTURE  
**Project Root:** `H:\people`  
**Owner:** People Intake System Program  
**Approval Authority:** Decision Log D-073  
**Created Date:** 2026-07-26  
**Last Updated:** 2026-07-26  
**Governing Documents:** IS-300; IS-201; IS-202; IS-102; Catalogs 01/03/08  
**Dependencies:** PEOPLE-IS-300 APPROVED (D-072)  
**Implementation Authorization:** `IMPLEMENTATION NOT AUTHORIZED`

```text
DESIGN COMPLETE
APPROVED FOR DOCUMENTATION GOVERNANCE
CANONICAL LOGICAL TABLE INVENTORY
LOGICAL ≠ PHYSICAL
NO SQL / DDL / PRISMA / MIGRATIONS / INDEXES / TRIGGERS
APPLICATION IMPLEMENTATION NOT AUTHORIZED
```

**Distinction (locked):**

```text
Domain        owns meaning
Database      owns persistence architecture (IS-300)
Logical table owns catalogued persistence objects (this IS)
Implementation owns execution (NOT YET AUTHORIZED)
```

These responsibilities must not overlap. This catalog describes **logical** tables—not deployed relations.

---

## 1. Purpose

Provide the canonical inventory of every logical persistence object so that future physical schema and migrations translate an approved catalog—never invent tables during implementation.

## 2. Scope

Logical table admission questionnaire; complete cards for intake-owned and explicitly external logical objects; persistence patterns; module ownership; package/migration placeholders; read-model consumers; audit/sensitivity/retention; logical relationships; extension doctrine.

## 3. Out of Scope

```text
FORBIDDEN:
  SQL, DDL, CREATE TABLE, Prisma schema, migrations,
  index/trigger definitions as executable artifacts,
  seed data, live database objects
```

Physical column typing, exact index DDL, and migration scripts → IS-303+ / authorized packages after Gate G-10.

## 4. Standing doctrine

### 4.1 Logical table extension tree

```text
Need new persistence?
  → Existing Aggregate? (IS-200/201)
      → Existing Entity?
          → Existing Field? (IS-202)
              → Existing Logical Table? (this IS)
                  YES → Reuse
                  NO  → Update IS-301 or create ADR
                        → Only then may future packages define physical schema
```

### 4.2 Catalog 01 / Match ≠ Promotion

* State columns on logical tables cite Catalog 01 only.  
* Match resolution logical tables do not own canonical person persistence.  
* Promotion logical tables own intake-side acceptance records only.

## 5. Mandatory logical-table questionnaire

| # | Question |
| --- | --- |
| L1 | Why does this logical table exist? |
| L2 | Which aggregate owns it? |
| L3 | Which entity or entities map to it? |
| L4 | Which value objects appear within it? |
| L5 | What is its primary business purpose? |
| L6 | What persistence pattern? (`TRANSACTIONAL` \| `LOOKUP` \| `APPEND_ONLY` \| `READ_MODEL` \| `EXTERNAL`) |
| L7 | Which module owns it? |
| L8 | Which future implementation package creates it? |
| L9 | Which future migrations will reference it? |
| L10 | Which read models consume it? |
| L11 | Which audit requirements apply? |
| L12 | Which sensitivity classification governs it? (Catalog 08) |
| L13 | Which retention rules apply? (Catalog 08 domain / ISSUE-RETENTION-001) |
| L14 | Which logical relationships exist with other tables? |

## 6. Functional Requirements

| ID | Description |
| --- | --- |
| REQ-LTC-001 | Every logical table admitted for intake persistence MUST have a complete questionnaire card. |
| REQ-LTC-002 | Logical tables MUST trace to IS-201 entities and IS-202 fields/VOs (or EXTERNAL). |
| REQ-LTC-003 | No SQL/Prisma/migration syntax MAY appear in this catalog. |
| REQ-LTC-004 | READ_MODEL tables MUST NOT accept claim or resolution writes. |
| REQ-LTC-005 | APPEND_ONLY tables MUST NOT support business updates/deletes. |
| REQ-LTC-006 | New logical tables require IS-301 amendment or ADR before physical schema. |
| REQ-LTC-007 | Canonical person master tables remain EXTERNAL — not intake-owned catalog entries for write authority. |

## 7. Persistence pattern glossary

| Pattern | Meaning |
| --- | --- |
| TRANSACTIONAL | Mutable write-model aggregate store |
| LOOKUP | Reference/config-like rows (rare in V1 intake) |
| APPEND_ONLY | Insert-only history/audit |
| READ_MODEL | Derived query surface; no dual write authority |
| EXTERNAL | Outside intake ownership; port/integration only |

---

## 8. Logical table cards

### LT-BATCH — `intake_batches`

| Q | Answer |
| --- | --- |
| L1 | Persist batch collection context and lifecycle |
| L2 | Batch aggregate |
| L3 | ENT-BATCH |
| L4 | VO-UUID, VO-BATCH-CODE, VO-SOURCE-TYPE, VO-PRIORITY, VO-CAT01-STATE, VO-TIMESTAMP, VO-RAW-TEXT |
| L5 | Group pages; shared source metadata; not people |
| L6 | TRANSACTIONAL |
| L7 | MOD-BATCHES |
| L8 | Future PKG-batch-persistence / Phase 3–4 packages |
| L9 | Initial intake core migration set (when authorized) |
| L10 | Batch admin lists; ops dashboards |
| L11 | Batch lifecycle transitions (Cat 03 BATCH domain) |
| L12 | CLASS-002 overall; some notes CLASS-003 |
| L13 | Intake operational retention (Cat 08; durations ISSUE-RETENTION-001) |
| L14 | 1—* LT-PAGE |

### LT-PAGE — `intake_pages`

| Q | Answer |
| --- | --- |
| L1 | Persist queue work items (sheets) |
| L2 | Page aggregate |
| L3 | ENT-PAGE |
| L4 | VO-UUID, VO-CAT01-STATE, VO-OPT-LOCK, VO-TIMESTAMP |
| L5 | Primary work unit; parent of entries; image ref |
| L6 | TRANSACTIONAL |
| L7 | MOD-PAGES |
| L8 | Future PKG-page-persistence |
| L9 | Intake core migration set |
| L10 | Queue READ_MODEL; transcription UI |
| L11 | Page lifecycle (Cat 03 PAGE) |
| L12 | CLASS-002 |
| L13 | Intake operational retention |
| L14 | *—1 LT-BATCH; 1—* LT-ENTRY; 0..1 active LT-IMAGE; 0..1 active LT-CLAIM |

### LT-ENTRY — `intake_entries`

| Q | Answer |
| --- | --- |
| L1 | Persist person-line transcription + linkage |
| L2 | Entry aggregate |
| L3 | ENT-ENTRY, ENT-DRAFT (facet) |
| L4 | VO-ROW-NUMBER, VO-RAW-TEXT, VO-NORM-*, VO-FIELD-CONDITION, VO-TRI-STATE, VO-CAT01-STATE, VO-UUID |
| L5 | Unique handwritten person line; never Canonical Person |
| L6 | TRANSACTIONAL |
| L7 | MOD-DRAFTS / MOD-TRANSCRIPTIONS (**ISSUE-MOD-001**) |
| L8 | Future PKG-entry-persistence |
| L9 | Intake core + entry writer-split amendments |
| L10 | Matching UI; reports (read) |
| L11 | Draft/transcription/match/promotion correlation |
| L12 | CLASS-003–004 (PII fields) |
| L13 | Higher sensitivity retention class PENDING exact rule |
| L14 | *—1 LT-PAGE; 1—* LT-MATCH-CANDIDATE; 0..1 LT-MATCH-RESOLUTION; 0..* LT-PROMOTION |

### LT-ENTRY-CORRECTION — `intake_entry_corrections`

| Q | Answer |
| --- | --- |
| L1 | Formal post-submit correction history |
| L2 | Entry aggregate (history) |
| L3 | ENT-ENTRY (correction facet) |
| L4 | VO-RAW-TEXT, VO-FIELD-CONDITION, VO-TIMESTAMP, VO-UUID |
| L5 | Preserve prior values when CORRECTED |
| L6 | APPEND_ONLY (preferred) / TRANSACTIONAL history rows |
| L7 | MOD-TRANSCRIPTIONS |
| L8 | Future PKG-entry-corrections |
| L9 | With entry persistence or follow-on migration |
| L10 | Audit/review UIs |
| L11 | Correction events required |
| L12 | CLASS-003–004 |
| L13 | Align with entry retention |
| L14 | *—1 LT-ENTRY |

### LT-CLAIM — `intake_page_claims`

| Q | Answer |
| --- | --- |
| L1 | Exclusive work holds |
| L2 | Claim aggregate |
| L3 | ENT-CLAIM |
| L4 | VO-UUID, VO-CAT01-STATE, VO-TIMESTAMP |
| L5 | One active claim per page/work type |
| L6 | TRANSACTIONAL |
| L7 | MOD-CLAIMS |
| L8 | Future PKG-claim-persistence |
| L9 | Intake core migration set |
| L10 | Queue READ_MODEL (overlay) |
| L11 | CLAIM audit seeds |
| L12 | CLASS-002 |
| L13 | Operational short-lived + history retention PENDING |
| L14 | *—1 LT-PAGE; *—1 LT-USER |

### LT-QUEUE — `intake_queue_items` (or view)

| Q | Answer |
| --- | --- |
| L1 | Shared worklist projection |
| L2 | Queue projection (not claim aggregate) |
| L3 | ENT-QUEUE-ITEM |
| L4 | VO-UUID, VO-CAT01-STATE (STATE-QUEUE-001), references |
| L5 | Ordering/visibility only |
| L6 | READ_MODEL |
| L7 | MOD-QUEUES |
| L8 | Future PKG-queue-read-model |
| L9 | May be view-only (no base table) — decide in IS-302/303 |
| L10 | Queue UI |
| L11 | Usually derived; material changes via page/claim audits |
| L12 | CLASS-002 |
| L13 | Ephemeral/derived |
| L14 | Projects LT-PAGE + LT-CLAIM; **no claim writes** |

### LT-IMAGE — `intake_source_images`

| Q | Answer |
| --- | --- |
| L1 | Private image refs + integrity metadata |
| L2 | Source Image / Upload aggregate |
| L3 | ENT-IMAGE |
| L4 | VO-CONTENT-HASH, VO-CAT01-STATE (storage), VO-UUID, VO-RAW-TEXT |
| L5 | Evidence layer; binaries external |
| L6 | TRANSACTIONAL |
| L7 | MOD-UPLOADS |
| L8 | Future PKG-image-persistence |
| L9 | Storage migration set (after ADR-005) |
| L10 | Image viewer; page UI |
| L11 | UPLOAD/IMAGE audit domains |
| L12 | CLASS-004 (keys); metadata CLASS-002–003 |
| L13 | Evidence retention (Cat 08; ISSUE-RETENTION-001) |
| L14 | 0..1 active per LT-PAGE; 1—* LT-IMAGE-VERSION; links LT-UPLOAD |

### LT-UPLOAD — `intake_upload_attempts`

| Q | Answer |
| --- | --- |
| L1 | Upload session lifecycle |
| L2 | Upload aggregate |
| L3 | ENT-UPLOAD |
| L4 | VO-UUID, VO-CAT01-STATE (STATE-UPLOAD-001), VO-TIMESTAMP |
| L5 | Track attempts independent of durable image |
| L6 | TRANSACTIONAL |
| L7 | MOD-UPLOADS |
| L8 | Future PKG-upload-persistence |
| L9 | With image migration set |
| L10 | Capture ops |
| L11 | UPLOAD domain |
| L12 | CLASS-002 |
| L13 | Operational |
| L14 | May produce LT-IMAGE |

### LT-IMAGE-VERSION — `intake_image_versions`

| Q | Answer |
| --- | --- |
| L1 | Original/display/thumb version refs |
| L2 | Source Image aggregate |
| L3 | ENT-IMAGE (versions) |
| L4 | VO-UUID, keys, VO-CONTENT-HASH |
| L5 | Supersede without losing provenance |
| L6 | TRANSACTIONAL |
| L7 | MOD-UPLOADS |
| L8 | Future PKG-image-versions |
| L9 | Storage migration set |
| L10 | Viewer derivatives |
| L11 | IMAGE domain |
| L12 | CLASS-004 |
| L13 | With image retention |
| L14 | *—1 LT-IMAGE |

### LT-MATCH-RUN — `intake_match_runs`

| Q | Answer |
| --- | --- |
| L1 | Immutable evaluation runs |
| L2 | Match Evaluation aggregate |
| L3 | ENT-MATCH-EVAL |
| L4 | VO-UUID, VO-CAT01-STATE (STATE-MATCH-EVAL-001), VO-TIMESTAMP |
| L5 | Bound candidate set; immutable after complete |
| L6 | TRANSACTIONAL (insert + terminal update) / effectively append after complete |
| L7 | MOD-MATCHING |
| L8 | Future PKG-match-persistence |
| L9 | Matching migration set |
| L10 | Matching UI |
| L11 | MATCHING domain |
| L12 | CLASS-003 |
| L13 | Match decision retention |
| L14 | *—1 LT-ENTRY; 1—* LT-MATCH-CANDIDATE |

### LT-MATCH-CANDIDATE — `intake_match_candidates`

| Q | Answer |
| --- | --- |
| L1 | Scored possible person links |
| L2 | Match Evaluation |
| L3 | ENT-MATCH-CANDIDATE |
| L4 | VO-MATCH-CONFIDENCE, VO-CANDIDATE-STATUS, VO-CONTACT-SHARE, VO-UUID |
| L5 | Explainable candidates; not resolution; not promotion |
| L6 | TRANSACTIONAL within run; immutable after run complete |
| L7 | MOD-MATCHING |
| L8 | Future PKG-match-persistence |
| L9 | Matching migration set |
| L10 | Matching UI |
| L11 | MATCHING domain |
| L12 | CLASS-003 |
| L13 | With match retention |
| L14 | *—1 LT-MATCH-RUN; references EXTERNAL person id |

### LT-MATCH-RESOLUTION — `intake_match_resolutions`

| Q | Answer |
| --- | --- |
| L1 | Final match outcomes |
| L2 | Match Resolution aggregate |
| L3 | ENT-MATCH-RESOLUTION |
| L4 | VO-RESOLUTION-OUTCOME, VO-RESOLUTION-METHOD, VO-CAT01-STATE, VO-UUID |
| L5 | Identity-confidence decision; **must not** write canonical masters |
| L6 | TRANSACTIONAL (versioned) |
| L7 | MOD-RESOLUTION |
| L8 | Future PKG-resolution-persistence |
| L9 | Matching/resolution migration set |
| L10 | Matching UI; promotion eligibility reads |
| L11 | RESOLUTION domain |
| L12 | CLASS-003 |
| L13 | Decision retention |
| L14 | *—1 LT-ENTRY; 0..* LT-PROMOTION |

### LT-PROMOTION — `intake_promotion_requests`

| Q | Answer |
| --- | --- |
| L1 | Controlled canonical acceptance requests |
| L2 | Promotion Request aggregate |
| L3 | ENT-PROMOTION |
| L4 | VO-UUID, VO-CAT01-STATE (STATE-PROMOTION-001), idempotency key |
| L5 | Business acceptance path; durable before async call |
| L6 | TRANSACTIONAL |
| L7 | MOD-PROMOTION |
| L8 | Future PKG-promotion-persistence |
| L9 | Promotion migration set (after ISSUE-CANONICAL-001) |
| L10 | Promotion ops UI |
| L11 | PROMOTION / CANONICAL_INTEGRATION domains |
| L12 | CLASS-003 |
| L13 | Integration retention |
| L14 | *—1 LT-MATCH-RESOLUTION; *—1 LT-ENTRY; may yield LT-PROMOTION-RESULT |

### LT-PROMOTION-RESULT — `intake_promotion_results`

| Q | Answer |
| --- | --- |
| L1 | Durable outcomes of promotion attempts |
| L2 | Promotion aggregate |
| L3 | ENT-PROMOTION (result facet) |
| L4 | VO-UUID, result person id, VO-TIMESTAMP |
| L5 | Record success/fail/review without owning person master |
| L6 | APPEND_ONLY preferred |
| L7 | MOD-PROMOTION |
| L8 | Future PKG-promotion-persistence |
| L9 | With promotion migrations |
| L10 | Ops/audit |
| L11 | PROMOTION domain |
| L12 | CLASS-003 |
| L13 | With promotion retention |
| L14 | *—1 LT-PROMOTION |

### LT-AUDIT — `intake_audit_events`

| Q | Answer |
| --- | --- |
| L1 | Append-only meaningful actions |
| L2 | Audit store |
| L3 | ENT-AUDIT |
| L4 | Catalog 03 event name; VO-TIMESTAMP; VO-UUID; JSON payload (no secrets) |
| L5 | Forensic/ops evidence |
| L6 | APPEND_ONLY |
| L7 | MOD-AUDIT |
| L8 | Future PKG-audit-persistence |
| L9 | Cross-cutting early migration |
| L10 | Audit timeline UI |
| L11 | Self |
| L12 | CLASS-002–003 by payload |
| L13 | Audit retention (Cat 08) |
| L14 | References many LT-* via correlation IDs (logical) |

### LT-ERROR — `intake_processing_errors`

| Q | Answer |
| --- | --- |
| L1 | Operator-visible processing failures |
| L2 | Ops/error boundary |
| L3 | ENT-ERROR |
| L4 | VO-UUID, VO-CAT01-STATE (STATE-ERROR-001), Catalog 2 codes |
| L5 | Track remediation |
| L6 | TRANSACTIONAL |
| L7 | MOD-OPERATIONS |
| L8 | Future PKG-ops-persistence |
| L9 | Ops migration set |
| L10 | Ops console |
| L11 | Ops/error audits |
| L12 | CLASS-002–003 |
| L13 | Ops retention |
| L14 | May reference LT-PAGE/ENTRY/JOB |

### LT-USER — `app_users`

| Q | Answer |
| --- | --- |
| L1 | Application actors |
| L2 | User aggregate |
| L3 | ENT-USER |
| L4 | VO-UUID, VO-CAT01-STATE (STATE-USER-001), email VO PENDING ADR-004 |
| L5 | AuthN identity binding target |
| L6 | TRANSACTIONAL |
| L7 | MOD-USERS |
| L8 | Future PKG-user-persistence |
| L9 | Auth migration set (after ADR-004) |
| L10 | Admin UI |
| L11 | USER_MANAGEMENT / AUTHENTICATION |
| L12 | CLASS-004 (email) |
| L13 | Account retention PENDING |
| L14 | 1—* LT-CLAIM; role grants future LT-ROLE-GRANT |

### LT-ROLE-GRANT — `app_role_grants` (seed name)

| Q | Answer |
| --- | --- |
| L1 | Role assignments |
| L2 | User / Role Grant |
| L3 | ENT-ROLE-GRANT |
| L4 | VO-UUID, VO-CAT01-STATE (STATE-ROLE-001) |
| L5 | Authorization grants |
| L6 | TRANSACTIONAL |
| L7 | MOD-ROLES |
| L8 | Future PKG-role-persistence |
| L9 | Authz migration set |
| L10 | Admin |
| L11 | ROLE_MANAGEMENT |
| L12 | CLASS-002 |
| L13 | With user retention |
| L14 | *—1 LT-USER |

### LT-CANONICAL-PERSON — EXTERNAL

| Q | Answer |
| --- | --- |
| L1 | Shared durable person identity (ecosystem) |
| L2 | EXTERNAL |
| L3 | ENT-CANONICAL-PERSON |
| L4 | External VOs |
| L5 | Canonical master — not intake-owned |
| L6 | EXTERNAL |
| L7 | Canonical domain (+ MOD-LAYER-INT port) |
| L8 | Not created by intake packages |
| L9 | Not intake migrations |
| L10 | Matching reads via port |
| L11 | CANONICAL_INTEGRATION on intake side only |
| L12 | Per canonical policy |
| L13 | Canonical retention |
| L14 | Referenced by candidates/promotion results — **no intake write ownership** |

### LT-PERSON-ATTRIBUTE — EXTERNAL

| Q | Answer |
| --- | --- |
| L1 | Canonical attributes with provenance |
| L2 | EXTERNAL |
| L3 | ENT-PERSON-ATTRIBUTE |
| L4 | External |
| L5 | History-preserving attributes |
| L6 | EXTERNAL |
| L7 | Canonical domain |
| L8–L9 | Not intake |
| L10 | Via promotion outcomes |
| L11–L13 | Canonical |
| L14 | Owned outside intake |

---

## 9. Catalog index

```text
LT-BATCH, LT-PAGE, LT-ENTRY, LT-ENTRY-CORRECTION,
LT-CLAIM, LT-QUEUE, LT-IMAGE, LT-UPLOAD, LT-IMAGE-VERSION,
LT-MATCH-RUN, LT-MATCH-CANDIDATE, LT-MATCH-RESOLUTION,
LT-PROMOTION, LT-PROMOTION-RESULT,
LT-AUDIT, LT-ERROR, LT-USER, LT-ROLE-GRANT,
LT-CANONICAL-PERSON (EXTERNAL), LT-PERSON-ATTRIBUTE (EXTERNAL)
```

## 10. Acceptance Criteria

| ID | Criterion | Met? |
| --- | --- | --- |
| AC-LTC-001 | Questionnaire defined and applied | Yes |
| AC-LTC-002 | Intake write-model tables carded | Yes |
| AC-LTC-003 | EXTERNAL canonical tables marked | Yes |
| AC-LTC-004 | READ_MODEL claim-write prohibition stated | Yes |
| AC-LTC-005 | No SQL/Prisma/migrations created | Yes |
| AC-LTC-006 | Extension doctrine locked | Yes |

## 11. Open Decisions

| ID | Notes |
| --- | --- |
| ISSUE-MOD-001 | Entry writer split may affect LT-ENTRY physical shape |
| ISSUE-MOD-002 | Additional report READ_MODEL tables |
| ISSUE-CANONICAL-001 | Promotion DTO; whether physical FK possible |
| ISSUE-DBA-001 | Shared DB audit before assuming existence |
| LT-QUEUE as view vs table | IS-302/303 |
| Exact Cat 08 retention durations | ISSUE-RETENTION-001 |

## 12. Risks

| ID | Risk | Mitigation |
| --- | --- | --- |
| RISK-LTC-001 | Treating logical names as deployed tables | NFR honesty; ISSUE-DBA-001 |
| RISK-LTC-002 | SQL sneaking into IS-301 | REQ-LTC-003 |
| RISK-LTC-003 | Queue table accepts claims | REQ-LTC-004 |

## 13. Dependencies

IS-300; IS-201; IS-202; Catalogs 01/03/08.

## 14. Traceability

LT-* ↔ ENT-* ↔ FLD-* ↔ MOD-* — FULLY_MAPPED (logical). Physical → IS-303+.

## 15. Implementation Boundary

**Authorized:** this catalog; governance updates; audit verification.  
**Forbidden:** any executable schema artifact.

## 16. Revision History

| Version | Date | Change | Approval |
| --- | --- | --- | --- |
| 1.0 | 2026-07-26 | Logical table encyclopedia | D-073 |

## Next primary

```text
PEOPLE-IS-302-LOGICAL-RELATIONSHIP-SPECIFICATIONS-1.0
```

## Independent lane

```text
PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0
```

## Final status

```text
PEOPLE-IS-301 LOGICAL TABLE CATALOG: APPROVED (DOCUMENTATION)
LOGICAL ≠ PHYSICAL
SQL / PRISMA / MIGRATIONS: NOT CREATED — NOT AUTHORIZED
```
