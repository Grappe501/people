/**
 * Generates Implementation Library Volumes 8–13, Engineering Catalogs,
 * and Implementation Package framework from approved design.
 * Docs only — no application code.
 */
import fs from "fs";
import path from "path";

const ROOT = "H:\\people";

function write(rel, contents) {
  const full = path.join(ROOT, rel);
  fs.mkdirSync(path.dirname(full), { recursive: true });
  fs.writeFileSync(full, contents.replace(/\n/g, "\r\n").replace(/\r\r\n/g, "\r\n"));
  console.log("wrote", rel);
}

const HDR = (title, volume, status = "draft_complete") =>
  `# ${title}

**Library volume:** ${volume}  
**Status:** ${status}  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked \`PENDING_FREEZE\`. Do not invent policy to fill gaps.

---
`;

const FOOT = (refs) => `
---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No \`PENDING_FREEZE\` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

${refs}
`;

// ── Volume 8 indexes + specs ──────────────────────────────────────────

write(
  "docs/09_technical_specifications/README.md",
  `# Volume 8 — Technical Specifications

**Purpose:** Turn every major domain decision into precise engineering specifications. These are the implementation source of truth for domain behavior.

| Spec | File |
| --- | --- |
| Authentication | \`TECH_SPEC_AUTHENTICATION.md\` |
| Authorization | \`TECH_SPEC_AUTHORIZATION.md\` |
| Batch | \`TECH_SPEC_BATCH.md\` |
| Page | \`TECH_SPEC_PAGE.md\` |
| Queue | \`TECH_SPEC_QUEUE.md\` |
| Claim | \`TECH_SPEC_CLAIM.md\` |
| Entry | \`TECH_SPEC_ENTRY.md\` |
| Matching | \`TECH_SPEC_MATCHING.md\` |
| Promotion | \`TECH_SPEC_PROMOTION.md\` |
| Image Storage | \`TECH_SPEC_IMAGE_STORAGE.md\` |
| Audit | \`TECH_SPEC_AUDIT.md\` |
| Background Jobs | \`TECH_SPEC_BACKGROUND_JOBS.md\` |

**Rule:** Cursor must not invent domain behavior absent from these specs and Volume 0.
`
);

