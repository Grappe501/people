# PEOPLE-IS-100 — REPOSITORY ARCHITECTURE

**Title:** Repository Architecture  
**Document ID:** `PEOPLE-IS-100-REPOSITORY-ARCHITECTURE-1.0`  
**Version:** 1.0  
**Status:** CLOSED / APPROVED  
**Phase:** PHASE 1 — REPOSITORY AND PLATFORM ARCHITECTURE  
**Project Root:** `H:\people`  
**Owner:** People Intake System Program  
**Technical Reviewer:** Program  
**Governance Reviewer:** Program  
**Traceability Reviewer:** Program  
**Approval Authority:** Decision Log D-061  
**Created Date:** 2026-07-26  
**Last Updated:** 2026-07-26  
**Governing Documents:** Master Build Outline; Volumes 0–13; Catalogs 00–09 (locked library); PEOPLE-IS-000…005  
**Dependencies:** ADR-001, ADR-002, ADR-003, ADR-006, ADR-009, ADR-011, ADR-020 (open — block implementation readiness, not documentation approval)  
**Implementation Authorization:** `IMPLEMENTATION NOT AUTHORIZED`

```text
DESIGN COMPLETE
APPROVED FOR DOCUMENTATION GOVERNANCE
CLOSED AT DOCUMENTATION LEVEL
APPLICATION IMPLEMENTATION NOT AUTHORIZED
IMPLEMENTATION READINESS BLOCKED BY OPEN ADRs
```

---

## 1. Purpose

Define the canonical repository architecture for the People Intake System: exclusive project root, top-level ownership, documentation vs implementation separation, module and dependency-direction rules, homes for contracts/source/tests/migrations/deployment/generated/local/temporary artifacts, GitHub and Netlify boundaries, and H-drive-only execution requirements.

A contributor must be able to inspect the repository and determine where a file belongs, which layer owns it, which modules may depend on it, whether it is canonical or generated, whether it may be committed, whether it may hold sensitive data, and whether changing it requires an approved specification.

## 2. Scope

Governs the future standalone repository rooted at `H:\people`, including documentation, contracts, source, tests, database specs/migrations, scripts, configuration templates, deployment definitions, operational artifacts, generated files, local development artifacts, GitHub source control, and Netlify packaging.

## 3. Out of Scope

Does **not** select framework, database, ORM, auth, object storage, job runtime, test framework, observability, or final hosting topology (those require ADRs). Does **not** authorize package installation, scaffolding, source creation, migrations, provider connection, deployment, environment provisioning, or production secret storage.

## 4. Governing References

* People Intake System Master Build Outline  
* Volumes 0–13  
* Catalogs **00–09** (Catalog Library locked; draft labels Catalogs 10–13 are **not** catalog authority — map to Volumes / IS phases)  
* PEOPLE-IS-000…005  
* H-Drive Protocol; Design-Before-Code Protocol  
* Gate G-10 (CLOSED)  

## 5. Definitions

| Term | Meaning |
| --- | --- |
| Canonical | Source-controlled and authoritative |
| Generated | Reproducible from canonical sources; never overrides source |
| Local-only | Required for local execution; never committed |
| Temporary | Safe to delete after processing |
| Provider-managed | Exists outside the repository (hosted DB, Netlify env, etc.) |
| Public module interface | Only surface other modules may import |

## 6. Assumptions

* Framework choice may require additional root artifacts; exceptions will be documented without abandoning logical ownership.  
* Current documentation tree under `docs/00_governance`…`docs/16_*` remains authoritative until an approved migration package remaps to the target `docs/master|volumes|…` layout.  
* Existing tooling may already use `H:\people\.tmp` and `H:\people\.npm-cache`; ADR-020 / PEOPLE-IS-104 will formalize redirection to canonical `tmp` / `local` / cache paths.  
* OS and unrelated installed apps may write outside H:\people; enforceable rule is **project-controlled** artifacts only.

## 7. Functional Requirements

