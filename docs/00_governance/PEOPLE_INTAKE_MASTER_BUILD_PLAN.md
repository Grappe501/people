# PEOPLE INTAKE SYSTEM

## Master Build Plan

**Working project name:** People Intake  
**Application root:** `H:\people`  
**Workspace ecosystem reference:** `H:\SOSWebsite`  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-GOVERNANCE-FOUNDATION-1.0  
**Application code authorized:** No  

**Primary purpose:** Securely capture photographed volunteer sign-up sheets, transcribe up to ten individual entries from each page, match those entries against the canonical people database, and preserve a complete source and audit history.

---

# 1. Governing Vision

## 1.1 Why We Are Building It

Campaigns and civic organizations collect valuable contact information on handwritten volunteer sheets, but the information often remains trapped on paper, becomes difficult to trace, or is inconsistently entered into multiple systems.

People Intake will create a reliable bridge between paper volunteer forms and the shared people database.

The system must make it easy to:

1. Photograph volunteer sheets in the field.
2. Upload many sheets as one batch.
3. Share the queue across multiple authenticated users.
4. Enter up to ten individual people from each page.
5. Preserve each line as a unique intake entry.
6. Match entries against existing people without unsafe automatic merging.
7. Create new canonical people when no match exists.
8. Preserve the original image and complete audit history.
9. Allow RedDirt and other authorized systems to use the canonical people data.

## 1.2 Product Principle

> Capture the page. Transcribe every entry. Match each person. Preserve the evidence.

## 1.3 Experience Principle

The application must require the fewest practical decisions and taps at each stage.

The system should feel like three focused tools:

* **Capture**
* **Transcribe**
* **Match**

Each user should see only the work appropriate to their role.

---

# 2. Permanent Technical Protocols

## 2.1 H-Drive-Only Protocol

The project root is permanently:

```text
H:\people
```

