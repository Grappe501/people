# PEOPLE-IS-201 — ENTITY SPECIFICATIONS

**Title:** Entity Specifications  
**Document ID:** `PEOPLE-IS-201-ENTITY-SPECIFICATIONS-1.0`  
**Version:** 1.0  
**Status:** APPROVED  
**Phase:** PHASE 2 — DOMAIN AND DATA MODEL  
**Project Root:** `H:\people`  
**Owner:** People Intake System Program  
**Approval Authority:** Decision Log D-070  
**Created Date:** 2026-07-26  
**Last Updated:** 2026-07-26  
**Governing Documents:** IS-200; IS-102; Catalogs 01–08 (esp. 01, 03, 05); Constitution Art. XIV; Glossary  
**Dependencies:** PEOPLE-IS-200 APPROVED (D-069)  
**Implementation Authorization:** `IMPLEMENTATION NOT AUTHORIZED`

```text
DESIGN COMPLETE
APPROVED FOR DOCUMENTATION GOVERNANCE
CANONICAL ENTITY ENCYCLOPEDIA
CATALOG 01 = SOLE STATE AUTHORITY
MATCH RESOLUTION ≠ PROMOTION (LOCKED)
APPLICATION IMPLEMENTATION NOT AUTHORIZED
PHYSICAL SCHEMA NOT FINAL (IS-300+)
```

---

## 1. Purpose

Provide the canonical encyclopedia of every People Intake business entity so that Burt (and every future package) can answer, **without exception**, the mandatory entity questionnaire before creating or extending any entity.

## 2. Scope

Entity admission rules; standing extension doctrine; mandatory questionnaire; complete cards for intake-owned and explicitly external entities; cross-cutting honesty rules for permissions, APIs, events, packages, and tests.

## 3. Out of Scope

* Physical DDL / migrations (IS-300+)  
* Inventing Catalog 01 states, Catalog 03 event names, or Catalog 05 permission keys beyond seeded foundations  
* Resolving ISSUE-MOD-001 / ISSUE-CANONICAL-001 by silent invention  
* Application code  

## 4. Governing References

IS-200 Domain Model; IS-102 ownership matrix; Catalog 01 state machines; Catalog 03 audit domains/seeds; Catalog 05 permission seeds; field dictionary (conceptual only — not Catalog 01).

## 5. Standing doctrine (locked)

### 5.1 Catalog 01 is the authoritative state model

No implementation package MAY redefine lifecycle, ownership, or business states outside Catalog 01. Conceptual labels in older workflow/field docs are **not** production enums until reconciled.

### 5.2 Match Resolution ≠ Promotion

| Concern | Owns | Must not |
| --- | --- | --- |
| **Matching / Resolution** | Identity confidence and resolution outcome | Mutate canonical persons |
| **Promotion** | Business acceptance into canonical domain | Redefine match outcomes |

Neither process owns the other.

### 5.3 Extension decision tree (mandatory)

```text
Does the feature belong to an existing domain concept (IS-200 / this encyclopedia)?

YES → Extend the existing specification / entity card.
NO  → Does the domain model need to evolve?
        YES → Update governing IS / Decision Log / ADR.
        NO  → Reject the implementation proposal.
```

Duplicate concepts, overlapping entities, and silent drift are forbidden.

### 5.4 Entity admission gate

No entity may enter the project unless **all** mandatory questionnaire fields are answered (use `PENDING` / `EXTERNAL` / `NOT_APPLICABLE` with rationale — never blank).

## 6. Mandatory entity questionnaire

Every entity card MUST answer:

| # | Question |
| --- | --- |
| Q1 | Why does this entity exist? |
| Q2 | Who owns it? (capability module) |
| Q3 | What aggregate owns it? |
| Q4 | What is its identity? |
| Q5 | What invariants are always true? |
| Q6 | What lifecycle does it follow? (Catalog 01 machine ID) |
| Q7 | Which module owns it? (same as Q2; explicit) |
| Q8 | Which services may modify it? |
| Q9 | Which events affect it? (Catalog 03 domain / seeded IDs) |
| Q10 | Which permissions protect it? (Catalog 05 seeds / family) |
| Q11 | Which APIs expose it? (seeded API family) |
| Q12 | Which implementation packages create or extend it? |
| Q13 | Which tests must always exist? |