| ID | Title | Description |
| --- | --- | --- |
| REQ-REPO-001 | Canonical root | All project-controlled artifacts MUST reside under `H:\people`. |
| REQ-REPO-002 | C-drive prohibition | Project scripts and configuration MUST NOT intentionally target C:\ paths. |
| REQ-REPO-003 | Documentation separation | Governing documentation MUST remain structurally separate from executable implementation. |
| REQ-REPO-004 | Directory ownership | Each top-level directory MUST have one documented purpose and owner. |
| REQ-REPO-005 | Dependency direction | Source dependencies MUST follow Presentation → Application → Domain; infrastructure implements interfaces. |
| REQ-REPO-006 | Module encapsulation | Modules MUST expose governed public interfaces and protect internals. |
| REQ-REPO-007 | Provider isolation | External provider implementations MUST remain behind adapter boundaries. |
| REQ-REPO-008 | Sensitive-data exclusion | Real production personal data MUST NOT be committed. |
| REQ-REPO-009 | Secret exclusion | Secrets MUST NOT be committed or embedded in documentation. |
| REQ-REPO-010 | Temporary artifact control | Temporary project artifacts MUST use approved H-drive paths. |
| REQ-REPO-011 | Generated distinction | Generated artifacts MUST be distinguishable from canonical sources. |
| REQ-REPO-012 | Migration governance | Migrations MUST live under `database/migrations` and trace to an approved package. |
| REQ-REPO-013 | Test separation | System-level tests and generated test outputs MUST use approved directories. |
| REQ-REPO-014 | Deployment separation | Preview, staging, and production concerns MUST remain distinguishable. |
| REQ-REPO-015 | Repository orientation | Repository MUST provide a canonical starting document (`START_HERE.md`). |
| REQ-REPO-016 | Validation | Repository MUST eventually include automated checks for architectural violations. |

Preferred language: MUST / MUST NOT / REQUIRED / SHALL / MAY.

## 8. Nonfunctional Requirements

| ID | Description |
| --- | --- |
| NFR-MAINTAINABILITY-001 | A new contributor can identify the correct destination for a new artifact via repository documentation. |
| NFR-SECURITY-001 | Architecture reduces risk of committing secrets or sensitive personal data. |
| NFR-RELIABILITY-001 | Generated and temporary files are not required to reconstruct canonical source. |
| NFR-PORTABILITY-001 | Provider-specific code is isolated enough to support replacement without redesigning the domain. |
| NFR-AUDITABILITY-001 | Implementation artifacts trace to approved specifications and packages. |
| NFR-OPERATIONS-001 | Operational evidence is retained in governed report locations, not mixed with source. |
| NFR-PERFORMANCE-001 | Organization avoids unnecessary package and build fragmentation. |

## 9. Architecture

### 9.1 Repository principles

1. One canonical project root: `H:\people`.  
2. H-drive-only project operations (source, docs, deps, caches, generated, temp, logs, test artifacts, local DBs, uploads, builds, bundles).  
3. Clear separation: governing docs / IS specs / executable implementation / generated / operational evidence / local-only.  
4. Dependency direction inward toward domain and contracts.  
5. No cross-module shortcuts (contracts, public interfaces, shared primitives, governed events only).  
6. Documentation and code remain aligned on every implementation package.

### 9.2 Canonical top-level structure (target)

```text
H:\people
├── .github
├── .netlify          (local-only; not committed)
├── app
├── config
├── contracts
├── data
├── database
├── deployment
├── docs
├── generated
├── infrastructure
├── local             (not committed)
├── logs              (not committed)
├── packages
├── public
├── scripts
├── src
├── tests
├── tmp               (not committed)
├── tools
├── .editorconfig
├── .env.example
├── .gitattributes
├── .gitignore
├── README.md
├── START_HERE.md
├── package.json
└── workspace configuration files
```

Some directories remain placeholders until an approved implementation package authorizes creation. **This specification does not authorize creating `src`, `app`, migrations, workflows, or guard code.**

### 9.3 Top-level directory ownership

