# PEOPLE-IS-305 — MIGRATION GOVERNANCE

**Title:** Migration Governance  
**Document ID:** `PEOPLE-IS-305-MIGRATION-GOVERNANCE-1.0`  
**Version:** 1.0  
**Status:** APPROVED  
**Phase:** PHASE 3 — DATABASE ARCHITECTURE  
**Project Root:** `H:\people`  
**Owner:** People Intake System Program  
**Approval Authority:** Decision Log D-077  
**Created Date:** 2026-07-26  
**Last Updated:** 2026-07-26  
**Governing Documents:** IS-300…304; IS-100; IS-105; Build Gates (G-10); Catalogs 01/08/09; D-065  
**Dependencies:** PEOPLE-IS-304 APPROVED (D-076)  
**Implementation Authorization:** `IMPLEMENTATION NOT AUTHORIZED`  
**Migrations Authorization:** `migrationsAuthorized = false` (unchanged by this package)

```text
DESIGN COMPLETE
APPROVED FOR DOCUMENTATION GOVERNANCE
CANONICAL MIGRATION GOVERNANCE (BRIDGE DESIGN → IMPLEMENTATION)
THIS PACKAGE DOES NOT CREATE MIGRATIONS
EXECUTABLE SCHEMA REMAINS UNAUTHORIZED
GATE G-10 REMAINS CLOSED
PHASE 3 LOGICAL PERSISTENCE + MIGRATION GOVERNANCE: COMPLETE
```

---

## 1. Purpose

Define **how migrations will be governed** once implementation is authorized. This IS is the bridge between approved logical design (IS-300…304) and future executable schema. It does **not** define migration SQL, Prisma schemas, or physical DDL.

## 2. Scope

Migration package (`MG-*`) admission rules; governance/traceability requirements; allowed vs prohibited object types; documentation-before-execution; validation/drift/evidence sequences; safety (destructive change, rename, data preservation, rollback, emergency stop); authorization preconditions and Gate G-10 relationship; standing migration doctrine.

## 3. Out of Scope

```text
FORBIDDEN IN THIS PACKAGE:
  Creating migrations/ or database/migrations/
  SQL / DDL / Prisma schema / seeds
  Applying schema to any environment
  Opening Gate G-10
  Setting migrationsAuthorized or applicationCodeAuthorized to true
  Inventing LT-*/REL-*/CON-*/RM-* via “helpful” migration drafts
```

First physical schema package content → only after separate Implementation Authorization.

## 4. Standing doctrine (locked)

```text
A migration implements
an approved logical design.

A migration never creates
a logical design.

No migration may introduce
a table,
relationship,
constraint,
or read model
that is not already governed.

Executable schema
is the final translation layer,
never the source of architecture.
```

### 4.1 Extension / change tree

```text
Need a schema change?
  → Exists in IS-301 / IS-302 / IS-303 / IS-304 (or approved amendment/ADR)?
      YES → May appear in an authorized MG-* package (when migrationsAuthorized)
      NO  → Amend governing IS / ADR first
              → Only then may MG-* translate it
```

### 4.2 Separation of responsibilities

| Role | Owns |
| --- | --- |
| Architecture (IS-200…304) | What must exist |
| Governance (this IS + gates) | How change is controlled |
| Implementation (future packages) | Translation into executable artifacts with evidence |

No architectural decisions should remain when the first MG-* package is authorized.

---

## 5. Mandatory migration-package questionnaire (`MG-*`)

Every future executable migration package MUST complete this card **before** any schema artifact is created or applied.

