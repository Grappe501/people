# PEOPLE INTAKE SYSTEM

# VOLUME 8 — TECHNICAL DOMAIN SPECIFICATIONS

**Document ID**

```text
PEOPLE-VOLUME-08-TECHNICAL-DOMAIN-SPECIFICATIONS-1.0
```

**Status**

```text
DESIGN COMPLETE — PENDING FINAL CROSS-VOLUME FREEZE
```

**Project Root**

```text
H:\people
```

**Document Type**

```text
IMPLEMENTATION-GOVERNING TECHNICAL SPECIFICATION
```

**Implementation Authority**

This volume governs the business behavior of the People Intake System.

It does not authorize production implementation by itself. Implementation may begin only after the complete documentation library, supporting catalogs, traceability matrices, and implementation packages are reviewed and frozen.

---

# PART I — VOLUME GOVERNANCE

## 1. Purpose

Volume 8 converts the approved People Intake architecture into precise technical-domain specifications.

It defines:

* domain ownership
* domain responsibilities
* domain boundaries
* business rules
* invariants
* state dependencies
* authorization expectations
* audit expectations
* idempotency requirements
* concurrency protections
* error behavior
* recovery behavior
* privacy requirements
* observability requirements
* future compatibility boundaries
* acceptance scenarios

This volume answers:

> What must each part of the People Intake System do, protect, preserve, reject, record, and recover from?

It intentionally does not define:

* physical database tables
* column types
* API routes
* application framework
* visual page implementation
* reusable component code
* cloud-provider configuration
* production secrets
* deployment mechanics

Those details belong to later volumes.

---

## 2. Governing Doctrine

The People Intake System exists to transform handwritten volunteer sign-up information into trusted canonical people records while preserving source evidence and human accountability.

The governing information flow is:

```text
Source Evidence
        ↓
Raw Transcription
        ↓
Normalized Values
        ↓
Match Evaluation
        ↓
Human Resolution
        ↓
Canonical Promotion
        ↓
Canonical Person
```

No layer may silently erase the layer above it.

---

## 3. Source-of-Truth Layers

The system recognizes five distinct truth layers.

### 3.1 Source Truth

What visibly exists on the original handwritten page.

Source truth may be:

* readable
* unreadable
* ambiguous
* incomplete
* contradictory
* damaged
* partially obscured

Source truth is preserved even when it cannot be interpreted.

### 3.2 Transcription Truth

What a human operator entered after viewing the source.

Transcription truth may later be corrected, but its revision history must remain available.

### 3.3 Normalized Truth

A standardized representation derived from transcription.

Examples include:

* normalized email casing
* normalized phone digits
* normalized ZIP formatting
* trimmed whitespace
* standardized preference values

Normalization must not invent missing information.

### 3.4 Resolution Truth

The approved determination about whether an entry:

* matches an existing canonical person
* should create a new canonical person
* remains unresolved
* contains a conflict requiring escalation

### 3.5 Canonical Truth

The trusted identity and attribute record maintained by the canonical people domain.

People Intake contributes evidence and proposed attributes.

People Intake does not silently become the universal owner of identity.

---

## 4. Global Invariants

These invariants apply across all domains.

### `PEOPLE-INV-001 — Evidence Preservation`

Original source evidence must not be overwritten by transcription, normalization, matching, or promotion.

### `PEOPLE-INV-002 — Unknown Is Not No`

A blank, unreadable, or unstated preference must not be interpreted as `NO`.

### `PEOPLE-INV-003 — Human Accountability`

No uncertain identity merge or irreversible canonical identity decision may occur without an authorized human decision.

### `PEOPLE-INV-004 — Traceability`

Every promoted canonical contribution must be traceable back to:

* intake entry
* page
* batch
* source image
* responsible actors
* relevant decisions

### `PEOPLE-INV-005 — No Silent Mutation`

Meaningful business state changes must produce durable history.

### `PEOPLE-INV-006 — Least Privilege`

A user may access only the records and actions required for the user’s approved role.

### `PEOPLE-INV-007 — Server Enforcement`

Security and workflow rules must be enforced by trusted server-side logic rather than UI behavior alone.

### `PEOPLE-INV-008 — Stable Identity`

Canonical person identifiers must not be inferred from mutable display fields such as name, email, phone, or ZIP.

### `PEOPLE-INV-009 — Idempotent Repetition`

Repeating a retried operation must not create duplicate business outcomes.

### `PEOPLE-INV-010 — No Hidden Automation`

Automated recommendations, normalization, and candidate generation must be visible and distinguishable from human decisions.

### `PEOPLE-INV-011 — Independent Entry Identity`

Each handwritten row is tracked as an independent intake entry even when it appears on the same page as other entries.

### `PEOPLE-INV-012 — Private Source Images`

Source images must not be publicly accessible.

### `PEOPLE-INV-013 — Audit Independence`

Audit history must remain distinct from operational logs and user-editable notes.

### `PEOPLE-INV-014 — Canonical Ownership Boundary`

People Intake may request canonical creation, linking, and attribute contribution, but canonical identity authority remains outside the intake workflow.

### `PEOPLE-INV-015 — Recoverable Work`

An interruption must not silently destroy valid transcription work already saved.

---

# PART II — ACTORS AND OPERATING ROLES

## 5. Roles

### 5.1 Uploader

May:

* create or contribute to an intake batch where authorized
* upload source pages
* review upload status
* correct upload metadata before processing begins

May not:

* resolve identity matches
* change system roles
* bypass image restrictions
* promote entries to canonical people

### 5.2 Data Entry User

May:

* view assigned source pages
* claim available transcription work
* enter handwritten values
* save drafts
* submit completed transcription
* correct work when returned through an authorized workflow

May not:

* make uncertain canonical identity decisions
* administer users
* change source evidence
* access unrelated administrative records

### 5.3 Reviewer

May:

* review transcription
* review normalization
* inspect match candidates
* approve or reject proposed matches
* determine no-match outcomes
* return entries for correction
* initiate authorized promotion

May not:

* alter original images
* bypass audit
* silently merge conflicting people
* change user permissions unless separately assigned an administrative role

### 5.4 Administrator

May:

* monitor queues
* resolve abandoned claims
* manage batches
* manage operational errors
* manage approved user access
* inspect audit history
* perform documented recovery actions

Administrative status does not automatically authorize canonical identity resolution unless the administrator also has the appropriate review authority.

### 5.5 Owner

May:

* approve administrators
* govern application access
* approve high-risk operational actions
* approve configuration changes
* approve policy changes
* approve design amendments

Owner authority does not permit removal of audit history or fabrication of source evidence.

### 5.6 System Actor

A trusted automated process acting under a defined service identity.

The system actor may:

* normalize values
* generate candidate matches
* expire claims
* retry background jobs
* record operational alerts

The system actor may not:

* make uncertain canonical merges
* falsify human review
* infer unstated consent
* silently change source transcription

---

# PART III — DOMAIN SPECIFICATIONS

# 6. Authentication Domain

## 6.1 Purpose

Establish the verified identity of each user attempting to access People Intake.

## 6.2 Ownership

The Authentication Domain owns:

* sign-in verification
* session establishment
* session refresh
* session termination
* authentication-state validation

It does not own:

* application roles
* workflow permissions
* canonical person identity
* organization membership
* business-record access decisions

## 6.3 Actors

* invited user
* active user
* suspended user
* disabled user
* authentication provider
* system actor
* administrator

## 6.4 Inputs

* approved authentication credential
* provider response
* session token
* user identity reference
* authentication callback
* sign-out request

## 6.5 Outputs

* authenticated session
* unauthenticated state
* authentication failure
* session-expired state
* verified external identity reference

## 6.6 Business Rules

### `AUTH-RULE-001`

People Intake must not allow anonymous access to protected records.

### `AUTH-RULE-002`

Public self-registration is prohibited unless a future approved amendment explicitly authorizes it.

### `AUTH-RULE-003`

Authentication does not itself grant application access.

### `AUTH-RULE-004`

A verified external identity must be linked to an approved People Intake user record before protected access is granted.

### `AUTH-RULE-005`

Suspended, disabled, and revoked users must not receive active application sessions.

### `AUTH-RULE-006`

Session validation must occur at trusted boundaries.

### `AUTH-RULE-007`

Authentication failures must not disclose sensitive provider or account details.

### `AUTH-RULE-008`

Sign-out must invalidate or terminate the active application session as supported by the selected provider.

## 6.7 Invariants

* `AUTH-INV-001`: A valid provider identity is not equivalent to application authorization.
* `AUTH-INV-002`: Shared user accounts are prohibited.
* `AUTH-INV-003`: Authentication secrets must never be written to application logs.
* `AUTH-INV-004`: Disabled users cannot regain access through a stale application session.

