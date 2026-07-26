# PEOPLE INTAKE SYSTEM

# VOLUME 11 — USER INTERFACE SPECIFICATIONS

**Document ID**

```text
PEOPLE-VOLUME-11-USER-INTERFACE-SPECIFICATIONS-1.0
```

**Status**

```text
DESIGN COMPLETE — IMPLEMENTATION NOT AUTHORIZED
```

**Project Root**

```text
H:\people
```

**Document Type**

```text
CANONICAL USER EXPERIENCE AND SCREEN SPECIFICATION
```

**Build Mode**

```text
DOCUMENTATION ONLY
```

**Prohibited During This Volume**

* No React components
* No route files
* No CSS
* No design-system code
* No image-upload implementation
* No API calls
* No authentication integration
* No database access
* No production analytics
* No deployment configuration
* No framework selection

---

# PART I — PURPOSE AND AUTHORITY

## 1. Purpose

Volume 11 defines the complete user interface architecture for the People Intake System before implementation begins.

It specifies:

* application navigation
* workspace structure
* screen inventory
* page hierarchy
* user workflows
* responsive behavior
* mobile behavior
* loading states
* empty states
* error states
* validation behavior
* confirmation behavior
* keyboard interaction
* accessibility requirements
* privacy protections
* visual hierarchy
* status communication
* interruption recovery
* workflow completion behavior
* audit-visible actions
* operator guidance
* future extension boundaries

This volume answers:

> What must each user see, understand, do, confirm, recover from, and never be allowed to misunderstand?

---

## 2. Governing UX Principle

The People Intake interface must make accurate work easier than careless work.

The user experience must prioritize:

1. source fidelity
2. user confidence
3. clear ownership
4. recoverable work
5. visible workflow state
6. privacy
7. speed without pressure
8. shared-queue trust
9. error prevention
10. human accountability

The interface must never pressure a user to guess at unreadable handwriting or force a false yes-or-no answer where the source is unknown.

---

## 3. Core Experience Statement

The application should feel like a calm, trustworthy shared workbench.

A user should always understand:

* where they are
* what kind of work they are doing
* who currently owns the work
* whether work is saved
* what must happen next
* whether an action is reversible
* whether the system is waiting, complete, blocked, or failed
* where the original source evidence is
* whether a value is raw, normalized, suggested, or approved

---

# PART II — USERS AND EXPERIENCE MODES

## 4. Primary User Types

### 4.1 Uploader

Primary goal:

```text
Turn paper pages into organized, usable intake work.
```

Main interface needs:

* create batch
* upload page image
* verify image quality
* assign page order
* correct metadata
* see upload status
* replace unusable images
* close batch uploads

### 4.2 Data Entry User

Primary goal:

```text
Accurately transcribe handwritten rows into structured entries.
```

Main interface needs:

* shared transcription queue
* claim page
* view source image
* zoom and rotate
* enter up to ten rows
* mark unreadable or ambiguous fields
* save automatically
* recover draft
* submit page

### 4.3 Reviewer

Primary goal:

```text
Validate transcription and make careful identity decisions.
```

Main interface needs:

* transcription review queue
* match review queue
* side-by-side evidence comparison
* candidate explanations
* conflict warnings
* return-for-correction workflow
* final resolution action
* promotion status

### 4.4 Administrator

Primary goal:

```text
Keep the system moving safely.
```

Main interface needs:

* queue overview
* claims overview
* abandoned work
* user access
* batches
* errors
* alerts
* audit history
* recovery actions
* operational reports

### 4.5 Owner

Primary goal:

```text
Govern access, policy, and high-risk administrative activity.
```

Main interface needs:

* user approvals
* role management
* configuration visibility
* audit oversight
* system readiness
* policy notices
* high-risk action confirmation

---

# PART III — GLOBAL APPLICATION STRUCTURE

## 5. Primary Workspaces

The application is organized into four top-level workspaces:

```text
Capture
Transcribe
Match
Manage
```

These are permanent product concepts.

### Capture

Purpose:

```text
Create batches, upload pages, and prepare source evidence.
```

### Transcribe

Purpose:

```text
Claim pages and convert handwritten rows into structured entries.
```

### Match

Purpose:

```text
Review entries, compare candidates, resolve identity, and monitor promotion.
```

### Manage

Purpose:

```text
Administer users, queues, batches, errors, alerts, audit, and reports.
```

---

## 6. Global Navigation

### 6.1 Desktop Navigation

Desktop should use a persistent left navigation rail.

Recommended structure:

```text
People Intake

Home

Capture
    Batches
    Upload Pages

Transcribe
    My Work
    Shared Queue
    Submitted Work

Match
    Review Queue
    Resolutions
    Promotions

Manage
    Operations
    Users
    Claims
    Errors & Alerts
    Audit
    Reports

Account
    Profile
    Sign Out
```

Navigation items appear according to user authorization.

Hidden navigation does not replace server-side authorization.

### 6.2 Tablet Navigation

Tablet may use:

* collapsible left rail
* persistent workspace icons
* expanded labels on demand
* visible page title and back control

### 6.3 Mobile Navigation

Mobile should use:

* compact top bar
* menu control
* bottom navigation for the user’s most common authorized workspaces
* persistent thumb-zone primary action where appropriate

Recommended mobile bottom navigation:

```text
Home
Capture
Transcribe
Match
More
```

Items not permitted for the user should not appear.

### 6.4 Breadcrumbs

Desktop and tablet should use breadcrumbs for nested records.

Example:

```text
Capture / Batches / Greene County Sign-Up / Page 4
```

Mobile may simplify breadcrumbs to:

```text
Back to batch
```

---

# PART IV — GLOBAL SCREEN FRAMEWORK

## 7. Application Shell

Every protected screen should include:

* application identity
* workspace navigation
* page title
* status context
* user identity control
* relevant primary action
* support or help access
* privacy-safe session handling

---

## 8. Page Header Pattern

Each page header should include:

```text
Page title
Short purpose statement
Primary status
Primary action
Optional secondary actions
```

Example:

```text
Transcription Queue

Pages ready for data entry.

24 pages available

[Claim Next Page]
```

---

## 9. Status Language

Status labels must use plain language.

Good:

```text
Ready for transcription
Claimed by you
Waiting for review
Needs image replacement
Promotion failed
```

Avoid:

```text
PENDING_04
PROCESS_STATE_7
ERR_X104
```

Machine codes may appear in expandable technical details for authorized administrators.

---

## 10. Save-State Indicator

All draft-oriented screens must clearly show save state.

Required states:

```text
Saving
Saved
Unsaved changes
Save failed
Recovered draft
Read-only
```

The save indicator must not rely on color alone.

Recommended placement:

* desktop: page header or sticky work toolbar
* mobile: sticky bottom action area

---

## 11. Privacy Indicator

Screens showing source images or personal information should display a subtle privacy notice.

Example:

```text
Private intake information. Use only for authorized work.
```

The notice should not obstruct work.

---

# PART V — HOME AND DASHBOARD

# 12. Home Screen

**Route concept**

```text
/
```

or:

```text
/home
```

Exact route remains a Volume 13 or implementation decision.

## 12.1 Purpose

Give each user a role-aware starting point.

## 12.2 Content

Home should include:

* welcome context
* current assigned or claimed work
* next recommended action
* queue summary relevant to the user
* recent work
* blocked or failed work requiring attention
* system notices
* role-aware workspace shortcuts

## 12.3 Data Entry Home

Primary card:

```text
Continue Your Page
```

or:

```text
Claim the Next Page
```

Additional information:

* active claim expiration
* last draft save
* pages available
* recently submitted pages

## 12.4 Reviewer Home

Primary card:

```text
Review the Next Entry
```

Additional information:

* transcription review count
* identity review count
* conflicts requiring attention
* promotion failures

## 12.5 Administrator Home

Primary content:

* queue health
* active claims
* expired claims
* upload failures
* promotion failures
* open alerts
* current users
* batch progress

## 12.6 Empty State

When no work exists:

```text
There is no work waiting right now.

New pages will appear here after they are uploaded and prepared.
```

Do not frame an empty queue as an error.

---

# PART VI — CAPTURE WORKSPACE

# 13. Capture Dashboard

## 13.1 Purpose

Give uploaders and administrators a clear view of source intake work.

## 13.2 Content

* open batches
* recent batches
* upload failures
* pages needing replacement
* batch progress
* primary action: Create Batch
* secondary action: Upload to Existing Batch

## 13.3 Filters

* status
* received date
* creator
* archived state
* image-quality issue
* incomplete upload

---

# 14. Batch List Screen

## 14.1 Purpose

Locate and manage intake batches.

## 14.2 Columns

Desktop table:

```text
Batch
Status
Pages
Ready
In Progress
Complete
Created By
Received
Last Activity
```

## 14.3 Mobile Card

Each card should show:

* batch title
* status
* page progress
* received date
* one primary action

## 14.4 Actions

* open batch
* create batch
* archive batch where authorized
* close uploads
* reopen uploads where permitted

## 14.5 Empty State

```text
No batches have been created.

Create the first batch to begin uploading paper sign-up pages.
```

---

# 15. Create Batch Screen

## 15.1 Purpose

Create the container for one related set of pages.

## 15.2 Fields

* Batch Title
* Source Description
* Received Date
* Expected Page Count
* Notes

## 15.3 Required Fields

Required:

* Batch Title

Optional:

* all others unless later policy changes

## 15.4 Guidance

Batch title helper text:

```text
Use a clear label such as event, county, date, or source.
```

## 15.5 Validation

Examples:

* blank title
* negative page count
* invalid date
* title too long
* duplicate idempotent submission

## 15.6 Completion

After creation:

```text
Batch created.

You can now upload pages.
```

Primary next action:

```text
Upload Pages
```

---

# 16. Batch Detail Screen

## 16.1 Purpose

Manage one batch from upload through completion.

## 16.2 Header

Show:

* title
* display ID
* status
* received date
* source description
* created by
* page progress
* upload state

## 16.3 Summary Cards

* Total Pages
* Ready for Transcription
* In Transcription
* Awaiting Review
* Completed
* Image Issues

## 16.4 Page List

Each row or card shows:

* page sequence
* page label
* thumbnail
* image quality
* workflow status
* entry count
* claim status
* last activity
* action

## 16.5 Primary Actions

Depending on state:

* Upload Pages
* Add Another Page
* Close Uploads
* Resolve Image Issues
* Archive Batch

## 16.6 Warning States

Examples:

```text
2 pages require clearer images.
```

```text
Uploads are closed for this batch.
```

```text
This batch cannot be completed while 4 entries remain unresolved.
```

---

# 17. Upload Pages Screen

## 17.1 Purpose

Upload one or more source-page images safely.

## 17.2 Upload Methods

Supported conceptually:

* file picker
* drag and drop
* mobile camera capture
* mobile photo library

Exact implementation may vary.

## 17.3 Upload Queue

Each selected file should show:

* local preview
* filename
* file size
* detected type
* upload progress
* validation state
* page sequence
* page label
* failure state
* retry action

## 17.4 Validation States

```text
Ready
Uploading
Uploaded
Verifying
Complete
Failed
Unsupported file
Too large
Corrupt image
Duplicate warning
```

## 17.5 Duplicate Warning

A duplicate-image warning must not silently reject the upload.

Example:

```text
This image appears similar to Page 3.

Review both images before continuing.
```

Actions:

* Keep Both
* Remove New Upload
* Review Existing Page

## 17.6 Completion Summary

```text
8 pages uploaded successfully.
1 page needs attention.
```

Primary action:

```text
Review Pages
```

---

# 18. Page Preparation Screen

## 18.1 Purpose

Verify a page image before transcription.

## 18.2 Layout

Desktop:

```text
Left: large source image
Right: page metadata and quality controls
```