## 7. Functional Requirements

| ID | Description |
| --- | --- |
| REQ-ENT-001 | Every admitted entity MUST have a complete questionnaire card. |
| REQ-ENT-002 | Lifecycle answers MUST cite Catalog 01 machine IDs only. |
| REQ-ENT-003 | Match Resolution entities/services MUST NOT write canonical person master data. |
| REQ-ENT-004 | Promotion entities/services MUST NOT redefine match resolution outcomes. |
| REQ-ENT-005 | New entities require IS-200/IS-201 amendment or ADR — not silent package invention. |
| REQ-ENT-006 | Field-dictionary conceptual statuses MUST NOT be treated as Catalog 01 enums. |
| REQ-ENT-007 | External entities (Canonical Person, etc.) MUST be marked EXTERNAL with port-only access. |
| REQ-ENT-008 | ISSUE-MOD-001 MUST remain visible on Entry/Draft cards until Decision Log closure. |

## 8. Nonfunctional Requirements

| ID | Description |
| --- | --- |
| NFR-ENT-HONEST-001 | Seeded catalog IDs only; expansions via amendment. |
| NFR-ENT-TRACE-001 | Each card maps to IS-200 aggregate + IS-102 module. |
| NFR-ENT-TEST-001 | Mandatory tests are named as obligations for future packages. |

## 9. Architecture — Entity encyclopedia

### 9.0 Card conventions

* **Table seed:** conceptual / Volume 9 bootstrap name — not physical finality.  
* **Permissions / Events:** cite seeded IDs or Catalog domains; `PENDING amendment` if inventory incomplete.  
* **Packages:** phase-oriented placeholders until PKG library authorized.  
* **Services:** owning module application/domain services only.

---

### ENT-BATCH — Intake Batch

| Q | Answer |
| --- | --- |
| Q1 Why | Groups pages from one collection context; shared source metadata; not people |
| Q2 / Q7 Owner | `MOD-BATCHES` |
| Q3 Aggregate | **Batch** (root) |
| Q4 Identity | `batch_id` (stable); optional human `batch_code` (non-PII) |
| Q5 Invariants | Contains pages not canonical people; counters never invent entries; UNKNOWN source allowed |
| Q6 Lifecycle | `STATE-BATCH-001` |
| Q8 Modifiers | Batch application service only; pages attach via page module coordination |
| Q9 Events | Catalog 03 domain `BATCH`; seeds as amended |
| Q10 Permissions | `PERM-BATCH-001`, `PERM-BATCH-002` (+ Catalog 5 expansion) |
| Q11 APIs | `API-BATCH-*` |
| Q12 Packages | Future batch capture/admin packages (Phase 4/5/6) |
| Q13 Tests | Create/open/complete/archive transitions; forbid person rows on batch; illegal Catalog 01 transition rejected |
| Table seed | `intake_batches` |

---

### ENT-PAGE — Intake Page

| Q | Answer |
| --- | --- |
| Q1 Why | Primary queue work item; one sheet; claim unit; parent of 0–10 entries |
| Q2 / Q7 Owner | `MOD-PAGES` |
| Q3 Aggregate | **Page** (root) |
| Q4 Identity | `page_id`; `page_number` is batch-relative order, not global ID |
| Q5 Invariants | 0–10 entries max; blank rows ≠ entries; ≤1 active claim per work type; completion follows entry terminal paths |
| Q6 Lifecycle | `STATE-PAGE-001` (image quality via `STATE-IMAGE-QUALITY-001` as related) |
| Q8 Modifiers | Page service; claim overlay via `MOD-CLAIMS`; uploads attach image refs via `MOD-UPLOADS` |
| Q9 Events | Catalog 03 domain `PAGE` (seed `AUDIT-PAGE-001` family) |
| Q10 Permissions | `PERM-PAGE-001`…`PERM-PAGE-004` |
| Q11 APIs | `API-PAGE-*` |
| Q12 Packages | Capture, queue UI, transcription packages |
| Q13 Tests | Entry cardinality; claim exclusivity coordination; Catalog 01 transitions; no fabricated entries |
| Table seed | `intake_pages` |

