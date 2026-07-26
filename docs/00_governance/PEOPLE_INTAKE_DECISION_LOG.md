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

## Decisions Locked in PEOPLE-WORKFLOW-UX-DESIGN-1.0

### D-021

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Capture, transcription, and matching remain separate workspaces (plus Manage). |
| Reason | Different jobs, locations, and cognitive loads. |
| Alternatives | Single combined workspace. |
| Consequences | Role homes and navigation differ by workspace. |
| Related files | `PEOPLE_INTAKE_UX_ARCHITECTURE.md`, `PEOPLE_INTAKE_USER_ROLES.md` |
| Revisit trigger | Proven confusion in usability testing |

### D-022

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | A page is the queue work item; each page supports up to ten independent intake entries. |
| Reason | Hard-copy sheets contain multiple people; page-centric office work. |
| Alternatives | One person per image as queue unit. |
| Consequences | Claims, submit, and completion are page-level. |
| Related files | Transcription and queue workflow docs |
| Revisit trigger | Physical form capacity change |

### D-023

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Data entry completes the entire page before matching; matching does not interrupt typing. |
| Reason | Protect transcription speed. |
| Alternatives | Inline duplicate prompts per row. |
| Consequences | Post-submit matching queue. |
| Related files | `PEOPLE_INTAKE_MATCHING_WORKFLOW.md` |
| Revisit trigger | Strong operational need for inline exact-match only |

### D-024

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Mobile entry is one person at a time; tablet/desktop may use a ten-row grid. |
| Reason | Phone width cannot host eight fields across. |
| Alternatives | Same UI on all devices. |
| Consequences | Dual layout specs. |
| Related files | Mobile and tablet/desktop specs |
| Revisit trigger | None expected |

### D-025

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Standard worker action is Claim Next Page with atomic exclusive claims. |
| Reason | Parallel office work without collisions. |
| Alternatives | Manual-only page picking. |
| Consequences | Claim renewal, expiration, admin reassignment required. |
| Related files | `PEOPLE_INTAKE_QUEUE_AND_CLAIMING.md` |
| Revisit trigger | Single-operator deployment only |

### D-026

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Drafts autosave; claims expire after inactivity; drafts survive expiration. |
| Reason | Mobile interruption and weak signal are expected. |
| Alternatives | Manual save only; discard expired drafts. |
| Consequences | Local/offline draft behavior and conflict protection. |
| Related files | Transcription and queue docs |
| Revisit trigger | Exact TTL mechanics in later design |

### D-027

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Bad images move to an exception/image-review path; Unreadable and Not Provided remain separate; Volunteer/Email List use Yes, No, Blank. |
| Reason | Preserve evidence and avoid invented No answers. |
| Alternatives | Boolean-only fields; silent No for blank. |
| Consequences | Field-options UI and exception queues. |
| Related files | Form behavior; exception workflows |
| Revisit trigger | Legal consent model change |

### D-028

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Primary submission action is Submit Page & Open Next; Exact/Possible/No Match/Conflict are distinct; uncertain matching requires humans; UI language stays plain. |
| Reason | Fastest correct office loop with safe matching. |
| Alternatives | Always return to queue; auto-merge uncertain matches. |
| Consequences | Reviewer workspace and copy guide constraints. |
| Related files | Content guide; matching workflow |
| Revisit trigger | None for Version 1 |

---

## Decisions Locked in PEOPLE-ARCHITECTURE-AUDIT-AND-DESIGN-VALIDATION-1.0

### D-038

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Design freeze is DENIED; implementation remains unauthorized until Critical findings are cleared and Gate G-9 is re-issued APPROVED. |
| Reason | Audit found missing quality/ops package, unlocked auto-link/NO_MATCH policies, unaudited shared DB, and dual state vocabularies. |
| Alternatives | Freeze anyway and fix during coding. |
| Consequences | Next build is remediation + quality/ops; Step 5B orchestration waits for freeze. |
| Related files | Architecture findings; freeze report; risk register |
| Revisit trigger | Successful remediation re-audit |

---

## Open Non-Blocking Questions

See `reports/PEOPLE_OPEN_DECISIONS_REGISTER.md` for the authoritative blocking and non-blocking lists after the architecture audit. The prior deferred list is superseded by that register.

---

## Decisions Locked in PEOPLE-SECURITY-API-ENGINEERING-DESIGN-1.0

