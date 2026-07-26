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

### D-044

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Volume 8 — PEOPLE-VOLUME-08-TECHNICAL-DOMAIN-SPECIFICATIONS-1.0 — is the implementation-governing technical domain specification. Canonical path is `docs/volumes/volume-08-technical-specifications/VOLUME_08_TECHNICAL_DOMAIN_SPECIFICATIONS.md`. Global invariants `PEOPLE-INV-001`…`015`, domain `*-RULE-*` / `*-INV-*` identifiers, forty locked domain decisions, and E2E scenarios A–H in that document are authoritative for domain behavior. Volume 8 does not authorize production code, tables, or API routes. |
| Reason | Convert approved architecture into precise domain operating rules before Volume 9 database design. |
| Alternatives | Keep only bootstrap TECH_SPEC drafts; invent rules during coding. |
| Consequences | Next build is Volume 9 Database Specifications (documented model only — no migrations). OD-B* items aligned with Volume 8 locks remain subject to Owner Decision Log acceptance where still marked provisional in audit registers. Gate G-10 remains closed. |
| Related files | Volume 8 master; `data/documentation/volume_08_domain_registry.json`; `data/documentation/volume_08_rule_registry.json`; `scripts/documentation/validate-volume-08.mjs` |
| Revisit trigger | Formal amendment to Volume 8 locked decisions |

### D-045

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Volume 9 — PEOPLE-VOLUME-09-DATABASE-SPECIFICATIONS-1.0 — is the implementation-governing database blueprint. Canonical path is `docs/volumes/volume-09-database-specifications/VOLUME_09_DATABASE_SPECIFICATIONS.md`. Table registry, `DB-PRINCIPLE-001`…`010`, locked database decisions 1–40, and deferred `DB-DEC-001`…`015` in that document are authoritative for data design. Volume 9 prohibits SQL migrations, Prisma/ORM schemas, provisioning, live DB connections, and schema deployment during this documentation build. |
| Reason | Freeze what data must exist, how records relate, what remains append-only, and how concurrency/provenance/canonical boundaries are protected before API and implementation work. |
| Alternatives | Keep only bootstrap TABLE_*.md drafts; invent schema during coding. |
| Consequences | Next build is Volume 10 API Specifications (contracts only — no handlers). Bootstrap `docs/10_database_specifications/TABLE_*.md` remain DRAFT until reconciled. Gate G-10 remains closed; `migrationsAuthorized` remains false. |
| Related files | Volume 9 master; `data/documentation/volume_09_table_registry.json`; `scripts/documentation/validate-volume-09.mjs` |
| Revisit trigger | Formal amendment to Volume 9 locked database decisions |

### D-046

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Volume 10 — PEOPLE-VOLUME-10-API-SPECIFICATIONS-1.0 — is the canonical API contract. Canonical path is `docs/volumes/volume-10-api-specifications/VOLUME_10_API_SPECIFICATIONS.md`. Prefix `/api/v1/`, endpoint inventory, envelopes, error codes, idempotency/concurrency rules, and locked API decisions in that document are authoritative. Volume 10 prohibits route handlers, framework/controller code, ORM/SQL, SDKs, and production deployment during this documentation build. |
| Reason | Freeze UI↔backend↔integration contracts before any production handlers are written, enforcing Volumes 8–9 without inventing endpoints during coding. |
| Alternatives | Keep only bootstrap API_*.md drafts; invent endpoints during implementation. |
| Consequences | Next build is Volume 11 UI Specifications (docs only — no React). Bootstrap `docs/11_api_specifications/API_*.md` remain DRAFT until reconciled. Gate G-10 remains closed; `applicationCodeAuthorized` remains false. |
| Related files | Volume 10 master; `data/documentation/volume_10_endpoint_registry.json`; `scripts/documentation/validate-volume-10.mjs` |
| Revisit trigger | Formal amendment to Volume 10 locked API decisions |

### D-047

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Volume 11 — PEOPLE-VOLUME-11-USER-INTERFACE-SPECIFICATIONS-1.0 — is the canonical UX and screen specification. Canonical path is `docs/volumes/volume-11-ui-specifications/VOLUME_11_USER_INTERFACE_SPECIFICATIONS.md`. Four workspaces (Capture, Transcribe, Match, Manage), screen inventory, locked UX decisions 1–40, and deferred `UI-DEC-001`…`018` in that document are authoritative. Volume 11 prohibits React, route files, CSS, design-system code, API/auth/DB integration, and framework selection during this documentation build. |
| Reason | Freeze what users must see and do before inventing layouts during coding; enforce Unknown-not-No, autosave, claim visibility, and accuracy-first UX. |
| Alternatives | Keep only bootstrap UI_*.md drafts; invent screens during implementation. |
| Consequences | Next build is Volume 12 Component Library and Design System (docs only — no component code). Bootstrap `docs/12_ui_specifications/UI_*.md` remain DRAFT until reconciled. Gate G-10 remains closed. |
| Related files | Volume 11 master; `data/documentation/volume_11_screen_registry.json`; `scripts/documentation/validate-volume-11.mjs` |
| Revisit trigger | Formal amendment to Volume 11 locked UX decisions |

### D-048

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Volume 12 — PEOPLE-VOLUME-12-COMPONENT-LIBRARY-AND-DESIGN-SYSTEM-1.0 — is the canonical component library and visual design system specification. Canonical path is `docs/volumes/volume-12-component-library/VOLUME_12_COMPONENT_LIBRARY_AND_DESIGN_SYSTEM.md`. Design principles, token architecture, color/typography/spacing/motion roles, component inventory, accessibility/privacy contracts, locked decisions 1–50, and deferred `COMP-DEC-001`…`025` in that document are authoritative. Volume 12 prohibits React/JSX/TSX, CSS files, design-token packages, Storybook, font/icon installation, framework selection, routes, API calls, and dependency installation during this documentation build. |
| Reason | Freeze reusable interface building blocks and visual contracts before inventing one-off UI during coding; enforce semantic tokens, WCAG 2.2 AA, PreferenceControl Yes/No/Unknown, and calm claim/save recovery patterns. |
| Alternatives | Keep only bootstrap CMP_*.md drafts; invent components during implementation. |
| Consequences | Next build is Volume 13 Canonical Platform Standards (docs only — no application code). Bootstrap `docs/13_component_library/CMP_*.md` remain DRAFT until reconciled. Gate G-10 remains closed; `applicationCodeAuthorized` remains false. |
| Related files | Volume 12 master; `data/documentation/volume_12_component_registry.json`; `scripts/documentation/validate-volume-12.mjs` |
| Revisit trigger | Formal amendment to Volume 12 locked component decisions |

