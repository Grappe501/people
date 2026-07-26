# People Intake — Decision Log

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-GOVERNANCE-FOUNDATION-1.0

---

## How to Use

Each decision includes:

- Decision ID
- Date
- Status
- Decision
- Reason
- Alternatives considered
- Consequences
- Related files
- Revisit trigger

Statuses: `accepted` | `provisional` | `superseded` | `open`

---

### D-001

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Project root is `H:\people`. |
| Reason | Independent app location; permanent H-drive protocol. |
| Alternatives | Nest under `H:\SOSWebsite\people`. |
| Consequences | All controllable artifacts stay under `H:\people`. |
| Related files | `PEOPLE_INTAKE_H_DRIVE_PROTOCOL.md` |
| Revisit trigger | Drive topology change |

### D-002

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Application remains separate from RedDirt. |
| Reason | Smaller surface, independent deploy/rollback, least privilege. |
| Alternatives | Build as a RedDirt module. |
| Consequences | Shared contracts, no direct code imports. |
| Related files | `PEOPLE_INTAKE_SCOPE_AND_BOUNDARIES.md` |
| Revisit trigger | Explicit product consolidation decision |

### D-003

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Application uses the same hosted database ecosystem as RedDirt. |
| Reason | Canonical people must be immediately usable by RedDirt. |
| Alternatives | Separate database with sync. |
| Consequences | Requires least-privilege credentials and additive schema discipline. |
| Related files | `PEOPLE_INTAKE_MASTER_BUILD_PLAN.md` |
| Revisit trigger | Hosting or tenancy change |

### D-004

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Page is the primary work unit. |
| Reason | Volunteer sheets often contain multiple people; office work is page-centric. |
| Alternatives | One person per image as primary unit. |
| Consequences | Queue claims, submission, and status are page-level. |
| Related files | Product charter; future workflow docs |
| Revisit trigger | Form redesign proving single-person sheets only |

### D-005

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Each page supports up to ten intake entries. |
| Reason | Matches hard-copy volunteer sheet capacity. |
| Alternatives | Unlimited rows; fixed eight rows. |
| Consequences | UI and validation enforce max ten active entries. |
| Related files | Scope; future form behavior spec |
| Revisit trigger | Physical form layout change |

### D-006

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Each line receives a unique intake-entry identity. |
| Reason | Auditability and independent matching. |
| Alternatives | One blob of people per page. |
| Consequences | Entry-level matching, provenance, and corrections. |
| Related files | Glossary; domain model (planned) |
| Revisit trigger | None expected |

### D-007

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Capture, transcription, and matching are separate workflows. |
| Reason | Different locations, skills, and cognitive loads. |
| Alternatives | Single combined field+office flow. |
| Consequences | Role-based homes and queue stages. |
| Related files | Product charter |
| Revisit trigger | Staffing model change |

### D-008

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Multiple users share one queue. |
| Reason | Parallel office processing. |
| Alternatives | Personal only queues. |
| Consequences | Claiming and concurrency controls required. |
| Related files | Future queue docs |
| Revisit trigger | Single-operator-only deployment |

### D-009

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Page claims prevent simultaneous editing. |
| Reason | Avoid last-write-wins corruption. |
| Alternatives | Optimistic locking only; soft advisory locks. |
| Consequences | Atomic claim, renewal, expiration, admin release. |
| Related files | Future claiming docs |
| Revisit trigger | Proven claim model failure in design audit |

### D-010

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Matching occurs after transcription. |
| Reason | Protect typing speed; separate judgment from transcription. |
| Alternatives | Interrupt on every row with duplicate UI. |
| Consequences | Matching queue and post-submit processing. |
| Related files | Matching philosophy in master plan |
| Revisit trigger | Strong user demand for inline exact-match prompts only |

### D-011

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Uncertain matches require human review. |
| Reason | Unsafe merges destroy trust and provenance. |
| Alternatives | Always auto-merge on score thresholds. |
| Consequences | Match review workspace required. |
| Related files | Scope no-automatic-merge rules |
| Revisit trigger | None for Version 1 |

### D-012

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Original images remain private. |
| Reason | PII and source evidence. |
| Alternatives | Public CDN with obscure URLs. |
| Consequences | Signed URLs; private buckets; authz on every image read. |
| Related files | Scope; future storage architecture |
| Revisit trigger | None expected |

### D-013

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Images are stored in object storage, not as database blobs. |
| Reason | Backup size, query performance, operational flexibility. |
| Alternatives | Postgres bytea primary storage. |
| Consequences | Storage keys in Postgres; private object store required. |
| Related files | Master plan image storage section |
| Revisit trigger | Hosting constraint forcing alternative |

### D-014

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Volunteer and Email List use `YES`, `NO`, and `UNKNOWN`. |
| Reason | Blank is not No. |
| Alternatives | Boolean only; nullable boolean without explicit UNKNOWN. |
| Consequences | UI shows Yes / No / Blank; DB stores three states. |
| Related files | Glossary; data semantics |
| Revisit trigger | Legal consent model change |

### D-015

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Version 1 excludes OCR and AI transcription. |
| Reason | Handwriting quality; keep product focused. |
| Alternatives | OCR-assisted entry. |
| Consequences | Manual transcription is the designed path. |
| Related files | Scope |
| Revisit trigger | Proven OCR quality for this form set |

### D-016

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | No application code is allowed before design freeze. |
| Reason | Prevent accidental source-of-truth drift. |
| Alternatives | Prototype-first. |
| Consequences | Documentation and contracts first. |
| Related files | Design-before-code protocol |
| Revisit trigger | Explicit emergency prototype authorization |

### D-017

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Dedicated GitHub repository is preferred. |
| Reason | Isolation and clear ownership. |
| Alternatives | Monorepo under SOSWebsite. |
| Consequences | Separate remote; no guessed URL in this build. |
| Related files | README; closeout |
| Revisit trigger | Org repository strategy change |

### D-018

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Dedicated Netlify deployment is preferred. |
| Reason | Isolated deploy, env, and rollback. |
| Alternatives | Shared RedDirt Netlify site. |
| Consequences | Separate site and secrets after implementation authorization. |
| Related files | Master plan deployment section |
| Revisit trigger | Hosting platform change |

### D-019

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Canonical people integration must be additive and least-privilege. |
| Reason | Protect RedDirt domain while sharing people. |
| Alternatives | Full shared admin DB role. |
| Consequences | Restricted credentials; additive migrations. |
| Related files | Scope; shared database protocol |
| Revisit trigger | Security review findings |

### D-020

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Raw transcription must never be discarded. |
| Reason | Audit evidence and correction integrity. |
| Alternatives | Store only normalized values. |
| Consequences | Raw + normalized fields; matching must not overwrite raw. |
| Related files | Glossary; data semantics |
| Revisit trigger | None expected |

---

## Open Non-Blocking Questions

These do not block governance foundation completion; they must be resolved during later design volumes:

1. Exact private storage provider choice (Supabase Storage vs S3-compatible vs other).
2. Preferred vs alternative canonical people integration model details against live RedDirt schema.
3. Final claim expiration minutes (30 recommended) and renewal events.
4. Exact auto-link criteria for EXACT matches.
5. Retention default (keep indefinitely vs timed deletion after verification).
