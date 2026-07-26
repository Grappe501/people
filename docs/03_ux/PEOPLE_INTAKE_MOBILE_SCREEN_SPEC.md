# People Intake — Mobile Screen Spec

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-WORKFLOW-UX-DESIGN-1.0  
**Viewport focus:** Phone portrait first; landscape supported

---

## Global Mobile Rules

- One dominant primary action per screen
- Bottom or hamburger nav with ≤5 destinations
- Large touch targets
- Save status always visible during editing
- Prefer stacked layouts; no ten-column spreadsheets on phone

---

## Auth

### Sign In

Brand + short promise + Continue with Google + approved-users note.

### Access Denied / Account Disabled / Session Expired

Plain explanation + next step (contact admin / sign in again).

---

## Capture Screens

### Uploader Home

Primary stack: Take Pictures, Upload From Device, Resume Upload. Recent Batches below.

### New Batch

Single-column form. Strong emphasis on Source/Event Name. Suggested batch name editable. Continue to capture.

### Camera Capture

Full-bleed camera. Retake / Accept / Finish. Page counter. Stay in camera until Finish.

### Select Images

Multi-select gallery; show count; Continue to review.

### Review Images

Vertical thumbnail list with page #, rotate, delete, replace, reorder handles, expand. Primary: Upload N Pages.

### Upload Progress

List of pages with Waiting/Uploading/Uploaded/Retry Needed. Retry on failures.

### Upload Complete

Success copy + Upload Another / View Batch / Done.

### My Batches / Batch Detail

Cards with name, page counts, status. Detail shows thumbnails and upload outcomes only — not person PII grids.

---

## Transcription Screens

### Data Entry Home

Metrics + Claim Next Page. Resume banner if active draft.

### Shared Queue

Compact cards: batch, page, wait time, status, assignee. Still emphasize Claim Next Page.

### Page Workspace (Mobile)

```text
Sticky header (batch, page x of y, people entered)
Image viewer (~40–50% height)
Person progress
Current person form
Completed people summaries
Page actions
Save status
```

### Mobile Person Entry

Fields in order: Last, First, Email, Phone, ZIP, Volunteer Yes/No/Blank, Email List Yes/No/Blank.  
Primary: Save Person & Continue.  
After save: Add Another Person / Finish Page.

### Completed Summary Row

```text
1. Grappe, Kelly
501-555-1212 · 72076
Volunteer: Yes · Email List: Yes
[Edit] [Remove]
```

### Full-Screen Image Viewer

Immersive image + close returns to same zoom/pan. Brightness/contrast viewing aids optional.

### Page Review

Scrollable list of people + warnings. Primary: Submit Page & Open Next. Secondary: Return to Entry / Submit & Return to Queue.

### Page Submitted

Brief confirmation + Opening next page…

### My Work / Correction Queue

Lists of active, recent, and returned pages with reasons.

---

## Matching Screens (Phone)

### Reviewer Home

Counts + Review Next Match.

### Match Workspace

Vertical sections: source image (collapsible/expandable), new entry, suggested person, reasons, other candidates, actions.

### Field Conflict Review

Stacked field cards with Existing / New / decision controls.

### Match Complete / Deferred

Short confirmation; auto-advance to next match when appropriate.

---

## Admin on Phone

Functional but dense: prefer cards and filters over wide tables. Full admin tables optimize for tablet/desktop.

---

## Shared Mobile

Help, Notifications, Account, Offline State, General Error — single column, clear recovery actions.
