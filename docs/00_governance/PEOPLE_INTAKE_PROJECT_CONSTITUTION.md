# PEOPLE INTAKE SYSTEM

# VOLUME 0 — PROJECT CONSTITUTION

**Document ID:** PEOPLE-PROJECT-CONSTITUTION-3.0  
**Status:** draft_complete — **highest-authority standing orders for this repository**  
**Version:** 3.0  
**Mandatory practice:** Every human contributor and every AI assistant **reads this Volume 0 before every build session.**

---

## Current Implementation Lock

```text
Design freeze: DENIED
Gate G-9: FAIL
Gate G-10: CLOSED
applicationCodeAuthorized: false
```

**No application code until Gate G-9 is APPROVED and Gate G-10 opens.**  
Maintaining this Constitution does not authorize implementation.

**Active control plane:** `contracts/governance/active-build.json`  
**Documentation library map:** `docs/00_governance/PEOPLE_INTAKE_DOCUMENTATION_LIBRARY.md`  
**Execution playbook (dormant until G-10):** `docs/08_implementation/PEOPLE_INTAKE_CURSOR_BUILD_ORCHESTRATION.md`

---

## PREAMBLE

The People Intake System is more than an application. It is the trusted front door to a larger ecosystem of civic technology whose foundation is accurate people records, preserved evidence, transparent decision-making, and long-term public trust.

Every architectural decision made within this project must strengthen those goals.

This Constitution exists to ensure that the software evolves without losing its original purpose.

Technology changes.

Frameworks change.

Developers change.

AI assistants change.

This Constitution is intended to remain stable.

It establishes the governing principles that every implementation, enhancement, refactor, migration, deployment, and future integration must follow.

When there is uncertainty, this Constitution takes precedence over convenience.

When implementation conflicts with the approved design, the design must be revisited before implementation continues.

The purpose of this document is not to describe how every feature works.

Its purpose is to define the permanent engineering philosophy of the project.

---

# ARTICLE I — MISSION

The mission of the People Intake System is to transform handwritten volunteer information into trusted canonical people while preserving every piece of source evidence required to explain how every decision was made.

The system exists to:

* preserve original evidence
* improve data quality
* reduce duplicate records
* provide transparent provenance
* support future civic applications
* maintain public trust
* minimize manual work without sacrificing accuracy

The software shall always favor accuracy over speed when those goals conflict.

### Operating mantra

> Capture the page. Transcribe every entry. Match each person. Preserve the evidence.

### What the system is not

People Intake is not a CRM, canvassing tool, messenger, OCR product, volunteer scheduler, public form host, or RedDirt application module.

---

# ARTICLE II — UNIVERSAL ENGINEERING CONSTITUTION

The following principles apply not only to People Intake, but to every application developed within the broader SOSWebsite ecosystem unless a future constitutional amendment explicitly states otherwise.

These principles establish a common engineering language across all applications — including RedDirt (`H:\SOSWebsite`), Relationship Command Center, ContactListSOS, Arkansas Civic University, and future systems.

## Section 1 — Shared Identity

Identity belongs to the canonical people domain.

Applications may contribute information.

Applications may consume information.

Applications do not own identity unless they are explicitly designated as the canonical identity service.

## Section 2 — Evidence First

Original evidence is never discarded merely because newer information exists.

Applications preserve:

* original submissions
* provenance
* correction history
* audit history

Derived information must always be explainable from preserved evidence.

## Section 3 — Human Accountability

Artificial intelligence may assist.

Artificial intelligence may recommend.

Artificial intelligence may summarize.

Artificial intelligence may classify.

Artificial intelligence does not silently make irreversible identity decisions without an explicitly approved workflow.

Human accountability remains the final authority for sensitive operations.

## Section 4 — Security by Default

Every application shall implement:

* authentication
* authorization
* least privilege
* audit logging
* private storage
* secure secrets management
* server-side enforcement

Security is never optional.

## Section 5 — Documentation Is Product

Documentation is part of the software.

A feature is incomplete until its documentation reflects its behavior.

No undocumented architecture becomes canonical.

## Section 6 — Design Before Code

Major architectural decisions shall be documented before implementation.

Implementation exists to realize approved design—not to invent it.

If implementation reveals a flaw in the design, the design must be updated first.

## Section 7 — Modular Architecture

Applications should communicate through stable contracts.

Direct dependencies between unrelated systems should be minimized.

Modules should be replaceable without redesigning the platform.

## Section 8 — Explainability

Every important system decision should be explainable.

A future developer—or future AI assistant—should be able to understand:

* why something exists
* what problem it solves
* who owns it
* how it should evolve

Opaque systems are discouraged.

## Section 9 — Auditability

