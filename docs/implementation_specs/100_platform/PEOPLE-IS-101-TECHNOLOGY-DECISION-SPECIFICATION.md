# PEOPLE-IS-101 — TECHNOLOGY DECISION SPECIFICATION

**Title:** Technology Decision Specification  
**Document ID:** `PEOPLE-IS-101-TECHNOLOGY-DECISION-SPECIFICATION-1.0`  
**Version:** 1.0  
**Status:** APPROVED  
**Phase:** PHASE 1 — REPOSITORY AND PLATFORM ARCHITECTURE  
**Project Root:** `H:\people`  
**Owner:** People Intake System Program  
**Technical Reviewer:** Program  
**Governance Reviewer:** Program  
**Traceability Reviewer:** Program  
**Approval Authority:** Decision Log D-063  
**Created Date:** 2026-07-26  
**Last Updated:** 2026-07-26  
**Governing Documents:** Master Build Outline; Constitution; Volumes 0–13; Catalogs 00–09; PEOPLE-IS-000…005; PEOPLE-IS-100; Catalog 09 Traceability  
**Dependencies:** Catalog Library COMPLETE (D-062); IS-100 CLOSED (D-061); ADR-001…020 remain OPEN for formal Decision Log acceptance of each ADR  
**Implementation Authorization:** `IMPLEMENTATION NOT AUTHORIZED`

```text
DESIGN COMPLETE
APPROVED FOR DOCUMENTATION GOVERNANCE
RECOMMENDATIONS RECORDED — INDIVIDUAL ADRs NOT YET ACCEPTED
APPLICATION IMPLEMENTATION NOT AUTHORIZED
IMPLEMENTATION READINESS BLOCKED BY OPEN ADRs
```

---

## 1. Purpose

Formally evaluate and document every major technology choice required before implementation packages may reference concrete technologies.

For each decision area this specification records:

* decision question
* decision criteria
* options considered
* recommendation (design alignment)
* trade-offs
* risks
* H-drive compatibility notes
* resulting ADR mapping
* residual open issues

**Honesty rule:** Constitution / Master Build Plan “as designed” stack language is **design intent**, not an accepted ADR. Catalog 4 seeded `AUTH_PROVIDER` / `STORAGE_PROVIDER` allowed values are **config-seed constraints**, not closed provider ADRs. This document may **recommend**; it does **not** silently mark ADR-001…020 as Decision-Log-accepted.

## 2. Scope

Programming language/runtime; application framework; workspace/package model; package manager; database provider; data-access strategy; authentication provider (and auth-method contradiction); authorization model boundary; object storage; background jobs; email/notification provider; AI provider boundary; validation library; test framework; observability/logging; hosting/deployment; H-drive development compatibility; ADR index and acceptance gate.

## 3. Out of Scope

* Accepting individual ADRs without Decision Log entries  
* Package installation, scaffolding, migrations, provider connections, deployments  
* Exact package versions (deferred to implementation packages after ADR acceptance)  
* PEOPLE-IS-102 module-boundary detail, IS-104 H-drive enforcement design depth, IS-105 GitHub/Netlify wiring depth (consume recommendations here)  
* Inventing Catalogs 10–13  

## 4. Governing References

* `docs/00_governance/PEOPLE_INTAKE_PROJECT_CONSTITUTION.md` (stack as designed)  
* Master Build Plan §16 recommended alignment  
* `docs/06_engineering/PEOPLE_INTAKE_APPLICATION_ARCHITECTURE.md`  
* Auth architecture + TECH_SPEC_AUTHENTICATION (method conflict)  
* Image storage architecture (provider deferred)  
* Volume 09 (Postgres-class; provider deferred)  
* Volume 13 platform standards (doctrine, not vendor picks)  
* Catalog 4 configuration seeds  
* PEOPLE-IS-100; Catalog 09; D-018 (dedicated Netlify preferred)  
* Gate G-10 CLOSED  

## 5. Definitions