### D-049

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Volume 13 — PEOPLE-VOLUME-13-CANONICAL-PLATFORM-STANDARDS-1.0 — is the canonical engineering standard for People Intake. Canonical path is `docs/volumes/volume-13-platform-standards/VOLUME_13_CANONICAL_PLATFORM_STANDARDS.md`. Repository, configuration, architecture layering, authn/authz, data protection, database/API/UI discipline, testing, deployment, observability, documentation synchronization, implementation-package governance, and the eighteen locked engineering decisions in that document are authoritative. Volume 13 prohibits application source, handlers, migrations, React/CSS implementation, runtime dependency installation for the app, production deployment, and secrets in source control during this documentation build. |
| Reason | Unify Volumes 0–12 into one engineering doctrine so Cursor and contributors cannot improvise project structure, security boundaries, or integration patterns during later implementation. |
| Alternatives | Keep only bootstrap PLATFORM_STANDARDS.md; invent engineering conventions during coding. |
| Consequences | Next build is PEOPLE-STATE-MACHINE-CATALOG-1.0, followed by Error, Audit Event, Configuration catalogs, Cross-Volume Traceability Matrix, and Implementation Package Library — all documentation only. Bootstrap `docs/15_platform_standards/PLATFORM_STANDARDS.md` remains DRAFT until reconciled. Gate G-10 remains closed; `applicationCodeAuthorized` remains false. |
| Related files | Volume 13 master; `data/documentation/volume_13_platform_registry.json`; `scripts/documentation/validate-volume-13.mjs` |
| Revisit trigger | Formal amendment to Volume 13 locked engineering decisions |

### D-050

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | Document set PEOPLE-CATALOG-LIBRARY-1.0 is authoritative for the catalog sequence. PEOPLE-CATALOG-00-MASTER-REGISTRY-1.0 (`docs/catalogs/catalog-00-master-registry/CATALOG_00_MASTER_REGISTRY.md`) defines the required catalog inventory (0–9), identifier/versioning/amendment rules, and the canonical-value rule. PEOPLE-CATALOG-01-STATE-MACHINES-1.0 (`docs/catalogs/catalog-01-state-machines/CATALOG_01_STATE_MACHINES.md`) defines twenty-three controlled lifecycles, transitions/guards/side effects, twenty-two locked state decisions, and deferred `STATE-DEC-001`…`010`. Catalog builds prohibit application code and undocumented production state/error/permission/audit/config/job values. Prior informal ID PEOPLE-STATE-MACHINE-CATALOG-1.0 is superseded by PEOPLE-CATALOG-01-STATE-MACHINES-1.0. |
| Reason | Convert Volumes 0–13 into exact operational values so implementation cannot invent states, transitions, or related controlled vocabularies. |
| Alternatives | Keep only bootstrap STATE_MACHINE_CATALOG.md; invent enums during coding. |
| Consequences | Next build is PEOPLE-CATALOG-02-ERRORS-1.0, then Audit Events, Configuration, Permissions, Notifications, Background Jobs, Data Retention, and Traceability — all documentation only. Gate G-10 remains closed; `applicationCodeAuthorized` remains false. |
| Related files | Catalog 0/1 masters; `data/documentation/catalog_00_master_registry.json`; `data/documentation/catalog_01_state_machine_registry.json`; `scripts/documentation/validate-catalog-library.mjs` |
| Revisit trigger | Formal amendment to Catalog 0 inventory or Catalog 1 locked state decisions |

### D-051

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | PEOPLE-CATALOG-02-ERRORS-1.0 is the canonical Error Catalog. Path: `docs/catalogs/catalog-02-errors/CATALOG_02_ERRORS.md`. It defines ten error principles, the standard API error envelope, severity/HTTP mapping, 154 cataloged error entries and canonical codes, preservation/retry/alert/audit/logging rules, thirty locked error decisions, and deferred `ERROR-DEC-001`…`012`. Production implementations may not invent error codes outside this catalog. Catalog 2 prohibits error classes, handlers, logging/alerting implementation, migrations, middleware, UI, retry workers, and dependency installation during this documentation build. |
| Reason | Freeze stable failure language so APIs, UI, workers, and operators communicate failures safely and consistently without inventing codes or leaking internals. |
| Alternatives | Keep only bootstrap ERROR_CATALOG.md; invent error codes during coding. |
| Consequences | Next build is PEOPLE-CATALOG-03-AUDIT-EVENTS-1.0. Gate G-10 remains closed; `applicationCodeAuthorized` remains false. |
| Related files | Catalog 2 master; `data/documentation/catalog_02_error_registry.json`; `scripts/documentation/validate-catalog-library.mjs` |
| Revisit trigger | Formal amendment to Catalog 2 locked error decisions |

### D-052

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | PEOPLE-CATALOG-03-AUDIT-EVENTS-1.0 is the canonical Audit Event Catalog foundation. Path: `docs/catalogs/catalog-03-audit-events/CATALOG_03_AUDIT_EVENTS.md`. It defines ten audit principles, the standard event contract, naming, 22 domains, the event template, privacy/correlation/retention hooks, testing and traceability rules, fifteen locked decisions, and six seeded example events (`AUDIT-USER-001`, `AUDIT-CLAIM-001`, `AUDIT-PAGE-001`, `AUDIT-MATCH-001`, `AUDIT-PROMOTION-001`, `AUDIT-SECURITY-001`). Scope is foundation-with-seeded-events; additional event entries require formal catalog amendment under this contract and must not invent undocumented production event names. Catalog 3 prohibits audit persistence, migrations, handlers, logging/alerting implementation, UI, and dependency installation during this documentation build. |
| Reason | Freeze the immutable audit language and contract so implementation cannot invent event shapes, leak secrets into audit payloads, or treat audit as business logic—without falsely claiming a fully enumerated hundreds-of-events inventory. |
| Alternatives | Invent a complete event list without owner review; keep only bootstrap EVENT_CATALOG.md. |
| Consequences | Next build is PEOPLE-CATALOG-04-CONFIGURATION-1.0. Full audit event inventory may expand via amendment. Gate G-10 remains closed; `applicationCodeAuthorized` remains false. |
| Related files | Catalog 3 master; `data/documentation/catalog_03_audit_event_registry.json`; `scripts/documentation/validate-catalog-library.mjs` |
| Revisit trigger | Formal amendment expanding seeded events or changing Catalog 3 locked decisions |

### D-053

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | PEOPLE-CATALOG-04-CONFIGURATION-1.0 is the canonical Configuration Catalog foundation. Path: `docs/catalogs/catalog-04-configuration/CATALOG_04_CONFIGURATION.md`. It defines ten configuration principles, the entry standard, 24 categories, environment scopes, data types, secret classification, startup validation and change-management rules, fifteen locked decisions, fifty-nine seeded configuration keys (`CONFIG-APP-*` through `CONFIG-EXPORT-*`), and four feature-flag examples. Scope is foundation-with-seeded-keys; exact production values and additional keys require formal catalog amendment under this contract and must not invent undocumented production configuration keys. Catalog 4 prohibits application source code, production secret env files, dependency installation, deployment configuration implementation, and feature-flag runtime wiring during this documentation build. |
| Reason | Freeze the authoritative configuration language so deployments remain predictable and no configurable value is hidden in code—without inventing exact production secrets or a complete env inventory ahead of environment design. |
| Alternatives | Keep only bootstrap CONFIGURATION_CATALOG.md; invent env keys during coding. |
| Consequences | Next build is PEOPLE-CATALOG-05-PERMISSIONS-1.0. Exact values and additional keys may expand via amendment. Gate G-10 remains closed; `applicationCodeAuthorized` remains false. |
| Related files | Catalog 4 master; `data/documentation/catalog_04_configuration_registry.json`; `scripts/documentation/validate-catalog-library.mjs` |
| Revisit trigger | Formal amendment expanding seeded keys or changing Catalog 4 locked decisions |