| Directory | Purpose | Canonical | Commit |
| --- | --- | ---: | ---: |
| `.github` | Workflows, issue templates, repo governance | Yes | Yes |
| `.netlify` | Local Netlify runtime state | No | No |
| `app` | Framework entry points if required | Yes | Yes |
| `config` | Typed config and non-secret defaults | Yes | Yes |
| `contracts` | Provider-neutral contracts | Yes | Yes |
| `data` | Reference/fixtures/seeds | Mixed | Conditional |
| `database` | Schema, migrations, seeds, DB tooling | Yes | Yes |
| `deployment` | Deploy defs, manifests, release scripts | Yes | Yes |
| `docs` | Governing and operational documentation | Yes | Yes |
| `generated` | Reproducible generated artifacts | No | Conditional |
| `infrastructure` | IaC / provider configuration | Yes | Yes |
| `local` | Local-only state and emulators | No | No |
| `logs` | Local logs | No | No |
| `packages` | Internal workspace packages | Yes | Yes |
| `public` | Safe static public assets | Yes | Yes |
| `scripts` | Governed automation | Yes | Yes |
| `src` | Primary / framework-neutral source | Yes | Yes |
| `tests` | Cross-cutting and system tests | Yes | Yes |
| `tmp` | Temporary files on H-drive | No | No |
| `tools` | Developer tools / validators | Yes | Yes |

### 9.4 Documentation architecture (target)

```text
docs/
├── master | volumes | catalogs | implementation_specs/ | protocols | adr
├── architecture | security | operations | runbooks | testing | releases | handoffs
└── archive
```

**Governing:** `master`, `volumes`, `catalogs`, `implementation_specs`, `protocols`, `adr`.  
**Supporting:** `architecture`, `security`, `operations`, `runbooks`, `testing`, `releases`, `handoffs`.  
**Historical:** `archive` (must identify replacement when one exists).

**Current-state honesty:** Until a documentation-layout migration package is authorized, the existing Volume/Catalog tree (`docs/00_governance`, `docs/catalogs`, `docs/implementation_specs`, …) remains the live governing layout. Target folders above describe the end-state map.

IS phase folders under `implementation_specs` (already in use):

```text
000_program … 1400_authorization, decisions, matrices, reports, templates
```

Root orientation documents:

* `README.md` — high-level project explanation  
* `START_HERE.md` — mandatory orientation for humans, Cursor, auditors (root, authorization, indexes, allowed/prohibited actions, next package)

### 9.5 Contract architecture

```text
contracts/
├── api | entities | errors | events | integrations | jobs
├── notifications | permissions | schemas | states | validation
```

Contracts MUST be provider-neutral, versioned, documented, machine-readable where practical, traceable, secret-free. Executable generated clients MUST NOT live in canonical contract dirs unless explicitly approved.

### 9.6 Application source architecture

Logical layers (framework may use `app`, `src`, or both):

```text
src/
├── application | domain | infrastructure | integrations
├── presentation | shared | workers
```

| Layer | Owns | May depend on | Must not |
| --- | --- | --- | --- |
| `domain` | Entities, VOs, state rules, invariants, domain events | nothing external | UI, HTTP, DB client, providers |
| `application` | Use cases, orchestration, permissions, commands/queries | domain, contracts, shared | provider impl when adapter required |
| `infrastructure` | Repos, adapters, telemetry, config load | implements app/domain/contracts | leak into domain |
| `integrations` | External-system adapters + anti-corruption | application contracts | leak provider types app-wide |
| `presentation` | Routes, UI, view models, a11y, error presentation | application services | DB, audit writes, state mutation, provider SDKs, inventing permission policy |
| `workers` | Job handlers, schedulers, consumers | application services | duplicate business rules |
| `shared` | Cross-cutting primitives only | — | feature business logic / dumping ground |

Domain families (consistent names across layers): identity, users, roles, permissions, invitations, batches, uploads, pages, queues, claims, drafts, transcriptions, normalization, matching, resolution, promotion, notifications, audit, reports, exports, retention, operations.

### 9.7 Internal packages

Optional under `packages/` (`contracts`, `domain`, `configuration`, `observability`, `test-support`, `ui`, `validation`). Create only with clear owner, stable public API, multiple consumers, independent validation, no cycles. Premature fragmentation is prohibited.

### 9.8 Database / tests / scripts / tools / config / data / public

**Database** (`database/`): `schema`, `migrations`, `seeds`, `fixtures`, `queries`, `functions`, `policies`, `validation`, `rollback`, `reports`. No migration before Phase 3 approval + package authorization. Migrations immutable after production apply; include verification and rollback/compensation; no workstation-specific paths.

