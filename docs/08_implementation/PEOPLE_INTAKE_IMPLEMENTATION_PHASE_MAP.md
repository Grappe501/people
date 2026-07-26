# People Intake — Implementation Phase Map

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-CURSOR-BUILD-ORCHESTRATION-1.0  
**Authority:** Summary map. Full playbook: `PEOPLE_INTAKE_CURSOR_BUILD_ORCHESTRATION.md`

---

## Hard Gate

| Condition | Required |
| --- | --- |
| Design freeze APPROVED | Yes |
| Gate G-10 open | Yes |
| `applicationCodeAuthorized` | true |

Until then: **no Phase 0+ application code.**

---

## Phase Sequence

| Phase | Name | RC relevance |
| --- | --- | --- |
| 0 | Project Foundation | — |
| 1 | Authentication & Authorization | RC1 |
| 2 | Storage Foundation | RC1 |
| 3 | Batch Management | RC1 |
| 4 | Queue & Claim System | RC1 |
| 5 | Transcription | RC1 |
| 6 | Matching Engine | RC2 |
| 7 | Canonical Promotion | RC2 |
| 8 | Administration | RC3 |
| 9 | Operations | RC4 |
| 10 | Accessibility & UX Polish | RC4 |
| 11 | Performance & Hardening | RC4 |
| 12 | Launch Readiness | RC5 |

---

## Release Candidates

| RC | Exit meaning |
| --- | --- |
| RC1 | Core capture + queue + transcription |
| RC2 | Matching + promotion |
| RC3 | Administration |
| RC4 | Ops hardening + a11y/perf |
| RC5 | Launch candidate |

---

## Ledger

Track slices in `PEOPLE_INTAKE_IMPLEMENTATION_LEDGER.md` and `contracts/governance/implementation-ledger.json`.
