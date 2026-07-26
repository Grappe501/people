# People Intake — Field Dictionary

> **SUPERSEDED AS CANONICAL FIELD AUTHORITY — AUDIT-SLICE-002 / D-071**  
> **Canonical field and value-object definitions:** `docs/implementation_specs/200_domain/PEOPLE-IS-202-FIELD-AND-VALUE-OBJECT-SPECIFICATIONS.md`.  
> **Canonical business-state enums:** Catalog 01 (not the `status` lists in this file).  
> This file remains a **historical conceptual companion**. Where it conflicts with IS-202 or Catalog 01, those authorities win (ISSUE-AUDIT-001).

**Status:** draft_complete — **SUPERSEDED (canonical fields → IS-202; states → Catalog 01)**  
**Version:** 1.0  
**Build:** PEOPLE-DATA-MATCHING-STORAGE-DESIGN-1.0  
**Note:** Conceptual fields. Physical column names deferred to IS-300+. Prefer IS-202 cards for engineering.

---

## Field Condition Values

```text
PROVIDED | NOT_PROVIDED | UNREADABLE | AMBIGUOUS | CORRECTED
```

| Value | Meaning |
| --- | --- |
| PROVIDED | Present and readable |
| NOT_PROVIDED | Volunteer left blank |
| UNREADABLE | Writing present but not reliably interpretable |
| AMBIGUOUS | Partially readable; multiple plausible readings |
| CORRECTED | Formal post-submit correction (prior value preserved) |

---

## Consent / Preference Values

```text
YES | NO | UNKNOWN
```

`UNKNOWN` = blank, unreadable, ambiguous, or not clearly marked. **Never interpret as No.**

---

## Intake Batch (Conceptual)

| Field | Notes |
| --- | --- |
| id | Stable unique ID |
| batch_code | Human-readable, non-PII (e.g., PI-2026-0728-00041) |
| batch_name | Display name |
| source_type | EVENT, MEETING, CANVASS, OFFICE_DROP, COMMUNITY_GROUP, VOLUNTEER_DRIVE, OTHER, UNKNOWN |
| source_name / event_name | Context |
| collection_date | When collected |
| county / city / community | Location context |
| collected_by_text / collected_by_person_id | Collector |
| uploaded_by_user_id | Uploader |
| notes | Free text |
| priority | NORMAL, HIGH, URGENT |
| status | DRAFT, UPLOADING, UPLOAD_PARTIAL, READY, IN_PROGRESS, NEEDS_ATTENTION, COMPLETED, ARCHIVED |
| page_count / entry_count | Counters |
| created_at / updated_at / completed_at / archived_at | Timestamps |

---

## Intake Page (Conceptual)

| Field | Notes |
| --- | --- |
| id | Stable unique ID |
| batch_id | Parent |
| page_number | Batch-relative order |
| page_code | e.g., …-P03 |
| source_image_id | Active original reference |
| status | Conceptual UX/workflow states |
| image_quality_status | Quality / exception |
| entry_count | 0–10 |
| claimed_by_user_id / claimed_at / claim_last_activity_at / claim_expires_at | Claim overlay |
| entered_by_user_id / submitted_at | Transcription |
| matching_started_at / completed_at / archived_at | Lifecycle |
| version | Optimistic concurrency |
| created_at / updated_at | Timestamps |

---

## Intake Entry (Conceptual)

| Field | Notes |
| --- | --- |
| id / entry_code | Unique; e.g., …-R07 |
| page_id / row_number | Row 1–10 unique per page |
| status | Entry lifecycle |
| *_raw | first/last/email/phone/zip as typed |
| volunteer_response / email_list_response | YES/NO/UNKNOWN |
| *_condition | Per-field condition enum |
| *_normalized | Deterministic safe forms |
| matched_person_id / match_status | After resolution/promotion |
| entered_by_user_id / reviewed_by_user_id | Actors |
| created_at / updated_at / submitted_at / resolved_at | Timestamps |

### Blank vs partial

- No meaningful values → do not create entry  
- At least one meaningful person field → may create entry (warn, do not discard)

---

## Normalization Rules (Summary)

| Field | May | Must not |
| --- | --- | --- |
| Names | Trim, collapse spaces, Unicode normalize, casefold for compare, keep punctuation | Guess legal names, expand nicknames, infer demographics |
| Email | Trim, lowercase, strip clearly nonsemantic surround punctuation, format-validate | Alter local-part, remove dots, rewrite domains, guess chars |
| Phone | Digits extract, US 10-digit recognition, unambiguous country code, separate extension | Add missing digits, guess area code, replace uncertain digits |
| ZIP | Trim, 5-digit / ZIP+4 | Infer from city, correct without evidence, geocode in V1 |

---

## Match Candidate / Resolution (Conceptual)

See matching engine spec for full dictionaries. Key enums:

- Confidence: EXACT, HIGH_CONFIDENCE, POSSIBLE, LOW_CONFIDENCE, NO_MATCH, CONFLICT  
- Candidate status: SUGGESTED, SELECTED, REJECTED, SUPERSEDED, EXPIRED  
- Resolution type: LINK_EXISTING, CREATE_NEW, RETURN_FOR_CORRECTION, DEFER, NO_ACTION  
- Resolution method: HUMAN, APPROVED_EXACT_RULE, ADMINISTRATIVE, SYSTEM_RECOVERY  

---

## Source Image (Conceptual)

| Field | Notes |
| --- | --- |
| storage_provider / bucket_name / storage_key_* | Original, display, thumbnail |
| original_filename / mime types / size / width / height / orientation | Metadata |
| sha256_hash | Duplicate detection |
| upload_status | PENDING, UPLOADING, UPLOADED, FAILED, REPLACED, QUARANTINED, DELETED |
| conversion_status | NOT_REQUIRED, PENDING, PROCESSING, COMPLETE, FAILED |

---

## Contact Sharing Classification (Canonical)

```text
PERSONAL | HOUSEHOLD_SHARED | ORGANIZATIONAL | UNKNOWN
```

Shared contacts cannot independently establish identity.