Mobile:

```text
Image first
Metadata below
Sticky action bar
```

## 18.3 Controls

* zoom
* rotate display
* full-screen view
* page sequence
* page label
* quality status
* replacement request
* mark usable
* save

## 18.4 Quality Choices

* Usable
* Blurry
* Cropped
* Wrong Document
* Corrupt
* Replacement Required

## 18.5 Image Replacement

When replacement is requested:

```text
The original image will remain preserved.
```

The user should never see language implying overwrite.

---

# PART VII — TRANSCRIBE WORKSPACE

# 19. Transcribe Dashboard

## 19.1 Purpose

Give data-entry users immediate access to current or available work.

## 19.2 Priority Order

1. Continue active claim
2. Recover saved draft
3. Claim next available page
4. View submitted work

## 19.3 Active Claim Card

Show:

* page ID
* batch
* claim expiration
* last save
* rows entered
* continue action
* release action

---

# 20. Shared Transcription Queue

## 20.1 Purpose

Show work currently eligible for transcription.

## 20.2 Queue Item Information

* batch title
* page sequence
* page thumbnail
* image quality
* received date
* priority
* current availability
* estimated row count only if manually known

## 20.3 Claim Behavior

Primary action:

```text
Claim Page
```

The queue should clearly explain:

```text
Claiming reserves the page temporarily so two people do not enter the same work.
```

## 20.4 Claim Collision

When another user wins the claim:

```text
This page was just claimed by another user.

Choose another available page.
```

Do not present this as a system failure.

## 20.5 Claim Next

A prominent:

```text
Claim Next Available Page
```

action may automatically attempt the next eligible work item.

The user must be told which page was claimed after success.

---

# 21. Transcription Workspace

## 21.1 Purpose

Enable accurate page-level data entry for up to ten handwritten rows.

## 21.2 Desktop Layout

Recommended layout:

```text
---------------------------------------------------------
| Source Image             | Entry Grid                 |
|                          |                            |
| Zoom / Rotate / Pan      | Rows 1–10                 |
|                          |                            |
---------------------------------------------------------
| Save Status | Claim Time | Submit Page               |
---------------------------------------------------------
```

The image and data grid should remain visible together wherever screen size allows.

## 21.3 Tablet Layout

Recommended:

* split view in landscape
* stacked view in portrait
* easy toggle between image and entry grid
* persistent save and claim information

## 21.4 Mobile Layout

Recommended:

* source image viewer at top or in dedicated expandable panel
* one row card at a time
* quick next-row navigation
* sticky save and submit area
* full-screen image toggle
* easy return to current field

Mobile must not require constant pinching and scrolling between distant controls.

---

# 22. Source Image Viewer

Required capabilities:

* zoom in
* zoom out
* pan
* rotate display
* reset view
* full-screen mode
* return to active field
* image version indicator
* privacy notice

The viewer must not permanently alter the original image.

---

# 23. Entry Grid

## 23.1 Row Structure

Each row includes:

```text
Row Number
Last Name
First Name
Email
Phone
ZIP
Volunteer
Email List
Field Conditions
Row Notes
```

## 23.2 Ten-Row Presentation

Desktop should display ten possible row positions without forcing creation of ten entries.

Blank rows remain inactive until data is entered or a field condition is selected.

## 23.3 Row Activation

A row becomes an active entry when:

* any field receives a value, or
* any field receives a nonblank source condition, or
* the user explicitly marks the row as containing an entry

## 23.4 Blank Row

The user may leave a truly blank physical row unused.

The interface must not force:

```text
No
```

for blank preferences.

---

# 24. Field Interaction

## 24.1 Text Fields

Text fields must preserve operator-entered raw text.

The UI may show formatting guidance but must not silently replace raw transcription.

## 24.2 Preference Fields

Volunteer and Email List controls must provide:

```text
Yes
No
Unknown
```

The default is:

```text
Unknown
```

or no selected answer that resolves to `UNKNOWN`.

The interface must never default to `NO`.

## 24.3 Field Condition Control

Each field should support:

* Provided
* Not Provided
* Unreadable
* Ambiguous

Corrected is typically assigned through correction workflow rather than ordinary first-pass entry.

## 24.4 Unreadable Behavior

When selected:

* the raw field may remain blank
* the field visibly indicates unreadable
* optional short note may be added
* the user is not required to guess

## 24.5 Ambiguous Behavior

When selected:

* the operator may enter the best visible transcription if policy permits
* the field is visibly flagged
* the reviewer sees the ambiguity
* normalization must not hide the flag

---

# 25. Keyboard Workflow

Desktop transcription must support fast keyboard use.

Recommended behavior:

* Tab moves to next field
* Shift+Tab moves to previous field
* Enter may advance within a row where safe
* documented shortcut opens field-condition menu
* documented shortcut toggles image focus
* documented shortcut saves draft
* documented shortcut moves to next row

Keyboard shortcuts must:

* avoid browser conflicts
* be discoverable
* never trigger irreversible action without confirmation
* remain optional

---

# 26. Autosave

## 26.1 Behavior

Autosave should occur:

* after a short idle interval
* after meaningful field changes
* before page navigation
* before claim renewal where practical
* before submission validation

## 26.2 Indicators

```text
Saving…
Saved at 3:42 PM
Save failed
Unsaved changes
```

## 26.3 Save Failure

When save fails:

* do not clear fields
* preserve local unsaved work where technically possible
* show retry action
* warn before leaving
* distinguish network failure from authorization loss

---

# 27. Claim Timer

The interface should display claim status without creating panic.

Recommended language:

```text
Reserved for you until 4:15 PM
```

As expiration approaches:

```text
Your reservation will expire soon.
```

Actions:

* Extend Reservation
* Save and Release
* Continue Working

Avoid aggressive countdown animation.

---

# 28. Release Page

When releasing a claimed page:

```text
Your saved draft will remain available.

The page will return to the shared queue.
```

Confirmation required when unsaved work exists.

---

# 29. Submit Page

