# PEOPLE-IS-105 — GITHUB AND NETLIFY ARCHITECTURE

**Title:** GitHub and Netlify Architecture  
**Document ID:** `PEOPLE-IS-105-GITHUB-AND-NETLIFY-ARCHITECTURE-1.0`  
**Version:** 1.0  
**Status:** APPROVED  
**Phase:** PHASE 1 — REPOSITORY AND PLATFORM ARCHITECTURE  
**Project Root:** `H:\people`  
**Owner:** People Intake System Program  
**Approval Authority:** Decision Log D-068  
**Created Date:** 2026-07-26  
**Last Updated:** 2026-07-26  
**Governing Documents:** IS-000; IS-100; IS-101 (ADR-009); IS-103; IS-104; D-018; D-065; PEOPLE-PROTOCOL-COMMIT-PUSH-DEPLOY-1.0  
**Dependencies:** IS-104 APPROVED (D-067); D-018 accepted (dedicated Netlify); ADR-009 remains OPEN for technology-lock packaging  
**Implementation Authorization:** `IMPLEMENTATION NOT AUTHORIZED` (architecture documentation approved; workflows, `netlify.toml`, site linking, and live deploys not authorized)

```text
DESIGN COMPLETE
APPROVED FOR DOCUMENTATION GOVERNANCE
PLATFORM SOURCE-CONTROL AND DEPLOYMENT MODEL LOCKED
APPLICATION IMPLEMENTATION NOT AUTHORIZED
GITHUB ACTIONS / NETLIFY WIRING NOT AUTHORIZED
DEPLOYMENT AUTHORIZATION REMAINS CLOSED
```

---

## 1. Purpose

Define the canonical source-control and deployment architecture for People Intake so that GitHub remains the engineering system of record and Netlify remains a dedicated, environment-isolated hosting surface — before any application implementation is authorized — without architectural ambiguity for Burt.

## 2. Scope

Repository topology; branch strategy and protection; commit conventions; release tagging; GitHub Actions governance; Netlify environment architecture (Preview / Staging / Production); environment-variable governance; deployment promotion rules; rollback strategy; artifact provenance; deployment verification; secrets-management boundaries; evidence collection for every deployment; future multi-environment scaling without changing the architectural model; honest limits for remote runners vs H-drive workspace rules.

## 3. Out of Scope

* Creating `.github/workflows/*`, `netlify.toml`, or linking a live Netlify site  
* Provisioning production/staging secrets or domains  
* Authorizing application implementation or Gate G-10 opening  
* Selecting auth/storage/job providers (ADR queue)  
* Guaranteeing that GitHub Actions or Netlify build agents execute on `H:\people` (they cannot; see §9.2)

## 4. Governing References

IS-100 §§9.11, deployment tree; IS-103 environment classes; IS-104 H-drive protocol (developer machines); D-018 dedicated Netlify; D-065 closeout; ADR-009 hosting recommendation; Cursor Execution Protocol (Burt execution authority within governance).

## 5. Definitions

| Term | Meaning |
| --- | --- |
| Canonical remote | Git remote `origin` for this project |
| Canonical integration branch | Long-lived branch that receives reviewed merges and (when authorized) Production builds |
| Deployable surface | Source-controlled app/docs publish config (e.g. `netlify.toml` + authorized publish root) explicitly authorized for Netlify |
| Preview | Ephemeral PR/branch verification deploy (IS-103) |
| Staging | Persistent pre-production verification (IS-103) |
| Production | Live constituent-facing context (IS-103) |
| Provenance record | Evidence linking Git SHA ↔ Netlify deploy ID ↔ environment ↔ validation |
| Project-controlled deploy config | Repo files and documented Netlify/GitHub settings we own |
| Remote execution exception | CI/CD agents that necessarily run outside `H:\people` |

## 6. Assumptions

* GitHub hosts the exclusive engineering history for People Intake.  
* Dedicated Netlify site remains preferred (D-018).  
* Developer machines obey IS-104; CI/CD agents do not have `H:`.  
* `applicationCodeAuthorized` and `deploymentAuthorized` remain false until Gate G-10 / Decision Log change.  
* Current remote URL and default branch are operational facts and are governed honestly (see §9.3–9.4).

