# People Intake — Image Storage Architecture

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-DATA-MATCHING-STORAGE-DESIGN-1.0  
**Buckets authorized:** No — design only

---

## Storage Model

Use **private object storage**. Postgres stores metadata and storage references only — not full image blobs.

### Object types per page

```text
Original Image
Display Derivative
Thumbnail
```

| Type | Rule |
| --- | --- |
| Original | Preserved without destructive alteration |
| Display | May rotate/resize/compress/convert for viewing |
| Thumbnail | Queue/batch views only |

Viewing adjustments must not modify the original.

---

## Metadata (Conceptual)

```text
id, page_id
storage_provider, bucket_name
storage_key_original, storage_key_display, storage_key_thumbnail
original_filename, mime_type_original, mime_type_display
file_size_bytes, width, height, orientation
sha256_hash
upload_status, conversion_status
uploaded_by_user_id, uploaded_at
created_at, updated_at, deleted_at
```

### Upload status

```text
PENDING | UPLOADING | UPLOADED | FAILED | REPLACED | QUARANTINED | DELETED
```

### Conversion status

```text
NOT_REQUIRED | PENDING | PROCESSING | COMPLETE | FAILED
```

---

## Path Convention

```text
people-intake/
  production/
    2026/
      07/
        batch-id/
          page-id/
            original/file.ext
            display/page.webp
            thumbnail/page.webp
```

Separate prefixes or buckets for development / preview / production.

Do **not** use public Netlify asset storage for source images.

---

## Signed Access

- Authenticated user  
- Server-side role check  
- Page-level authorization  
- Short expiration  
- No permanent public URL  
- No public bucket listing  
- No image in public HTML metadata or search indexes  
- Regenerate signed URL when expired  

---

## Replacement

Allowed when blurry, cut off, wrong page, wrong orientation, or better copy exists.

Must: preserve original record, mark prior replaced, create new version, record who/why, audit, reopen transcription if materially changed.

---

## Deletion

Restricted to Owner / Restricted Admin / Retention Process / Legal-Privacy Process.

Must record reason/actor/time, confirm DB references, preserve non-image audit, prevent orphaned metadata. Soft-delete before permanent where practical.

Routine users may not delete images.

---

## Provider Decision (Deferred)

Candidates: Supabase Storage, S3-compatible private storage, Netlify-compatible external object storage.

Must support: private buckets, signed URLs, server-side upload authz, metadata, lifecycle rules, env separation, reliable mobile upload, reasonable cost, auditability.

---

## Storage ↔ DB Compensation

Uploads that succeed in storage but fail in DB (or vice versa) require retry, orphan cleanup, and processing-error records. Not a single distributed transaction.