### D-054

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | PEOPLE-CATALOG-05-PERMISSIONS-1.0 is the canonical Permissions and Authorization Catalog foundation. Path: `docs/catalogs/catalog-05-permissions/CATALOG_05_PERMISSIONS.md`. It defines ten authorization principles, seven Version 1 roles (`Owner`, `Administrator`, `Reviewer`, `Data Entry`, `Uploader`, `Viewer`, `System`), eighteen resource types, sixteen actions, five resource scopes, eighteen seeded permission keys, three separation-of-duties rules, evaluation order, override/emergency/delegation constraints, audit and test requirements, and fifteen locked decisions. Scope is foundation-with-seeded-permissions; additional permission keys and matrix grants require formal catalog amendment under this contract and must not invent undocumented production roles or permission keys. Catalog 5 prohibits application source code, authz middleware, RLS/migrations, role-assignment UI/handlers, and dependency installation during this documentation build. |
| Reason | Freeze the server-enforced authorization model so UI cannot grant authority, SoD and Owner protections are explicit, and implementation cannot invent roles or permission keys outside the catalog. |
| Alternatives | Keep only draft authorization matrix prose; invent roles/permissions during coding. |
| Consequences | Next build is PEOPLE-CATALOG-06-NOTIFICATIONS-1.0. Full permission inventory may expand via amendment. Gate G-10 remains closed; `applicationCodeAuthorized` remains false. |
| Related files | Catalog 5 master; `data/documentation/catalog_05_permissions_registry.json`; `scripts/documentation/validate-catalog-library.mjs` |
| Revisit trigger | Formal amendment expanding seeded permissions or changing Catalog 5 locked decisions |

### D-055

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | PEOPLE-CATALOG-06-NOTIFICATIONS-1.0 is the canonical Notification Catalog foundation. Path: `docs/catalogs/catalog-06-notifications/CATALOG_06_NOTIFICATIONS.md`. It defines ten notification principles, delivery channels (IN_APP/EMAIL enabled; SMS/PUSH/WEBHOOK future), four priorities, six recipient types, four expiration behaviors, the entry template, deduplication/acknowledgment/privacy/accessibility/escalation rules, fifteen locked decisions, and nine seeded notifications (`WORK_AVAILABLE`, `CLAIM_EXPIRING`, `CLAIM_EXPIRED`, `DRAFT_RECOVERABLE`, `TRANSCRIPTION_RETURNED`, `MATCH_REQUIRES_REVIEW`, `PROMOTION_FAILED`, `SYSTEM_CONFIGURATION_CHANGED`, `SECURITY_EVENT`). Scope is foundation-with-seeded-notifications; additional notification types require formal catalog amendment under this contract and must not invent undocumented production notification names. Catalog 6 prohibits application source code, delivery implementation, notification workers/UI, and dependency installation during this documentation build. |
| Reason | Freeze the notification language and privacy/recipient rules so implementation cannot spam users, leak unauthorized detail, or invent notification types—without falsely claiming a complete operational notification inventory. |
| Alternatives | Invent a complete notification list without owner review; implement ad hoc toasts during coding. |
| Consequences | Next build is PEOPLE-CATALOG-07-BACKGROUND-JOBS-1.0. Full notification inventory may expand via amendment. Gate G-10 remains closed; `applicationCodeAuthorized` remains false. |
| Related files | Catalog 6 master; `data/documentation/catalog_06_notifications_registry.json`; `scripts/documentation/validate-catalog-library.mjs` |
| Revisit trigger | Formal amendment expanding seeded notifications or changing Catalog 6 locked decisions |

### D-056

| Field | Value |
| --- | --- |
| Date | 2026-07-25 |
| Status | accepted |
| Decision | PEOPLE-CATALOG-07-BACKGROUND-JOBS-1.0 is the canonical Background Job Catalog foundation. Path: `docs/catalogs/catalog-07-background-jobs/CATALOG_07_BACKGROUND_JOBS.md`. It defines ten job principles, seventeen Version 1 categories, job template, seven trigger types, four priorities, five concurrency policies, five retry classes, idempotency rules, failure/monitoring/audit/security/test requirements, fifteen locked decisions, and thirteen seeded jobs (`UPLOAD_VERIFICATION` through `SYSTEM_HEALTH_CHECK`, including `PROMOTION_EXECUTION`). Scope is foundation-with-seeded-jobs; additional job types require formal catalog amendment under this contract and must not invent undocumented production job names. Catalog 7 prohibits application source code, workers/schedulers, job-table migrations, cron/Netlify schedule wiring, and dependency installation during this documentation build. |
| Reason | Freeze the asynchronous execution architecture so implementation cannot invent hidden workers, skip idempotency for canonical mutations, or silently drop failures—without falsely claiming a complete hundreds-of-jobs inventory. |
| Alternatives | Invent a complete job list without owner review; implement ad hoc workers during coding. |
| Consequences | Next build is PEOPLE-CATALOG-08-DATA-RETENTION-1.0. Full job inventory may expand via amendment. Gate G-10 remains closed; `applicationCodeAuthorized` remains false. |
| Related files | Catalog 7 master; `data/documentation/catalog_07_background_jobs_registry.json`; `scripts/documentation/validate-catalog-library.mjs` |
| Revisit trigger | Formal amendment expanding seeded jobs or changing Catalog 7 locked decisions |

### D-057

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | PEOPLE-CATALOG-08-DATA-RETENTION-1.0 is the canonical Data Classification and Retention Catalog foundation. Path: `docs/catalogs/catalog-08-data-retention/CATALOG_08_DATA_RETENTION.md`. It defines ten retention principles, five classification levels (`PUBLIC`, `INTERNAL`, `CONFIDENTIAL`, `RESTRICTED`, `SYSTEM_SECRET`), twenty-two domains, five lifecycle states (`ACTIVE`, `ARCHIVED`, `LEGAL_HOLD`, `PENDING_DESTRUCTION`, `DESTROYED`), archival/legal-hold/destruction/recovery/privacy/audit/monitoring/governance rules, fifteen locked decisions, and four seeded retention examples (`RETAIN-AUDIT-001`, `RETAIN-DRAFT-001`, `RETAIN-IMAGE-001`, `RETAIN-SECRET-001`). Scope is foundation-with-seeded-retention-rules; additional rules and exact durations require formal catalog amendment under this contract and must not invent undocumented production classification levels or retention rules. Catalog 8 prohibits application source code, archival/destruction workers, retention-table migrations, production data deletion, and dependency installation during this documentation build. |
| Reason | Freeze the data-lifecycle language so no persistent data exists without classification and retention governance—without inventing complete regulatory mappings or every per-field duration in one pass. |
| Alternatives | Invent a complete retention schedule without owner review; implement ad hoc deletion during coding. |
| Consequences | Next build is PEOPLE-CATALOG-09-TRACEABILITY-1.0 (locked Catalog 0 sequence; not an API contract catalog). Full retention inventory and exact durations may expand via amendment. Gate G-10 remains closed; `applicationCodeAuthorized` remains false. |
| Related files | Catalog 8 master; `data/documentation/catalog_08_data_retention_registry.json`; `scripts/documentation/validate-catalog-library.mjs` |
| Revisit trigger | Formal amendment expanding seeded retention rules or changing Catalog 8 locked decisions |