## 7. Functional Requirements

| ID | Description |
| --- | --- |
| REQ-GHN-001 | People Intake MUST use a single governing GitHub repository for the product (current topology). Future packages MAY add in-repo workspaces without creating a second governing product repo. |
| REQ-GHN-002 | The canonical remote MUST be the Decision-Log-recognized GitHub URL (today: `https://github.com/Grappe501/people.git`). |
| REQ-GHN-003 | The canonical integration branch MUST be Decision-Log recognized (today: `master`). Rename to `main` requires an explicit Decision Log entry. |
| REQ-GHN-004 | Feature, fix, docs, and release work MUST use named branch prefixes (`feature/*`, `fix/*`, `docs/*`, `release/*`) when branching from the integration branch. |
| REQ-GHN-005 | Commit messages MUST identify the governing work item for documentation slices (`docs(<work-item>): …`) and MUST follow conventional commit types when application work is authorized. |
| REQ-GHN-006 | Application release tags MUST use `vMAJOR.MINOR.PATCH` and MUST point at an immutable Git SHA. Tags MUST NOT be created to invent a deployable surface. |
| REQ-GHN-007 | GitHub Actions workflows MUST NOT be added until an authorized implementation package names allowed workflows, paths, and secrets. |
| REQ-GHN-008 | When authorized, CI MUST validate before merge/deploy evidence is claimed; Production deploy automation MUST require explicit deployment authorization. |
| REQ-GHN-009 | Netlify MUST be a dedicated People Intake site (D-018), not a shared SOSWebsite/RedDirt site with inherited secrets. |
| REQ-GHN-010 | Netlify MUST map to IS-103 classes: Preview, Staging, and Production with separate secret/data boundaries. |
| REQ-GHN-011 | Preview success MUST NOT authorize Production release (IS-103 REQ-ENV-007). |
| REQ-GHN-012 | Production deployment MUST require explicit authorization and a complete evidence record. |
| REQ-GHN-013 | Every authorized deployment MUST record provenance: Git SHA, branch/tag, environment, Netlify deploy ID (or equivalent), actor, timestamp, validation result. |
| REQ-GHN-014 | Rollback MUST be defined for Netlify publish artifacts (previous deploy / pinned SHA redeploy). Data/migration rollback remains a separate package concern. |
| REQ-GHN-015 | Secrets MUST live in GitHub Secrets and/or Netlify environment variables — never in Git, docs, or completion reports. |
| REQ-GHN-016 | Until an authorized deployable surface exists, D-065 Netlify closeout MUST report `NOT APPLICABLE`. |
| REQ-GHN-017 | Burt MUST execute validate → commit → push → remote verify → deploy-when-applicable without waiting for operator prompts, except at reserved governance gates (§9.15). |
| REQ-GHN-018 | Multi-environment growth (extra staging brands, secondary Netlify site, additional protected branches) MUST preserve the same environment-class model and evidence rules. |

## 8. Nonfunctional Requirements

| ID | Description |
| --- | --- |
| NFR-GHN-AUDIT-001 | Deployment and merge evidence must be reconstructible from Git + deployment reports. |
| NFR-GHN-SEC-001 | Least privilege for tokens; Production secrets isolated from Preview/Staging. |
| NFR-GHN-OPS-001 | Operators can identify environment from deploy URL, Netlify context, and evidence file. |
| NFR-GHN-SCALE-001 | Architecture remains valid when adding packages/workspaces inside one repo. |
| NFR-GHN-HONEST-001 | Specs MUST NOT claim CI/CD agents execute under `H:\people`. |

## 9. Architecture

### 9.1 System roles

```text
GitHub  = system of record (source, PRs, reviews, Actions history, releases)
Netlify = hosting / preview / publish surface (when authorized)
H:\people = developer workspace (IS-104)
IS-103  = environment classes (Local / Preview / Staging / Production)
D-065   = closeout evidence chain
```

Netlify is **not** source of truth for schemas, documentation, migration state, or Decision Log history.

### 9.2 Honest limitation — remote execution (locked)

