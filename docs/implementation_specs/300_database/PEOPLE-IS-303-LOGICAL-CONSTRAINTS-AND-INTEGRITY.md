# PEOPLE-IS-303 — LOGICAL CONSTRAINTS AND INTEGRITY

**Title:** Logical Constraints and Integrity  
**Document ID:** `PEOPLE-IS-303-LOGICAL-CONSTRAINTS-AND-INTEGRITY-1.0`  
**Version:** 1.0  
**Status:** APPROVED  
**Phase:** PHASE 3 — DATABASE ARCHITECTURE  
**Project Root:** `H:\people`  
**Owner:** People Intake System Program  
**Approval Authority:** Decision Log D-075  
**Created Date:** 2026-07-26  
**Last Updated:** 2026-07-26  
**Governing Documents:** Catalog 01; IS-200; IS-201; IS-202; IS-300; IS-301; IS-302; Catalogs 02/03/08  
**Dependencies:** PEOPLE-IS-302 APPROVED (D-074)  
**Implementation Authorization:** `IMPLEMENTATION NOT AUTHORIZED`

```text
DESIGN COMPLETE
APPROVED FOR DOCUMENTATION GOVERNANCE
CANONICAL LOGICAL INTEGRITY AUTHORITY
NO SQL / DDL / CHECK / INDEX / TRIGGER / PRISMA / MIGRATIONS
NO EXECUTABLE VALIDATION CODE
APPLICATION IMPLEMENTATION NOT AUTHORIZED
```

---

## 1. Purpose

Define every **logical constraint** that must remain true across the governed persistence model so that future physical enforcement (DB constraints, application validation, jobs) **translates** approved business invariants—never invents them.

## 2. Scope

Constraint admission questionnaire; complete `CON-*` cards; category taxonomy; Catalog 01 lifecycle dependency; uniqueness / requiredness / referential / cardinality / temporal / ordering / immutability / append-only / concurrency / sensitivity / retention / cross-aggregate / external-boundary rules; failure classification placeholders; read-model implications; future physical enforcement options; required tests; traceability; package ownership.

## 3. Out of Scope

```text
FORBIDDEN:
  CREATE / ALTER / CHECK / UNIQUE / FK / INDEX / TRIGGER DDL
  Prisma @@unique / @@index / relation constraints as executable schema
  Migrations, seed scripts, live DB objects
  Executable validators, Zod/Joi schemas, service code
  Inventing invariants absent from Catalog 01 / IS-200…302
```

Exact SQL expressions, index strategies, and migration scripts → IS-305 / authorized packages after Gate G-10.  
Read-model composition deepens in **IS-304**.

## 4. Standing doctrine (locked)

### 4.1 Integrity doctrine

```text
A database constraint may enforce an approved business invariant.
It may not invent one.

Application validation may explain an invariant.
It may not weaken it.

Physical enforcement may use multiple mechanisms later.
The logical invariant remains technology-neutral and authoritative.
```

### 4.2 Authority hierarchy

```text
Catalog 01
  → lifecycle and state authority

IS-200
  → domain invariant authority

IS-201
  → entity invariant authority

IS-202
  → field / value-object constraint authority

IS-302
  → relationship invariant authority

IS-303 (this document)
  → consolidated logical integrity authority
```

Where source documents **conflict**, this IS **MUST surface** the conflict as an open issue or ADR dependency — it MUST NOT silently choose a rule.

### 4.3 Extension tree

```text
Need a new integrity rule?
  → Existing CON-* in this catalog?
      YES → Reuse / amend card
      NO  → Does Catalog 01 / IS-200…302 already require it?
              YES → Amend IS-303 (and upstream IS if needed) or ADR
              NO  → Reject
                    → Only then may physical packages implement enforcement
```

## 5. Mandatory constraint questionnaire

| # | Area | Questions |
| --- | --- | --- |
| C1 | Identity | Stable `CON-*` ID |
| C2 | Identity | Canonical name |
| C3 | Ownership | Owning aggregate |
| C4 | Ownership | Owning entity |
| C5 | Ownership | Owning logical table (`LT-*`) |
| C6 | Business | Invariant protected (plain language) |
| C7 | Category | Constraint category (see §6) |
| C8 | Scope | Scope (row / table / aggregate / cross-aggregate / external) |
| C9 | Boundary | Enforcement boundary (domain service / persistence / both / read-model) |
| C10 | Involved | Fields (`FLD-*` / VO-*) |
| C11 | Involved | Relationships (`REL-*`) |
| C12 | Behavior | Creation behavior |
| C13 | Behavior | Update behavior |
| C14 | Behavior | Deletion behavior |
| C15 | Behavior | Transition behavior |
| C16 | Lifecycle | Catalog 01 dependency |
| C17 | Null | Nullability / conditional requiredness |
| C18 | Unique | Uniqueness semantics |
| C19 | Ref | Referential-integrity expectation |
| C20 | Temporal | Temporal / sequencing rules |
| C21 | Concurrency | Concurrency implications |
| C22 | Sens | Sensitivity / audit / retention effects |
| C23 | Failure | Failure classification / future error mapping (Cat 02 placeholder) |
| C24 | Read | Read-model implications |
| C25 | Physical | Future physical enforcement options (non-SQL guidance) |
| C26 | Tests | Required tests |
| C27 | Trace | Traceability (IS-200…302 / Cat 01) |
| C28 | Package | Future implementation package ownership |