const techSpecs = [
  [
    "TECH_SPEC_AUTHENTICATION.md",
    "Authentication Specification",
    `
## 1. Purpose

Establish verified identity for every request. Approved users only. No public signup in V1.

## 2. Provider

**Designed:** Supabase Auth (email magic link / password per Owner config).  
**Adapter rule:** Auth provider is swappable behind an AuthPort interface; app code never calls provider SDKs outside the auth adapter.

## 3. Session Model

| Concern | Rule |
| --- | --- |
| Session transport | HTTP-only secure cookie (preferred) or approved bearer for server routes |
| Server trust | Browser tokens are untrusted; validate session server-side every request |
| Idle timeout | Configurable; default per security design |
| Absolute timeout | Configurable |
| Concurrent sessions | Allowed unless Owner policy restricts |
| Sign-out | Invalidate server session; clear client cookie |

## 4. Approved-User Gate

After provider authentication succeeds:

1. Resolve local \`app_user\` / approved-user record by auth subject ID / email.  
2. If missing → \`ACCESS_NOT_APPROVED\` (Access Denied screen).  
3. If \`disabled\` → \`ACCOUNT_DISABLED\`.  
4. Else attach \`userId\`, \`roles[]\`, \`displayName\` to request context.

## 5. Routes

| Path | Auth required | Notes |
| --- | --- | --- |
| Sign-in handling | No (bootstrap) | Provider callback only |
| All \`/api/v1/*\` | Yes | Except documented health if any |
| All app workspaces | Yes | |

## 6. Invariants

- Individual accounts only (no shared passwords).  
- Disabled users lose access immediately on next request.  
- Failed auth never reveals whether email exists when policy requires uniformity.  
- Auth events audited: sign-in success/failure (no secrets), sign-out, disable/enable.

## 7. Failure Modes

| Condition | Code | UX |
| --- | --- | --- |
| No session | AUTH_REQUIRED | Redirect sign-in |
| Not approved | ACCESS_NOT_APPROVED | Access Denied |
| Disabled | ACCOUNT_DISABLED | Account Disabled |
| Provider down | DEPENDENCY_UNAVAILABLE | Degraded message |

## 8. Tests Required

- Unauthenticated API → 401  
- Unapproved user → denied  
- Disabled user → denied  
- Approved user with valid session → 200 on \`GET /session\`  
- Sign-out clears subsequent access  
`,
    "- Volume 4: Auth architecture\n- Volume 10: Session endpoints\n- Volume 9: \`app_users\` table (conceptual)",
  ],
  [
    "TECH_SPEC_AUTHORIZATION.md",
    "Authorization Specification",
    `
## 1. Purpose

Deny-by-default access control: **role AND record AND state**.

## 2. Roles (V1)

\`UPLOADER\` · \`DATA_ENTRY\` · \`REVIEWER\` · \`ADMIN\` · \`OWNER\`

Users may hold multiple roles. Effective permissions = union, still subject to record/state checks.

## 3. Evaluation Order

1. Authenticated?  
2. Approved & enabled?  
3. Role allows operation?  
4. Record ownership / assignment allows?  
5. Resource state allows transition?  
6. Else deny → \`ROLE_NOT_ALLOWED\` or \`RECORD_ACCESS_DENIED\`

## 4. Matrix Summary (normative detail in Volume 4 authz matrix)

| Capability | U | DE | R | A | O |
| --- | --- | --- | --- | --- | --- |
| Create batch / upload | ✓ | policy | | ✓ | ✓ |
| Claim entry queue | | ✓ | | ✓ | ✓ |
| Submit page | | ✓ | | ✓ | ✓ |
| Match resolve | | | ✓ | ✓ | ✓ |
| Reassign claim | | | | ✓ | ✓ |
| Manage users | | | | ✓ | ✓ |
| Force complete / reopen | | | | ✓ | ✓ |
| Change security policy | | | | | ✓ |

\`PENDING_FREEZE\`: Data Entry upload rights marked “Optional by policy” in audit — Owner must lock before coding upload authz for DE.

## 5. Record Rules

- Claimant may edit claimed page draft.  
- Non-claimant cannot mutate draft (except Admin/Owner override with audit).  
- Image access requires page-level authorization + signed URL issuance.  
- Audit search: Admin/Owner (and scoped roles if later approved).

## 6. Server Enforcement

UI may hide controls; **server must enforce**. Never trust client role claims.

## 7. Tests Required

- Each role can perform allowed ops  
- Each role blocked on forbidden ops  
- Cross-user claim mutation denied  
- Override paths audited  
`,
    "- Volume 4: Authorization matrix\n- \`contracts/schemas/role-permissions.json\`",
  ],
  [
    "TECH_SPEC_BATCH.md",
    "Batch Specification",
    `
## 1. Purpose

Group pages from one capture effort with shared metadata.

## 2. Identity

- \`batchId\` UUID internal  
- Optional human code \`PI-YYYYMMDD-#####\`

## 3. Metadata Fields

| Field | Required | Notes |
| --- | --- | --- |
| title / label | optional | Operator-friendly |
| eventName | optional | |
| county | optional | |
| city | optional | |
| collectionDate | recommended | |
| collectedBy | optional | |
| notes | optional | |
| createdBy | system | uploader userId |
| status | system | see state machine |

## 4. Lifecycle

\`DRAFT → UPLOADING → READY → IN_PROGRESS → NEEDS_ATTENTION → COMPLETED → ARCHIVED\`

Completion requires all pages resolved (see Engineering Catalog / state machines).

## 5. Invariants

- Batch contains pages, not people.  
- Deleting a batch with pages is Admin-only and must preserve evidence or soft-delete.  
- Progress metrics derived from page states, not stored as sole truth.

## 6. Operations

Create · Patch metadata · Complete upload · Archive · Reopen (Admin)

## 7. Audit

\`BatchCreated\` \`BatchUpdated\` \`BatchUploadCompleted\` \`BatchArchived\` \`BatchReopened\`
`,
    "- Volume 3 domain model\n- Volume 9 \`intake_batches\`\n- Volume 10 batch endpoints",
  ],
  [
    "TECH_SPEC_PAGE.md",
    "Page Specification",
    `
## 1. Purpose

Primary queue work unit: one source image + 0–10 entries.

## 2. Identity

- \`pageId\` UUID  
- \`pageNumber\` unique within batch  
- Human code may include batch + page ordinal

## 3. Core Fields

| Field | Notes |
| --- | --- |
| batchId | required FK |
| pageNumber | 1..N within batch |
| status | page state machine |
| version | optimistic concurrency integer |
| imageQualityStatus | pending/pass/fail/\`PENDING_FREEZE\` labels |
| blankPage | boolean exception path |
| unreadablePage | boolean exception path |

## 4. Lifecycle

See Engineering Catalog — Page state machine. UX labels must not expose raw enum names to routine users.

## 5. Invariants

- At most one active original image version.  
- At most one active claim.  
- Entry count ≤ 10.  
- Page not \`COMPLETED\` while any entry has pending promotion (\`PENDING_FREEZE\` alignment with UX vocabulary — OD-B*).  
- Submit requires active claim (or audited override).

## 6. Exception Paths

- Upload failure → retryable page state  
- Unreadable → return path without inventing people  
- Blank page → documented zero-entry submit (\`PENDING_FREEZE\` vs API 1–10 — OD-B*)

## 7. Audit

\`PageRegistered\` \`PageUploaded\` \`PageStatusChanged\` \`PageSubmitted\` \`PageReturned\` \`PageReopened\` \`PageForceCompleted\`
`,
    "- Volume 2 workflows\n- Volume 9 \`intake_pages\`\n- Volume 10 page endpoints",
  ],
  [
    "TECH_SPEC_QUEUE.md",
    "Queue Specification",
    `
## 1. Purpose

Shared multi-user work lists for entry and matching.

## 2. Queues

| Queue | Consumer roles | Eligibility |
| --- | --- | --- |
| Entry queue | DATA_ENTRY, ADMIN, OWNER | Pages ready for entry, unclaimed or expired claim |
| Match queue | REVIEWER, ADMIN, OWNER | Entries/pages needing human match review |
| Correction queue | DATA_ENTRY (+admin) | Pages returned for correction |
| Exception queue | ADMIN, OWNER | Failures, stuck states |

## 3. Ordering

Default: priority (if set) then oldest first (created/ready timestamp). Admin may boost priority.

## 4. Listing vs Claim

- \`GET\` lists are eventually consistent views.  
- \`claim-next\` is the atomic assignment path — never “select then claim” in two non-atomic client steps as the only path.

## 5. Filters

Batch, county, status, assignee (admin), age — server-side only.

## 6. Invariants

- Claim-next must not return a page already actively claimed.  
- Concurrent claim-next must serialize via DB lock / unique active claim constraint.

## 7. Tests

- Two concurrent claim-next → distinct pages or one \`NO_PAGE_AVAILABLE\`  
- Expired claim returns to queue  
`,
    "- Volume 2 Queue and Claiming\n- TECH_SPEC_CLAIM.md",
  ],
  [
    "TECH_SPEC_CLAIM.md",
    "Claim Specification",
    `
## 1. Purpose

Atomic exclusive edit lock for a page (entry work) or match work unit (\`PENDING_FREEZE\`: match-claim underspecified in audit — lock policy before coding).

## 2. Claim Record

| Field | Notes |
| --- | --- |
| claimId | UUID |
| pageId | FK |
| claimantUserId | FK |
| claimType | ENTRY | MATCH (\`PENDING_FREEZE\`) |
| status | ACTIVE | RELEASED | EXPIRED | REASSIGNED |
| claimedAt | timestamptz |
| expiresAt | timestamptz |
| renewedAt | timestamptz |
| version | concurrency |

## 3. Defaults

- TTL: **30 minutes** from last renew/activity (design default).  
- Renew on draft save / heartbeat.  
- Warning UI before expiry.

## 4. Operations

| Op | Behavior |
| --- | --- |
| claim-next | Select eligible → insert active claim uniquely → audit |
| claim specific | Admin/override or allowed path |
| renew | Extend expiresAt if owner + ACTIVE |
| release | Soft release; draft preserved |
| reassign | Admin: release prior, create new, audit |
| expire job | Mark EXPIRED; page returns to queue; draft preserved |

## 5. Invariants

- **One ACTIVE claim per page per claimType.**  
- Expired ≠ delete draft.  
- Stale writes after lost claim → \`PAGE_CLAIM_OWNERSHIP_LOST\` / \`PAGE_CLAIM_EXPIRED\`.

## 6. Concurrency

Use transactional \`SELECT … FOR UPDATE\` on page + unique partial index on \`(page_id) WHERE status = 'ACTIVE'\`.

## 7. Audit

\`PageClaimed\` \`ClaimRenewed\` \`ClaimReleased\` \`ClaimExpired\` \`ClaimReassigned\`
`,
    "- Volume 2 Queue and Claiming\n- Volume 9 \`intake_page_claims\`",
  ],
  [
    "TECH_SPEC_ENTRY.md",
    "Entry Specification",
    `
## 1. Purpose

One handwritten person line; unique identity; ≤10 per page.

## 2. Fields (conceptual)

Raw + normalized pairs for: first/last name, phone, email, ZIP, volunteer (YES/NO/UNKNOWN), email list (YES/NO/UNKNOWN), notes, rowNumber 1–10, field conditions (BLANK/UNREADABLE/etc.).

## 3. Draft vs Submitted

- Draft: mutable under active claim; autosaved.  
- Submitted: raw values treated as evidence; corrections via correction history, not silent overwrite.

## 4. Invariants

- \`UNKNOWN ≠ NO\`.  
- Blank UI → UNKNOWN for tri-state fields.  
- Unreadable ≠ blank.  
- Row numbers unique per page.  
- Max 10 entries.

## 5. Normalization

Deterministic rules (lowercase email, digits phone, trim names). Never invent missing data.

## 6. Lifecycle

Draft → Transcribed → Matching → (Exact/Possible/No/Conflict) → Linked/Created → Completed (+ correction branches).

\`PENDING_FREEZE\`: exact-match auto-link policy; 0-entry unreadable submit vs API 1–10.

## 7. Audit

\`EntryDraftSaved\` \`EntrySubmitted\` \`EntryCorrected\` \`EntryMatchStatusChanged\`
`,
    "- Volume 3 Field dictionary\n- Volume 9 \`intake_entries\`",
  ],
  [
    "TECH_SPEC_MATCHING.md",
    "Matching Specification",
    `
## 1. Purpose

Find candidate canonical people; score; require human review for uncertain identity.

## 2. Principles (Constitution)

- Prefer temporary duplicates over false merges.  
- Household shared contacts do not independently prove identity.  
- AI may assist ranking; humans decide irreversible identity (\`PENDING_FREEZE\` auto-link).

## 3. Pipeline

1. Normalize entry fields.  
2. Search candidates (email, phone, name+ZIP, etc. per matching engine design).  
3. Score + tier: EXACT | POSSIBLE | CONFLICT | NONE.  
4. Persist candidates + explanations.  
5. Auto path only if frozen policy allows; else queue for review.  
6. Resolution → promotion request when needed.

## 4. Resolution Options

\`LINK_EXISTING\` · \`CREATE_NEW\` · \`DEFER\` · \`RETURN_FOR_CORRECTION\` · \`NO_ACTION\`

## 5. Invariants

- One final resolution per entry version.  
- Conflict never auto-merged.  
- Ranking explanations stored for audit.  
- Stable sort for equal scores (personId tie-break).

## 6. Degradation

If canonical domain unavailable: pause candidate lookup / final resolutions needing canonical; preserve transcription.

## 7. Audit

\`MatchRunStarted\` \`MatchCandidatesGenerated\` \`MatchResolved\` \`MatchDeferred\` \`MatchReturnedForCorrection\`
`,
    "- Volume 3 Matching engine\n- Volume 9 match tables\n- OD-B exact-match lock",
  ],
  [
    "TECH_SPEC_PROMOTION.md",
    "Promotion Specification",
    `
## 1. Purpose

Controlled bridge from intake resolution to canonical people domain (Model B).

## 2. Flow

Match resolution → \`PromotionRequest\` → Canonical service → \`PromotionResult\` → update entry/page status.

Browsers never call raw canonical mutation APIs.

## 3. Request Payload (conceptual)

entryId, resolutionId, action (CREATE|LINK|UPDATE_ATTRIBUTES), attribute decisions, idempotencyKey, actorId, provenance bundle.

## 4. Invariants

- Idempotent retry safe.  
- Provenance required for every promoted value.  
- Page not falsely marked complete while promotion pending.  
- No RedDirt operational table writes.  
- No routine automatic merges.

## 5. Failure

Canonical unavailable → keep resolution; mark promotion pending/retryable; user-safe message.

## 6. Audit

\`PromotionRequested\` \`PromotionSucceeded\` \`PromotionFailed\` \`PromotionRetried\`
`,
    "- Volume 3 Canonical person contract\n- Volume 4/6 engineering integration contract",
  ],
  [
    "TECH_SPEC_IMAGE_STORAGE.md",
    "Image Storage Specification",
    `
## 1. Purpose

Private storage of source images + optional derivatives; temporary authorized access only.

## 2. Model

| Object | Notes |
| --- | --- |
| Original | Immutable bytes; content hash |
| Display derivative | Optional resized/rotated for UI |
| Thumbnail | Optional |

Postgres stores metadata + storage keys — not primary blob store.

## 3. Upload Flow

1. Create/register page.  
2. \`upload-intent\` → authorized PUT target + intentId.  
3. Client uploads to storage.  
4. \`upload-complete\` → verify size/type/hash → activate image version → audit.

## 4. Access

\`GET image-access\` → short-lived signed URL after authz. Never public buckets for source images.

## 5. Invariants

- Replace image creates new version; prior retained for evidence.  
- Duplicate hash detection warned (not auto-delete).  
- Logs never contain signed URLs.

## 6. Limits

Max size / MIME allowlist per configuration catalog. Errors: \`UPLOAD_TOO_LARGE\` \`UPLOAD_TYPE_NOT_ALLOWED\`.

## 7. Audit

\`UploadIntentCreated\` \`ImageUploaded\` \`ImageReplaced\` \`ImageAccessGranted\` (metadata only)
`,
    "- Volume 3/5 Image storage architecture\n- Volume 9 storage tables",
  ],
  [
    "TECH_SPEC_AUDIT.md",
    "Audit Specification",
    `
## 1. Purpose

Append-only, attributable history of meaningful actions.

## 2. Event Shape

who · what · when · where (requestId, IP hash if approved) · subject refs (batch/page/entry/person) · why (optional) · result

No raw PII dumps, secrets, or signed URLs in audit payloads. Store references + redacted summaries.

## 3. Write Rules

- High-risk ops require successful audit write before commit completes (or compensating policy).  
- Audit is append-only in normal operations.  
- Failures escalate severity CRITICAL when privileged action cannot be audited.

## 4. Query

Admin/Owner search by actor, type, date, batch/page/entry. Paginated.

## 5. Retention

Per privacy/retention design (\`PENDING_FREEZE\` retention provider decisions).

## 6. Catalog

Normative event names live in Engineering Catalog — Event Catalog.
`,
    "- Volume 4 Logging and audit\n- EVENT_CATALOG.md",
  ],
  [
    "TECH_SPEC_BACKGROUND_JOBS.md",
    "Background Jobs Specification",
    `
## 1. Purpose

Reliable async work: matching runs, claim expiry, promotion retry, derivative generation, notifications (if any — V1 limited).

## 2. Job Record

jobId, type, payload ref, status (PENDING|RUNNING|SUCCEEDED|FAILED|DEAD), attempts, nextRunAt, lastError code, idempotencyKey.

## 3. Types (V1 intent)

| Type | Trigger |
| --- | --- |
| MATCH_EVALUATE_PAGE / ENTRY | After submit |
| CLAIM_EXPIRE | Scheduler |
| PROMOTION_RETRY | Failed promotion |
| IMAGE_DERIVATIVE | After upload |
| BATCH_PROGRESS_RECOMPUTE | Optional |

## 4. Rules

- Idempotent handlers.  
- Exponential backoff.  
- Dead-letter after N attempts → exception queue + alert.  
- Never lose transcription because a job failed.

## 5. Observability

Admin visibility into failing jobs; no PII in logs.
`,
    "- Volume 4 Background processing contract\n- Volume 9 job table (if used)",
  ],
];

