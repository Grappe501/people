# PEOPLE-IS-202 — FIELD AND VALUE OBJECT SPECIFICATIONS

**Title:** Field and Value Object Specifications  
**Document ID:** `PEOPLE-IS-202-FIELD-AND-VALUE-OBJECT-SPECIFICATIONS-1.0`  
**Version:** 1.0  
**Status:** APPROVED  
**Phase:** PHASE 2 — DOMAIN AND DATA MODEL  
**Project Root:** `H:\people`  
**Owner:** People Intake System Program  
**Approval Authority:** Decision Log D-071  
**Created Date:** 2026-07-26  
**Last Updated:** 2026-07-26  
**Governing Documents:** IS-200; IS-201; Catalogs 01, 04, 08; D-029…032; field dictionary (subordinate)  
**Dependencies:** PEOPLE-IS-201 APPROVED (D-070)  
**Implementation Authorization:** `IMPLEMENTATION NOT AUTHORIZED`

```text
DESIGN COMPLETE
APPROVED FOR DOCUMENTATION GOVERNANCE
CANONICAL FIELD / VALUE-OBJECT DICTIONARY
CATALOG 01 = SOLE BUSINESS-STATE AUTHORITY (NOT THIS DOC)
APPLICATION IMPLEMENTATION NOT AUTHORIZED
PHYSICAL COLUMN NAMES FINALIZE IN IS-300+
```

**Subordinate companion:** `docs/04_data/PEOPLE_INTAKE_FIELD_DICTIONARY.md` — historical conceptual draft; **IS-202 wins** for field definitions. Conceptual status strings in that file are **not** Catalog 01 enums (ISSUE-AUDIT-001).

---

## 1. Purpose

Define the atomic building blocks of the domain: every allowed field and value object, so that information inside entities has a **single authoritative definition**.

```text
IS-200  What is the system? (domain)
IS-201  What entities exist?
IS-202  What information may exist inside those entities?
```

## 2. Scope

Value-object catalog; field admission questionnaire; field cards for core intake entities; nullability/defaults/validation; ownership; sensitivity (Catalog 08 classes); audit/search notes; field-level extension doctrine; honesty rules for states.

## 3. Out of Scope

* Physical SQL types / indexes DDL (IS-300+)  
* Inventing Catalog 01 states as “fields”  
* Resolving ISSUE-MOD-001 storage shape by invention  
* Application code  

## 4. Standing doctrine (locked)

### 4.1 State fields

Any field representing **business lifecycle state** MUST reference a **Catalog 01** machine/enum. This document does **not** redefine those enums. UX/workflow draft labels are superseded for production.

### 4.2 Field extension decision tree

```text
New feature?
  → Existing Entity? (IS-201)
      → Existing Field? (this IS)
          YES → Reuse
          NO  → Existing Value Object?
                  YES → Reuse VO on entity (amend card)
                  NO  → Update IS-202 or create ADR
                        → Only then may packages reference the new field
```

### 4.3 One concept, one definition

The same business fact (e.g. raw email, field condition, YES/NO/UNKNOWN preference) MUST NOT be reinvented with divergent names/types across modules.

## 5. Mandatory field questionnaire

Every admitted field MUST answer:

| # | Question |
| --- | --- |
| F1 | Canonical name |
| F2 | Business meaning |
| F3 | Data type (logical) |
| F4 | Value object or primitive |
| F5 | Allowed values / constraints |
| F6 | Nullability |
| F7 | Default behavior |
| F8 | Validation rules |
| F9 | Owning entity + module |
| F10 | Sensitivity classification (Catalog 08) |
| F11 | Audit requirements |
| F12 | Search/index considerations |
| F13 | Traceability (entity / requirements) |

Use `PENDING` / `NOT_APPLICABLE` with rationale — never blank.

## 6. Functional Requirements

| ID | Description |
| --- | --- |
| REQ-FLD-001 | Every persisted business field used by packages MUST have an IS-202 card (or amendment). |
| REQ-FLD-002 | Lifecycle/status fields MUST cite Catalog 01 — not field-dictionary draft labels. |
| REQ-FLD-003 | Raw and normalized counterparts MUST remain distinct fields where normalization applies. |
| REQ-FLD-004 | Field conditions MUST use the locked condition VO. |
| REQ-FLD-005 | Preference/consent fields MUST allow YES\|NO\|UNKNOWN; UNKNOWN MUST NOT default to NO. |
| REQ-FLD-006 | Shared-contact classification MUST NOT alone establish identity. |
| REQ-FLD-007 | New fields require IS-202 update or ADR before package reference. |
| REQ-FLD-008 | Sensitivity MUST cite Catalog 08 CLASS-* levels. |

