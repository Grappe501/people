# PEOPLE-IS-302 — LOGICAL RELATIONSHIP SPECIFICATIONS

**Title:** Logical Relationship Specifications  
**Document ID:** `PEOPLE-IS-302-LOGICAL-RELATIONSHIP-SPECIFICATIONS-1.0`  
**Version:** 1.0  
**Status:** APPROVED  
**Phase:** PHASE 3 — DATABASE ARCHITECTURE  
**Project Root:** `H:\people`  
**Owner:** People Intake System Program  
**Approval Authority:** Decision Log D-074  
**Created Date:** 2026-07-26  
**Last Updated:** 2026-07-26  
**Governing Documents:** IS-300; IS-301; IS-200; IS-201; IS-102; Catalogs 01/03/08  
**Dependencies:** PEOPLE-IS-301 APPROVED (D-073)  
**Implementation Authorization:** `IMPLEMENTATION NOT AUTHORIZED`

```text
DESIGN COMPLETE
APPROVED FOR DOCUMENTATION GOVERNANCE
CANONICAL LOGICAL RELATIONSHIP TOPOLOGY
RELATIONSHIPS ARE GOVERNED BUSINESS CONCEPTS
NO PHYSICAL FK MAY INVENT A BUSINESS RELATIONSHIP
NO SQL / DDL / PRISMA / MIGRATIONS
APPLICATION IMPLEMENTATION NOT AUTHORIZED
```

---

## 1. Purpose

Define the **topology** of logical persistence: every governed relationship among LT-* objects so that future physical foreign keys, join tables, and ORM relations **translate** approved business structure—never invent it.

## 2. Scope

Relationship admission questionnaire; complete REL-* cards; cardinality; ownership/lifecycle/deletion semantics; business invariants; navigation rules; logical FK/join expectations; audit/sensitivity/retention interaction; future physical mapping guidance (non-SQL); extension doctrine.

## 3. Out of Scope

```text
FORBIDDEN:
  CREATE TABLE / ALTER / FK DDL
  Prisma relation blocks as executable schema
  Migrations, cascade SQL, index DDL
  Inventing relationships absent from this catalog
```

Exact constraint expressions deepen in **IS-303**. Read-model composition deepens in **IS-304**.

## 4. Standing doctrine (locked)

```text
Relationships are governed business concepts,
not implementation conveniences.

No future migration or ORM relationship may appear
unless it already exists in IS-302 (or an approved amendment/ADR).

No physical foreign key may invent a business relationship.
```

### 4.1 Extension tree

```text
Need a new association between persisted concepts?
  → Existing REL-* in this catalog?
      YES → Reuse
      NO  → Does domain (IS-200/201) require it?
              YES → Amend IS-302 (and IS-301 if new LT needed) or ADR
              NO  → Reject
                    → Only then may physical schema packages implement FKs
```

## 5. Mandatory relationship questionnaire

| # | Area | Questions |
| --- | --- | --- |
| R1–R4 | Identity | Relationship ID; name; owning aggregate; relationship type |
| R5–R6 | Cardinality | Cardinality class; optional vs required |
| R7–R9 | Ownership | Owning LT; lifecycle control; deletion semantics |
| R10–R12 | Business | Why exists; invariant; domain rule source |
| R13–R15 | Navigation | Allowed traversal; forbidden traversal; read-model implications |
| R16–R19 | Persistence | Logical FK expectation; join table?; denorm guidance; read-model notes |
| R20–R22 | Audit | Audit expectations; sensitivity propagation; retention interaction |
| R23–R25 | Future physical | PK/FK direction; cascade philosophy; migration package |

**Relationship types:** `COMPOSITION` | `AGGREGATION` | `REFERENCE` | `PROJECTION` | `EXTERNAL_REF` | `CORRELATION`

## 6. Functional Requirements