### D-058

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | PEOPLE-IMPLEMENTATION-MASTER-1.0 is the canonical Implementation Specification series master (foundation). Path: `docs/implementation-specifications/PEOPLE_IMPLEMENTATION_MASTER.md`. It defines a separate IS-* documentation series (not Catalog 10+), ten principles, fifty-five inventoried IS document IDs across Phases 0–10, traceability rules, recommended build order, small-package preference, and fifteen locked decisions. Volumes 8–13 remain canonical for already-authored domain specs; Catalogs remain sole authority for cataloged operational language; PKG-* units remain the executable packaging surface and stay BLOCKED until Gate G-10. Individual IS documents are not fully authored in this master. |
| Reason | Convert governance into a buildable specification series without inventing Catalog IDs beyond the locked 0–9 library, and without treating design authorship as coding authorization. |
| Alternatives | Extend Catalogs to 10–13; begin coding from volumes without an IS master; write monolithic implementation docs. |
| Consequences | Next Catalog Library build remains PEOPLE-CATALOG-09-TRACEABILITY-1.0. IS authorship may proceed as documentation-only drafts under this master. `applicationCodeAuthorized` remains false; Gate G-10 remains closed. |
| Related files | `docs/implementation-specifications/PEOPLE_IMPLEMENTATION_MASTER.md`; `docs/16_implementation_packages/PACKAGE_INDEX.md` |
| Revisit trigger | Formal amendment expanding IS inventory or changing Implementation Master locked decisions |

### D-059

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | PEOPLE-IMPLEMENTATION-SPECIFICATION-PROGRAM-1.0 is the canonical Implementation Specification Program Design. Path: `docs/implementation_specs/PEOPLE_IMPLEMENTATION_SPECIFICATION_PROGRAM.md`. It authorizes a documentation-only translation program with PEOPLE-IS-* document family, fourteen phases, mandatory template/traceability/readiness rules, H-drive boundary, and explicit Gate G-10 separation. Phase 0 documents PEOPLE-IS-000 through PEOPLE-IS-005 are STRUCTURALLY COMPLETE under `docs/implementation_specs/000_program/`. Catalog Library remains locked at 0–9; draft Catalogs 10–13 are not created—their concerns map into IS phases and existing Volumes. PEOPLE-IMPLEMENTATION-MASTER-1.0 is superseded as program authority but retained historically. Application implementation remains NOT AUTHORIZED. |
| Reason | Convert governance into build-ready engineering specifications without inventing Catalog IDs beyond 0–9 and without authorizing code. |
| Alternatives | Extend Catalogs to 13; begin coding from volumes; keep only the thinner IS Master inventory. |
| Consequences | Next catalog remains PEOPLE-CATALOG-09-TRACEABILITY-1.0. Next IS package is PEOPLE-IS-100-REPOSITORY-ARCHITECTURE-1.0. ADR-001…020 remain open and block coding. Gate G-10 remains closed. |
| Related files | `docs/implementation_specs/`; Phase 0 IS-000…005; `decisions/DECISION_REGISTER.md` |
| Revisit trigger | Formal amendment to Program Design locked decisions or Phase 0 gates |

### D-060

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | PEOPLE-IS-PHASE-0-GOVERNANCE-1.0 is complete. PEOPLE-IS-000 through PEOPLE-IS-005 are APPROVED as the Implementation Specification Program documentation governance foundation under `docs/implementation_specs/000_program/`. Support artifacts are canonical: README, `_index.md`, `templates/IMPLEMENTATION_SPECIFICATION_TEMPLATE.md`, `matrices/REQUIREMENT_TRACEABILITY_MATRIX.md` (REQ-GOV-001…010 VERIFIED), `decisions/DECISION_REGISTER.md` (DECISION-GOV-001…009 + ADR-001…020 queue), `decisions/OPEN_ISSUE_REGISTER.md` (nine Phase 0 issues), `reports/IMPLEMENTATION_SPECIFICATION_PROGRESS.md`, and `reports/PHASE_0_COMPLETION_REPORT.md`. Documentation approval does not authorize application implementation. |
| Reason | Close Phase 0 at the documentation level with objective readiness evidence, stable IDs, visible blocking issues, and separate implementation authorization. |
| Alternatives | Leave Phase 0 as STRUCTURALLY COMPLETE only; authorize coding; invent Catalogs 10–13. |
| Consequences | Next catalog remains PEOPLE-CATALOG-09-TRACEABILITY-1.0. Next IS document is PEOPLE-IS-100-REPOSITORY-ARCHITECTURE-1.0. ADR-001…020 and ISSUE-* entries remain open and continue to block coding/implementation readiness. Gate G-10 remains closed; `applicationCodeAuthorized` remains false. |
| Related files | `docs/implementation_specs/000_program/`; `docs/implementation_specs/reports/PHASE_0_COMPLETION_REPORT.md`; open-issue and decision registers |
| Revisit trigger | Formal amendment to Phase 0 locked decisions or readiness gates |

### D-061

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | PEOPLE-IS-100-REPOSITORY-ARCHITECTURE-1.0 is the canonical Repository Architecture specification. Path: `docs/implementation_specs/100_platform/PEOPLE-IS-100-REPOSITORY-ARCHITECTURE.md`. It defines the exclusive root `H:\people`, top-level directory ownership, documentation vs implementation separation, logical source layers and dependency direction, homes for contracts/database/tests/scripts/deployment/generated/local/tmp/logs, GitHub and Netlify boundaries, H-drive enforcement requirements, REQ-REPO-001…016, and acceptance criteria AC-REPO-001…010. `START_HERE.md` is established as the orientation entry. Documentation approval does not authorize creating `src`, `app`, migrations, workflows, Netlify config, repository guard code, package installs, or deployments. Catalog references remain locked at Catalogs 0–9; former “Catalog 10–13” concerns map to Volumes / IS phases. |
| Reason | Make correct repository placement and dependency direction easier than incorrect behavior before technology ADRs and coding begin. |
| Alternatives | Scaffold application directories now; select framework inside IS-100; invent Catalogs 10–13 as governing catalogs. |
| Consequences | Next IS document is PEOPLE-IS-101-TECHNOLOGY-DECISION-SPECIFICATION-1.0. Next catalog remains PEOPLE-CATALOG-09-TRACEABILITY-1.0. ADR-001…003,006,009,011,020 and ISSUE-HDRIVE-001 remain open and block implementation readiness. Gate G-10 remains closed; `applicationCodeAuthorized` remains false. |
| Related files | `docs/implementation_specs/100_platform/PEOPLE-IS-100-REPOSITORY-ARCHITECTURE.md`; `START_HERE.md`; RTM REQ-REPO-* rows |
| Revisit trigger | Formal amendment to repository ownership, dependency rules, or H-drive boundary |