| Term | Meaning |
| --- | --- |
| RECOMMENDED | Design-alignment recommendation recorded here; ADR still OPEN until Decision Log acceptance |
| PROPOSED (ADR) | Formal ADR candidate awaiting acceptance |
| ACCEPTED (ADR) | Decision Log accepted; may be cited by implementation packages |
| Design intent | Constitution/architecture language not yet ADR-closed |
| Adapter boundary | Provider-specific code isolated behind interfaces (IS-100) |

## 6. Assumptions

* Node.js remains available for documentation tooling; application runtime pin is part of ADR-001.  
* Dedicated GitHub repository already exists (`Grappe501/people`); local root remains `H:\people`.  
* Catalog Library 0–9 is complete at foundation level.  
* OS may write unrelated files outside H:\people; project-controlled artifacts must not.  

## 7. Functional Requirements

| ID | Description |
| --- | --- |
| REQ-TECH-001 | Every major technology area MUST map to an ADR ID. |
| REQ-TECH-002 | Each ADR evaluation MUST record criteria, alternatives, recommendation, trade-offs, and risks. |
| REQ-TECH-003 | Recommendations MUST NOT authorize implementation by themselves. |
| REQ-TECH-004 | Implementation packages MUST NOT hard-depend on a technology until its ADR is Decision-Log accepted. |
| REQ-TECH-005 | Known documentation contradictions MUST be recorded as open issues, not silently resolved. |
| REQ-TECH-006 | Provider selections MUST preserve adapter boundaries from PEOPLE-IS-100. |
| REQ-TECH-007 | H-drive compatibility MUST be evaluated for each tooling-affecting choice (ADR-020). |
| REQ-TECH-008 | Secrets MUST NOT appear in this specification. |

## 8. Nonfunctional Requirements

| ID | Description |
| --- | --- |
| NFR-TECH-MAINTAIN-001 | Recommendations prefer replaceable providers behind adapters. |
| NFR-TECH-SEC-001 | Auth, storage, and secret handling recommendations must not weaken Catalog 5/8 controls. |
| NFR-TECH-OPS-001 | Hosting recommendations must distinguish Preview / Staging / Production (IS-100). |
| NFR-TECH-PORT-001 | Domain layer must remain provider-neutral. |
| NFR-TECH-HDRIVE-001 | Selected tooling MUST support redirecting caches/temp under `H:\people` where configurable. |

## 9. Architecture — Decision Framework

### 9.1 Decision criteria (global)

| Criterion | Weight guidance |
| --- | --- |
| Fit to documented domain (claims, uploads, audit, promotion) | High |
| Adapter / replaceability | High |
| H-drive / Windows local-dev compatibility | High |
| Security & privacy posture | High |
| Operational clarity on Netlify-class hosting | High |
| Team familiarity / ecosystem maturity | Medium |
| Cost / operational complexity | Medium |
| Time-to-first-authorized-package (after freeze) | Medium |

### 9.2 Acceptance gate for each ADR

An ADR becomes usable by implementation packages only when:

1. Evaluation exists in this specification (or successor amendment)  
2. Decision Log records acceptance  
3. `DECISION_REGISTER.md` status → APPROVED  
4. Related CRITICAL open issue resolved or explicitly deferred with non-blocking rationale  
5. Allowed/forbidden paths updated in the consuming implementation package  

### 9.3 Recommended stack summary (design alignment — NOT ADR-accepted)

```text
Language/runtime:     TypeScript on Node.js
App framework:        Next.js (App Router intent) + React
Workspace:            Single package initially; packages/ only when IS-100 criteria met
Package manager:      npm (documentation already uses npm scripts)
Database:             Hosted PostgreSQL (Postgres-class)
Data access:          Prisma (or equivalent typed ORM) behind repository adapters
Auth provider:        Supabase Auth (method TBD — see contradiction)
Object storage:       Private object storage via adapter (NOT public Netlify assets)
Jobs:                 TBD — must not assume Netlify alone for durable/long-running work
Email/notify:         Provider TBD behind Catalog 6 contracts
AI:                   Optional assistive only; human review required (ADR-019)
Validation:           Schema validation library (Zod or JSON Schema toolchain) — ADR-010
Tests:                Framework TBD (ADR-011); Vitest/Playwright class tools typical
Observability:        Structured logs + metrics/traces provider TBD (ADR-012)
Hosting:              Dedicated Netlify site (D-018) for web/app; other backends as ADRs require
```