## 6. Constraint categories

| Category code | Meaning |
| --- | --- |
| `IDENTITY` | Durable identity uniqueness / immutability of IDs |
| `UNIQUENESS` | Business-key uniqueness |
| `REQUIREDNESS` | Required / conditionally required fields |
| `REFERENTIAL` | Logical FK / existence expectations |
| `CARDINALITY` | Count bounds (e.g. ≤10 entries) |
| `LIFECYCLE` | Catalog 01 state presence / legality |
| `STATE_TRANSITION` | Allowed Catalog 01 transitions only |
| `OWNERSHIP` | Module / service write ownership |
| `TEMPORAL` | Time, expiry, sequencing |
| `ORDERING` | Ordinal uniqueness / sort rules |
| `IMMUTABILITY` | Fields/rows that must not change after gate |
| `APPEND_ONLY` | Insert-only stores |
| `CONCURRENCY` | Optimistic locks / race prevention |
| `SENSITIVITY` | Classification / exposure limits |
| `RETENTION` | Retention / hold interaction |
| `CROSS_AGGREGATE` | Invariants spanning aggregates |
| `EXTERNAL_BOUNDARY` | External system / soft-ref rules |

---

## 7. Functional Requirements

| ID | Description |
| --- | --- |
| REQ-CON-001 | Every persisted integrity rule MUST have a `CON-*` card before physical enforcement. |
| REQ-CON-002 | Physical DB constraints MUST NOT invent business invariants absent from this catalog (or amendment/ADR). |
| REQ-CON-003 | Application validation MUST NOT weaken a logical invariant. |
| REQ-CON-004 | Lifecycle/state constraints MUST cite Catalog 01 exclusively. |
| REQ-CON-005 | Match Resolution constraints MUST NOT grant write authority to canonical person masters. |
| REQ-CON-006 | Promotion constraints MUST NOT redefine match resolution outcomes. |
| REQ-CON-007 | Queue / READ_MODEL constraints MUST forbid claim and resolution writes. |
| REQ-CON-008 | Source conflicts MUST be recorded as issues/ADRs — not silently resolved. |
| REQ-CON-009 | This package MUST NOT create SQL, Prisma, migrations, indexes, triggers, or executable validators. |
| REQ-CON-010 | New constraints require IS-303 amendment or ADR. |

---

## 8. Constraint catalog

Cards use the C1–C28 questionnaire. Condensed rows still bind the same fields.

### 8.1 Identity

#### CON-ID-ENTITY-PK — Entity primary identity

| Field | Value |
| --- | --- |
| C1–C2 | `CON-ID-ENTITY-PK` / EntityPrimaryIdentity |
| C3–C5 | Per owning aggregate / ENT-* / each TRANSACTIONAL `LT-*` |
| C6 | Every durable row has exactly one immutable opaque `id` (VO-UUID) |
| C7 | IDENTITY |
| C8–C9 | Row; persistence + domain create |
| C10–C11 | FLD-ID / VO-UUID; n/a |
| C12–C15 | Generated on create; never update; delete only via retention/archival policy; no transition of id |
| C16 | Independent of state |
| C17–C18 | NOT NULL; globally unique within LT |
| C19 | Referenced by child FKs where REL-* requires |
| C20–C21 | Stable forever; concurrent creates must not collide |
| C22 | Audit by entity id; retention keyed by id |
| C23 | `IDENTITY_COLLISION` / Cat 02 expansion |
| C24 | Read models key by id |
| C25 | PK unique; UUID gen; no natural-key PK for people lines |
| C26 | Create uniqueness; reject id mutation |
| C27 | IS-202 FLD-ID; REQ-DOM-007 |
| C28 | Intake core / per-module persistence pkgs |

#### CON-ID-BATCH-CODE — Batch code uniqueness

| Field | Value |
| --- | --- |
| C1–C2 | `CON-ID-BATCH-CODE` / BatchCodeUnique |
| C3–C5 | Batch / ENT-BATCH / LT-BATCH |
| C6 | `batch_code` uniquely identifies a batch for ops UX |
| C7 | IDENTITY + UNIQUENESS |
| C8–C9 | Table; MOD-BATCHES |
| C10–C11 | FLD-BATCH-CODE / VO-BATCH-CODE |
| C12–C15 | Assigned on create; immutable preferred; no delete reuse without ADR |
| C16 | N/A |
| C17–C18 | NOT NULL; unique |
| C19–C21 | n/a / stable / race on concurrent create |
| C22–C28 | CLASS-002; `BATCH_CODE_CONFLICT`; lists; unique index later; uniqueness tests; IS-202; batch pkg |

