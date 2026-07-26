# PEOPLE-IS-200 — DOMAIN MODEL

**Title:** Domain Model  
**Document ID:** `PEOPLE-IS-200-DOMAIN-MODEL-1.0`  
**Version:** 1.0  
**Status:** APPROVED  
**Phase:** PHASE 2 — DOMAIN AND DATA MODEL  
**Project Root:** `H:\people`  
**Owner:** People Intake System Program  
**Approval Authority:** Decision Log D-069  
**Created Date:** 2026-07-26  
**Last Updated:** 2026-07-26  
**Governing Documents:** Constitution Art. XIV; Glossary; IS-000; IS-102; Catalogs 0–9 (esp. Catalog 01); Volumes 8–9 (domain/DB conceptual); `docs/04_data/PEOPLE_INTAKE_DOMAIN_MODEL.md` (elevated foundation)  
**Dependencies:** Phase 1 platform COMPLETE (IS-100…105); Catalog Library 0–9 foundation complete  
**Implementation Authorization:** `IMPLEMENTATION NOT AUTHORIZED`

```text
DESIGN COMPLETE
APPROVED FOR DOCUMENTATION GOVERNANCE
BUSINESS ARCHITECTURE AUTHORITY FOR PHASE 2
APPLICATION IMPLEMENTATION NOT AUTHORIZED
PHYSICAL SCHEMA NOT FINALIZED (IS-300+)
```

**Companion foundations (still valid, subordinate to this IS for engineering packages):**

* `docs/04_data/PEOPLE_INTAKE_DOMAIN_MODEL.md`  
* `docs/00_governance/PEOPLE_INTAKE_GLOSSARY.md`  
* Constitution Article XIV  
* `docs/implementation_specs/100_platform/PEOPLE-IS-102-MODULE-BOUNDARY-SPECIFICATION.md`  
* Catalog 01 state machines  

---

## 1. Purpose

Establish the canonical business architecture for People Intake so that every future API, table, UI, workflow, job, and integration can answer **“Which domain concept owns this?”** before any code is written.

This specification answers Phase 2’s central question:

```text
What is the system?
```

Phase 1 answered how the system is built (repository, technology posture, modules, environments, workspace, GitHub/Netlify). Phase 2 begins with the business itself.

## 2. Scope

Canonical business vocabulary and ubiquitous language; core aggregates; entities; value objects; identity rules; ownership rules; lifecycle/state model references; invariants; relationships; aggregate boundaries; domain services; domain events (conceptual); business policies; extensibility rules; traceability to requirements and catalogs; explicit open issues that block implementation readiness (not documentation approval).

## 3. Out of Scope

* Physical database DDL / migrations (IS-300+)  
* API endpoint inventories (Phase 5)  
* UI component trees (Phase 6)  
* Accepting open ADRs or inventing Catalog keys  
* Resolving ISSUE-CANONICAL-001 full DTO surface (recorded; not invented here)  
* Application implementation  

## 4. Governing References

| Authority | Role |
| --- | --- |
| Constitution Art. XIV + Glossary | Ubiquitous language |
| Decision Log D-029…D-032, D-018, etc. | Locked product decisions |
| Catalog 01 | Production state/transition authority |
| Catalogs 2–8 | Errors, audit names, config, permissions, notifications, jobs, retention |
| Catalog 09 | Traceability discipline |
| IS-102 + ownership matrix | Capability module ownership |
| Volume 8 / `docs/04_data/*` | Conceptual domain depth (reconcile to catalogs) |

**Conflict rule:** Catalog production keys and accepted Decision Log entries win over conceptual draft labels in workflow/field docs. Do not silently equate non-catalog status strings with Catalog 01 states.

## 5. Definitions (ubiquitous language)

Use these terms consistently in specs, APIs, UI copy, jobs, and code names. Expanded prose: Glossary. Standing short forms: Constitution Art. XIV.

