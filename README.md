# People Intake

Secure, mobile-first paper-to-database intake for volunteer sign-up sheets.

> Capture the page. Transcribe every entry. Match each person. Preserve the evidence.

---

## Current Phase

**Phase 0: Complete Design** (in progress)  
**Build:** `PEOPLE-ARCHITECTURE-AUDIT-AND-DESIGN-VALIDATION-1.0`  
**Design freeze:** **DENIED** — no application code  
**Next:** audit remediation + quality/ops freeze package

---

## Authorized Root

```text
H:\people
```

## H-Drive Warning

No intentional project-controlled writes to `C:\`. See H-drive protocol.

---

## Read First After Audit

1. `reports/PEOPLE_ARCHITECTURE_FINDINGS_REPORT.md`
2. `reports/PEOPLE_OPEN_DECISIONS_REGISTER.md`
3. `reports/PEOPLE_RISK_REGISTER.md`
4. `docs/08_implementation/PEOPLE_INTAKE_DESIGN_FREEZE_REPORT.md`
5. `develop_notes/NEXT_CURSOR_BUILD.md`

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

---

## GitHub

https://github.com/Grappe501/people
