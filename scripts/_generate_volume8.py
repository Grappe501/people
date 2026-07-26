#!/usr/bin/env python3
"""Generate Volume 8 Technical Domain Specifications."""
from __future__ import annotations

from pathlib import Path

OUT = Path(r"H:\people\docs\volumes\volume-08-technical-specifications\VOLUME_08_TECHNICAL_DOMAIN_SPECIFICATIONS.md")

GLOBAL_INVARIANTS = [
    ("PEOPLE-INV-001", "Evidence Preservation",
     "Original source evidence (images, raw transcription after submit, correction history) is never discarded merely because newer or normalized information exists."),
    ("PEOPLE-INV-002", "Truth Layer Separation",
     "Source evidence, raw transcription, normalized intake values, match decisions, promotion outcomes, and canonical person values must remain distinguishable and must never be silently collapsed into a single undifferentiated value."),
    ("PEOPLE-INV-003", "Human Authority for Irreversible Identity",
     "Artificial intelligence may assist, recommend, rank, or classify; it must not silently perform irreversible identity linkage, merge, or canonical promotion without an explicitly approved human or Owner-accepted rule path."),
    ("PEOPLE-INV-004", "UNKNOWN Is Not NO",
     "Tri-state preference fields (Volunteer, Email List) use YES | NO | UNKNOWN. UNKNOWN means blank, unreadable, ambiguous, or not clearly marked. UNKNOWN must never silently become NO."),
    ("PEOPLE-INV-005", "Conservative Matching",
     "When matching confidence is uncertain, the system must prefer a temporary duplicate over a false merge. A false duplicate is more dangerous than deferring linkage."),
    ("PEOPLE-INV-006", "Household Contact Non-Identity",
     "Contact attributes classified HOUSEHOLD_SHARED or ORGANIZATIONAL cannot independently establish identity; they may support discovery only with corroborating personal signals."),
    ("PEOPLE-INV-007", "Server-Side Enforcement",
     "Authentication, authorization, and domain business rules are enforced on the server for every mutating operation. Client UI state, hidden controls, or role claims are never sufficient authorization."),
    ("PEOPLE-INV-008", "Append-Only Meaningful Audit",
     "Every meaningful privileged, identity, evidence, or workflow state change produces an append-only audit event attributable to actor (or System Actor), action, subject references, and timestamp."),
    ("PEOPLE-INV-009", "Single Active Claim",
     "At most one ACTIVE claim exists per page per claim type (ENTRY or MATCH) at any instant. Concurrent exclusive edit locks must serialize through atomic claim acquisition."),
    ("PEOPLE-INV-010", "Ten-Entry Page Cap",
     "Each intake page supports at most ten intake entries. Row numbers 1–10 are unique per page. No eleventh active entry may exist."),
    ("PEOPLE-INV-011", "No Blank Row Fabrication",
     "Blank handwriting rows do not create intake entries. The system must not fabricate people from rows with no meaningful person fields."),
    ("PEOPLE-INV-012", "Controlled Canonical Promotion",
     "Canonical person create, link, attribute add, retire, and primary-mark operations occur only through controlled promotion requests processed by the canonical people domain. People Intake must not write RedDirt operational tables."),
    ("PEOPLE-INV-013", "Private Source Image Storage",
     "Original source images reside in private object storage with authorized short-lived access only. Public buckets for source originals are prohibited."),
    ("PEOPLE-INV-014", "H-Drive Project Root",
     "All controllable project artifacts, caches, temporary files, and documentation for People Intake remain under H:\\people. Intentional project-controlled writes to C:\\ are prohibited."),
    ("PEOPLE-INV-015", "Design Before Code",
     "Approved design documents and Volume 8 domain rules govern implementation. Application code is not the accidental source of truth. Implementation before design freeze is prohibited."),
]

ACTORS = {
    "Uploader": {
        "may": [
            "Create intake batches and upload source images from field capture devices.",
            "Review orientation and readability before upload completes.",
            "Replace or remove bad images before batch upload completes.",
            "View batches they uploaded and upload progress.",
            "Resume interrupted uploads within policy.",
        ],
        "may_not": [
            "Transcribe handwritten entries as a required duty.",
            "Resolve duplicate or conflicting canonical identities.",
            "Claim pages in the shared entry queue (unless also holding Data Entry role).",
            "Access broad canonical people search or unrelated person histories.",
            "Delete source images outside restricted admin/owner procedures.",
            "Change user roles, retention policy, or security configuration.",
        ],
    },
    "Data Entry User": {
        "may": [
            "Claim next available page from the entry queue.",
            "Transcribe up to ten entries per claimed page with draft autosave.",
            "Mark field conditions (PROVIDED, NOT_PROVIDED, UNREADABLE, AMBIGUOUS, CORRECTED).",
            "Set Volunteer and Email List to YES, NO, or UNKNOWN (blank UI defaults to UNKNOWN).",
            "Submit completed page transcription under active claim.",
            "Release own claim; resume own claimed work; correct pages returned for correction.",
        ],
        "may_not": [
            "Resolve uncertain identity matches or merge canonical people.",
            "Edit another user's active claimed page draft.",
            "Silently overwrite submitted raw transcription (corrections use formal correction history).",
            "Invent missing handwritten values or normalize beyond approved rules.",
            "Force-complete pages or reassign claims (unless also Admin/Owner).",
            "Perform unrestricted bulk export of person data.",
        ],
    },
    "Reviewer": {
        "may": [
            "Review match candidates for possible, conflict, and deferred entries.",
            "Link intake entry to existing canonical person or authorize create-new path.",
            "Resolve field conflicts within approved attribute update rules.",
            "Return pages or entries for correction with documented reason.",
            "Defer match review when additional evidence is required.",
            "Claim match-review work units when match queue policy applies.",
        ],
        "may_not": [
            "Silently auto-merge conflicting identities without resolution record.",
            "Invent transcription values not supported by source evidence.",
            "Delete source images or override retention policy.",
            "Directly merge two canonical people (merge is outside routine intake).",
            "Bypass promotion contract to mutate canonical records from browser.",
            "Disable audit or suppress promotion failure alerts.",
        ],
    },
    "Administrator": {
        "may": [
            "View operational overview, queue metrics, and exception queues.",
            "Invite users, assign roles, disable or suspend accounts (within Owner policy).",
            "Release, reassign, or expire claims with audit.",
            "Change batch priority and correct batch metadata.",
            "Search audit history and manage exception recovery.",
            "Archive or reopen batches/pages within policy.",
            "Access restricted image deletion procedures when policy allows.",
        ],
        "may_not": [
            "Change retention or legal-hold policy (Owner only).",
            "Alter shared-database contracts or production secrets without Owner.",
            "Override Volume 8 locked domain rules without Owner Decision Log entry.",
            "Delete audit history in normal operations.",
            "Grant Owner role without Owner approval.",
            "Authorize production implementation when Gate G-10 is closed.",
        ],
    },
    "Owner": {
        "may": [
            "All Administrator capabilities plus governance authority.",
            "Approve retention, deletion, and legal-hold policy.",
            "Approve production integrations and shared-database contract changes.",
            "Accept or supersede blocking open decisions (OD-B*, contradictions).",
            "Authorize design freeze and implementation gate opening when criteria met.",
            "Manage Administrator access and security policy changes.",
        ],
        "may_not": [
            "Silently bypass audit requirements for privileged actions.",
            "Directly mutate canonical people outside promotion contract (same as all roles).",
            "Authorize production code while Gate G-9 FAIL / G-10 CLOSED without explicit documented exception.",
            "Reuse retired rule or invariant IDs.",
            "Collapse truth layers or discard source evidence without approved retention action.",
        ],
    },
    "System Actor": {
        "may": [
            "Execute approved background jobs: matching evaluation, claim expiry, promotion retry, derivative generation, progress recompute.",
            "Apply deterministic normalization rules without semantic reinterpretation.",
            "Generate operator alerts and enqueue exception queue items on failure.",
            "Expire claims and return pages to queue preserving drafts.",
            "Record audit events for automated actions with System Actor attribution.",
        ],
        "may_not": [
            "Perform irreversible identity linkage or canonical promotion without approved rule or human resolution.",
            "Delete source evidence or audit records in normal operations.",
            "Grant roles or bypass authentication.",
            "Invent transcription or preference values.",
            "Auto-merge CONFLICT-tier candidates.",
            "Write to RedDirt operational tables.",
        ],
    },
}