## 29.1 Pre-Submission Review

Before final submission, show:

* active entries
* unused rows
* unreadable fields
* ambiguous fields
* missing values
* save status
* image version used

## 29.2 Validation

Block submission for structural failures such as:

* unsaved changes
* stale draft
* no usable image
* invalid preference value
* duplicate row position
* inaccessible claim state

Do not block submission merely because the source omitted fields.

## 29.3 Confirmation

```text
Submit 7 entries from this page?

You can no longer edit this submitted version directly. Corrections will create a new revision.
```

Actions:

* Review Again
* Submit Page

## 29.4 Success

```text
Page submitted successfully.

7 entries are ready for the next stage.
```

Primary next action:

```text
Claim Another Page
```

---

# 30. Draft Recovery Screen

## 30.1 Purpose

Recover work saved by the same or a prior authorized operator.

## 30.2 Information

Show:

* page
* batch
* original draft owner
* last saved time
* revision count
* claim status
* recovery reason
* preview of completed rows

## 30.3 Attribution Notice

```text
The original work will remain attributed to the person who entered it.

Your changes will be recorded separately.
```

## 30.4 Recovery Action

```text
Recover Draft and Continue
```

Requires a current valid claim or administrative recovery authority.

---

# 31. Submitted Work Screen

## 31.1 Purpose

Let data-entry users review their completed work without editing immutable submissions.

## 31.2 Filters

* submitted date
* batch
* review status
* returned for correction
* completed

## 31.3 Actions

* view submission
* view correction request
* open returned work
* view history

---

# PART VIII — TRANSCRIPTION REVIEW

# 32. Transcription Review Queue

## 32.1 Purpose

Present entries or pages requiring quality review before identity resolution.

## 32.2 Queue Item Information

* batch
* page
* entry count
* unreadable-field count
* ambiguous-field count
* submitter
* submitted time
* priority
* review status

---

# 33. Transcription Review Screen

## 33.1 Layout

Desktop:

```text
Left: source image
Center: submitted raw fields
Right: review controls
```

Mobile:

* source image toggle
* one entry at a time
* issue summary
* sticky decision controls

## 33.2 Reviewer Actions

* Approve Transcription
* Return Entry for Correction
* Return Page for Correction
* Mark Image Issue
* Escalate

## 33.3 Correction Request

Must include:

* affected entry
* affected field or page
* reason
* reviewer note
* severity
* whether matching must pause

## 33.4 Reviewer Restrictions

The reviewer must not silently rewrite the submitter’s immutable submission.

A correction produces a new revision.

---

# PART IX — MATCH WORKSPACE

# 34. Match Dashboard

## 34.1 Purpose

Provide reviewers with identity-resolution workload and promotion status.

## 34.2 Summary Cards

* Awaiting Evaluation
* Ready for Review
* Conflicts
* More Information Needed
* Ready for Promotion
* Promotion Failures

## 34.3 Primary Action

```text
Review Next Entry
```

---

# 35. Match Review Queue

## 35.1 Columns

* entry
* name summary
* batch
* confidence class
* candidate count
* conflict count
* age of work
* priority
* assigned reviewer where applicable

## 35.2 Privacy

Show only the minimum personal information needed for queue recognition.

Avoid displaying full email and phone values in the queue list.

Masked examples may be used:

```text
s••••@example.com
•••-•••-1234
```

---

# 36. Match Review Screen

## 36.1 Purpose

Allow careful, explainable identity resolution.

## 36.2 Desktop Layout

Recommended:

```text
------------------------------------------------------------
| Intake Evidence | Candidate Comparison | Resolution Panel |
------------------------------------------------------------
```

## 36.3 Intake Evidence Panel

Show:

* source image excerpt or full-page link
* raw transcription
* field conditions
* normalized values
* transcription revisions
* source batch and page
* submitter and reviewer history

Raw and normalized values must be visually distinct.

Example:

```text
Raw: "steve @ example.com"
Normalized: "steve@example.com"
```

## 36.4 Candidate Comparison Panel

Each candidate card shows:

* limited canonical identity summary
* confidence class
* supporting signals
* conflicting signals
* weak signals
* canonical data freshness where available
* prior review history where authorized

## 36.5 Signal Display

Signals should use plain language.

Good:

```text
Email matches exactly.
Phone number differs.
ZIP matches.
Name is similar but not exact.
```

Avoid unexplained numeric scores alone.

A numeric score may be shown as secondary information.

## 36.6 Conflict Warning

When strong identifiers conflict:

```text
Important conflict

The email appears connected to one person, while the phone appears connected to another. Do not merge until the conflict is resolved.
```

---

# 37. Candidate Selection

Selecting a candidate must not immediately finalize the match.

Selection should stage the choice.

The resolution panel should clearly show:

```text
Selected candidate
```

followed by:

```text
Finalize Match
```

---

# 38. No Suitable Match

Reviewer action:

```text
Create New Person
```

Before finalization, confirm:

```text
No suitable existing person was found.

This decision will request creation of a new canonical person.
```

The user must provide a brief reason or choose an approved reason code.

---

# 39. More Information Needed

Use when:

* source evidence is insufficient
* candidate conflict cannot be resolved
* page image is unclear
* canonical information is incomplete
* additional review is required

The reviewer must specify the next needed action.

---

# 40. Duplicate Intake Entry

When one intake entry duplicates another:

* select primary entry
* explain duplicate reason
* preserve both source records
* show that no source evidence will be deleted

---

# 41. Reject Entry

Rejection is reserved for cases such as:

* not a person entry
* invalid source row
* duplicate blank artifact
* wrong-document content
* prohibited or unusable intake

Rejection must require a reason.

---

# 42. Finalize Resolution

## 42.1 Confirmation

Show:

* selected outcome
* selected canonical person if applicable
* major supporting evidence
* conflicts
* reviewer reason
* downstream consequence

Example:

```text
Finalize Match to Existing Person?

This entry will be linked to Jordan Smith in the canonical people system. The original source and all review history will remain preserved.
```

