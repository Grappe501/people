# People Intake — Exception Workflows

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-WORKFLOW-UX-DESIGN-1.0

---

## Purpose

Define recovery paths when images, claims, transcription, matching, or access fail the happy path.

---

## 1. Bad Image During Upload

Uploader actions:

```text
Retake · Replace · Remove · Keep Anyway
```

---

## 2. Bad Image Found During Entry

Operator selects a problem type:

```text
Image Too Blurry
Image Cut Off
Wrong Page
Duplicate Image
Page Blank
Other Problem
```

Then:

```text
Send Back for Image Review
```

Page leaves entry queue → exception / image review queue.

---

## 3. Partially Readable Page

Enter readable people. Mark unreadable fields or rows. Submit with Needs Review when required.

---

## 4. Entire Page Unreadable

```text
Mark Page Unreadable
```

Reason required. Admin/uploader may later replace image.

---

## 5. Correction (Return from Matching)

Reviewer returns entry or page with reason:

```text
Name appears mistyped
Phone entered on wrong row
ZIP is unreadable
Entry omitted
Duplicate entry created
Wrong Yes/No selection
Other
```

Data entry sees:

```text
Corrections Assigned to Me
```

Flow after fix:

```text
Review Correction → Resubmit → Resume Matching
```

Audit records original and corrected values.

---

## 6. Claim Exceptions

| Situation | Behavior |
| --- | --- |
| Expiring soon | 5-minute warning + Continue Working |
| Expired, unclaimed | Reclaim Page |
| Expired, reclaimed by other | Block overwrite; preserve draft for admin |
| Admin reassign | Preserve draft; reason; in-app notice |
| Double submit | Idempotent; no duplicate page completion |

---

## 7. Upload Exceptions

| Situation | Behavior |
| --- | --- |
| One page fails | Others continue; retry failed |
| Partial batch success | Batch Needs Attention until failures resolved |
| Offline capture | Local pending; not marked uploaded |

---

## 8. Matching Exceptions

| Situation | Behavior |
| --- | --- |
| Conflict | Human review required |
| Reviewer disagrees with suggestion | Choose Different Match / Create New / Return |
| Field conflicts | Explicit per-field decision UI |
| Page returned after matching began | Matching pauses; resumes after resubmit |

---

## 9. Access Exceptions

| Situation | Behavior |
| --- | --- |
| Access denied | Clear Access Denied screen |
| Account disabled mid-session | Block further writes; preserve local draft if possible; require admin |
| Session expired | Sign-in again; resume if claim still valid |

---

## 10. Image Access Exceptions

Signed viewing URL expired → refresh signed URL through authorized server path; never fall back to public URL.

---

## 11. Stuck / Inactive Batches

Admin overview surfaces aging and Needs Attention. Admin may pause, prioritize, reassign, or archive per policy.

---

## 12. Administrator Exception Powers

- Find stuck pages
- See assigned user and claim age
- Release or reassign
- Preserve drafts
- View audit history
- Resolve upload failures and unreadable pages
