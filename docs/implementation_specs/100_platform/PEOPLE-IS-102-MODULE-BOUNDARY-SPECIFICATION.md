# PEOPLE-IS-102 — MODULE BOUNDARY SPECIFICATION

**Title:** Module Boundary Specification  
**Document ID:** `PEOPLE-IS-102-MODULE-BOUNDARY-SPECIFICATION-1.0`  
**Version:** 1.0  
**Status:** APPROVED  
**Phase:** PHASE 1 — REPOSITORY AND PLATFORM ARCHITECTURE  
**Project Root:** `H:\people`  
**Owner:** People Intake System Program (Chief Systems Engineer)  
**Technical Reviewer:** Program  
**Governance Reviewer:** Program  
**Traceability Reviewer:** Program  
**Approval Authority:** Decision Log D-064  
**Created Date:** 2026-07-26  
**Last Updated:** 2026-07-26  
**Governing Documents:** Constitution; Volumes 0–13; Catalogs 00–09; PEOPLE-IS-000…005; PEOPLE-IS-100; PEOPLE-IS-101  
**Dependencies:** IS-100 CLOSED (D-061); IS-101 APPROVED (D-063); ADR-001…020 OPEN (boundaries remain technology-neutral where required)  
**Implementation Authorization:** `IMPLEMENTATION NOT AUTHORIZED`

```text
DESIGN COMPLETE
APPROVED FOR DOCUMENTATION GOVERNANCE
ARCHITECTURAL RULEBOOK FOR FUTURE PACKAGES
APPLICATION IMPLEMENTATION NOT AUTHORIZED
```

**Companion artifacts**

| Artifact | Path |
| --- | --- |
| Module dependency matrix | `docs/implementation_specs/matrices/MODULE_DEPENDENCY_MATRIX.md` |
| Module ownership matrix | `docs/implementation_specs/matrices/MODULE_OWNERSHIP_MATRIX.md` |
| Boundary validation rules | `docs/implementation_specs/matrices/MODULE_BOUNDARY_VALIDATION_RULES.md` |
| Interface contract index | `docs/implementation_specs/matrices/MODULE_INTERFACE_CONTRACT_INDEX.md` |
| Completion report | `docs/implementation_specs/reports/PEOPLE_IS_102_COMPLETION_REPORT.md` |

---

## 1. Purpose

Establish permanent, governable contracts between modules so that every future capability can answer:

1. Which module owns it?  
2. Which modules may call it?  
3. Which modules may not?  
4. Which contracts must be updated?  
5. Which tests are required?  
6. Which implementation package the work belongs to?

This is the architectural bridge between repository layout (IS-100), technology recommendations (IS-101), and every implementation package Burt will execute.

## 2. Scope

Canonical module inventory; purpose/scope; ownership; public vs internal surfaces; allowed/forbidden dependencies; shared contracts and DTO rules; event pub/sub ownership; service lifecycle; database/API/job/permission/validation/audit/notification/error/test ownership; versioning/compatibility; extensibility; anti-patterns; boundary validation rules.

## 3. Out of Scope

* Creating `src/`, `app/`, or package code  
* Accepting open ADRs  
* Exact TypeScript file trees for a chosen framework (framework folders must map to these logical modules)  
* Full per-endpoint inventory (API IDs expand via Volume 10 / IS-500; this doc assigns **ownership rules**)  
* Full table DDL (Volume 09 / IS-300; this doc assigns **entity/table owners**)  

## 4. Governing References

PEOPLE-IS-100 §§9.6–9.13; PEOPLE-IS-101 (technology-neutral boundaries); PEOPLE-IS-002 (IDs); PEOPLE-IS-003 (traceability); Catalogs 1–8 (operational language owners); Catalog 09 (linkage); Volumes 8–13.

## 5. Definitions