Exact versions: **deferred**.

---

## 10. Data Contracts

NOT_APPLICABLE for runtime entities. Technology selections MUST NOT invent database tables; Volume 09 / future IS-300 remain authoritative for schema.

## 11. Interface Contracts

Future provider adapters MUST implement interfaces owned by `src/application` / `contracts` per IS-100. This document defines **which** providers are recommended, not the adapter TypeScript surfaces.

## 12. State Behavior

NOT_APPLICABLE (no runtime state machine). ADR acceptance states: PROPOSED → UNDER_REVIEW → APPROVED | REJECTED | DEFERRED | SUPERSEDED.

## 13. Permission Behavior

Authorization **model** remains Catalog 5. Technology choice MUST NOT replace permission keys with framework roles silently. Supabase Auth (or alternate) supplies identity; Catalog 5 supplies authorization.

## 14. Error and Recovery Behavior

Technology failures MUST map to Catalog 2 codes when user/operator visible. Provider outages MUST degrade safely; no silent data loss. Selection criteria MUST prefer providers with clear failure modes and backup/restore stories (especially ADR-002, ADR-005, ADR-013).

## 15. Audit Requirements

Audit storage strategy is ADR-013. Recommendations MUST keep Catalog 3 event names stable regardless of storage technology.

## 16. Notification Requirements

Channels/providers are ADR-007 + ISSUE-NOTIFY-001. Catalog 6 owns notification contracts; providers implement them.

## 17. Background Processing

ADR-006 + ISSUE-JOBS-001. Netlify MUST NOT be assumed sufficient for durable queues or long-running jobs (IS-100).

## 18. Security and Privacy

Auth (ADR-004), storage (ADR-005), secrets (never in repo), retention enforcement (ADR-017). Private intake images MUST NOT live in public `public/` or public CDN buckets.

## 19. Data Classification and Retention

Catalog 8 remains authoritative. Technology choices MUST support classification-aware retention/hold/destruction workflows when authorized.

## 20. Observability

ADR-012. Local logs under `H:\people\logs` (IS-100); production telemetry provider TBD. Logs MUST NOT contain secrets or unrestricted PII.

## 21. Testing

ADR-011. Test locations per IS-100 (`tests/`, optional co-located units). Repository-guard and H-drive tests required before tooling authorization (ADR-020).

## 22. Acceptance Criteria

| ID | Criterion | Blocking for IS-101 docs close |
| --- | --- | --- |
| AC-TECH-001 | Every ADR-001…020 has an evaluation section with recommendation or explicit DEFER | Yes |
| AC-TECH-002 | Known contradictions (auth method; storage provider seed vs private storage) are recorded | Yes |
| AC-TECH-003 | Document states ADRs remain OPEN until Decision Log acceptance | Yes |
| AC-TECH-004 | No secrets or production connection strings included | Yes |
| AC-TECH-005 | H-drive compatibility addressed for tooling-affecting choices | Yes |
| AC-TECH-006 | Implementation remains NOT AUTHORIZED | Yes |
| AC-TECH-007 | Next docs (IS-102…105) can consume recommendations without re-deriving stack intent | Yes |

## 23. Open Decisions — ADR Evaluations

### ADR-001 — Application Framework