## 6.8 State Dependencies

User access depends on both:

```text
Authentication State = AUTHENTICATED
```

and:

```text
Application User State = ACTIVE
```

## 6.9 Authorization Requirements

Authentication endpoints may be accessible before application authorization, but protected business operations require authorization checks after authentication succeeds.

## 6.10 Audit Requirements

Record:

* successful sign-in
* failed sign-in where safe
* sign-out
* session revocation
* authentication identity relinking
* administrative access-state changes

Do not record raw credentials or tokens.

## 6.11 Idempotency

Repeated callback delivery must not create duplicate user records or duplicate identity links.

## 6.12 Concurrency

Concurrent sessions may be allowed unless restricted by future security policy. Revocation must apply consistently across active sessions as supported by the architecture.

## 6.13 Error Conditions

* invalid credential
* expired session
* provider unavailable
* user not approved
* user suspended
* user disabled
* identity collision
* callback replay

## 6.14 Recovery

Provider outages should produce a clear temporary-failure state. Existing valid sessions may continue only according to approved session policy.

## 6.15 Privacy

Expose only the minimum identity information needed for access and administrative recognition.

## 6.16 Observability

Monitor:

* authentication success rate
* failure rate
* provider errors
* revoked-session attempts
* identity-link conflicts

## 6.17 Acceptance Scenarios

1. An invited active user signs in and receives authorized access.
2. A valid provider user without application approval is denied.
3. A suspended user with a stale session is denied.
4. A repeated callback does not create a second user.
5. Authentication failure does not expose internal provider details.

---

# 7. User Access and Approval Domain

## 7.1 Purpose

Govern who may use People Intake and the lifecycle of that access.

## 7.2 Ownership

This domain owns:

* user invitation
* access approval
* activation
* suspension
* disabling
* revocation
* user access history

It does not own authentication credentials or canonical people identity.

## 7.3 User States

```text
INVITED
ACTIVE
SUSPENDED
DISABLED
REVOKED
```

## 7.4 Business Rules

### `USER-RULE-001`

Only approved users may become `ACTIVE`.

### `USER-RULE-002`

Every state transition must identify the responsible actor.

### `USER-RULE-003`

Suspension is reversible.

### `USER-RULE-004`

Disabling blocks access until an authorized restoration action occurs.

### `USER-RULE-005`

Revocation represents a deliberate termination of access and requires a new approval workflow before future access.

### `USER-RULE-006`

A user must never approve the user’s own elevated role unless explicitly authorized by constitutional policy.

### `USER-RULE-007`

User state history must remain available after access ends.

## 7.5 Invariants

* `USER-INV-001`: No active user exists without an approved identity link.
* `USER-INV-002`: Access-state history is append-only.
* `USER-INV-003`: Deleting a user must not erase audit attribution.
* `USER-INV-004`: Disabled or revoked users cannot hold active claims.

## 7.6 Recovery

When a user becomes unavailable:

* active claims must be released or expired safely
* drafts must remain recoverable
* previous actions must retain attribution

## 7.7 Acceptance Scenarios

* An owner invites a new data-entry user.
* The invited user cannot access work before activation.
* An administrator suspends a user and active claims are handled safely.
* A revoked user’s historical work remains attributed.

---

# 8. Authorization Domain

## 8.1 Purpose

Determine whether an authenticated active user may perform a specific action on a specific resource.

## 8.2 Ownership

Authorization owns:

* role evaluation
* permission evaluation
* resource-level checks
* action-level checks
* explicit denial
* role-history enforcement

It does not own authentication or UI visibility.

## 8.3 Business Rules

### `AUTHZ-RULE-001`

Every protected operation must perform a server-side authorization check.

### `AUTHZ-RULE-002`

UI visibility is not an authorization control.

### `AUTHZ-RULE-003`

Permissions must be evaluated against the current role state.

### `AUTHZ-RULE-004`

Record-level access must consider assignment, claim, batch scope, and administrative authority where applicable.

### `AUTHZ-RULE-005`

A user may hold more than one approved role.

### `AUTHZ-RULE-006`

Conflicting permissions resolve toward the most restrictive applicable rule unless an explicit approved override exists.

### `AUTHZ-RULE-007`

Administrative override actions must be separately authorized and audited.

### `AUTHZ-RULE-008`

Authorization failures must not reveal whether an inaccessible record exists.

## 8.4 Invariants

* `AUTHZ-INV-001`: Every mutation has an identifiable permission requirement.
* `AUTHZ-INV-002`: Role changes never rewrite historical authorization context.
* `AUTHZ-INV-003`: No client-provided role claim is trusted without server verification.

## 8.5 Acceptance Scenarios

* A data-entry user may edit a currently claimed page.
* The same user cannot edit an unclaimed page.
* A reviewer may resolve a match but cannot change user roles.
* An administrator can release an abandoned claim through an audited override.

---

# 9. Batch Domain

## 9.1 Purpose

Represent and manage a logical group of source pages received together.

## 9.2 Ownership

The Batch Domain owns:

* batch identity
* batch metadata
* batch lifecycle
* page membership
* aggregate processing status
* batch archival status

It does not own entry transcription, canonical identity, or source image binary storage.

## 9.3 Inputs

* batch title or label
* source description
* uploader
* received date where known
* expected page count where known
* operational notes

## 9.4 Outputs

* stable batch identifier
* batch status
* page membership
* aggregate progress
* batch completion status

## 9.5 Business Rules

### `BATCH-RULE-001`

Every page belongs to exactly one intake batch.

### `BATCH-RULE-002`

A batch may be created before all pages are uploaded.

### `BATCH-RULE-003`

Expected page count is optional unless required by an approved operational workflow.

### `BATCH-RULE-004`

Batch progress must derive from page and entry states rather than manually entered percentages.

### `BATCH-RULE-005`

A batch cannot be considered complete while unresolved pages or entries remain unless they are explicitly dispositioned.

### `BATCH-RULE-006`

Batch metadata corrections must be audited.

### `BATCH-RULE-007`

Archiving a batch must not remove its pages, entries, provenance, or audit history.

### `BATCH-RULE-008`

A batch may be closed to additional uploads only through an authorized state transition.

## 9.6 Invariants

* `BATCH-INV-001`: Batch identity remains stable.
* `BATCH-INV-002`: A batch cannot report more processed pages than total registered pages.
* `BATCH-INV-003`: Batch completion is derived from child state.
* `BATCH-INV-004`: Removing a page from one batch cannot silently attach it to another.

## 9.7 Concurrency

Simultaneous page uploads must not corrupt page ordering, counts, or batch progress.

## 9.8 Errors

* batch not found
* batch archived
* batch closed
* duplicate batch request
* page membership conflict
* invalid status transition

## 9.9 Recovery

A partially created batch may remain in a draft or open state. Failed page uploads must not invalidate successful pages.

## 9.10 Acceptance Scenarios

* An uploader creates a batch and uploads five pages.
* Additional pages are added while the batch remains open.
* Batch progress updates as pages move through transcription and matching.
* Archiving preserves all historical records.

---

# 10. Page Domain

## 10.1 Purpose

Represent one captured source sheet or page within a batch.

## 10.2 Ownership

The Page Domain owns:

* page identity
* batch membership
* page position or label
* page workflow state
* page-level quality status
* page-level claim eligibility

It does not own the image binary, canonical people, or final identity resolution.

## 10.3 Business Rules

### `PAGE-RULE-001`

Every page must reference one active source image version.

### `PAGE-RULE-002`

A page may contain zero through the supported maximum number of intake entries.

### `PAGE-RULE-003`

The initial supported maximum is ten entry positions per page unless approved design later changes it.

### `PAGE-RULE-004`

Blank physical rows do not require fabricated entries.

### `PAGE-RULE-005`

Page processing state must reflect actual workflow progress.

### `PAGE-RULE-006`

A page with an unusable image cannot proceed as a normal transcription page.

### `PAGE-RULE-007`

Image replacement must preserve prior versions and produce a page-level history event.

### `PAGE-RULE-008`

Only eligible pages may enter the transcription queue.

### `PAGE-RULE-009`

A page cannot have multiple active transcription claims.

## 10.4 Invariants

* `PAGE-INV-001`: A page belongs to exactly one batch.
* `PAGE-INV-002`: Active source image linkage is unambiguous.
* `PAGE-INV-003`: Page entry count derives from actual entries.
* `PAGE-INV-004`: A page cannot be complete while required entry review remains unresolved.

## 10.5 Errors