### 8.2 Uniqueness

#### CON-UNQ-PAGE-NUMBER — Page number unique per batch

| Field | Value |
| --- | --- |
| C1–C5 | `CON-UNQ-PAGE-NUMBER` / PageNumberPerBatch / Batch+Page / ENT-PAGE / LT-PAGE |
| C6 | `(batch_id, page_number)` unique among non-deleted pages |
| C7 | UNIQUENESS + ORDERING |
| C8–C9 | Aggregate; MOD-PAGES |
| C10–C11 | FLD-PAGE-NUMBER; REL-BATCH-PAGE |
| C12–C15 | Assigned on create; renumber only via governed transfer (not V1); restrict orphan pages |
| C16 | Independent |
| C17–C18 | NOT NULL; composite unique |
| C19 | batch_id must exist (CON-REF-BATCH-PAGE) |
| C20–C28 | Order stable for UX; create race; CLASS-002; conflict error; sort; composite unique later; tests; IS-202; pages pkg |

#### CON-UNQ-ENTRY-ROW — Entry row unique per page

| Field | Value |
| --- | --- |
| C1–C5 | `CON-UNQ-ENTRY-ROW` / EntryRowPerPage / Page+Entry / ENT-ENTRY / LT-ENTRY |
| C6 | `(page_id, row_number)` unique; row_number ∈ 1..10 |
| C7 | UNIQUENESS + ORDERING + CARDINALITY |
| C8–C9 | Aggregate; MOD-DRAFTS/TRANSCRIPTIONS |
| C10–C11 | FLD-ENTRY-ROW / VO-ROW-NUMBER; REL-PAGE-ENTRY |
| C12–C15 | Create only for real (non-blank) rows; no 11th row; blank ⇒ no entity |
| C16 | Entry Catalog 01 machine |
| C17–C18 | NOT NULL; composite unique |
| C19 | page_id exists |
| C20–C28 | Row order = sheet order; concurrent add race; CLASS-003; `ENTRY_ROW_CONFLICT` / `ENTRY_CARDINALITY`; lists; unique+check later; tests; IS-200 REQ-DOM-003; entry pkg |

#### CON-UNQ-CLAIM-ACTIVE — At most one active claim per page/work type

| Field | Value |
| --- | --- |
| C1–C5 | `CON-UNQ-CLAIM-ACTIVE` / ActiveClaimExclusive / Claim / ENT-CLAIM / LT-CLAIM |
| C6 | ≤1 active claim per `(page_id, work_type)` |
| C7 | UNIQUENESS + CARDINALITY + CONCURRENCY |
| C8–C9 | Aggregate; **claim service only** |
| C10–C11 | page_id, work_type, status, expires_at; REL-PAGE-CLAIM-ACTIVE |
| C12–C15 | Create active if none; updates release/expire; delete rare (prefer terminal state) |
| C16 | Claim Catalog 01 machine — active vs terminal |
| C17–C18 | Partial uniqueness among active states only |
| C19 | page_id + claimed_by_user_id required while active |
| C20 | Expiry may end active without erasing drafts |
| C21 | Must prevent dual-active races |
| C22–C28 | CLAIM audits; CLASS-002; `CLAIM_CONFLICT`; queue reads only; partial unique later; race tests; IS-201 claim; claim pkg |

#### CON-UNQ-PROMO-IDEMPOTENCY — Promotion idempotency key

| Field | Value |
| --- | --- |
| C1–C5 | `CON-UNQ-PROMO-IDEMPOTENCY` / PromotionIdempotency / Promotion / ENT-PROMOTION / LT-PROMOTION |
| C6 | `idempotency_key` unique for replay-safe promotion requests |
| C7 | UNIQUENESS |
| C8–C9 | Aggregate; MOD-PROMOTION |
| C10–C11 | FLD-PROMO-IDEMPOTENCY |
| C12–C15 | Set on create; immutable; no reuse |
| C16 | Promotion Catalog 01 |
| C17–C18 | NOT NULL; unique |
| C19–C28 | Ties to entry/resolution; concurrent replay returns same outcome; CLASS-002; conflict/idempotent success; unique later; ADR-014 posture; promotion pkg |

#### CON-UNQ-USER-EMAIL — User email uniqueness

| Field | Value |
| --- | --- |
| C1–C5 | `CON-UNQ-USER-EMAIL` / UserEmailUnique / User / ENT-USER / LT-USER |
| C6 | Login email unique among active users (provider-dependent) |
| C7 | UNIQUENESS |
| C8–C9 | Table; MOD-USERS |
| C10 | FLD-USER-EMAIL |
| C16–C28 | Auth lifecycle; NOT NULL when local; unique; CLASS-004; ADR-004; auth pkg — **exact provider uniqueness deferred if provider owns identity (surface ADR-004)** |