### D-062

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | PEOPLE-CATALOG-09-TRACEABILITY-1.0 is the canonical Cross-Volume Traceability Matrix foundation. Path: `docs/catalogs/catalog-09-traceability/CATALOG_09_TRACEABILITY.md`. It defines ten principles, the Catalog 0 and IS-003-aligned linkage chains, required matrix fields, status vocabulary, orphan rules, ten seeded TRACE-SEED rows, and fifteen locked decisions. Scope is foundation-with-seeded-matrix-rows; full cross-volume inventory expands via formal amendment under this contract and PEOPLE-IS authorship. Catalog Library 0–9 is marked `PEOPLE-CATALOG-LIBRARY-COMPLETE`. Application implementation remains NOT AUTHORIZED. |
| Reason | Close the locked Catalog Library with an honest, bidirectional linkage contract so IS-101 technology decisions can map to requirements, ADRs, risks, tests, and packages without inventing undocumented catalog keys. |
| Alternatives | Invent a complete production matrix now; leave Catalog 09 PLANNED indefinitely; invent Catalogs 10–13. |
| Consequences | Next recommended build is PEOPLE-IS-101-TECHNOLOGY-DECISION-SPECIFICATION-1.0. Parallel freeze remediation remains required. Gate G-10 remains closed; `applicationCodeAuthorized` remains false. Full matrix inventory remains amendment-driven. |
| Related files | Catalog 9 master; `data/documentation/catalog_09_traceability_registry.json`; `scripts/documentation/validate-catalog-library.mjs`; Catalog 0 inventory update |
| Revisit trigger | Formal amendment expanding seeded TRACE-SEED rows or changing Catalog 9 locked decisions |

### D-063

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | PEOPLE-IS-101-TECHNOLOGY-DECISION-SPECIFICATION-1.0 is the canonical Technology Decision Specification. Path: `docs/implementation_specs/100_platform/PEOPLE-IS-101-TECHNOLOGY-DECISION-SPECIFICATION.md`. It records decision criteria, alternatives, recommendations, trade-offs, risks, H-drive notes, and ADR mappings for ADR-001 through ADR-020. Recommendations are PROPOSED design alignment (Next.js/React/TypeScript, hosted PostgreSQL, Prisma-behind-adapters, Supabase Auth provider with unresolved auth method, private object storage adapter, dedicated Netlify hosting per D-018, etc.) and do **not** constitute Decision Log acceptance of individual ADRs. Auth-method and storage-provider contradictions remain explicit open issues. ADR index: `docs/adr/_index.md`. Application implementation remains NOT AUTHORIZED. |
| Reason | Enable later implementation packages to cite evaluated technology choices without treating Constitution “as designed” language or Catalog 4 seeds as closed ADRs, and without authorizing coding. |
| Alternatives | Silently accept all ADRs now; pick vendors without recording contradictions; defer IS-101 until freeze. |
| Consequences | Next IS document is PEOPLE-IS-102-MODULE-BOUNDARY-SPECIFICATION-1.0. ADR-001…020 remain OPEN until individually accepted. Gate G-10 remains closed; `applicationCodeAuthorized` remains false. Priority ADR acceptances may proceed as documentation-only Decision Log work. |
| Related files | PEOPLE-IS-101; `docs/adr/_index.md`; `docs/implementation_specs/reports/PEOPLE_IS_101_COMPLETION_REPORT.md` |
| Revisit trigger | Decision Log acceptance or rejection of any ADR-001…020; amendment of recommended stack |

### D-064

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | PEOPLE-IS-102-MODULE-BOUNDARY-SPECIFICATION-1.0 is the canonical Module Boundary Specification and architectural rulebook for future implementation packages. Path: `docs/implementation_specs/100_platform/PEOPLE-IS-102-MODULE-BOUNDARY-SPECIFICATION.md`. Companion matrices: module dependency, ownership, boundary validation rules, and interface contract index under `docs/implementation_specs/matrices/`. It defines layer and capability module inventory, public vs internal surfaces, allowed/forbidden dependencies, ownership of entities/APIs/jobs/permissions/validation/audit/notifications/errors/tests, event rules, versioning, extensibility, anti-patterns, and a feature placement algorithm for implementation. Application implementation remains NOT AUTHORIZED. |
| Reason | Make module ownership and dependency legality determinable before coding so Burt never guesses where functionality belongs. |
| Alternatives | Defer boundaries until first code package; allow ad hoc module creation; encode boundaries only in framework folders. |
| Consequences | Next IS document is PEOPLE-IS-103-ENVIRONMENT-ARCHITECTURE-1.0. Implementation packages must cite IS-102 matrices. ISSUE-MOD-001/002 remain open for entries split and reports read models. Gate G-10 remains closed; ADR-001…020 remain OPEN. |
| Related files | PEOPLE-IS-102; module matrices; `reports/PEOPLE_IS_102_COMPLETION_REPORT.md` |
| Revisit trigger | New capability module; new ALLOW dependency edge; ownership conflict resolution |

### D-065

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | PEOPLE-PROTOCOL-COMMIT-PUSH-DEPLOY-1.0 is the standing closeout protocol for every completed, validated Burt interaction. Path: `docs/00_governance/PEOPLE_PROTOCOL_COMMIT_PUSH_DEPLOY.md`. It requires validate → indexes/registers/RTM → completion report → commit → push → remote verification → Netlify deploy only when an authorized deployable surface exists. Documentation-first does not waive repository discipline. Application code remains unauthorized and must not be invented to force Netlify deploys. Cursor Execution Protocol §9.3.1 incorporates this standing order. |
| Reason | Correct operating drift that treated documentation slices as complete without GitHub remote evidence. |
| Alternatives | Local-only documentation; defer Git until implementation; force Netlify via unauthorized app scaffolding. |
| Consequences | Every future slice must report commit hash, branch, push, remote verification, and Netlify applicability. Current repo without authorized deployable surface reports Netlify NOT APPLICABLE. |
| Related files | `PEOPLE_PROTOCOL_COMMIT_PUSH_DEPLOY.md`; `PEOPLE_INTAKE_CURSOR_EXECUTION_PROTOCOL.md` |
| Revisit trigger | Authorization of a deployable Netlify docs/app surface (IS-105 or package) |