| Field | Content |
| --- | --- |
| Question | Which application framework hosts UI + server entrypoints? |
| Criteria | React ecosystem fit; Netlify deployability; adapter-friendly API routes; TypeScript; mobile-first UX |
| Options | Next.js; Remix; plain React SPA + separate API; NestJS+SPA |
| Recommendation | **Next.js + React + TypeScript** (aligns with Constitution / architecture intent) |
| Trade-offs | Framework conventions may pressure folder layout (IS-100 RISK-REPO-001) |
| Risks | Premature App Router / Pages Router lock-in; server/client boundary mistakes |
| H-drive | Next/Node caches MUST be redirected under `H:\people` (ADR-020) |
| Status | **PROPOSED / OPEN** — resolves ISSUE-PLATFORM-001 only after Decision Log acceptance |

### ADR-002 — Database Provider

| Field | Content |
| --- | --- |
| Question | Which hosted database provides durable relational storage? |
| Criteria | PostgreSQL-class features; backups; SSL; environment separation; no workstation-path coupling |
| Options | Supabase Postgres; Neon; RDS/Azure PG; self-hosted PG (discouraged for v1) |
| Recommendation | **Hosted PostgreSQL** (provider brand TBD among Postgres-class hosts; Supabase PG is a leading candidate if Auth/Storage co-locate) |
| Trade-offs | Vendor coupling vs operational simplicity |
| Risks | Choosing non-Postgres breaks Volume 09 assumptions |
| Status | **PROPOSED / OPEN** — ISSUE-DATABASE-001 |

### ADR-003 — ORM / Data Access

| Field | Content |
| --- | --- |
| Question | How does application code access the database? |
| Criteria | Type-safety; migration story; repository-adapter fit; Windows/H-drive OK |
| Options | Prisma; Drizzle; Kysely; raw `pg` |
| Recommendation | **Prisma** behind repository adapters (domain never imports Prisma Client directly) |
| Trade-offs | Migration rigidity; generate step must stay under H:\people |
| Status | **PROPOSED / OPEN** |

### ADR-004 — Authentication Provider

| Field | Content |
| --- | --- |
| Question | Who authenticates users and issues sessions/tokens? |
| Criteria | Adapter port (AuthPort); Catalog 5 separation; auditability |
| Options | Supabase Auth; Auth.js; Clerk; custom |
| Recommendation | **Supabase Auth** as identity provider |
| Contradiction | `PEOPLE_INTAKE_AUTH_ARCHITECTURE.md` emphasizes **Google OAuth**; `TECH_SPEC_AUTHENTICATION.md` emphasizes **email magic link / password**. **MUST NOT** silently pick one. |
| Residual issue | Record as auth-method sub-decision under ADR-004 / ISSUE-AUTH-001 |
| Status | **PROPOSED / OPEN** — provider recommended; **method UNRESOLVED** |

### ADR-005 — Object Storage Provider

| Field | Content |
| --- | --- |
| Question | Where are private intake images and sensitive blobs stored? |
| Criteria | Private by default; signed access; not public Netlify assets; retention-class aware |
| Options | Supabase Storage; S3-compatible; other private object store |
| Recommendation | **Private object storage via adapter**; public Netlify asset storage **MUST NOT** hold source images |
| Contradiction | Catalog 4 seed allows `STORAGE_PROVIDER=Netlify` — treat as **non-authoritative for private intake images** until amended; prefer private bucket providers |
| Status | **PROPOSED / OPEN** — ISSUE-STORAGE-001 |

### ADR-006 — Background Job Runtime

| Field | Content |
| --- | --- |
| Question | What runs durable/scheduled/async jobs? |
| Criteria | Catalog 7 job contracts; retries; idempotency; not solely Netlify request lifetime |
| Options | Queue worker (e.g. dedicated worker host); Supabase Edge + external queue; Netlify scheduled functions (limited); cloud queue + worker |
| Recommendation | **Dedicated job runtime / queue + worker** pattern; Netlify alone **insufficient** for durable long-running jobs |
| Status | **PROPOSED / OPEN** — ISSUE-JOBS-001; concrete vendor UNRESOLVED |

### ADR-007 — Notification / Email Provider