for (const [file, title, body, refs] of techSpecs) {
  write(
    `docs/09_technical_specifications/${file}`,
    HDR(title, "8 — Technical Specifications") + body + FOOT(refs)
  );
}

console.log("Volume 8 done");

// ── Volume 9 Database ─────────────────────────────────────────────────

write(
  "docs/10_database_specifications/README.md",
  `# Volume 9 — Database Specifications

**Purpose:** Engineer every table before SQL/Prisma. **No migrations in this phase.**

**Constraint:** Shared database must be audited before any migration. Table names are conceptual until compatibility report completes.

| Table | File |
| --- | --- |
| intake_batches | \`TABLE_intake_batches.md\` |
| intake_pages | \`TABLE_intake_pages.md\` |
| intake_entries | \`TABLE_intake_entries.md\` |
| intake_page_claims | \`TABLE_intake_page_claims.md\` |
| intake_source_images | \`TABLE_intake_source_images.md\` |
| intake_match_candidates | \`TABLE_intake_match_candidates.md\` |
| intake_match_resolutions | \`TABLE_intake_match_resolutions.md\` |
| intake_promotion_requests | \`TABLE_intake_promotion_requests.md\` |
| intake_audit_events | \`TABLE_intake_audit_events.md\` |
| app_users | \`TABLE_app_users.md\` |
| Overview | \`DATABASE_SPEC_OVERVIEW.md\` |
`
);

write(
  "docs/10_database_specifications/DATABASE_SPEC_OVERVIEW.md",
  HDR("Database Specification Overview", "9 — Database Specifications") +
    `
## Ownership

People Intake owns \`intake_*\` and local \`app_users\` / approval tables. Canonical \`people*\` structures are shared-domain (names TBD after audit).

## Identifier Rules

- UUID primary keys  
- Human-readable operational codes secondary  
- Never email/phone as PK  
- Avoid sequential public IDs exposing volume  

## Uniqueness Checklist

- (batch_id, page_number) unique  
- (page_id, row_number) unique  
- One ACTIVE claim per page (partial unique index)  
- One final resolution per entry version  
- One active original image version per page  
- Idempotency key unique per operation scope  

## Migration Strategy (future)

1. Shared DB compatibility audit report  
2. Additive migrations only  
3. Separate migration credential  
4. Expand/contract for renames  
5. Rollback notes per migration  

## Naming

snake_case tables/columns. Status enums match Engineering Catalog state machines once frozen.
` +
    FOOT("- Volume 3 Database architecture\n- Volume 6 audit OD shared DB")
);

function tableDoc(name, purpose, owner, fields, indexes, constraints, lifecycle, example, migration) {
  return (
    HDR(`Table: ${name}`, "9 — Database Specifications") +
    `
## Purpose

${purpose}

## Ownership

${owner}

## Fields

| Column | Type (conceptual) | Null | Notes |
| --- | --- | --- | --- |
${fields}

## Indexes

${indexes}

## Constraints

${constraints}

## Relationships

See ERD / related table specs.

## Lifecycle

${lifecycle}

## Example Row (illustrative, not PII-real)

\`\`\`json
${example}
\`\`\`

## Migration Strategy

${migration}

## Implementation Notes

- Do not create this table until Gate G-10 + migration authorization + shared DB audit.  
- Exact types may adjust to Postgres conventions after audit.
` +
    FOOT("- DATABASE_SPEC_OVERVIEW.md\n- Volume 3 ERD")
  );
}

