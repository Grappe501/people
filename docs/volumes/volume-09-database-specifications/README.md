# Volume 9 — Database Specifications

**Status:** DESIGN COMPLETE — PENDING CROSS-VOLUME VALIDATION  
**Document ID:** PEOPLE-VOLUME-09-DATABASE-SPECIFICATIONS-1.0  
**Project root:** `H:\people`  
**Build mode:** DOCUMENTATION ONLY

## Canonical document

| Item | Path |
| --- | --- |
| **Master specification** | [`VOLUME_09_DATABASE_SPECIFICATIONS.md`](./VOLUME_09_DATABASE_SPECIFICATIONS.md) |
| Legacy pointer | [`docs/10_database_specifications/VOLUME_09_DATABASE_SPECIFICATIONS.md`](../../10_database_specifications/VOLUME_09_DATABASE_SPECIFICATIONS.md) |
| Table registry | [`data/documentation/volume_09_table_registry.json`](../../../data/documentation/volume_09_table_registry.json) |

## What this volume governs

Volume 9 is the **implementation-governing database blueprint** for People Intake. It defines:

- Database principles (`DB-PRINCIPLE-001` … `010`)
- Logical entities and physical table responsibilities
- Keys, constraints, indexes, append-only vs mutable tables
- Transaction boundaries, concurrency, idempotency, provenance, audit
- Classification, archive/delete, migration governance
- Forty locked database decisions and fifteen deferred decisions (`DB-DEC-001` … `015`)

## What this volume does not authorize

- SQL migrations
- Prisma / ORM schemas
- Database provisioning or live connections
- Production credentials or schema deployment
- Application API handlers (Volume 10)
- Production code (Gate G-10 remains closed)

## Supplementary drafts

Per-table drafts under `docs/10_database_specifications/TABLE_*.md` remain **DRAFT_BOOTSTRAP** until reconciled against this master. Prefer the Volume 9 master for naming and ownership.

## Related volumes

| Volume | Topic |
| --- | --- |
| 8 | Technical domain specifications |
| 9 | Database specifications (this volume) |
| 10 | API specifications (next) |

See [`docs/DOCUMENTATION_MASTER_INDEX.md`](../../DOCUMENTATION_MASTER_INDEX.md).
