# PEOPLE-IS-104 — H-DRIVE WORKSPACE PROTOCOL

**Title:** H-Drive Workspace Protocol  
**Document ID:** `PEOPLE-IS-104-H-DRIVE-WORKSPACE-PROTOCOL-1.0`  
**Version:** 1.0  
**Status:** APPROVED  
**Phase:** PHASE 1 — REPOSITORY AND PLATFORM ARCHITECTURE  
**Project Root:** `H:\people`  
**Owner:** People Intake System Program  
**Approval Authority:** Decision Log D-067  
**Created Date:** 2026-07-26  
**Last Updated:** 2026-07-26  
**Governing Documents:** PEOPLE_INTAKE_H_DRIVE_PROTOCOL; IS-000; IS-100; IS-101 (ADR-020); IS-103; PEOPLE-PROTOCOL-COMMIT-PUSH-DEPLOY-1.0  
**Dependencies:** IS-103 APPROVED (D-066); ADR-020 remains OPEN for automated guard implementation authorization  
**Implementation Authorization:** `IMPLEMENTATION NOT AUTHORIZED` (protocol documentation approved; repository-guard **code** not authorized)

```text
DESIGN COMPLETE
APPROVED FOR DOCUMENTATION GOVERNANCE
OPERATIONAL STANDARD FOR EVERY BUILD MACHINE
APPLICATION IMPLEMENTATION NOT AUTHORIZED
REPOSITORY GUARD CODE NOT AUTHORIZED
```

**Companion / prior protocol:** `docs/00_governance/PEOPLE_INTAKE_H_DRIVE_PROTOCOL.md` remains in force; this IS elevates and details it for implementation packages and tooling.

---

## 1. Purpose

Define the definitive operational workspace standard for every machine that builds People Intake so that **all project-controlled and project-configurable artifacts** are directed under `H:\people`, while documenting unavoidable OS/third-party behavior honestly rather than claiming to eliminate every `C:\` write on Windows.

## 2. Scope

Canonical root; directory conventions; allowed/prohibited write locations; environment variables; package-manager cache strategy; temporary files; build artifacts; Git expectations; Cursor workspace configuration; Node/npm/future Prisma/test/browser tooling redirection; validation and enforcement rules; exception handling; recovery procedures.

## 3. Out of Scope

* Implementing `tools/repository_guard` executable code (requires authorized package + ADR-020 acceptance)  
* Guaranteeing OS, antivirus, browser, or IDE profile writes never touch `C:\`  
* Creating `src/` application trees  
* Authorizing package installation for application scaffolding (still Gate G-10 / explicit auth)  

## 4. Governing References

H-Drive Protocol; IS-100 §§4.2, 9.15, REQ-REPO-001/002/010; IS-101 ADR-020; IS-103 local env rules; D-065 closeout protocol; `scripts/validate-h-drive.mjs` / `npm run drive:validate`.

## 5. Definitions

| Term | Meaning |
| --- | --- |
| Project-controlled artifact | File/dir created by project scripts, configs, package installs we invoke, docs tooling, or authorized app commands |
| Project-configurable path | Path we can redirect via env vars, npm/config, framework config, or CLI flags |
| Unavoidable external write | OS/IDE/browser/vendor write we cannot redirect with project controls |
| Canonical root | `H:\people` — sole authorized project workspace |
| Dual-path era | Current ignored dirs (`.tmp`, `.npm-cache`, …) coexist with IS-100 target names (`tmp/`, `local/`, …) until a cutover package |

## 6. Assumptions

* Build machines are Windows-capable with `H:` available.  
* Node/npm used for documentation validation today.  
* Future Next.js/Prisma/Playwright (IS-101 recommendations) inherit these redirects when authorized.  

## 7. Functional Requirements

| ID | Description |
| --- | --- |
| REQ-HDRIVE-001 | The canonical project root MUST be `H:\people`. |
| REQ-HDRIVE-002 | No second governing clone or shadow root MAY operate without Decision Log approval. |
| REQ-HDRIVE-003 | Project-controlled artifacts MUST NOT be intentionally written to `C:\`. |
| REQ-HDRIVE-004 | Before package install, build, test, migration, codegen, or large processing, the active directory MUST resolve under `H:\people`. |
| REQ-HDRIVE-005 | `TEMP`, `TMP`, and `TMPDIR` MUST be set to an approved H-drive temp path for project sessions. |
| REQ-HDRIVE-006 | npm cache MUST use `H:\people\.npm-cache` (or approved successor under root). |
| REQ-HDRIVE-007 | Test/coverage/browser artifacts MUST write under approved H-drive paths. |
| REQ-HDRIVE-008 | Git for this project MUST operate only inside `H:\people`. |
| REQ-HDRIVE-009 | If a required tool cannot operate without intentional project-controlled writes to `C:\`, work MUST stop and the limitation documented. |
| REQ-HDRIVE-010 | Unavoidable external `C:\` writes MUST be distinguished from protocol violations in reports. |
| REQ-HDRIVE-011 | `npm run drive:validate` MUST pass before material project mutations in a Burt session. |
| REQ-HDRIVE-012 | Future repository guard (when authorized) MUST fail closed: stop, identify path, cite rule, non-zero exit, no C: fallback. |

## 8. Nonfunctional Requirements

| ID | Description |
| --- | --- |
| NFR-HDRIVE-AUDIT-001 | Workspace validation results are reportable and repeatable. |
| NFR-HDRIVE-OPS-001 | A new machine can be brought into compliance using this document alone. |
| NFR-HDRIVE-HONEST-001 | Specs MUST NOT claim OS-level impossibility of all `C:\` writes. |

## 9. Architecture — Workspace Standard

### 9.1 Canonical root

```text
H:\people
```

**Forbidden alternate roots (examples):**

```text
C:\Users\...\people
C:\dev\people
H:\SOSWebsite\people
```

People Intake may later **integrate with** systems under `H:\SOSWebsite`, but MUST NOT nest its governing root there.

### 9.2 Honest limitation (locked)

```text
Enforceable requirement:
No project-controlled or project-configurable artifact may intentionally write outside H:\people.