const tables = [
  [
    "TABLE_intake_batches.md",
    "intake_batches",
    "Collection of pages from one capture effort.",
    "People Intake",
    `| id | uuid | no | PK |
| public_code | text | yes | Human code |
| title | text | yes | |
| event_name | text | yes | |
| county | text | yes | |
| city | text | yes | |
| collection_date | date | yes | |
| collected_by | text | yes | |
| notes | text | yes | |
| status | text | no | Batch state enum |
| created_by | uuid | no | FK app_users |
| created_at | timestamptz | no | |
| updated_at | timestamptz | no | |`,
    "- idx_batches_status_created\n- idx_batches_created_by",
    "- PK id\n- status in allowed enum set",
    "DRAFT → … → ARCHIVED per state catalog",
    `{ "id": "…", "status": "READY", "county": "Pulaski" }`,
    "Create after audit; additive only.",
  ],
  [
    "TABLE_intake_pages.md",
    "intake_pages",
    "One photographed sheet; primary queue unit.",
    "People Intake",
    `| id | uuid | no | PK |
| batch_id | uuid | no | FK |
| page_number | int | no | Unique in batch |
| status | text | no | Page state |
| version | int | no | Optimistic lock |
| blank_page | boolean | no | default false |
| unreadable_page | boolean | no | default false |
| priority | int | yes | Queue boost |
| created_at | timestamptz | no | |
| updated_at | timestamptz | no | |`,
    "- idx_pages_queue (status, priority, created_at)\n- unique (batch_id, page_number)",
    "- FK batch_id\n- page_number >= 1",
    "UPLOADING → … → COMPLETED/ARCHIVED",
    `{ "id": "…", "page_number": 3, "status": "READY_FOR_ENTRY", "version": 4 }`,
    "Create with batches; FKs validated.",
  ],
  [
    "TABLE_intake_entries.md",
    "intake_entries",
    "One person line on a page.",
    "People Intake",
    `| id | uuid | no | PK |
| page_id | uuid | no | FK |
| row_number | int | no | 1–10 |
| status | text | no | Entry state |
| first_name_raw | text | yes | |
| last_name_raw | text | yes | |
| phone_raw | text | yes | |
| email_raw | text | yes | |
| zip_raw | text | yes | |
| volunteer_status | text | yes | YES/NO/UNKNOWN |
| email_list_status | text | yes | YES/NO/UNKNOWN |
| *_normalized | text | yes | Parallel cols |
| field_conditions | jsonb | yes | Per-field flags |
| canonical_person_id | uuid | yes | After promotion |
| version | int | no | |
| created_at | timestamptz | no | |
| updated_at | timestamptz | no | |`,
    "- unique (page_id, row_number)\n- idx_entries_match_status\n- idx_entries_norm_email / phone",
    "- row_number between 1 and 10\n- volunteer_status in (YES,NO,UNKNOWN) when set",
    "DRAFT → TRANSCRIBED → matching → completed",
    `{ "row_number": 1, "volunteer_status": "UNKNOWN", "status": "DRAFT" }`,
    "Additive columns preferred for new fields.",
  ],
  [
    "TABLE_intake_page_claims.md",
    "intake_page_claims",
    "Exclusive work lock on a page.",
    "People Intake",
    `| id | uuid | no | PK |
| page_id | uuid | no | FK |
| claimant_user_id | uuid | no | FK |
| claim_type | text | no | ENTRY / MATCH PENDING_FREEZE |
| status | text | no | ACTIVE/RELEASED/EXPIRED/REASSIGNED |
| claimed_at | timestamptz | no | |
| expires_at | timestamptz | no | |
| renewed_at | timestamptz | yes | |`,
    "- **partial unique** (page_id) WHERE status='ACTIVE' (and claim_type when multi-type)\n- idx_claims_expiry",
    "- One active claim rule enforced in DB",
    "Unclaimed → Active → Released/Expired/Reassigned",
    `{ "status": "ACTIVE", "claim_type": "ENTRY" }`,
    "Critical concurrency index — test before prod.",
  ],
  [
    "TABLE_intake_source_images.md",
    "intake_source_images",
    "Metadata for private source images and versions.",
    "People Intake",
    `| id | uuid | no | PK |
| page_id | uuid | no | FK |
| version_number | int | no | |
| storage_key | text | no | Object key |
| content_hash | text | yes | |
| byte_size | bigint | yes | |
| mime_type | text | yes | |
| is_active_original | boolean | no | |
| created_by | uuid | no | |
| created_at | timestamptz | no | |`,
    "- idx_images_page\n- idx_images_hash\n- unique active original per page (partial)",
    "- storage_key not publicly guessable",
    "Versions append; active pointer moves on replace",
    `{ "version_number": 1, "is_active_original": true, "mime_type": "image/jpeg" }`,
    "No blobs in Postgres as primary store.",
  ],
  [
    "TABLE_intake_match_candidates.md",
    "intake_match_candidates",
    "Scored possible canonical matches for an entry.",
    "People Intake",
    `| id | uuid | no | PK |
| entry_id | uuid | no | FK |
| match_run_id | uuid | yes | FK |
| person_id | uuid | no | Canonical ref |
| tier | text | no | EXACT/POSSIBLE/CONFLICT |
| score | numeric | yes | |
| reasons | jsonb | no | Explainability |
| rank | int | no | |
| status | text | no | OPEN/SELECTED/REJECTED |`,
    "- idx_candidates_entry_rank\n- idx_candidates_person",
    "- tier in allowed set",
    "Created by match job; resolved with resolution",
    `{ "tier": "POSSIBLE", "rank": 1, "reasons": ["normalized_phone"] }`,
    "Retain after resolution for audit.",
  ],
  [
    "TABLE_intake_match_resolutions.md",
    "intake_match_resolutions",
    "Final human/system determination for an entry.",
    "People Intake",
    `| id | uuid | no | PK |
| entry_id | uuid | no | FK |
| resolution | text | no | LINK_EXISTING/CREATE_NEW/DEFER/RETURN_FOR_CORRECTION/NO_ACTION |
| selected_person_id | uuid | yes | |
| selected_candidate_id | uuid | yes | |
| decided_by | uuid | no | |
| decided_at | timestamptz | no | |
| notes | text | yes | |
| entry_version | int | no | |`,
    "- unique final resolution per entry version\n- idx_resolutions_entry",
    "- One final per entry version",
    "Written in resolve transaction with promotion request when needed",
    `{ "resolution": "CREATE_NEW" }`,
    "Immutable after write except formal void by admin policy.",
  ],
  [
    "TABLE_intake_promotion_requests.md",
    "intake_promotion_requests",
    "Controlled promotion to canonical domain.",
    "People Intake",
    `| id | uuid | no | PK |
| entry_id | uuid | no | |
| resolution_id | uuid | no | |
| action | text | no | CREATE/LINK/UPDATE |
| status | text | no | PENDING/SUCCEEDED/FAILED |
| idempotency_key | text | no | Unique in scope |
| request_payload | jsonb | no | Redacted/minimized |
| result_payload | jsonb | yes | |
| attempts | int | no | |
| created_at | timestamptz | no | |
| updated_at | timestamptz | no | |`,
    "- unique idempotency_key\n- idx_promo_status",
    "- FK to resolution",
    "PENDING → SUCCEEDED/FAILED → retry",
    `{ "action": "CREATE", "status": "PENDING" }`,
    "Coordinate with canonical schema audit.",
  ],
  [
    "TABLE_intake_audit_events.md",
    "intake_audit_events",
    "Append-only meaningful action log.",
    "People Intake",
    `| id | uuid | no | PK |
| event_type | text | no | Catalog name |
| actor_user_id | uuid | yes | |
| batch_id | uuid | yes | |
| page_id | uuid | yes | |
| entry_id | uuid | yes | |
| person_id | uuid | yes | |
| request_id | text | yes | |
| summary | text | no | Non-PII |
| payload | jsonb | yes | Redacted |
| created_at | timestamptz | no | |`,
    "- idx_audit_created\n- idx_audit_type\n- idx_audit_page\n- idx_audit_actor",
    "- Append-only grants for app role",
    "Insert only",
    `{ "event_type": "PageClaimed", "summary": "Page claimed for entry" }`,
    "Partition by time later if volume requires.",
  ],
  [
    "TABLE_app_users.md",
    "app_users",
    "Approved local user profiles linked to auth subject.",
    "People Intake",
    `| id | uuid | no | PK |
| auth_subject | text | no | Unique provider subject |
| email | citext/text | no | |
| display_name | text | yes | |
| roles | text[] | no | |
| status | text | no | ACTIVE/DISABLED |
| created_at | timestamptz | no | |
| updated_at | timestamptz | no | |
| disabled_at | timestamptz | yes | |`,
    "- unique auth_subject\n- unique email\n- idx_users_status",
    "- roles subset of known roles",
    "Invited → Active → Disabled",
    `{ "roles": ["DATA_ENTRY"], "status": "ACTIVE" }`,
    "No public signup rows.",
  ],
];

for (const t of tables) {
  write(`docs/10_database_specifications/${t[0]}`, tableDoc(...t.slice(1)));
}

console.log("Volume 9 done");

// ── Volume 10 API ─────────────────────────────────────────────────────

