# People Intake — Transcription Workflow

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-WORKFLOW-UX-DESIGN-1.0  
**Workspace:** TRANSCRIBE  
**Primary role:** Data Entry Operator

---

## Purpose

Define how office users claim a page, enter up to ten people, review, submit, and automatically continue — without matching interruptions.

---

## Operating Goal

```text
Claim page
→ Read page
→ Enter up to ten people
→ Review the page
→ Submit the page
→ Continue automatically
```

---

## End-to-End Flow

```text
Data Entry Home
→ Claim Next Page (atomic)
→ Page Workspace opens
→ Enter people (mobile: one at a time; desktop/tablet: grid)
→ Autosave throughout
→ Review Page
→ Submit Page & Open Next
→ Page Submitted confirmation
→ Next page opens (or queue if none)
```

---

## 1. Data Entry Home

Show:

```text
Ready for Entry: 42 pages
My Active Page: 1
Completed Today: 8 pages
```

Primary:

```text
Claim Next Page
```

Secondary:

```text
Resume My Page · View Queue · Recent Work
```

If unfinished work exists, surface it first:

```text
Resume Page
7 of 10 entries entered
Last saved 14 minutes ago
```

---

## 2. Claim Next Page

Atomic assignment. Selection order:

1. Highest-priority batch
2. Oldest ready page
3. Lowest page sequence within the batch

No extra confirmation tap. Status:

```text
This page is assigned to you.
```

Manual queue selection is available only when needed; default remains Claim Next Page.

---

## 3. Page Workspace Components

1. Page status header
2. Image viewer
3. Entry progress
4. Person-entry interface
5. Completed-person summaries
6. Page actions
7. Save status

Header example:

```text
Greene County Volunteer Sheets
Page 3 of 14
0 of 10 people entered
```

---

## 4. Mobile Entry (One Person at a Time)

Layout:

```text
Header
Image Viewer
Person Progress
Current Person Form
Completed People
Page Actions
```

Form order:

```text
Last Name
First Name
Email
Phone
ZIP Code
Volunteer: Yes | No | Blank
Email List: Yes | No | Blank
```

Primary person action:

```text
Save Person & Continue
```

Effects:

1. Save person
2. Collapse to summary
3. Open next person form
4. Focus Last Name
5. Keep image zoom position

After each save (when under ten):

```text
Add Another Person · Finish Page
```

At ten:

```text
Maximum of 10 people entered
Review Page
```

---

## 5. Tablet / Desktop Entry (Grid)

Ten available rows. Blank rows ignored on submit.

Columns:

| # | Last | First | Email | Phone | ZIP | Volunteer | Email List | Status |

Keyboard: Tab horizontal; Enter may advance row; Yes/No/Blank keyboard accessible.

Sticky controls:

```text
Save Draft · Review Page · Release Page
```

Layout: image left or top; grid right or bottom.

---

## 6. Field Semantics (Operator-Facing)

- Preserve raw typing; trim surrounding spaces on names
- Email lowercase normalize for matching later; keep raw
- Phone visual format; keep raw; digit normalize later
- Warnings do not hard-block submission
- Field options: **Not Provided** and **Unreadable** (distinct)
- Blank Yes/No remains Blank (`UNKNOWN`), never silent No

---

## 7. Draft Saving

Triggers: field completion, Yes/No/Blank, save person, before fullscreen image, focus loss, active intervals, before release.

Indicators:

```text
Saving…
Saved
Offline — changes stored on this device
Save failed — retrying
```

---

## 8. Page Review

Shows all entered people with warnings:

```text
Email may be incomplete
Phone has fewer than 10 digits
ZIP may be incomplete
Volunteer response is blank
Possible duplicate on this page
Unreadable field
```

Warnings do not automatically block submission.

Blocking errors include: >10 entries, corrupted draft, lost claim, administrative reassignment, missing internal IDs.

Final actions:

```text
Return to Entry
Submit Page & Open Next   ← primary default
Submit Page & Return to Queue
```

---

## 9. Submission Side Effects

1. Verify claim ownership
2. Save all page entries as unique records
3. Preserve raw values
4. Create normalized values
5. Mark transcription complete
6. Start matching evaluation
7. Create audit events
8. Release operator claim
9. Update batch progress
10. Open next page when requested

User sees:

```text
Page Submitted
8 people entered
Opening next page…
```

---

## 10. Image Problems Mid-Entry

Operator may mark:

```text
Image Too Blurry · Image Cut Off · Wrong Page · Duplicate Image · Page Blank · Other Problem
```

Then:

```text
Send Back for Image Review
```

Or:

```text
Mark Page Unreadable
```

(reason required). Readable people may still be entered; page can submit with Needs Review.

---

## 11. Success Criteria

A new data-entry worker can claim, zoom, enter seven people, correct one, mark one field unreadable, submit, and automatically open the next page.
