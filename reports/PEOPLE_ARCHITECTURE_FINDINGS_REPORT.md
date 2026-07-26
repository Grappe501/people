# People Intake — Architecture Findings Report

**Audit ID:** PEOPLE-ARCHITECTURE-AUDIT-AND-DESIGN-VALIDATION-1.0  
**Date:** 2026-07-25  
**Project root:** `H:\people`  
**Philosophy:** Design is wrong until proven otherwise  
**Implementation authorized:** **No**  
**Design freeze status:** **BLOCKED**

---

## Executive Verdict

The People Intake design is **strong on product intent and domain separation**, and **not ready for implementation or design freeze**.

Primary blockers:

1. **Quality / Operations / Deployment / Freeze volume is missing** (14 planned documents, including freeze report and handoff).
2. **Several High-severity open engineering decisions** were deferred across multiple builds and never closed (exact auto-link, storage provider, shared DB audit, retention periods, match-claim model).
3. **Internal terminology and state-model dual tracks** create implementer ambiguity.
4. **UX field-condition model and data field-condition model disagree** on `AMBIGUOUS`.

Until Critical findings are remediated and Gate G-7/G-8/G-9 materials exist, Cursor must **not** write application code.

---

## Audit Coverage

| Prior package | Reviewed |
| --- | --- |
| Governance Foundation | Yes |
| Workflow & UX | Yes |
| Data, Matching & Storage | Yes |
| Security & Engineering Contracts | Yes |
| Quality, Operations & Design Freeze | **Not produced** — treated as Critical gap |

Document index at audit time: **46 draft_complete / 14 planned**.

---

## Finding Summary

| Severity | Count |
| --- | --- |
| Critical | 4 |
| High | 12 |
| Medium | 10 |
| Low | 6 |

---

## Critical Findings

### F-C01 — Quality/Ops/Freeze package absent

**What:** DOC-044–DOC-055 and DOC-059–DOC-060 remain `planned`. No test master plan, deployment architecture, runbooks, launch checklist, design freeze report, or implementation handoff.

**Why Critical:** Exit criteria for freeze explicitly require testing, operations, deployment, scorecard sign-off, and freeze approval. Implementation without these reintroduces guesswork the design-before-code protocol forbids.

**Mitigation:** Execute remediation build covering quality/ops docs + freeze package (or fold into `PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0`).

---

### F-C02 — Exact-match auto-link never closed

**What:** Matching workflow deferred auto-link to data design; matching engine deferred to security/engineering; security design listed it as still deferred. No Version 1 default is locked (auto-link vs always review).

**Why Critical:** Implementers will invent behavior. Wrong choice causes silent false merges or operational deadlock.

**Mitigation:** Lock V1 rule: e.g. **no automatic LINK without human confirmation** OR define E-1/E-2/E-3 as auto-link with explicit disqualifiers. Record Decision ID and update matching + security docs together.

---

### F-C03 — Shared database / RedDirt schema never audited

**What:** Architecture depends on controlled promotion into a shared canonical domain whose real tables, IDs, consent fields, and constraints are unknown. Docs correctly forbid assumed schema, but freeze/exit criteria require major decisions documented—and promotion contract cannot be implementation-ready without inspection.

**Why Critical:** Risk of redesigning promotion, uniqueness, and attribute models after coding starts.

**Mitigation:** Produce `PEOPLE_INTAKE_SHARED_DATABASE_COMPATIBILITY_REPORT.md` from read-only inspection of hosted Postgres (still no migrations). Until then, freeze remains blocked for canonical integration.

---

### F-C04 — Dual state vocabularies without a single authoritative map

**What:** UX/state docs use labels like `Assigned`, `In Progress`, `Entry Complete`. Engineering contracts use `READY_FOR_ENTRY`, `CLAIMED_FOR_ENTRY`, `ENTRY_IN_PROGRESS`, and promotion-pending concepts. `page-state-machine.json` and `entry-state-machine.json` omit promotion-pending / upload-failed states referenced elsewhere. Master plan lists yet another page enum set.

**Why Critical:** Impossible/conflicting workflow risk during implementation; trapped or unreachable states likely.

**Mitigation:** Publish one **canonical state dictionary** mapping user label ↔ internal enum ↔ allowed transitions ↔ owning service. Update all three layers to match. Reject any undocumented transition.

---

## High Findings

### F-H01 — Field condition `AMBIGUOUS` missing from UX/glossary

Data dictionary allows `PROVIDED|NOT_PROVIDED|UNREADABLE|AMBIGUOUS|CORRECTED`. Form UX only exposes Not Provided / Unreadable. Glossary omits Ambiguous.

**Mitigation:** Either add Ambiguous to UX + glossary, or remove from V1 data model.

### F-H02 — Consent UNKNOWN vs field UNREADABLE overlap

Field dictionary says UNKNOWN consent may mean blank, unreadable, ambiguous, or unclear. Separately, field conditions capture UNREADABLE. Operators may set contradictory combinations (e.g. Volunteer=YES with volunteer_condition=UNREADABLE).

**Mitigation:** Define validation: if condition is UNREADABLE/NOT_PROVIDED/AMBIGUOUS, response must be UNKNOWN (or null), and vice versa rules.

### F-H03 — Empty-page submit rules conflict