write(
  "docs/11_api_specifications/README.md",
  `# Volume 10 — API Specifications

**Base path:** \`/api/v1\`  
**Rule:** Cursor must not invent endpoints. Every operation needs a completed contract here (or linked file) before coding.

| Group | File |
| --- | --- |
| Conventions | \`API_CONVENTIONS.md\` |
| Session & Users | \`API_SESSION_AND_USERS.md\` |
| Batches | \`API_BATCHES.md\` |
| Pages & Uploads | \`API_PAGES_AND_UPLOADS.md\` |
| Queue & Claims | \`API_QUEUE_AND_CLAIMS.md\` |
| Transcription | \`API_TRANSCRIPTION.md\` |
| Matching | \`API_MATCHING.md\` |
| Promotion | \`API_PROMOTION.md\` |
| Admin | \`API_ADMIN.md\` |
`
);

write(
  "docs/11_api_specifications/API_CONVENTIONS.md",
  HDR("API Conventions", "10 — API Specifications") +
    `
## Envelope

Success: \`{ "ok": true, "data": {}, "meta": { "requestId": "…" } }\`  
Error: \`{ "ok": false, "error": { "code", "message", "retryable" }, "meta": { "requestId" } }\`

## Requirements per operation

Operation ID · method · path · purpose · roles · record authz · request schema · response schema · state prerequisites · transition · transaction boundary · idempotency · audit events · error codes · retry · privacy classification

## Auth

All routes authenticated except approved sign-in bootstrap.

## Idempotency

Header \`Idempotency-Key\` required on claim-next, submit, resolve-match, promotion-request, upload-complete.
` +
    FOOT("- Volume 4 API contracts\n- ERROR_CATALOG.md")
);

function apiGroup(file, title, endpoints) {
  write(
    `docs/11_api_specifications/${file}`,
    HDR(title, "10 — API Specifications") +
      endpoints +
      FOOT("- API_CONVENTIONS.md\n- api-endpoint-registry.json")
  );
}

apiGroup(
  "API_SESSION_AND_USERS.md",
  "API — Session & Users",
  `
### GET /api/v1/session
**Op:** getSession · Roles: any authenticated · Returns session user + roles · Errors: AUTH_REQUIRED · Audit: none (or SessionChecked if required)

### GET /api/v1/me
**Op:** getMe · Profile fields · Errors: AUTH_REQUIRED

### POST /api/v1/sign-out
**Op:** signOut · Clears session · Audit: UserSignedOut

### GET /api/v1/users
**Op:** listUsers · Roles: ADMIN, OWNER · Paginated

### POST /api/v1/users/invite
**Op:** inviteUser · Roles: ADMIN, OWNER · Body: email, roles · Audit: UserInvited · Idempotency: yes

### PATCH /api/v1/users/{userId}
**Op:** updateUser · Roles: ADMIN, OWNER · Audit: UserUpdated

### POST /api/v1/users/{userId}/disable | enable
**Op:** disableUser / enableUser · Roles: ADMIN, OWNER · Audit: UserDisabled / UserEnabled
`
);

apiGroup(
  "API_BATCHES.md",
  "API — Batches",
  `
### GET /api/v1/batches
List batches for role scope.

### POST /api/v1/batches
Create DRAFT/UPLOADING batch · Idempotency yes · Audit: BatchCreated

### GET /api/v1/batches/{batchId}
Detail + progress summary.

### PATCH /api/v1/batches/{batchId}
Metadata update · Audit: BatchUpdated

### POST /api/v1/batches/{batchId}/complete-upload
Mark upload complete when pages registered · Audit: BatchUploadCompleted · Errors: INVALID_STATE_TRANSITION

### POST /api/v1/batches/{batchId}/archive | reopen
Admin/Owner · Audited
`
);

apiGroup(
  "API_PAGES_AND_UPLOADS.md",
  "API — Pages & Uploads",
  `
### POST /api/v1/batches/{batchId}/pages
Register page slot · Audit: PageRegistered

### POST /api/v1/pages/{pageId}/upload-intent
Returns storage upload instructions · Authz page · Audit: UploadIntentCreated

### POST /api/v1/pages/{pageId}/upload-complete
Verify object · activate image · Idempotency yes · Errors: UPLOAD_* · Audit: ImageUploaded

### POST /api/v1/pages/{pageId}/replace-image
New version · Audit: ImageReplaced

### GET /api/v1/pages/{pageId}
Page detail + entry summaries as authorized

### GET /api/v1/pages/{pageId}/image-access
Signed URL · short TTL · Audit metadata only · Errors: IMAGE_ACCESS_DENIED

### POST /api/v1/pages/{pageId}/image-quality
Pass/fail quality review · state transition
`
);

apiGroup(
  "API_QUEUE_AND_CLAIMS.md",
  "API — Queue & Claims",
  `
### GET /api/v1/queues/entry
List eligible pages (non-authoritative vs claim).

### POST /api/v1/queues/entry/claim-next
**Critical path.** Atomic claim · Idempotency required · Transaction: select+lock+insert claim+audit  
Errors: ACTIVE_CLAIM_EXISTS, NO_PAGE_AVAILABLE, PAGE_ALREADY_CLAIMED, DATABASE_UNAVAILABLE  
Audit: PageClaimed  
Response: pageId, claimId, expiresAt, image access bootstrap

### POST /api/v1/pages/{pageId}/claim
Claim specific page when allowed.

### POST /api/v1/pages/{pageId}/claim/renew
Owner only · extends TTL · Audit: ClaimRenewed

### POST /api/v1/pages/{pageId}/claim/release
Owner or admin · Audit: ClaimReleased

### POST /api/v1/pages/{pageId}/claim/reassign
Admin · Audit: ClaimReassigned
`
);

apiGroup(
  "API_TRANSCRIPTION.md",
  "API — Transcription",
  `
### GET /api/v1/pages/{pageId}/draft
Requires claim ownership (or admin) · Returns entries + version

### PUT /api/v1/pages/{pageId}/draft
Autosave · version check · Errors: STALE_WRITE, PAGE_CLAIM_* · Audit: EntryDraftSaved (throttled policy OK)

### POST /api/v1/pages/{pageId}/submit
Validate 0–10/\`PENDING_FREEZE\` · normalize · release claim · enqueue match · Idempotency yes · Transactional  
Errors: ENTRY_LIMIT_EXCEEDED, VALIDATION_FAILED, INVALID_STATE_TRANSITION, STALE_WRITE  
Audit: PageSubmitted

### POST /api/v1/pages/{pageId}/return-unreadable
Exception path · Audit: PageReturned

### POST /api/v1/pages/{pageId}/corrections
Formal correction after return · Audit: EntryCorrected
`
);

apiGroup(
  "API_MATCHING.md",
  "API — Matching",
  `
### GET /api/v1/matching/queue
Reviewer queue listing

### POST /api/v1/matching/claim-next
\`PENDING_FREEZE\` match-claim policy · Audit when locked

### GET /api/v1/entries/{entryId}/match-review
Candidates + entry + image access

### POST /api/v1/entries/{entryId}/resolve-match
Body: resolution + candidate/person + field decisions · Idempotency yes · May create promotion  
Errors: MATCH_ALREADY_RESOLVED, INVALID_CANDIDATE, REVIEW_CLAIM_LOST, STALE_WRITE  
Audit: MatchResolved

### POST /api/v1/entries/{entryId}/defer-match
Audit: MatchDeferred

### POST /api/v1/entries/{entryId}/return-correction
Audit: MatchReturnedForCorrection
`
);

apiGroup(
  "API_PROMOTION.md",
  "API — Promotion",
  `
### GET /api/v1/promotion/{promotionId}
Status for operators/admin

### POST /api/v1/entries/{entryId}/promotion-request
Usually server-internal after resolve; if exposed, REVIEWER+ · Idempotency yes · Audit: PromotionRequested

### POST /api/v1/promotion/{promotionId}/retry
Admin/system · Audit: PromotionRetried

**Browser must not call raw canonical mutation endpoints.**
`
);

apiGroup(
  "API_ADMIN.md",
  "API — Admin",
  `
### GET /api/v1/admin/overview
Counts: queue depth, claims, exceptions, job failures

### GET /api/v1/admin/exceptions
Stuck pages/jobs

### GET /api/v1/admin/audit
Search audit events

### GET /api/v1/admin/claims
Active/expired claims

### POST /api/v1/admin/pages/{pageId}/reopen
Audit: PageReopened

### POST /api/v1/admin/pages/{pageId}/force-complete
Owner/Admin guarded · Audit: PageForceCompleted
`
);

