# People Intake — Privacy and Retention

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-DATA-MATCHING-STORAGE-DESIGN-1.0  
**Exact retention periods:** Deferred

---

## Privacy Boundaries

People Intake handles personal information. Minimize unnecessary exposure.

| Role | Access intent |
| --- | --- |
| Uploader | No broad people search |
| Data entry | No full person histories required |
| Reviewer | Matching-relevant information only |
| Administrator | Operational information |
| Owner | High-risk access control |

Additional rules:

- Image access temporary and authorized  
- Raw data not included in logs  
- Unrestricted bulk export not in Version 1 unless separately approved  

---

## Future Export (If Approved)

Must define: authorized roles, purpose, fields, redaction, encryption, expiration, audit logging, download limits.

---

## Retention States (Architecture Must Support)

```text
ACTIVE
RETAIN_UNTIL_DATE
LEGAL_HOLD
ELIGIBLE_FOR_DELETION
DELETED
```

Retention policy should separately address:

- Original images  
- Display derivatives  
- Intake entries  
- Audit events  
- Match candidates / resolutions  
- Canonical person provenance  
- Upload-error artifacts  

---

## Retention Principle

Source images should be retained long enough to verify transcription, resolve matching, support corrections, and support audit needs — not indefinitely without an approved purpose.

**Legal hold** overrides normal deletion schedules.

Exact periods deferred to owner/policy approval.

---

## Deletion vs Archive

See `PEOPLE_INTAKE_MIGRATION_AND_ROLLBACK.md` for archive / soft-delete / permanent-delete semantics.

Image deletion: `PEOPLE_INTAKE_IMAGE_STORAGE_ARCHITECTURE.md`.

Canonical person deletion: not a direct People Intake action.