| Field | Content |
| --- | --- |
| Question | How are Catalog 6 notifications delivered in v1? |
| Criteria | Template safety; no PII leakage in logs; adapter boundary |
| Options | Resend; SendGrid; Postmark; SES; in-app only for v1 |
| Recommendation | **Email provider behind notification adapter**; exact vendor **UNRESOLVED** (ISSUE-NOTIFY-001) |
| Status | **PROPOSED / OPEN** |

### ADR-008 — API Style and Versioning

| Field | Content |
| --- | --- |
| Question | How are HTTP APIs shaped and versioned? |
| Criteria | Match Volume 10 / API specs; stable API-* IDs even if routes change |
| Options | REST `/api/v1`; RPC-style; tRPC-only |
| Recommendation | **Versioned REST-style HTTP JSON APIs** under `/api/v1` (or equivalent), with OpenAPI/contract fragments in `contracts/` |
| Status | **PROPOSED / OPEN** |

### ADR-009 — Hosting and Deployment

| Field | Content |
| --- | --- |
| Question | Where does the web application run? |
| Criteria | Preview/Staging/Production separation; D-018; dedicated secrets |
| Options | Dedicated Netlify site; Vercel; container PaaS |
| Recommendation | **Dedicated Netlify site** for application hosting (D-018), with non-Netlify services for DB/storage/jobs as required |
| Status | **PROPOSED / OPEN** — detail in PEOPLE-IS-105 |

### ADR-010 — Schema Validation Library

| Field | Content |
| --- | --- |
| Question | What validates request/config/payload schemas at runtime? |
| Criteria | TypeScript synergy; JSON Schema interoperability with `contracts/` |
| Options | Zod; Ajv/JSON Schema; Valibot; Yup |
| Recommendation | **Zod** for app-level validation **and/or** Ajv for canonical JSON Schema contracts — final pick PROPOSED; contracts remain source of truth |
| Status | **PROPOSED / OPEN** |

### ADR-011 — Test Framework

| Field | Content |
| --- | --- |
| Question | What runs unit/integration/e2e tests? |
| Criteria | TS support; CI on GitHub; artifacts under `generated/tests` or `local/tests` |
| Options | Vitest + Playwright; Jest + Playwright; Node test runner |
| Recommendation | **Vitest** (unit/integration) + **Playwright** (e2e/a11y smoke) class toolchain |
| Status | **PROPOSED / OPEN** |

### ADR-012 — Observability Provider

| Field | Content |
| --- | --- |
| Question | Where do production logs/metrics/traces go? |
| Criteria | PII redaction; env separation; no secrets |
| Options | OpenTelemetry + vendor; Netlify logs only; Datadog; Sentry (errors) |
| Recommendation | **Structured logging locally**; **OpenTelemetry-friendly** production exporter TBD |
| Status | **PROPOSED / OPEN** — vendor UNRESOLVED |

### ADR-013 — Audit Storage Strategy

| Field | Content |
| --- | --- |
| Question | How are Catalog 3 audit events durably stored? |
| Criteria | Append-oriented; queryable; retention-class aware; integrity |
| Options | Postgres audit tables; immutable log store; hybrid |
| Recommendation | **Primary: Postgres audit tables** aligned to Volume 09/10 specs; immutability controls via app+DB policy |
| Status | **PROPOSED / OPEN** |

### ADR-014 — Idempotency Strategy

| Field | Content |
| --- | --- |
| Question | How are duplicate submissions/jobs prevented? |
| Criteria | Match engineering idempotency contract; stable keys |
| Options | Idempotency-Key headers + store; natural unique constraints; outbox |
| Recommendation | **Idempotency keys + unique constraints + application checks** per existing engineering contract |
| Status | **PROPOSED / OPEN** |

### ADR-015 — Optimistic Concurrency Strategy

| Field | Content |
| --- | --- |
| Question | How are concurrent edits detected? |
| Criteria | `STALE_VERSION` / version columns already in error vocabulary |
| Options | Row version columns; ETags; last-write-wins (rejected for critical entities) |
| Recommendation | **Optimistic concurrency via version columns**; map failures to Catalog 2 `STALE_VERSION` |
| Status | **PROPOSED / OPEN** |

