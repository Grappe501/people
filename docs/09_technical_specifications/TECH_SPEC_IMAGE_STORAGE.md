# Image Storage Specification

**Library volume:** 8 — Technical Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## 1. Purpose

Private storage of source images + optional derivatives; temporary authorized access only.

## 2. Model

| Object | Notes |
| --- | --- |
| Original | Immutable bytes; content hash |
| Display derivative | Optional resized/rotated for UI |
| Thumbnail | Optional |

Postgres stores metadata + storage keys — not primary blob store.

## 3. Upload Flow

1. Create/register page.  
2. `upload-intent` → authorized PUT target + intentId.  
3. Client uploads to storage.  
4. `upload-complete` → verify size/type/hash → activate image version → audit.

## 4. Access

`GET image-access` → short-lived signed URL after authz. Never public buckets for source images.

## 5. Invariants

- Replace image creates new version; prior retained for evidence.  
- Duplicate hash detection warned (not auto-delete).  
- Logs never contain signed URLs.

## 6. Limits

Max size / MIME allowlist per configuration catalog. Errors: `UPLOAD_TOO_LARGE` `UPLOAD_TYPE_NOT_ALLOWED`.

## 7. Audit

`UploadIntentCreated` `ImageUploaded` `ImageReplaced` `ImageAccessGranted` (metadata only)

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 3/5 Image storage architecture
- Volume 9 storage tables
