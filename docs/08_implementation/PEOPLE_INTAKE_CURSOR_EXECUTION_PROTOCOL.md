# People Intake — Cursor Execution Protocol

**Status:** draft_complete  
**Version:** 2.2  
**Build:** PEOPLE-PROJECT-CONSTITUTION-3.0  
**Authority:** Governs all future Cursor interactions for this project

---

## Supreme Document

```text
docs/00_governance/PEOPLE_INTAKE_PROJECT_CONSTITUTION.md
```

**VOLUME 0 — PROJECT CONSTITUTION** is mandatory before every build session. Follow **Article III — Cursor Implementation Oath**.

Library map: `docs/00_governance/PEOPLE_INTAKE_DOCUMENTATION_LIBRARY.md` (Volumes 0–7).

---

## 9.0 Execution Authority (Burt)

**Authority:** Decision Log D-068 / PEOPLE-IS-105 §9.15; standing closeout D-065.

Burt (Cursor) has **full execution authority** within established governance. Instructions are directed to the implementation engineer, not to an operator relay.

Burt MUST, when a slice is in scope and valid:

1. **Execute** required validation.  
2. **Generate** completion / evidence reports.  
3. **Update** governance indexes, registers, and RTM.  
4. **Commit** the slice.  
5. **Push** to the canonical branch.  
6. **Verify** the remote contains the commit.  
7. **Deploy** only when an authorized deployable surface exists.  
8. **Record** evidence in the completion report / latest Cursor report.

Burt MUST NOT ask Steve to run ordinary closeout steps, wait for approval to validate/commit/push, or defer D-065 publication when the work item is otherwise complete.

Execution **stops** only for reserved gates:

* New ADR requiring acceptance  
* Project scope change  
* Authorization to begin application implementation (Gate G-10 / `applicationCodeAuthorized`)  
* Authorization to enable deployment (`deploymentAuthorized`) or Production go-live  
* Legal, security, or business policy decisions reserved for Steve  
* Hard-boundary violations (H-drive, forbidden paths, secret exposure, constitution conflicts)

### 9.0.1 Domain extension doctrine (mandatory)

Authority: PEOPLE-IS-200; PEOPLE-IS-201 §5.3; Decision Log D-070.

```text
Does the feature belong to an existing domain concept?

YES → Extend the existing specification / entity card.
NO  → Does the domain model need to evolve?
        YES → Update governing IS / Decision Log / ADR.
        NO  → Reject the implementation proposal.
```

Additional locks:

1. **Catalog 01** is the sole production state authority — never redefine states in packages.  
2. **Match Resolution ≠ Promotion** — neither owns the other.  
3. No entity may be introduced without a complete IS-201 questionnaire card.

### 9.0.2 Field extension doctrine (mandatory)

Authority: PEOPLE-IS-202 §4.2; Decision Log D-071.

```text
New feature?
  → Existing Entity? (IS-201)
      → Existing Field? (IS-202)
          YES → Reuse
          NO  → Existing Value Object?
                  YES → Reuse VO on entity (amend card)
                  NO  → Update IS-202 or create ADR
                        → Only then may packages reference the new field
```

Lifecycle/state fields MUST use Catalog 01 via `VO-CAT01-STATE` — never field-dictionary draft status labels.

### 9.0.3 Persistence extension doctrine (mandatory)

Authority: PEOPLE-IS-300 §9.2; Decision Log D-072.

```text
New persistence requirement?
  → Existing Entity? (IS-201)
      → Existing Field? (IS-202)
          → Existing Value Object?
              → Existing Persistence Rule? (IS-300 / IS-301+)
                  YES → Reuse
                  NO  → Update IS-300/IS-301+ or create ADR
                        → Only then may future packages create tables/schemas/migrations
```

IS-300 and later database IS documents are **documentation only** until `migrationsAuthorized` / Gate G-10. Never create migrations, SQL, Prisma schemas, seeds, or live schema objects to “complete” a database specification package.

### 9.0.4 Logical table extension doctrine (mandatory)

Authority: PEOPLE-IS-301 §4.1; Decision Log D-073.