console.log("Volume 10 done");

// ── Volume 11 UI ──────────────────────────────────────────────────────

write(
  "docs/12_ui_specifications/README.md",
  `# Volume 11 — UI Specifications

Engineering specs for screens (not visual mockups). Screen inventory: 44 screens in \`contracts/documentation/screen-inventory.json\`.

| Group | File |
| --- | --- |
| Auth | \`UI_AUTH.md\` |
| Capture | \`UI_CAPTURE.md\` |
| Transcription | \`UI_TRANSCRIPTION.md\` |
| Matching | \`UI_MATCHING.md\` |
| Administration | \`UI_ADMIN.md\` |
| Shared | \`UI_SHARED.md\` |
`
);

function uiGroup(file, title, body) {
  write(
    `docs/12_ui_specifications/${file}`,
    HDR(title, "11 — UI Specifications") + body + FOOT("- Volume 2 UX docs\n- Volume 12 components")
  );
}

uiGroup(
  "UI_AUTH.md",
  "UI — Authentication Screens",
  `
## Sign In
**Layout:** Centered form; brand secondary to clarity.  
**Components:** Email/password or magic-link controls per config.  
**States:** Loading · Error (provider) · Success redirect.  
**A11y:** Labels, focus order, error announced.  
**Mobile:** Full width, large tap targets.

## Access Denied
Explain approved-user requirement; no sensitive enumeration.

## Account Disabled
Contact admin message; sign-out control.
`
);

uiGroup(
  "UI_CAPTURE.md",
  "UI — Capture Screens",
  `
## Uploader Home
Primary CTA: New Batch. List recent batches + status badges.

## New Batch
Metadata fields; continue to camera/select.

## Camera Capture / Select Images
Mobile-first; multi-image; review before upload.

## Review Images
Reorder/remove; confirm.

## Upload Progress / Complete
Per-page progress; retry failed pages; never fake success.

## My Batches / Batch Detail
Progress header; page list; link to detail.
`
);

uiGroup(
  "UI_TRANSCRIPTION.md",
  "UI — Transcription Screens",
  `
## Data Entry Home
Claim Next primary; secondary My Work / Correction Queue.

## Shared Queue
Read-only list; Claim Next still primary path.

## Page Workspace (critical)
**Layout:** Image pane + entry editor; mobile stacks image top/collapsible.  
**Components:** ImageViewer, EntryEditor, ProgressHeader, StatusBadge, save indicator.  
**Interactions:** Autosave on blur/interval; renew claim; Submit & Open Next.  
**Validation:** Inline field errors; UNKNOWN default for tri-state blanks.  
**Loading:** Skeleton image + form.  
**Empty:** Prompt add person rows up to 10.  
**Error:** Claim lost modal → draft preserved messaging.  
**A11y:** Keyboard between fields; image controls labeled; live region for save status.  
**Mobile:** Large Yes/No/Blank controls; sticky primary action.

## Full-Screen Image Viewer
Zoom/pan/rotate; return to workspace without losing draft.

## Page Review / Submitted
Summary; next claim CTA.

## Correction Queue
Returned pages only.
`
);

uiGroup(
  "UI_MATCHING.md",
  "UI — Matching Screens",
  `
## Reviewer Home / Match Queue
Claim next match work.

## Match Workspace
Entry summary + candidates ranked + ImageViewer.  
Actions: Link · Create New · Defer · Return correction.  
Conflict UI forces explicit field decisions.

## Field Conflict Review / Create New Person Review
Confirm attributes before promotion request.

## Match Complete / Deferred Review
Clear next step.
`
);

uiGroup(
  "UI_ADMIN.md",
  "UI — Administration Screens",
  `
Overview metrics · Batch/Queue/Claim management · Exception queue · User management · Audit search/detail · Settings (Owner).  
All destructive actions use ConfirmationDialog + audit.
`
);

uiGroup(
  "UI_SHARED.md",
  "UI — Shared Screens",
  `
Help · Notifications (V1 minimal) · Account · Session Expired · Offline State · General Error.  
Recovery-first copy per Content guide.
`
);

console.log("Volume 11 done");

// ── Volume 12 Components ──────────────────────────────────────────────

write(
  "docs/13_component_library/README.md",
  `# Volume 12 — Component Library

Reusable UI components. Each documents props, behavior, a11y, events, styling hooks, tests.

| Component | File |
| --- | --- |
| Image Viewer | \`CMP_ImageViewer.md\` |
| Claim Card | \`CMP_ClaimCard.md\` |
| Queue Card | \`CMP_QueueCard.md\` |
| Batch Card | \`CMP_BatchCard.md\` |
| Progress Header | \`CMP_ProgressHeader.md\` |
| Confirmation Dialog | \`CMP_ConfirmationDialog.md\` |
| Audit Timeline | \`CMP_AuditTimeline.md\` |
| Match Candidate Card | \`CMP_MatchCandidateCard.md\` |
| Entry Editor | \`CMP_EntryEditor.md\` |
| Status Badge | \`CMP_StatusBadge.md\` |
`
);

function cmp(file, name, body) {
  write(
    `docs/13_component_library/${file}`,
    HDR(`Component: ${name}`, "12 — Component Library") +
      body +
      FOOT("- Volume 11 UI specs\n- Volume 2 Accessibility spec")
  );
}

cmp(
  "CMP_ImageViewer.md",
  "ImageViewer",
  `
## Props
\`imageAccessUrl | fetcher\`, \`rotation\`, \`initialZoom\`, \`onRotate\`, \`onError\`, \`alt\`

## Behavior
Pan/zoom/rotate; does not persist rotations to original without replace-image flow; handles expired signed URL via refresh callback.

## Accessibility
Keyboard zoom/pan shortcuts documented; focusable controls; alt text required.

## Events
\`onReady\` \`onError\` \`onRotateRequest\`

## Styling
Full-bleed within pane; no decorative overlay badges on image (Constitution UX).

## Tests
Rotate; expired URL refresh; keyboard operability.
`
);

cmp(
  "CMP_ClaimCard.md",
  "ClaimCard",
  `
## Props
\`pageSummary\`, \`expiresAt\`, \`onRenew\`, \`onRelease\`, \`warningThresholdSec\`

## Behavior
Shows expiry countdown; warning state; actions per authz.

## A11y
Time remaining announced politely (not spam).

## Tests
Warning appears near expiry; actions hidden when unauthorized.
`
);

cmp(
  "CMP_QueueCard.md",
  "QueueCard",
  `
## Props
\`title\`, \`meta\`, \`status\`, \`age\`, \`onOpen\`  
Non-primary path vs Claim Next — informational.
`
);

cmp(
  "CMP_BatchCard.md",
  "BatchCard",
  `
## Props
\`batch\`, \`progress\`, \`onOpen\`  
Progress derived from page states.
`
);

cmp(
  "CMP_ProgressHeader.md",
  "ProgressHeader",
  `
## Props
\`batchProgress | pageProgress\`, \`saveStatus\`  
Always visible save status on transcription surfaces.
`
);

cmp(
  "CMP_ConfirmationDialog.md",
  "ConfirmationDialog",
  `
## Props
\`title\`, \`body\`, \`confirmLabel\`, \`destructive\`, \`onConfirm\`, \`onCancel\`  
Focus trap; Escape cancels; confirm not default for destructive.
`
);

cmp(
  "CMP_AuditTimeline.md",
  "AuditTimeline",
  `
## Props
\`events[]\` (summaries only)  
Chronological; no raw PII payloads rendered by default.
`
);

cmp(
  "CMP_MatchCandidateCard.md",
  "MatchCandidateCard",
  `
## Props
\`candidate\`, \`selected\`, \`onSelect\`  
Shows tier, reasons, rank; never hides conflict signals.
`
);

cmp(
  "CMP_EntryEditor.md",
  "EntryEditor",
  `
## Props
\`entry\`, \`onChange\`, \`disabled\`, \`rowNumber\`  
Tri-state Yes/No/Blank; unreadable toggles; validation messages.  
Blank → UNKNOWN for volunteer/email-list.
`
);

cmp(
  "CMP_StatusBadge.md",
  "StatusBadge",
  `
## Props
\`status\`, \`label\` (user-facing), \`tone\`  
Never color-only; include text label.
`
);

console.log("Volume 12 done");

// ── Engineering Catalogs ──────────────────────────────────────────────