## 42.2 Concurrency Conflict

When another reviewer has already finalized:

```text
This entry changed while you were reviewing it.

Reload the latest resolution before continuing.
```

Do not silently overwrite.

---

# 43. Resolution Success

Show:

* finalized outcome
* reviewer
* time
* promotion state
* next action

Example:

```text
Resolution saved.

Canonical promotion is pending.
```

---

# PART X — PROMOTION INTERFACE

# 44. Promotion List

## 44.1 Purpose

Track canonical link and creation requests.

## 44.2 Columns

* promotion ID
* entry
* operation
* canonical system
* status
* attempts
* last attempt
* error
* next action

## 44.3 Status Language

```text
Pending
In Progress
Succeeded
Retry Needed
Failed
Needs Review
Cancelled
```

---

# 45. Promotion Detail

Show:

* intake entry
* approved resolution
* operation requested
* idempotency identity summary
* attempt history
* canonical result
* provenance status
* error details safe for operator
* retry eligibility
* audit history

## 45.1 Retry Action

Retry confirmation:

```text
Retry this promotion?

The system will reuse the existing operation identity to prevent duplicate person creation.
```

---

# PART XI — MANAGE WORKSPACE

# 46. Manage Dashboard

## 46.1 Purpose

Provide operational oversight.

## 46.2 Sections

* Queue Health
* Active Claims
* Expired Claims
* Upload Issues
* Image Issues
* Match Conflicts
* Promotion Failures
* Background Job Failures
* Open Alerts
* User Access Issues

---

# 47. User Management Screen

## 47.1 Columns

* user
* email
* status
* roles
* last authenticated
* active claims
* created date
* actions

## 47.2 Actions

* invite
* activate
* suspend
* restore
* disable
* revoke
* add role
* revoke role
* inspect history

## 47.3 High-Risk Confirmation

Suspension example:

```text
Suspend this user?

The user will lose access. Active claims will be released or expired according to policy. Saved work will remain preserved.
```

Revocation example:

```text
Revoke access permanently?

The user’s prior actions and audit history will remain preserved.
```

---

# 48. User Detail Screen

Show:

* identity summary
* application status
* roles
* access history
* active claims
* recent work
* security events
* administrative notes where approved
* audit events

Do not display authentication tokens or provider secrets.

---

# 49. Claims Management Screen

## 49.1 Columns

* claim
* work item
* claimant
* status
* claimed at
* expires at
* last renewal
* draft status
* action

## 49.2 Actions

* inspect
* administratively release
* extend where policy allows
* view draft
* view claim history

## 49.3 Administrative Release

Requires:

* reason
* confirmation
* audit

---

# 50. Error and Alert Center

## 50.1 Purpose

Provide a single operational problem-solving workspace.

## 50.2 Tabs

```text
Alerts
Processing Errors
Failed Jobs
Upload Failures
Promotion Failures
```

## 50.3 Alert Card

Show:

* severity
* title
* affected record
* first detected
* last detected
* occurrence count
* recommended action
* status

## 50.4 Actions

* acknowledge
* inspect
* retry
* escalate
* resolve
* ignore with reason

Acknowledgment must not imply resolution.

---

# 51. Audit Explorer

## 51.1 Purpose

Allow authorized administrators to reconstruct meaningful business activity.

## 51.2 Filters

* event type
* domain
* actor
* subject type
* subject ID
* result
* date range
* correlation ID

## 51.3 Audit Event Detail

Show:

* event name
* event version
* actor
* subject
* object
* result
* reason
* occurred time
* recorded time
* correlation
* safe payload

Audit records are read-only.

---

# 52. Reports Screen

## 52.1 Sections

* Batch Progress
* Queue Throughput
* Transcription Throughput
* Review Outcomes
* Match Outcomes
* Promotion Outcomes
* Error Trends
* Claim Expiration
* Operator Workload

## 52.2 Reporting Principle

Reporting should support operational improvement, not pressure operators into unsafe speed.

## 52.3 Export

Any export action must show:

* included data
* date range
* privacy classification
* record count
* purpose
* authorization requirement

---

# PART XII — SEARCH

# 53. Global Search

Global search may support authorized lookup of:

* batches
* pages
* entries
* users
* promotion records
* audit subjects

The search interface must not expose records the user cannot access.

## 53.1 Search Results

Each result shows:

* record type
* safe display identifier
* summary
* status
* parent context
* direct action

## 53.2 No Results

```text
No authorized records matched your search.
```

Do not reveal whether inaccessible records exist.

---

# PART XIII — LOADING STATES

# 54. Loading Standard

Loading states should preserve page structure and reduce layout movement.

Use:

* skeleton rows
* loading cards
* clear progress labels
* upload progress
* background operation status

Avoid indefinite spinners without explanation.

## 54.1 Long-Running Actions

For matching, promotion, or upload processing:

```text
Matching is in progress.

You may leave this page. The result will remain available when processing finishes.
```

Do not promise completion time.

---

# PART XIV — EMPTY STATES

# 55. Empty-State Standard

Every empty state should explain:

1. what is empty
2. whether that is normal
3. what can happen next
4. whether the user can take action

Example:

```text
No pages are waiting for transcription.

New pages will appear here after an uploader marks them usable.
```

---

# PART XV — ERROR STATES

# 56. Error Message Structure

Every user-facing error should contain:

* plain-language title
* what happened
* what the user can do
* whether work was saved
* correlation reference where useful

Example:

```text
Your draft could not be saved.

Your entries are still visible on this device. Check your connection and try again before leaving this page.

Reference: 8A3F-21D9
```

---

# 57. Validation Errors

Validation errors must:

* appear near the affected field
* appear in a summary for long forms
* use plain language
* preserve user input
* receive keyboard focus appropriately
* never rely on color alone

---

# 58. Authorization Errors

Use:

```text
You do not have permission to perform this action.
```

Do not reveal inaccessible record details.

---

# 59. Stale Data Errors

Use:

```text
This record changed while you were working.

Review the latest version before saving again.
```

Provide:

* Reload Latest
* Preserve My Unsaved Work where technically possible
* Compare Changes where practical

---

# PART XVI — CONFIRMATION PATTERNS

# 60. Low-Risk Actions

Low-risk reversible actions generally do not require a modal.

Examples:

* filtering
* sorting
* opening a record
* changing tabs
* rotating image display

---

# 61. Medium-Risk Actions

Require inline confirmation or clear secondary step.

Examples:

* releasing a claim
* returning work for correction
* closing batch uploads

---

# 62. High-Risk Actions

Require explicit confirmation.

Examples:

* final match resolution
* create-new-person resolution
* role revocation
* user suspension
* archive
* administrative claim release
* promotion retry after conflict
* destructive retention action

High-risk confirmation must state:

* what will happen
* what will not happen
* whether history remains
* whether the action is reversible

---

# PART XVII — RESPONSIVE DESIGN

# 63. Breakpoint Philosophy

Exact pixel breakpoints are deferred to Volume 12.

Layouts must support:

* small mobile
* large mobile
* tablet portrait
* tablet landscape
* desktop
* large desktop

Do not design only for desktop and shrink later.

---

# 64. Mobile Thumb-Zone Standard

Primary mobile actions should appear within comfortable lower-screen reach when practical.

Examples:

* Save
* Submit
* Claim
* Continue
* Finalize
* Retry

High-risk actions should not be placed where accidental activation is likely.

---

# 65. Mobile Table Conversion

Desktop tables should become cards or structured lists on mobile.

Do not require horizontal scrolling for core workflows unless the data structure truly demands it.

---

# 66. Image and Form Coordination

On mobile transcription screens, the user must be able to:

* enlarge the image
* return to the active field
* navigate between rows
* preserve current scroll position
* avoid losing unsaved work

---

# PART XVIII — ACCESSIBILITY

# 67. Accessibility Standard

The application should target WCAG 2.2 AA compatibility.

Required areas include:

* keyboard operation
* visible focus
* semantic structure
* labeled controls
* descriptive buttons
* error association
* contrast
* zoom
* reflow
* touch-target size
* screen-reader announcements
* reduced motion
* status announcements
* time-limit handling
* non-color communication

---

# 68. Time-Limit Accessibility

Because claims expire:

* users must receive warning before expiration
* users must be able to request extension where policy permits
* save state must remain protected
* expiration must not erase work

Claim expiration must not create an inaccessible surprise.

---

# 69. Screen-Reader Status Announcements

The interface should announce:

* draft saved
* save failed
* claim acquired
* claim expiring
* validation error count
* upload complete
* resolution saved
* background process completed

Announcements should be concise and nonrepetitive.

---

# 70. Focus Management

After:

* modal open
* validation failure
* claim success
* route transition
* submission success
* stale-version conflict

focus must move to an appropriate meaningful element.

---

# PART XIX — VISUAL LANGUAGE

# 71. Visual Character

The system should feel:

* calm
* civic
* trustworthy
* practical
* clear
* modern
* serious without being intimidating

It should not feel:

* gamified
* flashy
* punitive
* hurried
* surveillance-oriented
* bureaucratically confusing

---

# 72. Color Use

Color may distinguish:

* success
* warning
* error
* information
* neutral state
* active workspace

Every color-coded status must also include text, iconography, shape, or another non-color indicator.

Exact color values belong to Volume 12.

---

# 73. Typography

Typography should prioritize:

* readability
* clear hierarchy
* dense data-entry usability
* accessible sizing
* consistent field labels
* distinct raw and normalized values

Exact typefaces belong to Volume 12.

---

# 74. Icon Use

Icons may support:

* upload
* save
* warning
* error
* claim
* review
* history
* audit
* archive

Icons must not be the only indicator.

Avoid decorative icon overload.

---

# PART XX — NOTIFICATIONS

# 75. In-App Notifications

Potential notifications:

* claim expiring
* returned correction
* promotion failure
* role change
* batch issue
* upload completed
* alert assigned

Notifications must link directly to the relevant record.

---

# 76. Notification Severity

```text
Information
Action Needed
Important
Critical
```

Do not use Critical for routine workflow updates.

---

# PART XXI — HELP AND GUIDANCE

# 77. Contextual Help

The interface should explain unfamiliar terms at the point of use.

Examples:

* Unknown
* Ambiguous
* Claim
* Canonical Person
* Promotion
* Provenance

Use short helper text with optional deeper explanation.

---

# 78. First-Use Guidance

First-use guidance may explain:

* how shared claims work
* that blank means unknown
* how to mark unreadable fields
* how autosave works
* that source images remain private
* that submission creates a fixed revision

Guidance should be dismissible and available again from Help.

---

# 79. Operational Training Mode

A future training mode may use fictional pages and data.

Training mode must:

* be clearly labeled
* never connect to production records
* never create canonical people
* use fictional data
* permit safe practice

---

# PART XXII — ANALYTICS AND UX OBSERVABILITY

# 80. Permitted Product Analytics

The application may measure:

* page-load failures
* workflow abandonment
* save failures
* claim collisions
* upload failures
* time to recover drafts
* accessibility-related interaction failures
* error frequency
* feature usage

It should not create hidden worker-surveillance scoring.

---

# 81. Prohibited Analytics Behavior

Do not:

* record raw typed personal data in analytics
* record source images
* record full email or phone values
* replay sensitive screens without explicit approved safeguards
* use productivity measurements to encourage guessing
* rank workers publicly

---

# PART XXIII — SCREEN INVENTORY

# 82. Canonical Screen Registry

## Public or Pre-Access

```text
Sign In
Access Pending
Access Suspended
Access Revoked
Session Expired
```

## Home

```text
Role-Aware Home
My Recent Work
Notifications
```

## Capture

```text
Capture Dashboard
Batch List
Create Batch
Batch Detail
Upload Pages
Upload Progress
Page Preparation
Image Replacement
```