### 8.3 Requiredness

#### CON-REQ-PAGE-BATCH — Page requires batch

| Field | Value |
| --- | --- |
| C1–C7 | `CON-REQ-PAGE-BATCH` / PageRequiresBatch / Page / ENT-PAGE / LT-PAGE / Page always belongs to one batch / REQUIREDNESS + REFERENTIAL |
| C8–C11 | Row; MOD-PAGES; batch_id; REL-BATCH-PAGE |
| C12–C15 | batch_id required at create; immutable in V1; restrict delete parent with children |
| C16–C28 | Page Cat 01; NOT NULL; FK expected; tests; IS-302 REL-BATCH-PAGE; pages pkg |

#### CON-REQ-ENTRY-PAGE — Entry requires page

Same pattern: `CON-REQ-ENTRY-PAGE` — entry.`page_id` NOT NULL; REL-PAGE-ENTRY; blank rows do not create entries.

#### CON-REQ-CLAIM-USER — Active claim requires user

`CON-REQ-CLAIM-USER` — while claim active, `claimed_by_user_id` NOT NULL; REL-CLAIM-USER.

#### CON-REQ-STATE-CAT01 — Lifecycle state required and Catalog 01 typed

| Field | Value |
| --- | --- |
| C1–C7 | `CON-REQ-STATE-CAT01` / Catalog01StateRequired / per stateful ENT / LT-* with VO-CAT01-STATE / Every business lifecycle field is Catalog 01 / REQUIREDNESS + LIFECYCLE |
| C8–C11 | Row; owning module; FLD-* status via VO-CAT01-STATE |
| C12–C15 | Required on create; updates only via legal transitions; terminal states restrict further illegal moves |
| C16 | **Sole** state authority = Catalog 01 |
| C17 | NOT NULL for stateful entities |
| C18–C19 | Enum membership = uniqueness of code within machine |
| C23 | `INVALID_STATE` / `ILLEGAL_TRANSITION` |
| C25 | Enum/check + service guard (both allowed; neither invents states) |
| C26 | Reject field-dictionary draft labels (`UPLOADING`, etc.) |
| C27 | Cat 01; IS-202 REQ-FLD-002; ISSUE-AUDIT-001 |
| C28 | Per-module pkgs |

#### CON-REQ-PREF-UNKNOWN — Preference UNKNOWN allowed

`CON-REQ-PREF-UNKNOWN` — YES\|NO\|UNKNOWN required where preference fields exist; UNKNOWN MUST NOT coerce to NO (IS-202 REQ-FLD-005). Category: REQUIREDNESS. LT-ENTRY.

### 8.4 Referential

#### CON-REF-BATCH-PAGE — Page → Batch existence

Enforces REL-BATCH-PAGE: child→parent; ON DELETE RESTRICT philosophy; no orphan pages.

#### CON-REF-PAGE-ENTRY — Entry → Page existence

Enforces REL-PAGE-ENTRY; RESTRICT; ≤10 enforced with CON-UNQ-ENTRY-ROW / CON-CARD-ENTRIES-MAX10.

#### CON-REF-PAGE-IMAGE-ACTIVE — Page active image ownership (resolved)

| Field | Value |
| --- | --- |
| C1–C2 | `CON-REF-PAGE-IMAGE-ACTIVE` / PageOwnsActiveImageRef |
| C3–C5 | Page / ENT-PAGE / LT-PAGE (+ LT-IMAGE) |
| C6 | At most one **active** source image per page; page holds the active `source_image_id` |
| C7 | REFERENTIAL + CARDINALITY |
| C8–C9 | Aggregate; MOD-PAGES + MOD-UPLOADS coordination |
| C10–C11 | LT-PAGE.`source_image_id`; REL-PAGE-IMAGE-ACTIVE; REL-IMAGE-VERSION |
| C12–C15 | Set on successful upload; supersede via new image/version without losing provenance; restrict delete of active image |
| C16 | Page/image Cat 01 as applicable |
| C17 | Nullable until first successful upload path completes; required afterward for transcription evidence path |
| C18 | Active uniqueness via page-side ref (not dual writers) |
| C19 | Logical FK **page → image** (canonical direction locked here; closes IS-302 open item) |
| C20–C28 | Version history on LT-IMAGE-VERSION; CLASS-004; no public URL as identity; storage pkg |

#### CON-REF-CLAIM-PAGE — Claim → Page

Enforces REL-PAGE-CLAIM-ACTIVE; claim service writer.

#### CON-REF-MATCH-RUN-ENTRY — Match run → Entry

Enforces REL-ENTRY-MATCH-RUN.

#### CON-REF-CANDIDATE-RUN — Candidate → Match run

Enforces REL-MATCH-RUN-CANDIDATE.

#### CON-REF-RESOLUTION-ENTRY — Resolution → Entry

Enforces REL-ENTRY-RESOLUTION; resolution does not write persons.

#### CON-REF-PROMOTION-RESOLUTION — Promotion → Resolution