All controllable project writes must remain on `H:\`.

Required project-local paths:

```text
H:\people\.tmp
H:\people\.cache
H:\people\.npm-cache
H:\people\.netlify
H:\people\.test-output
H:\people\.local-storage
H:\people\develop_notes
```

Required process variables:

```text
TEMP=H:\people\.tmp
TMP=H:\people\.tmp
TMPDIR=H:\people\.tmp
npm_config_cache=H:\people\.npm-cache
```

Cursor must never intentionally create, move, install, clone, or generate a project artifact on `C:\`.

Authoritative detail: `docs/00_governance/PEOPLE_INTAKE_H_DRIVE_PROTOCOL.md`.

## 2.2 Design-Before-Code Protocol

No application implementation may begin until the design package is written, reviewed, validated, cross-referenced, design-frozen, and approved for implementation.

Before design freeze, Cursor may create only documentation artifacts, contracts, schemas, diagrams, validation scripts, and explicitly authorized folder structures or documentation package metadata.

Authoritative detail: `docs/00_governance/PEOPLE_INTAKE_DESIGN_BEFORE_CODE_PROTOCOL.md`.

## 2.3 Shared Database Protocol

People Intake will use the same hosted Postgres environment and connectivity conventions as RedDirt but remain a separate application.

The design must establish:

* Shared canonical person identity
* Separate intake-domain tables
* Separate application credentials
* Least-privilege database permissions
* No direct cross-application imports
* Stable contracts between People Intake and RedDirt
* Additive database changes wherever possible
* Full migration and rollback documentation
* No destructive schema changes without explicit approval

## 2.4 Source-of-Truth Protocol

Hierarchy:

1. Approved master documents
2. Approved domain contracts
3. Approved state machines
4. Approved database design
5. Approved API contracts
6. Approved UX specifications
7. Implementation code
8. Generated documentation

Authoritative registry: `docs/00_governance/PEOPLE_INTAKE_SOURCE_OF_TRUTH_REGISTRY.md`.

## 2.5 Human-Control Protocol

The application may assist with matching, validation, and duplicate detection, but it must not:

* Silently merge uncertain people
* Invent missing data
* Interpret unmarked fields as "No"
* Replace raw transcription with normalized values as sole evidence
* Delete source evidence automatically
* Expose source images publicly
* Send email or text messages
* Make campaign decisions
* Perform autonomous outreach

---

# 3. System Boundaries

## 3.1 In Scope

Secure sign-in; role-based access; mobile image capture; multi-image upload; intake batch creation; shared page queue; page claiming; page transcription; up to ten individual entries per page; draft autosave; page-level submission; entry normalization; exact duplicate detection; possible-match generation; human matching review; canonical person creation or linkage; private image storage; audit history; batch progress; queue metrics; recent activity; administrative reassignment; image quality review; data validation; error recovery; mobile/tablet/desktop layouts; Netlify deployment; database connectivity; operational documentation.

## 3.2 Explicitly Out of Scope for Version 1

Handwriting OCR; AI transcription; email sending; text messaging; volunteer scheduling; event management; canvassing tools; donor management; relationship scoring; public intake forms; native iOS/Android apps; public image URLs; automatic uncertain merges; marketing automation; full CRM dashboards; voter-file matching; household modeling; address enrichment; external data purchases.

## 3.3 Future-Compatible Areas

PWA offline support; address fields; county/precinct enrichment; organization affiliations; event linkage; volunteer skills/availability; source campaigns; QR batch labels; AI-assisted quality review; RedDirt relationship integration; external form imports; bulk spreadsheet imports; retention schedules; consent-history expansion.

Authoritative detail: `docs/00_governance/PEOPLE_INTAKE_SCOPE_AND_BOUNDARIES.md`.

---

# 4. Core Domain Model

## 4.1 Batch

A batch represents a collection of photographed pages uploaded together, with metadata such as name, event/source, county, city, collection date, collected by, uploaded by, notes, priority, page count, status, and timestamps.

## 4.2 Page

A page is one photographed volunteer sheet and the primary queue work item. It contains one source image, up to ten intake entries, sequence number, batch membership, upload/quality/queue/claim/transcription/matching/review information, and audit history.

## 4.3 Intake Entry

An intake entry represents one handwritten line on a page, with unique identity, row number, raw fields, volunteer/email-list responses, readability states, transcription and matching status, matched person ID, operators, and timestamps.

## 4.4 Canonical Person

The shared individual identity used by RedDirt and other authorized systems. Distinct from raw transcription, normalized values, and matching decisions.

## 4.5 Match Candidate

A possible relationship between an intake entry and an existing canonical person, including score, reasons, confidence tier, conflicts, suggested action, and human resolution metadata.

## 4.6 Audit Event

Append-only record of meaningful actions (batch created, image uploaded, page claimed, draft saved, page submitted, match linked, new person created, admin reassignment, and related events).

---

# 5. Data Semantics

## 5.1 Volunteer and Email-List Values

```text
YES
NO
UNKNOWN
```

`UNKNOWN` means the paper did not clearly indicate an answer. Unknown may never be silently converted to No.

## 5.2 Field Condition Values

```text
PROVIDED
NOT_PROVIDED
UNREADABLE
```

## 5.3 Raw and Normalized Data

Preserve both. Raw is evidence of transcription. Normalized supports comparison and operations.

## 5.4 Entry Independence

Blank rows create no intake entries. Submitting a page with eight completed rows creates one page record, eight intake-entry records, zero to eight person links, and one page-level workflow transition.

## 5.5 Provenance

Every person attribute created or updated through intake must be traceable to batch, page, entry, source image, uploader, transcriber, reviewer, and date/time.

---

# 6. User Roles and Permissions

## 6.1 Uploader

May create batches, enter batch metadata, photograph/upload sheets, review orientation/readability, replace images before transcription begins, and view uploaded batches. May not resolve matches, merge people, delete completed source records, or edit other operators' completed work.

## 6.2 Data Entry Operator

May view available pages, claim next page, enter up to ten people, save drafts, mark fields unreadable, submit pages, edit own claimed page, and release a page. May not perform uncertain merges, delete source images, edit canonical people outside approved flow, or modify another active claim.

## 6.3 Matcher or Reviewer

May review possible matches, link entries, create canonical people, accept selected new information, reject suspected matches, return pages for correction, and complete matching review.

## 6.4 Administrator

May perform authorized workflows, manage users/roles, reassign pages, release abandoned claims, set priorities, review audit history, correct workflow errors, manage retention, archive batches, and access operational reporting.

## 6.5 Owner

May manage application-wide configuration, administrator access, retention/deletion policy approval, database-contract change approval, and production integration approval.

Detailed role matrix to be expanded in `PEOPLE_INTAKE_USER_ROLES.md` and `PEOPLE_INTAKE_AUTHORIZATION_MATRIX.md`.

---

# 7. Workflow Architecture

## 7.1 Capture Workflow

```text
Create Batch → Add Source Information → Take or Select Images → Preview Images → Reorder Pages → Confirm Upload → Upload Batch → Queue Pages
```

## 7.2 Image Quality Workflow

Each page receives one of: READY, NEEDS_ROTATION, TOO_BLURRY, DUPLICATE_IMAGE, INCOMPLETE_IMAGE, REPLACEMENT_REQUIRED.

## 7.3 Transcription Workflow

```text
Claim Next Page → Display Source Image → Enter All Visible People → Autosave Draft → Review Page Entries → Submit Page → Open Next Page
```

## 7.4 Matching Workflow

```text
Normalize Entries → Search Exact Matches → Generate Possible Matches → Categorize Each Entry → Resolve Human Review Cases → Link or Create Person → Complete Page
```

## 7.5 Page State Machine (Proposed)

```text
UPLOADING
UPLOAD_FAILED
UPLOADED
IMAGE_REVIEW
READY_FOR_ENTRY
CLAIMED_FOR_ENTRY
ENTRY_IN_PROGRESS
ENTRY_SUBMITTED
READY_FOR_MATCHING
MATCHING_IN_PROGRESS
NEEDS_MATCH_REVIEW
NEEDS_ENTRY_CORRECTION
COMPLETED
ARCHIVED
```

Every transition must define who can trigger it, required conditions, side effects, audit event, recovery path, and invalid transitions.

## 7.6 Entry State Machine (Proposed)

```text
DRAFT
TRANSCRIBED
VALIDATION_WARNING
READY_FOR_MATCHING
EXACT_MATCH
POSSIBLE_MATCH
NO_MATCH
MATCH_REVIEW
LINKED_EXISTING
CREATED_NEW
NEEDS_CORRECTION
COMPLETED
```

## 7.7 Claiming and Concurrency

Atomic claims with claimed-by, claimed-at, last-activity-at, expiration, and claim version. One active editor per page. Claims refresh during activity. Autosave validates ownership. Expired claims return to queue. Administrators may force-release. Prior drafts preserved. Conflicting writes rejected. No last-write-wins on shared pages. Recommended default claim window: 30 minutes, renewable.

---

# 8. User Experience Architecture

## 8.1 Global UX Requirements

Mobile-first; large touch targets; fast on ordinary cellular; readable outdoors; keyboard efficient on desktop; accessible; recoverable after interruption; clear save/upload status; free of unnecessary navigation.

## 8.2 Home Screen by Role

Uploader: Take Pictures, Upload Existing Pictures, Resume Upload, My Recent Batches.  
Data Entry: Claim Next Page, Resume My Page, View Queue, Recent Work.  
Reviewer: Review Next Match, Resume Review, Needs Correction, Completed Today.  
Administrator: Queue Overview, Batches, Users, Exceptions, Audit, Settings.

## 8.3 Capture Experience

Capture several pages without leaving camera flow; select multiple existing images; review thumbnails; rotate; remove; reorder; upload once; see progress; recover failed images individually.

## 8.4 Transcription Screen

Phone: sticky progress, image viewer, current person card, completed summaries, save person and next, finish page. Image viewer: zoom, pan, rotation, full screen, reset, brightness/contrast viewing aid, return to last position. Tablet/desktop: image plus ten-row grid, keyboard navigation, sticky submission controls.

## 8.5 Ten-Entry Page Behavior

Zero to ten entries; skip unused rows; edit previous rows; reorder only before submission; mark row or field unreadable; duplicate warning within page; page-level review before submission.

## 8.6 Submission Controls

Save Draft; Release Page; Review Page; Submit Page & Open Next; Submit Page & Return to Queue; Mark Page Unreadable.

## 8.7 Queue Experience

Views for ready, claimed, in progress, ready for matching, needs review, needs correction, completed. Standard action: Claim Next Page. Selection: priority, oldest ready, batch ordering, sequence number.

## 8.8 Matching Screen

Source image, raw entry, normalized entry, best candidate, other candidates, reasons, conflicts, authorized history. Actions: Link to Existing; Create New Person; Accept Selected Fields; Keep Existing Fields; Return for Correction; Defer Review.

---

# 9. Matching and Deduplication Design

## 9.1 Matching Philosophy

Explainable and conservative. Prefer duplicate review over unsafe merging; evidence over intuition; human review over ambiguous automation; preserving both records over destroying provenance.

## 9.2 Exact-Match Signals

Exact normalized email; exact normalized phone; exact email plus compatible name; exact phone plus compatible name.

## 9.3 Possible-Match Signals

Same first/last plus ZIP; similar name plus same phone/email; name reversal; handwriting/transcription variation; shared email or phone with differing name.

## 9.4 Conflict Signals

Same email with substantially different names; household phone ambiguity; ZIP conflicts; apparent corrections; equally good multiple matches.

## 9.5 Match Confidence Tiers

```text
EXACT
HIGH_CONFIDENCE
POSSIBLE
LOW_CONFIDENCE
NO_MATCH
CONFLICT
```

## 9.6 Automated Actions

May: normalize, generate/rank candidates, link only approved exact-match categories, create no-match recommendations.  
Must not: merge canonical records, replace conflicting fields, link ambiguous household phones, resolve conflicting emails, delete duplicate records.

## 9.7 Match Explanation

Every suggested match must provide human-readable reasons.

---

# 10. Database Architecture

## 10.1 Database Design Package Requirements

ERD; table/field definitions; types; required/optional; indexes; FKs; uniqueness; checks; lifecycle; soft-delete; audit; migration/rollback; RedDirt compatibility; least-privilege role plan.

## 10.2 Proposed Intake Tables

```text
intake_batches
intake_pages
intake_entries
intake_entry_fields
intake_match_candidates
intake_match_resolutions
intake_page_claims
intake_audit_events
intake_upload_attempts
intake_processing_errors
intake_user_preferences
```

## 10.3 Canonical People Integration

Preferred: use existing shared canonical people tables through a stable service/repository contract.  
Alternative: intake staging then controlled promotion.  
Final design must choose one and document why, risks, permissions, rollback, RedDirt impact, and duplicate-control behavior.

## 10.4 Indexing Requirements

Queue retrieval; batch page ordering; active claims; exact email/phone; name+ZIP; matching status; page status; user work history; audit lookup; recently completed pages.

## 10.5 Transaction Requirements

Claim page; submit page; create all page entries; link exact match; create canonical person; resolve possible match; complete page; release or expire claim.

---

# 11. Image Storage Architecture

## 11.1 Storage Principle

Images in private object storage. Postgres stores storage key, metadata, hash, type, size, dimensions, upload status, and access history when needed.

## 11.2 Storage Requirements

Private bucket; signed temporary URLs; no public listing; size limits; MIME validation; content hashing; duplicate-image detection; upload retry; orphan cleanup; retention policy; audit logging; env separation.

## 11.3 Supported Formats

JPEG; PNG; HEIC when server-side conversion is safely supported. Preserve original; may generate viewing derivative.

## 11.4 Suggested Storage Path

```text
volunteer-intake/
  environment/
    year/
      month/
        batch-id/
          page-id/
            original.ext
            display.webp