Every important action should be attributable to:

* who
* what
* when
* where
* why (when appropriate)

Audit history is treated as a first-class system component.

## Section 10 — Long-Term Maintainability

The project should always optimize for:

* clarity
* consistency
* simplicity
* stability
* extensibility

Short-term convenience should not compromise long-term maintainability.

### Ecosystem coherence test

If a new application cannot state (1) what canonical data it owns, (2) how it authenticates, (3) how it audits, and (4) how it deploys with preview/rollback, it is not ready to join the platform.

### Human approval boundaries (ecosystem)

| Action | Requires human Owner/admin approval |
| --- | --- |
| Design freeze / unfreeze | Yes |
| Production deployment | Yes |
| Schema migrations to shared data | Yes |
| Security-policy weakening | Yes |
| Automatic identity-merge policy | Yes |
| Cross-app destructive data ops | Yes |
| Secret rotation / production credential change | Yes |
| Constitutional amendment | Yes |

---

# ARTICLE III — CURSOR IMPLEMENTATION OATH

Before beginning any implementation session, Cursor shall conceptually follow this sequence:

1. Read the Project Constitution.
2. Read the relevant design volume.
3. Verify the current implementation phase.
4. Confirm the intended scope.
5. Build only the approved slice.
6. Validate all required gates.
7. Update documentation.
8. Commit to GitHub.
9. Verify deployment.
10. Report completion and any deviations.

If a requested implementation would violate this Constitution, implementation should stop and the conflict should be reported for review.

### Standing orders (People Intake)

- Confirm workspace is `H:\people`.  
- Read `contracts/governance/active-build.json` and respect authorized / forbidden paths.  
- Run H-drive preflight when tooling is available.  
- Never invent architecture or undocumented endpoints/states.  
- Never bypass validation gates.  
- On design conflict or missing decision: **stop**, document, escalate.  
- Keep commits small and reviewable.  
- Never set `applicationCodeAuthorized` outside the Owner freeze process.  
- Never intentionally write project-controlled artifacts to `C:\`.

While Gate G-10 is closed, steps 5–9 apply only to authorized documentation/remediation work — not application code.

---

# ARTICLE IV — CONSTITUTIONAL AMENDMENTS

This Constitution is intended to be stable.

Future amendments should:

* identify the affected articles
* explain the reason for the change
* describe the impact on existing systems
* maintain backward compatibility whenever practical
* be documented before implementation

Architectural changes should not occur silently through code alone.

### Change-control sequence (after design freeze)

1. Stop implementation that depends on the contested area.  
2. Document the issue (findings/risk + Decision Log).  
3. Update affected design volumes and contracts.  
4. Amend this Constitution if a standing order changes.  
5. Re-approve freeze scope (Owner).  
6. Resume implementation only under amended contracts.

---

# ARTICLE V — REPOSITORY CONSTITUTION

### Project root

```text
H:\people
```

- All project-controlled artifacts remain under this root.  
- No intentional project writes to `C:\`.  
- Controlled temp/cache under `H:\people` (`.tmp`, `.npm-cache`, related caches).  
- Application is separate from `H:\SOSWebsite`. Shared ecosystem contracts — not shared application modules.

### Repository ownership

- Dedicated GitHub repository: https://github.com/Grappe501/people  
- Dedicated Netlify site preferred when deployment is authorized.  
- No direct RedDirt code imports.

### Canonical directory layout (target after Gate G-10)

```text
docs/                 Design library + constitution
contracts/            Machine-readable governance and schemas
reports/              Audits, risk, readiness
develop_notes/        Build notes, next-build, slice templates
scripts/              Validators and tooling
diagrams/             Architecture diagrams
src/                  Application code (only after G-10)
tests/                Automated tests (only after G-10)
database/ or prisma/  Schema/migrations (only after authorization)
.github/              CI workflows (when authorized)
netlify/              Functions/config (when authorized)
```

Before G-10, only design-authorized paths may be written.

### Git strategy

Descriptive commits per slice; push after local validation; prefer small commits; never commit secrets.

---

# ARTICLE VI — ENGINEERING STANDARDS

### Stack (as designed; implement only after freeze)

Next.js · TypeScript · React · Prisma · hosted Postgres · Supabase Auth · private object storage · Netlify · server API routes/functions · schema validation.

Stack changes require Decision Log + design amendment.

### Coding standards

- Clarity over cleverness; preserve comments that encode invariants.  
- Explicit state transitions only.  
- Versioned HTTP API under `/api/v1` with contracts before endpoints.  
- Idempotency for duplicate-sensitive writes; claims/versions for concurrency.  
- Modular services: auth, storage, queue/claim, transcription, matching, promotion, admin, jobs.

### Naming

Domain terms match Article XIV. Machine enums match frozen contracts once approved.

### Testing

Every implementation phase includes unit, integration, workflow, and regression coverage. Manual-only phases are unacceptable.

---

# ARTICLE VII — ARCHITECTURE DOCTRINE

### Core flow

```text
Batch → Page → Intake Entry → Match Resolution → Promotion → Canonical Person
                 ↑
            Source Image (private)
