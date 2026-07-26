# Design Source Map

**Script:** PEOPLE-DOC-FOUNDATION-AND-INVENTORY-1.0  
**Machine:** `data/documentation/design_source_map.json`

## Authority hierarchy

1. Volume 0 — Project Constitution  
2. Approved design volumes  
3. Architecture Audit findings and resolutions  
4. Master Cursor Build Orchestration  
5. Newly produced specification volumes (8–13)  
6. Existing implementation (only after Gate G-10)

Lower layers may not silently contradict higher layers.

## Domain → governing paths

| Domain | Volume | Paths / notes |
| --- | --- | --- |
| Constitution | 0 | `PEOPLE_INTAKE_PROJECT_CONSTITUTION.md` |
| Workflow | 2 | `docs/02_workflows/` |
| UX | 2 | `docs/03_ux/` |
| Data / matching / storage | 3 | `docs/04_data/` + image storage/privacy |
| Security | 4 | `docs/05_security/` |
| API / services | 4 | `docs/06_engineering/` |
| Quality / ops | 5 | `docs/07_quality/` — **incomplete** |
| Audit / freeze | 6 | `reports/`, freeze report |
| Orchestration | 7 | `docs/08_implementation/` |
| Spec bridge | 8–13 | `docs/09_*`… bootstrap; formalize via DOC-1…6 |

## Freeze blockers affecting source map

- F-C01 / OD-B12: Quality/ops docs missing  
- F-C04 / OD-B03: Dual state vocabularies  
- OD-B01–OD-B11: See Open Decisions Register  