| ID | Description |
| --- | --- |
| REQ-REL-001 | Every persisted business association MUST have a REL-* card before physical FK/ORM mapping. |
| REQ-REL-002 | Physical FKs MUST NOT invent relationships absent from this catalog. |
| REQ-REL-003 | Match Resolution relationships MUST NOT imply ownership of canonical person masters. |
| REQ-REL-004 | Queue PROJECTION relationships MUST NOT grant claim-write authority. |
| REQ-REL-005 | Audit CORRELATION MUST remain append-only and non-owning. |
| REQ-REL-006 | New relationships require IS-302 amendment or ADR. |
| REQ-REL-007 | This package MUST NOT create SQL/Prisma/migrations. |

## 7. Relationship catalog

### REL-BATCH-PAGE — Batch contains Pages

| Field | Value |
| --- | --- |
| R1 ID | `REL-BATCH-PAGE` |
| R2 Name | BatchContainsPages |
| R3 Owning aggregate | Batch |
| R4 Type | COMPOSITION |
| R5 Cardinality | Batch **1 — \*** Page |
| R6 Optionality | Page **requires** Batch; Batch may have 0 pages temporarily |
| R7 Owning LT | LT-PAGE holds `batch_id` (child FK) |
| R8 Lifecycle | Page lifecycle nested under batch context; batch archive does not auto-erase evidence without Cat 08 |
| R9 Deletion | Restrict deleting batch with live pages; cascade only if explicit package + Cat 08 allow |
| R10 Why | Shared collection context (IS-200) |
| R11 Invariant | Every page belongs to exactly one batch |
| R12 Domain rule | D-029 / IS-200 hierarchy |
| R13 Allowed nav | Batch→Pages; Page→Batch |
| R14 Forbidden | Page without batch; page moving batches without formal transfer (not V1) |
| R15 Read-model | Queue/batch lists join on batch_id |
| R16 Logical FK | `intake_pages.batch_id → intake_batches.id` |
| R17 Join table | No |
| R18 Denorm | Optional batch_code on page **discouraged**; prefer join |
| R19 Read-model notes | Batch counters may be derived |
| R20 Audit | Page create/move audited |
| R21 Sensitivity | Propagates batch CLASS-002 + page |
| R22 Retention | Child cannot outlive parent purge without explicit hold |
| R23 FK direction | Child→parent |
| R24 Cascade philosophy | ON DELETE RESTRICT (default) |
| R25 Migration pkg | Intake core |

### REL-PAGE-ENTRY — Page contains Entries

| Field | Value |
| --- | --- |
| R1–R4 | `REL-PAGE-ENTRY` / PageContainsEntries / Page / COMPOSITION |
| R5–R6 | Page **1 — 0..\*** Entry (max 10); entry requires page |
| R7–R9 | LT-ENTRY.`page_id`; entry owned by page aggregate for membership; delete page restricted if entries exist unless package defines archival |
| R10–R12 | Person lines on sheet; ≤10; blank row ≠ entry (IS-200) |
| R13–R15 | Page→Entries; Entry→Page; UI must not invent 11th |
| R16–R19 | FK `entry.page_id→page.id`; unique `(page_id,row_number)`; no join table |
| R20–R22 | Transcription audits; CLASS-003–004 on entry; retention with evidence |
| R23–R25 | Child→parent; RESTRICT; intake core / entry pkg |

### REL-PAGE-IMAGE-ACTIVE — Page active Source Image

| Field | Value |
| --- | --- |
| R1–R4 | `REL-PAGE-IMAGE-ACTIVE` / PageActiveImage / Page / REFERENCE |
| R5–R6 | Page **1 — 0..1** active Image (required after successful upload path) |
| R7–R9 | LT-PAGE.`source_image_id` **or** LT-IMAGE.`page_id` + active flag (IS-303 picks one); image versions supersede without breaking page |
| R10–R12 | Evidence for transcription; private storage |
| R13–R15 | Page→Image; Image→Page; forbid public URL identity |
| R16–R19 | Logical FK either direction single-owner; versions via REL-IMAGE-VERSION |
| R20–R22 | IMAGE/UPLOAD audits; CLASS-004 keys; evidence retention |
| R23–R25 | Prefer page→image active ref; RESTRICT delete image if active; storage pkg |

### REL-IMAGE-VERSION — Image has Versions