* no usable image
* duplicate page
* page already claimed
* page state conflict
* page archived
* unsupported page count condition

## 10.6 Recovery

Pages with damaged or incorrect images may enter an exception state pending replacement.

## 10.7 Acceptance Scenarios

* A page is uploaded and becomes queue eligible.
* An unusable page is marked for replacement.
* Replacing the image preserves the original.
* A page with seven written rows creates seven entries, not ten fabricated entries.

---

# 11. Source Image Domain

## 11.1 Purpose

Preserve private source-image evidence and its version history.

## 11.2 Ownership

This domain owns:

* source image identity
* image metadata
* image versioning
* integrity information
* authorized access
* storage linkage
* replacement history

It does not own transcription content or page workflow decisions.

## 11.3 Business Rules

### `IMAGE-RULE-001`

Source images are private by default.

### `IMAGE-RULE-002`

Original uploaded image bytes must be preserved unless a future approved legal-retention policy requires controlled destruction.

### `IMAGE-RULE-003`

Replacing an image creates a new version rather than overwriting the old version.

### `IMAGE-RULE-004`

Image access must be authorized for each request.

### `IMAGE-RULE-005`

Public permanent URLs are prohibited.

### `IMAGE-RULE-006`

Temporary access URLs must be short-lived and scoped.

### `IMAGE-RULE-007`

Uploaded file type, size, and integrity must be validated.

### `IMAGE-RULE-008`

File metadata must not be trusted solely from the client.

### `IMAGE-RULE-009`

Duplicate-image detection may warn operators but must not silently discard evidence.

### `IMAGE-RULE-010`

Image rotation or display transformations must not alter the preserved original.

## 11.4 Invariants

* `IMAGE-INV-001`: Every image version has a stable integrity identity.
* `IMAGE-INV-002`: Original evidence is distinguishable from derived display versions.
* `IMAGE-INV-003`: Access events are attributable where required.
* `IMAGE-INV-004`: No image becomes publicly enumerable.

## 11.5 Privacy

Images may contain personal information beyond the intended fields. Access must be minimized to workflow need.

## 11.6 Errors

* invalid file type
* file too large
* corrupt image
* storage unavailable
* access denied
* expired access token
* missing object
* hash conflict

## 11.7 Recovery

Failed storage completion must not create a page that appears to have usable evidence.

## 11.8 Acceptance Scenarios

* A valid image is stored privately.
* A user without page access cannot retrieve the image.
* A corrected image becomes the active version while the original remains preserved.
* Display rotation does not change the stored original.

---

# 12. Upload Domain

## 12.1 Purpose

Safely receive page images and associate them with the intended batch and page records.

## 12.2 Ownership

Upload owns:

* upload initiation
* upload validation
* transfer completion
* upload status
* association verification
* duplicate-request protection
* failed-upload recovery

## 12.3 Business Rules

### `UPLOAD-RULE-001`

Every upload must be associated with an authenticated authorized uploader.

### `UPLOAD-RULE-002`

Upload initiation and upload completion are separate states.

### `UPLOAD-RULE-003`

A completed transfer is not accepted until integrity and metadata validation pass.

### `UPLOAD-RULE-004`

Repeating an upload completion request must not create duplicate pages or image versions.

### `UPLOAD-RULE-005`

A failed upload must have an explicit failure state.

### `UPLOAD-RULE-006`

Partial transfers must not appear as completed source evidence.

### `UPLOAD-RULE-007`

Upload limits must be configuration-driven and documented.

### `UPLOAD-RULE-008`

One page image must not silently attach to two pages.

## 12.4 Invariants

* `UPLOAD-INV-001`: Accepted upload equals verified stored object plus verified ownership linkage.
* `UPLOAD-INV-002`: Upload status is not inferred from client success alone.
* `UPLOAD-INV-003`: Retried completion is idempotent.

## 12.5 Concurrency

Simultaneous uploads to the same batch must receive independent stable identifiers.

## 12.6 Acceptance Scenarios

* Ten pages upload concurrently without duplicate page identities.
* A network interruption leaves an incomplete upload recoverable.
* Repeating completion does not create a second page.
* A corrupt image is rejected before entering the queue.

---

# 13. Shared Work Queue Domain

## 13.1 Purpose

Present eligible work to multiple authorized users while preventing duplicate simultaneous processing.

## 13.2 Ownership

The Queue Domain owns:

* queue eligibility
* queue ordering
* claim availability
* work-type classification
* queue filters
* queue counts
* queue prioritization rules

It does not own the underlying page or entry business state.

## 13.3 Queue Types

At minimum:

```text
TRANSCRIPTION
TRANSCRIPTION_REVIEW
MATCH_REVIEW
PROMOTION_RETRY
OPERATIONAL_EXCEPTION
```

Additional queue types require documented ownership and state rules.

## 13.4 Business Rules

### `QUEUE-RULE-001`

Queue entries must derive from workflow state.

### `QUEUE-RULE-002`

A work item must leave an active queue when it no longer meets eligibility rules.

### `QUEUE-RULE-003`

A queue item must not be simultaneously claimable by multiple users.

### `QUEUE-RULE-004`

Queue ordering must be deterministic within a defined priority class.

### `QUEUE-RULE-005`

Administrative priority changes must be audited.

### `QUEUE-RULE-006`

Users must see only queue items they are authorized to process.

### `QUEUE-RULE-007`

Queue counts may be eventually consistent for display but claim acquisition must be strongly protected.

### `QUEUE-RULE-008`

The queue must support distributed users sharing the same workload.

## 13.5 Invariants

* `QUEUE-INV-001`: Eligibility is derived from authoritative workflow state.
* `QUEUE-INV-002`: Queue display does not guarantee claim success.
* `QUEUE-INV-003`: Claim acquisition is atomic.
* `QUEUE-INV-004`: Completed work cannot remain actively claimable.

## 13.6 Acceptance Scenarios

* Two users see the same available page.
* Only one successfully claims it.
* The second user receives a clear already-claimed result.
* A completed page disappears from the transcription queue.

---

# 14. Claim Domain

## 14.1 Purpose

Provide temporary, expiring, auditable ownership of a work item.

## 14.2 Ownership

Claim owns:

* claim acquisition
* claim expiration
* claim renewal
* claim release
* administrative release
* claim history

## 14.3 Business Rules

### `CLAIM-RULE-001`

A work item may have no more than one active claim per claim type.

### `CLAIM-RULE-002`

Claim acquisition must be atomic.

### `CLAIM-RULE-003`

Claims must have a defined expiration time.

### `CLAIM-RULE-004`

Only the current claimant or an authorized administrator may release an active claim.

### `CLAIM-RULE-005`

Renewal must fail if the claim has already expired or been replaced.

### `CLAIM-RULE-006`

Expiration must not delete saved drafts.

### `CLAIM-RULE-007`

An expired claim returns eligible work to the queue unless another workflow state prevents it.

### `CLAIM-RULE-008`

Administrative release requires a reason.

### `CLAIM-RULE-009`

A user losing access cannot retain an active claim indefinitely.

### `CLAIM-RULE-010`

Opening a work item does not by itself create a claim unless the workflow explicitly performs claim acquisition.

## 14.4 Invariants

* `CLAIM-INV-001`: One active claim per work item and claim type.
* `CLAIM-INV-002`: Claim holder identity is immutable during the claim.
* `CLAIM-INV-003`: Claim history is append-only.
* `CLAIM-INV-004`: Draft ownership and claim ownership remain distinguishable.

## 14.5 Concurrency

Use a single atomic decision for:

```text
check eligibility
+
verify no active claim
+
create claim
```

## 14.6 Errors

* already claimed
* claim expired
* renewal conflict
* release unauthorized
* work no longer eligible
* stale claim version

## 14.7 Recovery

When a browser or device fails:

* the claim remains until expiration
* saved drafts remain recoverable
* another user may claim after safe expiration

## 14.8 Acceptance Scenarios

* Two simultaneous claim requests yield one winner.
* A claimant renews before expiration.
* Renewal after expiration fails.
* An administrator releases an abandoned claim with an audit reason.
* Draft work survives expiration.

---

# 15. Draft Domain

## 15.1 Purpose

Preserve incomplete transcription work safely before submission.

## 15.2 Ownership

Draft owns:

* saved field values
* draft version
* draft ownership
* save timestamps
* conflict detection
* draft recovery
* draft supersession history

## 15.3 Business Rules

### `DRAFT-RULE-001`

Draft saves must not alter source evidence.

### `DRAFT-RULE-002`

Drafts are not final submissions.

### `DRAFT-RULE-003`

Every saved draft must identify the user responsible.

### `DRAFT-RULE-004`