```text
Enforceable on developer machines (IS-104):
  Project-controlled artifacts stay under H:\people.

Expected and allowed on remote agents:
  GitHub Actions runners and Netlify build/deploy agents execute outside H:\people.

Non-claim:
  This specification does not relocate GitHub or Netlify cloud builders onto H:.
```

Project-controlled **repository files** that configure those agents (workflow YAML, `netlify.toml`, ignore rules, env **names**) remain governed here. Unavoidable vendor telemetry on those agents is documented, not eliminated.

### 9.3 Repository topology (locked)

| Rule | Decision |
| --- | --- |
| Topology | **Single governing repository** for People Intake |
| Current remote | `https://github.com/Grappe501/people.git` |
| Local clone root | `H:\people` only (IS-100 / IS-104) |
| Future workspaces | Allowed **inside** this repo (e.g. packages/) when an authorized package defines them |
| Second product repo | **Forbidden** without Decision Log approval |
| Recommended rename | IS-100 suggested `people-intake-system`; rename is **optional** (ISSUE-GHN-001) and does not block this architecture |

### 9.4 Branch strategy (locked)

| Branch | Role | Protection (when enabled) |
| --- | --- | --- |
| `master` | Canonical integration branch **today** | Require PR + required checks when protection package is authorized |
| `feature/*` | Feature work | Short-lived; merge via PR |
| `fix/*` | Defect fixes | Short-lived; merge via PR |
| `docs/*` | Documentation slices (optional) | Short-lived; merge via PR |
| `release/*` | Release preparation (when app releases exist) | Controlled merges |
| `staging` | Optional long-lived Staging publish branch | Protected; non-production only |

**Default branch fact:** the live default branch is `master`. A migration to `main` is a Decision Log change (ISSUE-GHN-002), not a silent rename.

**Force-push:** forbidden on `master`, `staging`, and release branches except emergency recovery with Decision Log / Steve authorization.

### 9.5 Commit conventions (locked)

Documentation / governance slices (current mode):

```text
docs(<work-item-kebab>): <why>
```

When application implementation is authorized, also allow:

```text
feat|fix|refactor|test|chore|ci|build|perf(<scope>): <why>
```

Rules:

* One logical slice per commit preferred; evidence follow-up commits allowed (D-065).  
* Never commit secrets, production personal data, or unauthorized `src/` while Gate G-10 is closed.  
* Commit message SHOULD cite Decision IDs when closing ADRs/Decision Log items.

### 9.6 Release tagging (locked)

| Tag form | When |
| --- | --- |
| `vMAJOR.MINOR.PATCH` | Authorized application/docs publish releases only |
| `docs/<work-item>` | Optional documentation milestone markers |

Tags MUST resolve to a reachable SHA on the remote. Tagging MUST NOT substitute for Gate G-10 or invent Netlify applicability.

### 9.7 GitHub Actions governance (locked)

**Current status:** workflows **NOT AUTHORIZED**.

When an authorized package introduces Actions:

| Rule | Requirement |
| --- | --- |
| Location | `.github/workflows/` only |
| First purpose | Validation (`governance:validate`, catalog validate, lint/test when authorized) |
| Production deploy via Actions | Only if `deploymentAuthorized` (or Decision Log equivalent) is true for that package |
| Secrets | GitHub Actions secrets / environments; never plaintext in YAML |
| Permissions | Least privilege (`contents: read` default; escalate only as needed) |
| Branch filters | Production jobs limited to canonical integration branch / release tags |
| H-drive | Runner paths are remote exceptions (§9.2); workflows MUST NOT instruct developers to write project caches to `C:\` |

Unauthorized addition of `.github/workflows` while documentation-only mode is active is a governance violation.

### 9.8 Netlify environment architecture (locked)

**Site posture:** dedicated People Intake Netlify site (D-018). No secret inheritance from unrelated SOSWebsite apps.

**Environment mapping (preferred initial model — single site, multi-context):**

| IS-103 class | Netlify mechanism | Git trigger (when authorized) |
| --- | --- | --- |
| Local | Developer machine + `.netlify` local state (ignored) | N/A |
| Preview | Deploy Previews | Pull requests / preview branches |
| Staging | Branch deploy of `staging` (or Netlify Branch Deploys) | Updates to `staging` |
| Production | Production context | Canonical integration branch (`master`) after explicit authorization |

**Scaling without model change:**

* Additional staging brands MAY add named branch deploys or a **second dedicated Netlify site** still labeled Staging/Production under IS-103.  
* Environment **classes** and evidence rules do not change.  
* Preview remains ephemeral; Staging remains non-production persistent; Production remains explicit-authorization-only.

**Until authorized deployable surface exists:** Netlify closeout = `NOT APPLICABLE` (D-065). Do not invent `netlify.toml` or app trees to force applicability.

### 9.9 Environment variable governance

| Store | Holds | Forbidden |
| --- | --- | --- |
| Git / docs | Non-secret names, `.env.example` shapes | Secret values |
| Netlify context env | Runtime secrets/config per Preview/Staging/Production | Cross-env Production credential reuse |
| GitHub Secrets / Environments | CI tokens, deploy hooks, validation credentials | Embedding in workflow logs |
| Local `.env*` under `H:\people` | Developer-only; ignored by Git | Committing real secrets |

IS-103 rules apply: no silent Production defaults; fail closed; Preview ≠ Production authorization.

### 9.10 Deployment promotion rules

```text
Author docs / (later) code
  → validate
  → PR review (when protection enabled)
  → merge to integration branch
  → Preview (optional evidence)
  → Staging verification (required before Production when Staging exists)
  → Explicit Production authorization
  → Production deploy
  → Verification + provenance record