### D-066

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | PEOPLE-IS-103-ENVIRONMENT-ARCHITECTURE-1.0 is the canonical Environment Architecture specification. Path: `docs/implementation_specs/100_platform/PEOPLE-IS-103-ENVIRONMENT-ARCHITECTURE.md`. It defines Local/Preview/Staging/Production separation, secret vs config-name rules, forbidden silent production defaults, H-drive local env rules, Netlify env boundaries, and REQ-ENV-001…012. No secret values are recorded. Application implementation and live environment provisioning remain NOT AUTHORIZED. |
| Reason | Establish environment isolation before hosting wiring (IS-105) and before any runtime config loaders. |
| Alternatives | Defer environments until Netlify wiring; embed secrets in docs; collapse Preview into Production. |
| Consequences | Next IS document is PEOPLE-IS-104-H-DRIVE-WORKSPACE-PROTOCOL-1.0. Provider-specific env var brands finalize with ADR acceptance. Gate G-10 remains closed. |
| Related files | PEOPLE-IS-103; `reports/PEOPLE_IS_103_COMPLETION_REPORT.md` |
| Revisit trigger | ADR acceptance changing env var brands; IS-105 staging topology decision |

### D-067

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | PEOPLE-IS-104-H-DRIVE-WORKSPACE-PROTOCOL-1.0 is the canonical H-Drive Workspace Protocol for every build machine. Path: `docs/implementation_specs/100_platform/PEOPLE-IS-104-H-DRIVE-WORKSPACE-PROTOCOL.md`. It defines canonical root `H:\people`, directory conventions, allowed/prohibited writes, session environment variables, package-manager cache and temp strategies, Git/Cursor expectations, Node/future Prisma/tooling redirection policy, validation via `drive:validate`, failure/recovery, and exception handling. It preserves the honest limitation that only project-controlled and project-configurable artifacts are enforceable; OS/third-party writes to `C:\` are documented rather than falsely claimed eliminated. Existing `.tmp`/`.npm-cache` paths remain approved pending future cutover to IS-100 `tmp/`/`local/`. Repository guard **code** remains NOT AUTHORIZED (ADR-020 OPEN). Application implementation remains NOT AUTHORIZED. |
| Reason | Make H-drive workspace compliance an auditable operational standard before GitHub/Netlify architecture (IS-105) and before any authorized tooling installs. |
| Alternatives | Claim total elimination of all `C:\` writes; defer workspace rules until coding; implement guard without ADR-020. |
| Consequences | Next IS document is PEOPLE-IS-105-GITHUB-AND-NETLIFY-ARCHITECTURE-1.0. ISSUE-HDRIVE-001 remains open until ADR-020 acceptance/implementation. Gate G-10 remains closed. |
| Related files | PEOPLE-IS-104; `PEOPLE_INTAKE_H_DRIVE_PROTOCOL.md`; `reports/PEOPLE_IS_104_COMPLETION_REPORT.md` |
| Revisit trigger | ADR-020 acceptance; path cutover package; new non-redirectable tool exception |

### D-068

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | PEOPLE-IS-105-GITHUB-AND-NETLIFY-ARCHITECTURE-1.0 is the canonical GitHub and Netlify Architecture specification. Path: `docs/implementation_specs/100_platform/PEOPLE-IS-105-GITHUB-AND-NETLIFY-ARCHITECTURE.md`. It locks single-repo topology with canonical remote `https://github.com/Grappe501/people.git`, canonical integration branch `master` (rename to `main` requires Decision Log), branch prefixes, commit/tag conventions, GitHub Actions authorization boundary, dedicated Netlify site (D-018) mapped to Preview/Staging/Production without secret inheritance from unrelated sites, promotion/rollback/provenance/verification/secrets rules, multi-environment scaling without model change, and the honest limitation that GitHub Actions / Netlify agents execute outside `H:\people` while project-controlled config remains governed. It also locks Burt full execution authority within governance (validate/commit/push/verify/deploy-when-applicable) with stops only at reserved Steve gates (ADR acceptance, scope, implementation/deployment authorization, legal/security/business policy). Creating workflows, `netlify.toml`, site linking, and live deploys remains NOT AUTHORIZED. Phase 1 platform documentation (IS-100…105) is COMPLETE. Application implementation remains NOT AUTHORIZED. |
| Reason | Define source-control and deployment architecture before application implementation so Burt has a complete platform framework without ambiguity. |
| Alternatives | Shared SOSWebsite Netlify site; multi-repo product split; silent `master`→`main` rename; inventing app surface to force Netlify evidence. |
| Consequences | Next IS document is PEOPLE-IS-200-DOMAIN-MODEL-1.0. Parallel freeze remediation remains required. ISSUE-GHN-001/002 open (non-blocking). ADR-009 remains OPEN/PROPOSED. Gate G-10 remains closed; `deploymentAuthorized` remains false. |
| Related files | PEOPLE-IS-105; `reports/PEOPLE_IS_105_COMPLETION_REPORT.md`; Cursor Execution Protocol §9.0 |
| Revisit trigger | Repo rename; default-branch migration; first authorized deploy package; ADR-009 acceptance |

### D-069

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | (1) PEOPLE-IS-200-DOMAIN-MODEL-1.0 is the canonical Domain Model specification for Phase 2 business architecture. Path: `docs/implementation_specs/200_domain/PEOPLE-IS-200-DOMAIN-MODEL.md`. It locks ubiquitous language (Constitution Art. XIV / Glossary), data-layer separation, aggregate/entity/value-object catalogs, identity and ownership rules, invariants, Catalog 01 as state authority, Match Resolution ≠ Promotion, canonical/RedDirt write boundaries, domain services/events/policies, and a placement algorithm requiring every future package to name owning domain concepts before coding. It elevates `docs/04_data/PEOPLE_INTAKE_DOMAIN_MODEL.md` as subordinate foundation. Physical schema and application code remain NOT AUTHORIZED. ISSUE-MOD-001 and ISSUE-CANONICAL-001 remain OPEN and block related implementation packages. (2) PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0 is chartered as an independent governance lane (path: `docs/00_governance/lanes/PEOPLE_AUDIT_REMEDIATION_AND_QUALITY_OPS_FREEZE.md`): continuous audit/remediation/freeze readiness that does not block the primary IS sequence, and is required before design freeze approval / Gate G-10 opening. Phase 1 platform (IS-100…105) remains COMPLETE as permanent baseline. |
| Reason | Transition from platform governance to business architecture while keeping freeze quality work from stalling domain authorship. |
| Alternatives | Fold freeze into IS sequence; invent full entity DDL in IS-200; treat Entry as Canonical Person; silently close ISSUE-MOD-001. |
| Consequences | Next primary IS is PEOPLE-IS-201-ENTITY-SPECIFICATIONS-1.0. Audit lane may run remediation slices in parallel. Gate G-10 remains closed; `applicationCodeAuthorized` remains false. |
| Related files | PEOPLE-IS-200; audit lane charter; `reports/PEOPLE_IS_200_COMPLETION_REPORT.md` |
| Revisit trigger | ISSUE-MOD-001/CANONICAL-001 resolution; IS-201 authorship; freeze campaign start |