| Term | Meaning |
| --- | --- |
| Module | Named capability unit with one owner, public interface, and internal implementation |
| Public interface | Only surface other modules may import (`index` / `contracts`) |
| Internal | Implementation files other modules MUST NOT import |
| Layer | Cross-cutting architectural tier (presentation, application, domain, infrastructure, integrations, workers, shared) |
| Capability module | Domain-family module spanning layers under one ownership name (e.g. `claims`) |
| Owner | Sole authority to change business rules for a capability |
| Consumer | Module allowed to call another’s public interface |
| Contract | Versioned, provider-neutral schema/interface in `contracts/` or module `contracts/` |
| Deep import | Import into another module’s `internal` path — **forbidden** |

## 6. Assumptions

* Logical modules map into IS-100 `src/{layer}/{capability}` (or framework-equivalent) without changing ownership.  
* Until ADR-001 is accepted, path examples remain logical, not framework-literal.  
* Catalogs 1–8 remain authoritative for states, errors, permissions, audit, config, notifications, jobs, retention language.  
* Shared must not become a dumping ground (IS-100).  

## 7. Functional Requirements

| ID | Description |
| --- | --- |
| REQ-MOD-001 | Every business capability MUST have exactly one owning module. |
| REQ-MOD-002 | Every module MUST define a public interface and protect internals. |
| REQ-MOD-003 | Dependencies MUST follow approved layer and module direction rules. |
| REQ-MOD-004 | Circular module dependencies are PROHIBITED. |
| REQ-MOD-005 | UI/presentation MUST NOT bypass application services. |
| REQ-MOD-006 | Domain MUST NOT depend on infrastructure, providers, or presentation. |
| REQ-MOD-007 | Cross-module communication MUST use public interfaces or documented domain/application events. |
| REQ-MOD-008 | Each API endpoint ID MUST belong to exactly one owning module. |
| REQ-MOD-009 | Each durable entity/table MUST have exactly one owning module. |
| REQ-MOD-010 | Each Catalog 7 job MUST have exactly one owning module (handler via workers → application). |
| REQ-MOD-011 | Permission policy definitions remain Catalog 5; enforcement checks live in application of the owning capability. |
| REQ-MOD-012 | Audit event emission for a state mutation is owned by the mutating capability’s application service (Catalog 3 names). |
| REQ-MOD-013 | Notification triggers are owned by the capability that detects the condition; delivery adapter is infrastructure/integrations. |
| REQ-MOD-014 | Canonical errors are Catalog 2; modules MUST NOT invent production error codes outside catalog amendment. |
| REQ-MOD-015 | Validation of capability inputs is owned by the capability’s application layer (shared may hold primitives only). |
| REQ-MOD-016 | Tests for a module’s rules MUST be owned by that module or mapped in `tests/` with clear owner metadata. |
| REQ-MOD-017 | No shared mutable state across module boundaries. |
| REQ-MOD-018 | Future modules require IS-102 amendment (or successor) before implementation packages use them. |

## 8. Nonfunctional Requirements

| ID | Description |
| --- | --- |
| NFR-MOD-MAINTAIN-001 | A new feature’s owner module is identifiable from matrices without tribal knowledge. |
| NFR-MOD-SEC-001 | Permission and audit ownership prevent authorization/audit bypass via UI or workers. |
| NFR-MOD-PORT-001 | Provider SDKs remain behind integrations/infrastructure adapters. |
| NFR-MOD-EVOLVE-001 | Public contracts version compatibility rules prevent silent breaking changes. |

## 9. Architecture — Module Model

### 9.1 Engineering doctrine (enforced)

1. Single responsibility at module level.  
2. One authoritative owner for every business capability.  
3. No circular dependencies.  
4. No shared mutable state across module boundaries.  
5. Public contracts only; no deep imports.  
6. Infrastructure depends on abstractions, not feature modules’ internals.  
7. UI never bypasses application services.  
8. Cross-module communication only through approved interfaces or documented events.  

### 9.2 Two-axis model

**Axis A — Layers** (dependency direction):

```text
presentation → application → domain
workers      → application → domain
infrastructure implements application/domain contracts
integrations  implement application contracts
shared ← used by all; must not own feature rules
```

**Axis B — Capability modules** (ownership names reused across layers):