## 7. Nonfunctional Requirements

| ID | Description |
| --- | --- |
| NFR-FLD-HONEST-001 | No invented Catalog keys; physical names deferred to IS-300. |
| NFR-FLD-PRIV-001 | RESTRICTED/CONFIDENTIAL fields never appear in docs as sample PII. |
| NFR-FLD-SEARCH-001 | Index notes are design intent, not DDL mandates. |

## 8. Value object catalog

| VO ID | Name | Allowed values / shape | Rules |
| --- | --- | --- | --- |
| VO-UUID | EntityId | Opaque unique ID | Never reuse; format finalize IS-300 |
| VO-BATCH-CODE | BatchCode | Human-readable non-PII code | No embedded personal data |
| VO-ROW-NUMBER | RowNumber | Integer 1–10 | Unique per page among existing entries |
| VO-FIELD-CONDITION | FieldCondition | `PROVIDED` \| `NOT_PROVIDED` \| `UNREADABLE` \| `AMBIGUOUS` \| `CORRECTED` | Locked (D-030) |
| VO-TRI-STATE | YesNoUnknown | `YES` \| `NO` \| `UNKNOWN` | UNKNOWN ≠ NO; never silent default to NO |
| VO-RAW-TEXT | RawFieldValue | Unicode string as typed | Preserve; no semantic rewrite |
| VO-NORM-NAME | NormalizedName | Trimmed/collapsed/casefolded compare form | Must not guess legal names/nicknames/demographics |
| VO-NORM-EMAIL | NormalizedEmail | Lowercased trimmed email form | Must not alter local-part meaning / invent chars |
| VO-NORM-PHONE | NormalizedPhone | Digits-focused compare form (+ optional extension separate) | Must not invent missing digits/area codes |
| VO-NORM-ZIP | NormalizedZip | 5-digit or ZIP+4 when evidenced | Must not infer from city/geocode in V1 |
| VO-CONTENT-HASH | ContentHash | SHA-256 hex | Integrity / duplicate detection |
| VO-PRIORITY | WorkPriority | `NORMAL` \| `HIGH` \| `URGENT` | Batch/page ops priority — not Catalog 01 state |
| VO-SOURCE-TYPE | BatchSourceType | `EVENT` \| `MEETING` \| `CANVASS` \| `OFFICE_DROP` \| `COMMUNITY_GROUP` \| `VOLUNTEER_DRIVE` \| `OTHER` \| `UNKNOWN` | Context only |
| VO-MATCH-CONFIDENCE | MatchConfidence | `EXACT` \| `HIGH_CONFIDENCE` \| `POSSIBLE` \| `LOW_CONFIDENCE` \| `NO_MATCH` \| `CONFLICT` | Explainable; policy-bound auto-link |
| VO-CANDIDATE-STATUS | CandidateStatus | `SUGGESTED` \| `SELECTED` \| `REJECTED` \| `SUPERSEDED` \| `EXPIRED` | Not a resolution; not promotion |
| VO-RESOLUTION-OUTCOME | ResolutionOutcome | `LINK_EXISTING` \| `CREATE_NEW` \| `DEFER` \| `RETURN_FOR_CORRECTION` \| `NO_ACTION` | Closed set (IS-200) |
| VO-RESOLUTION-METHOD | ResolutionMethod | `HUMAN` \| `APPROVED_EXACT_RULE` \| `ADMINISTRATIVE` \| `SYSTEM_RECOVERY` | Audit who/how |
| VO-CONTACT-SHARE | ContactSharingClass | `PERSONAL` \| `HOUSEHOLD_SHARED` \| `ORGANIZATIONAL` \| `UNKNOWN` | Shared ≠ identity alone |
| VO-TIMESTAMP | Instant | UTC instant | Server authority preferred |
| VO-OPT-LOCK | VersionToken | Monotonic version / etag | Optimistic concurrency (ADR-015 posture) |
| VO-CAT01-STATE | Catalog01State | Per machine enum in Catalog 01 | **Sole** business-state VO; never redefine here |

---

## 9. Field cards (core)

Card format: compact answers to F1–F13. Logical types only.

### 9.1 Shared / cross-cutting