---

### ENT-ENTRY — Intake Entry

| Q | Answer |
| --- | --- |
| Q1 Why | One handwritten person line with unique identity, transcription, match, and promotion linkage |
| Q2 / Q7 Owner | `MOD-DRAFTS` (draft states) / `MOD-TRANSCRIPTIONS` (submit/finalize) — **ISSUE-MOD-001** |
| Q3 Aggregate | **Entry (Draft→Submitted)** |
| Q4 Identity | `entry_id` durable; `row_number` 1–10 positional only |
| Q5 Invariants | Not a Canonical Person; raw+normalized+condition layers preserved; UNKNOWN≠NO; blank row ⇒ no entity |
| Q6 Lifecycle | `STATE-ENTRY-001` (+ draft machine while drafting) |
| Q8 Modifiers | Draft service XOR transcription service per state (single-writer rules); normalization may update normalized fields only; matching/resolution/promotion write **related** entities, not redefine entry identity |
| Q9 Events | Domains `DRAFT`, `TRANSCRIPTION`, `MATCHING`, `RESOLUTION`, `PROMOTION` as applicable |
| Q10 Permissions | Page/match/promotion families as workflow requires; no silent bypass |
| Q11 APIs | Draft APIs + transcription APIs (seed) |
| Q12 Packages | Transcription, matching, promotion packages |
| Q13 Tests | Identity≠row; layer separation; UNKNOWN≠NO; writer-split rules; illegal transitions |
| Table seed | `intake_entries` |
| Open | **ISSUE-MOD-001** blocks unrestricted dual writers |

---

### ENT-DRAFT — Draft (transcription persistence)

| Q | Answer |
| --- | --- |
| Q1 Why | Persist in-progress transcription before immutable submit revision |
| Q2 / Q7 Owner | `MOD-DRAFTS` |
| Q3 Aggregate | Entry aggregate (draft facet) |
| Q4 Identity | Draft ID and/or entry-scoped draft revision ID |
| Q5 Invariants | Survives claim expiry when recoverable; submit creates immutable revision; does not invent entries for blank rows |
| Q6 Lifecycle | `STATE-DRAFT-001` |
| Q8 Modifiers | Draft service only |
| Q9 Events | Domain `DRAFT` |
| Q10 Permissions | Page transcription permissions (Catalog 5 page family) |
| Q11 APIs | Draft APIs |
| Q12 Packages | Transcription packages |
| Q13 Tests | Recover after claim expiry; supersede rules; submit immutability |
| Table seed | Often same `intake_entries` draft columns/revisions — finalize IS-300 / ISSUE-MOD-001 |

---

### ENT-IMAGE — Source Image

| Q | Answer |
| --- | --- |
| Q1 Why | Private original (and derivatives) for a page; evidence layer |
| Q2 / Q7 Owner | `MOD-UPLOADS` |
| Q3 Aggregate | **Source Image / Upload** |
| Q4 Identity | `image_id`; content hash as integrity evidence |
| Q5 Invariants | Private storage only; not public CDN identity; page holds active image ref; supersede via versioning |
| Q6 Lifecycle | `STATE-STORAGE-001` + `STATE-IMAGE-QUALITY-001` |
| Q8 Modifiers | Upload/storage adapters via owning module; pages reference, do not store binaries |
| Q9 Events | Domains `UPLOAD`, `IMAGE` |
| Q10 Permissions | Page/upload families (Catalog 5); export separate |
| Q11 APIs | API upload family |
| Q12 Packages | Upload/capture packages |
| Q13 Tests | Private ACL; hash integrity; quarantine path; no public URL assumption |
| Table seed | `intake_source_images` |
| Open | ISSUE-STORAGE-001 / ADR-005 provider |