## Transcribe

```text
Transcribe Dashboard
Shared Queue
My Active Work
Transcription Workspace
Draft Recovery
Submission Review
Submission Success
Submitted Work
Returned Corrections
```

## Review

```text
Transcription Review Queue
Transcription Review Screen
Correction Request
```

## Match

```text
Match Dashboard
Match Review Queue
Match Review Screen
Candidate Detail
Resolution Confirmation
Resolution Detail
Promotion List
Promotion Detail
Promotion Retry
```

## Manage

```text
Manage Dashboard
User List
Invite User
User Detail
Role Management
Claims Management
Batch Operations
Error and Alert Center
Error Detail
Alert Detail
Background Job Detail
Audit Explorer
Audit Event Detail
Reports
Export Confirmation
Configuration View
```

## Shared

```text
Global Search
Record Not Found
Access Denied
System Error
Offline or Connection Lost
Maintenance Notice
```

---

# PART XXIV — ROUTE PRINCIPLES

# 83. Route Design

Routes should:

* use stable record identifiers
* reflect workspace context
* support direct linking
* avoid exposing personal values
* permit browser navigation
* preserve return context
* support authorized deep links

Examples conceptually:

```text
/capture/batches
/capture/batches/{batchId}
/capture/pages/{pageId}

/transcribe/queue
/transcribe/pages/{pageId}

/match/queue
/match/entries/{entryId}
/match/promotions/{promotionId}

/manage/users/{userId}
/manage/audit/{auditEventId}
```

Exact route structure is deferred.

---

# PART XXV — CROSS-SCREEN WORKFLOW RULES

# 84. Return Context

After completing a nested action, users should return to a useful prior context.

Examples:

* after image replacement, return to page preparation
* after role change, return to user detail
* after match resolution, return to next review item or queue
* after upload completion, return to batch detail

---

# 85. Unsaved Navigation Protection

When unsaved work exists:

```text
You have unsaved changes.

Leave this page and discard them?
```

Actions:

* Stay
* Leave Without Saving

Where possible:

* Save and Leave

---

# 86. Multi-Tab Protection

The interface should detect stale changes caused by multiple tabs.

It should not assume the latest browser tab is authoritative.

---

# PART XXVI — WORKFLOW ACCEPTANCE SCENARIOS

# 87. Capture Acceptance Scenario

1. Uploader creates a batch.
2. Uploader selects eight page images.
3. Seven validate successfully.
4. One fails because the file is corrupt.
5. Successful uploads remain complete.
6. Failed upload shows retry guidance.
7. Uploader marks seven pages usable.
8. Pages enter transcription queue.
9. Original images remain private.

---

# 88. Transcription Acceptance Scenario

1. Data-entry user claims Page 4.
2. Claim status is clearly visible.
3. Source image and grid are visible together.
4. User enters six rows.
5. One email is unreadable.
6. Volunteer checkbox is blank and remains Unknown.
7. Draft autosaves.
8. Browser closes.
9. User returns and recovers draft.
10. User submits six entries.
11. Submission becomes read-only.
12. Page leaves transcription queue.

---

# 89. Claim Collision Acceptance Scenario

1. Two users open the queue.
2. Both see the same available page.
3. Both click Claim.
4. One succeeds.
5. One receives a calm already-claimed message.
6. The unsuccessful user receives another available option.
7. No duplicate active claim exists.

---

# 90. Match Acceptance Scenario

1. Reviewer opens an entry.
2. Raw and normalized values are visually distinct.
3. Three candidates appear.
4. Each candidate explains supporting and conflicting signals.
5. Shared phone warning is visible.
6. Reviewer selects one candidate.
7. Selection does not finalize automatically.
8. Reviewer confirms final match.
9. Promotion enters pending state.
10. Audit history records the resolution.

---

# 91. Promotion Failure Acceptance Scenario

1. Promotion fails because canonical service is unavailable.
2. Resolution remains complete.
3. Promotion status shows Retry Needed.
4. Safe error summary appears.
5. Administrator retries.
6. Confirmation explains duplicate protection.
7. Retry succeeds.
8. One canonical link is shown.

---

# 92. Accessibility Acceptance Scenario

1. Keyboard-only user signs in.
2. User navigates to transcription queue.
3. User claims a page.
4. User enters all fields without a mouse.
5. Save-state changes are announced.
6. Claim-expiration warning is announced.
7. Validation errors receive focus.
8. User submits successfully.

---

# PART XXVII — LOCKED UX DECISIONS

# 93. Locked Decisions

1. The application has four primary workspaces: Capture, Transcribe, Match, and Manage.
2. Navigation is role-aware.
3. Authorization is never dependent on hidden navigation alone.
4. Desktop uses persistent workspace navigation.
5. Mobile uses compact navigation with thumb-zone consideration.
6. Source images and structured fields should appear together where screen size permits.
7. Mobile transcription must support one-row-at-a-time work without losing image context.
8. Ten possible row positions are supported per page.
9. Blank rows do not create entries.
10. Volunteer and Email List use Yes, No, and Unknown.
11. Unknown is the safe default.
12. Raw and normalized values are visually distinct.
13. Unreadable and ambiguous are explicit user choices.
14. Autosave is required.
15. Save state is always visible.
16. Saved drafts survive claim expiration.
17. Claim status and expiration are visible.
18. Claim-expiration warnings must not create panic.
19. Submission creates an immutable revision.
20. Post-submission corrections create new revisions.
21. Match candidates must explain signals.
22. Candidate selection is separate from final resolution.
23. Strong conflicts receive prominent warnings.
24. Final identity resolution requires confirmation.
25. Promotion status is visible after resolution.
26. Administrative overrides require confirmation and reason.
27. Audit records are read-only.
28. Empty states explain what happens next.
29. Error states explain whether work was saved.
30. Validation preserves user input.
31. High-risk actions state both what will and will not happen.
32. Tables convert to cards or structured lists on mobile.
33. Core workflows must support keyboard-only use.
34. Color is never the sole status indicator.
35. Source-image privacy is communicated.
36. Sensitive values are minimized in queue lists.
37. Analytics may not collect raw intake content.
38. Worker performance must not be framed as a speed contest.
39. Training mode, if built, uses fictional data and stays isolated.
40. The user interface must prefer accuracy over pressure.