| Field | Value |
| --- | --- |
| R1–R4 | `REL-IMAGE-VERSION` / ImageHasVersions / Source Image / COMPOSITION |
| R5–R6 | Image **1 — \*** Version |
| R7–R9 | LT-IMAGE-VERSION.`image_id`; versions owned by image |
| R10–R12 | Original/display/thumb without losing provenance |
| R13–R15 | Image→Versions; Version→Image |
| R16–R19 | FK child→parent; no N:N |
| R20–R22 | IMAGE domain; CLASS-004; with image retention |
| R23–R25 | Child→parent; RESTRICT/SET policy in IS-303; storage pkg |

### REL-UPLOAD-IMAGE — Upload produces Image

| Field | Value |
| --- | --- |
| R1–R4 | `REL-UPLOAD-IMAGE` / UploadProducesImage / Upload / REFERENCE |
| R5–R6 | Upload **0..1 — 0..1** Image (success path) |
| R7–R9 | LT-UPLOAD may reference resulting image_id; upload does not outrank image as evidence |
| R10–R12 | Track attempt vs durable evidence |
| R13–R15 | Upload→Image; not Image→all uploads required |
| R16–R19 | Optional FK upload→image |
| R20–R22 | UPLOAD audits |
| R23–R25 | Optional FK; RESTRICT; storage pkg |

### REL-PAGE-CLAIM-ACTIVE — Page active Claim

| Field | Value |
| --- | --- |
| R1–R4 | `REL-PAGE-CLAIM-ACTIVE` / PageActiveClaim / Claim / COMPOSITION (of claim aggregate) |
| R5–R6 | Page **1 — 0..1** active Claim per work type |
| R7–R9 | LT-CLAIM owns relationship (`page_id`); claim service sole writer; queue must not write |
| R10–R12 | Exclusive transcription hold; expiry ≠ draft erase |
| R13–R15 | Page→active Claim; Claim→Page; forbid dual active |
| R16–R19 | FK claim→page; partial unique active; no join table |
| R20–R22 | CLAIM audits; CLASS-002 |
| R23–R25 | Child→parent; RESTRICT; claim pkg |

### REL-CLAIM-USER — Claim held by User

| Field | Value |
| --- | --- |
| R1–R4 | `REL-CLAIM-USER` / ClaimHeldByUser / Claim / REFERENCE |
| R5–R6 | Claim **\* — 1** User (required while claim exists) |
| R7–R9 | LT-CLAIM.`claimed_by_user_id`; user does not own claim lifecycle |
| R10–R12 | Actor accountability |
| R13–R15 | Claim→User; User→Claims (admin) |
| R16–R19 | FK claim→user |
| R20–R22 | Actor on CLAIM audits |
| R23–R25 | Child→user; RESTRICT user delete if active claims; auth+claim pkgs |

### REL-QUEUE-PAGE — Queue projects Page

| Field | Value |
| --- | --- |
| R1–R4 | `REL-QUEUE-PAGE` / QueueProjectsPage / Queue projection / PROJECTION |
| R5–R6 | Queue item **1 — 1** Page (logical) |
| R7–R9 | LT-QUEUE derived; **no write ownership** of page/claim |
| R10–R12 | Worklist visibility |
| R13–R15 | Queue→Page read; forbid queue→mutate claim |
| R16–R19 | View/join; not authoritative FK inventing new business |
| R20–R22 | Derived; underlying page/claim audits suffice |
| R23–R25 | Prefer SQL VIEW later; queue read-model pkg |

### REL-QUEUE-CLAIM — Queue overlays Claim

| Field | Value |
| --- | --- |
| R1–R4 | `REL-QUEUE-CLAIM` / QueueOverlaysClaim / Queue / PROJECTION |
| R5–R6 | Queue item **0..1** Claim overlay |
| R7–R9 | Read-only projection of active claim |
| R10–R12 | Show holder/expiry without second claim store |
| R13–R15 | Read only; **forbidden** claim writes via queue |
| R16–R19 | Join/view |
| R20–R22 | None beyond claim |
| R23–R25 | View; queue pkg |