Enforces REL-RESOLUTION-PROMOTION; promotion independently stateful.

#### CON-REF-PROMOTION-ENTRY — Promotion → Entry

Enforces REL-PROMOTION-ENTRY.

#### CON-REF-CORRECTION-ENTRY — Correction → Entry

Enforces REL-ENTRY-CORRECTION; append-preferred.

#### CON-REF-ROLE-USER — Role grant → User

Enforces REL-USER-ROLE.

### 8.5 Cardinality

#### CON-CARD-ENTRIES-MAX10 — Max ten entries per page

| Field | Value |
| --- | --- |
| C1–C7 | `CON-CARD-ENTRIES-MAX10` / MaxTenEntriesPerPage / Page / ENT-PAGE+ENTRY / LT-ENTRY / Count(entries) ≤ 10 / CARDINALITY |
| C8–C11 | Aggregate; transcription modules; REL-PAGE-ENTRY; FLD-PAGE-ENTRY-COUNT derived |
| C12–C15 | Reject 11th create; blank rows do not count |
| C16–C28 | Entry machine; `ENTRY_CARDINALITY`; IS-200; entry pkg |

#### CON-CARD-ACTIVE-RESOLUTION — At most one current resolution per entry

`CON-CARD-ACTIVE-RESOLUTION` — 0..1 **current** resolution; prior versions retained; REL-ENTRY-RESOLUTION.

### 8.6 Lifecycle & state transition

#### CON-LIFE-CAT01-ONLY — No alternate state vocabularies

| Field | Value |
| --- | --- |
| C1–C7 | `CON-LIFE-CAT01-ONLY` / Catalog01SoleStateAuthority / all stateful / LIFECYCLE |
| C6 | Production persisted state codes MUST be Catalog 01 machine enums only |
| C23 | `INVALID_STATE` |
| C26 | Sweep rejects field-dictionary statuses as production |
| C27 | Cat 01; ISSUE-AUDIT-001 (surfaced, not silently closed) |
| C28 | All stateful pkgs |

#### CON-LIFE-TRANSITION-LEGAL — Only Catalog 01 transitions

| Field | Value |
| --- | --- |
| C1–C7 | `CON-LIFE-TRANSITION-LEGAL` / LegalStateTransitionsOnly / stateful ENT / STATE_TRANSITION |
| C6 | State changes MUST follow Catalog 01 transition graph for that machine |
| C9 | Domain service primary; DB may store state but MUST NOT invent transitions |
| C15 | Illegal transition → reject; audit attempted failure per Cat 03 policy |
| C23 | `ILLEGAL_TRANSITION` |
| C25 | Service guard required; optional DB trigger **only if** it enforces same graph (not a new graph) |
| C27 | Cat 01; IS-201 Q6 answers |
| C28 | Per-entity pkgs |

### 8.7 Ownership

#### CON-OWN-CLAIM-SERVICE — Claim writes exclusive

| Field | Value |
| --- | --- |
| C1–C7 | `CON-OWN-CLAIM-SERVICE` / ClaimServiceSoleWriter / Claim / OWNERSHIP |
| C6 | Only claim service may insert/update claim rows; queue MUST NOT |
| C9 | Domain service boundary (DB role grants later optional) |
| C11 | REL-PAGE-CLAIM-ACTIVE; REL-QUEUE-CLAIM |
| C23 | `OWNERSHIP_VIOLATION` |
| C26 | Queue mutation attempts fail |
| C27 | IS-201 claim; IS-302 REL-QUEUE-* |
| C28 | claim pkg |

#### CON-OWN-QUEUE-READONLY — Queue projection non-authoritative

`CON-OWN-QUEUE-READONLY` — LT-QUEUE is READ_MODEL; no claim/resolution/page authoritative writes (REQ-LTC-004; REL-QUEUE-*).

#### CON-OWN-SINGLE-MODULE — One owning module per write concept

`CON-OWN-SINGLE-MODULE` — cross-check IS-102; `OWNERSHIP_CONFLICT` if dual writers (REQ-DOM-004).

### 8.8 Temporal & ordering

#### CON-TEMP-CLAIM-EXPIRY — Claim expiry restores availability

| Field | Value |
| --- | --- |
| C1–C7 | `CON-TEMP-CLAIM-EXPIRY` / ClaimExpirySemantics / Claim / TEMPORAL |
| C6 | Expiry ends active claim **without** erasing recoverable drafts |
| C16 | Claim Cat 01 terminal/expired path |
| C20 | `expires_at` compared to trusted clock |
| C26 | Expiry job / transition tests; draft survival |
| C27 | IS-201 claim invariants |
| C28 | claim + jobs pkgs |

#### CON-TEMP-MATCH-BEFORE-PROMOTE — Promotion requires resolution context