```text
identity | users | roles | permissions | invitations
batches | uploads | pages | queues | claims
drafts | transcriptions | normalization
matching | resolution | promotion
notifications | audit | reports | exports
retention | operations | config | observability
```

A capability’s code appears under matching folders in domain/application/infrastructure/presentation/workers as needed. **Ownership does not split** because files live in multiple layers.

### 9.3 Canonical module inventory

| Module ID | Name | Type | Purpose |
| --- | --- | --- | --- |
| MOD-LAYER-PRES | Presentation Layer | Layer | HTTP/UI entry, view models, a11y, user-facing errors |
| MOD-LAYER-APP | Application Layer | Layer | Use cases, orchestration, permission checks, transactions |
| MOD-LAYER-DOM | Domain Layer | Layer | Entities, invariants, state rules, domain events |
| MOD-LAYER-INFRA | Infrastructure Layer | Layer | Repositories, DB/queue/storage/telemetry adapters |
| MOD-LAYER-INT | Integrations Layer | Layer | External systems (auth IdP, AI, canonical person, email) |
| MOD-LAYER-WORK | Workers Layer | Layer | Job/schedule entrypoints invoking application services |
| MOD-LAYER-SHARED | Shared Layer | Layer | Stable non-domain primitives only |
| MOD-IDENTITY | Identity | Capability | Principal identity binding (provider-neutral) |
| MOD-USERS | Users | Capability | Application user lifecycle |
| MOD-ROLES | Roles | Capability | Role assignments (Catalog 5 roles) |
| MOD-PERMISSIONS | Permissions | Capability | Enforcement helpers; Catalog 5 remains key authority |
| MOD-INVITATIONS | Invitations | Capability | Invite/onboard flows |
| MOD-BATCHES | Batches | Capability | Batch lifecycle |
| MOD-UPLOADS | Uploads | Capability | Upload session/initiation |
| MOD-PAGES | Pages | Capability | Page/image page model |
| MOD-QUEUES | Queues | Capability | Work queue visibility/ordering |
| MOD-CLAIMS | Claims | Capability | Page claim acquire/release/expire |
| MOD-DRAFTS | Drafts | Capability | Draft transcription persistence |
| MOD-TRANSCRIPTIONS | Transcriptions | Capability | Transcription workflow |
| MOD-NORMALIZATION | Normalization | Capability | Field normalization rules |
| MOD-MATCHING | Matching | Capability | Candidate generation/scoring |
| MOD-RESOLUTION | Resolution | Capability | Match decision recording |
| MOD-PROMOTION | Promotion | Capability | Promotion request/approve/execute boundary |
| MOD-NOTIFICATIONS | Notifications | Capability | Trigger ownership for Catalog 6 events |
| MOD-AUDIT | Audit | Capability | Audit write/query services (Catalog 3 names) |
| MOD-REPORTS | Reports | Capability | Operational reporting reads |
| MOD-EXPORTS | Exports | Capability | Controlled export generation |
| MOD-RETENTION | Retention | Capability | Retention/hold/destruction orchestration |
| MOD-OPERATIONS | Operations | Capability | Admin/ops tooling surfaces |
| MOD-CONFIG | Configuration | Capability | Typed config loading (Catalog 4 keys) |
| MOD-OBSERVABILITY | Observability | Capability | Correlation, metrics hooks, health |

### 9.4 Public interface pattern (every module)

```text
<module>/
  index          ← public exports only
  contracts/     ← DTOs, ports, event payloads
  internal/      ← private implementation
  tests/         ← optional co-located unit tests
```

Consumers MAY import only `index` / `contracts`. Deep imports into `internal` are **REJECTED** by boundary validation.

### 9.5 Dependency direction (layers)

| From \ To | PRES | APP | DOM | INFRA | INT | WORK | SHARED |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRES | — | ALLOW | FORBID | FORBID | FORBID | FORBID | ALLOW |
| APP | FORBID | — | ALLOW | PORT only | PORT only | FORBID | ALLOW |
| DOM | FORBID | FORBID | — | FORBID | FORBID | FORBID | ALLOW* |
| INFRA | FORBID | impl ports | impl ports | — | ALLOW** | FORBID | ALLOW |
| INT | FORBID | impl ports | FORBID | ALLOW** | — | FORBID | ALLOW |
| WORK | FORBID | ALLOW | FORBID | FORBID | FORBID | — | ALLOW |
| SHARED | FORBID | FORBID | FORBID | FORBID | FORBID | FORBID | — |