```

### Domain ownership

| Domain | Owner |
| --- | --- |
| Batches, pages, entries, claims, match work, intake audit | People Intake |
| Canonical person identity and attributes (shared) | Canonical people domain via **controlled promotion** |
| RedDirt operational tables / UI | RedDirt — People Intake does not write them |

### Workspaces

**CAPTURE · TRANSCRIBE · MATCH · MANAGE** — separate jobs. Matching must not interrupt transcription typing.

### Integration rule

Canonical people are reached only through the approved promotion contract.

---

# ARTICLE VIII — SECURITY CONSTITUTION

1. Authenticate every route except explicitly approved sign-in handling.  
2. Approved users only; no public signup; individual accounts.  
3. Server-side authorization: deny by default; enforce role **and** record **and** state.  
4. Least-privilege database credential ≠ migration credential.  
5. Source images in private object storage; temporary authorized access only; never public source URLs.  
6. Logs never contain raw PII dumps, secrets, or signed URLs.  
7. High-risk operations require successful audit write.  
8. Secrets live in approved stores — never in git.

### Prohibited

Public source images · client-only authorization · automatic uncertain merges · destructive canonical changes without policy and audit · production secret exposure · bypassing Gate G-9 / G-10.

---

# ARTICLE IX — DATA CONSTITUTION

- Source images and raw transcription are retained.  
- Normalized values support matching without discarding raw.  
- Corrections append history; they do not erase prior evidence.  
- Every promoted canonical value requires provenance.  
- Volunteer / email-list style fields: **YES / NO / UNKNOWN** — blank never silently becomes NO.  
- Prefer temporary duplicates over false merges.  
- Household shared contacts do not independently prove identity.  
- Schema changes are additive and compatibility-audited; no schema writes until shared-database inspection and authorization allow them.

---

# ARTICLE X — USER EXPERIENCE DOCTRINE

- Mobile-first for capture and transcription.  
- Accessibility is required (keyboard, screen reader, contrast, focus, non-color-only status).  
- One primary action per screen; plain language; never hide save status.  
- Draft preservation and resume after interruption are mandatory.  
- Primary cadence: Claim Next → Enter → Review → Submit & Open Next.  
- Errors explain recovery.  
- Role-appropriate homes only.

---

# ARTICLE XI — VALIDATION GATES

Each phase and significant slice must pass applicable gates before advancing:

| Gate | Requirement |
| --- | --- |
| Build | Project compiles / builds |
| Type | No type errors |
| Test | Automated tests for the change pass |
| Documentation | Docs, ledger, and contracts updated |
| Accessibility | Applicable a11y checks pass |
| Security | Required controls verified for the slice |
| Deployment preview | Preview deploy succeeds once Netlify is wired |
| Manual acceptance | Human checklist for the critical path |

Fail any gate → do not start the next phase.

Named program gates G-1…G-10 remain defined in Volume 7 / build-gates documentation. **G-9 (design freeze) and G-10 (implementation authorization) are absolute.**

---

# ARTICLE XII — OPERATIONAL DOCTRINE

- Structured logging without prohibited payloads.  
- Monitoring for queue health, job failures, auth anomalies, and storage errors.  
- Background jobs are retryable, idempotent where required, and observable.  
- Backups and recovery are documented and verified before production trust.  
- Incident response: contain → preserve evidence → remediate → postmortem → Decision Log if policy changes.  
- Deployment promotion: preview → approved RC → production with Owner approval.  
- Rollback paths exist for app release, config, and (when authorized) migrations.

---

# ARTICLE XIII — FUTURE EXPANSION RULES

Enhancements must extend the platform without collapsing domain layers or weakening security.

| Allowed later (with design) | Must not violate |
| --- | --- |
| OCR / AI assist as **assistive** tools | Human remains accountable; raw evidence preserved |
| Additional apps reading canonical people | Controlled contracts; least privilege |
| New modules (export, training, analytics) | Separate scopes; no silent CRM sprawl |

New capability process: propose → design → Decision Log → amend freeze scope → implement behind gates.

Version 1 non-goals (OCR-as-authority, messaging, canvassing, public forms, auto-uncertain-merge, etc.) stay out until formally re-scoped.

---

# ARTICLE XIV — GLOSSARY

Use these terms consistently across docs, code, APIs, and AI sessions. Expanded glossary: `PEOPLE_INTAKE_GLOSSARY.md`. Conflicts resolve toward this Constitution and accepted Decision Log entries.

| Term | Definition |
| --- | --- |
| **Batch** | Collection of photographed pages uploaded together, usually with shared source metadata |
| **Page** | One photographed volunteer sheet; primary queue work item; one source image; up to ten entries |
| **Intake Entry (Entry)** | One handwritten person line transcribed from a page; unique identity even among siblings on the same page |
| **Claim** | Atomic lock giving one user exclusive editing rights to a page for authorized work |
| **Queue** | Shared multi-user work list of pages across upload, entry, match, review, and completion |
| **Match Candidate** | Scored possible relationship between an entry and a canonical person, with reasons and tier |
| **Promotion** | Controlled process that creates or links canonical person data from an intake entry with provenance |
| **Canonical Person** | Shared individual identity used by RedDirt and other authorized systems; not the raw transcription |
| **Provenance** | Trail from a value or decision to batch, page, entry, image, actors, and timestamps |
| **Audit Event** | Append-only record of a meaningful system or user action |
| **Raw Value** | Exactly what the operator transcribed |
| **Normalized Value** | Cleaned comparison form used for matching/ops without discarding raw |
| **Source Image** | Original uploaded photograph/scan, stored privately and linked to the page |
| **Idempotency** | Safe replay of the same logical request without duplicate side effects |
| **UNKNOWN** | Paper did not clearly indicate Yes or No; never silently treated as NO |
| **Unreadable** | Writing appears present but cannot be read confidently |
| **Design Freeze** | Gate after which design contracts govern implementation until formally amended |

---

# ARTICLE XV — DOCUMENTATION LIBRARY

The People Intake design and implementation package is organized as a cohesive engineering library:

| Volume | Title |
| --- | --- |
| **0** | Project Constitution (this document) |
| **1** | Governance Foundation |
| **2** | Workflow & User Experience |
| **3** | Data, Matching & Storage |
| **4** | Security, API & Engineering Contracts |
| **5** | Quality, Operations & Design Freeze |
| **6** | Architecture Audit & Design Validation |
| **7** | Master Cursor Build Orchestration |
| **8** | Technical Specifications |
| **9** | Database Specifications |
| **10** | API Specifications |
| **11** | UI Specifications |
| **12** | Component Library |
| **13** | Canonical Platform Standards |
| **EC** | Engineering Catalogs (states, errors, events, configuration) |
| **IP** | Implementation Packages (executable Cursor work units) |

Folder paths under `docs/` may retain historical numbering for stability; **library volume numbers** in the documentation index and `PEOPLE_INTAKE_DOCUMENTATION_LIBRARY.md` are authoritative for reading order.

**Implementation bridge:** Volumes 8–13 + EC + IP convert architecture into an implementation system. Production code must not begin until Gate G-10, and must not invent behavior absent from these specifications.

Full map: `docs/00_governance/PEOPLE_INTAKE_DOCUMENTATION_LIBRARY.md`

---

# PROJECT CHARTER

The success of the People Intake System will not be measured solely by the amount of code written.

Success will be measured by whether the platform remains trustworthy, understandable, maintainable, secure, and capable of supporting future civic applications without requiring its foundation to be rebuilt.

Every line of code should reinforce that objective.

Every future contributor—human or AI—is expected to uphold these principles.

### Definition of operational success

A volunteer sheet can be photographed, uploaded, transcribed, reviewed, matched, promoted to the canonical people domain, and fully audited **without data loss**, with recoverable workflows and an architecture that future enhancements can extend without foundation redesign.

---

## Cross-References

| Need | Document |
| --- | --- |
| Documentation library map | `docs/00_governance/PEOPLE_INTAKE_DOCUMENTATION_LIBRARY.md` |
| Execution playbook (Volume 7) | `docs/08_implementation/PEOPLE_INTAKE_CURSOR_BUILD_ORCHESTRATION.md` |
| Cursor protocol | `docs/08_implementation/PEOPLE_INTAKE_CURSOR_EXECUTION_PROTOCOL.md` |
| Build gates | `docs/08_implementation/PEOPLE_INTAKE_BUILD_GATES.md` |
| Freeze / audit | `docs/08_implementation/PEOPLE_INTAKE_DESIGN_FREEZE_REPORT.md` · `reports/` |
| Full glossary | `docs/00_governance/PEOPLE_INTAKE_GLOSSARY.md` |
| Active build | `contracts/governance/active-build.json` |

---

**End of Volume 0.**  
If any other document conflicts with this Constitution on a standing order, stop and resolve via Decision Log before proceeding.
