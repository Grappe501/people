# Volume 10 — API Specifications

**Status:** DESIGN COMPLETE — IMPLEMENTATION NOT AUTHORIZED  
**Document ID:** PEOPLE-VOLUME-10-API-SPECIFICATIONS-1.0  
**Project root:** `H:\people`  
**Build mode:** DOCUMENTATION ONLY

## Canonical document

| Item | Path |
| --- | --- |
| **Master specification** | [`VOLUME_10_API_SPECIFICATIONS.md`](./VOLUME_10_API_SPECIFICATIONS.md) |
| Legacy pointer | [`docs/11_api_specifications/VOLUME_10_API_SPECIFICATIONS.md`](../../11_api_specifications/VOLUME_10_API_SPECIFICATIONS.md) |
| Endpoint registry | [`data/documentation/volume_10_endpoint_registry.json`](../../../data/documentation/volume_10_endpoint_registry.json) |

## What this volume governs

Volume 10 is the **canonical API contract** between UI, backend, and future integrations. It defines:

- Versioned prefix `/api/v1/`
- Endpoint inventory and envelopes
- Authn/authz, validation, idempotency, concurrency
- Pagination, filtering, sorting, error codes
- Audit requirements and canonical integration operations
- Locked API decisions and readiness criteria

## What this volume does not authorize

- Route handlers or framework code
- Controllers, ORM, SQL, or SDKs
- Production deployment
- UI component implementation (Volume 11)

## Supplementary drafts

Per-area drafts under `docs/11_api_specifications/API_*.md` remain **DRAFT_BOOTSTRAP** until reconciled against this master.

## Related volumes

| Volume | Topic |
| --- | --- |
| 8 | Technical domain specifications |
| 9 | Database specifications |
| 10 | API specifications (this volume) |
| 11 | User interface specifications (next) |

See [`docs/DOCUMENTATION_MASTER_INDEX.md`](../../DOCUMENTATION_MASTER_INDEX.md).