\* Shared helpers only; no domain types owned by capabilities.  
\*\* Infrastructure/integrations may share low-level clients only through adapters, not feature internals.

### 9.6 Capability dependency rules (summary)

* Capabilities collaborate through **application services** and **domain events**, not by importing another capability’s repositories.  
* `presentation/{X}` may call only `application/{X}` and approved read models — not `application/{Y}` internals. Cross-capability UI flows call an orchestrating application service in the owning workflow module.  
* `matching` MUST NOT write promotion outcomes; `promotion` owns promotion.  
* `claims` owns claim exclusivity; queues/pages must not invent parallel claim stores.  
* `audit` provides write/query ports; other modules MUST NOT write raw audit rows bypassing audit service.  
* `permissions` does not redefine Catalog 5 keys; it enforces them.  

Full matrix: `MODULE_DEPENDENCY_MATRIX.md`.

### 9.7 Event ownership

| Rule | Requirement |
| --- | --- |
| Publication | Only the owning capability’s domain/application layer may publish that capability’s domain events |
| Payload | Defined in owner `contracts/` and/or `contracts/events/` |
| Subscription | Consumers react via application handlers; MUST NOT mutate owner’s aggregates directly |
| Naming | Align with Catalog 3 where the event is an audit-relevant fact; domain events may be finer-grained |

### 9.8 Database ownership

| Rule | Requirement |
| --- | --- |
| One owner | Each entity/table has one owning capability |
| Writes | Only owner’s infrastructure repository (invoked by owner application) may write |
| Reads | Other modules MAY read via owner-published query ports / read DTOs — not ad hoc SQL into foreign tables |
| Migrations | Migration files cite owning module + implementation package |

Seed ownership map (from Volume 09 table set; expandable by amendment):

| Entity / Table (known) | Owner module |
| --- | --- |
| `app_users` | MOD-USERS |
| `intake_batches` | MOD-BATCHES |
| `intake_pages` / `intake_source_images` | MOD-PAGES / MOD-UPLOADS (images owned with pages/uploads split: pages metadata → MOD-PAGES; binary object refs → MOD-UPLOADS) |
| `intake_page_claims` | MOD-CLAIMS |
| `intake_entries` (drafts/entries) | MOD-DRAFTS / MOD-TRANSCRIPTIONS |
| `intake_match_candidates` | MOD-MATCHING |
| `intake_match_resolutions` | MOD-RESOLUTION |
| `intake_promotion_requests` | MOD-PROMOTION |
| `intake_audit_events` | MOD-AUDIT |

Exact column ownership expands in IS-300; disputes → open issue, not silent dual-write.

### 9.9 API ownership

| Rule | Requirement |
| --- | --- |
| One owner | Each `API-*` ID belongs to one capability |
| Handlers | Live in presentation of that capability; call that capability’s application service |
| Versioning | Route changes do not change API ID (IS-002) |
| No UI inventing APIs | New endpoints require owning module + contract update |

### 9.10 Job ownership

| Rule | Requirement |
| --- | --- |
| Catalog 7 | Job canonical name owned as catalog language |
| Handler | `workers` entry → owning capability `application` service |
| No business logic in worker shell | Worker is transport only |

Example (seeded): claim expiration check → MOD-CLAIMS application via workers.

### 9.11 Permission / validation / audit / notification / error ownership

| Concern | Authority | Runtime owner |
| --- | --- | --- |
| Permission keys | Catalog 5 | Enforcement in owning capability application |
| Validation schemas | contracts + capability application | Shared primitives only for non-domain parsing |
| Audit event names | Catalog 3 | Emission via MOD-AUDIT ports from mutating capability |
| Notification names | Catalog 6 | Trigger in detecting capability; send via integrations adapter |
| Error codes | Catalog 2 | Mapped at application/presentation boundary; no inventing |