| Term | Meaning |
| --- | --- |
| **Batch** | Collection of photographed pages uploaded together with shared source context; contains pages, not canonical people |
| **Page** | One volunteer sheet image work item; primary queue unit; claim unit; parent of 0–10 entries |
| **Intake Entry (Entry)** | One handwritten person line; unique identity among siblings on the same page |
| **Claim** | Atomic exclusive lock for authorized work on a page |
| **Queue** | Shared multi-user work list of pages across lifecycle stages |
| **Draft** | In-progress transcription persistence before immutable submit revision |
| **Raw Value** | Exactly what the operator transcribed |
| **Normalized Value** | Safe comparison form; never silently replaces raw |
| **Field Condition** | Evidence quality of a field: `PROVIDED` \| `NOT_PROVIDED` \| `UNREADABLE` \| `AMBIGUOUS` \| `CORRECTED` (D-030) |
| **Source Image** | Private original photograph/scan linked to a page (+ optional derivatives) |
| **Match Candidate** | Scored possible link between an entry and a canonical person |
| **Match Resolution** | Final determination for an entry’s match outcome |
| **Promotion** | Controlled create/link of canonical person data from an intake entry with provenance |
| **Canonical Person** | Shared durable identity outside intake ownership; not the raw entry |
| **Person Attribute** | Canonical fact with provenance/history (not silent flat overwrite) |
| **Provenance** | Trail from value/decision to batch, page, entry, image, actors, timestamps |
| **Audit Event** | Append-only meaningful action (Catalog 3 names) |
| **UNKNOWN** | Paper did not clearly indicate Yes/No; never silently treated as NO |
| **Unreadable** | Writing appears present but cannot be read confidently |

### Synonym discipline

| Prefer | Avoid as synonym for |
| --- | --- |
| Page | “Sheet record” as a second entity |
| Intake Entry | “Person” (reserved for Canonical Person) |
| Promotion | “Merge” (merges are outside routine intake) |
| Claim | “Lock” without claim semantics |
| Canonical Person | “Contact” / “Volunteer” as identity root |

## 6. Assumptions

* Catalog Library 0–9 foundations are complete; inventories expand by amendment only.  
* IS-102 module ownership remains the capability ownership rulebook.  
* Matching is post-transcription, conservative, explainable (D-031).  
* Controlled promotion Model B is locked (D-032 / domain model).  
* Gate G-10 remains closed.  

## 7. Functional Requirements

| ID | Description |
| --- | --- |
| REQ-DOM-001 | The domain MUST preserve distinguishable data layers: Source Evidence, Raw Transcription, Normalized Intake Value, Canonical Person Value, Match Decision, Accepted Person Update, Rejected Person Update. |
| REQ-DOM-002 | Batch, Page, Intake Entry, and Canonical Person MUST remain separate concepts (D-029). |
| REQ-DOM-003 | A Page MUST be the primary queue work item and MAY contain 0–10 uniquely identified Entries. |
| REQ-DOM-004 | Every persistent business concept in scope MUST have exactly one owning capability module (IS-102). |
| REQ-DOM-005 | Aggregate boundaries MUST define consistency and transaction intent; consumers MUST NOT mutate foreign aggregates. |
| REQ-DOM-006 | Production lifecycle states/transitions MUST come from Catalog 01; undocumented states are forbidden. |
| REQ-DOM-007 | Identity rules MUST ensure Entries have unique IDs independent of row number; row number is positional metadata (1–10). |
| REQ-DOM-008 | Raw and normalized values MUST both be retained where normalization applies (D-030). |
| REQ-DOM-009 | Field conditions MUST be recordable per field using the locked condition set. |
| REQ-DOM-010 | UNKNOWN consent/preference MUST NEVER silently become NO. |
| REQ-DOM-011 | Match Resolution MUST be distinct from Promotion (Volume 8 locks). |
| REQ-DOM-012 | Promotion MUST be independently stateful and idempotent at the request boundary. |
| REQ-DOM-013 | People Intake MUST NOT write RedDirt operational entities (missions, tasks, campaign calendars, etc.). |
| REQ-DOM-014 | Canonical Person identity/attributes live outside intake ownership; intake interacts only via controlled promotion ports. |
| REQ-DOM-015 | Claim expiration MUST NOT erase recoverable drafts (Catalog 01 / claim rules). |
| REQ-DOM-016 | Submission MUST create an immutable transcription revision (correction via formal history only). |
| REQ-DOM-017 | Shared household/contact signals alone MUST NOT establish identity (D-031). |
| REQ-DOM-018 | Blank rows MUST NOT fabricate Entries. |
| REQ-DOM-019 | Every future implementation package MUST cite the owning aggregate/entity before coding. |
| REQ-DOM-020 | Conceptual draft status labels in older workflow docs MUST be reconciled to Catalog 01 before use as production enums. |

## 8. Nonfunctional Requirements