**Tests** (`tests/`): `unit`, `component`, `repository`, `service`, `api`, `workflow`, `integration`, `end_to_end`, `security`, `accessibility`, `performance`, `recovery`, `operations`, `fixtures`, `factories`, `mocks`, `reports`. Co-located unit tests MAY exist if framework benefits; convention locked in PEOPLE-IS-1100. Generated output → `generated/tests` or `local/tests`.

**Scripts** (`scripts/`): `setup`, `validation`, `development`, `database`, `testing`, `deployment`, `operations`, `documentation`, `maintenance`. Fail clearly; validate root and H-drive; no secrets; meaningful exit codes; dry-run where practical.

**Tools** (`tools/`): `repository_guard`, documentation/traceability/contract/migration validators, `secret_scanner`, `package_reporter`. Not authorized until a package allows them.

**Config** (`config/`): `schema`, `defaults`, `environments`, `features`, `documentation`. No secrets; `.env.example` names only; local `.env` ignored. Exact implementation: PEOPLE-IS-102.

**Data** (`data/`): `reference`, `seed_definitions`, `safe_fixtures`, `dictionaries`, `imports`, `examples`. Committed data MUST be synthetic/public/non-sensitive. Prohibited in Git: production exports, voter files, real uploads/transcriptions/PII/credentials/provider PII payloads/unrestricted audits/real users.

**Public** (`public/`): logos, icons, licensed fonts, public help, robots, safe manifests. Never intake images or protected content.

### 9.9 Generated / local / tmp / logs

| Root | Classification | Commit |
| --- | --- | --- |
| `generated/` (`api`, `contracts`, `database`, `documentation`, `reports`, `tests`, `types`) | GENERATED | Conditional |
| `local/` (`database`, `storage`, `queues`, `emulators`, `sessions`, `uploads`, `backups`) | LOCAL_ONLY | No |
| `tmp/` (`build`, `cache`, `downloads`, `extraction`, `processing`, `testing`, `uploads`) | TEMPORARY | No |
| `logs/` (`application`, `database`, `development`, `jobs`, `operations`, `scripts`, `tests`) | LOCAL_ONLY | No |

Generated artifacts MUST document source, command, version, commit policy, and authority (never authoritative over source). Do not manually edit generated files.

### 9.10 Deployment and infrastructure

**Deployment** (`deployment/`): `netlify`, `environments`, `manifests`, `verification`, `rollback`, `release`, `reports`. Distinguish Preview / Staging / Production (separate config, secrets, data, evidence, authorization). Preview success ≠ production authorization.

Netlify source-controlled artifacts under `deployment/netlify` (or framework-required root path). `.netlify` is non-canonical. Netlify is not source of truth for schemas, env values, docs, release history, or migration state. GitHub remains the engineering record.

**Infrastructure** (`infrastructure/`): `database`, `storage`, `identity`, `networking`, `queues`, `observability`, `security`, `environments`. Reviewable, versioned, secret-free, environment-aware, rollback-conscious. **No provisioning under this specification.**

### 9.11 GitHub and Netlify

Recommended GitHub repo name: `people-intake-system`. Local clone MUST be `H:\people`.

Initial branch model: `main`, `feature/*`, `fix/*`, `docs/*`, `release/*`. Final branch policy: PEOPLE-IS-1202.

Commit messages SHOULD include package/spec ID, e.g. `docs(people-is-100): define canonical repository architecture`.

Future `.gitignore` MUST exclude at minimum: `.env` (except `.env.example`), `node_modules`, `.netlify`, `local`, `logs`, `tmp`, coverage/test-results/playwright-report, unapproved generated output, local DBs/uploads, provider/build caches.

Netlify: dedicated site, env vars, DB/storage credentials, domain. MUST NOT inherit secrets from unrelated SOSWebsite apps. Netlify may host app/previews/serverless/logs/env injection/rollback; MUST NOT be assumed to provide durable queues, object storage, or long-running jobs without separate ADRs.

### 9.12 Dependency direction

```text
Presentation → Application → Domain
Workers → Application → Domain
Infrastructure implements Application/Domain contracts
Integrations implement Application contracts
```