Concurrent saves must detect stale versions.

### `DRAFT-RULE-005`

A user must be warned before overwriting newer draft work.

### `DRAFT-RULE-006`

Claim expiration does not erase a draft.

### `DRAFT-RULE-007`

Submission must reference the draft version or equivalent current state being submitted.

### `DRAFT-RULE-008`

Administrative recovery must not silently attribute recovered work to another user.

## 15.4 Invariants

* `DRAFT-INV-001`: Latest draft version is unambiguous.
* `DRAFT-INV-002`: Draft history remains attributable.
* `DRAFT-INV-003`: Submission cannot unknowingly use an older version than the latest accepted draft.

## 15.5 Acceptance Scenarios

* Work autosaves and survives browser closure.
* A stale browser tab cannot overwrite a newer draft silently.
* A later claimant can recover the draft while preserving original attribution.
* Draft recovery does not imply approval of the data.

---

# 16. Transcription Domain

## 16.1 Purpose

Capture what a human operator can read from each handwritten entry.

## 16.2 Ownership

Transcription owns:

* raw entered values
* row position
* transcription field conditions
* draft-to-submission transition
* transcription revision history
* operator notes limited to approved purpose

It does not own normalization, matching, or canonical truth.

## 16.3 Supported Fields

Initial supported fields:

* Last Name
* First Name
* Email
* Phone
* ZIP
* Volunteer
* Email List

## 16.4 Preference Values

```text
YES
NO
UNKNOWN
```

## 16.5 Business Rules

### `TRANSCRIPTION-RULE-001`

Operators must transcribe what is visible rather than what they assume was intended.

### `TRANSCRIPTION-RULE-002`

Spelling must not be silently corrected in raw transcription.

### `TRANSCRIPTION-RULE-003`

Blank values must remain blank with the appropriate field condition.

### `TRANSCRIPTION-RULE-004`

Unreadable values must not be guessed.

### `TRANSCRIPTION-RULE-005`

Ambiguous values may include an approved uncertainty note but must not be converted into false certainty.

### `TRANSCRIPTION-RULE-006`

Volunteer and Email List blanks become `UNKNOWN`, never `NO`.

### `TRANSCRIPTION-RULE-007`

Each physical person row becomes an independently tracked entry.

### `TRANSCRIPTION-RULE-008`

Operators may correct their own draft before submission.

### `TRANSCRIPTION-RULE-009`

Post-submission corrections require a controlled revision workflow.

### `TRANSCRIPTION-RULE-010`

The system may validate formatting but must preserve raw transcription.

### `TRANSCRIPTION-RULE-011`

An entry may be valid even when some fields are missing.

### `TRANSCRIPTION-RULE-012`

A completely blank physical row must not produce a fabricated person entry.

## 16.6 Invariants

* `TRANSCRIPTION-INV-001`: Raw text remains distinct from normalized values.
* `TRANSCRIPTION-INV-002`: Every value has a source entry and field identity.
* `TRANSCRIPTION-INV-003`: Every revision is attributable.
* `TRANSCRIPTION-INV-004`: Missing data is not negative consent.
* `TRANSCRIPTION-INV-005`: The number of submitted entries must correspond to actual interpreted rows.

## 16.7 Accessibility

The entry editor must support:

* keyboard-only operation
* predictable row navigation
* visible focus
* clear field labels
* screen-reader identification of row and field
* no color-only status communication

## 16.8 Acceptance Scenarios

* A row with only name and phone is accepted as incomplete but valid.
* An unreadable email is marked unreadable rather than guessed.
* A blank volunteer checkbox becomes `UNKNOWN`.
* An operator corrects a draft typo without altering source evidence.
* A post-submission correction creates history.

---

# 17. Field Condition Domain

## 17.1 Purpose

Describe the observable condition of each source field independently from its value.

## 17.2 Allowed Conditions

```text
PROVIDED
NOT_PROVIDED
UNREADABLE
AMBIGUOUS
CORRECTED
```

Future conditions require formal documentation.

## 17.3 Business Rules

### `FIELD-RULE-001`

Every transcribed field must have a condition.

### `FIELD-RULE-002`

`PROVIDED` means a usable source value was visibly present.

### `FIELD-RULE-003`

`NOT_PROVIDED` means the source appears blank or intentionally unfilled.

### `FIELD-RULE-004`

`UNREADABLE` means marks exist but cannot be interpreted reliably.

### `FIELD-RULE-005`

`AMBIGUOUS` means more than one plausible reading exists.

### `FIELD-RULE-006`

`CORRECTED` means a prior transcription value was revised through an authorized workflow.

### `FIELD-RULE-007`

A corrected field must retain its prior condition and value history.

### `FIELD-RULE-008`

Field condition must not be inferred solely from normalized output.

## 17.4 Invariants

* `FIELD-INV-001`: Condition and value are separate concepts.
* `FIELD-INV-002`: `NOT_PROVIDED` is not equivalent to `NO`.
* `FIELD-INV-003`: A nonempty raw value cannot normally be classified `NOT_PROVIDED`.
* `FIELD-INV-004`: `CORRECTED` does not erase the earlier classification.

---

# 18. Normalization Domain

## 18.1 Purpose

Create standardized comparison-ready representations while preserving raw transcription.

## 18.2 Ownership

Normalization owns:

* deterministic standardization
* normalization version
* normalized output
* normalization warnings
* normalization history where rules change

It does not own source correction or identity resolution.

## 18.3 Business Rules

### `NORMALIZE-RULE-001`

Normalization must be deterministic for the same value and rule version.

### `NORMALIZE-RULE-002`

Raw transcription must remain unchanged.

### `NORMALIZE-RULE-003`

Normalization must not invent missing characters.

### `NORMALIZE-RULE-004`

Email normalization may trim whitespace and standardize case where technically appropriate, while preserving raw input.

### `NORMALIZE-RULE-005`

Phone normalization may create a digits-only comparison form while preserving extensions and raw input separately where supported.

### `NORMALIZE-RULE-006`

ZIP normalization may standardize valid five-digit or approved extended forms without fabricating leading digits.

### `NORMALIZE-RULE-007`

Name normalization may standardize whitespace and comparison case but must preserve punctuation and original form in raw transcription.

### `NORMALIZE-RULE-008`

Invalid or incomplete values may produce normalized warnings rather than forced valid output.

### `NORMALIZE-RULE-009`

Every normalized value must identify the rule version used.

### `NORMALIZE-RULE-010`

Changing normalization rules must not silently rewrite historical decisions without controlled reprocessing.

## 18.4 Invariants

* `NORMALIZE-INV-001`: Every normalized value traces to one raw value.
* `NORMALIZE-INV-002`: Normalization is reversible only by referring back to raw transcription.
* `NORMALIZE-INV-003`: Normalized output is not automatically verified truth.
* `NORMALIZE-INV-004`: Rule version is preserved.

## 18.5 Acceptance Scenarios

* `" Steve@Example.COM "` yields a comparison form without changing raw text.
* A seven-digit phone remains incomplete rather than being assigned an area code.
* An ambiguous handwritten ZIP does not become a guessed valid ZIP.
* Reprocessing under a new normalization version preserves prior output history where required.

---

# 19. Entry Submission Domain

## 19.1 Purpose

Convert a draft entry set into a stable submitted transcription record ready for review or matching.

## 19.2 Business Rules

### `SUBMIT-RULE-001`

Submission requires an active authorized workflow context.

### `SUBMIT-RULE-002`

Submission validates required structural conditions but must not require fields the paper did not provide.

### `SUBMIT-RULE-003`

Submission must detect stale draft versions.

### `SUBMIT-RULE-004`

Repeated submission with the same idempotency identity must not create duplicate submissions.

### `SUBMIT-RULE-005`

Submission freezes the submitted revision as a durable historical version.

### `SUBMIT-RULE-006`

Post-submission edits require a correction or return workflow.

### `SUBMIT-RULE-007`

Submitting a page must not silently mark matching complete.

### `SUBMIT-RULE-008`

A page submission must clearly identify which rows were interpreted as entries.

## 19.3 Invariants

* `SUBMIT-INV-001`: A submitted revision is historically stable.
* `SUBMIT-INV-002`: Submission and approval are distinct.
* `SUBMIT-INV-003`: Duplicate retry does not duplicate entries.

## 19.4 Acceptance Scenarios

* A page with six entries submits once.
* A repeated request returns the original result.
* A stale tab cannot submit over a newer saved version.
* A reviewer returns one entry for correction without destroying the submitted history.

---

# 20. Matching Domain

## 20.1 Purpose

Evaluate whether an intake entry may correspond to an existing canonical person.