### 9.12 Test ownership

| Test type | Owner |
| --- | --- |
| Unit (domain/application rules) | Owning capability |
| Repository | Owning capability + MOD-LAYER-INFRA |
| API/workflow | Owning capability (+ orchestrator if cross-capability) |
| Boundary/import rules | Platform tools / IS-102 validation suite (future) |
| E2E | Mapped to primary capability under test; must list secondary modules |

### 9.13 Versioning and compatibility

* Public contracts use semantic intent: additive changes preferred.  
* Breaking contract changes REQUIRE CHANGE-* + consumer impact analysis (IS-003).  
* Modules MUST NOT rely on another module’s internal types.  
* Deprecated public exports remain until consumers migrate; mark `DEPRECATED` in contract index.  

### 9.14 Extensibility

* New capability module → amend IS-102 inventory + matrices + Decision Log if material.  
* New dependency edge → update dependency matrix before coding.  
* Provider replacement → only integrations/infrastructure change; domain/application contracts stable (IS-100 REQ-REPO-007).  

## 10. Data Contracts

Module DTOs and ports are listed in `MODULE_INTERFACE_CONTRACT_INDEX.md`. Runtime entity fields remain Volume 09 / field dictionary.

## 11. Interface Contracts

See interface contract index. Pattern: `CONTRACT-<MODULE>-<NAME>` for module ports; reuse `API-*`, `ENTITY-*`, `JOB-*`, etc. from IS-002.

## 12. State Behavior

State machines remain Catalog 1. Owning capability’s domain layer owns transition rules for its resources; other modules MUST NOT apply illegal transitions.

## 13. Permission Behavior

Catalog 5 keys; application of owning capability performs checks before privileged operations. Presentation MUST NOT invent authorization.

## 14. Error and Recovery Behavior

Boundary violations surface as repository-tooling / review failures today; future automated checker SHOULD emit:

```text
FORBIDDEN_DEPENDENCY | CIRCULAR_DEPENDENCY | DEEP_IMPORT
OWNERSHIP_CONFLICT | CONTRACT_MISSING | SHARED_MUTATION
UI_BYPASS_SERVICE | FOREIGN_TABLE_WRITE
```

## 15. Audit Requirements

State-mutating application services MUST emit Catalog 3 events (or documented exception). MOD-AUDIT owns persistence port.

## 16. Notification Requirements

Detecting capability owns trigger; MOD-NOTIFICATIONS/integrations own delivery mechanics.

## 17. Background Processing

MOD-LAYER-WORK invokes application only. Job ownership per §9.10.

## 18. Security and Privacy

Integrations hold provider SDKs. No PII in shared logs. Exports/reports modules enforce classification (Catalog 8).

## 19. Data Classification and Retention

MOD-RETENTION orchestrates Catalog 8 policies; data-holding modules must expose retention hooks, not private delete paths that bypass policy.

## 20. Observability

MOD-OBSERVABILITY defines correlation helpers; capabilities emit safe structured events without secrets.

## 21. Testing

Boundary tests (future package) MUST cover forbidden imports, UI bypass, foreign writes, and circular graphs. Until tooling exists, package reviews use `MODULE_BOUNDARY_VALIDATION_RULES.md` as checklist.

## 22. Acceptance Criteria

| ID | Given / When / Then |
| --- | --- |
| AC-MOD-001 | Given a new feature, when ownership matrix is consulted, then exactly one owning module is identified |
| AC-MOD-002 | Given module A needs module B, when dependency matrix is checked, then the edge is ALLOW or the design is rejected |
| AC-MOD-003 | Given a presentation change needing persistence, when reviewed, then it calls application services only |
| AC-MOD-004 | Given a new API endpoint, when registered, then one owning module and contract entry exist |
| AC-MOD-005 | Given a new table, when registered, then one owning module is assigned |
| AC-MOD-006 | Given an import into `internal/`, when boundary validation runs, then it fails |
| AC-MOD-007 | Given a circular dependency, when validation runs, then it fails |
| AC-MOD-008 | Given Burt implements a package, when reading IS-102 matrices, then owner/caller/forbidden/contracts/tests/package mapping are determinable |