**Forbidden:** Domain→Presentation/Infrastructure/Provider SDK; Application→UI/route objects; Presentation→DB client/Provider SDK; Worker→direct DB mutation bypassing services; Integration→UI; Shared→feature business logic. Circular dependencies prohibited — use orchestration, shared contract, domain event, or inversion.

### 9.13 Module public interfaces

```text
<module>/index | contracts | internal | tests
```

Deep imports into another module’s internals are prohibited.

### 9.14 Path classification

`CANONICAL | GENERATED | LOCAL_ONLY | TEMPORARY | PROVIDER_MANAGED | ARCHIVED`

### 9.15 H-drive enforcement (design requirements)

REQ-REPO-001 guard MUST verify active project directory resolves under `H:\people` before package install, build, test, migration, codegen, deployment packaging, large-file processing.

Redirect TEMP/TMP, package/framework/browser/compiler caches, build output, DB files, upload processing to H-drive where supported (exact vars: ADR-020 + PEOPLE-IS-104).

**Failure:** stop before write; identify path; explain correction; non-zero exit; no C-drive fallback.

**Honest OS limit:** project cannot prevent unrelated OS/app writes to C:\. Enforceable rule: no project-controlled or project-configurable artifact may intentionally write outside `H:\people`.

## 10. Data Contracts

NOT_APPLICABLE for runtime entities. Path ownership and classification rules in §9 are the data-placement contracts for repository artifacts.

## 11. Interface Contracts

Future module public interfaces (§9.13). Repository indexes (§34 in package source): `START_HERE.md`, `docs/_index.md`, `docs/implementation_specs/_index.md`, `contracts/_index.md`, `database/_index.md`, `scripts/_index.md`, `tests/_index.md`, `deployment/_index.md`.

## 12. State Behavior

NOT_APPLICABLE (no runtime resource state machine). Authorization states remain those in PEOPLE-IS-000.

## 13. Permission Behavior

NOT_APPLICABLE for runtime permissions. Repository change authority: documentation vs implementation packages; production deploy requires separate authorization.

## 14. Error and Recovery Behavior

Future tooling SHOULD define:

```text
INVALID_PROJECT_ROOT | FORBIDDEN_WRITE_TARGET | UNAPPROVED_TOP_LEVEL_DIRECTORY
FORBIDDEN_DEPENDENCY | CIRCULAR_DEPENDENCY | SECRET_DETECTED | SENSITIVE_FILE_DETECTED
UNAPPROVED_IMPLEMENTATION_ARTIFACT | MISSING_DOCUMENT_INDEX | BROKEN_TRACEABILITY_REFERENCE
GENERATED_FILE_MODIFIED
```

On violation: stop before destructive action; report path; cite rule; recommend correction; no silent drive relocation.

## 15. Audit Requirements

Future repository-health report SHOULD include: branch, working tree, untracked files, unapproved directories, documentation/traceability status, secret-scan, dependency-direction, migration/test/build status, H-drive boundary, implementation authorization.

## 16. Notification Requirements

NOT_APPLICABLE (no runtime notifications). Governance notifications remain Decision Log / open-issue register.

## 17. Background Processing

NOT_APPLICABLE for runtime jobs. Workers layer location defined in §9.6 for when authorized.

## 18. Security and Privacy

Secrets MUST NOT appear in Git history, markdown, screenshots, committed env files, sample payloads, logs, fixtures, issue templates, or generated reports. Variable names, descriptions, placeholders, provisioning/rotation instructions MAY appear.

Repository is a security boundary: secret/large-file/sensitive-pattern scanning; ignored local-data dirs; protected branches; dependency review; code owners where appropriate; restricted production access; deploy-change audit.

Sensitive local test artifacts (if ever authorized) stay under ignored paths with source auth, access control, retention, destruction, classification, audit.

## 19. Data Classification and Retention

Committed repository data: PUBLIC or INTERNAL synthetic/reference only. RESTRICTED/SYSTEM_SECRET material MUST NOT be committed. Local sensitive artifacts follow Catalog 8 principles when authorized. Production personal data is provider-managed or ignored local — never Git.

## 20. Observability