```

## 11.5 Image Security

Never public routes, public repos, base64 logs, permanent unsigned URLs, or unauthorized public CDN caching.

---

# 12. Authentication and Security

Use approved Supabase authentication pattern from the broader ecosystem. Authenticated access only; approved-user onboarding; no public signup; session refresh; server-side authorization; role resolution; secure sign-out; account disablement. Every read/write authorized server-side. Separate restricted DB credentials. Protect names, emails, phones, ZIPs, images, identities, audit history. Logs may include IDs and statuses, not PII, signed URLs, or secrets. Pre-launch security review required.

---

# 13. Reliability and Recovery

Autosave on meaningful changes, between entries, before fullscreen image, on blur, and on safe interval. Upload progress, retry, resume, duplicate protection, partial completion. Draft recovery after interruption. Idempotency for sensitive writes. Error categories: UPLOAD_ERROR, STORAGE_ERROR, DATABASE_ERROR, CLAIM_CONFLICT, VALIDATION_ERROR, MATCHING_ERROR, AUTHORIZATION_ERROR, ORPHANED_FILE, INCOMPLETE_TRANSACTION.

---

# 14. Validation Rules

Names: preserve raw punctuation; trim; do not require both names when incomplete; warn on likely reversals.  
Email: raw + lowercase normalize; structural validation; warn rather than hard-block.  
Phone: raw + digit normalize; support 10-digit US; allow extensions; warn rather than hard-block.  
ZIP: raw; five-digit and room for ZIP+4; warn when incomplete.  
Page: max ten active entries; blank rows ignored; duplicate-row warning; at least one entry unless page marked blank/unusable; explicit review before submit.

---

# 15. API and Service Design

Services for authz, batches, upload, queue, claims, draft transcription, submission, normalization, matching, person create/link, audit, reporting, administration. Every endpoint documented before code with method, path, roles, schemas, validation, transaction boundary, errors, idempotency, audit effects, state transitions. No client-direct writes to sensitive canonical tables.

---

# 16. Application Architecture

Recommended alignment: Next.js, TypeScript, React, Prisma, hosted Postgres, Supabase Auth, private object storage, Netlify, server-side API routes/functions, schema-based runtime validation.

Proposed structure (post-freeze):

```text
H:\people
├── docs
├── develop_notes
├── contracts
├── diagrams
├── prisma
├── scripts
├── src
│   ├── app
│   ├── components
│   ├── domains
│   ├── lib
│   └── types
├── tests
├── public
├── package.json
├── netlify.toml
└── README.md
```

`src`, `prisma`, and related implementation directories are forbidden until Gate G-10.

---

# 17. Testing Strategy

Layers: contract, schema, unit, service, DB integration, authorization, file-upload, state-machine, concurrency, queue, matching, UI, responsive, accessibility, e2e, deployment smoke.

Critical scenarios include dual claim races, claim expiry with drafts, upload interruption, partial batch failure, ten-entry and one-entry pages, unreadable page/fields, exact email match, household phone ambiguity, name+ZIP candidates, double submit, storage/DB partial failures, admin reassignment, return for correction, unauthorized image access, expired signed URL, exceeding ten entries, authorized reopen of completed page.

---

# 18. Accessibility and Mobile Standards

Keyboard navigation; visible focus; semantic labels; screen-reader support; sufficient contrast; large touch targets; no color-only status; reduced motion; portrait/landscape; iPhone/iPad/Android/desktop testing; zoom support; error summaries; clear save-state announcements.

---

# 19. Operational Reporting

Queue metrics, batch metrics, and non-punitive user work metrics as specified in the governing outline (ready/claimed/matching/review/correction/completed counts; oldest waiting; average times; entries created; linked vs new people; errors).

---

# 20. Deployment Architecture

Dedicated GitHub repository. Dedicated Netlify site. Environments: local, development, preview, production — each with separate storage paths/buckets, URLs, secrets, and audit labels where practical. Production gates: typecheck, lint, tests, schema validation, DB/storage connectivity, permission tests, H-drive preflight, Netlify config validation, smoke tests, documented rollback.

---

# 21. Documentation Package

Sixty governing documents across eight volumes as listed in `contracts/documentation/documentation-index.json`, covering governance, product, workflows, UX, data, security, engineering, quality/operations, and implementation control.

---

# 22. Design Validation Contracts

Machine-readable contracts under `contracts/` for schemas, state machines, API index, documentation index, and design-freeze checklist. A documentation validator verifies existence, status, cross-references, naming consistency, and that no application code exists before design freeze.

---

# 23. Cursor Execution Strategy

Nine-script model:

1. Governance and Workspace Foundation (this build)
2. Complete Workflow and UX Design
3. Complete Data, Matching, and Storage Architecture
4. Complete Security and Engineering Contracts
5. Complete Test, Deployment, and Operations Design
6. Design Audit and Freeze
7. Foundation Implementation (after freeze)
8. Full Workflow Implementation
9. Hardening and Launch

Authoritative runtime rules: `docs/08_implementation/PEOPLE_INTAKE_CURSOR_EXECUTION_PROTOCOL.md`.

---

# 24. Implementation Phase Map

| Phase | Name |
| --- | --- |
| -1 | Governance |
| 0 | Complete Design |
| 1 | Technical Foundation |
| 2 | Capture and Upload |
| 3 | Shared Queue and Claims |
| 4 | Ten-Entry Transcription |
| 5 | Matching and Canonical People |
| 6 | Administration and Reporting |
| 7 | Hardening |
| 8 | Launch |

Details: `contracts/governance/build-phase-registry.json`.

---

# 25. Design Freeze Gate

Implementation may begin only when the master plan is complete; workflows, state machines, ten-entry design, queue/claims, matching, canonical person integration, tables, storage, roles, APIs, errors, security, testing, and deployment designs are final; H-drive validation is operational; no blocking unresolved decisions remain; design audit passes; design freeze report is approved.

---

# 26. Definition of Done

Authorized field user can sign in, create a batch, photograph multiple sheets, review/upload, and leave.  
Authorized office user can sign in, view queue, claim next page, view image, enter up to ten people, save/recover drafts, review, submit, and auto-open next page.  
Authorized reviewer can resolve matches, link or create people, return corrections, and complete pages.  
System preserves original image, batch/page/entry identities, raw and normalized values, person relationship, users, timestamps, match reasoning, and audit history — securely, without public image exposure or silent evidence alteration.

---

# 27. Documentation Cross-References

- Product charter: `docs/01_product/PEOPLE_INTAKE_PRODUCT_CHARTER.md`
- Scope: `docs/00_governance/PEOPLE_INTAKE_SCOPE_AND_BOUNDARIES.md`
- H-drive: `docs/00_governance/PEOPLE_INTAKE_H_DRIVE_PROTOCOL.md`
- Design-before-code: `docs/00_governance/PEOPLE_INTAKE_DESIGN_BEFORE_CODE_PROTOCOL.md`
- Decisions: `docs/00_governance/PEOPLE_INTAKE_DECISION_LOG.md`
- Glossary: `docs/00_governance/PEOPLE_INTAKE_GLOSSARY.md`
- Active build: `contracts/governance/active-build.json`

---

# 28–33. Control Surfaces

Build gates, progress ledger, Cursor protocol, phase registry, documentation index, and validation scripts operationalize this master plan. They do not replace it.
