# People Intake — Master Cursor Build Orchestration

**Design ID:** PEOPLE-CURSOR-BUILD-ORCHESTRATION-1.0  
**Library volume:** 7 — Master Cursor Build Orchestration  
**Project root:** `H:\people`  
**Status:** IMPLEMENTATION ORCHESTRATION (prepared)  
**Supreme companion:** Volume 0 — `PEOPLE_INTAKE_PROJECT_CONSTITUTION.md` — **read before every session**; this playbook does not replace it.  
**Library map:** `docs/00_governance/PEOPLE_INTAKE_DOCUMENTATION_LIBRARY.md`

---

## Prerequisites (Hard Gate)

This playbook **governs implementation only when all are true**:

| Prerequisite | Current status (2026-07-25) |
| --- | --- |
| Steps 1–4 design volumes complete | Met (draft_complete) |
| Step 5 Quality/Ops/Freeze package complete | **Not met** |
| Step 5A Architecture Audit passed | **Failed** (Critical findings open) |
| Design freeze APPROVED (Gate G-9) | **DENIED** |
| Implementation authorized (Gate G-10) | **CLOSED** |
| `applicationCodeAuthorized` in active-build | **false** |

Until prerequisites flip to pass:

```text
ALLOWED: documentation, remediation, contracts, orchestration maintenance
FORBIDDEN: src/, prisma/, migrations, live auth/storage, Netlify app feature deploys
```

**Next required build before Phase 0 code:**  
`PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0`

After freeze APPROVED, set active-build `applicationCodeAuthorized: true` and begin Phase 0.

---

## 1. Governing Build Rules

Every implementation slice must:

1. Begin from the **frozen** approved design.  
2. Stay within defined scope.  
3. Update documentation when behavior changes.  
4. Pass validation before continuing.  
5. Preserve backward compatibility within the active build.  
6. Never invent undocumented architecture.

If implementation reveals a design flaw:

1. Stop implementation.  
2. Document the issue (Decision Log + Risk Register).  
3. Update the design.  
4. Re-approve affected freeze scope.  
5. Resume implementation.

---

## 2. Workspace Rules

All project-controlled files root under:

```text
H:\people
```

Target repository shape after Gate G-10 (not before):

```text
docs/
develop_notes/
contracts/
reports/
scripts/
src/                 # only after G-10
tests/               # only after G-10
database/            # or prisma/ per freeze — only after G-10
storage/             # adapters only after G-10
.github/             # CI after G-10
netlify/             # functions after G-10
public/              # static only; never source images
```