```text
Need new persistence?
  → Existing Aggregate / Entity / Field?
      → Existing Logical Table? (IS-301)
          YES → Reuse
          NO  → Update IS-301 or create ADR
                → Only then may future packages define physical schema
```

Logical tables ≠ physical tables. No SQL/DDL in IS-301/IS-302 documentation packages.

### 9.0.5 Relationship doctrine (mandatory)

Authority: PEOPLE-IS-302 §4; Decision Log D-074.

```text
Relationships are governed business concepts, not implementation conveniences.
No migration/ORM relationship may appear unless it exists in IS-302 (or amendment/ADR).
No physical foreign key may invent a business relationship.
```

### 9.0.6 Integrity doctrine (mandatory)

Authority: PEOPLE-IS-303 §4; Decision Log D-075.

```text
A database constraint may enforce an approved business invariant.
It may not invent one.

Application validation may explain an invariant.
It may not weaken it.

Physical enforcement may use multiple mechanisms later.
The logical invariant remains technology-neutral and authoritative.
```

Authority hierarchy: Catalog 01 → IS-200 → IS-201 → IS-202 → IS-302 → IS-303.  
Source conflicts MUST be surfaced as issues/ADRs — never silently chosen.  
No CHECK/UNIQUE/FK/index/trigger/validator may appear unless backed by a `CON-*` card (or amendment/ADR).

### 9.0.7 Read-model doctrine (mandatory)

Authority: PEOPLE-IS-304 §4; Decision Log D-076.

```text
Read models exist for consumption, not ownership.
Read models project truth. They do not create truth.
A read model may derive information. It may never redefine an approved business concept.
Read models are disposable. The governed domain is authoritative.
```

No SQL view / materialized projection / reporting dual-write may appear unless backed by an `RM-*` card (or amendment/ADR). Queue and worklist projections MUST NOT accept claim/resolution authoritative writes.

### 9.0.8 Migration doctrine (mandatory)

Authority: PEOPLE-IS-305 §4; Decision Log D-077.

```text
A migration implements an approved logical design.
A migration never creates a logical design.
No migration may introduce a table, relationship, constraint, or read model that is not already governed.
Executable schema is the final translation layer, never the source of architecture.
```

No migration artifact may be created unless `migrationsAuthorized` is true, Gate G-10 has passed, and a complete `MG-*` card exists. Completing IS-305 / Phase 3 documentation does **not** authorize migrations or open Gate G-10.

### 9.0.9 Pre–Gate G-10 Burt posture (mandatory)

Authority: Post–D-078 standing confirmation; `docs/00_governance/PEOPLE_GATE_G10_REMEDIATION_PLAN.md`.

Until Gate G-10 opens **and** Steve grants Implementation Authorization, Burt’s work is **governance maintenance**, not engineering expansion:

```text
ALLOWED:
  Audit, remediation, traceability, consistency,
  documentation quality, evidence generation, governance reporting

FORBIDDEN:
  Drafting migrations, executable schemas, ORM models, APIs,
  or implementation packages beyond the approved governance sequence
  ("getting ahead")
```

Do not expand Phase 3+ design to “prepare for coding.” Reduce uncertainty; keep criteria stable.

### 9.0.10 Gate G-10 meaning doctrine (mandatory)

Authority: Post–D-078 standing confirmation; Gate G-10 readiness assessment (D-078).

```text
Passing every technical audit
does not
authorize implementation.

Implementation Authorization
is a separate governance decision.

Failing G-10
does not mean
the architecture failed.

It means
the governance prerequisites
remain unsatisfied.
```

Future G-10 reassessment (Decision Log **D-079 or later**) must use the **same** three-outcome rubric and standards; only **evidence** may change — never lower the threshold to force OPEN.

Canonical remediation sequence: `docs/00_governance/PEOPLE_GATE_G10_REMEDIATION_PLAN.md` — no skip/reorder without Decision Log.

---

## 9.1 Start-of-Run Requirements

Cursor must:

1. Confirm current directory is under `H:\people`.
2. **Read Volume 0** — Project Constitution (Preamble through applicable Articles; re-confirm standing orders if already loaded this session).
3. Read the active-build registry (`contracts/governance/active-build.json`).
4. Identify the relevant library volume(s) for the slice (see Documentation Library).
5. Read the H-drive protocol and design-before-code protocol if not already internalized this session.
6. If coding is authorized: read Volume 7 orchestration for the active phase/slice, then Volumes 8–12 / EC / IP package for that slice. Never invent endpoints, tables, states, or components.
7. Confirm the authorized phase and forbidden paths.
8. Run the H-drive preflight (`npm run drive:validate` when Node scripts are available).
9. Stop if a hard boundary is violated.
10. If `applicationCodeAuthorized` is false: do not create `src/` or other forbidden paths.

---

## 9.2 During-Run Requirements

Cursor must:

- Remain inside the authorized scope for the active build
- Avoid unrelated RedDirt changes
- Avoid intentional writes to `C:\`
- Preserve document cross-references
- Record decisions in the Decision Log when closing or changing material choices
- Update the progress ledger when progress meaningfully changes
- Validate generated contracts
- Report contradictions instead of silently inventing resolutions for major ambiguity
- Never expose secrets
- Never make production changes without authorization
- Never create application code while `applicationCodeAuthorized` is `false`

---

## 9.3 End-of-Run Requirements

Cursor must report:

1. Exact files created
2. Exact files modified
3. Commands run
4. Validation results
5. Boundary verification
6. Unresolved decisions
7. Risks
8. Progress by layer
9. Recommended next build
10. Git status
11. Commit status
12. Deployment status

### 9.3.1 Standing Commit / Push / Deploy Protocol (mandatory)

Authority: `docs/00_governance/PEOPLE_PROTOCOL_COMMIT_PUSH_DEPLOY.md` (D-065).

After every completed, validated slice:

1. Validate (`governance:validate`, and `docs:catalogs:validate` when catalogs touched).  
2. Confirm no forbidden implementation artifacts while application code is not authorized.  
3. Update indexes, registers, RTM, completion report.  
4. **Commit** with work-item ID in the message.  
5. **Push** to the canonical GitHub branch.  
6. **Verify** the remote contains the commit.  
7. **Deploy/verify Netlify** only when an authorized deployable surface exists.  
8. Never treat local-only changes as complete.  
9. Never invent application code to force a Netlify deploy.  

If no authorized deployable surface exists, completion evidence MUST state:

```text
Netlify deployment: NOT APPLICABLE — no authorized deployable surface exists
Application implementation: NOT AUTHORIZED
```

---

## 9.4 Hard Stops

Cursor must stop for:

- Any intentional controlled project write to `C:\`
- Unauthorized database change
- Unauthorized migration
- Production-secret exposure
- Production deployment before approval
- Application code before design freeze
- Cross-project edits outside `H:\people`
- Public exposure of source images
- Destructive canonical-person changes
- Automatic uncertain merging design or implementation
- Any instruction that conflicts with the governing documents without an explicit Decision Log amendment

---

## Active Build Enforcement

Before creating files, compare intended paths against:

```text
contracts/governance/active-build.json
```

Respect:

- `authorizedPaths`
- `forbiddenPaths`
- `hardBoundaries`
- `applicationCodeAuthorized`
- `databaseChangesAuthorized`
- `migrationsAuthorized`
- `deploymentAuthorized`

---

## Recommended Next Build

```text
PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0
```

Phase 3 (IS-300…305) documentation is complete.  
Gate G-10 readiness verdict (D-078): **REMAIN CLOSED** — `reports/PEOPLE_GATE_G10_READINESS_ASSESSMENT.md`.  
This does **not** authorize implementation. Implementation Authorization is a separate Steve decision after G-10 (if opened).

No application code, migrations, SQL, or Prisma until freeze APPROVED and Gate G-10 / migrationsAuthorized opens.

Orchestration reference: `docs/08_implementation/PEOPLE_INTAKE_CURSOR_BUILD_ORCHESTRATION.md`
