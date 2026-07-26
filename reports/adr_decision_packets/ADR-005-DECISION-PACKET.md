# ADR-005 Decision Packet

**Slice:** PEOPLE-G10-BLOCKER-REMEDIATION-PACKETS-1.0
**Status:** PROPOSED FOR STEVE DECISION
**Prepared against commit:** `c1c7c36`

## 1. Identity

| Field | Value |
| --- | --- |
| ADR ID | ADR-005 |
| Title | Object Storage |
| Current status | OPEN / PROPOSED (not accepted) |
| Decision owner | Steve |
| Prepared by | Burt (Cursor) |
| Prepared against commit | c1c7c36 |
| Classification | BLOCKING_G10 |

## 2. Decision question

Should **ADR-005** be accepted as the governing Decision Log decision for **Object Storage**?

If accepting the IS-101 recommendation: Accept private object storage adapter; forbid public Netlify assets for source images

## 3. Background

- Why open: IS-101 recommendation recorded; Decision Log acceptance never completed.
- Why it matters: ISSUE-STORAGE-001; Catalog 4 STORAGE_PROVIDER=Netlify seed conflict
- Depends on: IS-101; related issues/catalogs; Phase 1-3 specs as applicable.
- What changed: Phase 3 logical persistence completed without selecting runtime stack; ADR remains OPEN.

## 4. Options

### Option 1

- Description: Accept private storage adapter (provider brand TBD)
- G-10: Disposition in Decision Log does not alone open G-10.
- Reversibility: SUPERSEDE via new ADR if needed.

### Option 2

- Description: Accept named private provider now
- G-10: Disposition in Decision Log does not alone open G-10.
- Reversibility: SUPERSEDE via new ADR if needed.

### Option 3

- Description: Waive for non-upload core schema only (Owner Decision Log)
- G-10: Disposition in Decision Log does not alone open G-10.
- Reversibility: SUPERSEDE via new ADR if needed.

### Option 4

- Description: Reject / revise
- G-10: Disposition in Decision Log does not alone open G-10.
- Reversibility: SUPERSEDE via new ADR if needed.



## 5. Engineering recommendation

```text
ERNIE ENGINEERING RECOMMENDATION
```

Accept private object storage adapter; forbid public Netlify assets for source images

This is **not** Steve's decision. Label: **PROPOSED FOR STEVE DECISION**.

## 6. Acceptance criteria (if Steve accepts)

1. Decision Log entry accepting ADR-005 with selected option.
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

- IS-101 ADR-005; `docs/adr/_index.md`
- `reports/PEOPLE_GATE_G10_READINESS_ASSESSMENT.md` (REMAIN CLOSED)
- `docs/08_implementation/PEOPLE_INTAKE_DESIGN_FREEZE_REPORT.md` (DENIED)
- G-10 effect: BLOCKING_G10 | MG effect: Blocks upload/image packages

```text
ACCEPTING THIS ADR DOES NOT OPEN GATE G-10
OPENING G-10 DOES NOT AUTHORIZE IMPLEMENTATION
```
