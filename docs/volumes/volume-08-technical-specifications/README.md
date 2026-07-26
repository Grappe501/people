# Volume 8 — Technical Domain Specifications

**Status:** DESIGN COMPLETE — PENDING FINAL CROSS-VOLUME FREEZE  
**Document ID:** PEOPLE-VOLUME-08-TECHNICAL-DOMAIN-SPECIFICATIONS-1.0  
**Project root:** `H:\people`

## Canonical document

| Item | Path |
| --- | --- |
| **Master specification** | [`VOLUME_08_TECHNICAL_DOMAIN_SPECIFICATIONS.md`](./VOLUME_08_TECHNICAL_DOMAIN_SPECIFICATIONS.md) |
| Legacy pointer | [`docs/09_technical_specifications/VOLUME_08_TECHNICAL_DOMAIN_SPECIFICATIONS.md`](../../09_technical_specifications/VOLUME_08_TECHNICAL_DOMAIN_SPECIFICATIONS.md) |

## What this volume governs

Volume 8 is the **implementation-governing behavioral source of truth** for People Intake domain logic. It defines:

- Global invariants (`PEOPLE-INV-001` … `PEOPLE-INV-015`)
- Actor may/may-not boundaries
- Twenty-eight domain specifications (Authentication through Error Recovery) with stable `*-RULE-*` and `*-INV-*` identifiers
- Transaction boundaries, observability, privacy, accessibility, and future-compatibility constraints
- E2E acceptance criteria (A–H), forty locked domain decisions, and deferred implementation items

## What this volume does not authorize

- Production application code (Gate G-10 remains closed until design freeze)
- Database tables or migrations (Volume 9)
- API routes or HTTP contracts (Volume 10)
- UI components or screens (Volumes 11–12)

## Supplementary drafts

Per-domain draft files under `docs/09_technical_specifications/TECH_SPEC_*.md` remain supplementary references until formally merged or superseded by this volume.

## Related volumes

| Volume | Topic |
| --- | --- |
| 0 | Project Constitution |
| 3 | Data, matching, storage design |
| 4 | Security and API engineering |
| 6 | Architecture audit and open decisions |
| 9 | Database specifications (next) |

See [`docs/DOCUMENTATION_MASTER_INDEX.md`](../../DOCUMENTATION_MASTER_INDEX.md).