Future tooling SHOULD log: validation start, repository root, category, pass/fail, violation path, package ID, correlation ID, summary — never secret values or sensitive file contents. Production logging: PEOPLE-IS-1000.

## 21. Testing

Eventually: unit (path classification/normalization, root validation, ignore rules, naming); integration (correct/incorrect root commands, cache/tmp redirection, secret scanner, dependency validator); workflow (docs-only / app / migration / deploy / rollback packages); failure (C-drive target, secret commit, unapproved top-level, deep import, circular dependency, sensitive file in public).

## 22. Acceptance Criteria

| ID | Given / When / Then | Blocking |
| --- | --- | --- |
| AC-REPO-001 | Contributor reads `START_HERE.md` → identifies root, authorization, governing docs, next package | Yes for orientation completeness |
| AC-REPO-002 | New artifact proposed → one canonical destination | Yes |
| AC-REPO-003 | Command would write outside H:\people → guard stops before write | Yes before tooling auth |
| AC-REPO-004 | Presentation needs data → uses application service, not DB | Yes for app packages |
| AC-REPO-005 | Provider replaced → domain/presentation avoid provider-specific rewrites | Yes for integrations |
| AC-REPO-006 | Generated artifact → source and generation process identifiable | Yes |
| AC-REPO-007 | Real PII in tracked path → validation rejects/flags blocking | Yes |
| AC-REPO-008 | Migration proposed → under `database/migrations` with package ID | Yes for Phase 3+ |
| AC-REPO-009 | New top-level folder → ownership, purpose, approval required | Yes |
| AC-REPO-010 | Local Netlify state → non-canonical, excluded from Git | Yes |

## 23. Open Decisions

| Decision | Status | Blocks |
| --- | --- | --- |
| ADR-001 Application Framework | OPEN | Implementation readiness |
| ADR-002 Database Provider | OPEN | Phase 3 / coding |
| ADR-003 ORM / Data Access | OPEN | Phase 3 / coding |
| ADR-006 Background Job Runtime | OPEN | Phase 7 |
| ADR-009 Hosting and Deployment | OPEN | Phase 12 |
| ADR-011 Test Framework | OPEN | Phase 11 |
| ADR-020 H-Drive Enforcement Mechanism | OPEN | Tooling / package install |
| ISSUE-HDRIVE-001 / ISSUE-PLATFORM-001 | OPEN | See open-issue register |

## 24. Risks

| ID | Description | Mitigation |
| --- | --- | --- |
| RISK-REPO-001 | Framework-driven structure conflict | Allow required root artifacts; document exceptions; preserve logical ownership |
| RISK-REPO-002 | Third-party C-drive caches | Redirect supported paths; document unavoidable OS behavior honestly |
| RISK-REPO-003 | Shared-folder overgrowth | Require ownership + multi-module justification |
| RISK-REPO-004 | Premature package fragmentation | Create packages only when reuse and ownership proven |
| RISK-REPO-005 | Documentation drift | Automated validation + package closure docs updates |
| RISK-REPO-006 | Sensitive files in Git history | Pre-commit and CI scanning before commit |

## 25. Dependencies

* Phase 0 governance APPROVED (D-060)  
* Open ADRs listed in §23 for **implementation readiness**  
* Catalog 09 Traceability for system-wide matrix closure (partial dependency)  
* PEOPLE-IS-101…105 for Phase 1 completion  

## 26. Traceability Matrix

