# Critical Issue Disposition Matrix

**Slice:** PEOPLE-G10-BLOCKER-REMEDIATION-PACKETS-1.0  
**Verified commit:** `c1c7c36`  
**Gate:** REMAIN CLOSED  
**Issues closed by this slice:** NONE

| Issue ID | Status | Classification | Why open | Conflict type | Decision owner | Evidence owner | Required resolution | Waiver permitted? | Valid waiver must contain | Mitigate w/o close? | G-10 consequence | MG consequence | Recommended next action | Dependency order | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ISSUE-FREEZE-001 | OPEN | BLOCKING_G10 | Freeze DENIED | Governance gate | Steve | Burt/Ernie | Freeze APPROVED | No | N/A | No | Direct block | All MG blocked | Complete ADR+issue remediations | After ADRs + DBA + Criticals | Freeze report; delta |
| ISSUE-PLATFORM-001 | OPEN | BLOCKING_G10 | ADR-001 open | Architecture decision | Steve | Burt | ADR-001 accept | No | N/A | No | Blocks | Scaffold | Steve ADR-001 packet | 1 | ADR-001 packet |
| ISSUE-DATABASE-001 | OPEN | BLOCKING_G10 / MG | ADR-002/003 open | Architecture decision | Steve | Burt | ADR-002/003 accept | No | N/A | No | Blocks | First MG | Steve ADR-002/003 | 3–4 | packets |
| ISSUE-AUTH-001 | OPEN | BLOCKING_G10 | Method unresolved | Product + security | Steve | Burt | ADR-004 + method | No | N/A | No | Blocks | Auth pkgs | Steve ADR-004 | 5 | packet |
| ISSUE-STORAGE-001 | OPEN | BLOCKING_G10 | Cat 4 vs private storage | Config conflict | Steve | Burt | ADR-005 + Cat 4 amend | Conditional | Explicit non-upload-core scope; DL | Partial | Blocks | Upload MG | Steve ADR-005 | 6 | packet |
| ISSUE-HDRIVE-001 | OPEN | BLOCKING_G10 | Guard not accepted | Tooling/governance | Steve | Burt | ADR-020 | No | N/A | No | Tooling block | Install/scaffold | Steve ADR-020 | 2 | packet |
| ISSUE-JOBS-001 | OPEN | CONDITIONAL | Runtime unselected | Implementation dependency | Steve | Burt | ADR-006 or DL defer | Yes | Defer past MG core; DL | Yes | Freeze unless deferred | Phase 7 | Defer w/ DL | After minimum ADRs | packet |
| ISSUE-CANONICAL-001 | OPEN | CONDITIONAL / PKG | Contract imprecise | Architecture + integration | Steve | Ernie | Contract + ADR-016 | Yes for soft-ref core | Soft-ref only; promo blocked | Soft-ref | Conditional | Promo MG | Soft-ref + contract work | Parallel | ADR-016; IS-303 |
| ISSUE-DBA-001 | OPEN | BLOCKING_MG | Audit not executed | Evidence gap | Steve | Burt→auditor | Execute plan; accept findings | No for mig auth | N/A | Plan only | Indirect / mig flag | First apply | Keep OPEN; plan ready | After ADR-002 | DBA plan |
| ISSUE-AUDIT-001 | MITIGATED | MITIGATED | Residual draft labels | Documentation conflict | Ernie/Steve | Burt | Freeze review | N/A | N/A | Yes (banners) | Freeze review item | Enum honesty | Retain until freeze | Before freeze APPROVED | IS-202 banners |
| ISSUE-RETENTION-001 | OPEN | DEFERRED | Durations unset | Business policy | Steve | Policy | Durations at launch | Yes | Launch deferral | Pattern via ADR-017 | Not direct G-10 | Launch | Defer | Launch | Cat 08 |
| ISSUE-MOD-001 | OPEN | BLOCKING_PACKAGE | Drafts vs transcriptions split | Architecture ownership | Steve/Ernie | Burt | Ownership Decision Log | Limited | Explicit module split | Docs only | Not direct if freeze allows | Entry pkgs | Disposition before entry impl | Before entry MG | IS-201 |
| ISSUE-REPO-002 | OPEN | BLOCKING_PACKAGE | gitignore depends on ADRs | Implementation dependency | Steve | Burt | After ADR-001/020 | Yes until scaffold | — | Yes | Indirect | Scaffold | After ADR-001/020 | After tooling ADRs | — |

```text
Plans and packets do not close issues.
```