```

Hard rules:

1. Merge ≠ Production authorization.  
2. Preview green ≠ Production authorization.  
3. Staging green ≠ automatic Production deploy unless a Decision Log–approved automation package says so **and** `deploymentAuthorized` is true.  
4. Unauthorized Production deploy is a hard stop.

### 9.11 Rollback strategy

| Layer | Rollback method |
| --- | --- |
| Netlify publish | Restore previous successful deploy / redeploy known-good SHA |
| Git | Revert merge commit on integration branch; re-run authorized pipeline |
| Database / storage | **Out of scope here** — dedicated migration/data packages |
| Secrets compromise | Rotate Netlify + GitHub secrets; invalidate tokens; record incident |

Rollback of Production requires the same evidence discipline as deploy (provenance + verification).

### 9.12 Artifact provenance

Every authorized deployment evidence record MUST include:

```text
workItemId
gitSha
gitBranchOrTag
environment          # Preview | Staging | Production
netlifyDeployId      # or NOT_APPLICABLE with reason
netlifySiteIdOrName  # non-secret identifier
validationSummary
actor
timestampUtc
authorizationReference   # package ID / Decision Log / gate
result                   # VERIFIED | FAILED | ROLLED_BACK
```

Preferred future home (when `deployment/` tree is authorized): `deployment/reports/`.

Until then, documentation slices record Netlify applicability in completion reports / `PEOPLE_LATEST_CURSOR_REPORT.md`.

### 9.13 Deployment verification

When a deployable surface exists and deploy is authorized, verification MUST confirm:

1. Remote Git SHA matches intended release.  
2. Netlify deploy succeeded for the correct context.  
3. Smoke checks defined by the authorizing package pass.  
4. No Production secrets appear in build logs.  
5. Evidence file written and committed/pushed per D-065 (or attached to the authorized ops package process).

### 9.14 Secrets management boundaries

```text
GitHub: Actions secrets / Environment secrets
Netlify: per-context environment variables
Humans: password manager / org secret store (ops)
Repo: names and shapes only
```

Forbidden: secrets in markdown, screenshots in docs, chat paste into committed files, sharing Production credentials into Preview.

### 9.15 Burt execution authority (locked)

Within established governance, Burt has **full execution authority** to:

```text
Execute validation suites
Generate completion reports
Update governance indexes/registers/RTM
Commit the slice
Push to the canonical branch
Verify the remote
Deploy when an authorized deployable surface exists
Record evidence in the completion report
```

Execution **stops** only for reserved product/governance gates, including:

* New ADR requiring acceptance  
* Project scope change  
* Authorization to begin application implementation (Gate G-10 / `applicationCodeAuthorized`)  
* Authorization to enable deployment (`deploymentAuthorized`) or Production go-live  
* Legal, security, or business policy decisions reserved for Steve  
* Hard-boundary violations (IS-104, forbidden paths, secret exposure)

Instructions to Burt SHOULD be imperative (`Execute`, `Commit`, `Push`) — not operator-relay prompts — except at those gates.

### 9.16 Source-controlled deployment layout (future authorization)

When an implementation package authorizes creation:

```text
deployment/
  netlify/           # netlify.toml companion docs, headers, redirects notes
  environments/      # non-secret env matrices
  manifests/
  verification/
  rollback/
  release/
  reports/           # provenance evidence