| # | Area | Questions |
| --- | --- | --- |
| G1 | Identity | Stable `MG-*` identifier |
| G2 | Identity | Human title / version |
| G3 | Package | Governing implementation package ID |
| G4 | Trace | Traceability to IS-300…304 (cite sections / LT / REL / CON / RM) |
| G5 | Trace | Referenced ADRs (must be accepted or explicitly waived with Decision Log) |
| G6 | Trace | Referenced requirements (REQ-* / Catalog 09 rows) |
| G7 | Trace | Referenced logical tables (`LT-*`) |
| G8 | Trace | Referenced relationships (`REL-*`) |
| G9 | Trace | Referenced constraints (`CON-*`) |
| G10 | Trace | Referenced read models (`RM-*`) if projections included |
| G11 | Scope | Allowed object types in this MG |
| G12 | Scope | Explicitly prohibited object types in this MG |
| G13 | Scope | Documentation required before execution |
| G14 | Scope | Rollback expectations |
| G15 | Scope | Forward-only policy applicability |
| G16 | Scope | Version compatibility rules |
| G17 | Validation | Required validation sequence |
| G18 | Validation | Schema comparison expectations |
| G19 | Validation | Drift detection expectations |
| G20 | Validation | Documentation verification |
| G21 | Validation | Evidence generation |
| G22 | Validation | Completion reporting |
| G23 | Safety | Destructive change policy for this MG |
| G24 | Safety | Rename policy |
| G25 | Safety | Data preservation expectations |
| G26 | Safety | Compatibility with existing deployments |
| G27 | Safety | Rollback doctrine for this MG |
| G28 | Safety | Emergency stop criteria |
| G29 | Auth | Preconditions checklist (see §9) — all PASS or blocked |
| G30 | Auth | Gate dependencies |
| G31 | Auth | Required approvals |
| G32 | Auth | Required audit status |
| G33 | Auth | Required ADR status |

---

## 6. Functional Requirements

| ID | Description |
| --- | --- |
| REQ-MIG-001 | Every executable migration package MUST have a complete `MG-*` card before artifacts are created. |
| REQ-MIG-002 | Migrations MUST only translate governed LT-*/REL-*/CON-*/RM-* (or approved amendments/ADRs). |
| REQ-MIG-003 | Migrations MUST NOT invent tables, relationships, constraints, or read models. |
| REQ-MIG-004 | Additive-first policy: prefer expand; use expand/contract for renames; no silent destructive rewrites. |
| REQ-MIG-005 | Shared-DB compatibility audit (ISSUE-DBA-001) MUST be satisfied before first apply to shared environments. |
| REQ-MIG-006 | Migration credentials MUST be separate from application runtime credentials. |
| REQ-MIG-007 | Each applied migration MUST produce validation evidence and a completion report. |
| REQ-MIG-008 | This IS-305 package MUST NOT create executable migrations or open Gate G-10. |
| REQ-MIG-009 | `migrationsAuthorized` and `applicationCodeAuthorized` remain false until separately set by Gate G-10 / Decision Log. |
| REQ-MIG-010 | Emergency stop: halt apply on unexplained drift, failed validation, or missing MG-* traceability. |

---

## 7. Scope policies (standing)

### 7.1 Allowed object types (when authorized)

Examples (not an inventory of this package):

* Tables/columns translating approved `LT-*` / `FLD-*`
* FKs / uniqueness / checks translating approved `REL-*` / `CON-*`
* Views or disposable projections translating approved `RM-*`
* Indexes that optimize without inventing invariants
* Migration metadata / ledger rows

### 7.2 Explicitly prohibited object types (always, unless ADR + IS amendment)

* Undocumented production tables
* Physical FKs inventing business relationships absent from IS-302
* CHECK/UNIQUE inventing invariants absent from IS-303
* Reporting dual-write tables used as alternate truth (violates IS-304)
* Intake-owned canonical person master tables (EXTERNAL boundary)
* Seeds that invent Catalog 01 states or production business data without package authority
* Mixing app runtime credentials into migration runners

### 7.3 Documentation required before execution

1. Completed `MG-*` questionnaire  
2. Trace map to IS-300…304  
3. ADR status sheet for referenced OPEN ADRs  
4. Rollback / expand-contract notes  
5. Target environment authorization  
6. Pre-apply validation plan  

### 7.4 Forward-only and version compatibility

