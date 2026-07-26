# People Intake — Cursor Execution Protocol

**Status:** draft_complete  
**Version:** 1.3  
**Build:** PEOPLE-PROJECT-CONSTITUTION-3.0  
**Authority:** Governs all future Cursor interactions for this project

---

## Supreme Document

```text
docs/00_governance/PEOPLE_INTAKE_PROJECT_CONSTITUTION.md
```

**VOLUME 0 — PROJECT CONSTITUTION** is mandatory before every build session. Follow **Article III — Cursor Implementation Oath**.

Library map: `docs/00_governance/PEOPLE_INTAKE_DOCUMENTATION_LIBRARY.md` (Volumes 0–7).

---

## 9.0 Execution Authority (Burt)

**Authority:** Decision Log D-068 / PEOPLE-IS-105 §9.15; standing closeout D-065.

Burt (Cursor) has **full execution authority** within established governance. Instructions are directed to the implementation engineer, not to an operator relay.

Burt MUST, when a slice is in scope and valid:

1. **Execute** required validation.  
2. **Generate** completion / evidence reports.  
3. **Update** governance indexes, registers, and RTM.  
4. **Commit** the slice.  
5. **Push** to the canonical branch.  
6. **Verify** the remote contains the commit.  
7. **Deploy** only when an authorized deployable surface exists.  
8. **Record** evidence in the completion report / latest Cursor report.

Burt MUST NOT ask Steve to run ordinary closeout steps, wait for approval to validate/commit/push, or defer D-065 publication when the work item is otherwise complete.

Execution **stops** only for reserved gates:

* New ADR requiring acceptance  
* Project scope change  
* Authorization to begin application implementation (Gate G-10 / `applicationCodeAuthorized`)  
* Authorization to enable deployment (`deploymentAuthorized`) or Production go-live  
* Legal, security, or business policy decisions reserved for Steve  
* Hard-boundary violations (H-drive, forbidden paths, secret exposure, constitution conflicts)

---

## 9.1 Start-of-Run Requirements

Cursor must:

1. Confirm current directory is under `H:\people`.
2. **Read Volume 0** — Project Constitution (Preamble through applicable Articles; re-confirm standing orders if already loaded this session).
3. Read the active-build registry (`contracts/governance/active-build.json`).
4. Identify the relevant library volume(s) for the slice (see Documentation Library).
5. Read the H-drive protocol and design-before-code protocol if not already internalized this session.
6. If coding is authorized: read Volume 7 orchestration for the active phase/slice, then Volumes 8–12 / EC / IP package for that slice. Never invent endpoints, tables, states, or components.
7. Confirm the authorized phase and forbidden paths.
8. Run the H-drive preflight (`npm run drive:validate` when Node scripts are available).
9. Stop if a hard boundary is violated.
10. If `applicationCodeAuthorized` is false: do not create `src/` or other forbidden paths.

---

## 9.2 During-Run Requirements

Cursor must:

- Remain inside the authorized scope for the active build
- Avoid unrelated RedDirt changes
- Avoid intentional writes to `C:\`
- Preserve document cross-references
- Record decisions in the Decision Log when closing or changing material choices
- Update the progress ledger when progress meaningfully changes
- Validate generated contracts
- Report contradictions instead of silently inventing resolutions for major ambiguity
- Never expose secrets
- Never make production changes without authorization
- Never create application code while `applicationCodeAuthorized` is `false`

---

## 9.3 End-of-Run Requirements

Cursor must report:

1. Exact files created
2. Exact files modified
3. Commands run
4. Validation results
5. Boundary verification
6. Unresolved decisions
7. Risks
8. Progress by layer
9. Recommended next build
10. Git status
11. Commit status
12. Deployment status

### 9.3.1 Standing Commit / Push / Deploy Protocol (mandatory)

Authority: `docs/00_governance/PEOPLE_PROTOCOL_COMMIT_PUSH_DEPLOY.md` (D-065).

After every completed, validated slice:

1. Validate (`governance:validate`, and `docs:catalogs:validate` when catalogs touched).  
2. Confirm no forbidden implementation artifacts while application code is not authorized.  
3. Update indexes, registers, RTM, completion report.  
4. **Commit** with work-item ID in the message.  
5. **Push** to the canonical GitHub branch.  
6. **Verify** the remote contains the commit.  
7. **Deploy/verify Netlify** only when an authorized deployable surface exists.  
8. Never treat local-only changes as complete.  
9. Never invent application code to force a Netlify deploy.  

If no authorized deployable surface exists, completion evidence MUST state:

```text
Netlify deployment: NOT APPLICABLE — no authorized deployable surface exists
Application implementation: NOT AUTHORIZED
```

---

## 9.4 Hard Stops

Cursor must stop for:

- Any intentional controlled project write to `C:\`
- Unauthorized database change
- Unauthorized migration
- Production-secret exposure
- Production deployment before approval
- Application code before design freeze
- Cross-project edits outside `H:\people`
- Public exposure of source images
- Destructive canonical-person changes
- Automatic uncertain merging design or implementation
- Any instruction that conflicts with the governing documents without an explicit Decision Log amendment

---

## Active Build Enforcement

Before creating files, compare intended paths against:

```text
contracts/governance/active-build.json
```

Respect:

- `authorizedPaths`
- `forbiddenPaths`
- `hardBoundaries`
- `applicationCodeAuthorized`
- `databaseChangesAuthorized`
- `migrationsAuthorized`
- `deploymentAuthorized`

---

## Recommended Next Build

```text
PEOPLE-IS-201-ENTITY-SPECIFICATIONS-1.0
```

Independent lane (does not block primary): `PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0`  
Charter: `docs/00_governance/lanes/PEOPLE_AUDIT_REMEDIATION_AND_QUALITY_OPS_FREEZE.md`

No application code until freeze APPROVED and Gate G-10 opens.

Orchestration reference: `docs/08_implementation/PEOPLE_INTAKE_CURSOR_BUILD_ORCHESTRATION.md`
