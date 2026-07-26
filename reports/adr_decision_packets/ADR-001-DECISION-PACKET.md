# ADR-001 Decision Packet

**Slice:** PEOPLE-G10-BLOCKER-REMEDIATION-PACKETS-1.0
**Status:** PROPOSED FOR STEVE DECISION
**Prepared against commit:** `c1c7c36`

## 1. Identity

| Field | Value |
| --- | --- |
| ADR ID | ADR-001 |
| Title | Application Framework |
| Current status | OPEN / PROPOSED (not accepted) |
| Decision owner | Steve |
| Prepared by | Burt (Cursor) |
| Prepared against commit | c1c7c36 |
| Classification | BLOCKING_G10 |

## 2. Decision question

Should **ADR-001** be accepted as the governing Decision Log decision for **Application Framework**?

If accepting the IS-101 recommendation: Accept Next.js + React + TypeScript as governing application framework

## 3. Background

- Why open: IS-101 recommendation recorded; Decision Log acceptance never completed.
- Why it matters: Determines app runtime, scaffolding, and ISSUE-PLATFORM-001
- Depends on: IS-101; related issues/catalogs; Phase 1-3 specs as applicable.
- What changed: Phase 3 logical persistence completed without selecting runtime stack; ADR remains OPEN.

## 4. Options

### Option 1

- Description: Accept IS-101 recommendation (Next.js+React+TS)
- G-10: Disposition in Decision Log does not alone open G-10.
- Reversibility: SUPERSEDE via new ADR if needed.

### Option 2

- Description: Reject and require alternate framework ADR revision
- G-10: Disposition in Decision Log does not alone open G-10.
- Reversibility: SUPERSEDE via new ADR if needed.

### Option 3

- Description: Defer with Decision Log waiver (not recommended for G-10)
- G-10: Disposition in Decision Log does not alone open G-10.
- Reversibility: SUPERSEDE via new ADR if needed.



## 5. Engineering recommendation

```text
ERNIE ENGINEERING RECOMMENDATION
```

Accept Next.js + React + TypeScript as governing application framework

This is **not** Steve's decision. Label: **PROPOSED FOR STEVE DECISION**.

## 6. Acceptance criteria (if Steve accepts)

1. Decision Log entry accepting ADR-001 with selected option.
2. ADR index status updated to ACCEPTED (or equivalent).
3. Related ISSUE-* disposition updated if applicable.
4. Catalog seed conflicts amended if required (esp. ADR-004/005).
5. Does **not** set applicationCodeAuthorized, open G-10, or approve design freeze by itself.

## 7. Decision recording template

```text
STEVE DECISION

Selected option:
Decision:
Conditions:
Effective date:
Follow-up required:
Authorized by:
Decision Log entry:
Commit:
```

Do not fill this block.

## 8. Traceability

- IS-101 ADR-001; `docs/adr/_index.md`
- `reports/PEOPLE_GATE_G10_READINESS_ASSESSMENT.md` (REMAIN CLOSED)
- `docs/08_implementation/PEOPLE_INTAKE_DESIGN_FREEZE_REPORT.md` (DENIED)
- G-10 effect: BLOCKING_G10 | MG effect: Blocks app scaffolding; not first MG DDL alone

```text
ACCEPTING THIS ADR DOES NOT OPEN GATE G-10
OPENING G-10 DOES NOT AUTHORIZE IMPLEMENTATION
```