| Policy | Rule |
| --- | --- |
| Prefer additive | New columns/tables over in-place destructive rewrite |
| Renames | Expand/contract (add new → dual-write/read → drop old) unless empty env + ADR |
| Forward-only in shared/prod | Down-migrations not relied on for production recovery; restore from backup + forward fix preferred |
| Empty/dev | Controlled reset may be allowed only when environment policy and package explicitly permit |
| Compatibility | App versions MUST tolerate expand phase (ignore unknown columns / dual read) per package |

### 7.5 Rollback doctrine

1. Prefer restore-forward over fragile down scripts in shared environments.  
2. Each MG-* documents whether a down path exists and its limits.  
3. Data-destructive rollback requires explicit Decision Log / Steve authorization.  
4. Audit append-only stores (CON-APP-AUDIT) MUST NOT be rewritten to “undo” history.

---

## 8. Validation sequence (required when applying)

Technology-neutral sequence for every MG-* apply:

```text
1. Preflight: H-drive / governance / package authorization flags
2. Documentation verification: MG-* card complete; LT/REL/CON/RM trace present
3. ADR / issue gate: blockers for this MG resolved or explicitly deferred with Decision Log
4. Schema comparison: intended delta vs current schema inventory
5. Drift detection: fail if undocumented objects appear in target
6. Dry-run / plan (when tooling supports) — still no inventing
7. Apply (only if migrationsAuthorized + env authorized)
8. Post-apply schema comparison
9. Constraint/relationship smoke checks mapped to CON-*/REL-*
10. Evidence pack: logs, hashes, operator, timestamps, MG-* ID
11. Completion report + Decision Log / package closeout citation
```

Failure at any step → **emergency stop** (REQ-MIG-010). Do not “fix forward” by inventing schema.

---

## 9. Authorization — first executable migration preconditions

**Completing IS-305 does not authorize migrations.**

The first executable migration package MAY be **considered** only when **all** of the following are true:

| # | Precondition | Current posture (as of D-077) |
| --- | --- | --- |
| P1 | Gate G-10 Implementation Authorization PASSED | **CLOSED** |
| P2 | `applicationCodeAuthorized` / `databaseChangesAuthorized` / `migrationsAuthorized` set true by governance | **false** |
| P3 | Design freeze status no longer blocked (`designFreezeStatus`) | **blocked** |
| P4 | ISSUE-FREEZE-001 resolved or Decision Log waiver | **OPEN** |
| P5 | Critical ADRs accepted or Decision Log disposition | **OPEN set remains** |
| P6 | ISSUE-DBA-001 shared-DB compatibility audit complete for target | **OPEN** |
| P7 | ISSUE-CANONICAL-001 disposition sufficient for any EXTERNAL_REF physical choices in that MG | **OPEN** |
| P8 | Independent audit lane reports G-10 readiness (no silent Critical findings) | **ACTIVE / required** |
| P9 | MG-* card complete with IS-300…304 trace | N/A until authorized |
| P10 | Steve (or designated authority) Decision Log acceptance for first physical schema package | **Not granted** |

```text
IS-305 complete
  ≠ Gate G-10 open
  ≠ migrationsAuthorized
  ≠ first physical schema package authorized
```

Wording locked: Implementation Authorization **may be considered** after governance/audit/ADR/freeze evaluation — it is **not** automatically granted by Phase 3 completion.

---

## 10. Example MG-* skeleton (non-executable, illustrative)

### MG-INTAKE-CORE-001 — (FUTURE — NOT AUTHORIZED)

| Field | Value |
| --- | --- |
| G1–G3 | `MG-INTAKE-CORE-001` / Intake Core Schema Translate / future PKG-intake-core |
| G4–G10 | Cite IS-301 LT-BATCH/PAGE/ENTRY/…; IS-302 REL-*; IS-303 CON-*; RM-* only if included |
| G11–G12 | Allowed: translating listed LT/REL/CON; Prohibited: canonical masters, undocumented tables |
| G13–G16 | Full MG docs; expand-first; forward-only in shared; app dual-read during expand |
| G17–G22 | §8 sequence; evidence + completion report |
| G23–G28 | No destructive drops in v1 apply; renames expand/contract; preserve data; stop on drift |
| G29–G33 | All §9 preconditions PASS — **currently FAIL (G-10 closed)** |