write(
  "docs/14_engineering_catalogs/README.md",
  `# Engineering Library — Catalogs

Project-wide references companion to Volumes 8–13.

| Catalog | File |
| --- | --- |
| State Machine Catalog | \`STATE_MACHINE_CATALOG.md\` |
| Error Catalog | \`ERROR_CATALOG.md\` |
| Event Catalog | \`EVENT_CATALOG.md\` |
| Configuration Catalog | \`CONFIGURATION_CATALOG.md\` |
`
);

write(
  "docs/14_engineering_catalogs/STATE_MACHINE_CATALOG.md",
  HDR("State Machine Catalog", "Engineering Catalogs") +
    `
## Rule

No state exists in code without a documented diagram and transition table here (or linked machine JSON under \`contracts/schemas/\`).

## Batch

\`\`\`text
DRAFT → UPLOADING → READY → IN_PROGRESS → NEEDS_ATTENTION → COMPLETED → ARCHIVED
\`\`\`

## Page

\`\`\`text
UPLOADING → UPLOADED → IMAGE_REVIEW → READY_FOR_ENTRY → ASSIGNED → IN_PROGRESS
→ ENTRY_COMPLETE → MATCHING → NEEDS_MATCH_REVIEW → NEEDS_CORRECTION → COMPLETED → ARCHIVED
\`\`\`

Exception branches: upload failure, unreadable, admin reopen/force-complete.

**PENDING_FREEZE:** Unify UX vs engineering vocabulary (audit F-C04).

## Entry

\`\`\`text
DRAFT → TRANSCRIBED → MATCHING → EXACT_MATCH | POSSIBLE_MATCH | NO_MATCH | CONFLICT
→ LINKED_EXISTING | CREATED_NEW → COMPLETED
\`\`\`

## Claim

\`\`\`text
UNCLAIMED → CLAIMED/ACTIVE → EXPIRING_SOON → EXPIRED | RELEASED | REASSIGNED
\`\`\`

## Promotion

\`\`\`text
PENDING → SUCCEEDED | FAILED → (retry) PENDING
\`\`\`

## Job

\`\`\`text
PENDING → RUNNING → SUCCEEDED | FAILED | DEAD
\`\`\`

## User

\`\`\`text
INVITED → ACTIVE → DISABLED
\`\`\`

## Diagrams

See also Volume 2 state machines mermaid and \`contracts/schemas/*-state-machine.json\` / \`state-transition-registry.json\`.
` +
    FOOT("- Volume 2 State machines\n- TECH_SPEC_* lifecycle sections")
);

write(
  "docs/14_engineering_catalogs/ERROR_CATALOG.md",
  HDR("Error Catalog", "Engineering Catalogs") +
    `
## Registry

Machine file: \`contracts/schemas/error-code-registry.json\` (expand to match this catalog before coding).

| Code | HTTP | Retryable | User-safe intent |
| --- | --- | --- | --- |
| AUTH_REQUIRED | 401 | no | Sign in required |
| ACCESS_NOT_APPROVED | 403 | no | Account not approved |
| ACCOUNT_DISABLED | 403 | no | Account disabled |
| ROLE_NOT_ALLOWED | 403 | no | Not permitted |
| RECORD_ACCESS_DENIED | 403 | no | Not permitted |
| BATCH_NOT_FOUND | 404 | no | Not found |
| PAGE_NOT_FOUND | 404 | no | Not found |
| ENTRY_NOT_FOUND | 404 | no | Not found |
| PAGE_ALREADY_CLAIMED | 409 | no | Assigned to another user |
| PAGE_CLAIM_EXPIRED | 409 | no | Claim expired; draft preserved |
| PAGE_CLAIM_OWNERSHIP_LOST | 409 | no | No longer your claim |
| ACTIVE_CLAIM_EXISTS | 409 | no | Finish or release current claim |
| NO_PAGE_AVAILABLE | 200/404 | no | Queue empty (product choice of empty UX) |
| STALE_WRITE | 409 | yes | Refresh and retry |
| INVALID_STATE_TRANSITION | 409 | no | Action not available now |
| ENTRY_LIMIT_EXCEEDED | 422 | no | Max 10 people |
| VALIDATION_FAILED | 422 | no | Fix highlighted fields |
| UPLOAD_TYPE_NOT_ALLOWED | 415 | no | Unsupported file type |
| UPLOAD_TOO_LARGE | 413 | no | File too large |
| UPLOAD_CONFIRMATION_FAILED | 409 | yes | Retry upload confirm |
| IMAGE_ACCESS_DENIED | 403 | no | Cannot view image |
| MATCH_ALREADY_RESOLVED | 409 | no | Already resolved |
| INVALID_CANDIDATE | 422 | no | Invalid candidate |
| INVALID_FIELD_DECISION | 422 | no | Complete field decisions |
| REVIEW_CLAIM_LOST | 409 | no | Review claim lost |
| PROMOTION_PENDING | 409 | yes | Waiting on promotion |
| PROMOTION_ALREADY_COMPLETED | 409 | no | Already promoted |
| CANONICAL_SERVICE_UNAVAILABLE | 503 | yes | Try again later |
| IDEMPOTENCY_CONFLICT | 409 | no | Conflicting replay |
| RATE_LIMITED | 429 | yes | Slow down |
| DATABASE_UNAVAILABLE | 503 | yes | Could not save |
| DEPENDENCY_UNAVAILABLE | 503 | yes | Service unavailable |
| INTERNAL_ERROR | 500 | maybe | Something went wrong |

Each code must define operator action + log severity before production.
` +
    FOOT("- Volume 4 Error contract")
);

write(
  "docs/14_engineering_catalogs/EVENT_CATALOG.md",
  HDR("Event Catalog", "Engineering Catalogs") +
    `
## Rule

Every meaningful mutation emits a catalogued audit event.

| Event | When |
| --- | --- |
| UserSignedIn | Successful auth (no secrets) |
| UserSignedOut | Sign-out |
| UserInvited | Admin invite |
| UserUpdated | Role/profile change |
| UserDisabled | Disable |
| UserEnabled | Enable |
| BatchCreated | New batch |
| BatchUpdated | Metadata change |
| BatchUploadCompleted | Upload complete |
| BatchArchived | Archive |
| BatchReopened | Reopen |
| PageRegistered | Page slot created |
| PageUploaded | Image activated |
| PageStatusChanged | Status transition |
| PageClaimed | Claim acquired |
| ClaimRenewed | TTL extended |
| ClaimReleased | Voluntary release |
| ClaimExpired | Expiry job |
| ClaimReassigned | Admin reassign |
| EntryDraftSaved | Draft persist |
| PageSubmitted | Submit success |
| PageReturned | Unreadable/return |
| EntryCorrected | Correction saved |
| ImageReplaced | New image version |
| UploadIntentCreated | Intent issued |
| ImageAccessGranted | Signed URL issued (meta only) |
| MatchRunStarted | Job start |
| MatchCandidatesGenerated | Candidates stored |
| MatchResolved | Resolution saved |
| MatchDeferred | Defer |
| MatchReturnedForCorrection | Return |
| PromotionRequested | Request created |
| PromotionSucceeded | Canonical OK |
| PromotionFailed | Canonical fail |
| PromotionRetried | Retry |
| PageReopened | Admin |
| PageForceCompleted | Admin |
| JobFailed | Dead/fail visible |

Payloads: references + redacted summaries only.
` +
    FOOT("- TECH_SPEC_AUDIT.md")
);

write(
  "docs/14_engineering_catalogs/CONFIGURATION_CATALOG.md",
  HDR("Configuration Catalog", "Engineering Catalogs") +
    `
## Rule

Nothing undocumented. Secrets never in git.

## Environment variables (conceptual names)

| Name | Purpose | Secret |
| --- | --- | --- |
| DATABASE_URL | App DB (least privilege) | yes |
| DATABASE_MIGRATE_URL | Migrations only | yes |
| AUTH_SUPABASE_URL | Auth provider | no |
| AUTH_SUPABASE_ANON_KEY | Public anon if required | careful |
| AUTH_SUPABASE_SERVICE_ROLE | Server only | yes |
| STORAGE_ENDPOINT / keys | Private object storage | yes |
| STORAGE_BUCKET_SOURCE | Source images bucket | no |
| SIGNED_URL_TTL_SECONDS | Image access TTL | no |
| CLAIM_TTL_SECONDS | Default 1800 | no |
| CLAIM_RENEW_WINDOW_SECONDS | Renew policy | no |
| NETLIFY / site keys | Deploy | yes |
| LOG_LEVEL | Logging | no |
| FEATURE_* | Flags below | no |

## Feature flags (V1 intent)

| Flag | Default | Notes |
| --- | --- | --- |
| FEATURE_EXACT_MATCH_AUTOLINK | false | PENDING_FREEZE |
| FEATURE_DATA_ENTRY_UPLOAD | false | PENDING_FREEZE policy |
| FEATURE_MATCH_CLAIM | false | PENDING_FREEZE |
| FEATURE_OFFLINE_DRAFT | false | PENDING_FREEZE V1 offline |

## Runtime settings

Max upload bytes · MIME allowlist · rate limits · session timeouts · job retry limits.

Document actual names in \`.env.example\` at Phase 0 — still no production secrets in repo.
` +
    FOOT("- Volume 4 Configuration contract")
);

