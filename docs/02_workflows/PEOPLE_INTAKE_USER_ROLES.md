# People Intake — User Roles

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-WORKFLOW-UX-DESIGN-1.0  
**Governs:** Role definitions, home experiences, permission intent  
**Related:** `PEOPLE_INTAKE_AUTHORIZATION_MATRIX.md` (later security lock)

---

## Purpose

Define who uses People Intake, what each role is responsible for, and what each role must never be asked to do.

---

## Workspaces by Role

| Role | Primary workspace | Also may use |
| --- | --- | --- |
| Field Uploader | CAPTURE | Help, Account, My Batches |
| Data Entry Operator | TRANSCRIBE | Corrections, Queue (view), Help, Account |
| Matching Reviewer | MATCH | Needs Correction (return), Help, Account |
| Administrator | MANAGE | All workspaces as needed |
| Owner | MANAGE + governance | All workspaces; policy authority |

---

## 1. Field Uploader

### Mission

Capture readable volunteer sheets, group them into a batch, provide basic source information, and upload successfully.

### Must do

- Create batches
- Photograph or select images
- Review orientation and readability before upload
- Replace or remove bad images before upload completes
- View batches they uploaded

### Must not be required to

- Read handwriting into the database
- Enter people
- Resolve duplicates
- Understand the canonical people database
- Perform matching review

### Home emphasis

```text
Take Pictures
Upload From Device
Resume Upload
Recent Batches
```

### Navigation

```text
Home · Upload Sheets · My Batches · Help · Account
```

---

## 2. Data Entry Operator

### Mission

Claim a page, read the sheet, enter every visible person (up to ten), review, submit, and continue.

### Must do

- Claim next available page
- Transcribe up to ten people
- Mark fields Not Provided or Unreadable
- Save drafts
- Submit pages
- Resume own claimed work
- Release a page when needed
- Correct pages returned to them

### Must not be required to

- Resolve uncertain person matches
- Merge canonical people
- Delete source images
- Raise batch priority
- Edit another user’s active claim

### Home emphasis

```text
Claim Next Page
Resume My Page
View Queue
Recent Work
```

### Navigation

```text
Home · Enter Sheets · My Work · Queue · Help · Account
```

---

## 3. Matching Reviewer

### Mission

Resolve entries that cannot be confidently linked automatically: possible matches, conflicts, and related review work.

### Must do

- Review next unresolved match
- Compare intake entry to existing people
- Link to existing or create new person
- Resolve field conflicts within approved rules
- Return pages/entries for correction with reason
- Defer review when needed

### Must not be required to

- Capture field images as their primary job
- Invent missing handwritten values
- Silently overwrite intake evidence

### Home emphasis

```text
Review Next Match
Possible Matches
Conflicts
Needs Correction
Completed Today
```

### Navigation

```text
Home · Match People · Needs Correction · Completed · Help · Account
```

---

## 4. Administrator

### Mission

Keep the shared queue healthy, resolve exceptions, manage users, and oversee operational correctness.

### Must do

- View operational overview
- Change batch priority
- Release/reassign claims
- Manage exception queues
- Invite and assign roles
- Disable access
- View full audit history
- Correct batch metadata
- Pause or archive batches within policy

### Must not (without Owner)

- Change retention policy
- Unrestricted source-image deletion outside restricted admin procedures
- Alter shared-database contracts

### Navigation

```text
Overview · Batches · Queue · Matching · Exceptions · Users · Audit · Settings
```

---

## 5. Owner

### Mission

Govern application-wide authority: administrators, retention, production configuration, shared-database contracts, sensitive deletion, and design/governance approvals.

### Additional authority

- Approve retention and deletion policies
- Approve production integrations
- Approve database-contract changes
- Manage administrator access

---

## Role Combinations

A single person may hold more than one role. The interface should show the union of authorized actions, still organized by workspace so the next job remains obvious.

---

## Provisional Permission Matrix

| Action | Uploader | Data Entry | Reviewer | Admin | Owner |
| --- | ---: | ---: | ---: | ---: | ---: |
| Create batch | Yes | Optional | No | Yes | Yes |
| Upload pages | Yes | Optional | No | Yes | Yes |
| Claim page | No | Yes | No | Yes | Yes |
| Transcribe page | No | Yes | Optional | Yes | Yes |
| Resolve possible match | No | No | Yes | Yes | Yes |
| Create canonical person through intake | No | No | Yes | Yes | Yes |
| Reassign page | No | No | No | Yes | Yes |
| Manage users | No | No | No | Yes | Yes |
| Change retention policy | No | No | No | No | Yes |
| Delete source image | No | No | No | Restricted | Yes |
| View audit history | Limited | Limited | Limited | Yes | Yes |

Final security lock occurs in the authorization matrix design phase. This matrix defines intended operating permissions for UX and workflow design.