.github/
  workflows/         # only when package-authorized
```

Framework-required root files (e.g. root `netlify.toml`) MAY exist when that package explicitly allows them. `.netlify/` remains local/non-canonical (IS-100).

## 10. Data Contracts

NOT_APPLICABLE for business entities. Provenance record fields in §9.12 are the deployment evidence contract.

## 11. Interface Contracts

| Interface | Contract |
| --- | --- |
| Git ↔ humans/Burt | Canonical remote + branch rules |
| GitHub ↔ Netlify | Site linked to repo when authorized; Production branch = integration branch |
| Netlify ↔ runtimes | Env injection per context (IS-103) |
| D-065 ↔ Netlify | Deploy only if authorized surface exists |

## 12. State Behavior

NOT_APPLICABLE for Catalog 1 entity states. Deployment lifecycle states for evidence:

```text
NOT_APPLICABLE → AUTHORIZED → QUEUED → BUILDING → DEPLOYED → VERIFIED
                                 ↘ FAILED → ROLLED_BACK (optional)
```

## 13. Permission Behavior

Runtime page permissions: NOT_APPLICABLE. Operational permissions:

* Merge to `master`: reviewers + (when enabled) required checks  
* Production secret changes: ops role / Steve  
* Production deploy trigger: only when `deploymentAuthorized` or Decision Log package says so  

## 14. Error and Recovery Behavior

| Failure | Recovery |
| --- | --- |
| Push rejected | Fix auth/branch protection; do not force-push `master` |
| Remote missing commit | Re-push; re-verify ancestry |
| Preview build fail | Fix in PR; do not promote |
| Production deploy fail | Stop; do not retry blindly with secret changes; record evidence; rollback if partial |
| Secrets leaked in logs | Rotate; treat as incident |
| Unauthorized workflow/netlify files appear | Delete/revert; governance violation report |

## 15. Audit Requirements

Material Production deploys, rollbacks, and secret rotations SHOULD produce durable evidence (Catalog 3 alignment later). Documentation closeouts MUST retain D-065 evidence fields.

## 16. Notification Requirements

NOT_APPLICABLE for Catalog 6 product notifications. Future ops may notify on Production deploy/failure via approved channels without storing secrets in repo.

## 17. Background Processing

Netlify scheduled functions are **not** the durable job runtime (ADR-006). Job architecture remains separate. Do not assume Netlify cron replaces Catalog 7.

## 18. Security and Privacy

* Protected branches when protection package authorized  
* Secret scanning expectations for future CI  
* No Production PII in Git  
* Dedicated Netlify site boundary (D-018)  
* Preview environments MUST use non-production data policies when app exists  

## 19. Data Classification and Retention

Deployment logs/evidence: operational records; retain per future ops package. No Production secrets in retained markdown evidence.

## 20. Observability

Deploy evidence MUST be correlatable by Git SHA and Netlify deploy ID. Environment label required in ops reports.

## 21. Testing

Future packages SHOULD test:

* Branch protection assumptions (documented)  
* Preview ≠ Production authorization checks in release scripts  
* Provenance schema validation  
* Failure: unauthorized `netlify.toml` / workflow addition while Gate G-10 closed  

## 22. Acceptance Criteria

| ID | Criterion | Met by this doc? |
| --- | --- | --- |
| AC-GHN-001 | Single-repo topology and canonical remote documented | Yes |
| AC-GHN-002 | Branch model including current `master` fact documented | Yes |
| AC-GHN-003 | Commit and tag conventions documented | Yes |
| AC-GHN-004 | GitHub Actions authorization boundary documented | Yes |
| AC-GHN-005 | Netlify Preview/Staging/Production mapping documented | Yes |
| AC-GHN-006 | Promotion and rollback rules documented | Yes |
| AC-GHN-007 | Provenance and verification fields documented | Yes |
| AC-GHN-008 | Secrets boundaries documented | Yes |
| AC-GHN-009 | Honest remote-agent vs H-drive limitation documented | Yes |
| AC-GHN-010 | Scaling without model change documented | Yes |
| AC-GHN-011 | Burt execution authority vs reserved gates documented | Yes |
| AC-GHN-012 | No unauthorized workflows/`netlify.toml` created by this package | Yes |

## 23. Open Decisions

| ID | Question | Status |
| --- | --- | --- |
| ISSUE-GHN-001 | Rename GitHub repo `people` → `people-intake-system`? | OPEN (non-blocking) |
| ISSUE-GHN-002 | Migrate default branch `master` → `main`? | OPEN (non-blocking) |
| ADR-009 | Hosting/deployment technology lock packaging | OPEN / PROPOSED (aligned with D-018 + this IS) |
| Staging second site vs branch deploy | Allowed variants under §9.8; pick in first deploy package | DEFER to authorized deploy package |

## 24. Risks

| ID | Risk | Mitigation |
| --- | --- | --- |
| RISK-GHN-001 | Inventing app/`netlify.toml` to force deploy evidence | REQ-GHN-016; D-065 |
| RISK-GHN-002 | Preview treated as Production auth | REQ-GHN-011 |
| RISK-GHN-003 | Secret inheritance from SOSWebsite Netlify | REQ-GHN-009 |
| RISK-GHN-004 | Silent `master`→`main` rename breaking automation | REQ-GHN-003; ISSUE-GHN-002 |
| RISK-GHN-005 | Claiming CI runs on H: | §9.2; NFR-GHN-HONEST-001 |
| RISK-GHN-006 | Actions deploy Production without authorization | REQ-GHN-008/012 |

## 25. Dependencies

IS-100, IS-103, IS-104, D-018, D-065, ADR-009 (open), Gate G-10 closed.

## 26. Traceability

| Requirement | Maps to | Status |
| --- | --- | --- |
| REQ-GHN-001…018 | IS-100 GitHub/Netlify; IS-103 env; D-065; D-018 | FULLY_MAPPED (design) |
| REQ-REPO-014 | Environment distinguishability | FULLY_MAPPED via §9.8 |
| REQ-ENV-007/011 | Preview≠Prod; deploy evidence | FULLY_MAPPED |

## 27. Implementation Boundary

**Authorized by this approval:** this specification; indexes/registers/RTM/reports; Cursor protocol execution-authority clarification.

**Forbidden:** `.github/workflows/**`, root/app `netlify.toml`, Netlify site linking, secret provisioning, application scaffolding, Production/Preview deploys, claiming Netlify applicable without an authorized surface.

## 28. Revision History

| Version | Date | Change | Approval |
| --- | --- | --- | --- |
| 1.0 | 2026-07-26 | GitHub and Netlify architecture; Burt execution authority within governance | D-068 |

## Phase 1 platform closure

```text
PEOPLE-IS-100 Repository Architecture           APPROVED
PEOPLE-IS-101 Technology Decision Specification APPROVED (ADRs OPEN)
PEOPLE-IS-102 Module Boundary Specification     APPROVED
PEOPLE-IS-103 Environment Architecture          APPROVED
PEOPLE-IS-104 H-Drive Workspace Protocol        APPROVED
PEOPLE-IS-105 GitHub and Netlify Architecture   APPROVED

Phase 1 platform documentation: COMPLETE
Application implementation: NOT AUTHORIZED
```

## Next

```text
PEOPLE-IS-200-DOMAIN-MODEL-1.0
```

Parallel (still required for freeze):

```text
PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0
```

## Final status

```text
PEOPLE-IS-105 GITHUB AND NETLIFY ARCHITECTURE: APPROVED (DOCUMENTATION)
SOURCE-CONTROL / DEPLOYMENT MODEL: ACTIVE
GITHUB ACTIONS / NETLIFY WIRING: NOT AUTHORIZED
APPLICATION IMPLEMENTATION: NOT AUTHORIZED
DEPLOYMENT AUTHORIZATION: CLOSED
```