| Field ID | F1 Name | F2 Meaning | F3 Type | F4 VO | F5 Constraints | F6 Null | F7 Default | F8 Validation | F9 Owner | F10 Class | F11 Audit | F12 Index | F13 Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FLD-ID | `id` | Durable entity identity | ID | VO-UUID | Unique, immutable | NO | Generated | Non-empty unique | Owning entity module | CLASS-002/003 by entity | Create only | PK | REQ-DOM-007; ENT-* |
| FLD-CREATED-AT | `created_at` | Creation instant | Instant | VO-TIMESTAMP | UTC | NO | Server now | Valid instant | Owning module | CLASS-002 | Optional | Range | Ops |
| FLD-UPDATED-AT | `updated_at` | Last mutation instant | Instant | VO-TIMESTAMP | UTC ≥ created | NO | Server now on write | Valid instant | Owning module | CLASS-002 | Optional | Range | Ops |
| FLD-VERSION | `version` | Optimistic concurrency token | Int/token | VO-OPT-LOCK | Monotonic | NO | 0/1 | Conflict → STALE_VERSION | Owning module | CLASS-002 | On conflict useful | — | ADR-015 |

### 9.2 ENT-BATCH fields

| Field ID | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F10 | F11 | F12 | F13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FLD-BATCH-CODE | `batch_code` | Human batch label | String | VO-BATCH-CODE | Non-PII pattern | NO | Generated | Unique; no PII | ENT-BATCH / MOD-BATCHES | CLASS-002 | Create | Unique | Batch UX |
| FLD-BATCH-NAME | `batch_name` | Display name | String | VO-RAW-TEXT | Length PENDING | YES | None | Trim | MOD-BATCHES | CLASS-002 | Material changes | Optional | — |
| FLD-BATCH-SOURCE-TYPE | `source_type` | Collection context type | Enum | VO-SOURCE-TYPE | Closed set | NO | `UNKNOWN` | Enum membership | MOD-BATCHES | CLASS-002 | Optional | Filter | — |
| FLD-BATCH-SOURCE-NAME | `source_name` | Event/source label | String | VO-RAW-TEXT | — | YES | None | Trim | MOD-BATCHES | CLASS-002 | Optional | Search | — |
| FLD-BATCH-COLLECTION-DATE | `collection_date` | When collected | Date | primitive date | Plausible range | YES | None | Not future-absurd | MOD-BATCHES | CLASS-002 | Optional | Range | — |
| FLD-BATCH-COUNTY | `county` | Location context | String | VO-RAW-TEXT | — | YES | None | Trim | MOD-BATCHES | CLASS-002 | Optional | Filter | — |
| FLD-BATCH-CITY | `city` | Location context | String | VO-RAW-TEXT | — | YES | None | Trim | MOD-BATCHES | CLASS-002 | Optional | Filter | — |
| FLD-BATCH-COMMUNITY | `community` | Community label | String | VO-RAW-TEXT | — | YES | None | Trim | MOD-BATCHES | CLASS-002 | Optional | — | — |
| FLD-BATCH-COLLECTED-BY-TEXT | `collected_by_text` | Collector free text | String | VO-RAW-TEXT | — | YES | None | Trim | MOD-BATCHES | CLASS-003 | Optional | — | Privacy |
| FLD-BATCH-UPLOADED-BY | `uploaded_by_user_id` | Uploader | ID | VO-UUID | Must ref user | NO | Actor | FK integrity | MOD-BATCHES | CLASS-002 | Yes | FK | AUDIT |
| FLD-BATCH-NOTES | `notes` | Free notes | String | VO-RAW-TEXT | Length PENDING | YES | None | — | MOD-BATCHES | CLASS-003 | Material edits | — | — |
| FLD-BATCH-PRIORITY | `priority` | Ops priority | Enum | VO-PRIORITY | Closed set | NO | `NORMAL` | Enum | MOD-BATCHES | CLASS-002 | Optional | Filter | — |
| FLD-BATCH-STATE | `lifecycle_state` | Batch business state | Enum | **VO-CAT01-STATE** | **STATE-BATCH-001 only** | NO | Per Cat01 | Illegal transition reject | MOD-BATCHES | CLASS-002 | Transition audit | Filter | REQ-FLD-002 |
| FLD-BATCH-PAGE-COUNT | `page_count` | Counter | Int | primitive | ≥0 | NO | 0 | Non-negative | MOD-BATCHES | CLASS-002 | — | — | Derived/persist PENDING STATE-DEC |
| FLD-BATCH-ENTRY-COUNT | `entry_count` | Counter | Int | primitive | ≥0 | NO | 0 | Non-negative | MOD-BATCHES | CLASS-002 | — | — | Same |
| FLD-BATCH-COMPLETED-AT | `completed_at` | Completion instant | Instant | VO-TIMESTAMP | — | YES | None until complete | — | MOD-BATCHES | CLASS-002 | Yes | Range | — |
| FLD-BATCH-ARCHIVED-AT | `archived_at` | Archive instant | Instant | VO-TIMESTAMP | — | YES | None | — | MOD-BATCHES | CLASS-002 | Yes | — | — |