| Field | Value |
| --- | --- |
| C1–C7 | `CON-TEMP-MATCH-BEFORE-PROMOTE` / PromotionAfterResolution / Promotion / TEMPORAL + CROSS_AGGREGATE + ORDERING |
| C6 | Promotion request references an existing match resolution; promotion does not invent match outcome |
| C11 | REL-RESOLUTION-PROMOTION; REL-PROMOTION-ENTRY |
| C16 | Both machines independent; sequencing is business prerequisite |
| C23 | `PREREQUISITE_MISSING` |
| C27 | Match ≠ Promotion (IS-200) |
| C28 | promotion pkg |

#### CON-ORD-PAGE-NUMBER — Page ordinal ≥ 1

Covered with CON-UNQ-PAGE-NUMBER; ordinal ≥1.

#### CON-ORD-ENTRY-ROW — Entry row ∈ [1,10]

Covered with CON-UNQ-ENTRY-ROW.

### 8.9 Immutability & append-only

#### CON-IMM-ENTITY-ID — Primary keys immutable

Covered by CON-ID-ENTITY-PK.

#### CON-IMM-SUBMITTED-REVISION — Submitted transcription immutable

| Field | Value |
| --- | --- |
| C1–C7 | `CON-IMM-SUBMITTED-REVISION` / SubmittedRevisionImmutable / Entry / IMMUTABILITY |
| C6 | After submit gate, submitted revision fields and `submitted_at` MUST NOT mutate in place; corrections via LT-ENTRY-CORRECTION |
| C10 | FLD-ENTRY-SUBMITTED-AT + submitted payload fields |
| C13 | In-place update forbidden post-submit |
| C23 | `IMMUTABILITY_VIOLATION` |
| C27 | IS-201 draft/entry; IS-202 |
| C28 | transcription pkg |

#### CON-IMM-MATCH-RUN — Completed match run immutable

`CON-IMM-MATCH-RUN` — LT-MATCH-RUN immutable after complete; supersede via new run (REL-ENTRY-MATCH-RUN).

#### CON-APP-AUDIT — Audit append-only

| Field | Value |
| --- | --- |
| C1–C7 | `CON-APP-AUDIT` / AuditAppendOnly / Audit / APPEND_ONLY + IMMUTABILITY |
| C6 | LT-AUDIT insert-only; no business update/delete; no cascade rewrite of history |
| C11 | REL-AUDIT-CORRELATION |
| C14 | Physical delete only under Cat 08 retention / legal hold exceptions |
| C22 | Sensitivity by payload class; retention holds |
| C25 | No UPDATE grants; partitioning later OK |
| C27 | Cat 03; IS-301 APPEND_ONLY |
| C28 | audit pkg |

#### CON-APP-ENTRY-CORRECTION — Corrections append-preferred

`CON-APP-ENTRY-CORRECTION` — LT-ENTRY-CORRECTION append-only preferred; preserves prior values.

#### CON-APP-PROMOTION-RESULT — Promotion results append-preferred

`CON-APP-PROMOTION-RESULT` — LT-PROMOTION-RESULT append for attempt outcomes.

### 8.10 Concurrency

#### CON-CONC-OPT-LOCK — Optimistic concurrency token

| Field | Value |
| --- | --- |
| C1–C7 | `CON-CONC-OPT-LOCK` / OptimisticLockToken / mutable TRANSACTIONAL LTs / CONCURRENCY |
| C6 | Updates carrying stale `version` MUST fail; token monotonic |
| C10 | FLD-VERSION / VO-OPT-LOCK |
| C21 | Prevent lost updates on page/entry/claim/promotion |
| C23 | `STALE_VERSION` |
| C25 | version column compare-and-swap; optional row lock in critical claim path |
| C27 | ADR-015 posture; IS-202 |
| C28 | Per mutable aggregate pkgs |

#### CON-CONC-CLAIM-RACE — Dual-active claim prevention

Works with CON-UNQ-CLAIM-ACTIVE; claim acquire must be atomic relative to exclusivity constraint.

### 8.11 Sensitivity & retention

#### CON-SENS-NO-PUBLIC-IMAGE — Image identity not public URL

| Field | Value |
| --- | --- |
| C1–C7 | `CON-SENS-NO-PUBLIC-IMAGE` / PrivateImageIdentity / Source Image / SENSITIVITY |
| C6 | Active image identity MUST NOT be a public CDN URL; private storage keys only |
| C22 | CLASS-004; IMAGE audits |
| C23 | `SENSITIVITY_VIOLATION` |
| C27 | IS-201 image; IS-302 REL-PAGE-IMAGE-ACTIVE |
| C28 | storage pkg |

#### CON-SENS-CLASS-PROPAGATE — Child inherits parent classification floor

`CON-SENS-CLASS-PROPAGATE` — child rows must not under-classify relative to governing Cat 08 class for the evidence chain (guidance; exact matrix Cat 08).

#### CON-RET-CHILD-PARENT — Child retention vs parent purge

`CON-RET-CHILD-PARENT` — child evidence must not outlive parent purge without explicit hold (IS-302 R22 patterns); durations ISSUE-RETENTION-001.