### D-070

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | (1) PEOPLE-IS-201-ENTITY-SPECIFICATIONS-1.0 is the canonical Entity Specifications encyclopedia. Path: `docs/implementation_specs/200_domain/PEOPLE-IS-201-ENTITY-SPECIFICATIONS.md`. Every admitted entity must answer the mandatory questionnaire (why, owner, aggregate, identity, invariants, Catalog 01 lifecycle, module, modifiers, events, permissions, APIs, packages, tests). Catalog 01 remains the sole production state authority. Match Resolution and Promotion remain separate. Standing extension doctrine: belong to existing concept → extend; else evolve domain via IS/ADR or reject. (2) Audit lane slice AUDIT-SLICE-001 findings recorded at `reports/PEOPLE_AUDIT_SLICE_001_FINDINGS.md` (field-dictionary/workflow status drift; open Critical issues unchanged). Application implementation remains NOT AUTHORIZED. |
| Reason | Ensure every entity is fully specified before packages invent concepts; keep Catalog 01 and Match≠Promotion discipline; advance freeze readiness without blocking the primary IS lane. |
| Alternatives | Defer entity cards until database phase; invent Catalog keys to fill permission/API gaps; merge matching and promotion. |
| Consequences | Next primary IS is PEOPLE-IS-202-FIELD-AND-VALUE-OBJECT-SPECIFICATIONS-1.0. Audit lane continues independently. Gate G-10 remains closed. |
| Related files | PEOPLE-IS-201; `reports/PEOPLE_IS_201_COMPLETION_REPORT.md`; `reports/PEOPLE_AUDIT_SLICE_001_FINDINGS.md` |
| Revisit trigger | IS-202 field reconciliation; ISSUE-MOD-001 closure; freeze campaign |

### D-071

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | (1) PEOPLE-IS-202-FIELD-AND-VALUE-OBJECT-SPECIFICATIONS-1.0 is the canonical Field and Value Object Specifications dictionary. Path: `docs/implementation_specs/200_domain/PEOPLE-IS-202-FIELD-AND-VALUE-OBJECT-SPECIFICATIONS.md`. It defines value objects, the mandatory field questionnaire, core field cards (F1–F13), Catalog 01 as sole authority for lifecycle/state fields via VO-CAT01-STATE, UNKNOWN≠NO, raw≠normalized separation, and the field-level extend doctrine (reuse field → reuse VO → update IS-202/ADR → then packages). The historical field dictionary is subordinate. (2) AUDIT-SLICE-002 applies supersession banners to `docs/02_workflows/PEOPLE_INTAKE_STATE_MACHINES.md` and `docs/04_data/PEOPLE_INTAKE_FIELD_DICTIONARY.md` (findings: `reports/PEOPLE_AUDIT_SLICE_002_FINDINGS.md`). Application implementation remains NOT AUTHORIZED. |
| Reason | Define atomic domain information units before database architecture; eliminate draft-status ambiguity without inventing Catalog 01 enums. |
| Alternatives | Keep field dictionary as authority; embed physical SQL types now; redefine states in IS-202. |
| Consequences | Next primary IS is PEOPLE-IS-300-DATABASE-ARCHITECTURE-1.0. Audit lane continues. Gate G-10 remains closed. |
| Related files | PEOPLE-IS-202; AUDIT-SLICE-002 banners; `reports/PEOPLE_IS_202_COMPLETION_REPORT.md` |
| Revisit trigger | IS-300 physical mapping; ISSUE-MOD-001; remaining unbannered draft peers |

### D-072

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | (1) PEOPLE-IS-300-DATABASE-ARCHITECTURE-1.0 is the canonical Database Architecture specification for Phase 3. Path: `docs/implementation_specs/300_database/PEOPLE-IS-300-DATABASE-ARCHITECTURE.md`. It locks the principle that the database is an implementation/projection of the governed domain (IS-200…202), not a source of domain invention. It defines persistence philosophy, aggregate-to-table mapping, identity/PK/FK, ownership, normalization, write vs read models, soft-delete/archival, audit persistence, concurrency, sensitive-data segregation, naming, schema organization, migration governance (docs only), scaling notes, and the persistence extension doctrine. Creating migrations, SQL, Prisma schemas, seeds, indexes, triggers, or live schema objects remains FORBIDDEN. (2) AUDIT-SLICE-003 records Phase 3 start readiness without silently clearing Critical ADRs/issues (`reports/PEOPLE_AUDIT_SLICE_003_FINDINGS.md`). Historical `docs/04_data/PEOPLE_INTAKE_DATABASE_ARCHITECTURE.md` is bannered subordinate. Application implementation remains NOT AUTHORIZED. |
| Reason | Begin physical persistence design while preserving one-directional authority from domain → entities → fields → persistence → future schema. |
| Alternatives | Author Prisma/SQL now; invent tables without IS-201/202; treat Volume 9 bootstrap as already deployed. |
| Consequences | Next primary IS is PEOPLE-IS-301-LOGICAL-TABLE-CATALOG-1.0. ADR-002/003 remain OPEN. Gate G-10 and migrationsAuthorized remain closed/false. |
| Related files | PEOPLE-IS-300; AUDIT-SLICE-003; `reports/PEOPLE_IS_300_COMPLETION_REPORT.md` |
| Revisit trigger | Shared DB audit; ADR-002/003 acceptance; first authorized migration package |

### D-073

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | (1) PEOPLE-IS-301-LOGICAL-TABLE-CATALOG-1.0 is the canonical Logical Table Catalog. Path: `docs/implementation_specs/300_database/PEOPLE-IS-301-LOGICAL-TABLE-CATALOG.md`. It inventories logical persistence objects (LT-*) with a mandatory questionnaire (why, aggregate, entities, VOs, purpose, pattern, module, packages, migrations, read models, audit, sensitivity, retention, relationships). Logical tables are not physical/deployed tables. SQL, DDL, Prisma, migrations, indexes, and triggers remain FORBIDDEN. Domain owns meaning; database owns persistence architecture; implementation owns execution (not authorized). (2) AUDIT-SLICE-004 verifies docs-only posture (`reports/PEOPLE_AUDIT_SLICE_004_FINDINGS.md`). Application implementation and migrationsAuthorized remain false. |
| Reason | Catalog logical persistence objects before relationship specs and any physical schema planning. |
| Alternatives | Emit Prisma/SQL now; treat Volume 9 bootstrap tables as deployed; invent tables without IS-201/202. |
| Consequences | Next primary IS is PEOPLE-IS-302-LOGICAL-RELATIONSHIP-SPECIFICATIONS-1.0. Gate G-10 remains closed. |
| Related files | PEOPLE-IS-301; AUDIT-SLICE-004; `reports/PEOPLE_IS_301_COMPLETION_REPORT.md` |
| Revisit trigger | IS-302; shared DB audit; first authorized migration package |