**Explicit reject:** field-dictionary batch statuses (`UPLOADING`, `READY`, `IN_PROGRESS`, …) are **not** production enums — use Catalog 01.

### 9.3 ENT-PAGE fields

| Field ID | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F10 | F11 | F12 | F13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FLD-PAGE-BATCH-ID | `batch_id` | Parent batch | ID | VO-UUID | Must exist | NO | Required | FK | ENT-PAGE / MOD-PAGES | CLASS-002 | — | FK | Hierarchy |
| FLD-PAGE-NUMBER | `page_number` | Order in batch | Int | primitive | ≥1 | NO | Assigned | Unique per batch | MOD-PAGES | CLASS-002 | — | Composite | — |
| FLD-PAGE-CODE | `page_code` | Human page code | String | VO-RAW-TEXT | Non-PII | YES | Generated | Unique optional | MOD-PAGES | CLASS-002 | — | Unique | — |
| FLD-PAGE-IMAGE-ID | `source_image_id` | Active original image | ID | VO-UUID | — | YES | None until upload | FK when set | MOD-PAGES+UPLOADS | CLASS-004 | Yes | FK | Evidence |
| FLD-PAGE-STATE | `lifecycle_state` | Page business state | Enum | **VO-CAT01-STATE** | **STATE-PAGE-001** | NO | Per Cat01 | Transition rules | MOD-PAGES | CLASS-002 | Transition | Filter | REQ-FLD-002 |
| FLD-PAGE-IMAGE-QUALITY-STATE | `image_quality_state` | Quality lifecycle | Enum | **VO-CAT01-STATE** | **STATE-IMAGE-QUALITY-001** | YES | PENDING path | Cat01 | MOD-UPLOADS/PAGES | CLASS-002 | Yes | Filter | — |
| FLD-PAGE-ENTRY-COUNT | `entry_count` | 0–10 | Int | primitive | 0–10 | NO | 0 | ≤10 | MOD-PAGES | CLASS-002 | — | — | REQ-DOM-003 |
| FLD-PAGE-ENTERED-BY | `entered_by_user_id` | Transcriber | ID | VO-UUID | — | YES | None | FK | MOD-TRANSCRIPTIONS | CLASS-002 | Yes | FK | — |
| FLD-PAGE-SUBMITTED-AT | `submitted_at` | Transcription submit | Instant | VO-TIMESTAMP | — | YES | None | — | MOD-TRANSCRIPTIONS | CLASS-002 | Yes | Range | — |
| FLD-PAGE-COMPLETED-AT | `completed_at` | Page complete | Instant | VO-TIMESTAMP | — | YES | None | — | MOD-PAGES | CLASS-002 | Yes | — | — |
| FLD-PAGE-ARCHIVED-AT | `archived_at` | Archive | Instant | VO-TIMESTAMP | — | YES | None | — | MOD-PAGES | CLASS-002 | Yes | — | — |

**Claim overlay fields** live on ENT-CLAIM (not duplicated as authority on page): see §9.5. Page may expose read-only projection.

### 9.4 ENT-ENTRY fields (person-line)