| Requirement | Governing Source | Future Implementation | Verification | Status |
| --- | --- | --- | --- | --- |
| REQ-REPO-001 | IS-000 H-drive | Repository guard | Root validation test | FULLY_MAPPED (design) |
| REQ-REPO-002 | IS-000 boundary | Env/cache controls | Forbidden-target test | FULLY_MAPPED (design) |
| REQ-REPO-003 | Volume 13 / IS-100 | Documentation structure | Index audit | FULLY_MAPPED (design) |
| REQ-REPO-004 | IS-100 | Repository map | Ownership validation | FULLY_MAPPED (design) |
| REQ-REPO-005 | Volume 13 / IS-100 | Dependency rules | Import-boundary tests | FULLY_MAPPED (design) |
| REQ-REPO-006 | Volume 13 / IS-100 | Module public interfaces | Deep-import test | FULLY_MAPPED (design) |
| REQ-REPO-007 | Volume 10–13 / IS-100 | Integration adapters | Provider replacement test | FULLY_MAPPED (design) |
| REQ-REPO-008 | Catalog 8 | Git and data controls | Sensitive-file scan | FULLY_MAPPED (design) |
| REQ-REPO-009 | Catalog 4 & 8 | Secret management | Secret scan | FULLY_MAPPED (design) |
| REQ-REPO-010 | IS-100 | tmp/local/log paths | File-location test | FULLY_MAPPED (design) |
| REQ-REPO-011 | Volume 13 / IS-100 | generated metadata | Generated-artifact audit | FULLY_MAPPED (design) |
| REQ-REPO-012 | Future IS-305 | migration governance | Migration validation | PARTIALLY_MAPPED |
| REQ-REPO-013 | Volume 5 / future IS-1100 | test architecture | Test-path validation | PARTIALLY_MAPPED |
| REQ-REPO-014 | Volume 12 / future IS-1200 | deployment structure | Environment-separation review | PARTIALLY_MAPPED |
| REQ-REPO-015 | Catalog/Vol 13 / IS-100 | START_HERE.md | Orientation review | FULLY_MAPPED (design) |
| REQ-REPO-016 | Volume 5 / IS-100 | validation tooling | Repository-health gate | PARTIALLY_MAPPED |

**Note:** Traceability sources that user drafts labeled “Catalog 10–13” are mapped to **Volumes / IS phases** because Catalog Library is locked at **0–9**.

## 27. Implementation Boundary

**Authorized now (documentation):** this specification; indexes/registers/progress updates; orientation docs such as `START_HERE.md`.

**Not authorized:**

```text
src | app | database migrations | package dependencies | GitHub workflows
Netlify configuration | repository guard code | test code | provider adapters
deployment scripts | infrastructure provisioning
```

A later implementation package MUST define exact files, allowed/forbidden paths, selected technology, validation commands, rollback, commit, and deployment behavior.

## 28. Revision History

| Version | Date | Change | Author | Reviewer | Approval |
| --- | --- | --- | --- | --- | --- |
| 1.0 | 2026-07-26 | Initial repository architecture APPROVED for documentation governance | Program | Program | D-061 |

---

## Phase 1 readiness impact

```text
PEOPLE-IS-100 Repository Architecture        100%
PEOPLE-IS-101 Technology Decision Spec         0%
PEOPLE-IS-102 Module Boundary Spec              0%
PEOPLE-IS-103 Environment Architecture          0%
PEOPLE-IS-104 H-Drive Workspace Protocol        0%
PEOPLE-IS-105 GitHub and Netlify Architecture   0%

Phase 1 overall documentation progress ≈ 17%
```

## Completion gate

```text
STRUCTURALLY_COMPLETE
TECHNICALLY_REVIEWED AT GOVERNANCE LEVEL
TRACEABILITY_COMPLETE (design-level; system matrix still PARTIAL pending Catalog 09)
APPROVED
NOT YET IMPLEMENTATION READY
```

Reason not implementation-ready: required technology ADRs and H-drive enforcement design remain unresolved.

## Next ready specification

```text
PEOPLE-IS-101-TECHNOLOGY-DECISION-SPECIFICATION-1.0
```

Also continue Catalog Library: `PEOPLE-CATALOG-09-TRACEABILITY-1.0`.

## Final status

```text
PEOPLE-IS-100 REPOSITORY ARCHITECTURE: CLOSED
DOCUMENTATION STATUS: APPROVED FOR DOCUMENTATION GOVERNANCE (D-061)
APPLICATION IMPLEMENTATION: NOT AUTHORIZED
IMPLEMENTATION READINESS: BLOCKED BY OPEN ADRs
CANONICAL PROJECT ROOT: H:\people
COMPLETION REPORT: docs/implementation_specs/reports/PEOPLE_IS_100_COMPLETION_REPORT.md
NEXT BUILD (DEPENDENCY ORDER):
  1. PEOPLE-CATALOG-09-TRACEABILITY-1.0
  2. PEOPLE-IS-101-TECHNOLOGY-DECISION-SPECIFICATION-1.0
```
