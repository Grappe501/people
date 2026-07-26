# People Intake — Documentation Root

**Program:** PEOPLE-IMPLEMENTATION-SPECIFICATION-LIBRARY-1.0  
**Mode:** DOCUMENTATION_AND_SPECIFICATION_ONLY  
**Production code:** PROHIBITED

## Start here

1. [Volume 0 — Project Constitution](00_governance/PEOPLE_INTAKE_PROJECT_CONSTITUTION.md)  
2. [Documentation Master Index](DOCUMENTATION_MASTER_INDEX.md)  
3. [Documentation Library Map](00_governance/PEOPLE_INTAKE_DOCUMENTATION_LIBRARY.md)  
4. [Design Source Map](traceability/DESIGN_SOURCE_MAP.md)  
5. `contracts/governance/active-build.json`

## Layout

| Path | Role |
| --- | --- |
| `docs/00_governance` … `docs/08_implementation` | Approved Volumes 0–7 content (equivalent structure) |
| `docs/09_*` … `docs/16_*` | Spec bootstrap (DRAFT_BOOTSTRAP) |
| `docs/volumes/` | Canonical volume pointers |
| `docs/catalogs/` | Engineering catalogs (formalize DOC-7…9) |
| `docs/implementation-packages/` | Package framework (DOC-11) |
| `docs/traceability/` | Source maps and later matrices |

## Validation

```powershell
npm run docs:inventory:validate
```