#### CON-RET-AUDIT-HOLD — Audit retention independent of UI delete

`CON-RET-AUDIT-HOLD` — UI/business delete MUST NOT silently purge audit required by Cat 08 / holds.

### 8.12 Cross-aggregate

#### CON-XAGG-MATCH-NE-PROMO — Match Resolution ≠ Promotion

| Field | Value |
| --- | --- |
| C1–C7 | `CON-XAGG-MATCH-NE-PROMO` / MatchNotPromotion / Match Resolution + Promotion / CROSS_AGGREGATE |
| C6 | Neither aggregate owns the other; promotion must not rewrite resolution outcome; resolution must not perform promotion |
| C11 | REL-RESOLUTION-PROMOTION |
| C23 | `BOUNDARY_VIOLATION` |
| C26 | Cross-module write attempts fail |
| C27 | IS-200 REQ-DOM-011; IS-201; IS-302 |
| C28 | matching + resolution + promotion pkgs |

#### CON-XAGG-RESOLUTION-NO-PERSON-WRITE — Resolution cannot write person masters

`CON-XAGG-RESOLUTION-NO-PERSON-WRITE` — Match resolution / candidates MUST NOT write LT-CANONICAL-PERSON (EXTERNAL). Soft refs only.

#### CON-XAGG-LINKED-PERSON-VIA-PROMO — Entry linked person only via promotion success

`CON-XAGG-LINKED-PERSON-VIA-PROMO` — `linked_canonical_person_id` set only through promotion success path (REL-ENTRY-PERSON-LINK); not by resolution alone.

#### CON-XAGG-SHARED-CONTACT-NE-IDENTITY — Shared contact ≠ identity

`CON-XAGG-SHARED-CONTACT-NE-IDENTITY` — household/shared contact classification MUST NOT alone establish canonical identity (IS-202 REQ-FLD-006).

### 8.13 External-system boundary

#### CON-EXT-CANONICAL-SOFT-REF — Canonical person soft reference default

| Field | Value |
| --- | --- |
| C1–C7 | `CON-EXT-CANONICAL-SOFT-REF` / CanonicalSoftRefDefault / EXTERNAL_BOUNDARY |
| C6 | Intake stores external person ids as soft references by default; physical FK to person master only if ISSUE-CANONICAL-001 / ISSUE-DBA-001 authorize |
| C19 | Soft referential integrity (existence checked via port, not required local FK) |
| C25 | Prefer application/port checks; physical FK deferred |
| C27 | IS-302 EXTERNAL_REF RELs; ISSUE-CANONICAL-001; ISSUE-DBA-001 (**surfaced**) |
| C28 | matching + promotion + integration pkgs |

#### CON-EXT-NO-INTAKE-PERSON-MASTER — No intake-owned person master table writes

`CON-EXT-NO-INTAKE-PERSON-MASTER` — LT-CANONICAL-PERSON / LT-PERSON-ATTRIBUTE remain EXTERNAL; intake MUST NOT invent local master write tables to bypass the port.

---

## 9. Constraint index

```text
CON-ID-ENTITY-PK
CON-ID-BATCH-CODE
CON-UNQ-PAGE-NUMBER
CON-UNQ-ENTRY-ROW
CON-UNQ-CLAIM-ACTIVE
CON-UNQ-PROMO-IDEMPOTENCY
CON-UNQ-USER-EMAIL
CON-REQ-PAGE-BATCH
CON-REQ-ENTRY-PAGE
CON-REQ-CLAIM-USER
CON-REQ-STATE-CAT01
CON-REQ-PREF-UNKNOWN
CON-REF-BATCH-PAGE
CON-REF-PAGE-ENTRY
CON-REF-PAGE-IMAGE-ACTIVE
CON-REF-CLAIM-PAGE
CON-REF-MATCH-RUN-ENTRY
CON-REF-CANDIDATE-RUN
CON-REF-RESOLUTION-ENTRY
CON-REF-PROMOTION-RESOLUTION
CON-REF-PROMOTION-ENTRY
CON-REF-CORRECTION-ENTRY
CON-REF-ROLE-USER
CON-CARD-ENTRIES-MAX10
CON-CARD-ACTIVE-RESOLUTION
CON-LIFE-CAT01-ONLY
CON-LIFE-TRANSITION-LEGAL
CON-OWN-CLAIM-SERVICE
CON-OWN-QUEUE-READONLY
CON-OWN-SINGLE-MODULE
CON-TEMP-CLAIM-EXPIRY
CON-TEMP-MATCH-BEFORE-PROMOTE
CON-ORD-PAGE-NUMBER
CON-ORD-ENTRY-ROW
CON-IMM-ENTITY-ID
CON-IMM-SUBMITTED-REVISION
CON-IMM-MATCH-RUN
CON-APP-AUDIT
CON-APP-ENTRY-CORRECTION
CON-APP-PROMOTION-RESULT
CON-CONC-OPT-LOCK
CON-CONC-CLAIM-RACE
CON-SENS-NO-PUBLIC-IMAGE
CON-SENS-CLASS-PROPAGATE
CON-RET-CHILD-PARENT
CON-RET-AUDIT-HOLD
CON-XAGG-MATCH-NE-PROMO
CON-XAGG-RESOLUTION-NO-PERSON-WRITE
CON-XAGG-LINKED-PERSON-VIA-PROMO
CON-XAGG-SHARED-CONTACT-NE-IDENTITY
CON-EXT-CANONICAL-SOFT-REF
CON-EXT-NO-INTAKE-PERSON-MASTER
```