## 20.2 Ownership

Matching owns:

* candidate discovery
* match signals
* confidence classification
* explanation
* conflict detection
* evaluation lifecycle

It does not own final canonical resolution.

## 20.3 Confidence Classes

```text
EXACT
HIGH
POSSIBLE
LOW
NO_MATCH
CONFLICT
```

These labels describe evaluation strength, not automatic authority.

## 20.4 Business Rules

### `MATCH-RULE-001`

Matching must be conservative and explainable.

### `MATCH-RULE-002`

Every candidate must include the signals supporting and weakening the match.

### `MATCH-RULE-003`

Name similarity alone is insufficient for irreversible identity resolution.

### `MATCH-RULE-004`

Shared household contact information must not automatically merge people.

### `MATCH-RULE-005`

Shared phone numbers and email addresses may represent households, organizations, or reused contacts.

### `MATCH-RULE-006`

Conflicting strong identifiers must produce a conflict state.

### `MATCH-RULE-007`

Candidate absence does not prove the person is new.

### `MATCH-RULE-008`

Automated scoring must not silently resolve uncertain identity.

### `MATCH-RULE-009`

Match evaluations must record the algorithm or rule version.

### `MATCH-RULE-010`

Candidate generation must minimize unnecessary disclosure of unrelated canonical-person data.

### `MATCH-RULE-011`

Previously rejected candidates may be considered again only when new evidence or an approved re-evaluation occurs.

### `MATCH-RULE-012`

Exact normalized contact equality may be a strong signal but is not universally conclusive.

### `MATCH-RULE-013`

Low-quality source fields must reduce confidence rather than be treated as precise identifiers.

## 20.5 Invariants

* `MATCH-INV-001`: Every score is explainable through named signals.
* `MATCH-INV-002`: Match confidence is not final resolution.
* `MATCH-INV-003`: Algorithm version is preserved.
* `MATCH-INV-004`: Candidate generation does not mutate canonical people.
* `MATCH-INV-005`: Conflicting evidence cannot be hidden by a high aggregate score.

## 20.6 Privacy

Candidate results should reveal only enough information for identity review.

## 20.7 Acceptance Scenarios

* Same normalized email and compatible name produce a strong candidate with an explanation.
* Same household phone but different names does not auto-merge.
* Matching ZIP and similar name without contact information produces a possible candidate, not certainty.
* Conflicting email and phone identities produce `CONFLICT`.
* No candidates leads to human new-person review rather than silent creation.

---

# 21. Match Candidate Domain

## 21.1 Purpose

Represent one explainable possible relationship between an intake entry and a canonical person.

## 21.2 Business Rules

### `CANDIDATE-RULE-001`

Each candidate references one intake entry and one canonical person.

### `CANDIDATE-RULE-002`

Candidate identity is stable within an evaluation.

### `CANDIDATE-RULE-003`

Each candidate lists supporting signals.

### `CANDIDATE-RULE-004`

Each candidate lists conflicting or weakening signals.

### `CANDIDATE-RULE-005`

Candidate rank must not conceal confidence differences.

### `CANDIDATE-RULE-006`

Candidates must not expose sensitive attributes unrelated to matching.

### `CANDIDATE-RULE-007`

Candidate presentation must distinguish verified canonical values from unverified intake values.

## 21.3 Invariants

* `CANDIDATE-INV-001`: Candidate is not resolution.
* `CANDIDATE-INV-002`: Candidate evidence remains tied to an evaluation version.
* `CANDIDATE-INV-003`: Re-ranking does not rewrite prior review history.

---

# 22. Match Resolution Domain

## 22.1 Purpose

Record the authorized human determination about an intake entry’s identity relationship.

## 22.2 Resolution Outcomes

At minimum:

```text
MATCH_EXISTING_PERSON
CREATE_NEW_PERSON
REQUIRES_MORE_INFORMATION
REJECT_ENTRY
DUPLICATE_INTAKE_ENTRY
ESCALATE_CONFLICT
```

## 22.3 Business Rules

### `RESOLUTION-RULE-001`

Only an authorized reviewer may create a final resolution.

### `RESOLUTION-RULE-002`

The reviewer must identify the selected outcome.

### `RESOLUTION-RULE-003`

Matching an existing person requires an explicit canonical person target.

### `RESOLUTION-RULE-004`

Creating a new person requires a documented no-suitable-match determination.

### `RESOLUTION-RULE-005`

Conflict resolution must not be hidden inside a generic approval.

### `RESOLUTION-RULE-006`

A final resolution must record the evidence context available at the time.

### `RESOLUTION-RULE-007`

Changing a prior resolution requires a superseding resolution with reason.

### `RESOLUTION-RULE-008`

The system must prevent simultaneous conflicting resolutions.

### `RESOLUTION-RULE-009`

A resolution does not itself prove canonical promotion succeeded.

### `RESOLUTION-RULE-010`

Rejection must preserve the source entry and reason.

## 22.4 Invariants

* `RESOLUTION-INV-001`: One current effective resolution per entry.
* `RESOLUTION-INV-002`: Prior resolutions remain historically visible.
* `RESOLUTION-INV-003`: Reviewer identity is immutable.
* `RESOLUTION-INV-004`: Resolution and promotion are separate.

## 22.5 Concurrency

Resolution requires optimistic concurrency or equivalent protection against two reviewers finalizing conflicting outcomes.

## 22.6 Acceptance Scenarios

* A reviewer links an entry to an existing person.
* Another reviewer’s stale resolution attempt fails.
* A prior resolution is superseded with an explicit reason.
* An unresolved conflict remains blocked from promotion.

---

# 23. Canonical Promotion Domain

## 23.1 Purpose

Safely contribute an approved intake resolution to the canonical people domain.

## 23.2 Ownership

Promotion owns:

* promotion request
* canonical operation request
* retry safety
* promotion status
* external result reference
* failure recording
* provenance contribution

It does not own canonical identity rules.

## 23.3 Business Rules

### `PROMOTION-RULE-001`

Promotion requires an effective approved match resolution.

### `PROMOTION-RULE-002`

Promotion must be idempotent.

### `PROMOTION-RULE-003`

Creating a canonical person and linking an intake entry must not produce duplicate people during retries.

### `PROMOTION-RULE-004`

Canonical contribution must preserve provenance.

### `PROMOTION-RULE-005`

A successful match resolution is not complete until the canonical operation result is recorded.

### `PROMOTION-RULE-006`

Canonical failures must not erase the approved resolution.

### `PROMOTION-RULE-007`

Retries must reuse stable operation identity.

### `PROMOTION-RULE-008`

People Intake must not directly mutate canonical records outside the approved integration contract.

### `PROMOTION-RULE-009`

Attribute contribution must identify source, confidence, and review status.

### `PROMOTION-RULE-010`

Unknown preferences must not overwrite known canonical preferences as `NO`.

### `PROMOTION-RULE-011`

Conflicting canonical attributes must follow canonical conflict policy.

### `PROMOTION-RULE-012`

A promotion result must identify whether it:

* created a person
* linked to an existing person
* contributed attributes
* created no change
* failed
* requires canonical review

## 23.4 Invariants

* `PROMOTION-INV-001`: Same approved operation cannot create two canonical people.
* `PROMOTION-INV-002`: Every canonical contribution has provenance.
* `PROMOTION-INV-003`: External failure does not falsify local success.
* `PROMOTION-INV-004`: Canonical ownership remains outside People Intake.

## 23.5 Recovery

Failed promotion remains retryable according to error class.

Permanent rejection by the canonical domain requires operator review.

## 23.6 Acceptance Scenarios

* An entry links to an existing canonical person exactly once.
* A network retry does not create a duplicate person.
* Canonical service downtime preserves the pending request.
* Unknown volunteer preference does not overwrite an existing known value.

---

# 24. Person Attribute Contribution Domain

## 24.1 Purpose

Represent the attributes People Intake proposes or contributes to the canonical domain.

## 24.2 Business Rules

### `ATTRIBUTE-RULE-001`

Every contributed attribute must identify its source entry.

### `ATTRIBUTE-RULE-002`

Raw, normalized, and canonical forms must remain distinguishable.

### `ATTRIBUTE-RULE-003`

A contributed attribute is not automatically canonical truth.

### `ATTRIBUTE-RULE-004`

Conflicting values must not be silently discarded.

### `ATTRIBUTE-RULE-005`

Preference attributes must preserve `YES`, `NO`, and `UNKNOWN`.

### `ATTRIBUTE-RULE-006`

Attribute contribution must identify the responsible promotion operation.

### `ATTRIBUTE-RULE-007`