DOMAINS: list[tuple[str, str, int, int, list[tuple[str, str]], list[tuple[str, str]] | None, dict | None]] = [
    ("6", "Authentication", "AUTH", 8, 4, [
        ("001", "Every API request except documented health/bootstrap endpoints requires validated server-side session before handler execution."),
        ("002", "Authentication uses an approved identity provider behind an AuthPort adapter; application code outside the adapter must not call provider SDKs directly."),
        ("003", "After provider authentication succeeds, the system resolves a local approved-user record; missing approval yields ACCESS_NOT_APPROVED without revealing whether the email exists when uniform-denial policy applies."),
        ("004", "Disabled, suspended, or revoked users lose access on the next request; no grace period for mutating operations."),
        ("005", "Sessions use HTTP-only secure cookies (preferred) or approved bearer tokens for server routes; browser-held tokens are untrusted until server validation."),
        ("006", "Idle timeout and absolute session timeout are configurable; sign-out invalidates server session and clears client cookie."),
        ("007", "Concurrent sessions are allowed unless Owner policy restricts; each session is independently revocable."),
        ("008", "Authentication events (sign-in success/failure without secrets, sign-out, disable/enable) are audited."),
    ], [
        ("001", "Individual accounts only; shared passwords are prohibited."),
        ("002", "Failed authentication responses must not leak account existence when uniform-denial policy is active."),
        ("003", "No public self-service signup in Version 1; users are invited and approved."),
        ("004", "Authentication success never implies authorization; role checks are separate (see Authorization domain)."),
    ], None),
    ("7", "User Access", "USER", 7, 4, [
        ("001", "Each human operator has exactly one app_user record linked to provider auth subject and/or approved email."),
        ("002", "User lifecycle states are INVITED, ACTIVE, SUSPENDED, DISABLED, REVOKED; only ACTIVE users may perform mutating domain operations unless Admin override is audited."),
        ("003", "INVITED users may complete first sign-in/bootstrap only; they may not access queues until promoted to ACTIVE."),
        ("004", "SUSPENDED users may sign in but all mutating operations are denied until restored to ACTIVE."),
        ("005", "DISABLED users are denied on next request; REVOKED is terminal for access (invitation invalidated)."),
        ("006", "Users may hold multiple roles; effective permissions are the union of role grants subject to record/state checks."),
        ("007", "User profile fields (displayName, email) are sourced from approved records; privileged changes require Admin/Owner with audit."),
    ], [
        ("001", "A user ID, once assigned, is never reused for a different human."),
        ("002", "Role assignment changes are audited with prior and new role sets."),
        ("003", "Disabling a user immediately invalidates active claims owned by that user on next claim check or expiry job."),
        ("004", "Owner role assignment requires existing Owner approval except bootstrap documented in Decision Log."),
    ], {"states": ["INVITED", "ACTIVE", "SUSPENDED", "DISABLED", "REVOKED"]}),
    ("8", "Authorization", "AUTHZ", 8, 3, [
        ("001", "Authorization is deny-by-default: authenticated, approved, role-permitted, record-permitted, and state-permitted — all must pass."),
        ("002", "Evaluation order: (1) authenticated, (2) approved and enabled user state, (3) role allows operation, (4) record ownership/assignment, (5) resource state allows transition; else deny."),
        ("003", "Only the active claimant may mutate draft transcription for a claimed page except Admin/Owner override with audit."),
        ("004", "Image bytes are never returned without page-level authorization plus short-lived signed URL issuance."),
        ("005", "Audit search and user management require Admin or Owner unless future scoped roles are Owner-approved."),
        ("006", "UI may hide forbidden controls but server must enforce identical rules on every API route."),
        ("007", "Promotion and canonical mutation endpoints are server-side only; browsers never receive canonical write credentials."),
        ("008", "Authorization matrix in Volume 4 is normative detail; conflicts with Volume 8 require Decision Log resolution before coding."),
    ], [
        ("001", "No operation inherits permissions from a related record without explicit rule (e.g., batch access does not imply all page drafts editable)."),
        ("002", "Override paths (force complete, reassign, reopen) require Admin or Owner and produce high-severity audit."),
        ("003", "Role names and permission tokens are stable enums; ad hoc string roles are prohibited."),
    ], None),
    ("9", "Batch", "BATCH", 8, 4, [
        ("001", "A batch groups pages from one capture effort with shared metadata; batches contain pages, not canonical people."),
        ("002", "Each batch has internal batchId (UUID) and optional human batch_code (e.g., PI-YYYYMMDD-#####)."),
        ("003", "Metadata fields include title, eventName, county, city, collectionDate, collectedBy, notes, priority, source_type; createdBy is system-set from uploader."),
        ("004", "Lifecycle states: DRAFT → UPLOADING → READY → IN_PROGRESS → NEEDS_ATTENTION → COMPLETED → ARCHIVED."),
        ("005", "Batch transitions to COMPLETED only when every page is resolved per page completion rules."),
        ("006", "Progress metrics (page_count, entry_count, completion percentage) are derived from child page/entry states, not sole source of truth."),
        ("007", "Deleting a batch with pages is Admin-only and must preserve evidence via soft-delete or archive, never silent hard-delete of images."),
        ("008", "Operations: Create, Patch metadata, Complete upload, Archive, Reopen (Admin) — each audited."),
    ], [
        ("001", "batchId is immutable once created."),
        ("002", "A page belongs to exactly one batch."),
        ("003", "Batch priority affects queue ordering but does not bypass claim rules."),
        ("004", "Archived batches are read-only for routine operators unless Admin reopen with audit."),
    ], None),
    ("10", "Page", "PAGE", 8, 4, [
        ("001", "A page is the primary queue work unit: one source image and zero to ten intake entries."),
        ("002", "pageId is UUID; pageNumber is unique within batch; optional human page_code includes batch ordinal."),
        ("003", "Core fields: batchId, pageNumber, status, version (optimistic concurrency), imageQualityStatus, blankPage flag, unreadablePage flag."),
        ("004", "Lifecycle follows Page state machine (Uploading through Archived); user-facing labels must not expose raw enum names."),
        ("005", "At most one active original image version; replacement creates new version retaining prior for evidence."),
        ("006", "Page submit requires active ENTRY claim by submitter (or audited Admin/Owner override)."),
        ("007", "Page may not reach COMPLETED while any child entry has pending promotion or unresolved match conflict."),
        ("008", "Zero-entry submit is allowed for documented blank or unreadable pages with required reason codes (Volume 8 lock aligned with OD-B09)."),
        ("009", "Exception paths: upload failure (retryable), unreadable page (return without inventing people), blank page (zero entries with reason)."),
    ], [
        ("001", "entry_count on page is always ≤ 10."),
        ("002", "At most one ACTIVE claim per page per claim type."),
        ("003", "Optimistic concurrency: stale version writes rejected with conflict error."),
        ("004", "Page status transitions are valid only per state machine catalog; illegal transitions denied server-side."),
    ], None),
    ("11", "Source Image", "IMAGE", 10, 4, [
        ("001", "Each page references exactly one active original source image at a time."),
        ("002", "Storage model: original (immutable bytes + sha256), optional display derivative, optional thumbnail; Postgres holds metadata and storage keys only."),
        ("003", "upload_status enum: PENDING, UPLOADING, UPLOADED, FAILED, REPLACED, QUARANTINED, DELETED."),
        ("004", "conversion_status enum: NOT_REQUIRED, PENDING, PROCESSING, COMPLETE, FAILED."),
        ("005", "Replacing an image creates a new version; prior version retained for evidence with REPLACED status."),
        ("006", "Duplicate content hash (SHA-256) across batches triggers warning; never auto-delete duplicate without human/admin decision."),
        ("007", "Access via image-access endpoint produces short-lived signed URL after authorization; signed URLs never logged."),
        ("008", "MIME allowlist and max size enforced per configuration catalog; violations yield UPLOAD_TOO_LARGE or UPLOAD_TYPE_NOT_ALLOWED."),
        ("009", "Quarantined images are inaccessible to routine operators until Admin/Owner release or reject with audit."),
        ("010", "Image metadata records uploader, timestamps, dimensions, orientation, and linkage to batch/page."),
    ], [
        ("001", "Original bytes are never stored in Postgres BLOB columns as primary store."),
        ("002", "Public ACL on source originals is prohibited."),
        ("003", "Deleted image status retains audit trail and tombstone metadata per retention policy."),
        ("004", "Display derivatives must not become the only preserved evidence of original capture."),
    ], None),
    ("12", "Upload", "UPLOAD", 8, 3, [
        ("001", "Upload flow: register page → upload-intent (authorized PUT target + intentId) → client PUT → upload-complete (verify size/type/hash) → activate image → audit."),
        ("002", "Upload-intent is single-use and time-bounded; expired intents cannot complete upload."),
        ("003", "upload-complete verifies declared hash matches stored object before activating image version."),
        ("004", "Partial uploads remain in retryable state; batch may enter UPLOADING until all pages complete or fail visibly."),
        ("005", "Mobile capture and multi-image batch selection follow same intent/complete contract."),
        ("006", "Failed uploads surface retry UX; operator may replace image before batch marked READY."),
        ("007", "Uploader role required for field upload; Data Entry upload optional by policy (default deny per OD-B06 lock)."),
        ("008", "Brief local buffer allowed for offline capture; online upload-complete required before page enters office queue (OD-B07 lock)."),
    ], [
        ("001", "No page enters Ready for Entry without successful upload-complete for active image."),
        ("002", "Upload credentials never grant read access to unrelated pages."),
        ("003", "Upload audit events: UploadIntentCreated, ImageUploaded, ImageReplaced — no secrets or signed URLs in payload."),
    ], None),
    ("13", "Shared Work Queue", "QUEUE", 8, 4, [
        ("001", "Queue types: ENTRY (Data Entry), MATCH (Reviewer), CORRECTION (returned work), EXCEPTION (Admin/Owner failures)."),
        ("002", "Entry queue eligibility: pages Ready for Entry with no active ENTRY claim or expired claim."),
        ("003", "Match queue eligibility: entries/pages needing human match review (POSSIBLE, CONFLICT, deferred EXACT/NO_MATCH per Volume 8 locks)."),
        ("004", "Default ordering: priority (if set) then oldest ready timestamp (FIFO within priority band)."),
        ("005", "claim-next is the atomic assignment path; list-then-claim in two non-atomic client-only steps is not the sole assignment mechanism."),
        ("006", "Queue listings are eventually consistent views; claim-next must serialize concurrent claimants via DB lock or unique constraint."),
        ("007", "Filters (batch, county, status, assignee, age) are server-side only; clients may not fetch unrestricted full queue dumps."),
        ("008", "Admin may boost batch/page priority affecting sort order but not claim invariants."),
    ], [
        ("001", "claim-next must never return a page with an ACTIVE claim of the same type."),
        ("002", "Two concurrent claim-next operations yield distinct pages or one NO_PAGE_AVAILABLE."),
        ("003", "Expired claims return page to eligible queue without deleting draft."),
        ("004", "Exception queue items require Admin/Owner visibility within SLA defined in alerts domain."),
    ], {"queue_types": ["ENTRY", "MATCH", "CORRECTION", "EXCEPTION"]}),
    ("14", "Claim", "CLAIM", 10, 4, [
        ("001", "Claim grants exclusive edit lock for ENTRY transcription or MATCH review work on a page (or match unit per policy)."),
        ("002", "Claim record fields: claimId, pageId, claimantUserId, claimType (ENTRY | MATCH), status, claimedAt, expiresAt, renewedAt, version."),
        ("003", "Default TTL: 30 minutes from last renew/activity; configurable in configuration catalog."),
        ("004", "Renew on draft save, heartbeat, or explicit renew operation while ACTIVE and owned by claimant."),
        ("005", "claim-next selects eligible page and inserts ACTIVE claim in one transaction with page row lock."),
        ("006", "release: claimant or Admin may release; draft preserved; status RELEASED."),
        ("007", "reassign: Admin releases prior claim and creates new claim for target user with audit."),
        ("008", "expire job marks EXPIRED; page returns to queue; draft preserved; claimant warned on next write attempt."),
        ("009", "Stale writes after lost claim return PAGE_CLAIM_OWNERSHIP_LOST or PAGE_CLAIM_EXPIRED without applying mutation."),
        ("010", "Warning UI before expiry; expiring-soon is UX overlay, not separate domain claim status."),
    ], [
        ("001", "One ACTIVE claim per page per claimType at any instant."),
        ("002", "Expired claim does not delete draft transcription."),
        ("003", "Claim reassignment always audited with prior and new claimant."),
        ("004", "Match claims mirror page claim TTL policy (OD-B08 lock)."),
    ], None),
    ("15", "Draft", "DRAFT", 8, 3, [
        ("001", "Draft transcription is mutable only under ACTIVE ENTRY claim by claimant (or audited override)."),
        ("002", "Autosave persists draft without submitting; save does not advance entry to Transcribed state."),
        ("003", "Draft preserves raw field values and field conditions separately from normalized preview."),
        ("004", "Draft survives claim release, expiry, and reassignment until page submit or Admin purge with audit."),
        ("005", "Concurrent draft saves use optimistic concurrency on page/entry version."),
        ("006", "Draft delete of an entry row is soft or versioned; never silent remove of submitted evidence."),
        ("007", "Offline draft buffer may queue saves locally; server draft wins on conflict with operator merge UX."),
        ("008", "DraftSaved audit events recorded without full PII payload dumps."),
    ], [
        ("001", "Submit transitions draft to submitted evidence; raw values after submit are immutable except formal CORRECTED path."),
        ("002", "No draft mutation after submit except through correction workflow reopen."),
        ("003", "Empty draft rows (no meaningful fields) are not persisted as entries."),
    ], None),
    ("16", "Transcription", "TRANSCRIPTION", 12, 5, [
        ("001", "Transcription captures handwritten volunteer form fields per entry row 1–10 on a page."),
        ("002", "Fields: lastName, firstName, email, phone, zipCode (raw pairs), volunteer_response, email_list_response."),
        ("003", "Tri-state responses: YES, NO, UNKNOWN only."),
        ("004", "Blank UI for Volunteer or Email List persists as UNKNOWN, never NO."),
        ("005", "Each field has parallel field_condition: PROVIDED, NOT_PROVIDED, UNREADABLE, AMBIGUOUS, CORRECTED."),
        ("006", "NOT_PROVIDED means volunteer left field blank on paper; distinct from UNREADABLE and AMBIGUOUS."),
        ("007", "UNREADABLE means writing present but not reliably interpretable; UNREADABLE ≠ blank."),
        ("008", "AMBIGUOUS means partially readable with multiple plausible readings; operators must select AMBIGUOUS in UX (Volume 8 lock, OD-B04)."),
        ("009", "At least one meaningful person field required to create entry; otherwise row is not fabricated (PEOPLE-INV-011)."),
        ("010", "Row numbers unique per page 1–10; entry_code human identifier optional (e.g., batch-page-R07)."),
        ("011", "Transcription occurs only after page image available; matching must not interrupt typing."),
        ("012", "Post-submit transcription is evidence; corrections append CORRECTED history preserving prior raw values."),
    ], [
        ("001", "Maximum ten entries per page."),
        ("002", "UNKNOWN ≠ NO for preference fields."),
        ("003", "Submitted raw values are never silently overwritten."),
        ("004", "Transcription audit: EntryDraftSaved, EntrySubmitted, EntryCorrected."),
        ("005", "Zero entries allowed on page only via documented blank/unreadable exception with reason codes."),
    ], {"fields": ["lastName", "firstName", "email", "phone", "zipCode", "volunteer_response", "email_list_response"], "tri_state": ["YES", "NO", "UNKNOWN"]}),
    ("17", "Field Condition", "FIELD", 8, 4, [
        ("001", "Field conditions apply per field independently on each entry."),
        ("002", "PROVIDED: value present and operator confirms readable transcription."),
        ("003", "NOT_PROVIDED: volunteer left field blank on source form."),
        ("004", "UNREADABLE: handwriting present but not reliably interpretable; raw value may be empty or best-effort with condition flag."),
        ("005", "AMBIGUOUS: partially readable; multiple plausible readings; operator must not guess — mark AMBIGUOUS (Volume 8 lock)."),
        ("006", "CORRECTED: formal post-submit correction; prior value preserved in correction history."),
        ("007", "Field condition drives validation: UNREADABLE/AMBIGUOUS on email/phone may block auto EXACT match rules."),
        ("008", "Field condition changes after submit require correction workflow, not silent patch."),
    ], [
        ("001", "Field condition enum is closed: PROVIDED, NOT_PROVIDED, UNREADABLE, AMBIGUOUS, CORRECTED."),
        ("002", "NOT_PROVIDED must not be used when writing is present but illegible (use UNREADABLE)."),
        ("003", "AMBIGUOUS must be selectable in V1 UX when dictionary includes it (Volume 8 lock)."),
        ("004", "CORRECTED always retains pointer to superseded raw value and actor."),
    ], {"values": ["PROVIDED", "NOT_PROVIDED", "UNREADABLE", "AMBIGUOUS", "CORRECTED"]}),
    ("18", "Normalization", "NORMALIZE", 10, 4, [
        ("001", "Normalization produces deterministic machine-readable counterparts; never reinterprets meaning."),
        ("002", "Names: trim, collapse spaces, Unicode normalize, casefold for compare; keep punctuation; no nickname expansion or demographic inference."),
        ("003", "Email: trim, lowercase, strip clearly nonsemantic surround punctuation, format-validate; no local-part alteration or domain guessing."),
        ("004", "Phone: extract digits, US 10-digit recognition, unambiguous country code, separate extension; no digit invention."),
        ("005", "ZIP: trim, accept 5-digit or ZIP+4; no city inference or geocoding in V1."),
        ("006", "Normalization runs on submit and on demand for matching; draft may show preview but canonical normalized fields set at submit boundary."),
        ("007", "UNREADABLE or AMBIGUOUS field conditions may yield empty normalized values without fabricating data."),
        ("008", "Normalized values stored alongside raw; matching uses normalized; audit explains normalization version."),
        ("009", "Same raw input always yields same normalized output for a given normalization rule version."),
        ("010", "Normalization rule version changes require Decision Log entry and do not retroactively alter submitted evidence without migration plan."),
    ], [
        ("001", "Normalization never converts UNKNOWN preference to NO."),
        ("002", "Normalization never creates values from NOT_PROVIDED blank fields."),
        ("003", "Normalization is reversible in audit sense (raw always preserved post-submit)."),
        ("004", "Matching engine must record normalization rule version used per match run."),
    ], None),
    ("19", "Entry Submission", "SUBMIT", 8, 3, [
        ("001", "Page submit validates all entries, field conditions, row uniqueness, and claim ownership before state transition."),
        ("002", "Submit transitions page from In Progress to Entry Complete and entries from Draft to Transcribed."),
        ("003", "Submit freezes raw transcription as evidence; subsequent edits require correction workflow."),
        ("004", "Submit triggers matching evaluation jobs for each transcribed entry asynchronously."),
        ("005", "Submit denied without ACTIVE ENTRY claim (except audited override)."),
        ("006", "Submit with zero entries requires blankPage or unreadablePage reason codes (OD-B09 lock)."),
        ("007", "Submit validates at most ten entries and warns on same-page duplicate email/phone/name+zip."),
        ("008", "Submit audit: PageSubmitted, EntrySubmitted with subject references."),
    ], [
        ("001", "One submit operation is atomic at page boundary per transaction rules (Part IV)."),
        ("002", "Partial page submit (subset of rows) is prohibited; page submits as a unit."),
        ("003", "Failed submit leaves page in In Progress with draft intact."),
    ], None),
    ("20", "Matching", "MATCH", 13, 5, [
        ("001", "Matching runs after transcription submit; must not block data entry UX."),
        ("002", "Pipeline: normalize → search candidates → rank + explain → assign confidence tier → human review path → resolution → promotion request."),
        ("003", "Confidence tiers: EXACT, HIGH_CONFIDENCE, POSSIBLE, LOW_CONFIDENCE, NO_MATCH, CONFLICT."),
        ("004", "EXACT tier meets versioned deterministic rules (E-1, E-2, E-3); human review required in V1 (OD-B01 lock: no auto-link without Owner flag)."),
        ("005", "NO_MATCH does not auto-create canonical person in V1; human Create New required (OD-B02 lock)."),
        ("006", "POSSIBLE and CONFLICT always require human review."),
        ("007", "LOW_CONFIDENCE is context only; not recommended as likely match without reviewer judgment."),
        ("008", "Strong signals: exact normalized email; exact phone + compatible name; exact email + compatible last name; etc. per matching engine spec."),
        ("009", "Weak signals (same ZIP only, same last name only) never auto-link."),
        ("010", "Negative/conflict signals block auto-link: different strong emails/phones, substantially different names, household shared contact alone, multiple equal candidates."),
        ("011", "Same-page duplicate detection warns; operator chooses Keep Both, Edit, or Remove — never silent remove."),
        ("012", "Match run stores rule_version, signals, explanations; stable sort tie-break by candidate personId."),
        ("013", "Canonical domain unavailable: pause candidate lookup/resolution needing canonical; preserve transcription."),
    ], [
        ("001", "One final resolution per entry version."),
        ("002", "CONFLICT never auto-merged."),
        ("003", "Household shared contacts cannot independently establish identity."),
        ("004", "Ranking explanations stored for audit."),
        ("005", "False duplicate preferred over false merge."),
    ], {"confidence_classes": ["EXACT", "HIGH_CONFIDENCE", "POSSIBLE", "LOW_CONFIDENCE", "NO_MATCH", "CONFLICT"]}),
    ("21", "Match Candidate", "CANDIDATE", 7, 3, [
        ("001", "Each candidate links intake_entry_id to candidate_person_id with rank, confidence_tier, score, match_rule_version."),
        ("002", "Candidate stores positive_signals, negative_signals, conflicting_fields, and human-readable explanation."),
        ("003", "Candidate status enum: SUGGESTED, SELECTED, REJECTED, SUPERSEDED, EXPIRED."),
        ("004", "Score is ranking aid only; identity truth requires resolution record."),
        ("005", "At most one SELECTED candidate per entry at resolution time unless DEFER."),
        ("006", "Superseded candidates remain for audit when new match run executes."),
        ("007", "Expired candidates cannot be selected without new match run."),
    ], [
        ("001", "Candidate records are immutable after resolution except status SUPERSEDED/EXPIRED."),
        ("002", "Candidate generation is idempotent per entry version and rule_version."),
        ("003", "No candidate row without intake_entry_id and candidate_person_id."),
    ], None),
    ("22", "Match Resolution", "RESOLUTION", 10, 4, [
        ("001", "Resolution types: LINK_EXISTING, CREATE_NEW, DEFER, RETURN_FOR_CORRECTION, NO_ACTION."),
        ("002", "LINK_EXISTING requires selected candidate and resolved_person_id; provenance bundle attached."),
        ("003", "CREATE_NEW requires human reviewer (or approved rule path) when no acceptable existing person; creates promotion request for new person."),
        ("004", "DEFER pauses resolution with reason; entry remains in match queue."),
        ("005", "RETURN_FOR_CORRECTION sends page/entry to correction queue with documented reason; reopens transcription path."),
        ("006", "NO_ACTION documents intentional non-promotion (e.g., illegible row later removed) with audit."),
        ("007", "Resolution methods: HUMAN, APPROVED_EXACT_RULE, ADMINISTRATIVE, SYSTEM_RECOVERY."),
        ("008", "V1 default: HUMAN for POSSIBLE/CONFLICT/NO_MATCH/EXACT (OD-B01/B02 locks)."),
        ("009", "Resolution record fields: intake_entry_id, resolution_type, resolved_person_id, created_person_id, resolution_reason, selected_candidate_id, resolved_by_user_id, resolution_method, rule_version, created_at."),
        ("010", "One final resolution per entry version; superseding requires new entry version via correction."),
    ], [
        ("001", "Resolution without promotion request when LINK/CREATE is invalid state."),
        ("002", "RETURN_FOR_CORRECTION preserves submitted evidence history."),
        ("003", "Administrative resolution requires Admin/Owner with elevated audit."),
        ("004", "SYSTEM_RECOVERY only for documented error recovery patterns (Part III §33)."),
    ], {"outcomes": ["LINK_EXISTING", "CREATE_NEW", "DEFER", "RETURN_FOR_CORRECTION", "NO_ACTION"]}),
    ("23", "Canonical Promotion", "PROMOTION", 12, 4, [
        ("001", "Promotion is Model B controlled bridge: match resolution → PromotionRequest → canonical service → PromotionResult → entry/page status update."),
        ("002", "Browsers never call raw canonical mutation APIs."),
        ("003", "Request payload includes entryId, resolutionId, action (CREATE|LINK|UPDATE_ATTRIBUTES), attribute decisions, idempotencyKey, actorId, provenance bundle."),
        ("004", "Idempotent retry safe; duplicate idempotencyKey returns prior result without double mutation."),
        ("005", "Provenance required for every promoted attribute value linking batch, page, entry, image, actors, timestamps."),
        ("006", "Page not marked COMPLETED while any child promotion pending."),
        ("007", "No RedDirt operational table writes from People Intake."),
        ("008", "No routine automatic merges of two canonical people."),
        ("009", "Canonical unavailable: retain resolution, mark promotion PENDING/RETRYABLE, surface operator-safe message, enqueue PROMOTION_RETRY job."),
        ("010", "Attribute update on link: same value adds provenance; new value may add additional; conflict requires explicit decision (Keep Existing, Add Additional, Mark Primary, Reject, Defer)."),
        ("011", "Preference supersession: newer explicit YES/NO supersedes older; UNKNOWN never supersedes known YES/NO (OD-B11 lock)."),
        ("012", "Audit: PromotionRequested, PromotionSucceeded, PromotionFailed, PromotionRetried."),
    ], [
        ("001", "Every successful promotion has matching PromotionResult record."),
        ("002", "Failed promotion never silently drops resolution."),
        ("003", "Promotion does not delete canonical people."),
        ("004", "Promotion requests are append-only with status transitions."),
    ], None),
    ("24", "Person Attribute", "ATTRIBUTE", 8, 3, [
        ("001", "Attribute types: NAME, EMAIL, PHONE, ZIP, VOLUNTEER_PREFERENCE, EMAIL_LIST_PREFERENCE."),
        ("002", "Each attribute supports value_raw, value_normalized, status, is_primary, confidence, source_type, source_reference_id, effective_at, retired_at."),
        ("003", "Multiple values per type allowed (e.g., second phone); new intake must not destroy older valid values."),
        ("004", "Contact sharing classification: PERSONAL, HOUSEHOLD_SHARED, ORGANIZATIONAL, UNKNOWN."),
        ("005", "Primary mark changes require explicit promotion decision, not silent overwrite."),
        ("006", "Retired attributes remain in history; not hard-deleted in normal operations."),
        ("007", "Volunteer and email-list preferences are time-aware; preserve prior explicit choices."),
        ("008", "Attribute conflicts during link resolved per promotion rules with reviewer or promotion service decision."),
    ], [
        ("001", "Flat silent overwrite of canonical attribute history is prohibited."),
        ("002", "UNKNOWN preference never supersedes explicit YES/NO."),
        ("003", "HOUSEHOLD_SHARED cannot alone justify identity link."),
    ], None),
    ("25", "Provenance", "PROVENANCE", 6, 3, [
        ("001", "Provenance links canonical values to intake entry, page, batch, source image, uploader, transcriber, reviewer, normalization version, match resolution, and promotion result."),
        ("002", "Every promoted attribute records source_type and source_reference_id pointing to intake evidence chain."),
        ("003", "Provenance bundles are immutable once promotion succeeds."),
        ("004", "Correction history on intake side does not retroactively alter provenance of already-promoted values without new promotion decision."),
        ("005", "Provenance queries available to Admin/Owner and canonical domain consumers under least privilege."),
        ("006", "Provenance records never contain secrets, signed URLs, or full raw PII dumps in logs."),
    ], [
        ("001", "No canonical attribute without traceable provenance reference after promotion."),
        ("002", "Provenance chain must survive entry correction branches that trigger re-promotion."),
        ("003", "System Actor promotions still record initiating human resolution where applicable."),
    ], None),
    ("26", "Audit", "AUDIT", 10, 4, [
        ("001", "Audit events are append-only in normal operations."),
        ("002", "Event shape: who, what, when, where (requestId, optional IP hash), subject refs, optional why, result."),
        ("003", "No raw PII dumps, secrets, session tokens, or signed URLs in audit payloads."),
        ("004", "High-risk operations require successful audit write before commit completes or compensating documented policy."),
        ("005", "Audit failure on privileged action escalates CRITICAL alert."),
        ("006", "Normative event names maintained in Engineering Event Catalog."),
        ("007", "Admin/Owner may search by actor, type, date, batch/page/entry/person with pagination."),
        ("008", "Audit retention follows Retention domain; legal hold overrides deletion."),
        ("009", "Authentication, claim, submit, match, promotion, and override events are mandatory catalog entries."),
        ("010", "Audit records are never updated in place; corrections are new events."),
    ], [
        ("001", "Every meaningful action in PEOPLE-INV-008 scope produces an audit event."),
        ("002", "Audit actor is authenticated userId or System Actor label."),
        ("003", "Audit timestamps are UTC with timezone stored."),
        ("004", "Deletion of audit records prohibited except approved archival migration with Owner acceptance."),
    ], None),
    ("27", "Background Jobs", "JOB", 9, 3, [
        ("001", "Job record: jobId, type, payload ref, status, attempts, nextRunAt, lastError code, idempotencyKey."),
        ("002", "Status enum: PENDING, RUNNING, SUCCEEDED, FAILED, DEAD."),
        ("003", "Job types (V1): MATCH_EVALUATE_PAGE, MATCH_EVALUATE_ENTRY, CLAIM_EXPIRE, PROMOTION_RETRY, IMAGE_DERIVATIVE, BATCH_PROGRESS_RECOMPUTE."),
        ("004", "Handlers must be idempotent; safe to retry."),
        ("005", "Exponential backoff on failure; DEAD after N attempts → exception queue + alert."),
        ("006", "Failed jobs must never cause loss of transcription or submitted evidence."),
        ("007", "CLAIM_EXPIRE runs on schedule; marks claims EXPIRED and returns pages to queue."),
        ("008", "MATCH jobs triggered after page submit; may run per page or per entry per implementation package."),
        ("009", "Admin visibility into failing/dead jobs without PII in logs."),
    ], [
        ("001", "Job idempotencyKey prevents duplicate side effects."),
        ("002", "RUNNING jobs stale-lock recovered via timeout and SYSTEM_RECOVERY patterns."),
        ("003", "DEAD jobs require human operator acknowledgment to retry or resolve."),
    ], {"states": ["PENDING", "RUNNING", "SUCCEEDED", "FAILED", "DEAD"]}),
    ("28", "Operator Alerts", "ALERT", 6, 0, [
        ("001", "Alerts notify operators of failures requiring attention: promotion dead-letter, audit write failure, upload quarantine, job DEAD, exception queue backlog."),
        ("002", "Severity enum: INFO, WARNING, HIGH, CRITICAL."),
        ("003", "CRITICAL: audit failure on privileged action, canonical promotion repeatedly failing, security anomalies."),
        ("004", "HIGH: dead-letter jobs, claim expiry storms, matching pipeline stalled beyond SLA."),
        ("005", "WARNING: retryable upload failures, promotion retry in progress, expiring claims aggregate."),
        ("006", "INFO: routine job completion summaries for Admin dashboard (optional V1)."),
    ], None, {"severities": ["INFO", "WARNING", "HIGH", "CRITICAL"]}),
    ("29", "Search", "SEARCH", 7, 0, [
        ("001", "V1 search scope is operational, not public people discovery."),
        ("002", "Uploader: search own batches only."),
        ("003", "Data Entry: queue filters and own work history; no unrestricted person search."),
        ("004", "Reviewer: search candidates and linked person summaries needed for match review only."),
        ("005", "Admin/Owner: audit search, batch/page/entry lookup, exception queue search."),
        ("006", "All search endpoints enforce authorization and pagination; no bulk export in V1 unless Owner-approved separate policy."),
        ("007", "Search indexes must not expose signed URLs or secrets in results."),
    ], None, None),
    ("30", "Administration", "ADMIN", 9, 0, [
        ("001", "Admin workspace covers overview, batches, queues, matching oversight, exceptions, users, audit, settings."),
        ("002", "User invite flow creates INVITED user; role assignment audited."),
        ("003", "Disable/suspend/revoke user access with immediate effect on claims and sessions."),
        ("004", "Claim release and reassignment with mandatory reason on reassignment."),
        ("005", "Batch priority change and metadata correction audited."),
        ("006", "Force complete and reopen page/batch only with documented reason and elevated audit."),
        ("007", "Exception queue triage assigns owner operator and tracks resolution."),
        ("008", "Admin cannot change retention/legal-hold (Owner only)."),
        ("009", "Admin actions on canonical data still go through promotion contract."),
    ], None, None),
    ("31", "Reporting", "REPORT", 8, 0, [
        ("001", "Operational reports: queue depth, claim aging, batch progress, match backlog, promotion pending count."),
        ("002", "Reports derive from domain state, not ad hoc mutable report tables as sole truth."),
        ("003", "Uploader-visible: own batch upload status."),
        ("004", "Data Entry-visible: personal throughput (pages submitted, corrections pending)."),
        ("005", "Reviewer-visible: matches resolved, deferred, returned."),
        ("006", "Admin/Owner-visible: system-wide metrics and exception rates."),
        ("007", "Reports contain aggregated data; no unnecessary PII in downloadable exports."),
        ("008", "Report generation failures are logged and alerted at WARNING or above."),
    ], None, None),
    ("32", "Retention", "RETENTION", 8, 3, [
        ("001", "Retention states: ACTIVE, RETAIN_UNTIL_DATE, LEGAL_HOLD, ELIGIBLE_FOR_DELETION, DELETED."),
        ("002", "Separate retention policies may apply to originals, derivatives, intake entries, audit, match artifacts, promotion records."),
        ("003", "Legal hold overrides normal deletion schedules."),
        ("004", "V1: retain source images until Owner signs retention policy; no auto-delete of originals in V1 (OD-B10 lock)."),
        ("005", "Deletion vs archive: archive preserves retrieval path; permanent delete requires Owner-approved procedure."),
        ("006", "Canonical person deletion is not a People Intake direct action."),
        ("007", "Retention changes require Owner approval and Decision Log entry."),
        ("008", "Eligible-for-deletion items are not deleted without second-step confirmation job."),
    ], [
        ("001", "Audit events under legal hold are never deleted."),
        ("002", "Retention metadata recorded on applicable entities."),
        ("003", "Image deletion retains tombstone and audit trail."),
    ], None),
    ("33", "Error Recovery", "RECOVERY", 10, 0, [
        ("001", "Error categories: TRANSIENT, PERMANENT, OPERATOR, SECURITY, DATA_INTEGRITY."),
        ("002", "TRANSIENT: retry with backoff (upload, promotion, canonical read)."),
        ("003", "PERMANENT: surface actionable error; route to exception queue; no infinite retry."),
        ("004", "OPERATOR: requires human decision (correction return, quarantine release, dead job retry)."),
        ("005", "SECURITY: deny operation, audit, alert CRITICAL, preserve evidence."),
        ("006", "DATA_INTEGRITY: halt affected transaction, alert HIGH/CRITICAL, require Admin triage."),
        ("007", "Pattern: stale claim write → PAGE_CLAIM_OWNERSHIP_LOST; operator refreshes and reclaims."),
        ("008", "Pattern: promotion failure → resolution preserved, PROMOTION_RETRY job, page not falsely COMPLETED."),
        ("009", "Pattern: matching unavailable → transcription preserved, match DEFER, alert WARNING."),
        ("010", "Pattern: audit write failure on privileged op → rollback mutation, CRITICAL alert, no silent success."),
    ], None, {"categories": ["TRANSIENT", "PERMANENT", "OPERATOR", "SECURITY", "DATA_INTEGRITY"]}),
]

