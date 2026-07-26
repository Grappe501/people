# Gate G-10 — Canonical Remediation Plan

**Document ID:** `PEOPLE-GATE-G10-REMEDIATION-PLAN-1.0`  
**Status:** LOCKED — CANONICAL  
**Authority:** Post–D-078 standing confirmation (Decision Log)  
**Project root:** `H:\people`  
**Does not open Gate G-10**  
**Does not authorize implementation**

```text
CRITERIA REMAIN STABLE.
ONLY EVIDENCE CHANGES.
FUTURE G-10 REASSESSMENT = D-079 OR LATER
(when evidence changes — not when standards are lowered)
```

---

## 1. Purpose

Define the **only** ordered path from the current D-078 verdict (**REMAIN CLOSED**) to a future Gate G-10 reassessment. No step may be skipped or reordered without an explicit Decision Log action.

## 2. Canonical sequence

```text
1. Resolve or formally accept blocking ADRs
   (Steve Decision Log / ADR acceptance)
        ↓
2. Resolve ISSUE-DBA-001
   (shared-DB compatibility audit — read-only)
        ↓
3. Disposition remaining Critical Issues
   (per open-issue triage: close, waive, or Conditional Decision Log)
        ↓
4. Approve Design Freeze
   (re-issue Design Freeze Approval Report = APPROVED)
        ↓
5. Run a fresh Gate G-10 Assessment
   (same three-outcome rubric; new evidence pack)
        ↓
6. Steve decides Implementation Authorization
   YES / NO
        ↓
7. If YES → first MG-* package eligible (e.g. MG-001)
   under IS-305 governance
```

## 3. Blocking ADR minimum (step 1)

Unless Decision Log waives specifically:

* ADR-001 Application Framework  
* ADR-002 Database Provider  
* ADR-003 ORM / Data Access  
* ADR-004 Authentication Provider (including method)  
* ADR-005 Object Storage  
* ADR-020 H-Drive Enforcement  

Additional ADRs may remain open only if Decision Log records a **CONDITIONAL** deferral that does not contradict freeze exit criteria.

## 4. Stable assessment rubric (unchanged)

Future reassessment must still conclude with exactly one of:

```text
OPEN
OPEN WITH CONDITIONS
REMAIN CLOSED
```

Standards must not be lowered to force OPEN. Only evidence may change.

## 5. Meaning doctrines (locked)

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

## 6. Burt posture until G-10 opens

Until Gate G-10 opens **and** Steve grants Implementation Authorization:

```text
ALLOWED: audit, remediation, traceability, consistency,
         documentation quality, evidence, governance reporting

FORBIDDEN: drafting migrations, executable schemas, ORM models,
           APIs, or implementation packages beyond this governance sequence
           ("getting ahead")
```

The project benefits more from reducing uncertainty than from adding design.

## 7. Related evidence

| Artifact | Path |
| --- | --- |
| Current verdict | `reports/PEOPLE_GATE_G10_READINESS_ASSESSMENT.md` (REMAIN CLOSED) |
| Issue triage | `docs/implementation_specs/decisions/OPEN_ISSUE_REGISTER.md` |
| Freeze report | `docs/08_implementation/PEOPLE_INTAKE_DESIGN_FREEZE_REPORT.md` |
| Migration governance | `docs/implementation_specs/300_database/PEOPLE-IS-305-MIGRATION-GOVERNANCE.md` |

## 8. Revision History

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-07-26 | Canonical plan locked post D-078 affirmation |