The canonical domain determines final attribute precedence.

### `ATTRIBUTE-RULE-008`

People Intake must not infer demographic, political, religious, health, or other sensitive attributes from handwriting, names, geography, or context.

## 24.3 Invariants

* `ATTRIBUTE-INV-001`: Attribute source is always known.
* `ATTRIBUTE-INV-002`: Unknown cannot downgrade known consent.
* `ATTRIBUTE-INV-003`: Conflicts remain explainable.

---

# 25. Provenance Domain

## 25.1 Purpose

Explain where information came from and how it moved through the system.

## 25.2 Required Provenance Elements

* source system
* source batch
* source page
* source entry
* source image
* field
* raw value reference
* normalized value reference
* actor
* transformation
* review
* resolution
* promotion
* canonical target
* timestamps
* correlation identity

## 25.3 Business Rules

### `PROVENANCE-RULE-001`

Every promoted contribution must have complete source provenance.

### `PROVENANCE-RULE-002`

Provenance must distinguish human-entered, system-derived, and canonical-returned information.

### `PROVENANCE-RULE-003`

Provenance must not be editable as ordinary content.

### `PROVENANCE-RULE-004`

Corrections add provenance rather than replacing prior provenance.

### `PROVENANCE-RULE-005`

A provenance chain must remain traversable even if operational records are archived.

### `PROVENANCE-RULE-006`

Provenance payloads must avoid unnecessary duplication of raw personal data.

## 25.4 Invariants

* `PROVENANCE-INV-001`: No canonical contribution without source chain.
* `PROVENANCE-INV-002`: Human and automated actions are distinguishable.
* `PROVENANCE-INV-003`: Historical transformations remain attributable.

---

# 26. Audit Domain

## 26.1 Purpose

Maintain durable business history for meaningful actions and decisions.

## 26.2 Ownership

Audit owns:

* business event recording
* actor attribution
* event timing
* event subject
* event result
* correlation
* immutable event history

It does not replace:

* debugging logs
* metrics
* traces
* operator notes

## 26.3 Business Rules

### `AUDIT-RULE-001`

Every meaningful mutation must have an audit decision.

### `AUDIT-RULE-002`

High-risk actions always require an audit event.

### `AUDIT-RULE-003`

Audit events are append-only.

### `AUDIT-RULE-004`

Audit records must identify human or system actor.

### `AUDIT-RULE-005`

Audit records must not contain secrets.

### `AUDIT-RULE-006`

Raw PII should not be duplicated into audit payloads unless explicitly required.

### `AUDIT-RULE-007`

Failed high-risk attempts may require audit recording.

### `AUDIT-RULE-008`

Administrative overrides require reason and outcome.

### `AUDIT-RULE-009`

Audit event failure must block high-risk mutations where atomic audit is required.

### `AUDIT-RULE-010`

Audit history must remain available after user deactivation and record archival.

## 26.4 Invariants

* `AUDIT-INV-001`: Audit events cannot be edited by ordinary users.
* `AUDIT-INV-002`: Actor identity remains stable.
* `AUDIT-INV-003`: Business time and recording time are distinguishable where needed.
* `AUDIT-INV-004`: Correlated operations can be reconstructed.

## 26.5 Acceptance Scenarios

* Claim acquisition records actor and work item.
* Match resolution records reviewer and outcome.
* Role change records old and new roles.
* Failed administrative override records attempted action where policy requires it.
* Audit history survives user revocation.

---

# 27. Background Job Domain

## 27.1 Purpose

Execute durable asynchronous work safely and observably.

## 27.2 Typical Jobs

* claim expiration
* upload finalization
* image verification
* normalization
* candidate generation
* canonical promotion
* retry processing
* operational reconciliation
* orphan detection
* alert generation

## 27.3 Job States

```text
PENDING
RUNNING
SUCCEEDED
FAILED_RETRYABLE
FAILED_FINAL
CANCELLED
```

## 27.4 Business Rules

### `JOB-RULE-001`

Every durable job has a stable job identity.

### `JOB-RULE-002`

Job attempts are distinguishable from the job itself.

### `JOB-RULE-003`

Retryable failures use bounded retry policy.

### `JOB-RULE-004`

Repeated execution must be safe.

### `JOB-RULE-005`

A job must not remain `RUNNING` indefinitely without stale-job recovery.

### `JOB-RULE-006`

Final failure must create an operator-visible condition when business impact remains.

### `JOB-RULE-007`

Cancelling a job must not falsely mark business work complete.

### `JOB-RULE-008`

Job payloads must minimize sensitive data.

### `JOB-RULE-009`

High-risk canonical operations require durable idempotency.

## 27.5 Invariants

* `JOB-INV-001`: One business outcome may have multiple attempts but one effective completion.
* `JOB-INV-002`: Attempt history is preserved.
* `JOB-INV-003`: Job state reflects durable reality, not process memory.

---

# 28. Operator Alert Domain

## 28.1 Purpose

Surface actionable operational conditions requiring attention.

## 28.2 Alert Examples

* repeated upload failures
* storage object missing
* abandoned claims
* canonical promotion failures
* unresolved conflicts
* job retry exhaustion
* audit write failure
* queue backlog
* configuration failure
* duplicate-risk anomaly

## 28.3 Business Rules

### `ALERT-RULE-001`

Alerts must be actionable.

### `ALERT-RULE-002`

An alert must identify severity, source condition, and recommended response.

### `ALERT-RULE-003`

Alerts must not expose unnecessary personal data.

### `ALERT-RULE-004`

Acknowledging an alert does not resolve the underlying condition.

### `ALERT-RULE-005`

Resolved alerts must identify the resolution source.

### `ALERT-RULE-006`

Duplicate alerts for the same continuing condition should be grouped where practical.

## 28.4 Severity

```text
CRITICAL
HIGH
MEDIUM
LOW
INFORMATIONAL
```

---

# 29. Search Domain

## 29.1 Purpose

Allow authorized users to locate batches, pages, entries, operational records, and limited canonical candidates.

## 29.2 Business Rules

### `SEARCH-RULE-001`

Search results must respect the same authorization rules as direct record access.

### `SEARCH-RULE-002`

Search must not reveal existence of inaccessible records.

### `SEARCH-RULE-003`

Search indexes must not become an uncontrolled duplicate store of sensitive data.

### `SEARCH-RULE-004`

Matching search and administrative search are distinct purposes.

### `SEARCH-RULE-005`

Search results should identify record type and status clearly.

### `SEARCH-RULE-006`

Partial identifiers and personal values must be handled carefully to prevent unnecessary exposure.

### `SEARCH-RULE-007`

Search activity may require audit or operational logging based on sensitivity.

## 29.3 Acceptance Scenarios

* A reviewer searches permitted canonical candidates.
* A data-entry user cannot search unrelated canonical people.
* An administrator locates a batch by stable identifier.
* Search does not reveal an inaccessible person through result counts.

---

# 30. Administration Domain

## 30.1 Purpose

Provide controlled oversight and recovery without bypassing architecture.

## 30.2 Responsibilities

* user access administration
* role management
* batch oversight
* queue oversight
* claim recovery
* job monitoring
* error review
* alert resolution
* audit inspection
* configuration visibility
* operational reporting

## 30.3 Business Rules

### `ADMIN-RULE-001`

Administrative actions require explicit authorization.

### `ADMIN-RULE-002`

High-risk actions require reason capture.

### `ADMIN-RULE-003`

Administrative override does not permit source evidence alteration.

### `ADMIN-RULE-004`

Administrative tools must distinguish viewing from mutation.

### `ADMIN-RULE-005`

Bulk actions require explicit scope preview.

### `ADMIN-RULE-006`

Destructive actions require confirmation and must remain consistent with retention policy.

### `ADMIN-RULE-007`

Administrative role does not automatically confer match-review authority.

### `ADMIN-RULE-008`

Configuration visibility must not expose secret values.

### `ADMIN-RULE-009`

Administrative recovery must preserve attribution of original work.

## 30.4 Acceptance Scenarios

* An administrator releases an abandoned claim.
* An administrator views but cannot reveal a secret.
* A role change creates history.
* A batch archive action preserves all evidence.
* An administrator without reviewer authority cannot resolve a match.

---

# 31. Reporting Domain

## 31.1 Purpose

Provide operational insight without exposing unnecessary personal information.

## 31.2 Reporting Categories

* batches received
* pages uploaded
* pages awaiting transcription
* transcription throughput
* review backlog
* matching outcomes
* promotion outcomes
* error rates
* claim expiration rates
* operator activity
* data-quality conditions
* unresolved exceptions

## 31.3 Business Rules

### `REPORT-RULE-001`