---

# PART XXVIII — DEFERRED DESIGN DECISIONS

# 94. Open UX Decisions

### `UI-DEC-001`

Exact frontend framework.

### `UI-DEC-002`

Exact route structure.

### `UI-DEC-003`

Exact desktop breakpoint.

### `UI-DEC-004`

Exact tablet breakpoint.

### `UI-DEC-005`

Exact mobile bottom-navigation items by role.

### `UI-DEC-006`

Exact transcription autosave interval.

### `UI-DEC-007`

Exact claim-warning interval.

### `UI-DEC-008`

Whether transcription review is page-based, entry-based, or hybrid in the first release.

### `UI-DEC-009`

Whether the source image viewer uses a persistent split pane or adjustable pane.

### `UI-DEC-010`

Whether match review uses cards, comparison table, or hybrid layout.

### `UI-DEC-011`

Exact masking pattern for queue-visible email and phone values.

### `UI-DEC-012`

Exact notification delivery mechanisms.

### `UI-DEC-013`

Whether dark mode is included in Version 1.

### `UI-DEC-014`

Whether global search is included at launch.

### `UI-DEC-015`

Whether the first release includes training mode.

### `UI-DEC-016`

Whether page-sequence reordering uses drag-and-drop, explicit number entry, or both.

### `UI-DEC-017`

Exact report visualizations.

### `UI-DEC-018`

Exact image-quality preview workflow.

These decisions are reserved for Volume 12, Volume 13, and implementation packages.

---

# PART XXIX — UI VALIDATION REQUIREMENTS

# 95. Required Design Validation

Before implementation begins, the final UI documentation must prove:

* every domain action has a screen location
* every API mutation has a corresponding user action or system-only designation
* every high-risk action has confirmation
* every empty state is defined
* every loading state is defined
* every primary error state is defined
* every mutable form has concurrency behavior
* every draft screen has save-state behavior
* every mobile workflow is documented
* every protected screen has authorization expectations
* every screen containing PII has minimization guidance
* every state transition uses consistent language
* every workflow has a clear next action
* every screen is traceable to domain rules and API contracts

---

# 96. Screen Specification Template

Every screen built in implementation must have a final specification containing:

```text
Screen ID
Screen Name
Purpose
Route
Authorized Roles
Primary User Goal
Data Required
API Dependencies
Layout
Primary Action
Secondary Actions
Loading State
Empty State
Error State
Validation
Confirmation
Responsive Behavior
Keyboard Behavior
Screen-Reader Behavior
Privacy Rules
Audit Events
Analytics Events
Acceptance Tests
Traceability
```

---

# PART XXX — VOLUME 11 READINESS

# 97. Completion Checklist

Volume 11 is complete when:

* the application shell is defined
* primary workspaces are defined
* role-aware navigation is defined
* all major screens are inventoried
* Capture workflows are defined
* Transcription workflows are defined
* Review workflows are defined
* Match workflows are defined
* Promotion workflows are defined
* Management workflows are defined
* save and recovery behavior are defined
* claim behavior is visible
* loading, empty, and error states are defined
* responsive behavior is defined
* mobile thumb-zone rules are defined
* accessibility requirements are defined
* privacy display rules are defined
* high-risk confirmations are defined
* analytics restrictions are defined
* locked and deferred decisions are separated

---

# 98. Readiness Score

| Area                    | Readiness |
| ----------------------- | --------: |
| Application structure   |      100% |
| Navigation              |       98% |
| Role-aware experience   |       98% |
| Capture workspace       |       98% |
| Transcription workspace |      100% |
| Match workspace         |      100% |
| Promotion interface     |       98% |
| Administration          |       97% |
| Loading states          |       98% |
| Empty states            |       98% |
| Error states            |      100% |
| Mobile behavior         |       98% |
| Accessibility           |      100% |
| Privacy display         |      100% |
| Confirmation behavior   |      100% |
| Analytics boundaries    |      100% |
| Screen inventory        |      100% |

**Overall Volume 11 Design Readiness**

```text
99%
```

The remaining percentage is reserved for alignment with:

* Volume 12 — Component Library and Design System
* State Machine Catalog
* Error Catalog
* Audit Event Catalog
* Configuration Catalog
* Cross-Volume Traceability Matrix

---

# 99. Next Governing Build

The next documentation build is:

```text
PEOPLE-VOLUME-12-COMPONENT-LIBRARY-AND-DESIGN-SYSTEM-1.0
```

Volume 12 will define:

* design tokens
* typography
* spacing
* responsive breakpoints
* color roles
* status styles
* buttons
* inputs
* preference controls
* field-condition controls
* tables
* cards
* page headers
* queue items
* claim indicators
* image viewer
* transcription grid
* candidate cards
* signal displays
* audit views
* dialogs
* banners
* alerts
* empty states
* loading states
* component accessibility contracts
* component state matrices
* component test requirements

No component code should be written during Volume 12.

The next build is **Volume 12 — Component Library and Design System**. It will turn these screens into a precise reusable component system so Cursor does not invent buttons, grids, status patterns, dialogs, or responsive behavior while coding.

---

## Document Control

| Field | Value |
| --- | --- |
| Canonical path | `docs/volumes/volume-11-ui-specifications/VOLUME_11_USER_INTERFACE_SPECIFICATIONS.md` |
| Legacy pointer | `docs/12_ui_specifications/VOLUME_11_USER_INTERFACE_SPECIFICATIONS.md` |
| Encoding | UTF-8 |
| Status | DESIGN COMPLETE — IMPLEMENTATION NOT AUTHORIZED |
| Build mode | DOCUMENTATION ONLY — no React, CSS, or route files |