LOCKED_DECISIONS = [
    ("LD-01", "Project root is H:\\people; no intentional project writes to C:\\.", "D-001", "PEOPLE_INTAKE_H_DRIVE_PROTOCOL.md"),
    ("LD-02", "Application separate from RedDirt; shared DB ecosystem only.", "D-002", "PEOPLE_INTAKE_SCOPE_AND_BOUNDARIES.md"),
    ("LD-03", "Same hosted Postgres ecosystem as RedDirt with least-privilege credentials.", "D-003", "PEOPLE_INTAKE_MASTER_BUILD_PLAN.md"),
    ("LD-04", "Page is primary work unit.", "D-004", "PEOPLE_INTAKE_DOMAIN_MODEL.md"),
    ("LD-05", "Maximum ten intake entries per page.", "D-005", "Field dictionary"),
    ("LD-06", "Each line receives unique intake-entry identity.", "D-006", "Domain model"),
    ("LD-07", "Capture, transcription, matching are separate workflows.", "D-007", "Workflows"),
    ("LD-08", "Multiple users share one queue with atomic claims.", "D-008/D-009", "Queue and Claiming"),
    ("LD-09", "Matching occurs after transcription.", "D-010", "Matching workflow"),
    ("LD-10", "Controlled promotion (Model B) to canonical people.", "D-011+", "Canonical person contract"),
    ("LD-11", "Field conditions include PROVIDED, NOT_PROVIDED, UNREADABLE, AMBIGUOUS, CORRECTED.", "Volume 8", "OD-B04 aligned"),
    ("LD-12", "AMBIGUOUS selectable in V1 UX when in data dictionary.", "Volume 8", "OD-B04 PROPOSED RESOLVED"),
    ("LD-13", "Blank preference UI → UNKNOWN, never NO.", "Volume 8", "PEOPLE-INV-004"),
    ("LD-14", "Blank rows do not fabricate intake entries.", "Volume 8", "PEOPLE-INV-011"),
    ("LD-15", "EXACT matches require human review in V1; no auto-link by default.", "Volume 8", "OD-B01 PROPOSED RESOLVED"),
    ("LD-16", "NO_MATCH does not auto-create person; human Create New.", "Volume 8", "OD-B02 PROPOSED RESOLVED"),
    ("LD-17", "POSSIBLE and CONFLICT always require human review.", "Volume 8", "Matching engine"),
    ("LD-18", "Household shared contacts cannot alone establish identity.", "Volume 8", "PEOPLE-INV-006"),
    ("LD-19", "Prefer temporary duplicate over false merge.", "Volume 8", "PEOPLE-INV-005"),
    ("LD-20", "Data Entry batch/upload denied by default.", "Volume 8", "OD-B06 PROPOSED RESOLVED"),
    ("LD-21", "Brief local capture buffer; online upload-complete required.", "Volume 8", "OD-B07 PROPOSED RESOLVED"),
    ("LD-22", "Match claims mirror page claim TTL (30 min default).", "Volume 8", "OD-B08 PROPOSED RESOLVED"),
    ("LD-23", "Zero-entry submit allowed with blank/unreadable reason codes.", "Volume 8", "OD-B09 PROPOSED RESOLVED"),
    ("LD-24", "No auto-delete of source images in V1.", "Volume 8", "OD-B10 PROPOSED RESOLVED"),
    ("LD-25", "Preference supersession: explicit YES/NO over older; UNKNOWN never supersedes.", "Volume 8", "OD-B11 PROPOSED RESOLVED"),
    ("LD-26", "No public signup; invite and approve only.", "AUTH-RULE-003 area", "Authentication"),
    ("LD-27", "Private object storage for originals; signed URL access only.", "IMAGE domain", "Image storage architecture"),
    ("LD-28", "Append-only audit for meaningful actions.", "AUDIT domain", "PEOPLE-INV-008"),
    ("LD-29", "Server-side authorization on every mutation.", "AUTHZ domain", "PEOPLE-INV-007"),
    ("LD-30", "No RedDirt operational table writes.", "PROMOTION domain", "Scope boundaries"),
    ("LD-31", "No OCR/AI transcription in V1.", "Constitution", "V1 exclusions"),
    ("LD-32", "No automatic uncertain merges.", "Constitution", "Matching philosophy"),
    ("LD-33", "Tri-state YES/NO/UNKNOWN for Volunteer and Email List.", "Transcription", "Field dictionary"),
    ("LD-34", "Raw transcription immutable after submit except CORRECTED path.", "DRAFT/SUBMIT", "Provenance"),
    ("LD-35", "One ACTIVE claim per page per claim type.", "CLAIM domain", "PEOPLE-INV-009"),
    ("LD-36", "Promotion idempotent with idempotencyKey.", "PROMOTION domain", "Canonical contract"),
    ("LD-37", "Design before code; Gate G-10 closed until freeze.", "Constitution", "Build gates"),
    ("LD-38", "Canonical state dictionary must be published before freeze.", "OD-B03", "PROPOSED RESOLVED pending Owner"),
    ("LD-39", "Shared DB compatibility audit required before schema implementation.", "OD-B05", "PROPOSED RESOLVED pending Owner"),
    ("LD-40", "Quality/ops/freeze docs must exist before implementation authorization.", "OD-B12", "Design freeze report"),
]