console.log("Catalogs done");

// ── Volume 13 Platform Standards ──────────────────────────────────────

write(
  "docs/15_platform_standards/README.md",
  `# Volume 13 — Canonical Platform Standards

Standards every future application must follow when interacting with the shared civic/tech platform. People Intake is the first adopter, not the only one.
`
);

write(
  "docs/15_platform_standards/PLATFORM_STANDARDS.md",
  HDR("Canonical Platform Standards", "13 — Canonical Platform Standards") +
    `
## Purpose

Define shared platform expectations for People Intake, RedDirt, Relationship Command Center, ContactListSOS, Arkansas Civic University, and future apps.

These standards extend Volume 0 Article II (Universal Engineering Constitution).

## 1. Canonical Person Standards

- Single canonical identity domain.  
- Apps contribute via controlled promotion / approved write APIs.  
- Apps consume via read contracts.  
- No silent merges; merge is an explicit privileged workflow.  
- Attributes carry provenance.

## 2. Shared Identity Standards

- External auth subjects map to per-app or shared identity records as designed.  
- Individual accounts; disablement honored across session validation.  
- Roles are app-scoped unless a shared permissions model is explicitly adopted.

## 3. Common Audit Model

- Append-only events with who/what/when/subject refs.  
- Redacted payloads; no secrets/signed URLs.  
- High-risk actions require durable audit.

## 4. Shared Attachment Model

- Private object storage; metadata in DB.  
- Temporary authorized access.  
- Originals preserved across replacements.

## 5. Shared Notification Model (future)

- Notifications are explicit product features, not side effects of random writes.  
- V1 People Intake does not send email/SMS.  
- Future shared notifier must be opt-in per app with audit.

## 6. Shared Organization Model (future)

- Organizations/tenants defined once if multi-org appears.  
- People Intake V1 may be single-org operationally; do not hard-code assumptions that block org_id later.

## 7. Shared Permissions Model

- Deny by default.  
- Server-side enforcement.  
- Matrix documented per app; shared verbs preferred (\`read\`, \`write\`, \`admin\`, \`promote\`).

## 8. Shared Event Model

- Past-tense catalog names (\`PageClaimed\`).  
- Stable event types; additive evolution.  
- Consumers must tolerate unknown future event types.

## 9. Shared API Conventions

- Versioned HTTP (\`/api/v1\`).  
- Standard envelope.  
- Idempotency keys on mutating critical paths.  
- Consistent error codes where domain-overlap exists.

## 10. Shared UI Conventions

- Plain language; recovery-first errors.  
- Accessibility baseline (keyboard, labels, non-color-only status).  
- Do not expose internal enum names to routine users.

## 11. Shared Testing Standards

- Authz denial tests mandatory.  
- Concurrency tests for claims/idempotency where applicable.  
- No production deploy without automated regression for critical paths.

## Adoption Rule

New apps should link this Volume 13 in their constitution/README and document deviations via Decision Log.
` +
    FOOT("- Volume 0 Article II\n- Canonical person contracts")
);

console.log("Volume 13 done");

// ── Phase C Implementation Packages ───────────────────────────────────

write(
  "docs/16_implementation_packages/README.md",
  `# Implementation Packages

Executable Cursor work units. **No package authorizes coding until Gate G-10.**

| Doc | Purpose |
| --- | --- |
| \`PACKAGE_TEMPLATE.md\` | Copy for every package |
| \`PACKAGE_INDEX.md\` | Planned packages mapped to orchestration phases |
| \`PKG-0.0-SPEC-LIBRARY-BOOTSTRAP.md\` | This documentation library build (docs only) |
`
);

write(
  "docs/16_implementation_packages/PACKAGE_TEMPLATE.md",
  `# Package X.Y — Title

**Status:** NOT_STARTED | IN_PROGRESS | BLOCKED | READY_FOR_REVIEW | COMPLETE  
**Phase:** (orchestration 0–12)  
**Depends on:**  
**Blocks:**  

## Objectives

## Scope

## Out of Scope

## Files Expected

## Tests

## Validation

\`\`\`powershell
$env:TEMP="H:\\people\\.tmp"
$env:TMP="H:\\people\\.tmp"
$env:TMPDIR="H:\\people\\.tmp"
$env:npm_config_cache="H:\\people\\.npm-cache"
npm run drive:validate
# lint / typecheck / test when available
\`\`\`

## Rollback

## Expected Commits

## Expected Documentation Updates

## Exit Criteria

## Spec References

- Volume 0  
- Volume 8…  
- Volume 9…  
- Volume 10…  
`
);

write(
  "docs/16_implementation_packages/PACKAGE_INDEX.md",
  `# Implementation Package Index

Mapped to Volume 7 orchestration phases. All coding packages **BLOCKED** until Gate G-10.

| Package | Phase | Title | Status |
| --- | --- | --- | --- |
| PKG-0.0 | Pre | Spec library bootstrap | COMPLETE (docs) |
| PKG-0.1 | 0 | Foundation scaffolding | BLOCKED |
| PKG-1.1 | 1 | Auth session + approved users | BLOCKED |
| PKG-1.2 | 1 | Authorization middleware + matrix | BLOCKED |
| PKG-2.1 | 2 | Storage adapter + upload intent | BLOCKED |
| PKG-2.2 | 2 | Image access + hash | BLOCKED |
| PKG-3.1 | 3 | Batch APIs + UI capture shell | BLOCKED |
| PKG-3.2 | 3 | Page registration + upload complete | BLOCKED |
| PKG-4.1 | 4 | Claim-next atomic service | BLOCKED |
| PKG-4.2 | 4 | Renew/expire/reassign | BLOCKED |
| PKG-5.1 | 5 | Draft autosave + EntryEditor | BLOCKED |
| PKG-5.2 | 5 | Submit page transaction | BLOCKED |
| PKG-6.1 | 6 | Match candidate generation | BLOCKED |
| PKG-6.2 | 6 | Resolve match workspace | BLOCKED |
| PKG-7.1 | 7 | Promotion request + retry | BLOCKED |
| PKG-8.1 | 8 | Admin overview + users | BLOCKED |
| PKG-8.2 | 8 | Audit viewer | BLOCKED |
| PKG-9.1 | 9 | Jobs + claim expiry worker | BLOCKED |
| PKG-10.1 | 10 | A11y pass | BLOCKED |
| PKG-11.1 | 11 | Perf/security hardening | BLOCKED |
| PKG-12.1 | 12 | Launch readiness | BLOCKED |

Next documentation packages (still no app code): deepen PENDING_FREEZE sections after audit remediation.
`
);

write(
  "docs/16_implementation_packages/PKG-0.0-SPEC-LIBRARY-BOOTSTRAP.md",
  `# Package 0.0 — Spec Library Bootstrap

**Status:** COMPLETE  
**Phase:** Pre-implementation  

## Objectives

Create Volumes 8–13, Engineering Catalogs, and package framework so Cursor cannot invent architecture during later coding.

## Scope

Documentation under \`docs/09_*\` … \`docs/16_*\`; governance index updates.

## Out of Scope

Application code, migrations, Netlify feature deploy.

## Exit Criteria

- [x] Volume 8 technical specs present  
- [x] Volume 9 table specs present  
- [x] Volume 10 API specs present  
- [x] Volume 11–12 UI/components present  
- [x] Catalogs present  
- [x] Volume 13 platform standards present  
- [x] Package template + index present  
`
);

console.log("Packages done");
console.log("ALL GENERATION COMPLETE");