| ID | Description |
| --- | --- |
| NFR-DOM-AUDIT-001 | Meaningful state changes and promotions are auditable (Catalog 3). |
| NFR-DOM-TRACE-001 | Domain concepts map to requirements/modules/catalogs without invented keys. |
| NFR-DOM-EXT-001 | New concepts require Decision Log / catalog amendment — not silent schema growth. |
| NFR-DOM-HONEST-001 | Specs MUST NOT invent full production inventories beyond seeded foundations. |

## 9. Architecture — Business Domain

### 9.1 Bounded context

```text
People Intake (this system)
  owns intake capture → transcription → matching → promotion requests
  does NOT own canonical person master data
  does NOT own RedDirt operational planning/execution domains
```

Anti-corruption: promotion and canonical ports isolate shared-person semantics (ADR-016 OPEN for packaging depth; ISSUE-CANONICAL-001 OPEN).

### 9.2 Core hierarchy

```text
Intake Batch
  └── Intake Page
        ├── Source Image (private)
        ├── Page Claim (when claimed)
        └── Intake Entry [0..10]
              ├── Draft / Submitted revision
              ├── Field values (raw + normalized + conditions)
              ├── Match Evaluation / Candidates
              ├── Match Resolution
              └── Promotion Request → Canonical Person (external)
```

### 9.3 Data layer separation (locked)

| Layer | Must preserve |
| --- | --- |
| Source Evidence | Image, upload metadata, batch context, hashes |
| Raw Transcription | Operator-entered values at submit |
| Normalized Intake Value | Safe machine forms for compare/ops |
| Match Decision | Candidates, scores, resolution |
| Canonical Person Value | Shared domain via promotion |
| Accepted / Rejected Person Update | Promotion outcomes with provenance |

Collapsing these layers is a domain defect.

### 9.4 Aggregate catalog

| Aggregate root | Contained / closely held | Consistency intent | Owner module |
| --- | --- | --- | --- |
| **Batch** | Batch metadata; page membership references; batch lifecycle | Batch open/complete/archive coherence | `MOD-BATCHES` |
| **Page** | Page metadata/order; active image ref; completion when entries resolve | Page lifecycle vs queue visibility | `MOD-PAGES` |
| **Source Image / Upload** | Storage object refs; upload session | Upload/verify/quarantine | `MOD-UPLOADS` |
| **Claim** | Active exclusive hold | One active claim per work item/type | `MOD-CLAIMS` |
| **Entry (Draft→Submitted)** | Row identity; raw/normalized fields; conditions; draft/submit revisions | Draft save vs immutable submit | `MOD-DRAFTS` / `MOD-TRANSCRIPTIONS` (**ISSUE-MOD-001**) |
| **Match Evaluation** | Candidate set for an entry run | Immutable after completion | `MOD-MATCHING` |
| **Match Resolution** | Final decision + versioning | Distinct from promotion | `MOD-RESOLUTION` |
| **Promotion Request** | Request + result linkage | Idempotent; durable before async call | `MOD-PROMOTION` |
| **User / Role Grant** | Access identity | Not intake hierarchy | `MOD-USERS` / `MOD-ROLES` |
| **Canonical Person** | **Outside** intake | Via INT ports only | External + `MOD-LAYER-INT` |

**Queue** is a projection/worklist concern (`MOD-QUEUES`) — it MUST NOT own claim writes.

### 9.5 Entity catalog (conceptual)

| Entity | Identity | Notes |
| --- | --- | --- |
| Intake Batch | Batch ID | Shared source context; not people |
| Intake Page | Page ID | Queue work item |
| Intake Entry | Entry ID | Row 1–10 positional; ID is authority |
| Source Image | Image ID | Private object storage refs |
| Upload Session | Upload ID | Upload lifecycle (Catalog 01) |
| Page Claim | Claim ID | Exclusive hold |
| Draft | Draft ID / entry-scoped | Survives claim expiry when recoverable |
| Match Candidate | Candidate ID | Entry ↔ possible person |
| Match Resolution | Resolution ID | Outcome enum below |
| Promotion Request | Promotion ID | Independently stateful |
| Application User | User ID | Access domain |
| Audit Event | Event ID | Append-only; Catalog 3 names |
| Processing Error / Alert | Error/Alert ID | Operator lifecycles (Catalog 01) |

Seeded table names (not physical finality): `intake_batches`, `intake_pages`, `intake_entries`, `intake_source_images`, `intake_page_claims`, `intake_match_candidates`, `intake_match_resolutions`, `intake_promotion_requests`, `intake_audit_events`, `app_users` — finalize in IS-300+.

