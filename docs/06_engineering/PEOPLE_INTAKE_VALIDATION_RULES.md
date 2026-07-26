# People Intake — Validation Rules (Engineering)

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-SECURITY-API-ENGINEERING-DESIGN-1.0

---

## Layers (Authoritative Order)

```text
Transport validation
→ Schema validation
→ Business-rule validation
→ Authorization validation
→ State-transition validation
→ Database constraint validation
```

Client validation improves UX but is **never** authoritative.

Sensitive write endpoints prefer **strict rejection** of unexpected fields.

---

## Must Validate Server-Side

Route/query params · JSON bodies · forms · file metadata · upload completion callbacks · role-management · match resolutions · batch metadata · page claims

---

## Upload Security

Allowed: approved image formats only (JPEG/PNG; HEIC when safely supported).

Validate: declared MIME, extension, decodable image content, size, dimensions, corruption, hash, storage key.

- Never trust user filename as storage key  
- Sanitize and store original filename as metadata only  
- Display derivatives should strip unnecessary embedded metadata (e.g., geolocation) when feasible  
- Undecodable/suspicious → `QUARANTINED` (not displayed until approved/replaced)  

Exact size limits deferred.

---

## Transcription Business Rules (Summary)

- Max 10 entries; unique row numbers 1–10  
- Blank rows create no entries  
- Partial entries allowed with warnings  
- YES/NO/UNKNOWN for volunteer and email list  
- Field conditions enforced  
- Warnings generally non-blocking; claim/version/state errors blocking  

Align with field dictionary and form behavior specs.

---

## Privacy Validation

Do not collect or invent race, religion, gender, ideology, income, household relationship, citizenship, disability, or other sensitive inferred traits.

Purpose limited to intake, transcription, matching, canonical create/update, preference recording, audit/correction.