### REL-ENTRY-MATCH-RUN — Entry has Match Runs

| Field | Value |
| --- | --- |
| R1–R4 | `REL-ENTRY-MATCH-RUN` / EntryHasMatchRuns / Match Evaluation / COMPOSITION |
| R5–R6 | Entry **1 — \*** Match Run |
| R7–R9 | LT-MATCH-RUN.`entry_id`; run immutable after complete |
| R10–R12 | Evaluation history; supersede via new run |
| R13–R15 | Entry→Runs; Run→Entry |
| R16–R19 | FK run→entry |
| R20–R22 | MATCHING audits |
| R23–R25 | Child→parent; RESTRICT; matching pkg |

### REL-MATCH-RUN-CANDIDATE — Run contains Candidates

| Field | Value |
| --- | --- |
| R1–R4 | `REL-MATCH-RUN-CANDIDATE` / RunContainsCandidates / Match Evaluation / COMPOSITION |
| R5–R6 | Run **1 — \*** Candidate |
| R7–R9 | LT-MATCH-CANDIDATE.`match_run_id` |
| R10–R12 | Scored possibilities; not resolution |
| R13–R15 | Run→Candidates; Candidate→Run |
| R16–R19 | FK candidate→run |
| R20–R22 | MATCHING |
| R23–R25 | Child→parent; matching pkg |

### REL-CANDIDATE-PERSON — Candidate references Canonical Person

| Field | Value |
| --- | --- |
| R1–R4 | `REL-CANDIDATE-PERSON` / CandidateReferencesPerson / Match Evaluation / EXTERNAL_REF |
| R5–R6 | Candidate **\* — 1** external person id (logical) |
| R7–R9 | LT-MATCH-CANDIDATE stores external id; **no intake ownership** of person |
| R10–R12 | Possible identity link; shared contact ≠ identity alone |
| R13–R15 | Candidate→Person (read via port); forbid candidate write to person master |
| R16–R19 | Logical external ref; physical FK only if shared-DB audit allows |
| R20–R22 | MATCHING; CLASS-003 |
| R23–R25 | Soft ref default; matching pkg + ISSUE-CANONICAL-001 |

### REL-ENTRY-RESOLUTION — Entry has Match Resolution

| Field | Value |
| --- | --- |
| R1–R4 | `REL-ENTRY-RESOLUTION` / EntryHasResolution / Match Resolution / COMPOSITION |
| R5–R6 | Entry **1 — 0..\*** Resolution versions; **0..1 current** |
| R7–R9 | LT-MATCH-RESOLUTION.`entry_id`; resolution does **not** write persons |
| R10–R12 | Final match outcome; Match ≠ Promotion |
| R13–R15 | Entry→Resolution; Resolution→Entry; forbid resolution→mutate person |
| R16–R19 | FK resolution→entry |
| R20–R22 | RESOLUTION domain |
| R23–R25 | Child→parent; resolution pkg |

### REL-RESOLUTION-PROMOTION — Resolution drives Promotion

| Field | Value |
| --- | --- |
| R1–R4 | `REL-RESOLUTION-PROMOTION` / ResolutionDrivesPromotion / Promotion / REFERENCE |
| R5–R6 | Resolution **1 — 0..\*** Promotion requests (policy-bound; typically 0..1 active) |
| R7–R9 | LT-PROMOTION.`resolution_id`; promotion independently stateful |
| R10–R12 | Business acceptance after identity decision; neither owns the other |
| R13–R15 | Resolution→Promotions; Promotion→Resolution; forbid promotion rewriting outcome |
| R16–R19 | FK promotion→resolution (+ entry_id denorm optional for integrity checks) |
| R20–R22 | PROMOTION audits |
| R23–R25 | Child→resolution; RESTRICT; promotion pkg |

### REL-PROMOTION-ENTRY — Promotion subjects Entry

| Field | Value |
| --- | --- |
| R1–R4 | `REL-PROMOTION-ENTRY` / PromotionSubjectsEntry / Promotion / REFERENCE |
| R5–R6 | Promotion **\* — 1** Entry |
| R7–R9 | LT-PROMOTION.`entry_id` |
| R10–R12 | Subject of create/link request |
| R13–R15 | Promotion→Entry |
| R16–R19 | FK promotion→entry |
| R20–R22 | PROMOTION |
| R23–R25 | Child→entry; promotion pkg |

