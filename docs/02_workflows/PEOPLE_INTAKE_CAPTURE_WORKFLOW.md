# People Intake — Capture Workflow

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-WORKFLOW-UX-DESIGN-1.0  
**Workspace:** CAPTURE  
**Primary role:** Field Uploader

---

## Purpose

Define the complete field path from starting a batch through successful upload into the shared office queue.

---

## Operating Goal

```text
Capture readable pages
→ Group them into a batch
→ Provide basic source information
→ Upload them successfully
```

---

## End-to-End Flow

```text
Uploader Home
→ New Batch
→ Enter source information
→ Take Pictures and/or Upload From Device
→ Review Images (rotate, reorder, replace, delete)
→ Upload Batch
→ Per-page upload progress
→ Batch Uploaded
→ Done / Upload Another / View Batch
```

---

## 1. Uploader Home

### Primary actions

```text
Take Pictures
Upload From Device
Resume Upload
```

### Secondary

```text
Recent Batches
```

### Must not show

Matching queues, person records, or detailed transcription tools.

---

## 2. Start Batch

User chooses **New Batch**.

### Fields

| Field | Required intensity |
| --- | --- |
| Source or Event Name | Strongly encouraged |
| Date Collected | Optional but useful |
| County | Optional |
| City or Community | Optional |
| Collected By | Optional (default may use current user display name) |
| Notes | Optional |

### Automatic system fields

- Upload date/time
- Uploader identity
- Batch number / ID
- Device time at creation

### Suggested name

```text
Greene County Volunteer Sheets — July 24, 2026
```

User may edit the name.

---

## 3. Camera Capture Mode

Camera remains open between pages.

```text
Take Page 1 → Accept → Take Page 2 → Accept → … → Finish → Review Batch
```

### Controls

```text
Retake · Accept · Finish
```

### Counter

```text
8 pages captured
```

---

## 4. Upload Existing Images

- Multi-select supported
- Formats: JPG, JPEG, PNG, HEIC where safely supported
- Preserve or allow reorder into page sequence

---

## 5. Image Review Before Upload

Thumbnails show:

- Page number
- Rotate
- Delete
- Replace
- Reorder
- Expand preview

Primary action:

```text
Upload 12 Pages
```

### Field quality guidance (shown before/during capture)

```text
Place the entire sheet inside the frame.
Use good lighting.
Avoid shadows.
Make sure names and phone numbers are readable.
```

No OCR or automated image-analysis scoring in Version 1.

---

## 6. Upload Progress

Page-level status:

```text
Waiting · Uploading · Uploaded · Retry Needed
```

Display:

```text
Uploading Page 4 of 12
```

If one page fails, remaining pages continue. User can retry failed pages individually.

---

## 7. Batch Completion

```text
Batch Uploaded
12 pages are ready for office entry.
```

Actions:

```text
Upload Another Batch · View Batch · Done
```

Uploader may leave immediately after confirmation.

---

## 8. Resume Upload

If upload was interrupted:

```text
Resume Upload
Pending pages remain on this device until upload completes.
```

Incomplete batches must never be shown as fully uploaded.

---

## 9. Capture Edge Cases

| Case | Behavior |
| --- | --- |
| Blurry/cut-off before upload | Retake, Replace, Remove, or Keep Anyway |
| Partial upload failure | Continue others; mark failures Retry Needed |
| Weak signal | Local queue; clear incomplete status |
| Duplicate selection | Allowed at capture; later exception/matching may flag duplicates |
| Zero pages | Cannot upload empty batch |
| Sideways image | Rotate in review before upload |

---

## 10. Success Criteria

A new uploader can sign in, start a batch, photograph five pages, review, upload, and confirm completion using only in-app guidance.