| Field ID | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F10 | F11 | F12 | F13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FLD-ENTRY-PAGE-ID | `page_id` | Parent page | ID | VO-UUID | Must exist | NO | Required | FK | ENT-ENTRY | CLASS-002 | — | FK | — |
| FLD-ENTRY-ROW | `row_number` | Sheet row 1–10 | Int | VO-ROW-NUMBER | 1–10 unique/page | NO | Assigned | Unique per page | MOD-DRAFTS/TRANS | CLASS-002 | — | Composite | Identity≠row |
| FLD-ENTRY-CODE | `entry_code` | Human code | String | VO-RAW-TEXT | Non-PII | YES | Generated | — | MOD-DRAFTS/TRANS | CLASS-002 | — | Optional unique | — |
| FLD-ENTRY-STATE | `lifecycle_state` | Entry business state | Enum | **VO-CAT01-STATE** | **STATE-ENTRY-001** | NO | Per Cat01 | Transitions | ISSUE-MOD-001 writers | CLASS-003 | Transition | Filter | REQ-FLD-002 |
| FLD-ENTRY-FIRST-RAW | `first_name_raw` | Typed first name | String | VO-RAW-TEXT | — | YES | None | With condition | MOD-DRAFTS/TRANS | CLASS-003 | Submit snapshot | — | D-030 |
| FLD-ENTRY-LAST-RAW | `last_name_raw` | Typed last name | String | VO-RAW-TEXT | — | YES | None | With condition | MOD-DRAFTS/TRANS | CLASS-003 | Submit snapshot | — | D-030 |
| FLD-ENTRY-EMAIL-RAW | `email_raw` | Typed email | String | VO-RAW-TEXT | — | YES | None | With condition | MOD-DRAFTS/TRANS | CLASS-004 | Submit snapshot | — | Privacy |
| FLD-ENTRY-PHONE-RAW | `phone_raw` | Typed phone | String | VO-RAW-TEXT | — | YES | None | With condition | MOD-DRAFTS/TRANS | CLASS-004 | Submit snapshot | — | Privacy |
| FLD-ENTRY-ZIP-RAW | `zip_raw` | Typed ZIP | String | VO-RAW-TEXT | — | YES | None | With condition | MOD-DRAFTS/TRANS | CLASS-003 | Submit snapshot | — | — |
| FLD-ENTRY-FIRST-NORM | `first_name_normalized` | Compare form | String | VO-NORM-NAME | Norm rules | YES | None until norm | Norm service only | MOD-NORMALIZATION | CLASS-003 | — | Match index | REQ-FLD-003 |
| FLD-ENTRY-LAST-NORM | `last_name_normalized` | Compare form | String | VO-NORM-NAME | Norm rules | YES | None until norm | Norm only | MOD-NORMALIZATION | CLASS-003 | — | Match index | — |
| FLD-ENTRY-EMAIL-NORM | `email_normalized` | Compare form | String | VO-NORM-EMAIL | Norm rules | YES | None until norm | Norm only | MOD-NORMALIZATION | CLASS-004 | — | Match index | — |
| FLD-ENTRY-PHONE-NORM | `phone_normalized` | Compare form | String | VO-NORM-PHONE | Norm rules | YES | None until norm | Norm only | MOD-NORMALIZATION | CLASS-004 | — | Match index | — |
| FLD-ENTRY-ZIP-NORM | `zip_normalized` | Compare form | String | VO-NORM-ZIP | Norm rules | YES | None until norm | Norm only | MOD-NORMALIZATION | CLASS-003 | — | Optional | — |
| FLD-ENTRY-FIRST-COND | `first_name_condition` | Evidence quality | Enum | VO-FIELD-CONDITION | Closed | NO when field touched | `NOT_PROVIDED` if blank path | Enum | MOD-DRAFTS/TRANS | CLASS-002 | On correct | — | D-030 |
| FLD-ENTRY-LAST-COND | `last_name_condition` | Evidence quality | Enum | VO-FIELD-CONDITION | Closed | NO when touched | Same | Enum | MOD-DRAFTS/TRANS | CLASS-002 | On correct | — | — |
| FLD-ENTRY-EMAIL-COND | `email_condition` | Evidence quality | Enum | VO-FIELD-CONDITION | Closed | NO when touched | Same | Enum | MOD-DRAFTS/TRANS | CLASS-002 | On correct | — | — |
| FLD-ENTRY-PHONE-COND | `phone_condition` | Evidence quality | Enum | VO-FIELD-CONDITION | Closed | NO when touched | Same | Enum | MOD-DRAFTS/TRANS | CLASS-002 | On correct | — | — |
| FLD-ENTRY-ZIP-COND | `zip_condition` | Evidence quality | Enum | VO-FIELD-CONDITION | Closed | NO when touched | Same | Enum | MOD-DRAFTS/TRANS | CLASS-002 | On correct | — | — |
| FLD-ENTRY-VOL-RESP | `volunteer_response` | Volunteer preference | Enum | VO-TRI-STATE | YES/NO/UNKNOWN | NO | **UNKNOWN** if unclear | Never coerce UNKNOWN→NO | MOD-DRAFTS/TRANS | CLASS-003 | Submit | Filter | REQ-FLD-005 |
| FLD-ENTRY-EMAIL-LIST | `email_list_response` | Email-list preference | Enum | VO-TRI-STATE | YES/NO/UNKNOWN | NO | **UNKNOWN** if unclear | Never coerce UNKNOWN→NO | MOD-DRAFTS/TRANS | CLASS-003 | Submit | Filter | REQ-FLD-005 |
| FLD-ENTRY-CANONICAL-LINK | `linked_canonical_person_id` | Link after promotion success | ID | VO-UUID | External ID | YES | None until promoted | Set only via promotion success | MOD-PROMOTION | CLASS-003 | Yes | FK/ext | ≠ match alone |
| FLD-ENTRY-ENTERED-BY | `entered_by_user_id` | Actor | ID | VO-UUID | — | YES | Actor | FK | MOD-DRAFTS/TRANS | CLASS-002 | Yes | — | — |
| FLD-ENTRY-REVIEWED-BY | `reviewed_by_user_id` | Reviewer | ID | VO-UUID | — | YES | None | FK | MOD-RESOLUTION etc. | CLASS-002 | Yes | — | — |
| FLD-ENTRY-SUBMITTED-AT | `submitted_at` | Immutable revision time | Instant | VO-TIMESTAMP | — | YES | None until submit | — | MOD-TRANSCRIPTIONS | CLASS-002 | Yes | — | Immutability |
| FLD-ENTRY-RESOLVED-AT | `resolved_at` | Match resolution time | Instant | VO-TIMESTAMP | — | YES | None | — | MOD-RESOLUTION | CLASS-002 | Yes | — | — |