DEFERRED = [
    ("DI-01", "Exact storage provider vendor and bucket naming.", "OD-N01", "Before upload implementation wave"),
    ("DI-02", "Exact signed URL TTL and claim TTL numeric values.", "OD-N02", "Configuration catalog; 30 min claim default documented"),
    ("DI-03", "Exact upload size and rate limits.", "OD-N03", "Quality package"),
    ("DI-04", "Exact match score formula weights.", "OD-N04", "Ranking aid only; reasons mandatory"),
    ("DI-05", "Exact CSP headers and session timeout numbers.", "OD-N05", "Security hardening wave"),
    ("DI-06", "Background job host (Netlify functions vs worker).", "OD-N06", "Engineering package"),
    ("DI-07", "Prisma/table physical names.", "OD-N07", "After shared DB audit"),
    ("DI-08", "Monitoring/alerting vendor.", "OD-N08", "Ops package"),
    ("DI-09", "auto_exact_match_linking feature flag default off until Owner enables.", "OD-B01", "Post-V1 optional"),
    ("DI-10", "Exact retention day counts per artifact class.", "Retention", "Owner policy signature"),
    ("DI-11", "Physical API route paths and HTTP status code matrix.", "Volume 10", "API specifications volume"),
    ("DI-12", "Database table DDL and indexes.", "Volume 9", "Database specifications volume"),
]


