# People Intake — H-Drive Protocol

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-GOVERNANCE-FOUNDATION-1.0  
**Authority:** Permanent protocol

---

## Permanent Rule

> No Cursor instruction, script, dependency installation, generated artifact, application file, cache, test file, project temporary file, or project-controlled output may intentionally be written to C:.

---

## Authorized Root

```text
H:\people
```

The application may later interact with systems under `H:\SOSWebsite`, but the People Intake project root remains independent at `H:\people`.

Do not create or operate this project under:

```text
H:\SOSWebsite\people
```

---

## Prohibited Drive

```text
C:\
```

Intentional controlled project writes to `C:\` are forbidden.

---

## Controlled Write Categories

All of the following must remain on `H:\`:

- Source files
- Documentation
- Temporary files
- Cache files
- Logs
- Build output
- Generated reports
- Test output
- Package cache
- Git repository data
- Netlify state
- Prisma output (future phases)
- Browser automation files
- Uploaded development images
- Screenshots
- Cursor scratch files related to this project
- Generated diagrams

---

## Required Local Directories

```text
H:\people\.tmp
H:\people\.cache
H:\people\.npm-cache
H:\people\.test-output
H:\people\.local-storage
H:\people\.netlify
H:\people\docs
H:\people\develop_notes
H:\people\contracts
H:\people\diagrams
H:\people\scripts
H:\people\reports
```

---

## Required Environment Variables

Before running package or script commands:

```powershell
$env:TEMP="H:\people\.tmp"
$env:TMP="H:\people\.tmp"
$env:TMPDIR="H:\people\.tmp"
$env:npm_config_cache="H:\people\.npm-cache"
```

---

## Command Execution Rules

1. Run commands from `H:\people` (or an authorized subdirectory).
2. Do not run project commands from `C:\`.
3. Do not install packages globally for this project.
4. Do not use `%TEMP%` unless it resolves to `H:\people\.tmp`.
5. Do not use the Windows user-profile directory as a project workspace.
6. Do not clone or initialize another copy of this repository elsewhere.

If a required tool cannot operate without creating controlled project data on `C:\`, stop and document the limitation instead of continuing.

---

## Dependency Rules

- Install dependencies only inside `H:\people`.
- Prefer project-local npm cache at `H:\people\.npm-cache`.
- Do not copy `node_modules` from unrelated projects on `C:\`.

---

## Cache Rules

Controlled caches:

| Cache | Location |
| --- | --- |
| npm | `H:\people\.npm-cache` |
| General project cache | `H:\people\.cache` |
| Temporary files | `H:\people\.tmp` |
| Test output | `H:\people\.test-output` |
| Local storage fixtures | `H:\people\.local-storage` |
| Netlify CLI state | `H:\people\.netlify` |

---

## Git Rules

- Initialize and operate Git only inside `H:\people`.
- Do not create a second clone on `C:\` for convenience.
- Do not store secrets in the repository.

---

## Netlify Rules

- Netlify state for this project belongs under `H:\people\.netlify`.
- Do not deploy application code before design freeze and explicit authorization.
- Documentation-only Netlify deployment is unnecessary during governance.

---

## Prisma Rules (Future Phases)

When Prisma is authorized after design freeze:

- Schema, migrations, and generated client must live under `H:\people`.
- Temporary Prisma output must use `H:\people\.tmp` or project-local paths.
- No Prisma artifacts may be intentionally written to `C:\`.

---

## Test-Output Rules

All test reports, coverage, screenshots, and automation artifacts must write to:

```text
H:\people\.test-output
```

or another approved `H:\people` subdirectory.

---

## Image-Fixture Rules

Development images and fixtures must remain under:

```text
H:\people\.local-storage
```

or an explicitly approved uploads-dev path under `H:\people`.

Never place volunteer source images in public repositories or public CDN paths.

---

## Preflight Behavior

Before creating or modifying project artifacts, Cursor must:

1. Confirm working directory is under `H:\people`.
2. Confirm TEMP/TMP/TMPDIR point to `H:\people\.tmp`.
3. Confirm npm cache points to `H:\people\.npm-cache`.
4. Confirm required H-drive directories exist.
5. Stop if a controlled path resolves to `C:\`.

Use:

```text
npm run drive:validate
```

---

## Failure Behavior

On controlled-path violation:

1. Stop immediately.
2. Do not continue the build.
3. Record the failure in `H:\people\reports\`.
4. Remediate path configuration before retrying.

---

## Honest Limitations

Windows, Cursor, Node, browsers, or authentication tools may independently write application-level files to the user profile on `C:\`. This protocol aggressively configures every command we control to use `H:\`, adds validation scripts that detect forbidden controlled paths, and stops the build when a project artifact is configured for `C:\`.

This protocol does **not** claim that a web application or Cursor session can prevent Windows itself from writing operating-system files.