API submit example requires 1–10 entries unless blank-page exception. UX/workflows allow Mark Page Unreadable / blank page paths. Exact exception codes incomplete.

**Mitigation:** Define `BLANK_PAGE` / `UNREADABLE_PAGE` submit contracts with zero entries allowed and required reason.

### F-H04 — Match-review claiming underspecified

Queue doc says match claiming “may be detailed further.” Race of two reviewers on one entry is required by concurrency contract but not fully workflow-specified.

**Mitigation:** Mirror entry-claim model for match review items (atomic claim-next, TTL, release, admin override).

### F-H05 — Storage provider undecided

Architecture is provider-agnostic, but upload-intent, signed URL, HEIC conversion, and lifecycle depend on provider capabilities.

**Mitigation:** Choose provider (or shortlist with required capability matrix) before implementation wave 2.

### F-H06 — Retention periods undecided

Retention states exist; periods do not. Lifecycle deletion risk called out in storage audit questions remains open.

**Mitigation:** Owner-approved interim policy (e.g. retain originals until freeze+90 days post-completion, legal hold supported) before any lifecycle automation.

### F-H07 — “Optional by policy” authz holes

Data Entry may create batches / upload “Optional by policy” without a written policy.

**Mitigation:** V1 default: Data Entry **cannot** create batches or upload unless Admin grants an explicit capability flag.

### F-H08 — NO_MATCH auto-create undecided

Whether no-match auto-creates a person or requires reviewer Create New remains open.

**Mitigation:** Lock V1: NO_MATCH prepares recommendation; human (or Admin) confirms CREATE_NEW except where an approved feature flag enables auto-create in non-prod first.

### F-H09 — Preference supersession rules deferred

Unknown must not supersede Yes/No, but Yes/No supersession timing/rules incomplete.

**Mitigation:** Lock: newer explicit YES/NO with later `effective_at` supersedes prior explicit value; UNKNOWN never supersedes.

### F-H10 — Offline draft security unresolved for V1

Security says full offline may be deferred; UX promises weak-signal draft survival.

**Mitigation:** Lock V1: **online-required submit**; brief disconnect allows local draft buffer with clear “not synced” UI; no multi-day offline queue in V1.

### F-H11 — Promotion-pending page completeness not in UX states

Engineering: page not complete while promotion pending. UX page states jump Matching → Completed without PROMOTION_PENDING user label.

**Mitigation:** Add user label e.g. “Finishing” / “Updating people records” and admin visibility of promotion backlog.

### F-H12 — Dependency / monitoring / incident packages missing

Threat model defers incidents; no dependency plan, monitoring, or alert routing docs.

**Mitigation:** Include in quality/ops freeze package.

---

## Medium Findings

| ID | Finding | Mitigation |
| --- | --- | --- |
| F-M01 | Batch status enums differ slightly across docs (UPLOAD_PARTIAL vs Uploading) | Unify in state dictionary |
| F-M02 | Entry outcome “Exact Match” used as both state and outcome | Separate `match_outcome` from `entry_status` |
| F-M03 | Human-readable codes (`PI-…`) format not formally regex-specified | Add format contract |
| F-M04 | CSS breakpoints / perf thresholds deferred | Acceptable for freeze if non-blocking; set targets in quality doc |
| F-M05 | Admin “force-complete” exists without abuse criteria | Require reason + dual audit |
| F-M06 | Same-sheet in two batches edge case listed but resolution policy thin | Prefer duplicate-image warning + admin keep/discard |
| F-M07 | Reviewer “Optional” transcription in roles vs No claim in matrix | Align: Reviewer does not transcribe in V1 |
| F-M08 | Feature flags listed but no default environment matrix | Add env×flag table |
| F-M09 | Canonical merge “restricted separate process” undetailed | Explicitly out of V1 with pointer to future admin design |
| F-M10 | Diagrams folder largely empty despite ERD mermaid in docs | Acceptable; optional export to `diagrams/` |

---

## Low Findings

| ID | Finding |
| --- | --- |
| F-L01 | “Volunteer Sheet” vs “Page” both correct; reinforce in training |
| F-L02 | Some docs still say “next build PEOPLE-DATA…” historically in prose |
| F-L03 | Progress ledger percentages are approximate |
| F-L04 | Screen inventory JSON vs markdown could drift |
| F-L05 | Consider shortening security test list cross-links |
| F-L06 | GitHub remote now present; document in ops when freeze happens |

---

## What Survived Challenge (Strengths)

- Clear Capture / Transcribe / Match separation  
- Page as queue unit; ≤10 independent entries  
- Raw vs normalized separation; Unknown ≠ No  
- Controlled promotion (Model B) over unrestricted canonical writes  
- Household contact caution; no routine person merges  
- Private images + signed access intent  
- Deny-by-default server authorization philosophy  
- Idempotency/concurrency awareness for claims and promotion  
- H-drive protocol and design-before-code discipline  

These should be preserved; remediations must not collapse layers.

---

## Recommended Immediate Sequence

1. Remediate Critical + High findings in design docs (no code).  
2. Complete Quality/Ops/Freeze volume.  
3. Shared DB compatibility audit (read-only).  
4. Re-run architecture validation.  
5. Sign Design Freeze Approval only if scorecard targets met.  
6. Then Step 5B Cursor Build Orchestration.  
7. Only then Gate G-10 implementation.
