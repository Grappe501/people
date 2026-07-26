# ISSUE-DBA-001 — Shared Database Audit Plan

**Document ID:** `PEOPLE-ISSUE-DBA_001_SHARED_DATABASE_AUDIT_PLAN-1.0`  
**Issue:** ISSUE-DBA-001  
**Slice:** PEOPLE-G10-BLOCKER-REMEDIATION-PACKETS-1.0  
**Verified commit:** `c1c7c36`  
**Status:** PLAN ONLY — NOT EXECUTED  

```text
Database audit ≠ Database modification

Default posture for this slice:
PLAN ONLY
NO DATABASE CONNECTION
NO CREDENTIAL USE
NO LIVE SCHEMA INSPECTION
```

---

## 1. Exact question

> Can People Intake’s future physical schema (translating IS-301…305) coexist safely with any shared/existing database environment without assuming undocumented tables, inventing ownership, or colliding with external systems (especially canonical person stores)?

## 2. Why it blocks

| Gate | Effect |
| --- | --- |
| Gate G-10 | Indirect via freeze / migrations readiness narrative; listed in IS-305 §9 as P6 |
| `migrationsAuthorized` | **Direct BLOCKING_MG** — must complete before first apply to shared environments |
| First MG-* apply | Must not assume remote tables exist (ISSUE-DBA-001 text) |

## 3. Current assumptions

* Phase 3 logical design is technology-neutral and complete (IS-300…305).  
* Canonical person masters are EXTERNAL (soft-ref default).  
* No executable migrations exist in repo.  
* Shared DB target identity (host/brand/schema) may depend on ADR-002.

## 4. Current unknowns

* Whether a shared production/staging Postgres already hosts related schemas.  
* Naming collisions with conceptual Volume 10 table names.  
* Privilege model (migration role vs app role).  
* Whether canonical person DB is same instance or separate.

## 5. Required evidence (when audit executes — later)

* Inventory of existing schemas/tables in target (read-only).  
* Collision report vs LT-* logical names.  
* Ownership map: intake vs external.  
* Compatibility conclusion: COMPATIBLE / COMPATIBLE_WITH_CONDITIONS / INCOMPATIBLE.  
* Redacted evidence pack (no secrets).

## 6. Permitted evidence sources (future execution)

* Read-only DB role explicitly issued for audit.  
* Existing architecture docs / DBA interviews.  
* Schema dump provided by Steve/ops (offline file under `H:\people` if authorized).

## 7. Prohibited actions (always in this plan; until re-authorized)

```text
No CREATE/ALTER/DROP
No migration apply
No Prisma db push/pull against live systems
No use of production credentials in repo
No writing secrets into reports
```

## 8. Audit steps (future execution package)

1. Confirm ADR-002 posture (hosted PG target class).  
2. Obtain read-only access or offline inventory (Steve/ops).  
3. Compare inventory to IS-301 LT-* catalog.  
4. Flag collisions / ownership conflicts.  
5. Assess EXTERNAL_REF physical FK feasibility (ISSUE-CANONICAL-001).  
6. Write findings report.  
7. Decision Log disposition of ISSUE-DBA-001.

## 9. Completion criteria

* Written audit report committed under `reports/`.  
* ISSUE-DBA-001 status updated only after Steve/Ernie accept findings.  
* No schema modified.

## 10. Possible outcomes

| Outcome | Consequence |
| --- | --- |
| COMPATIBLE | migrationsAuthorized may be considered after G-10+Impl Auth |
| COMPATIBLE_WITH_CONDITIONS | Conditions recorded; MG scope limited |
| INCOMPATIBLE | Alternate DB strategy / ADR-002 revisit |

## 11. Owners

| Role | Responsibility |
| --- | --- |
| Decision owner | Steve (accept findings / authorize later execution) |
| Evidence owner | Burt (plan now); designated auditor later |
| Architecture interpretation | Ernie |

## 12. Credentials / access

* **Later execution may require** read-only credentials or an ops-provided inventory.  
* **This slice does not.**  
* Safe handling: never commit secrets; redact connection strings; prefer offline inventory files under `H:\people`.

## 13. No-change assurance

Completing this **plan** does not change any database. Future audit execution must remain read-only unless a separate Decision Log authorizes otherwise.

## 14. Traceability

* Open-issue register ISSUE-DBA-001  
* IS-305 §9 P6  
* G-10 readiness assessment D-078  
* Remediation plan step 2  
* ADR-002 / ADR-003 packets  

```text
ISSUE-DBA-001 REMAINS OPEN
PLAN EXISTENCE ≠ ISSUE CLOSURE
```