This skeleton MUST NOT be implemented by this package.

---

## 11. Safety policies (standing)

| Topic | Rule |
| --- | --- |
| Destructive changes | Default deny in shared/prod; require Decision Log + data preservation plan |
| Drop table/column | Only after expand/contract deprecation window or empty authorized env |
| Rename | Expand/contract; never lose FK/trace mid-flight |
| Data preservation | Backups / snapshots before destructive applies; PII handling per Cat 08 |
| Existing deployments | Compatibility audit (ISSUE-DBA-001) before shared apply |
| Emergency stop | Drift, failed validation, missing MG trace, unauthorized env, secret exposure |

---

## 12. Phase 3 completion statement

With IS-305 APPROVED, Phase 3 Database Architecture documentation is **complete**:

```text
IS-300  Persistence Philosophy          APPROVED
IS-301  Logical Objects                 APPROVED
IS-302  Logical Relationships           APPROVED
IS-303  Logical Constraints             APPROVED
IS-304  Read Models                     APPROVED
IS-305  Migration Governance            APPROVED
```

Next checkpoint:

```text
Gate G-10 Review
  → if and only if governance prerequisites satisfied
  → Implementation Authorization may be considered
  → First Physical Schema Package (MG-*)
```

## 13. Acceptance Criteria

| ID | Criterion | Met? |
| --- | --- | --- |
| AC-MIG-001 | MG-* questionnaire defined | Yes |
| AC-MIG-002 | Migration doctrine locked | Yes |
| AC-MIG-003 | Allowed/prohibited scope + safety/rollback defined | Yes |
| AC-MIG-004 | Validation sequence defined | Yes |
| AC-MIG-005 | G-10 / first-migration preconditions explicit; no auto-grant | Yes |
| AC-MIG-006 | No executable migrations/SQL/Prisma created | Yes |
| AC-MIG-007 | Flags remain unauthorized | Yes |

## 14. Risks

| ID | Risk | Mitigation |
| --- | --- | --- |
| RISK-MIG-001 | “Helpful” migration invents design | REQ-MIG-002/003; doctrine §4 |
| RISK-MIG-002 | Treating IS-305 as G-10 open | REQ-MIG-008/009; §9 |
| RISK-MIG-003 | Destructive apply without evidence | §8 / §11 |
| RISK-MIG-004 | Shared DB assumptions | ISSUE-DBA-001; REQ-MIG-005 |

## 15. Dependencies

IS-300…304; Build Gates G-10; ISSUE-FREEZE-001; ISSUE-DBA-001; ISSUE-CANONICAL-001; Critical ADR set; audit lane; D-065 closeout protocol.

## 16. Traceability

MG-* (future) ↔ IS-300…304 ↔ Catalog 09 — governance FULLY_MAPPED.  
Executable artifacts ↔ NOT AUTHORIZED.

## 17. Implementation Boundary

**Authorized now:** this governance specification; indexes; audit verification; Decision Log.  
**Forbidden now:** migrations, SQL, Prisma, schema apply, Gate G-10 self-opening.

## 18. Revision History

| Version | Date | Change | Approval |
| --- | --- | --- | --- |
| 1.0 | 2026-07-26 | Migration governance; Phase 3 complete (docs) | D-077 |

## Next primary

```text
PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0
```

(Gate G-10 readiness / freeze remediation — **not** automatic implementation.)

## Independent lane

```text
Continues as primary focus for Gate G-10 readiness.
Critical ADRs and open issues remain visible.
```

## Final status

```text
PEOPLE-IS-305 MIGRATION GOVERNANCE: APPROVED (DOCUMENTATION)
MIGRATION IMPLEMENTS APPROVED DESIGN — NEVER CREATES IT
EXECUTABLE SCHEMA = FINAL TRANSLATION LAYER — NOT ARCHITECTURE SOURCE
PHASE 3 COMPLETE (DOCUMENTATION)
GATE G-10: CLOSED
MIGRATIONS / APPLICATION: NOT AUTHORIZED
```