## 10. Surfaced conflicts & deferred decisions (not silently resolved)

| ID | Conflict / deferral | Disposition in IS-303 |
| --- | --- | --- |
| ISSUE-AUDIT-001 | Field-dictionary draft statuses vs Catalog 01 | CON-LIFE-CAT01-ONLY / CON-REQ-STATE-CAT01 enforce Cat 01; issue remains OPEN until draft docs remediated |
| ISSUE-CANONICAL-001 | Exact canonical person contract / physical FK | CON-EXT-CANONICAL-SOFT-REF; physical FK not invented |
| ISSUE-DBA-001 | Shared-DB compatibility | Soft-ref default; no assumed remote tables |
| ISSUE-RETENTION-001 | Exact retention durations | CON-RET-* cite holds; durations still OPEN |
| ADR-004 | Auth provider email uniqueness ownership | CON-UNQ-USER-EMAIL notes provider-dependent |
| ADR-014 | Idempotency exact scheme | CON-UNQ-PROMO-IDEMPOTENCY posture only |
| ADR-015 | Concurrency token exact type | CON-CONC-OPT-LOCK posture only |
| Queue VIEW vs table | Physical shape | Constraint CON-OWN-QUEUE-READONLY locked; physical choice → IS-304 |
| Cascade matrix detail | Per-table ON DELETE | Default philosophy RESTRICT; package-level cascade only with Cat 08 + IS-305 |

**Resolved in this IS (was open in IS-302):** Page↔Image active FK direction → **page owns `source_image_id`** (CON-REF-PAGE-IMAGE-ACTIVE).

## 11. Acceptance Criteria

| ID | Criterion | Met? |
| --- | --- | --- |
| AC-CON-001 | Questionnaire C1–C28 defined | Yes |
| AC-CON-002 | All §6 categories represented by ≥1 CON-* | Yes |
| AC-CON-003 | Integrity doctrine locked | Yes |
| AC-CON-004 | Authority hierarchy locked; conflicts surfaced | Yes |
| AC-CON-005 | Match≠Promotion / EXTERNAL / queue non-write constrained | Yes |
| AC-CON-006 | Catalog 01 sole state authority constrained | Yes |
| AC-CON-007 | No SQL/Prisma/migrations/validators created | Yes |

## 12. Risks

| ID | Risk | Mitigation |
| --- | --- | --- |
| RISK-CON-001 | DB CHECK invents business rule | REQ-CON-002 |
| RISK-CON-002 | App validation weakens invariant | REQ-CON-003 |
| RISK-CON-003 | Duplicate state vocabularies | CON-LIFE-CAT01-ONLY + ISSUE-AUDIT-001 |
| RISK-CON-004 | Physical FK to canonical invents ownership | CON-EXT-*; ISSUE-CANONICAL-001 |

## 13. Dependencies

Catalog 01; IS-200; IS-201; IS-202; IS-301; IS-302; Catalogs 02/03/08; open ADRs/issues listed in §10.

## 14. Traceability

`CON-*` ↔ `REL-*` ↔ `LT-*` ↔ `ENT-*` ↔ `FLD-*` / Cat 01 — FULLY_MAPPED (logical).  
Physical enforcement DDL → IS-305 / authorized packages.

## 15. Implementation Boundary

**Authorized:** this constraint catalog; governance; audit verification.  
**Forbidden:** executable schema, indexes, triggers, migrations, validators.

## 16. Revision History

| Version | Date | Change | Approval |
| --- | --- | --- | --- |
| 1.0 | 2026-07-26 | Logical constraints & integrity catalog | D-075 |

## Next primary

```text
PEOPLE-IS-304-READ-MODEL-SPECIFICATIONS-1.0
```

## Independent lane

```text
PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0
```

## Final status

```text
PEOPLE-IS-303 LOGICAL CONSTRAINTS AND INTEGRITY: APPROVED (DOCUMENTATION)
DB CONSTRAINT MAY ENFORCE — MUST NOT INVENT — BUSINESS INVARIANTS
APPLICATION VALIDATION MAY EXPLAIN — MUST NOT WEAKEN
LOGICAL INVARIANT IS TECHNOLOGY-NEUTRAL AND AUTHORITATIVE
SQL / PRISMA / MIGRATIONS / EXECUTABLE VALIDATORS: NOT AUTHORIZED
```