### ADR-016 — Canonical Person Integration Boundary

| Field | Content |
| --- | --- |
| Question | How does intake promote into canonical person systems? |
| Criteria | Anti-corruption layer; no provider types leaking into domain |
| Options | Explicit integration adapter + DTO contracts; shared DB (rejected) |
| Recommendation | **Anti-corruption integration module** under `src/integrations` with explicit DTOs (ISSUE-CANONICAL-001) |
| Status | **PROPOSED / OPEN** — contract details UNRESOLVED |

### ADR-017 — Data Retention Enforcement Strategy

| Field | Content |
| --- | --- |
| Question | How are Catalog 8 retention/hold/destruction rules enforced? |
| Criteria | Deterministic; auditable; legal hold suspends destruction |
| Options | Scheduled jobs + policy engine; manual ops only (insufficient for production) |
| Recommendation | **Policy metadata in DB + scheduled enforcement jobs** after job runtime ADR; exact durations still ISSUE-RETENTION-001 |
| Status | **PROPOSED / OPEN** |

### ADR-018 — Feature Flag Strategy

| Field | Content |
| --- | --- |
| Question | How are incomplete capabilities gated? |
| Criteria | No undocumented production behavior; env-aware |
| Options | Config keys (Catalog 4); LaunchDarkly-class; simple env flags |
| Recommendation | **Catalog 4 configuration flags** first; external flag SaaS only if justified later |
| Status | **PROPOSED / OPEN** |

### ADR-019 — AI Provider and Human Review Boundary

| Field | Content |
| --- | --- |
| Question | May AI assist transcription/matching, and under what controls? |
| Criteria | Human review for consequential outcomes; auditability; no silent auto-promotion |
| Options | No AI in v1; assistive AI with mandatory human confirm; autonomous AI (rejected for promotion) |
| Recommendation | **Assistive AI optional behind adapter; human review REQUIRED for finalize/promote**; provider TBD |
| Status | **PROPOSED / OPEN** |

### ADR-020 — H-Drive Development Enforcement

| Field | Content |
| --- | --- |
| Question | How are project-controlled writes kept under `H:\people`? |
| Criteria | Fail closed; no C: fallback; honest OS limitation |
| Options | `repository_guard` tool + env redirects; docs-only warnings (insufficient) |
| Recommendation | **Repository guard + TEMP/TMP/npm/next cache redirects** under `H:\people` (`tmp`, `local`, `.npm-cache`); detailed design in PEOPLE-IS-104 |
| Status | **PROPOSED / OPEN** — ISSUE-HDRIVE-001; ISSUE-REPO-002 |

### Package manager & workspace (supporting decisions)

| Topic | Recommendation | ADR link |
| --- | --- | --- |
| Package manager | **npm** (already used for governance scripts); lockfile when app scaffolding authorized | ADR-001 companion |
| Workspace model | **Single package first**; `packages/` only when IS-100 multi-consumer criteria met | ADR-001 / IS-100 |
| Language | **TypeScript** | ADR-001 |

## 24. Risks

| ID | Description | Mitigation |
| --- | --- | --- |
| RISK-TECH-001 | Treating recommendations as accepted ADRs | Explicit OPEN status; REQ-TECH-003/004 |
| RISK-TECH-002 | Auth method contradiction causes rework | ISSUE-AUTH-001 blocking until method ADR addendum |
| RISK-TECH-003 | Catalog 4 STORAGE_PROVIDER=Netlify vs private storage | Prefer private adapter; amend Catalog 4 if needed |
| RISK-TECH-004 | Netlify assumed for jobs/storage | IS-100 + ADR-006/005 explicit bans |
| RISK-TECH-005 | Prisma generate / caches write to C:\ | ADR-020 redirects before install |
| RISK-TECH-006 | Premature monorepo fragmentation | IS-100 package criteria |
| RISK-TECH-007 | AI autonomy creep | ADR-019 human-review lock |