---

### ENT-UPLOAD — Upload Session

| Q | Answer |
| --- | --- |
| Q1 Why | Track upload attempt lifecycle independent of durable image row |
| Q2 / Q7 Owner | `MOD-UPLOADS` |
| Q3 Aggregate | Source Image / Upload |
| Q4 Identity | `upload_id` |
| Q5 Invariants | Terminal fail/expire/cancel does not leave silent “success” image; idempotent retries policy-bound |
| Q6 Lifecycle | `STATE-UPLOAD-001` |
| Q8 Modifiers | Upload service only |
| Q9 Events | Domain `UPLOAD` |
| Q10 Permissions | Upload/page families |
| Q11 APIs | API upload family |
| Q12 Packages | Capture packages |
| Q13 Tests | Idempotent retry; expire; fail closed |
| Table seed | upload session table (future IS-300) |

---

### ENT-CLAIM — Page Claim

| Q | Answer |
| --- | --- |
| Q1 Why | Exclusive editing rights for transcription/authorized work |
| Q2 / Q7 Owner | `MOD-CLAIMS` |
| Q3 Aggregate | **Claim** (root) |
| Q4 Identity | `claim_id` |
| Q5 Invariants | One active claim per page/work type; expiry returns availability; **does not erase** recoverable drafts |
| Q6 Lifecycle | `STATE-CLAIM-001` |
| Q8 Modifiers | Claim service only; queue must not write claims |
| Q9 Events | Domain `CLAIM` (seed `AUDIT-CLAIM-001`) |
| Q10 Permissions | `PERM-PAGE-*` claim/work permissions as Catalog 5 defines |
| Q11 APIs | `API-CLAIM-*` / queue-and-claims family |
| Q12 Packages | Queue/transcription packages |
| Q13 Tests | Mutual exclusion; renew; expire without draft loss; double-claim rejected |
| Table seed | `intake_page_claims` |

---

### ENT-QUEUE-ITEM — Queue Item (projection)

| Q | Answer |
| --- | --- |
| Q1 Why | Shared worklist visibility/order across stages |
| Q2 / Q7 Owner | `MOD-QUEUES` |
| Q3 Aggregate | Projection over Page (+ claim overlay) — not a second claim store |
| Q4 Identity | Queue item ID or page-keyed projection identity (IS-300 decides persistence) |
| Q5 Invariants | **No claim writes**; reflects Catalog 01 page/claim/queue machines honestly |
| Q6 Lifecycle | `STATE-QUEUE-001` |
| Q8 Modifiers | Queue projection builders; never claim service |
| Q9 Events | Domain `QUEUE` (typically derived) |
| Q10 Permissions | Page queue read/work permissions |
| Q11 APIs | `API-QUEUE-*` |
| Q12 Packages | Queue UI/API packages |
| Q13 Tests | No claim mutation via queue APIs; ordering stability |
| Table seed | queue views/tables (future) |

---

### ENT-MATCH-EVAL — Match Evaluation Run

| Q | Answer |
| --- | --- |
| Q1 Why | Produce explainable candidate set for an entry |
| Q2 / Q7 Owner | `MOD-MATCHING` |
| Q3 Aggregate | **Match Evaluation** (root) |
| Q4 Identity | Evaluation run ID |
| Q5 Invariants | Immutable after completion; supersede via new run; household/shared contact alone ≠ identity; does not write canonical persons |
| Q6 Lifecycle | `STATE-MATCH-EVAL-001` |
| Q8 Modifiers | Matching domain/application service only |
| Q9 Events | Domain `MATCHING` (seed `AUDIT-MATCH-001` family) |
| Q10 Permissions | `PERM-MATCH-001`, `PERM-MATCH-002` |
| Q11 APIs | `API-MATCH-*` |
| Q12 Packages | Matching packages |
| Q13 Tests | Immutability after complete; explainability fields present; no canonical writes |
| Table seed | evaluation run store (future) + candidates |

