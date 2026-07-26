# People Intake — Data Provenance

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-DATA-MATCHING-STORAGE-DESIGN-1.0

---

## Requirement

No canonical person attribute created by People Intake may exist without a valid provenance reference.

---

## Provenance Record (Conceptual)

```text
id
source_system          # PEOPLE_INTAKE
source_type
batch_id
page_id
entry_id
source_image_id
uploader_user_id
transcriber_user_id
reviewer_user_id
match_resolution_id
captured_at
transcribed_at
resolved_at
created_at
```

---

## Layers Distinguishing Evidence

| Layer | Question answered |
| --- | --- |
| Source evidence | What image/file supports this? |
| Raw transcription | What did the operator type? |
| Normalized intake | What safe compare form was used? |
| Match decision | Why was this person linked/created? |
| Accepted update | What canonical change was approved? |
| Rejected update | What was proposed and refused? |

---

## Correction History (Append-Only)

```text
id, intake_entry_id, field_name
old_raw_value, new_raw_value
old_condition, new_condition
reason, corrected_by_user_id, corrected_at
```

Original submitted values remain discoverable via audit/correction history.

---

## Preference History (Time-Aware)

```text
person_id, preference_type, preference_value
source_reference, effective_at, recorded_at, status
```

Types: VOLUNTEER, EMAIL_LIST  
Values: YES, NO, UNKNOWN  

Unknown must not supersede known Yes/No. Explicit Yes/No may supersede older explicit values per final business rules (deferred detail).

---

## Audit Events (Append-Only)

Conceptual fields:

```text
id, event_type, actor_user_id, actor_role
batch_id, page_id, entry_id, person_id, match_resolution_id
before_summary, after_summary, reason, metadata, created_at
```

### Event categories (non-exhaustive)

BATCH_CREATED, BATCH_UPDATED, PAGE_UPLOADED, PAGE_REORDERED, IMAGE_REPLACED,  
PAGE_CLAIMED, PAGE_RELEASED, CLAIM_EXPIRED, DRAFT_SAVED,  
ENTRY_CREATED, ENTRY_UPDATED, PAGE_SUBMITTED,  
MATCH_CANDIDATES_GENERATED, MATCH_LINKED, PERSON_CREATED,  
ATTRIBUTE_ADDED, ATTRIBUTE_RETIRED, ENTRY_RETURNED, ENTRY_CORRECTED,  
PAGE_COMPLETED, BATCH_COMPLETED, ADMIN_OVERRIDE,  
ACCESS_DENIED, STORAGE_ERROR, PROCESSING_ERROR  

### Sensitive content rule

Store concise change summaries — not unnecessary full PII copies. Full source values remain in authorized records.

---

## Processing Errors

```text
id, error_type, severity
batch_id, page_id, entry_id, operation
message_safe, technical_reference
retryable, retry_count, status
created_at, resolved_at, resolved_by_user_id
```

Do not store secrets or full PII in technical error messages.
