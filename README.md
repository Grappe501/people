# People Intake

Secure, mobile-first paper-to-database intake for volunteer sign-up sheets.

> Capture the page. Transcribe every entry. Match each person. Preserve the evidence.

---

## Current Phase

**Phase 0: Complete Design** (implementation library ready; freeze still DENIED)  
**Last completed build:** `PEOPLE-DOC-FOUNDATION-AND-INVENTORY-1.0` (DOC-0)  
**Design freeze:** **DENIED** — no application code  
**Next:** `PEOPLE-VOLUME-08-TECHNICAL-SPECIFICATIONS-1.0` (DOC-1)  
**Also required for freeze:** audit remediation + Volume 5 quality/ops

---

## Supreme Document — Read Before Every Session

```text
docs/00_governance/PEOPLE_INTAKE_PROJECT_CONSTITUTION.md
```

### Documentation Library (Volumes 0–13 + EC + IP)

| Vol | Title |
| --- | --- |
| 0 | Project Constitution |
| 1 | Governance Foundation |
| 2 | Workflow & User Experience |
| 3 | Data, Matching & Storage |
| 4 | Security, API & Engineering Contracts |
| 5 | Quality, Operations & Design Freeze |
| 6 | Architecture Audit & Design Validation |
| 7 | Master Cursor Build Orchestration |
| 8 | Technical Specifications |
| 9 | Database Specifications |
| 10 | API Specifications |
| 11 | UI Specifications |
| 12 | Component Library |
| 13 | Canonical Platform Standards |
| EC | Engineering Catalogs |
| IP | Implementation Packages |

Map: `docs/00_governance/PEOPLE_INTAKE_DOCUMENTATION_LIBRARY.md`

Then: `contracts/governance/active-build.json`

---

## Authorized Root

```text
H:\people
```

## H-Drive Warning

No intentional project-controlled writes to `C:\`. See H-drive protocol.

---

## Validation

```powershell
$env:TEMP="H:\people\.tmp"
$env:TMP="H:\people\.tmp"
$env:TMPDIR="H:\people\.tmp"
$env:npm_config_cache="H:\people\.npm-cache"
npm run governance:all
```

---

## Prohibited

Application code, Prisma migrations, production auth/storage config, Netlify app deploy for features — until freeze APPROVED and Gate G-10 opens.

Do not invent endpoints, tables, states, errors, events, or components absent from Volumes 8–13 / EC / IP.

---

## GitHub

https://github.com/Grappe501/people