### 9.6 Value objects (representative)

| Value object | Rule |
| --- | --- |
| RowNumber | Integer 1–10; unique per page among existing entries |
| RawFieldValue | Opaque transcribed string; preserved |
| NormalizedFieldValue | Deterministic normalize; never invent meaning |
| FieldCondition | Locked enum set (D-030) |
| ConfidenceTier / MatchScore | Explainable; policy-bound |
| Email / Phone normalized forms | Digits/lowercase rules in matching/normalization specs — raw retained |
| ContentHash | Image/integrity evidence |
| ProvenanceRef | Links to batch/page/entry/image/actors/time |

### 9.7 Identity rules

1. **Entry ID** is the durable identity of a person-line; never reuse IDs.  
2. **Row number** may change only under explicit correction rules (future entity IS); it is not global identity.  
3. **Canonical Person ID** is minted/owned outside intake; intake stores linkage only after successful promotion.  
4. **Blank sheet rows** produce no Entry.  
5. **Page completion** requires all existing Entries to reach terminal resolution paths per Catalog 01 / workflow rules — not “10 entries always.”  

### 9.8 Ownership rules

| Owns | Does not own / must not write |
| --- | --- |
| Intake: batches, pages, entries, images, claims, candidates, resolutions, promotion requests/results, intake audit, processing errors | Canonical master person/attributes/merges; RedDirt missions/tasks/events/email campaigns/assignments |

Module ownership: IS-102 matrix. Dual unrestricted writers on `intake_entries` forbidden (ISSUE-MOD-001 interim: single-writer-per-state).

### 9.9 Lifecycle / state models

Authority: **Catalog 01**. Domain packages cite machine IDs; they do not redefine enums.

| Concern | Machine (examples) |
| --- | --- |
| Batch | `STATE-BATCH-001` |
| Page | `STATE-PAGE-001` |
| Upload / Storage / Image quality | `STATE-UPLOAD-001`, `STATE-STORAGE-001`, `STATE-IMAGE-QUALITY-001` |
| Queue / Claim / Draft | `STATE-QUEUE-001`, `STATE-CLAIM-001`, `STATE-DRAFT-001` |
| Entry | `STATE-ENTRY-001` |
| Normalization / Match eval / Resolution | `STATE-NORMALIZATION-001`, `STATE-MATCH-EVAL-001`, `STATE-MATCH-RESOLUTION-001` |
| Promotion / Canonical link | `STATE-PROMOTION-001`, `STATE-CANONICAL-LINK-001` |
| Cross-cutting | jobs, errors, alerts, notifications, exports, archival machines |

Deferred Catalog decisions (`STATE-DEC-*`) may affect whether some statuses are persisted vs derived — record in open decisions; do not invent.

### 9.10 Invariants

1. Layers in §9.3 remain distinguishable.  
2. Page has at most one **active** claim of a given work type.  
3. Match evaluation results are immutable after completion; supersede via new run.  
4. Resolution outcome does not itself mutate canonical persons.  
5. Promotion is the only intake path that requests canonical create/link.  
6. UNKNOWN ≠ NO.  
7. Unreadable/ambiguous fields do not become fabricated certainty.  
8. Household/shared contact alone ≠ identity.  
9. No undocumented Catalog states/errors/permissions/audit/job names in production behavior.  
10. Consumers never bypass owning module to write foreign aggregates.

### 9.11 Relationships

```text
Batch 1—* Page
Page 1—0..1 active Source Image (versions may supersede)
Page 1—* Entry (0..10)
Page 1—0..1 active Claim (per type)
Entry 1—* Match Candidate (per evaluation)
Entry 1—0..1 current Match Resolution (versioned history allowed)
Match Resolution 0..1—* Promotion Request (policy-bound)
Promotion Request → Canonical Person (external success path)
Entry / Page / Batch → Audit Events (append-only)
```

### 9.12 Match resolution outcomes (locked vocabulary)

| Outcome | Meaning |
| --- | --- |
| `LINK_EXISTING` | Link entry to an existing canonical person via promotion |
| `CREATE_NEW` | Create new canonical person via promotion |
| `DEFER` | Delay decision |
| `RETURN_FOR_CORRECTION` | Send back for transcription/correction |
| `NO_ACTION` | Explicit non-action terminal for the match step |

### 9.13 Domain services (conceptual)

