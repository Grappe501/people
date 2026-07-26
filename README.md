# People Intake

Secure, mobile-first paper-to-database intake for volunteer sign-up sheets.

> Capture the page. Transcribe every entry. Match each person. Preserve the evidence.

---

## Current Phase

**Phase 0: Complete Design** (in progress)  
**Build:** `PEOPLE-DATA-MATCHING-STORAGE-DESIGN-1.0` (data + matching + storage package)  
**Design-before-code status:** Active — **no application code authorized**

---

## Authorized Root

```text
H:\people
```

## H-Drive Warning

No intentional project-controlled writes to `C:\`. See:

```text
docs/00_governance/PEOPLE_INTAKE_H_DRIVE_PROTOCOL.md
```

---

## Read First

1. `docs/00_governance/PEOPLE_INTAKE_MASTER_BUILD_PLAN.md`
2. `docs/00_governance/PEOPLE_INTAKE_H_DRIVE_PROTOCOL.md`
3. `docs/00_governance/PEOPLE_INTAKE_DESIGN_BEFORE_CODE_PROTOCOL.md`
4. `docs/00_governance/PEOPLE_INTAKE_SOURCE_OF_TRUTH_REGISTRY.md`
5. `docs/08_implementation/PEOPLE_INTAKE_CURSOR_EXECUTION_PROTOCOL.md`
6. `docs/08_implementation/PEOPLE_INTAKE_PROGRESS_LEDGER.md`
7. `docs/04_data/PEOPLE_INTAKE_DOMAIN_MODEL.md`
8. `docs/04_data/PEOPLE_INTAKE_CANONICAL_PERSON_CONTRACT.md`
9. `docs/04_data/PEOPLE_INTAKE_MATCHING_ENGINE_SPEC.md`

---

## Validation Commands

From `H:\people`, with H-drive env vars set:

```powershell
$env:TEMP="H:\people\.tmp"
$env:TMP="H:\people\.tmp"
$env:TMPDIR="H:\people\.tmp"
$env:npm_config_cache="H:\people\.npm-cache"

npm run drive:validate
npm run governance:validate
npm run governance:all
```

---

## Prohibited Until Design Freeze + Gate G-10

- `src/`
- Application routes / React components
- Prisma migrations
- Auth / storage / matching implementation
- Netlify functions
- Production deployment

---

## Next Recommended Build

```text
PEOPLE-SECURITY-API-ENGINEERING-DESIGN-1.0
```

Design-only. See `develop_notes/NEXT_CURSOR_BUILD.md`.