H-drive protocol remains permanent. No intentional writes to `C:\`.

Remote: https://github.com/Grappe501/people

---

## 3. Git Workflow

Every completed implementation slice:

1. Pass local validation  
2. Update documentation  
3. Commit with descriptive message  
4. Push to GitHub  
5. Trigger Netlify preview (when configured)  
6. Verify deployment status  
7. Record progress in implementation ledger  

### Commit message format

```text
BUILD-0.1 Project foundation scaffolding
AUTH-1.2 Enforce role matrix on API routes
QUEUE-4.1 Atomic claim-next service
MATCH-6.3 Household shared-phone guard
PROMO-7.2 Idempotent create-person promotion
```

Preferred pattern: `{AREA}-{phase}.{slice} Short description`

---

## 4. Build Phases (Thirteen)

Implementation order after Gate G-10. Do not skip gates between phases.

### Phase 0 — Project Foundation

**Deliverables:** Repo structure under authorization · tooling · lint · format · env validation · build scripts · doc framework hooks  

**Validation:** Project builds · no runtime errors on boot shell · documentation index current · H-drive preflight passes  

**Depends on:** Freeze APPROVED  

---

### Phase 1 — Authentication & Authorization

**Deliverables:** Auth · approved users · roles · sessions · route protection  

**Validation:** Unauthorized blocked · role matrix enforced · access-denied audited · disabled users denied  

**Maps to design:** Auth architecture · Authorization matrix  

---

### Phase 2 — Storage Foundation

**Deliverables:** Private image storage · upload intents · metadata · derivative pipeline · content hash  

**Validation:** Private store · signed access · hash duplicate detect · no public URLs  

**Maps to:** Image storage architecture · upload security  

---

### Phase 3 — Batch Management

**Deliverables:** Batch create · metadata · page registration · upload workflow · batch status  

**Validation:** Multi-batch · accurate progress · upload recovery · partial failure handling  

---

### Phase 4 — Queue & Claim System

**Deliverables:** Queue engine · claim-next · renew · expire · reassign · match-claim if frozen  

**Validation:** No duplicate claims · concurrency tests · expired claim recovery · stale write rejection  

---

### Phase 5 — Transcription

**Deliverables:** Page workspace · draft autosave · field validation · normalization · submit  

**Validation:** Draft preserved · no lost data · ≤10 entries · blank/unreadable page paths · version conflicts handled  

---

### Phase 6 — Matching Engine

**Deliverables:** Candidate search · confidence tiers · reviewer workspace · resolution engine  

**Validation:** Stable ranking · household protections · exact rules per **frozen** policy · no silent merges  

---

### Phase 7 — Canonical Promotion

**Deliverables:** Promotion requests · canonical integration · provenance · attribute updates  

**Validation:** Safe create · correct link · idempotent retry · page not complete while promotion pending  

---

### Phase 8 — Administration

**Deliverables:** Dashboard · users · queue/batch monitoring · audit viewer  

**Validation:** Admin workflows · permissions · audited overrides  

---

### Phase 9 — Operations

**Deliverables:** Monitoring · logging · retries · error dashboards · background jobs  

**Validation:** Failure recovery · job retry · alerts · no PII in logs  

---

### Phase 10 — Accessibility & UX Polish

**Deliverables:** Keyboard · screen reader · responsive · error copy · polish  

**Validation:** A11y review · mobile capture/entry paths  

---

### Phase 11 — Performance & Hardening

**Deliverables:** Query/image optimization · caching · security review · load testing  

**Validation:** Perf targets · security checklist  

---

### Phase 12 — Launch Readiness

**Deliverables:** Final docs · operator manuals · training · backup/DR test · release checklist  

**Validation:** Production readiness · design compliance  

---

## 5. Slice Structure (Mandatory Template)

Every Cursor implementation slice must include in its develop note or PR body:

### Objective
What is being built?

### Scope
Exactly what is included.

### Out of Scope
Explicit exclusions.

### Files Expected
Created or modified paths.

### Validation Commands
Commands to run (with H-drive env).

### Manual Tests
Human verification steps.

### Rollback Plan
How to safely undo.

### Documentation Updates
Which docs change.

### Exit Criteria
Conditions before moving on.

---

## 6. Validation Gates (Every Phase)

| Gate | Requirement |
| --- | --- |
| Build | Project compiles / builds |
| Type | No type errors |
| Test | Automated tests for the phase pass |
| Documentation | Docs + progress ledger updated |
| Accessibility | Applicable checks pass |
| Security | Required controls verified for slice |
| Deployment | Preview deployment succeeds (once Netlify wired) |

**Only then** may the next phase begin.

Suggested local prelude (post G-10):

```powershell
$env:TEMP="H:\people\.tmp"
$env:TMP="H:\people\.tmp"
$env:TMPDIR="H:\people\.tmp"
$env:npm_config_cache="H:\people\.npm-cache"
npm run drive:validate
npm run lint
npm run typecheck
npm test
```

Exact script names are established in Phase 0.

---

## 7. Cursor Operating Rules

Cursor must:

- Read Volume 0 constitution + frozen design before coding  
- Avoid architectural changes  
- Keep implementations focused  
- Prefer small, reviewable commits  
- Preserve comments for non-obvious logic  
- Never remove functionality without explicit approval  
- Never bypass validation gates  
- Never set `applicationCodeAuthorized` itself without Owner freeze process  

---

## 8. Documentation Discipline

Each completed slice updates:

- Progress ledger  
- Implementation ledger  
- Changelog (when introduced)  
- Architecture references if needed  
- API docs if endpoints change  
- Operator docs if workflows change  

Documentation is a deliverable, not an afterthought.

---

## 9. Testing Discipline

Alongside each phase:

- Unit tests for new logic  
- Integration tests for interactions  
- Workflow tests for user journeys  
- Regression tests for prior phases  

No phase relies solely on manual testing.

Critical scenarios from design (claims, idempotency, promotion retry, image authz, etc.) must appear in automated suites by the phase that introduces them.

---

## 10. Deployment Discipline

- Preview after each completed phase (once configured)  
- Production requires: all validations · approved RC · updated docs · completed release checklist · Owner approval  
- Separate secrets per environment; no silent production fallbacks  

---

## 11. Progress Tracking

Living ledger: `docs/08_implementation/PEOPLE_INTAKE_IMPLEMENTATION_LEDGER.md`

Fields:

```text
Phase | Slice | Status | Owner | Started | Completed | Validation | Deployment | Notes
```

Status values:

```text
NOT_STARTED | IN_PROGRESS | BLOCKED | READY_FOR_REVIEW | COMPLETE
```

Machine companion: `contracts/governance/implementation-ledger.json`

---

## 12. Risk Tracking

Implementation risks append to `reports/PEOPLE_RISK_REGISTER.md` with:

Description · Severity · Probability · Mitigation · Status · Linked slice  

Carry forward unresolved audit risks (R-001+) until closed.

---

## 13. Release Candidates

| RC | Meaning |
| --- | --- |
| RC1 | Core capture + queue + transcription complete |
| RC2 | Matching complete |
| RC3 | Administration complete |
| RC4 | Operational hardening complete |
| RC5 | Launch candidate |

Each RC is tested against the full Capture → Transcribe → Match → Promote → Audit journey.

---

## 14. Acceptance Checklist

Implementation complete only when:

- [ ] All planned phases complete  
- [ ] All validation gates passed  
- [ ] All automated tests pass  
- [ ] Documentation current  
- [ ] Accessibility review complete  
- [ ] Security review complete  
- [ ] Performance goals met  
- [ ] Backup/recovery verified  
- [ ] Deployment procedures documented  
- [ ] Implementation matches approved frozen design  

---

## 15. Success Criteria

Success when:

1. A volunteer sheet can be photographed, uploaded, transcribed, reviewed, matched, promoted to the canonical people domain, and fully audited without data loss.  
2. Every significant action is traceable.  
3. Every workflow has documented recovery.  
4. Implementation remains faithful to approved architecture.  
5. Future enhancements (OCR, AI assist, etc.) can extend without foundation redesign.

---

## 16. Phase-to-Design Map

| Phase | Primary design authorities |
| --- | --- |
| 0 | Constitution, H-drive, build gates |
| 1 | Auth architecture, authorization matrix |
| 2 | Image storage, upload security, privacy |
| 3 | Capture workflow, batch data design |
| 4 | Queue/claiming, concurrency, state machines |
| 5 | Transcription UX, form behavior, validation |
| 6 | Matching engine, matching workflow |
| 7 | Canonical contract, promotion, provenance |
| 8 | Admin UX, authz matrix admin section |
| 9 | Logging/audit, background jobs, error contract |
| 10 | Accessibility, UX architecture, copy guide |
| 11 | Threat model, security tests, perf targets (quality docs) |
| 12 | Operator manual, launch checklist, runbooks |

---

## 17. First Slice After Gate G-10 (Preview)

When authorized, open with:

```text
BUILD-0.1 Foundation scaffolding under H:\people
```

Scope: app shell, tooling, env validation, CI stub, no feature UI.  
Out of scope: auth provider live wiring unless already freeze-approved for Phase 0/1 overlap.  
Exit: build + type + drive validate + empty forbidden-path check.

---

## 18. Orchestration Status Record

| Field | Value |
| --- | --- |
| Orchestration written | Yes |
| Orchestration active for coding | **No** (awaiting freeze) |
| Blocking next action | Audit remediation + quality/ops + freeze re-approval |