## 23. Open Decisions

| ID | Question | Status |
| --- | --- | --- |
| ADR-001 | Exact folder mapping under Next.js `app/` vs `src/` | OPEN — logical modules still bind |
| ISSUE-MOD-001 | Precise split of `intake_entries` between drafts vs transcriptions | OPEN — temporary dual note in ownership matrix |
| ISSUE-MOD-002 | Whether reports/exports share read models or dedicated DB views | OPEN — default: owner query ports |
| ISSUE-CANONICAL-001 | Canonical person DTO contract detail | OPEN — MOD-PROMOTION + MOD-LAYER-INT |

## 24. Risks and anti-patterns

| ID | Anti-pattern | Why forbidden | Correct pattern |
| --- | --- | --- | --- |
| AP-MOD-001 | UI → repository/DB | Bypasses rules/audit/permissions | UI → application → domain |
| AP-MOD-002 | Domain → Prisma/SDK | Locks domain to provider | Ports + infrastructure |
| AP-MOD-003 | Deep import `internal` | Breaks encapsulation | Public `index`/`contracts` |
| AP-MOD-004 | Shared “utils” with claim rules | Hidden second owner | Move to MOD-CLAIMS |
| AP-MOD-005 | Dual-write claims from queues + claims | Race/integrity failure | Single owner MOD-CLAIMS |
| AP-MOD-006 | Worker embeds matching algorithm | Untested divergent logic | Call matching application |
| AP-MOD-007 | Invent error strings in UI | Breaks Catalog 2 | Map Catalog 2 codes |
| AP-MOD-008 | Circular feature imports | Undeployable graph | Events or orchestrator module |
| AP-MOD-009 | Cross-module mutable singleton | Hidden coupling | Explicit commands/events |
| AP-MOD-010 | New module without matrix update | Ungovernable growth | Amend IS-102 first |

## 25. Dependencies

IS-100, IS-101, Catalogs 1–9, Volumes 8–13. Implementation still blocked by G-10 and open ADRs.

## 26. Traceability

| Requirement | Source | Artifact | Status |
| --- | --- | --- | --- |
| REQ-MOD-001…018 | IS-102 | Matrices + this spec | FULLY_MAPPED (design) |
| REQ-REPO-005/006 | IS-100 | Dependency + encapsulation | FULLY_MAPPED |
| REQ-TECH-006 | IS-101 | Adapter boundaries | FULLY_MAPPED |
| AC-MOD-001…008 | IS-102 | Acceptance | FULLY_MAPPED |

## 27. Implementation Boundary

**Authorized:** documentation and matrices under `docs/implementation_specs/`.  
**Forbidden:** creating application modules on disk; npm app scaffolding; migrations; “temporary” deep-import exceptions.

## 28. Revision History

| Version | Date | Change | Approval |
| --- | --- | --- | --- |
| 1.0 | 2026-07-26 | Initial module boundary rulebook | D-064 |

---

## Feature placement algorithm (for Burt)

```text
1. Identify capability noun (claim, batch, match, …)
2. Find Module ID in inventory / ownership matrix
3. Place domain rules in domain/<capability>
4. Place use case in application/<capability>
5. Place persistence in infrastructure/<capability> implementing owner ports
6. Place HTTP/UI in presentation/<capability> calling application only
7. Place jobs in workers invoking application/<capability>
8. Update contracts + tests owned by that module
9. If second capability is involved, add orchestrating application service or domain event — do not deep-import
10. Cite this IS and matrices in the implementation package
```

## Next specification

```text
PEOPLE-IS-103-ENVIRONMENT-ARCHITECTURE-1.0
```

## Final status

```text
PEOPLE-IS-102 MODULE BOUNDARY SPECIFICATION: APPROVED (DOCUMENTATION)
APPLICATION IMPLEMENTATION: NOT AUTHORIZED
ARCHITECTURAL RULEBOOK: ACTIVE FOR FUTURE PACKAGES
```