| Service | Responsibility | Notes |
| --- | --- | --- |
| Normalization | Raw → normalized without semantic invention | `MOD-NORMALIZATION` |
| Matching evaluation | Produce candidates + explanations | `MOD-MATCHING`; conservative |
| Claim management | Acquire/renew/release/expire | `MOD-CLAIMS` |
| Promotion orchestration | Build idempotent promotion requests; call canonical port | `MOD-PROMOTION` + INT |
| Retention orchestration | Apply Catalog 8 classes | `MOD-RETENTION` |

Domain services enforce invariants; they are not UI controllers.

### 9.14 Domain events (conceptual)

Events are design-level signals for future audit/job/notification wiring. **Names MUST map to Catalog 3** (or amendment) before production. Examples of **concepts** (not new catalog invents):

* BatchOpened / BatchCompleted  
* PageQueued / PageClaimed / PageSubmitted  
* EntrySubmitted / EntryMatchResolved  
* PromotionRequested / PromotionSucceeded / PromotionFailed  
* ClaimExpired / DraftRecovered  

Implementation packages bind these to Catalog 3 event names — never invent production event strings here.

### 9.15 Business policies (locked / standing)

| Policy | Source |
| --- | --- |
| Preserve what was written; record what was typed; normalize what is safe; never hide how a person was created/changed | Domain governing principle |
| Controlled promotion (Model B) | D-032 / domain model |
| Matching after transcription; explainable; no auto-uncertain-merge | D-031 |
| Raw vs normalized preserved; field conditions; UNKNOWN≠NO | D-030 |
| Separate Batch/Page/Entry/Canonical Person | D-029 |
| Private object storage for images | D-032 / storage posture |
| Match Resolution ≠ Promotion | Volume 8 |
| Design docs precede code; Gate G-10 closed until authorized | Constitution / active-build |

### 9.16 Future extensibility

Allowed only via Decision Log and/or catalog amendment:

* New aggregates/entities  
* New resolution outcomes  
* New field condition values  
* New state machines/states  
* Expanding beyond Version 1 non-goals (OCR-as-authority, public forms, etc.)

In-repo package/workspace growth does not by itself create new domain concepts.

### 9.17 Placement algorithm (for Burt / packages)

Before implementing any feature:

```text
1. Name the business concept in ubiquitous language (§5).
2. Identify aggregate root (§9.4).
3. Identify owning module (IS-102 matrix).
4. Identify Catalog 01 machine(s) if stateful.
5. Identify Catalog 2/3/5/6/7/8 keys if applicable — or stop for amendment.
6. Confirm invariants (§9.10) still hold.
7. Only then design API/UI/job/table changes in later IS/PKG docs.
```

If step 1–5 cannot be answered, **stop** — do not code.

## 10. Data Contracts

Conceptual only. Physical columns → IS-201 entity specs + IS-300 database. Field dictionary remains a conceptual companion until reconciled.

Required distinguishable fields conceptually: raw, normalized, condition, provenance refs, identity keys listed in §9.5–9.7.

## 11. Interface Contracts

| Port | Direction | Rule |
| --- | --- | --- |
| Canonical Person Service | Outbound from promotion | Create/link/add/retire/reject with provenance; intake does not own person rows |
| Object storage | Outbound from uploads | Private; not public CDN identity |
| RedDirt operational APIs | Generally forbidden writes | Additive least-privilege reads only if Decision Log authorizes |

Exact DTOs: ISSUE-CANONICAL-001 / ADR-016 — **not invented here**.

## 12. State Behavior

See §9.9. Server-enforced transitions (Catalog 01). Client cannot invent states.

## 13. Permission Behavior

Authorization keys = Catalog 5. Domain model does not invent permission strings. Capability modules enforce checks at application boundary (IS-102).

## 14. Error and Recovery Behavior

Error codes = Catalog 2. Domain failures (invariant violation, illegal transition, blank-row fabrication attempt) fail closed. Claim expiry recovers queue availability without destroying recoverable drafts.

## 15. Audit Requirements

Meaningful domain actions emit Catalog 3 events via `MOD-AUDIT`. Promotion and resolution changes are high-sensitivity audit targets.

## 16. Notification Requirements

Catalog 6 names only when product notifications are specified. Domain does not invent notification types.

## 17. Background Processing

Catalog 7 job names for match/promotion/retention/upload verification etc. Domain defines **what** must remain true after jobs; job runtime is ADR-006.

## 18. Security and Privacy

* Source images private  
* No Production PII in Git  
* Canonical merges outside routine intake  
* Least privilege across bounded contexts  

## 19. Data Classification and Retention