---

### ENT-MATCH-CANDIDATE — Match Candidate

| Q | Answer |
| --- | --- |
| Q1 Why | Scored possible relationship entry ↔ existing canonical person |
| Q2 / Q7 Owner | `MOD-MATCHING` |
| Q3 Aggregate | Match Evaluation |
| Q4 Identity | `candidate_id` |
| Q5 Invariants | Belongs to one evaluation; scores/reasons required; not a resolution; not a promotion |
| Q6 Lifecycle | Contained under evaluation; resolution outcome separate (`STATE-MATCH-RESOLUTION-001`) |
| Q8 Modifiers | Matching service during evaluation only |
| Q9 Events | Domain `MATCHING` |
| Q10 Permissions | `PERM-MATCH-*` |
| Q11 APIs | `API-MATCH-*` |
| Q12 Packages | Matching packages |
| Q13 Tests | Candidate not auto-promoted; conflict flags preserved |
| Table seed | `intake_match_candidates` |

---

### ENT-MATCH-RESOLUTION — Match Resolution

| Q | Answer |
| --- | --- |
| Q1 Why | Final determination of match outcome for an entry |
| Q2 / Q7 Owner | `MOD-RESOLUTION` |
| Q3 Aggregate | **Match Resolution** (root) |
| Q4 Identity | `resolution_id` (versioned history allowed) |
| Q5 Invariants | Outcomes only: `LINK_EXISTING` \| `CREATE_NEW` \| `DEFER` \| `RETURN_FOR_CORRECTION` \| `NO_ACTION`; **MUST NOT** mutate canonical person rows; promotion is separate |
| Q6 Lifecycle | `STATE-MATCH-RESOLUTION-001` |
| Q8 Modifiers | Resolution service only |
| Q9 Events | Domain `RESOLUTION` |
| Q10 Permissions | `PERM-MATCH-*` (decision) — not promotion execute alone |
| Q11 APIs | Resolution APIs (seed under match/resolution family) |
| Q12 Packages | Matching/resolution packages |
| Q13 Tests | Outcome enum closed set; no canonical writes; reopen/supersede rules |
| Table seed | `intake_match_resolutions` |

---

### ENT-PROMOTION — Promotion Request

| Q | Answer |
| --- | --- |
| Q1 Why | Controlled business acceptance: create/link canonical person data with provenance |
| Q2 / Q7 Owner | `MOD-PROMOTION` (+ `MOD-LAYER-INT` port) |
| Q3 Aggregate | **Promotion Request** (root) |
| Q4 Identity | `promotion_id` |
| Q5 Invariants | Independently stateful from resolution; idempotent at request boundary; durable before async canonical call; only intake path that requests canonical create/link |
| Q6 Lifecycle | `STATE-PROMOTION-001` (+ link `STATE-CANONICAL-LINK-001` on success path) |
| Q8 Modifiers | Promotion service; canonical port adapter |
| Q9 Events | Domains `PROMOTION`, `CANONICAL_INTEGRATION` (seed `AUDIT-PROMOTION-001`) |
| Q10 Permissions | `PERM-PROMOTION-001` |
| Q11 APIs | `API-PROMOTION-*` |
| Q12 Packages | Promotion packages |
| Q13 Tests | Idempotency; no resolution rewrite; fail/retry; provenance required |
| Table seed | `intake_promotion_requests` |
| Open | **ISSUE-CANONICAL-001**, ADR-016 |

---

### ENT-USER — Application User