def fmt_rules(prefix: str, rules: list[tuple[str, str]]) -> str:
    lines = []
    for num, text in rules:
        lines.append(f"**{prefix}-RULE-{num}** — {text}")
    return "\n\n".join(lines)


def fmt_invs(prefix: str, invs: list[tuple[str, str]]) -> str:
    lines = []
    for num, text in invs:
        lines.append(f"**{prefix}-INV-{num}** — {text}")
    return "\n\n".join(lines)


def domain_section(d: tuple) -> str:
    num, title, prefix, rc, ic, rules, invs, extra = d
    parts = [f"## {num}. {title} Domain", "", f"### {num}.1 Purpose", ""]
    parts.append(f"Normative business rules and invariants for the **{title}** domain. "
                 f"This section governs behavior precision for implementation packages; "
                 f"it does not authorize database DDL, API routes, or framework choices.")
    parts += ["", f"### {num}.2 Business Rules", "", fmt_rules(prefix, rules)]
    if invs:
        parts += ["", f"### {num}.3 Domain Invariants", "", fmt_invs(prefix, invs)]
    if extra:
        for k, v in extra.items():
            parts += ["", f"### {num}.4 {k.replace('_', ' ').title()}", "", "```text", " | ".join(v) if isinstance(v, list) else str(v), "```"]
    return "\n".join(parts)