### REL-PROMOTION-RESULT — Promotion has Results

| Field | Value |
| --- | --- |
| R1–R4 | `REL-PROMOTION-RESULT` / PromotionHasResults / Promotion / COMPOSITION |
| R5–R6 | Promotion **1 — \*** Result rows (append preferred) |
| R7–R9 | LT-PROMOTION-RESULT.`promotion_id` |
| R10–R12 | Durable attempt outcomes |
| R13–R15 | Promotion→Results |
| R16–R19 | FK result→promotion |
| R20–R22 | PROMOTION |
| R23–R25 | Child→parent; promotion pkg |

### REL-PROMOTION-PERSON — Promotion results in Canonical Person link

| Field | Value |
| --- | --- |
| R1–R4 | `REL-PROMOTION-PERSON` / PromotionLinksPerson / Promotion / EXTERNAL_REF |
| R5–R6 | Promotion success **0..1** external person |
| R7–R9 | Result/person id on promotion tables; person master EXTERNAL |
| R10–R12 | Only intake path requesting create/link |
| R13–R15 | Promotion→Person via port; forbid matching modules writing this |
| R16–R19 | External ref; physical FK TBD ISSUE-CANONICAL-001 |
| R20–R22 | CANONICAL_INTEGRATION |
| R23–R25 | Soft ref default; promotion pkg |

### REL-ENTRY-CORRECTION — Entry has Corrections

| Field | Value |
| --- | --- |
| R1–R4 | `REL-ENTRY-CORRECTION` / EntryHasCorrections / Entry / COMPOSITION |
| R5–R6 | Entry **1 — \*** Correction |
| R7–R9 | LT-ENTRY-CORRECTION.`entry_id` |
| R10–R12 | Preserve prior values on CORRECTED |
| R13–R15 | Entry→Corrections |
| R16–R19 | FK correction→entry; append-only preferred |
| R20–R22 | Transcription correction audits |
| R23–R25 | Child→parent; entry pkg |

### REL-ENTRY-PERSON-LINK — Entry linked Canonical Person (post-promotion)

| Field | Value |
| --- | --- |
| R1–R4 | `REL-ENTRY-PERSON-LINK` / EntryLinkedPerson / Entry / EXTERNAL_REF |
| R5–R6 | Entry **0..1** linked person after success |
| R7–R9 | LT-ENTRY.`linked_canonical_person_id` set **only** via promotion success |
| R10–R12 | Distinct from candidate refs and resolution selected id |
| R13–R15 | Entry→Person read; forbid match resolution setting this alone |
| R16–R19 | External ref |
| R20–R22 | Promotion success audit |
| R23–R25 | Soft ref; promotion pkg |

### REL-USER-ROLE — User has Role Grants

| Field | Value |
| --- | --- |
| R1–R4 | `REL-USER-ROLE` / UserHasRoleGrants / User / COMPOSITION |
| R5–R6 | User **1 — \*** Role Grant |
| R7–R9 | LT-ROLE-GRANT.`user_id` |
| R10–R12 | Authorization grants (Cat 5 roles) |
| R13–R15 | User→Grants |
| R16–R19 | FK grant→user |
| R20–R22 | ROLE_MANAGEMENT |
| R23–R25 | Child→parent; authz pkg |

### REL-AUDIT-CORRELATION — Audit correlates entities

| Field | Value |
| --- | --- |
| R1–R4 | `REL-AUDIT-CORRELATION` / AuditCorrelatesEntities / Audit / CORRELATION |
| R5–R6 | Audit **\* — 0..\*** Batch/Page/Entry/Claim/Promotion (via payload/ids) |
| R7–R9 | LT-AUDIT non-owning; append-only |
| R10–R12 | Forensic linkage without FK spaghetti required |
| R13–R15 | Audit→subjects read; subjects do not own audit rows |
| R16–R19 | Logical correlation IDs; optional FKs discouraged for append perf |
| R20–R22 | Self; sensitivity by payload class |
| R23–R25 | No cascade from business delete into rewriting history; audit pkg |