| Q | Answer |
| --- | --- |
| Q1 Why | Authenticated actor in the system |
| Q2 / Q7 Owner | `MOD-USERS` (identity bind `MOD-IDENTITY`) |
| Q3 Aggregate | User / Role Grant |
| Q4 Identity | `user_id` |
| Q5 Invariants | Not an intake hierarchy member; auth method pending ADR-004 |
| Q6 Lifecycle | `STATE-USER-001` |
| Q8 Modifiers | User admin / identity services |
| Q9 Events | Domains `AUTHENTICATION`, `USER_MANAGEMENT` (seed `AUDIT-USER-001`) |
| Q10 Permissions | `PERM-USER-001`…`004`; `PERM-SYSTEM-001` as applicable |
| Q11 APIs | `API-USER-*` / session family |
| Q12 Packages | Auth/user packages (post ADR-004) |
| Q13 Tests | Invite/activate/suspend/revoke; no intake data smuggling |
| Table seed | `app_users` |

---

### ENT-ROLE-GRANT — Role Grant

| Q | Answer |
| --- | --- |
| Q1 Why | Assign authorized capability roles to users |
| Q2 / Q7 Owner | `MOD-ROLES` |
| Q3 Aggregate | User / Role Grant |
| Q4 Identity | Role grant ID |
| Q5 Invariants | Catalog 5 roles only; expired/revoked cannot authorize |
| Q6 Lifecycle | `STATE-ROLE-001` |
| Q8 Modifiers | Role service |
| Q9 Events | Domain `ROLE_MANAGEMENT` |
| Q10 Permissions | `PERM-ROLE-001` |
| Q11 APIs | `API-ROLE-*` |
| Q12 Packages | Admin/authz packages |
| Q13 Tests | Expire/revoke enforcement |
| Table seed | role tables (future) |

---

### ENT-AUDIT — Audit Event

| Q | Answer |
| --- | --- |
| Q1 Why | Append-only meaningful action record |
| Q2 / Q7 Owner | `MOD-AUDIT` |
| Q3 Aggregate | Audit store (append-only) |
| Q4 Identity | `event_id` |
| Q5 Invariants | Append-only; Catalog 03 names only; no secret values in payloads |
| Q6 Lifecycle | Append model (not a Catalog 01 business entity machine) |
| Q8 Modifiers | Audit writers via approved emitters; no update/delete of history |
| Q9 Events | Self (Catalog 03) |
| Q10 Permissions | `PERM-AUDIT-001` |
| Q11 APIs | `API-AUDIT-*` |
| Q12 Packages | Cross-cutting; every mutating package |
| Q13 Tests | Immutability; required fields; forbidden secret scan |
| Table seed | `intake_audit_events` |

---

### ENT-ERROR — Processing Error

| Q | Answer |
| --- | --- |
| Q1 Why | Operator-visible processing failure requiring handling |
| Q2 / Q7 Owner | `MOD-OPERATIONS` (with domain emitters) |
| Q3 Aggregate | Ops/error boundary |
| Q4 Identity | Error ID |
| Q5 Invariants | Catalog 2 codes for typed errors; no silent swallow of Critical |
| Q6 Lifecycle | `STATE-ERROR-001` |
| Q8 Modifiers | Ops/error services |
| Q9 Events | Ops/error audit as designed |
| Q10 Permissions | Admin/ops permissions |
| Q11 APIs | `API-ADMIN-*` / error surfaces |
| Q12 Packages | Ops packages |
| Q13 Tests | Open→resolved paths; escalation |
| Table seed | future |

---

### ENT-ALERT — Alert

| Q | Answer |
| --- | --- |
| Q1 Why | Operator attention signal |
| Q2 / Q7 Owner | `MOD-OPERATIONS` / notifications coordination |
| Q3 Aggregate | Ops |
| Q4 Identity | Alert ID |
| Q5 Invariants | Distinct from in-app Catalog 6 notification product messages when those exist |
| Q6 Lifecycle | `STATE-ALERT-001` |
| Q8 Modifiers | Ops/alert services |
| Q9 Events | Ops |
| Q10 Permissions | Admin/ops |
| Q11 APIs | Admin/ops |
| Q12 Packages | Ops |
| Q13 Tests | Ack/dismiss/escalate |
| Table seed | future |

---