Non-claim:
This protocol does not guarantee that Windows, Cursor, browsers, auth helpers,
antivirus, or other installed applications never write their own unrelated files under C:\.
```

Reports MUST use this distinction. Treating every incidental OS profile write as a project failure is incorrect; treating redirected-capable caches that still target `C:\` as acceptable is also incorrect.

### 9.3 Directory conventions

#### 9.3.1 Currently required local directories (in force)

| Path | Role | Git |
| --- | --- | --- |
| `H:\people\.tmp` | Session TEMP/TMP/TMPDIR | Ignored |
| `H:\people\.cache` | General project cache | Ignored |
| `H:\people\.npm-cache` | npm cache | Ignored |
| `H:\people\.test-output` | Test reports/coverage/screenshots | Ignored |
| `H:\people\.local-storage` | Local fixtures / emulated storage | Ignored |
| `H:\people\.netlify` | Local Netlify CLI state | Ignored |
| `H:\people\docs` | Governing docs | Commit |
| `H:\people\contracts` | Contracts | Commit |
| `H:\people\scripts` | Scripts | Commit |
| `H:\people\reports` | Validation/ops reports | Commit (non-secret) |
| `H:\people\develop_notes` | Operator notes | Commit |
| `H:\people\diagrams` | Diagrams | Commit |
| `H:\people\data\documentation` | Doc registries | Commit |

#### 9.3.2 IS-100 target paths (future cutover)

When an authorized package performs cutover, prefer:

| Target | Role |
| --- | --- |
| `tmp/` | Temporary processing |
| `local/` | Local DB/emulators/uploads |
| `logs/` | Local logs |
| `generated/` | Reproducible generated output |

Until cutover, `.tmp` / `.npm-cache` / `.test-output` / `.local-storage` remain **approved** project-controlled locations. Dual naming MUST be documented in any package that migrates paths.

### 9.4 Allowed vs prohibited write locations

| Allowed (under root) | Prohibited (intentional project-controlled) |
| --- | --- |
| Approved dirs in §9.3 | `C:\` any path |
| Future `src/`, `app/`, `database/` when authorized | User-profile project clones |
| `node_modules/` under root when install authorized | Global npm prefix used as project store |
| Ignored local/tmp/cache dirs | Second Git clone as “real” workspace |

### 9.5 Environment variables (session standard)

Before project commands:

```powershell
Set-Location H:\people
$env:TEMP = "H:\people\.tmp"
$env:TMP = "H:\people\.tmp"
$env:TMPDIR = "H:\people\.tmp"
$env:npm_config_cache = "H:\people\.npm-cache"
```

Optional / future (when tools authorized):

| Variable | Intended target | Notes |
| --- | --- | --- |
| `npm_config_cache` | `.npm-cache` | Required now |
| `NEXT_CACHE_DIR` / analogous | `.cache` or `tmp/cache` | When Next authorized |
| `PRISMA_*` temp overrides | `.tmp` | When Prisma authorized — exact flags per ADR-003 |
| `PLAYWRIGHT_BROWSERS_PATH` | `.cache/playwright` or similar under root | When e2e authorized |
| `XDG_CACHE_HOME` | `.cache` | If tooling honors it |

Exact framework variable names finalize with accepted ADRs; this IS locks the **policy**: if configurable, point under `H:\people`.

### 9.6 Package manager cache strategy

* Use project-local npm cache only.  
* Do not install dependencies globally for this project.  
* Do not copy `node_modules` from unrelated `C:\` projects.  
* Application `npm install` remains **unauthorized** until Gate G-10 / explicit package authorization — when authorized, still under root + local cache.  

### 9.7 Temporary file strategy

* All project temp → `.tmp` (or future `tmp/`).  
* Safe to delete; must not hold production secrets longer than needed.  
* Cleanup procedures belong in ops runbooks; temp must remain gitignored.  

### 9.8 Build / generated / test artifact locations

| Artifact | Location |
| --- | --- |
| Coverage / jest/vitest output | `.test-output` or `generated/tests` when adopted |
| Playwright reports/traces | `.test-output` (never commit unless approved) |
| Next/dist build | under root `build/` / `.next/` (ignored) when authorized |
| Prisma generate | under project; temp to `.tmp` |
| Governance validation reports | `reports/` |

### 9.9 Git workspace expectations

* Single clone at `H:\people` tracking `origin` (`https://github.com/Grappe501/people.git`).  
* No convenience clone on `C:\`.  
* Closeout per D-065: commit → push → remote verify.  
* Secrets never committed (`.env` ignored; `.env.example` names only).  

### 9.10 Cursor workspace configuration

* Open the folder `H:\people` as the workspace root (not a parent or alternate clone).  
* Agent terminals MUST `Set-Location H:\people` and export TEMP/TMP/npm cache as above.  
* Cursor/OS may still write IDE telemetry under the user profile on `C:\` — classify as **unavoidable external** unless a project-controlled path is misconfigured.  
* Do not instruct Cursor to use `%USERPROFILE%` temp for project artifacts.  

### 9.11 Node / future Prisma / tooling

| Tool | Rule |
| --- | --- |
| Node scripts | Run from root; use H-drive temp/cache |
| npm | `npm_config_cache` under root |
| Prisma (future) | schema/migrations/client under root; no intentional C: generate |
| Playwright (future) | browsers/cache under root if configurable |
| Netlify CLI | state under `.netlify`; no unauthorized app deploy |

### 9.12 Validation and enforcement

**Now (authorized):**

```text
npm run drive:validate
npm run governance:validate
```

Preflight before material writes:

1. CWD under `H:\people`  
2. TEMP/TMP/TMPDIR → `.tmp`  
3. npm cache → `.npm-cache`  
4. Required dirs exist  
5. Stop if controlled path resolves to `C:\`  

**Future (not authorized yet):** `tools/repository_guard` per ADR-020 — fail closed, cite REQ-HDRIVE-*, no C: fallback.

### 9.13 Exception handling (third-party / OS)

| Situation | Response |
| --- | --- |
| Tool supports redirect | MUST redirect under root |
| Tool cannot redirect project-controlled output | STOP; open ISSUE; do not proceed |
| OS/IDE writes unrelated profile files on `C:\` | Document as unavoidable; do not falsify as project compliance failure |
| Ambiguous whether write is project-controlled | Treat as controlled until proven otherwise; prefer stop + clarify |

### 9.14 Recovery if workspace validation fails

1. Stop the build/session immediately.  
2. Do not continue installs, migrations, or codegen.  
3. Record failure under `H:\people\reports\`.  
4. Fix CWD and env redirects.  
5. Re-run `npm run drive:validate`.  
6. Only then resume.  
7. If failure is an unavoidable tool limitation, file ISSUE + Decision Log note; do not silently bypass.  

## 10–13. Data / Interface / State / Permission

NOT_APPLICABLE for runtime domain entities. Workspace paths are operational contracts. No Catalog 5 permission grants exemption from H-drive rules.

## 14. Error and Recovery Behavior

Canonical failure names (align IS-100):

```text
INVALID_PROJECT_ROOT
FORBIDDEN_WRITE_TARGET
```

Behavior: stop; identify path; cite this IS / H-Drive Protocol; recommend correction; non-zero exit; no automatic fallback to `C:\`.

## 15–17. Audit / Notification / Jobs

Material workspace-policy changes record via Decision Log. No runtime jobs authorized by this IS.

## 18–19. Security / Retention

Local ignored dirs may hold sensitive fixtures only if authorized and classified; prefer synthetic data. Do not commit secrets. Retention of local artifacts: delete when safe; never treat local as sole canonical store.

## 20. Observability

`drive:validate` and future guard SHOULD log root, pass/fail, offending path — never secret values.

## 21. Testing

Future tests (when tooling authorized): correct root; incorrect root; TEMP mispointed to `C:\`; npm cache mispointed; recovery path. Until then, session preflight + `drive:validate` is mandatory evidence.

## 22. Acceptance Criteria

| ID | Criterion |
| --- | --- |
| AC-HDRIVE-001 | Canonical root fixed as `H:\people` |
| AC-HDRIVE-002 | Allowed/prohibited write locations documented |
| AC-HDRIVE-003 | Session env var standard documented |
| AC-HDRIVE-004 | Cache/temp/test/build locations documented |
| AC-HDRIVE-005 | Git and Cursor expectations documented |
| AC-HDRIVE-006 | Honest OS/third-party limitation explicit |
| AC-HDRIVE-007 | Validation (`drive:validate`) and failure/recovery defined |
| AC-HDRIVE-008 | Exception handling for non-redirectable tools defined |
| AC-HDRIVE-009 | Dual-path era (`.tmp` vs `tmp/`) acknowledged |
| AC-HDRIVE-010 | No application/guard code created by this package |

## 23. Open Decisions

| ID | Status |
| --- | --- |
| ADR-020 | OPEN — automated repository guard implementation |
| ISSUE-HDRIVE-001 | OPEN until guard design accepted/implemented |
| ISSUE-REPO-002 | OPEN — exact ignore patterns with framework ADRs |
| Path cutover `.tmp` → `tmp/` | DEFER to dedicated docs/tooling package |

## 24. Risks

| ID | Risk | Mitigation |
| --- | --- | --- |
| RISK-HDRIVE-001 | Claiming zero `C:\` OS writes | Honest limitation §9.2 |
| RISK-HDRIVE-002 | Drift to second clone on C: | REQ-HDRIVE-002/008 |
| RISK-HDRIVE-003 | Framework caches ignore env | Per-tool config in authorized packages |
| RISK-HDRIVE-004 | Dual path confusion | Document both; cutover package later |

## 25. Dependencies

H-Drive Protocol; IS-100/103; D-065; open ADR-020 for code enforcement.

## 26. Traceability

| Requirement | Maps to | Status |
| --- | --- | --- |
| REQ-HDRIVE-001…012 | IS-100 REQ-REPO-001/002/010; H-Drive Protocol | FULLY_MAPPED (design) |
| ADR-020 | Guard implementation | PARTIALLY_MAPPED |

## 27. Implementation Boundary

**Authorized:** this specification; updates to indexes/reports; continued use of `drive:validate`.  
**Forbidden:** implementing repository guard binaries; forcing app `npm install`; creating `src/`; claiming OS-total control over `C:\`.

## 28. Revision History

| Version | Date | Change | Approval |
| --- | --- | --- | --- |
| 1.0 | 2026-07-26 | H-drive workspace operational standard | D-067 |

## Next

```text
PEOPLE-IS-105-GITHUB-AND-NETLIFY-ARCHITECTURE-1.0
```

## Final status

```text
PEOPLE-IS-104 H-DRIVE WORKSPACE PROTOCOL: APPROVED (DOCUMENTATION)
OPERATIONAL STANDARD: ACTIVE
APPLICATION IMPLEMENTATION: NOT AUTHORIZED
REPOSITORY GUARD CODE: NOT AUTHORIZED
```
