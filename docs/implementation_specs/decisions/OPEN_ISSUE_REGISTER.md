# Open-Issue Register

**Program:** PEOPLE-IMPLEMENTATION-SPECIFICATION-PROGRAM-1.0  
**Governed by:** PEOPLE-IS-004  
**Last Updated:** 2026-07-26  
**Triage authority:** AUDIT-SLICE-009 / PEOPLE-GATE-G10-READINESS-ASSESSMENT-1.0 (D-078)

**Triage classes:** `BLOCKING_G10` | `BLOCKING_MG` | `BLOCKING_PACKAGE` | `CONDITIONAL` | `DEFERRED` | `MITIGATED`

| Issue ID | Title | Severity | Triage | Required By | Status |
| --- | --- | --- | --- | --- | --- |
| ISSUE-AUTH-001 | Authentication provider/session; method conflict unresolved | CRITICAL | BLOCKING_G10 | Phase 9 / ADR-004 | OPEN |
| ISSUE-STORAGE-001 | Object storage not approved; Cat 4 Netlify seed conflict | CRITICAL | BLOCKING_G10 (CONDITIONAL for non-upload core only with Owner waiver) | Upload IS / ADR-005 | OPEN |
| ISSUE-PLATFORM-001 | Application framework not Decision-Log accepted | CRITICAL | BLOCKING_G10 | IS-101 / ADR-001 | OPEN |
| ISSUE-DATABASE-001 | Database provider/access not formally selected | CRITICAL | BLOCKING_G10 / BLOCKING_MG | Physical schema / ADR-002/003 (Phase 3 **docs** completed technology-neutral; selection still required before G-10) | OPEN |
| ISSUE-JOBS-001 | Background-job runtime not selected | CRITICAL | DEFERRED (with Decision Log) past first MG core; BLOCKING_PACKAGE for Phase 7 | Phase 7 / ADR-006 | OPEN |
| ISSUE-CANONICAL-001 | Canonical person integration boundary requires exact contract | CRITICAL | CONDITIONAL for core soft-ref; BLOCKING_PACKAGE for promotion | Promotion IS / ADR-016 | OPEN |
| ISSUE-RETENTION-001 | Exact retention durations require policy approval | HIGH | DEFERRED to launch | Launch / ADR-017 | OPEN |
| ISSUE-NOTIFY-001 | V1 notification channels require formal selection | MEDIUM | DEFERRED | Notify IS / ADR-007 | OPEN |
| ISSUE-HDRIVE-001 | H-drive enforcement mechanism; automated guard pending | CRITICAL | BLOCKING_G10 tooling | ADR-020 / IS-104 | OPEN |
| ISSUE-CATALOG-009 | Catalog 09 full inventory amendment-driven | MEDIUM | DEFERRED | Amendments | OPEN |
| ISSUE-REPO-001 | Target docs/ layout migration | MEDIUM | DEFERRED | IS-100 follow-on | OPEN |
| ISSUE-REPO-002 | Exact .gitignore / cache env vars depend on framework ADRs | MEDIUM | BLOCKING_PACKAGE scaffolding | IS-101 / ADR-020 | OPEN |
| ISSUE-MOD-001 | intake_entries ownership split MOD-DRAFTS vs MOD-TRANSCRIPTIONS | HIGH | BLOCKING_PACKAGE entry impl | IS-200 / IS-201 | OPEN |
| ISSUE-MOD-002 | Reports/exports shared RM vs dedicated views | MEDIUM | DEFERRED | IS-304 amendment / reporting | OPEN |
| ISSUE-GHN-001 | Optional rename GitHub repo | LOW | DEFERRED | Ops | OPEN |
| ISSUE-GHN-002 | Optional migrate default branch master→main | LOW | DEFERRED | Ops | OPEN |
| ISSUE-FREEZE-001 | Design freeze blocked pending Critical ADR/issue remediation | CRITICAL | BLOCKING_G10 | Audit/freeze lane | OPEN |
| ISSUE-AUDIT-001 | Field-dictionary status labels vs Catalog 01 | MEDIUM | MITIGATED — retain until freeze review | IS-202 / audit | MITIGATED |
| ISSUE-DBA-001 | Shared DB compatibility audit not executed | HIGH | BLOCKING_MG / migrationsAuthorized | Shared-DB audit | OPEN |

Related ADRs: ADR-001…ADR-020 all **OPEN / PROPOSED** (`docs/adr/_index.md`).  
G-10 readiness: `reports/PEOPLE_GATE_G10_READINESS_ASSESSMENT.md` — **REMAIN CLOSED**.  
Latest findings: `reports/PEOPLE_AUDIT_SLICE_010_FINDINGS.md`.  
Steve decision surface: `reports/PEOPLE_STEVE_G10_DECISION_DASHBOARD.md`.  
G-10 blocker register: `reports/PEOPLE_GATE_G10_BLOCKER_MASTER_REGISTER.md`.

Phase 3 documentation complete (IS-300…305). Gate G-10 remains CLOSED. Implementation Authorization is a separate Steve decision.  
**G-10 blocker remediation packets prepared — no issues closed by packet creation alone.**
