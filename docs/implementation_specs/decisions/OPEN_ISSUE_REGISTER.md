# Open-Issue Register

**Program:** PEOPLE-IMPLEMENTATION-SPECIFICATION-PROGRAM-1.0  
**Governed by:** PEOPLE-IS-004  
**Last Updated:** 2026-07-26

| Issue ID | Title | Severity | Blocking | Required By | Status |
| --- | --- | --- | --- | --- | --- |
| ISSUE-AUTH-001 | Authentication provider and session architecture not formally approved; auth **method** conflict (Google OAuth vs magic-link/password) unresolved in IS-101 | CRITICAL | Yes before Phase 9 / implementation | Phase 9 / ADR-004 | OPEN |
| ISSUE-STORAGE-001 | Object storage provider not formally approved; Catalog 4 `STORAGE_PROVIDER=Netlify` seed conflicts with private-image posture in IS-101 | CRITICAL | Yes before upload implementation | Upload IS / ADR-005 | OPEN |
| ISSUE-PLATFORM-001 | Application framework not Decision-Log accepted (IS-101 recommends Next.js+React+TS as PROPOSED) | CRITICAL | Yes before coding; recommendation recorded in IS-101 | IS-101 / ADR-001 | OPEN |
| ISSUE-DATABASE-001 | Database provider and access strategy not formally selected | CRITICAL | Yes before Phase 3 | Phase 3 / ADR-002/003 | OPEN |
| ISSUE-JOBS-001 | Background-job runtime not selected | CRITICAL | Yes before Phase 7 implementation readiness | Phase 7 / ADR-006 | OPEN |
| ISSUE-CANONICAL-001 | Canonical person integration boundary requires exact contract | CRITICAL | Yes before promotion implementation | Promotion IS | OPEN |
| ISSUE-RETENTION-001 | Exact retention durations require policy approval | HIGH | Yes before production launch; not blocking early docs | Launch | OPEN |
| ISSUE-NOTIFY-001 | Version 1 notification channels require formal selection | MEDIUM | No for docs; yes before notification implementation | Notify IS | OPEN |
| ISSUE-HDRIVE-001 | H-drive-only execution enforcement mechanism requires formal design; IS-104 documents operational standard; automated guard still pending ADR-020 | CRITICAL | Yes before development tooling / package installation | Phase 1 / ADR-020 / IS-104 | OPEN |
| ISSUE-CATALOG-009 | Catalog 09 Traceability DESIGN COMPLETE (foundation); full inventory remains amendment-driven | MEDIUM | No for library close; yes for claiming system-wide completeness | Amendments / IS phases | OPEN |
| ISSUE-REPO-001 | Target docs/ layout (master/volumes/…) not yet migrated from live Volume tree | MEDIUM | No for docs authorship; yes before layout cutover package | IS-100 follow-on | OPEN |
| ISSUE-REPO-002 | Exact .gitignore / cache env vars depend on framework ADRs | MEDIUM | Yes before app scaffolding | IS-101 / ADR-020 | OPEN |
| ISSUE-MOD-001 | Precise split of intake_entries ownership between MOD-DRAFTS and MOD-TRANSCRIPTIONS | HIGH | Yes before entry implementation packages | IS-200 / IS-201 / domain follow-on | OPEN |
| ISSUE-MOD-002 | Whether reports/exports use shared read models or dedicated views | MEDIUM | Yes before reports/exports packages | IS-102 / reporting IS | OPEN |
| ISSUE-GHN-001 | Optional rename of GitHub repo `people` → `people-intake-system` (IS-100 suggestion) | LOW | No | Ops / Decision Log | OPEN |
| ISSUE-GHN-002 | Optional migrate default branch `master` → `main` | LOW | No | Ops / Decision Log | OPEN |
| ISSUE-FREEZE-001 | Design freeze blocked pending Critical ADR/issue remediation via independent audit lane | CRITICAL | Yes before Gate G-10 | PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0 | OPEN |
| ISSUE-AUDIT-001 | Field dictionary / pre-catalog workflow status labels drift vs Catalog 01 (FIND-AUDIT-001/005) | MEDIUM | Yes before claiming enum finality | IS-202 / AUDIT-SLICE-002 | MITIGATED — banners + IS-202; retain until freeze review |
| ISSUE-DBA-001 | Shared DB compatibility audit not yet executed; conceptual tables must not be assumed to exist | HIGH | Yes before migrationsAuthorized | IS-300 / shared-DB audit | OPEN |

Related ADRs: ADR-001…ADR-020 in `DECISION_REGISTER.md`.  
Audit lane charter: `docs/00_governance/lanes/PEOPLE_AUDIT_REMEDIATION_AND_QUALITY_OPS_FREEZE.md`.  
Latest findings: `reports/PEOPLE_AUDIT_SLICE_006_FINDINGS.md`.