### D-034

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Auth required (approved users only, no public signup, individual accounts); authorization is server-side deny-by-default with role + record + state checks. |
| Reason | Browser is untrusted; prevent escalation and over-access. |
| Alternatives | Client role trusts; open signup. |
| Consequences | Approved-user registry; server session verification. |
| Related files | Auth architecture; authorization matrix |
| Revisit trigger | Provider compatibility audit |

### D-035

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Private images via temporary authorized access; sensitive writes only through server services; dedicated least-privilege DB credential separate from migration credential. |
| Reason | Prevent leakage and over-privileged runtime. |
| Alternatives | Public URLs; shared RedDirt admin DB role. |
| Consequences | Image access service; credential separation. |
| Related files | Authorization; secret management |
| Revisit trigger | None expected |

### D-036

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Versioned APIs with written contracts before implementation; explicit state transitions; claim/match concurrency protection; idempotency for duplicate-sensitive actions. |
| Reason | Safe multi-user operations and no silent duplicates. |
| Alternatives | Ad-hoc routes; last-write-wins. |
| Consequences | `/api/v1` inventory; registries for errors/transitions. |
| Related files | API contracts; idempotency and concurrency |
| Revisit trigger | Framework choice at freeze |

### D-037

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Canonical changes via controlled contract; no RedDirt imports or operational table writes; audit separate from logs; logs contain no raw PII/secrets; upload validation + quarantine; high-risk actions require audit success; durable idempotent jobs; promotion failure preserves resolution; no V1 unrestricted export; no silent production fallbacks. |
| Reason | Integrity, privacy, and cross-app isolation. |
| Alternatives | Direct canonical table writes; PII in logs; mock fallbacks in prod. |
| Consequences | Integration + background + error contracts; security tests. |
| Related files | Canonical integration; logging; configuration; threat model |
| Revisit trigger | Pre-migration audit findings |

---

## Decisions Locked in PEOPLE-DATA-MATCHING-STORAGE-DESIGN-1.0

### D-029

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Batch, Page, Intake Entry, and Canonical Person are separate entities; page is the queue work item with 0–10 uniquely identified entries. |
| Reason | Preserve page-centric operations and independent matching/provenance. |
| Alternatives | Flat person-per-image; blob of people per page. |
| Consequences | Distinct IDs, row numbers, and resolution per entry. |
| Related files | Domain model; ERD; field dictionary |
| Revisit trigger | Physical form capacity change |

### D-030

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Raw transcription is preserved separately from normalized values; field conditions include PROVIDED, NOT_PROVIDED, UNREADABLE, AMBIGUOUS, CORRECTED; Unknown consent never becomes No. |
| Reason | Evidence integrity and honest consent semantics. |
| Alternatives | Store only normalized; boolean-only consent. |
| Consequences | Correction history; preference history; UI Blank = UNKNOWN. |
| Related files | Field dictionary; provenance |
| Revisit trigger | Legal consent model change |

### D-031

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Matching is post-transcription, conservative, and explainable; shared household contacts cannot independently establish identity; canonical contacts support multiple attributes; merges are outside routine intake. |
| Reason | False duplicates are more dangerous than temporary duplicates. |
| Alternatives | Aggressive auto-merge; flat single-phone/email overwrite. |
| Consequences | Match candidates/resolutions; human review for uncertain cases. |
| Related files | Matching engine; canonical person contract |
| Revisit trigger | Approved exact-rule authorization changes |

### D-032

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | People Intake uses controlled promotion into the shared canonical people domain; intake owns intake tables; images use private object storage with original vs display separation and temporary authorized access. |
| Reason | Isolate risk from RedDirt while sharing people truth; keep images private. |
| Alternatives | Direct canonical table writes; Postgres blobs; public CDN. |
| Consequences | Promotion requests/results; signed URLs; compensation for storage/DB. |
| Related files | Canonical contract; image storage; database architecture |
| Revisit trigger | Pre-migration audit finding forcing Model A |

### D-033

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Every promoted canonical value requires provenance; audit and corrections are append-only; migrations must be additive and compatibility-audited; no schema is written until the shared database is inspected. |
| Reason | Traceability and safe coexistence with RedDirt. |
| Alternatives | Silent overwrites; assume conceptual tables exist. |
| Consequences | Pre-migration audit gate; no Prisma/SQL in this phase. |
| Related files | Provenance; migration and rollback |
| Revisit trigger | None expected before audit |