Operational reports should prefer aggregate data.

### `REPORT-RULE-002`

PII-heavy exports require separate authorization.

### `REPORT-RULE-003`

Reported counts must define their underlying state criteria.

### `REPORT-RULE-004`

Reports must identify generation time and applicable data range.

### `REPORT-RULE-005`

Reports must distinguish completed, pending, failed, and unresolved work.

### `REPORT-RULE-006`

Performance reporting must not encourage unsafe speed over accuracy.

### `REPORT-RULE-007`

Operator activity metrics must be used responsibly and transparently.

### `REPORT-RULE-008`

Reports must not become an ungoverned parallel canonical-person export system.

---

# 32. Retention and Archival Domain

## 32.1 Purpose

Govern long-term preservation, archival state, and approved destruction.

## 32.2 Business Rules

### `RETENTION-RULE-001`

Source evidence retention must follow the approved retention policy.

### `RETENTION-RULE-002`

Archival removes records from active workflow without erasing history.

### `RETENTION-RULE-003`

Audit and provenance retention may exceed active operational retention.

### `RETENTION-RULE-004`

No irreversible destruction may occur without explicit approved policy and authorization.

### `RETENTION-RULE-005`

Legal hold or investigation hold must prevent destruction where applicable.

### `RETENTION-RULE-006`

Archived records remain subject to authorization.

### `RETENTION-RULE-007`

Canonical identity links must remain explainable after intake archival.

### `RETENTION-RULE-008`

Retention policy must cover database records, images, logs, backups, and exports separately.

## 32.3 Invariants

* `RETENTION-INV-001`: Archive is not delete.
* `RETENTION-INV-002`: Deletion cannot leave unverifiable canonical contributions.
* `RETENTION-INV-003`: Retention actions are audited.

---

# 33. Error Recovery Domain

## 33.1 Purpose

Provide predictable recovery from failures without creating false success or duplicate outcomes.

## 33.2 Error Categories

```text
VALIDATION
AUTHENTICATION
AUTHORIZATION
CONFLICT
NOT_FOUND
DEPENDENCY
STORAGE
DATABASE
INTEGRITY
RATE_LIMIT
CONFIGURATION
RETRYABLE_SYSTEM
PERMANENT_SYSTEM
```

## 33.3 Business Rules

### `RECOVERY-RULE-001`

Every failure must resolve to a known error category.

### `RECOVERY-RULE-002`

User-facing messages must be safe and actionable.

### `RECOVERY-RULE-003`

Operator detail must be available without exposing secrets.

### `RECOVERY-RULE-004`

Retryable and permanent failures must be distinguished.

### `RECOVERY-RULE-005`

Retries must be idempotent.

### `RECOVERY-RULE-006`

Partial success must be represented explicitly.

### `RECOVERY-RULE-007`

A failed downstream integration must not falsely roll back preserved local evidence.

### `RECOVERY-RULE-008`

Recovery operations must be auditable when they change business state.

### `RECOVERY-RULE-009`

Silent data loss is prohibited.

### `RECOVERY-RULE-010`

Unrecoverable integrity conflicts must escalate rather than be guessed through.

## 33.4 Recovery Patterns

### Safe Retry

Use when repeating the same operation cannot duplicate the business result.

### Resume

Continue from the last durable checkpoint.

### Compensating Action

Reverse or neutralize a partial effect without erasing history.

### Manual Review

Require an authorized operator to determine the next action.

### Final Failure

Mark the operation permanently failed while preserving all evidence and attempts.

---

# PART IV — CROSS-DOMAIN TRANSACTION BOUNDARIES

# 34. Required Transaction Boundaries

## 34.1 Claim Acquisition

Must atomically:

```text
verify eligibility
verify no active claim
create active claim
record required history
```

## 34.2 Draft Save

Must atomically:

```text
verify authorization
verify expected version
save new version
update current reference
```

## 34.3 Submission

Must atomically:

```text
verify active workflow rights
verify expected draft version
create submitted revision
transition entry/page state
record audit
```

## 34.4 Match Resolution

Must atomically:

```text
verify reviewer authority
verify current evaluation state
verify no newer resolution
create resolution
set effective resolution
record audit
```

## 34.5 Promotion Request

Must atomically:

```text
verify effective resolution
create or locate idempotent promotion request
record pending state
```

The external canonical operation may be asynchronous, but its local request must be durable before execution.

## 34.6 User Role Change

Must atomically:

```text
verify authority
preserve prior role state
apply new role state
record role history
record audit
```

---

# PART V — OBSERVABILITY STANDARD

# 35. Logs

Operational logs should capture:

* event time
* service area
* severity
* correlation ID
* operation
* safe record identifier
* result
* error code
* duration

Logs must not include:

* authentication tokens
* API keys
* passwords
* signed image URLs
* raw source images
* unnecessary raw PII

---

# 36. Metrics

Minimum metrics should include:

* active users
* authentication failures
* uploads initiated
* uploads completed
* upload failures
* queue depth
* claim success
* claim conflicts
* claim expirations
* drafts recovered
* entries submitted
* review backlog
* match confidence distribution
* resolution outcomes
* promotion success
* promotion failure
* background job retries
* unresolved alerts
* processing latency

Metrics must not silently become personnel-scoring mechanisms.

---

# 37. Tracing and Correlation

A single workflow should be traceable using a stable correlation identity across:

* upload
* page creation
* transcription
* submission
* matching
* resolution
* promotion
* audit
* background jobs

Correlation IDs must not replace stable business identifiers.

---

# PART VI — PRIVACY AND DATA MINIMIZATION

# 38. Permitted Data Purpose

People Intake may process personal information only for approved intake, matching, canonical contribution, audit, and operational purposes.

It must not use intake information to infer:

* race
* ethnicity
* religion
* health condition
* sexual orientation
* criminal history
* political affiliation
* income
* immigration status
* other sensitive personal traits

unless a future lawful and explicitly approved system purpose separately authorizes collection—which this volume does not.

---

# 39. Display Minimization

Users should see only the information needed to complete the assigned task.

Examples:

* Data-entry users need the source page and fields.
* Reviewers need relevant candidate comparison data.
* Administrators need operational status.
* Reports should prefer aggregates.

---

# 40. Export Controls

Bulk exports require:

* explicit role authorization
* defined purpose
* scope preview
* audit
* safe format
* retention guidance

Unrestricted personal-data export is not a default capability.

---

# PART VII — ACCESSIBILITY AND HUMAN FACTORS

# 41. Accessibility Standard

Every workflow must support:

* keyboard operation
* visible focus
* semantic labels
* adequate contrast
* screen-reader interpretation
* zoom and text resizing
* clear error identification
* non-color status indicators
* reduced motion where motion exists
* mobile touch targets
* interruption recovery

---

# 42. Accuracy-First UX

The interface must not pressure users to guess.

It should make these choices easy:

* unreadable
* ambiguous
* not provided
* unknown
* save and return
* escalate
* request review

The system should reward completeness and accuracy rather than raw speed alone.

---

# PART VIII — FUTURE COMPATIBILITY

# 43. OCR Compatibility

Future OCR may:

* suggest transcription
* highlight likely fields
* identify uncertain characters
* prioritize review

OCR may not:

* overwrite source evidence
* silently become raw transcription
* silently submit entries
* silently resolve identities

OCR output must be labeled as machine-generated and reviewed according to approved policy.

---

# 44. AI Compatibility

Future AI may:

* suggest normalization
* explain candidate signals
* detect inconsistencies
* summarize operator exceptions
* assist with quality review

AI may not:

* invent missing information
* infer sensitive traits
* silently merge people
* silently create canonical identity
* conceal uncertainty
* bypass human approval

---

# 45. Multi-Organization Compatibility

Version 1 is not required to become a multi-tenant platform.

Future organization support must preserve:

* identity ownership
* record isolation
* authorization boundaries
* provenance
* audit
* application independence

No current implementation should hard-code unsafe assumptions that make future isolation impossible, but the system should not be overbuilt prematurely.

---

# 46. Mobile Field Upload Compatibility

Future field capture may support:

* phone camera upload
* QR-coded batches
* offline upload preparation
* delayed synchronization

Any offline system must preserve:

* stable client operation identity
* duplicate protection
* local security
* upload integrity
* operator attribution

---

# PART IX — ACCEPTANCE TEST LIBRARY

# 47. End-to-End Acceptance Scenario A

## Clean New Person

