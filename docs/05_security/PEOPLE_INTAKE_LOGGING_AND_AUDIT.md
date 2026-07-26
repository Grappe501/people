# People Intake — Logging and Audit

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-SECURITY-API-ENGINEERING-DESIGN-1.0

---

## Separation

| System | Purpose | Mutability |
| --- | --- | --- |
| Technical logging | Debug, performance, infra, jobs | Rotatable / limited retention |
| Audit history | Accountability, corrections, matching, admin overrides | **Append-only** |

---

## Logs May Include

```text
request ID, user ID, role, record IDs
operation name, status, duration, error code
retry count, job ID, deployment environment
```

## Logs Must Not Include

```text
full names, raw emails, raw phones
unnecessary ZIP + identifying context
source image data / base64
signed URLs, access/refresh tokens
DB/storage/OAuth secrets
complete request bodies containing PII
```

Use structured logs. Distinguish development / preview / production.

---

## Always Audit

- User invited / role changed / user disabled  
- Batch archived  
- Image replaced  
- Page force-released / reassigned / submitted  
- Match resolved  
- Person creation requested / person linked  
- Canonical attribute promoted  
- Correction made  
- Completed page reopened  
- Retention deletion approved  
- High-risk image access when policy requires  
- Administrative override  

Routine autosave may be summarized to avoid audit noise.

---

## High-Risk Operations

Failure to write required audit evidence should **block completion**.

---

## Visibility Minimization (Reminder)

Uploader / data entry / reviewer see only work-necessary data. No donor/voter/campaign relationship data in Version 1 intake views. No unrestricted bulk export.
