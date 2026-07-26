# Gate G-10 Remediation Execution Queue

**Slice:** PEOPLE-G10-BLOCKER-REMEDIATION-PACKETS-1.0  
**Verified commit:** `c1c7c36`  
**Canonical order:** `docs/00_governance/PEOPLE_GATE_G10_REMEDIATION_PLAN.md`

```text
Later items are NOT actionable until earlier exit criteria pass.
```

| ID | Objective | Owner | Dependencies | Inputs | Outputs | Entry criteria | Exit criteria | Validation | Commit evidence | Steve? | Ernie? | Burt independent? | Status | Blocked-by | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G10-REM-001 | Disposition blocking ADRs (min 001–005, 020; then CONDITIONAL set) | Steve | Packets ready | ADR packets; index; dashboard | Decision Log entries | Packets committed | ADRs accepted or DL deferred | ADR index updated | DL commits | YES | Review recs | Packets only | **READY FOR STEVE** | — | Steve decision pass |
| G10-REM-002 | ISSUE-DBA-001 evidence + disposition | Steve + auditor | ADR-002 posture | DBA plan | Audit report; issue update | Plan exists; access/inventory authorized later | Issue dispositioned | Report review | Audit report commit | YES outcome | Interpret | Plan done; exec later | **PLAN READY / EXEC BLOCKED** | Access not authorized this slice | Authorize read-only audit later |
| G10-REM-003 | Critical issue disposition | Steve | REM-001 | Disposition matrix | Register updates | ADRs moving | Criticals closed/waived | Register | Commits | YES | Classify | Docs only | **BLOCKED** | REM-001 | After ADR pass |
| G10-REM-004 | Design freeze approval review | Steve | REM-001…003 | Freeze delta | Freeze APPROVED | Exit criteria met | Sign-off | Freeze report | Commit | YES | Prepare | Cannot approve | **BLOCKED** | REM-001…003 | — |
| G10-REM-005 | Fresh Gate G-10 assessment | Burt/Ernie | REM-004 | New evidence | D-079+ assessment | Freeze APPROVED path | OPEN / OPEN WITH CONDITIONS / REMAIN CLOSED | Same rubric | Report commit | No (assess) | Interpret | Execute assessment | **BLOCKED** | REM-004 | — |
| G10-REM-006 | Implementation Authorization | Steve | REM-005 OPEN | Assessment | YES/NO | G-10 OPEN | DL authorization | Flags | Commit | YES | Advise | No | **BLOCKED** | REM-005 | — |
| G10-REM-007 | First MG-* translation | Burt | REM-006 YES | IS-301…305; MG card | Schema artifacts | migrationsAuthorized | MG complete+evidence | IS-305 seq | Commits | Prior YES | Review | After auth only | **BLOCKED** | REM-006 | — |

### Permanently blocked until sequence advances

```text
Fresh G-10 reassessment
Implementation Authorization
First MG-* package
Physical schema work
Migration execution
Application implementation
```