### ENT-CANONICAL-PERSON — Canonical Person (**EXTERNAL**)

| Q | Answer |
| --- | --- |
| Q1 Why | Shared durable individual identity across authorized ecosystem |
| Q2 / Q7 Owner | **EXTERNAL** canonical domain (not People Intake) |
| Q3 Aggregate | External |
| Q4 Identity | Canonical person ID (minted outside intake) |
| Q5 Invariants | Intake must not write master rows except via controlled promotion port; Entry ≠ Person |
| Q6 Lifecycle | Owned externally; intake link via `STATE-CANONICAL-LINK-001` |
| Q8 Modifiers | Canonical service only; intake calls port |
| Q9 Events | Domain `CANONICAL_INTEGRATION` on intake side |
| Q10 Permissions | Promotion execute + external authz |
| Q11 APIs | External; intake `API-PROMOTION-*` only |
| Q12 Packages | Integration packages after ISSUE-CANONICAL-001 / ADR-016 |
| Q13 Tests | Anti-corruption: no direct table writes from matching/UI |
| Table seed | **OUTSIDE** intake schema |

---

### ENT-PERSON-ATTRIBUTE — Person Attribute (**EXTERNAL**)

| Q | Answer |
| --- | --- |
| Q1 Why | Canonical fact with provenance/history |
| Q2 / Q7 Owner | EXTERNAL canonical domain |
| Q3 Aggregate | External person |
| Q4 Identity | Attribute ID in canonical domain |
| Q5 Invariants | No silent flat overwrite; provenance required on accepted updates |
| Q6 Lifecycle | External |
| Q8 Modifiers | Canonical service via promotion outcomes |
| Q9 Events | Canonical integration |
| Q10 Permissions | External + promotion |
| Q11 APIs | External |
| Q12 Packages | Integration |
| Q13 Tests | Provenance present; rejected updates retained as decisions |
| Table seed | OUTSIDE intake |

---

### ENT-NORMALIZATION-RUN — Normalization Run

| Q | Answer |
| --- | --- |
| Q1 Why | Produce safe normalized counterparts without semantic invention |
| Q2 / Q7 Owner | `MOD-NORMALIZATION` |
| Q3 Aggregate | Often entry-associated run |
| Q4 Identity | Normalization run ID |
| Q5 Invariants | Raw preserved; UNKNOWN≠NO; no meaning reinterpretation |
| Q6 Lifecycle | `STATE-NORMALIZATION-001` |
| Q8 Modifiers | Normalization service |
| Q9 Events | Transcription/matching prep audits as designed |
| Q10 Permissions | Transcription/match families |
| Q11 APIs | Internal/domain; may be embedded in transcription APIs |
| Q12 Packages | Transcription/matching |
| Q13 Tests | Raw unchanged; deterministic normalize; refuse invention |
| Table seed | future / entry columns |

---

## 10. Data Contracts

Entity cards are conceptual. Column-level contracts → IS-202 / IS-300. Do not treat field-dictionary `status` strings as Catalog 01.

## 11. Interface Contracts

APIs listed are **families** (seed). Exact routes → Phase 5 IS. External canonical port → ISSUE-CANONICAL-001.

## 12–17. State / Permission / Error / Audit / Notification / Jobs

* State: Catalog 01 only (§5.1).  
* Permission: Catalog 05 seeds + amendment.  
* Error: Catalog 02.  
* Audit: Catalog 03 domains/seeds.  
* Notification: Catalog 06 when productized.  
* Jobs: Catalog 07 names for async touchpoints (match/promotion/upload/retention).  

## 18. Security and Privacy

Private images; no PII in Git; external canonical isolation; audit append-only.

## 19. Retention

Catalog 08 classes apply per entity class; exact durations ISSUE-RETENTION-001.

## 20. Observability

Correlate `batch_id` / `page_id` / `entry_id` / `promotion_id` / `claim_id`.

## 21. Testing matrix (mandatory themes)