### REL-ERROR-SUBJECT — Error references subject

| Field | Value |
| --- | --- |
| R1–R4 | `REL-ERROR-SUBJECT` / ErrorReferencesSubject / Ops / REFERENCE |
| R5–R6 | Error **\* — 0..1** Page/Entry/etc. |
| R7–R9 | LT-ERROR optional subject ids |
| R10–R12 | Operator remediation context |
| R13–R15 | Error→subject |
| R16–R19 | Optional FKs or soft refs |
| R20–R22 | Ops audits |
| R23–R25 | Soft ref preferred; ops pkg |

---

## 8. Relationship index

```text
REL-BATCH-PAGE
REL-PAGE-ENTRY
REL-PAGE-IMAGE-ACTIVE
REL-IMAGE-VERSION
REL-UPLOAD-IMAGE
REL-PAGE-CLAIM-ACTIVE
REL-CLAIM-USER
REL-QUEUE-PAGE
REL-QUEUE-CLAIM
REL-ENTRY-MATCH-RUN
REL-MATCH-RUN-CANDIDATE
REL-CANDIDATE-PERSON
REL-ENTRY-RESOLUTION
REL-RESOLUTION-PROMOTION
REL-PROMOTION-ENTRY
REL-PROMOTION-RESULT
REL-PROMOTION-PERSON
REL-ENTRY-CORRECTION
REL-ENTRY-PERSON-LINK
REL-USER-ROLE
REL-AUDIT-CORRELATION
REL-ERROR-SUBJECT
```

## 9. Acceptance Criteria

| ID | Criterion | Met? |
| --- | --- | --- |
| AC-REL-001 | Questionnaire defined | Yes |
| AC-REL-002 | Core hierarchy + match/promotion topology carded | Yes |
| AC-REL-003 | Match≠Promotion and EXTERNAL_REF rules locked | Yes |
| AC-REL-004 | Queue projection non-write locked | Yes |
| AC-REL-005 | Doctrine: no physical FK invents business relationship | Yes |
| AC-REL-006 | No SQL/Prisma/migrations created | Yes |

## 10. Open Decisions

| ID | Notes |
| --- | --- |
| Page↔Image FK ownership side | IS-303 |
| Physical FK to canonical | ISSUE-CANONICAL-001 / ISSUE-DBA-001 |
| Queue as VIEW vs table | IS-303/304 |
| Exact cascade matrix | IS-303 |

## 11. Risks

| ID | Risk | Mitigation |
| --- | --- | --- |
| RISK-REL-001 | ORM convenience relations invent links | REQ-REL-001/002 |
| RISK-REL-002 | Resolution FK to person master | REQ-REL-003 |
| RISK-REL-003 | Queue mutates claims | REQ-REL-004 |

## 12. Dependencies

IS-301; IS-200; Catalog 01 for stateful sides.

## 13. Traceability

REL-* ↔ LT-* ↔ ENT-* — FULLY_MAPPED (logical). Physical FK DDL → IS-303+ / migration packages.

## 14. Implementation Boundary

**Authorized:** this topology; governance; audit verification.  
**Forbidden:** executable FK/ORM schema artifacts.

## 15. Revision History

| Version | Date | Change | Approval |
| --- | --- | --- | --- |
| 1.0 | 2026-07-26 | Logical relationship topology | D-074 |

## Next primary

```text
PEOPLE-IS-303-LOGICAL-CONSTRAINTS-AND-INTEGRITY-1.0
```

## Independent lane

```text
PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0
```

## Final status

```text
PEOPLE-IS-302 LOGICAL RELATIONSHIP SPECIFICATIONS: APPROVED (DOCUMENTATION)
RELATIONSHIPS = GOVERNED BUSINESS CONCEPTS
PHYSICAL FK MUST NOT INVENT BUSINESS RELATIONSHIPS
SQL / PRISMA / MIGRATIONS: NOT AUTHORIZED
```