Catalog 8 classes apply to domain artifacts (images, entries, audit, exports). Exact durations: ISSUE-RETENTION-001.

## 20. Observability

Correlate by Batch/Page/Entry/Promotion IDs. No secrets in logs. Environment labels per IS-103.

## 21. Testing (future packages)

* Invariant tests (UNKNOWN≠NO; layer separation; claim exclusivity)  
* Illegal transition rejection  
* Blank row → no Entry  
* Resolution does not write canonical person  
* Promotion idempotency at request boundary  
* Module ownership boundary tests (IS-102)  

## 22. Acceptance Criteria

| ID | Criterion | Met? |
| --- | --- | --- |
| AC-DOM-001 | Ubiquitous language locked and conflict rule stated | Yes |
| AC-DOM-002 | Aggregates, entities, value objects cataloged | Yes |
| AC-DOM-003 | Identity, ownership, invariants documented | Yes |
| AC-DOM-004 | Catalog 01 cited as state authority | Yes |
| AC-DOM-005 | Match Resolution ≠ Promotion enforced in model | Yes |
| AC-DOM-006 | Canonical/RedDirt write boundaries stated | Yes |
| AC-DOM-007 | Placement algorithm for future packages defined | Yes |
| AC-DOM-008 | Open issues that block impl readiness listed honestly | Yes |
| AC-DOM-009 | No application/schema code created | Yes |

## 23. Open Decisions

| ID | Impact on domain | Status |
| --- | --- | --- |
| ISSUE-MOD-001 | Draft vs transcription writer split on `intake_entries` | OPEN — blocking before entry implementation packages |
| ISSUE-CANONICAL-001 | Exact canonical promotion DTO/port | OPEN — blocking before promotion implementation |
| ISSUE-MOD-002 | Reports/exports read models | OPEN — blocking before reports packages |
| ADR-016 | Anti-corruption packaging | OPEN / PROPOSED |
| STATE-DEC-* | Persisted vs derived statuses; claim duration; review granularity | OPEN in Catalog 01 |
| ISSUE-RETENTION-001 | Exact retention durations | OPEN — launch-level |

Documentation approval of IS-200 does **not** close these issues.

## 24. Risks

| ID | Risk | Mitigation |
| --- | --- | --- |
| RISK-DOM-001 | Treating Entry as Canonical Person | Ubiquitous language + D-029 |
| RISK-DOM-002 | Collapsing raw/normalized/canonical layers | REQ-DOM-001 |
| RISK-DOM-003 | Using draft workflow labels as Catalog 01 enums | REQ-DOM-020; audit lane |
| RISK-DOM-004 | Matching writing canonical rows | REQ-DOM-011/014 |
| RISK-DOM-005 | Dual writers on entries | ISSUE-MOD-001; IS-102 |
| RISK-DOM-006 | Inventing catalog keys to “finish” matrices | Honesty rule; Catalog 09 |

## 25. Dependencies

Phase 1 platform; Catalogs 0–9; IS-102; Glossary/Constitution; parallel audit/freeze lane (independent).

## 26. Traceability

| Requirement | Maps to | Status |
| --- | --- | --- |
| REQ-DOM-001…020 | D-029…032; Catalog 01; IS-102; Constitution | FULLY_MAPPED (design) |
| Entity physical columns | IS-201 / IS-300 | PARTIALLY_MAPPED |
| Canonical DTOs | ISSUE-CANONICAL-001 | PARTIALLY_MAPPED |

## 27. Implementation Boundary

**Authorized:** this specification; indexes/registers/RTM/reports; domain folder under `200_domain/`.  
**Forbidden:** migrations, Prisma models as runtime app, `src/` entities, inventing Catalog keys, claiming ISSUE-MOD-001/CANONICAL-001 resolved without Decision Log.

## 28. Revision History

| Version | Date | Change | Approval |
| --- | --- | --- | --- |
| 1.0 | 2026-07-26 | Phase 2 domain model authority elevated from foundations | D-069 |

## Next (primary sequence)

```text
PEOPLE-IS-201-ENTITY-SPECIFICATIONS-1.0
```

## Independent parallel lane (not sequenced behind IS-201)

```text
PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0
```

## Final status

```text
PEOPLE-IS-200 DOMAIN MODEL: APPROVED (DOCUMENTATION)
PHASE 2 BUSINESS ARCHITECTURE: STARTED
APPLICATION IMPLEMENTATION: NOT AUTHORIZED
```