**Blank row rule:** if no meaningful person field values → **do not create** entry (IS-200/IS-201).

### 9.5 ENT-CLAIM fields

| Field ID | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F10 | F11 | F12 | F13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FLD-CLAIM-PAGE-ID | `page_id` | Claimed page | ID | VO-UUID | Must exist | NO | Required | FK | ENT-CLAIM / MOD-CLAIMS | CLASS-002 | Yes | FK | — |
| FLD-CLAIM-USER-ID | `claimed_by_user_id` | Holder | ID | VO-UUID | Must exist | NO | Actor | FK | MOD-CLAIMS | CLASS-002 | Yes | FK | AUDIT-CLAIM |
| FLD-CLAIM-STATE | `lifecycle_state` | Claim state | Enum | **VO-CAT01-STATE** | **STATE-CLAIM-001** | NO | ACTIVE on create | Transitions | MOD-CLAIMS | CLASS-002 | Transition | Filter | — |
| FLD-CLAIM-AT | `claimed_at` | Acquire time | Instant | VO-TIMESTAMP | — | NO | Server now | — | MOD-CLAIMS | CLASS-002 | Yes | — | — |
| FLD-CLAIM-LAST-ACTIVITY | `last_activity_at` | Renew signal | Instant | VO-TIMESTAMP | — | NO | claimed_at | — | MOD-CLAIMS | CLASS-002 | Optional | — | — |
| FLD-CLAIM-EXPIRES-AT | `expires_at` | Expiry | Instant | VO-TIMESTAMP | > claimed_at | NO | Policy duration | — | MOD-CLAIMS | CLASS-002 | Yes | Range | STATE-DEC duration |

### 9.6 ENT-IMAGE fields

| Field ID | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F10 | F11 | F12 | F13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FLD-IMAGE-HASH | `sha256_hash` | Content integrity | Hash | VO-CONTENT-HASH | 64 hex | NO when stored | Computed | Format | MOD-UPLOADS | CLASS-002 | Yes | Unique optional | Dup detect |
| FLD-IMAGE-STORAGE-KEY | `storage_key_original` | Private object key | String | primitive | Non-public URL as identity | NO when stored | Assigned | No public ACL | MOD-UPLOADS | CLASS-004 | Yes | — | Private storage |
| FLD-IMAGE-STORAGE-STATE | `storage_state` | Object lifecycle | Enum | **VO-CAT01-STATE** | **STATE-STORAGE-001** | NO | Per Cat01 | Transitions | MOD-UPLOADS | CLASS-002 | Transition | Filter | — |
| FLD-IMAGE-FILENAME | `original_filename` | Upload name | String | VO-RAW-TEXT | — | YES | None | Sanitize display | MOD-UPLOADS | CLASS-003 | Optional | — | — |
| FLD-IMAGE-MIME | `mime_type` | Media type | String | primitive | Allow-list PENDING | YES | None | Allow-list | MOD-UPLOADS | CLASS-002 | — | — | — |
| FLD-IMAGE-SIZE | `byte_size` | Size | Int | primitive | ≥0 | YES | None | Max PENDING Cat4 | MOD-UPLOADS | CLASS-002 | — | — | — |

Provider/bucket brand fields: **PENDING** ADR-005 / ISSUE-STORAGE-001 — names only, no secrets.

### 9.7 Match / resolution / promotion fields