def build() -> str:
    lines = [
        "# Volume 8 — Technical Domain Specifications",
        "",
        "**Document ID:** PEOPLE-VOLUME-08-TECHNICAL-DOMAIN-SPECIFICATIONS-1.0  ",
        "**Status:** DESIGN COMPLETE — PENDING FINAL CROSS-VOLUME FREEZE  ",
        "**Project Root:** H:\\people  ",
        "**Type:** IMPLEMENTATION-GOVERNING TECHNICAL SPECIFICATION  ",
        "",
        "> **Authority note:** This volume governs domain behavior precision for implementation. "
        "It does **not** authorize production implementation alone. "
        "It does **not** define database tables, API routes, or application frameworks — those belong to Volumes 9–11 and implementation packages after design freeze.",
        "",
        "---",
        "",
        "## Reconciliation with Architecture Audit",
        "",
        "Volume 8 **locks** the following positions that remediate architecture-audit contradictions (X-01 through X-08 and related findings):",
        "",
        "- **Field conditions** include `AMBIGUOUS` as a first-class operator-selectable condition alongside `PROVIDED`, `NOT_PROVIDED`, `UNREADABLE`, and `CORRECTED`.",
        "- **Human review** is required for uncertain identity outcomes in V1: `EXACT`, `POSSIBLE`, `CONFLICT`, and `NO_MATCH` resolution paths default to human decision (no silent auto-link or auto-create).",
        "- **Blank preference** on Volunteer and Email List fields persists as `UNKNOWN`; it must never silently become `NO`.",
        "- **Blank rows** with no meaningful person fields do **not** fabricate intake entries.",
        "",
        "Open Decision items **OD-B01 through OD-B12** that align with these locks are marked **PROPOSED RESOLVED** in this volume pending formal acceptance in the Owner Decision Log. "
        "They are **not** silently closed. Implementation packages must treat PROPOSED RESOLVED items as locked design intent until Owner records acceptance or supersession.",
        "",
        "---",
        "",
        "# PART I — Volume Governance",
        "",
        "## 1. Purpose",
        "",
        "Volume 8 translates approved product, workflow, data, and security design into **implementation-governing domain specifications**. "
        "Each domain defines stable business rules (`*-RULE-*`) and invariants (`*-INV-*` and `PEOPLE-INV-*`) that implementation code must satisfy. "
        "Volume 8 is the behavioral source of truth for domain logic at the engineering boundary.",
        "",
        "## 2. Governing Doctrine",
        "",
        "All intake processing follows the evidence and identity pipeline:",
        "",
        "```text",
        "Source → Raw → Normalized → Match → Human → Promotion → Canonical",
        "```",
        "",
        "| Stage | Meaning |",
        "| --- | --- |",
        "| **Source** | Original capture: private image bytes, upload metadata, batch context |",
        "| **Raw** | Operator transcription after submit: immutable evidence except formal CORRECTED history |",
        "| **Normalized** | Deterministic machine-readable forms for matching; no semantic invention |",
        "| **Match** | Candidate search, scoring, confidence tier, explanations |",
        "| **Human** | Reviewer or approved rule path for irreversible identity decisions |",
        "| **Promotion** | Controlled request to canonical people service |",
        "| **Canonical** | Durable shared person and provenance-aware attributes |",
        "",
        "Stages must remain distinguishable. Collapsing layers violates PEOPLE-INV-002.",
        "",
        "## 3. Five Truth Layers",
        "",
        "Every important value must remain classifiable as one of:",
        "",
        "1. **Source Evidence** — image, upload metadata, batch/page linkage  ",
        "2. **Raw Transcription** — operator-entered values after submit  ",
        "3. **Normalized Intake Value** — deterministic normalized counterparts  ",
        "4. **Match Decision** — candidates, tiers, resolutions  ",
        "5. **Canonical Person Value** — promoted attributes with provenance  ",
        "",
        "Match decisions and promotion outcomes are recorded explicitly and are not merged into raw or canonical layers without audit.",
        "",
        "## 4. Global Invariants",
        "",
    ]
    for iid, ititle, itext in GLOBAL_INVARIANTS:
        lines.append(f"**{iid} — {ititle}**  ")
        lines.append(f"{itext}")
        lines.append("")

    lines += [
        "---",
        "",
        "# PART II — Actors and Roles",
        "",
        "Roles may combine; effective permissions are union subject to Authorization domain rules.",
        "",
    ]
    for actor, perms in ACTORS.items():
        lines += [f"## {actor}", "", "### May", ""]
        for m in perms["may"]:
            lines.append(f"- {m}")
        lines += ["", "### May Not", ""]
        for m in perms["may_not"]:
            lines.append(f"- {m}")
        lines.append("")

    lines += ["---", "", "# PART III — Domain Specifications", ""]
    for d in DOMAINS:
        lines.append(domain_section(d))
        lines.append("")
        lines.append("---")
        lines.append("")

    lines += [
        "# PART IV — Transaction Boundaries",
        "",
        "## 34.1 Page Submit Boundary",
        "",
        "Page submit is a single atomic transaction: validate claim → validate entries → freeze raw → set normalized → transition page/entry states → enqueue match jobs → write audit. "
        "Partial submit prohibited.",
        "",
        "## 34.2 Claim Acquisition Boundary",
        "",
        "claim-next executes in one transaction: select eligible page with row lock → insert ACTIVE claim → update page assigned overlay → audit. "
        "Concurrent claimants serialize.",
        "",
        "## 34.3 Match Resolution Boundary",
        "",
        "Resolution and promotion request creation are one transaction per entry: persist resolution → create promotion request (if LINK/CREATE) → audit. "
        "Promotion execution is separate async transaction via canonical service.",
        "",
        "## 34.4 Promotion Result Boundary",
        "",
        "Applying PromotionResult updates entry matched_person_id, match status, and page completion flags in one transaction with audit. "
        "Failed promotion does not roll back resolution.",
        "",
        "## 34.5 Correction Reopen Boundary",
        "",
        "RETURN_FOR_CORRECTION or formal correction reopens transcription under new claim; creates correction history entries without deleting prior raw evidence.",
        "",
        "## 34.6 Audit-Required Commit Boundary",
        "",
        "Privileged mutations (override, reassign, disable user, image quarantine release, force complete) commit only if audit write succeeds, or compensating rollback per RECOVERY-RULE-010.",
        "",
        "---",
        "",
        "# PART V — Observability",
        "",
        "## 35. Structured Logging",
        "",
        "Logs use structured fields: timestamp, level, requestId, actorId, domain, operation, result code. "
        "No raw PII, secrets, session tokens, or signed URLs.",
        "",
        "## 36. Metrics",
        "",
        "Operational metrics: queue depth, claim count, submit throughput, match backlog, promotion pending/failed, job DEAD count, upload failure rate, API latency percentiles. "
        "Metrics are aggregated; no PII labels.",
        "",
        "## 37. Tracing",
        "",
        "Cross-service operations (upload-complete → derivative job → match job → promotion retry) propagate correlation/request IDs. "
        "Tracing complements audit events; does not replace them.",
        "",
        "---",
        "",
        "# PART VI — Privacy",
        "",
        "## 38. Data Minimization",
        "",
        "Each role receives minimum data required for assigned workflow (see Privacy and Retention design). "
        "Unrestricted bulk export prohibited in V1 unless Owner-approved separate policy.",
        "",
        "## 39. Image Access",
        "",
        "Source images accessed via authorized short-lived signed URLs after page-level authorization. "
        "Access events audited at metadata level (ImageAccessGranted).",
        "",
        "## 40. Retention and Deletion",
        "",
        "Retention states and legal hold per Retention domain. "
        "Deletion procedures require Owner approval for policy changes. "
        "People Intake does not directly delete canonical people.",
        "",
        "---",
        "",
        "# PART VII — Accessibility",
        "",
        "## 41. Operator UX Requirements",
        "",
        "Transcription and matching workspaces must support keyboard navigation, visible focus, readable contrast, and screen-reader labels for field conditions including AMBIGUOUS. "
        "Touch targets sized for mobile field upload and office entry.",
        "",
        "## 42. Language and Error Clarity",
        "",
        "User-facing errors use plain language with actionable recovery (retry upload, reclaim page, contact admin). "
        "Internal enum names not exposed in routine operator UI.",
        "",
        "---",
        "",
        "# PART VIII — Future Compatibility",
        "",
        "## 43. OCR and AI Assistance",
        "",
        "V1 excludes automated handwriting OCR and AI transcription as product dependencies. "
        "Future OCR/AI modules may suggest values but must not bypass human submit, field conditions, or identity review locks without Owner-approved amendment.",
        "",
        "## 44. Multi-Organization Tenancy",
        "",
        "V1 assumes single authorized organization context. "
        "Future multi-org support requires explicit tenant isolation in authz, queues, and canonical promotion contracts.",
        "",
        "## 45. Native Mobile Applications",
        "",
        "V1 is mobile-first web, not native app store delivery. "
        "Future native clients must use same upload-intent, claim, and submit contracts.",
        "",
        "## 46. Extended Field Sets",
        "",
        "Additional form fields require field dictionary amendment, Volume 8 rule additions, matching signal review, and promotion contract update before implementation.",
        "",
        "---",
        "",
        "# PART IX — End-to-End Acceptance Criteria",
        "",
        "## 47. Acceptance A — Field Capture",
        "",
        "Authorized uploader creates batch, captures/uploads images, completes upload; images stored privately; batch reaches READY.",
        "",
        "## 48. Acceptance B — Shared Queue Claim",
        "",
        "Two data entry users concurrently claim; each receives distinct page; second claim-next never returns actively claimed page.",
        "",
        "## 49. Acceptance C — Ten-Entry Transcription",
        "",
        "Operator transcribes up to ten rows with field conditions including AMBIGUOUS; blank preferences save as UNKNOWN; blank rows do not create entries.",
        "",
        "## 50. Acceptance D — Page Submit and Match Enqueue",
        "",
        "Submit under active claim freezes raw values, normalizes, transitions states, enqueues match jobs, audits.",
        "",
        "## 51. Acceptance E — Human Match Resolution",
        "",
        "Reviewer resolves POSSIBLE/CONFLICT/EXACT/NO_MATCH without auto-link/auto-create defaults; resolution recorded with method HUMAN.",
        "",
        "## 52. Acceptance F — Controlled Promotion",
        "",
        "Promotion request succeeds or retries; canonical updated via service; page not COMPLETED while promotion pending; provenance recorded.",
        "",
        "## 53. Acceptance G — Correction Loop",
        "",
        "Reviewer returns page for correction; data entry edits under new claim; correction history preserves prior raw; rematch occurs.",
        "",
        "## 54. Acceptance H — Audit and Recovery",
        "",
        "Admin searches audit for submit/match/promotion chain; dead promotion job surfaces alert; operator retry succeeds idempotently.",
        "",
        "---",
        "",
        "# PART X — Locked Domain Decisions",
        "",
        "The following forty decisions are **locked** by Volume 8 unless Owner supersedes via Decision Log:",
        "",
        "| ID | Decision | Trace | Notes |",
        "| --- | --- | --- | --- |",
    ]
    for lid, dec, trace, notes in LOCKED_DECISIONS:
        lines.append(f"| {lid} | {dec} | {trace} | {notes} |")

    lines += [
        "",
        "---",
        "",
        "# PART XI — Deferred Implementation Decisions",
        "",
        "The following remain explicitly deferred to later volumes or packages:",
        "",
        "| ID | Topic | Register | When |",
        "| --- | --- | --- | --- |",
    ]
    for did, topic, reg, when in DEFERRED:
        lines.append(f"| {did} | {topic} | {reg} | {when} |")

    lines += [
        "",
        "---",
        "",
        "# PART XII — Completion Standard",
        "",
        "## 57. Volume 8 Readiness Criteria",
        "",
        "Volume 8 is design-complete when every row in the readiness table below is satisfied.",
        "",
        "## 58. Readiness Table",
        "",
        "| Criterion | Required State | Current |",
        "| --- | --- | --- |",
        "| All domain rule IDs published | Every `*-RULE-*` in Part III present | Yes |",
        "| All domain invariant IDs published | Every `*-INV-*` and `PEOPLE-INV-*` present | Yes |",
        "| Cross-volume terminology aligned | Field conditions, tri-state, confidence tiers match Volume 3 | Pending freeze |",
        "| OD-B PROPOSED RESOLVED items | Recorded in Owner Decision Log | Pending Owner |",
        "| No contradiction with Volume 0 Constitution | Verified | Yes |",
        "| Architecture audit reconciliation section | Published | Yes |",
        "| Transaction boundaries defined | Part IV complete | Yes |",
        "| E2E acceptance A–H defined | Part IX complete | Yes |",
        "| Locked decisions enumerated | 40 decisions Part X | Yes |",
        "| Implementation authorization | Gate G-9 APPROVED, G-10 OPEN | **Not authorized** |",
        "",
        "## 59. Next Volume",
        "",
        "**Volume 9 — Database Specifications** translates these domain rules into physical schema, tables, indexes, constraints, and migration discipline after shared-database compatibility audit (OD-B05) and Owner acceptance of PROPOSED RESOLVED decisions.",
        "",
        "---",
        "",
        "## Document Control",
        "",
        "| Field | Value |",
        "| --- | --- |",
        "| Canonical path | `docs/volumes/volume-08-technical-specifications/VOLUME_08_TECHNICAL_DOMAIN_SPECIFICATIONS.md` |",
        "| Legacy pointer | `docs/09_technical_specifications/VOLUME_08_TECHNICAL_DOMAIN_SPECIFICATIONS.md` |",
        "| Supersedes | Individual `TECH_SPEC_*.md` drafts as behavioral index (those files remain supplementary until merged) |",
        "| Encoding | UTF-8 |",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    content = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(content, encoding="utf-8")
    rule_count = content.count("-RULE-")
    inv_count = content.count("-INV-")
    line_count = content.count("\n") + 1
    print(f"Wrote {OUT}")
    print(f"Lines: {line_count}")
    print(f"RULE IDs (substring matches): {rule_count}")
    print(f"INV IDs (substring matches): {inv_count}")


if __name__ == "__main__":
    main()
