# People Intake — Architecture Readiness Scorecard

**Audit:** PEOPLE-ARCHITECTURE-AUDIT-AND-DESIGN-VALIDATION-1.0  
**Target:** ≥95 per domain for freeze, or documented justification  

| Domain | Score | Target | Gap drivers | Freeze ready? |
| --- | ---: | ---: | --- | --- |
| Governance | 92 | 100 | Freeze/approval process incomplete; quality volume missing | No |
| UX | 88 | 100 | AMBIGUOUS gap; offline ambiguity; promotion-pending UX | No |
| Workflow | 90 | 100 | Match claim gap; blank submit; state dual-track | No |
| Data Model | 91 | 100 | Physical schema unknown; AMBIGUOUS coupling | No |
| Matching | 82 | 100 | Auto-link & NO_MATCH create unlocked | No |
| Canonical Integration | 78 | 100 | No shared DB audit; transport undecided | No |
| Storage | 85 | 100 | Provider & retention periods open | No |
| Security | 90 | 100 | Numeric TTLs open; incident runbook missing; solid model | No* |
| API Design | 88 | 100 | Contracts conceptual; blank-page endpoint rules incomplete | No |
| Services | 90 | 100 | Boundaries clear; job host deferred | No* |
| Operations | 35 | 100 | Volume largely unwritten | No |
| Testing | 40 | 100 | No master plan/catalog; only requirement lists | No |
| Accessibility | 75 | 100 | Spec exists; verification plan missing | No |
| Deployment | 30 | 100 | No deployment architecture/runbooks | No |
| Documentation | 80 | 100 | Strong volume 0–6; contradictions; empty ops volume | No |

\*Security/Services conceptually strong but cannot freeze while dependent Criticals open.

### Weighted overall (equal weight)

**Approximately 76 / 100** — **below freeze threshold**.

### Justification rule

Scores &lt; 95 require remediation or formal Owner acceptance with residual risk. **No domain currently meets both ≥95 and empty blocking decisions.**
