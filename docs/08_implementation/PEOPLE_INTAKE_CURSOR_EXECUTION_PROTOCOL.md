# People Intake — Cursor Execution Protocol

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-GOVERNANCE-FOUNDATION-1.0  
**Authority:** Governs all future Cursor interactions for this project

---

## 9.1 Start-of-Run Requirements

Cursor must:

1. Confirm current directory is under `H:\people`.
2. Read the master build plan.
3. Read the H-drive protocol.
4. Read the design-before-code protocol.
5. Read the source-of-truth registry.
6. Read the active-build registry (`contracts/governance/active-build.json`).
7. Confirm the authorized phase.
8. Confirm forbidden paths.
9. Run the H-drive preflight (`npm run drive:validate` when Node scripts are available).
10. Stop if a hard boundary is violated.

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

## Recommended Next Build (After This Foundation)

```text
PEOPLE-WORKFLOW-UX-DESIGN-1.0
```

That build remains design-only.