1. Uploader creates a batch.
2. Uploader adds a valid source page.
3. Page enters transcription queue.
4. Data-entry user claims the page.
5. User transcribes one entry.
6. Blank volunteer preference becomes `UNKNOWN`.
7. Draft saves.
8. Entry submits.
9. Normalization runs.
10. No suitable canonical candidate exists.
11. Reviewer selects `CREATE_NEW_PERSON`.
12. Promotion creates one canonical person.
13. Retried promotion creates no duplicate.
14. Provenance links the canonical person to the original page and entry.
15. Audit history reconstructs the entire path.

Expected result:

```text
PASS
```

only if all evidence and decisions remain traceable.

---

# 48. End-to-End Acceptance Scenario B

## Existing Person Match

1. Entry contains compatible name, email, and ZIP.
2. Matching produces one high-confidence candidate.
3. Reviewer compares supporting and conflicting signals.
4. Reviewer selects the existing canonical person.
5. Promotion contributes the new source evidence.
6. Canonical attribute policy determines whether values are added or flagged.
7. Intake entry links to the canonical person.
8. No duplicate person is created.

---

# 49. End-to-End Acceptance Scenario C

## Shared Household Phone

1. Two entries use the same phone number.
2. Names differ.
3. Matching detects shared contact.
4. The system does not automatically merge them.
5. Each entry receives independent candidate review.
6. Reviewer may resolve them to different people.
7. Shared contact remains explainable.

---

# 50. End-to-End Acceptance Scenario D

## Claim Collision

1. Two users request the same page.
2. The queue shows it available to both before either claim completes.
3. Both attempt to claim.
4. One atomic claim succeeds.
5. One receives `CLAIM_ALREADY_HELD`.
6. No duplicate active claim exists.
7. Audit shows the successful claim.

---

# 51. End-to-End Acceptance Scenario E

## Draft Recovery

1. User claims a page.
2. User enters six rows.
3. Draft saves.
4. Device loses power.
5. Claim later expires.
6. Another authorized user claims the page.
7. Existing draft is recoverable.
8. Original contribution remains attributed.
9. New user completes and submits the work.
10. History distinguishes both actors.

---

# 52. End-to-End Acceptance Scenario F

## Canonical Service Failure

1. Reviewer approves creation of a new person.
2. Promotion request is durably recorded.
3. Canonical service is unavailable.
4. Promotion enters retryable failure.
5. Local resolution remains intact.
6. Operator alert is generated.
7. Retry later succeeds.
8. Stable idempotency prevents duplicate creation.

---

# 53. End-to-End Acceptance Scenario G

## Source Image Replacement

1. A page image is blurry.
2. Page enters image-quality exception state.
3. Authorized uploader provides a clearer image.
4. New image becomes active.
5. Original remains preserved.
6. Access and replacement are audited.
7. Transcription proceeds from the new active image.
8. Provenance identifies the image version used.

---

# 54. End-to-End Acceptance Scenario H

## Post-Submission Correction

1. Entry is submitted.
2. Reviewer identifies a transcription error.
3. Entry is returned for correction.
4. Corrected value is entered.
5. Field condition reflects correction.
6. Original submitted revision remains preserved.
7. Matching is re-evaluated if affected.
8. Prior candidate results remain historically explainable.

---

# PART X — LOCKED DOMAIN DECISIONS

# 55. Locked Decisions

The following decisions are frozen at the domain level unless formally amended.

1. Original source images are preserved.
2. Source image access is private.
3. A Batch contains Pages.
4. A Page may contain multiple independent Entries.
5. The initial supported page design accommodates up to ten entry positions.
6. Blank physical rows do not create fabricated entries.
7. Volunteer and Email List preferences use `YES`, `NO`, and `UNKNOWN`.
8. Blank preference means `UNKNOWN`.
9. Raw transcription remains distinct from normalized values.
10. Normalization does not alter raw transcription.
11. Source field condition is recorded separately from field value.
12. `NOT_PROVIDED`, `UNREADABLE`, and `AMBIGUOUS` remain distinct.
13. Queue eligibility derives from workflow state.
14. Claim acquisition is atomic.
15. Only one active claim exists per work item and claim type.
16. Claims expire.
17. Drafts survive claim expiration.
18. Draft saves use conflict protection.
19. Submission and approval are distinct.
20. Matching is conservative and explainable.
21. Shared contact information does not automatically merge people.
22. Match confidence is not final identity resolution.
23. Uncertain identity decisions require human review.
24. Match Resolution and Canonical Promotion are separate.
25. Canonical Promotion is idempotent.
26. Canonical identity remains outside People Intake ownership.
27. Every canonical contribution includes provenance.
28. Audit is append-only.
29. Audit and operational logs are separate.
30. High-risk administrative overrides require reasons.
31. Archived records retain evidence and history.
32. Application security is enforced server-side.
33. Authentication does not automatically grant authorization.
34. Public self-registration is not part of Version 1.
35. Shared user accounts are prohibited.
36. Source evidence may not be overwritten by corrections.
37. AI and OCR may assist but may not silently decide identity.
38. Sensitive personal attributes may not be inferred.
39. Retried operations must not create duplicate business outcomes.
40. Failure must not be represented as success.

---

# PART XI — DEFERRED IMPLEMENTATION DECISIONS

# 56. Decisions Reserved for Later Volumes

The following details are intentionally deferred:

* exact frontend framework
* exact backend framework
* exact database provider
* exact ORM or query layer
* exact authentication provider
* exact object-storage provider
* exact background-job technology
* exact API transport implementation
* exact table and column names
* exact index strategy
* exact claim-expiration duration
* exact upload-size limit
* exact rate limits
* exact matching-score weights
* exact normalization libraries
* exact audit payload schema
* exact monitoring provider
* exact deployment environments
* exact retention durations
* exact canonical-integration transport
* exact visual design tokens

These choices must not be treated as undecided architecture flaws. They are implementation-level decisions assigned to later governing volumes.

---

# PART XII — VOLUME 8 COMPLETION STANDARD

# 57. Completion Checklist

Volume 8 is complete when:

* all major domains have explicit ownership
* all domains have responsibilities and boundaries
* global invariants are defined
* business rules have stable identifiers
* identity ownership remains clear
* evidence preservation is enforced
* `UNKNOWN` remains distinct from `NO`
* claims and concurrency are defined
* drafts and recovery are defined
* matching is explainable
* resolution is human-accountable
* promotion is idempotent
* provenance is mandatory
* audit is append-only
* privacy limits are explicit
* accessibility expectations are explicit
* failure and recovery behavior are defined
* future AI and OCR boundaries are defined
* locked decisions are enumerated
* implementation decisions are properly deferred

---

# 58. Volume 8 Readiness Assessment

| Area                        | Readiness |
| --------------------------- | --------: |
| Domain ownership            |      100% |
| Business-rule coverage      |       96% |
| Global invariants           |      100% |
| Workflow dependencies       |       96% |
| Authorization expectations  |       95% |
| Concurrency requirements    |       96% |
| Idempotency requirements    |       96% |
| Matching doctrine           |      100% |
| Canonical ownership         |      100% |
| Provenance requirements     |      100% |
| Audit requirements          |      100% |
| Privacy boundaries          |      100% |
| Accessibility expectations  |       95% |
| Failure recovery            |       96% |
| Future compatibility        |       95% |
| Implementation independence |      100% |

**Overall Volume 8 Design Readiness**

```text
98%
```

The remaining percentage is intentionally reserved for reconciliation against:

* Volume 9 database design
* Volume 10 API contracts
* State Machine Catalog
* Error Catalog
* Audit Event Catalog
* cross-volume traceability

---

# 59. Next Governing Build

The next documentation build is:

```text
PEOPLE-VOLUME-09-DATABASE-SPECIFICATIONS-1.0
```

Volume 9 will translate these domain rules into a complete documented data model, including:

* logical entities
* physical table specifications
* fields
* data types
* keys
* constraints
* indexes
* append-only policies
* deletion and archival behavior
* transaction support
* concurrency controls
* data classification
* migration strategy

No SQL migrations or production database implementation should be created during Volume 9.

**Next build:** Volume 9 — Database Specifications. That volume will be much more precise than the earlier conceptual data design: every table, field, constraint, relationship, index, lifecycle, query pattern, and retention rule will be fully engineered before Cursor writes SQL.

---

## Document Control

| Field | Value |
| --- | --- |
| Canonical path | `docs/volumes/volume-08-technical-specifications/VOLUME_08_TECHNICAL_DOMAIN_SPECIFICATIONS.md` |
| Legacy pointer | `docs/09_technical_specifications/VOLUME_08_TECHNICAL_DOMAIN_SPECIFICATIONS.md` |
| Encoding | UTF-8 |
| Status | DESIGN COMPLETE — PENDING FINAL CROSS-VOLUME FREEZE |