## 25. Dependencies

* Catalog Library COMPLETE (D-062)  
* IS-100 CLOSED (D-061)  
* Decision Log acceptance of each ADR before coding against that technology  
* PEOPLE-IS-104 for ADR-020 depth; PEOPLE-IS-105 for Netlify/GitHub depth  
* Freeze / Gate G-10 for application implementation  

## 26. Traceability Matrix

| Requirement | Source | ADR / Artifact | Status |
| --- | --- | --- | --- |
| REQ-TECH-001 | IS-101 | ADR-001…020 | FULLY_MAPPED |
| REQ-TECH-002 | IS-101 | §23 evaluations | FULLY_MAPPED |
| REQ-TECH-003 | IS-000 / IS-101 | Implementation Authorization header | VERIFIED |
| REQ-TECH-004 | IS-005 Gate 6 | Package gate | FULLY_MAPPED |
| REQ-TECH-005 | IS-101 | Auth method + storage contradictions | FULLY_MAPPED |
| REQ-TECH-006 | IS-100 | Adapter rules | FULLY_MAPPED |
| REQ-TECH-007 | IS-100 / ADR-020 | H-drive notes per ADR | FULLY_MAPPED |
| REQ-TECH-008 | IS-000 | Secret exclusion | VERIFIED |
| ISSUE-PLATFORM-001 | Open register | ADR-001 | PARTIALLY_MAPPED (recommendation only) |
| ISSUE-DATABASE-001 | Open register | ADR-002/003 | PARTIALLY_MAPPED |
| ISSUE-AUTH-001 | Open register | ADR-004 | PARTIALLY_MAPPED |
| ISSUE-STORAGE-001 | Open register | ADR-005 | PARTIALLY_MAPPED |
| ISSUE-JOBS-001 | Open register | ADR-006 | PARTIALLY_MAPPED |
| ISSUE-HDRIVE-001 | Open register | ADR-020 / IS-104 | PARTIALLY_MAPPED |

## 27. Implementation Boundary

**Authorized now:** this specification; ADR index updates; Decision Log D-063; progress/index updates.

**Not authorized:** accepting ADRs without Decision Log; `npm install` for application scaffolding; creating `src/`/`app/`; Prisma migrations; Netlify production config; provider account binding; AI provider keys; any executable business logic.

## 28. Revision History

| Version | Date | Change | Author | Reviewer | Approval |
| --- | --- | --- | --- | --- | --- |
| 1.0 | 2026-07-26 | Initial technology decision specification with PROPOSED recommendations | Program | Program | D-063 |

---

## Phase 1 impact

```text
PEOPLE-IS-100 Repository Architecture        100% (CLOSED)
PEOPLE-IS-101 Technology Decision Spec       100% (docs APPROVED; ADRs OPEN)
PEOPLE-IS-102 Module Boundary Spec              0%
PEOPLE-IS-103 Environment Architecture          0%
PEOPLE-IS-104 H-Drive Workspace Protocol        0%
PEOPLE-IS-105 GitHub and Netlify Architecture   0%

Phase 1 overall documentation progress ≈ 33%
```

## Next ready specification

```text
PEOPLE-IS-102-MODULE-BOUNDARY-SPECIFICATION-1.0
```

Parallel: begin Decision Log acceptance of high-priority ADRs (001–006, 009, 020) when ready — still **not** implementation authorization.

## Final status

```text
PEOPLE-IS-101 TECHNOLOGY DECISION SPECIFICATION: COMPLETE (DOCUMENTATION)
RECOMMENDATIONS: RECORDED AS PROPOSED
ADR-001…020: OPEN (PENDING DECISION LOG ACCEPTANCE)
APPLICATION IMPLEMENTATION: NOT AUTHORIZED
NEXT SPECIFICATION: PEOPLE-IS-102-MODULE-BOUNDARY-SPECIFICATION-1.0
```