### D-039

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Master Cursor Build Orchestration (phases 0–12) and Volume 0 Project Constitution are the execution control plane once Gate G-10 opens; they do not authorize coding while design freeze is DENIED. |
| Reason | Reduce drift across long builds; keep a hard gate when Step 5B is written before freeze prerequisites are met. |
| Alternatives | Begin Phase 0 immediately after writing orchestration; skip Volume 0. |
| Consequences | Next build remains audit remediation; `applicationCodeAuthorized` stays false; Phase 0 slices stay BLOCKED in the implementation ledger. |
| Related files | `PEOPLE_INTAKE_CURSOR_BUILD_ORCHESTRATION.md`; `PEOPLE_INTAKE_PROJECT_CONSTITUTION.md`; `implementation-ledger.json` |
| Revisit trigger | Design freeze APPROVED |

### D-040

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Volume 0 — PEOPLE INTAKE PROJECT CONSTITUTION — is the highest-authority standing-orders document in the repository; Cursor must read it before every build session; it includes a Universal Engineering Constitution for the broader SOSWebsite ecosystem. |
| Reason | Prevent drift; give AI and humans one non-negotiable reference without repeating full design volumes. |
| Alternatives | Treat Volume 0 as optional summary; keep rules scattered across Steps 1–5B only. |
| Consequences | Source-of-truth hierarchy places Volume 0 first; conflicts with draft prose require Decision Log resolution; ecosystem apps are expected to inherit universal principles where applicable. |
| Related files | `PEOPLE_INTAKE_PROJECT_CONSTITUTION.md`; source-of-truth registry; Cursor execution protocol |
| Revisit trigger | Owner amends constitution sections |

### D-041

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Volume 0 is structured as Preamble + Articles (mission, universal engineering constitution, Cursor oath, amendments, People Intake doctrines) and the documentation set is renumbered as library Volumes 0–7 (Constitution through Master Cursor Build Orchestration). |
| Reason | Give every developer and AI the why behind the rules; make the design package read as one engineering manual with Constitution first. |
| Alternatives | Keep informal section numbering; keep folder-based volume labels (1–8) as the reading taxonomy. |
| Consequences | `documentation-index.json` uses library volumes 0–7; folder paths under `docs/` remain for link stability; `PEOPLE_INTAKE_DOCUMENTATION_LIBRARY.md` is the map. |
| Related files | Constitution v3; Documentation Library; documentation-index.json |
| Revisit trigger | Library volume added or renumbered |

### D-042

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Before production code, build an Implementation Library: Volumes 8–12 (tech/DB/API/UI/components), Engineering Catalogs, Implementation Packages, and Volume 13 Canonical Platform Standards; Cursor must not invent endpoints, tables, states, errors, events, or components absent from these specs. |
| Reason | Prevent architectural drift across hundreds of implementation slices; support a multi-year canonical people platform. |
| Alternatives | Start Phase 0 coding immediately after orchestration; specify only while coding. |
| Consequences | `applicationCodeAuthorized` remains false; next required build is still audit remediation + quality/ops freeze; coding uses IP packages referencing Volumes 8–13. |
| Related files | `docs/09_*` … `docs/16_*`; Documentation Library v2 |
| Revisit trigger | Gate G-10 opens |

### D-043

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Execute PEOPLE-IMPLEMENTATION-SPECIFICATION-LIBRARY-1.0 via sequenced DOC-0…DOC-12 scripts; DOC-0 establishes inventory and canonical volume pointers without silently rewriting Volumes 0–7; existing docs/00_*…docs/16_* paths remain equivalent content homes; bootstrap specs are DRAFT_BOOTSTRAP until formal DOC scripts pass. |
| Reason | Prevent duplicate/conflicting volumes and give Cursor a controlled documentation-production sequence. |
| Alternatives | Mass-migrate all docs into docs/volumes/; treat bootstrap as final Vol 8–13. |
| Consequences | Next script is DOC-1 (Volume 8 formal); production code remains prohibited; weighted docs progress starts at 5%. |
| Related files | DOC-0 artifacts under data/documentation, docs/volumes, develop_notes |
| Revisit trigger | DOC-12 specification freeze |