| Field ID | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F10 | F11 | F12 | F13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FLD-CAND-ENTRY-ID | `entry_id` | Subject entry | ID | VO-UUID | — | NO | — | FK | ENT-MATCH-CANDIDATE | CLASS-003 | — | FK | — |
| FLD-CAND-PERSON-ID | `candidate_canonical_person_id` | Possible person | ID | VO-UUID | External | NO | — | — | MOD-MATCHING | CLASS-003 | — | — | Not promotion |
| FLD-CAND-CONFIDENCE | `confidence` | Tier | Enum | VO-MATCH-CONFIDENCE | Closed | NO | — | Enum | MOD-MATCHING | CLASS-002 | Yes | Filter | D-031 |
| FLD-CAND-STATUS | `candidate_status` | Candidate row status | Enum | VO-CANDIDATE-STATUS | Closed | NO | SUGGESTED | Enum | MOD-MATCHING | CLASS-002 | Optional | — | ≠ resolution |
| FLD-CAND-REASON | `explanation` | Why suggested | String/structured | VO-RAW-TEXT | Required non-empty for suggest | NO | — | Present | MOD-MATCHING | CLASS-002 | Yes | — | Explainable |
| FLD-CAND-SHARE-CLASS | `contact_sharing_class` | Contact sharing | Enum | VO-CONTACT-SHARE | Closed | YES | UNKNOWN | Enum; shared≠identity | MOD-MATCHING | CLASS-003 | Yes | — | REQ-FLD-006 |
| FLD-RES-ENTRY-ID | `entry_id` | Resolved entry | ID | VO-UUID | — | NO | — | FK | ENT-MATCH-RESOLUTION | CLASS-003 | Yes | FK | — |
| FLD-RES-OUTCOME | `outcome` | Resolution outcome | Enum | VO-RESOLUTION-OUTCOME | Closed set | NO | — | Enum; **no canonical write** | MOD-RESOLUTION | CLASS-003 | Yes | Filter | Match≠Promo |
| FLD-RES-METHOD | `method` | How decided | Enum | VO-RESOLUTION-METHOD | Closed | NO | — | Enum | MOD-RESOLUTION | CLASS-002 | Yes | — | — |
| FLD-RES-STATE | `lifecycle_state` | Resolution lifecycle | Enum | **VO-CAT01-STATE** | **STATE-MATCH-RESOLUTION-001** | NO | — | Transitions | MOD-RESOLUTION | CLASS-002 | Transition | — | — |
| FLD-RES-SELECTED-PERSON | `selected_canonical_person_id` | If LINK_EXISTING | ID | VO-UUID | Required iff LINK | YES | None | Consistent with outcome | MOD-RESOLUTION | CLASS-003 | Yes | — | Still not promo exec |
| FLD-PROMO-ENTRY-ID | `entry_id` | Subject | ID | VO-UUID | — | NO | — | FK | ENT-PROMOTION | CLASS-003 | Yes | FK | — |
| FLD-PROMO-RESOLUTION-ID | `resolution_id` | Driving resolution | ID | VO-UUID | — | NO | — | FK | MOD-PROMOTION | CLASS-003 | Yes | FK | Separate aggregate |
| FLD-PROMO-STATE | `lifecycle_state` | Promotion lifecycle | Enum | **VO-CAT01-STATE** | **STATE-PROMOTION-001** | NO | PENDING | Transitions; idempotent key | MOD-PROMOTION | CLASS-003 | Transition | Filter | — |
| FLD-PROMO-IDEMPOTENCY | `idempotency_key` | Replay safety | String | primitive | Unique | NO | Derived | Unique constraint | MOD-PROMOTION | CLASS-002 | Yes | Unique | ADR-014 posture |
| FLD-PROMO-RESULT-PERSON | `result_canonical_person_id` | Result person | ID | VO-UUID | On success | YES | None | Set on success only | MOD-PROMOTION | CLASS-003 | Yes | — | ISSUE-CANONICAL-001 |

### 9.8 ENT-USER (minimal)

| Field ID | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F10 | F11 | F12 | F13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FLD-USER-STATE | `lifecycle_state` | User lifecycle | Enum | **VO-CAT01-STATE** | **STATE-USER-001** | NO | — | Transitions | MOD-USERS | CLASS-002 | Transition | Filter | — |
| FLD-USER-EMAIL | `email` | Login/contact email | String | VO-NORM-EMAIL / raw pair PENDING | Valid email | Provider-dependent | — | Format | MOD-USERS | CLASS-004 | Yes | Unique | ADR-004 |

Auth provider fields: **PENDING** ADR-004 — do not invent.

### 9.9 Audit event (minimal)