### D-074

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | (1) PEOPLE-IS-302-LOGICAL-RELATIONSHIP-SPECIFICATIONS-1.0 is the canonical Logical Relationship Specifications. Path: `docs/implementation_specs/300_database/PEOPLE-IS-302-LOGICAL-RELATIONSHIP-SPECIFICATIONS.md`. It defines REL-* topology with identity, cardinality, ownership, business rules, navigation, logical persistence expectations, audit/sensitivity/retention interaction, and future physical mapping guidance without SQL. Standing doctrine: relationships are governed business concepts, not implementation conveniences; no physical foreign key may invent a business relationship; no migration/ORM relationship may appear unless present in IS-302 (or amendment/ADR). (2) AUDIT-SLICE-005 verifies docs-only posture. Application implementation and migrationsAuthorized remain false. |
| Reason | Complete logical persistence topology before constraints, read models, and migration governance. |
| Alternatives | Let ORM invent relations; embed FK DDL now; skip relationship catalog. |
| Consequences | Next primary IS is PEOPLE-IS-303-LOGICAL-CONSTRAINTS-AND-INTEGRITY-1.0. Gate G-10 remains closed. |
| Related files | PEOPLE-IS-302; AUDIT-SLICE-005; `reports/PEOPLE_IS_302_COMPLETION_REPORT.md` |
| Revisit trigger | IS-303; ISSUE-CANONICAL-001 physical FK decision |

### D-075

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | (1) PEOPLE-IS-303-LOGICAL-CONSTRAINTS-AND-INTEGRITY-1.0 is the canonical Logical Constraints and Integrity specification. Path: `docs/implementation_specs/300_database/PEOPLE-IS-303-LOGICAL-CONSTRAINTS-AND-INTEGRITY.md`. It defines CON-* cards consolidating Catalog 01 / IS-200…302 invariants with questionnaire C1–C28 across identity, uniqueness, requiredness, referential, cardinality, lifecycle, state-transition, ownership, temporal, ordering, immutability, append-only, concurrency, sensitivity, retention, cross-aggregate, and external-boundary categories. Standing integrity doctrine: a database constraint may enforce an approved business invariant but may not invent one; application validation may explain an invariant but may not weaken it; physical enforcement may use multiple mechanisms later while the logical invariant remains technology-neutral and authoritative. Authority hierarchy Catalog 01 → IS-200 → IS-201 → IS-202 → IS-302 → IS-303 locked; source conflicts must be surfaced as issues/ADRs. Page active image FK direction resolved logically as page-owned `source_image_id` (CON-REF-PAGE-IMAGE-ACTIVE). (2) AUDIT-SLICE-006 verifies docs-only posture, constraint contradiction visibility, and Gate G-10 blockers. Application implementation and migrationsAuthorized remain false. |
| Reason | Complete logical integrity rules before read models and migration governance so physical schema translates governed invariants. |
| Alternatives | Encode CHECK/UNIQUE DDL now; let ORM invent constraints; silently pick rules where docs conflict. |
| Consequences | Next primary IS is PEOPLE-IS-304-READ-MODEL-SPECIFICATIONS-1.0. Gate G-10 remains closed. |
| Related files | PEOPLE-IS-303; AUDIT-SLICE-006; `reports/PEOPLE_IS_303_COMPLETION_REPORT.md` |
| Revisit trigger | IS-304; IS-305; ISSUE-CANONICAL-001; ISSUE-DBA-001; ISSUE-AUDIT-001 |

### D-076

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | (1) PEOPLE-IS-304-READ-MODEL-SPECIFICATIONS-1.0 is the canonical Read Model Specifications. Path: `docs/implementation_specs/300_database/PEOPLE-IS-304-READ-MODEL-SPECIFICATIONS.md`. It defines RM-* logical read models with questionnaire M1–M24 covering consumers, source LT/REL/CON, projection boundaries, technology-neutral refresh/consistency (IMMEDIATE/BOUNDED/EVENTUAL as business expectations), filter/search/sort/pagination, aggregations/derived fields, security trimming, Catalog 08 sensitivity, audit visibility, retention, ownership, traceability, and package ownership. Standing doctrine: read models exist for consumption not ownership; project truth and do not create truth; may derive but never redefine approved business concepts; are disposable while the governed domain remains authoritative. Queue/worklist projections remain non-writers. (2) AUDIT-SLICE-007 verifies docs-only posture and G-10 blocker visibility. Application implementation and migrationsAuthorized remain false. |
| Reason | Complete logical presentation/query surfaces before migration governance so physical projections translate governed read models. |
| Alternatives | Invent SQL views now; let UI DTOs become alternate truth; skip read-model catalog. |
| Consequences | Next primary IS is PEOPLE-IS-305-MIGRATION-GOVERNANCE-1.0. Gate G-10 remains closed. Phase 3 persistence architecture nearly complete (migration governance remains). |
| Related files | PEOPLE-IS-304; AUDIT-SLICE-007; `reports/PEOPLE_IS_304_COMPLETION_REPORT.md` |
| Revisit trigger | IS-305; ISSUE-MOD-002; ISSUE-CANONICAL-001 |

### D-077

| Field | Value |
| --- | --- |
| Date | 2026-07-26 |
| Status | accepted |
| Decision | (1) PEOPLE-IS-305-MIGRATION-GOVERNANCE-1.0 is the canonical Migration Governance specification. Path: `docs/implementation_specs/300_database/PEOPLE-IS-305-MIGRATION-GOVERNANCE.md`. It defines how future MG-* migration packages will be governed (traceability to IS-300…304, scope allow/prohibit, validation/drift/evidence, safety/rollback/emergency stop, and authorization preconditions) without creating executable migrations. Standing doctrine: a migration implements an approved logical design and never creates one; no migration may introduce a table, relationship, constraint, or read model that is not already governed; executable schema is the final translation layer, never the source of architecture. (2) Phase 3 Database Architecture documentation is complete (IS-300…305). Completing IS-305 does NOT open Gate G-10 and does NOT set migrationsAuthorized or applicationCodeAuthorized. Implementation Authorization may be considered only after separate G-10 / freeze / ADR / audit evaluation. (3) AUDIT-SLICE-008 verifies docs-only posture and G-10 still closed. Next primary focus: PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0. |
| Reason | Bridge design to future implementation with controlled change rules while remaining documentation-only. |
| Alternatives | Author SQL/Prisma now; treat Phase 3 complete as auto G-10; skip migration governance. |
| Consequences | Phase 3 docs complete. Gate G-10 remains closed. First physical schema package not authorized. |
| Related files | PEOPLE-IS-305; AUDIT-SLICE-008; `reports/PEOPLE_IS_305_COMPLETION_REPORT.md` |
| Revisit trigger | Gate G-10 review; ISSUE-FREEZE-001; ISSUE-DBA-001; first MG-* when authorized |
