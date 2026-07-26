# People Intake — Content and Copy Guide

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-WORKFLOW-UX-DESIGN-1.0

---

## Voice

Plain, calm, operational. Short sentences. Tell the user what to do next.

---

## Preferred Terms

| Use | Avoid |
| --- | --- |
| Volunteer Sheet | Form artifact |
| Page | Work item / entity |
| Person | Record instance |
| Possible Match | Candidate object |
| Needs Review | Pending resolution |
| Blank | Null / unset (in UI) |
| Unreadable | Illegible glyph |
| Not Provided | Empty string |

---

## Primary Action Labels (Locked Intent)

```text
Take Pictures
Upload From Device
Upload Batch / Upload N Pages
Claim Next Page
Save Person & Continue
Add Another Person
Finish Page
Review Page
Submit Page & Open Next
Submit Page & Return to Queue
Save & Release Page
Link to Existing Person
Create New Person
Review Next Match
Continue Working
Reclaim Page
Send Back for Image Review
Mark Page Unreadable
```

---

## Status Copy

### Save

```text
Saving…
Saved
Offline — changes stored on this device
Save failed — retrying
```

### Upload

```text
Waiting
Uploading
Uploaded
Retry Needed
Uploading Page 4 of 12
```

### Claim

```text
This page is assigned to you.
Your page will be released in 5 minutes.
Continue Working
```

### Submit

```text
Page Submitted
8 people entered
Opening next page…
```

### Match explanations intro

```text
Why this may be the same person
```

---

## Onboarding Snippets

### Uploader

```text
Your job is to photograph or upload clear volunteer sheets.
Office staff will enter the handwritten information later.
```

### Data Entry

```text
Your job is to enter every person shown on one volunteer sheet.
The system will save your work automatically.
```

### Reviewer

```text
Your job is to resolve possible matches and confirm whether each entry belongs to an existing person.
```

---

## Warning Copy Examples

```text
Email may be incomplete
Phone has fewer than 10 digits
ZIP may be incomplete
Volunteer response is blank
Possible duplicate on this page
Unreadable field
```

---

## Notifications (In-App)

```text
Your batch finished uploading.
A page was returned for correction.
Your claim will expire soon.
This page was reassigned.
Batch Greene County Meeting is complete.
```

---

## Help Titles

```text
How to photograph a readable page
How to mark unreadable or missing fields
How to decide whether two records are the same person
```

---

## Sign-In

```text
People Intake
Secure volunteer-sheet entry
Continue with Google
Only approved users may access this system.
```

---

## Rules

1. No jargon in routine UI.
2. Internal enum names stay in admin diagnostics only.
3. Never imply Blank means No.
4. Never claim upload/submit succeeded until it did.
5. Always name the next action in empty/error states.