| Field ID | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F10 | F11 | F12 | F13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FLD-AUDIT-NAME | `event_name` | Catalog 03 event | String | primitive | Catalog 03 only | NO | — | Must be cataloged | MOD-AUDIT | CLASS-002 | Self | Filter | Cat3 |
| FLD-AUDIT-AT | `occurred_at` | When | Instant | VO-TIMESTAMP | — | NO | Server | — | MOD-AUDIT | CLASS-002 | — | Range | — |
| FLD-AUDIT-ACTOR | `actor_user_id` | Who | ID | VO-UUID | — | YES | System | — | MOD-AUDIT | CLASS-002 | — | FK | — |
| FLD-AUDIT-PAYLOAD | `payload` | Structured facts | JSON | primitive | **No secrets** | YES | — | Secret scan | MOD-AUDIT | CLASS-003+ | — | — | Privacy |

---

## 10. Normalization policy (bound to VOs)

| Target | May | Must not |
| --- | --- | --- |
| Names | Trim, collapse spaces, Unicode normalize, casefold for compare, keep punctuation | Guess legal names, expand nicknames, infer demographics |
| Email | Trim, lowercase, strip nonsemantic surround punctuation, format-validate | Alter local-part meaning, remove significant dots by policy invention, rewrite domains, guess chars |
| Phone | Digit extract, US 10-digit recognition when unambiguous, separate extension | Add missing digits, guess area code, replace uncertain digits |
| ZIP | Trim, 5-digit / ZIP+4 when evidenced | Infer from city, “correct” without evidence, geocode in V1 |

## 11. Data / interface / state sections

* Physical types → IS-300.  
* APIs expose fields only via owning module contracts.  
* State fields → Catalog 01 exclusively.  

## 12. Acceptance Criteria

| ID | Criterion | Met? |
| --- | --- | --- |
| AC-FLD-001 | Value object catalog defined | Yes |
| AC-FLD-002 | Mandatory field questionnaire defined | Yes |
| AC-FLD-003 | Core entity fields carded with F1–F13 | Yes |
| AC-FLD-004 | Catalog 01 sole authority for lifecycle fields | Yes |
| AC-FLD-005 | Field-dictionary draft statuses explicitly rejected as enums | Yes |
| AC-FLD-006 | UNKNOWN≠NO and raw≠normalized locked | Yes |
| AC-FLD-007 | Field extension doctrine locked | Yes |
| AC-FLD-008 | No application/schema code created | Yes |

## 13. Open Decisions

| ID | Notes |
| --- | --- |
| ISSUE-AUDIT-001 | Complete reconciliation of remaining draft docs (Slice 002 banners) |
| ISSUE-MOD-001 | Entry field writer split |
| ISSUE-STORAGE-001 / ADR-005 | Storage provider field brands |
| ADR-004 | User identity fields |
| STATE-DEC-* | Derived vs persisted counters/states |
| Exact string lengths / mime allow-lists | Catalog 4 / IS-300 |

## 14. Risks

| ID | Risk | Mitigation |
| --- | --- | --- |
| RISK-FLD-001 | Packages use field-dict statuses as enums | REQ-FLD-002; banners |
| RISK-FLD-002 | Duplicate email fields across modules | One-definition rule §4.3 |
| RISK-FLD-003 | UNKNOWN coerced to NO in UI | REQ-FLD-005; tests |
| RISK-FLD-004 | Normalization mutates raw | REQ-FLD-003 |

## 15. Dependencies

IS-200/201; Catalogs 01/08; audit lane.

## 16. Traceability

| Requirement | Status |
| --- | --- |
| REQ-FLD-001…008 | FULLY_MAPPED (design) |
| Physical columns | PARTIALLY_MAPPED → IS-300 |

## 17. Implementation Boundary

**Authorized:** this dictionary; subordinate banner updates on field dictionary; governance.  
**Forbidden:** migrations; inventing Cat01 states; treating draft UX statuses as production.

## 18. Revision History

| Version | Date | Change | Approval |
| --- | --- | --- | --- |
| 1.0 | 2026-07-26 | Canonical field/VO dictionary + field doctrine | D-071 |

## Next primary

```text
PEOPLE-IS-300-DATABASE-ARCHITECTURE-1.0
```

## Independent lane

```text
AUDIT-SLICE-002 (supersession banners) — this closeout
```

## Final status

```text
PEOPLE-IS-202 FIELD AND VALUE OBJECT SPECIFICATIONS: APPROVED (DOCUMENTATION)
APPLICATION IMPLEMENTATION: NOT AUTHORIZED
```
