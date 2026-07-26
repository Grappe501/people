# Volume 13 — Canonical Platform Standards

**Status:** DESIGN COMPLETE — IMPLEMENTATION NOT AUTHORIZED  
**Document ID:** PEOPLE-VOLUME-13-CANONICAL-PLATFORM-STANDARDS-1.0  
**Project root:** `H:\people`  
**Build mode:** DOCUMENTATION ONLY

## Canonical document

| Item | Path |
| --- | --- |
| **Master specification** | [`VOLUME_13_CANONICAL_PLATFORM_STANDARDS.md`](./VOLUME_13_CANONICAL_PLATFORM_STANDARDS.md) |
| Legacy pointer | [`docs/15_platform_standards/VOLUME_13_CANONICAL_PLATFORM_STANDARDS.md`](../../15_platform_standards/VOLUME_13_CANONICAL_PLATFORM_STANDARDS.md) |
| Platform registry | [`data/documentation/volume_13_platform_registry.json`](../../../data/documentation/volume_13_platform_registry.json) |

## What this volume governs

Volume 13 is the **canonical engineering standard**. It defines:

- Documentation-first doctrine and single source of truth
- Repository, naming, configuration, and environment rules
- Architecture layering and separation of concerns
- Authentication, authorization, privacy, provenance, and audit
- Database, API, UI, media, background-job, and error discipline
- Testing, deployment, dependency, and documentation synchronization
- Eighteen locked engineering decisions
- The next catalog sequence before implementation

## What this volume does not authorize

- Application source under `src/`
- API handlers, routes, or ORM models
- Database migrations
- React/CSS/UI implementation
- Runtime dependency installation for the application
- Production deployment or secrets in source control

## Supplementary drafts

Bootstrap content under `docs/15_platform_standards/PLATFORM_STANDARDS.md` remains **DRAFT_BOOTSTRAP** until reconciled against this master.

## Related volumes / next builds

| Item | Topic |
| --- | --- |
| 12 | Component library and design system |
| 13 | Canonical platform standards (this volume) |
| Next | `PEOPLE-STATE-MACHINE-CATALOG-1.0` |

See [`docs/DOCUMENTATION_MASTER_INDEX.md`](../../DOCUMENTATION_MASTER_INDEX.md).