| Theme | Applies to |
| --- | --- |
| Illegal Catalog 01 transition rejected | All stateful entities |
| Single active claim | ENT-CLAIM, ENT-PAGE |
| Draft survives claim expiry | ENT-DRAFT, ENT-CLAIM |
| No canonical write from match/resolution | ENT-MATCH-* |
| Promotion idempotency | ENT-PROMOTION |
| UNKNOWN≠NO / layer separation | ENT-ENTRY, ENT-NORMALIZATION-RUN |
| Queue cannot write claims | ENT-QUEUE-ITEM |
| Append-only audit | ENT-AUDIT |
| External boundary | ENT-CANONICAL-PERSON |

## 22. Acceptance Criteria

| ID | Criterion | Met? |
| --- | --- | --- |
| AC-ENT-001 | Mandatory questionnaire defined and applied to all admitted entities | Yes |
| AC-ENT-002 | Catalog 01 cited as sole state authority | Yes |
| AC-ENT-003 | Match Resolution ≠ Promotion enforced on cards | Yes |
| AC-ENT-004 | Extension decision tree locked | Yes |
| AC-ENT-005 | EXTERNAL entities explicitly marked | Yes |
| AC-ENT-006 | ISSUE-MOD-001 / CANONICAL-001 remain visible | Yes |
| AC-ENT-007 | No application/schema code created | Yes |

## 23. Open Decisions

| ID | Notes |
| --- | --- |
| ISSUE-MOD-001 | Entry writer split |
| ISSUE-CANONICAL-001 | Promotion DTO/port |
| ISSUE-STORAGE-001 | Storage provider |
| STATE-DEC-* | Persisted vs derived statuses |
| Field-dictionary ↔ Catalog 01 reconciliation | Tracked in audit lane |

## 24. Risks

| ID | Risk | Mitigation |
| --- | --- | --- |
| RISK-ENT-001 | Packages invent entities without cards | REQ-ENT-001/005 |
| RISK-ENT-002 | Field-dict statuses used as enums | REQ-ENT-006; audit lane |
| RISK-ENT-003 | Resolution writes persons | REQ-ENT-003 |
| RISK-ENT-004 | Promotion owns matching | REQ-ENT-004 |

## 25. Dependencies

IS-200, IS-102, Catalogs 01/03/05, audit lane for drift.

## 26. Traceability

| Requirement | Status |
| --- | --- |
| REQ-ENT-001…008 | FULLY_MAPPED (design) |
| Physical columns | PARTIALLY_MAPPED → IS-202/300 |

## 27. Implementation Boundary

**Authorized:** this encyclopedia; governance indexes/reports.  
**Forbidden:** migrations, Prisma app models, inventing catalog keys, closing open issues by omission.

## 28. Revision History

| Version | Date | Change | Approval |
| --- | --- | --- | --- |
| 1.0 | 2026-07-26 | Entity encyclopedia + admission gate + standing doctrine | D-070 |

## Entity index

```text
ENT-BATCH, ENT-PAGE, ENT-ENTRY, ENT-DRAFT, ENT-IMAGE, ENT-UPLOAD,
ENT-CLAIM, ENT-QUEUE-ITEM, ENT-MATCH-EVAL, ENT-MATCH-CANDIDATE,
ENT-MATCH-RESOLUTION, ENT-PROMOTION, ENT-USER, ENT-ROLE-GRANT,
ENT-AUDIT, ENT-ERROR, ENT-ALERT, ENT-NORMALIZATION-RUN,
ENT-CANONICAL-PERSON (EXTERNAL), ENT-PERSON-ATTRIBUTE (EXTERNAL)
```

## Next primary

```text
PEOPLE-IS-202-FIELD-AND-VALUE-OBJECT-SPECIFICATIONS-1.0
```

## Independent lane

```text
PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0
```

## Final status

```text
PEOPLE-IS-201 ENTITY SPECIFICATIONS: APPROVED (DOCUMENTATION)
APPLICATION IMPLEMENTATION: NOT AUTHORIZED
```
