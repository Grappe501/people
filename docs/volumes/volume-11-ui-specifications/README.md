# Volume 11 — User Interface Specifications

**Status:** DESIGN COMPLETE — IMPLEMENTATION NOT AUTHORIZED  
**Document ID:** PEOPLE-VOLUME-11-USER-INTERFACE-SPECIFICATIONS-1.0  
**Project root:** `H:\people`  
**Build mode:** DOCUMENTATION ONLY

## Canonical document

| Item | Path |
| --- | --- |
| **Master specification** | [`VOLUME_11_USER_INTERFACE_SPECIFICATIONS.md`](./VOLUME_11_USER_INTERFACE_SPECIFICATIONS.md) |
| Legacy pointer | [`docs/12_ui_specifications/VOLUME_11_USER_INTERFACE_SPECIFICATIONS.md`](../../12_ui_specifications/VOLUME_11_USER_INTERFACE_SPECIFICATIONS.md) |
| Screen registry | [`data/documentation/volume_11_screen_registry.json`](../../../data/documentation/volume_11_screen_registry.json) |

## What this volume governs

Volume 11 is the **canonical UX and screen specification**. It defines:

- Four workspaces: Capture, Transcribe, Match, Manage
- Role-aware navigation and screen inventory
- Transcription, match, promotion, and admin workflows
- Loading/empty/error/confirmation patterns
- Accessibility (WCAG 2.2 AA), privacy display, mobile behavior
- Forty locked UX decisions and eighteen deferred decisions (`UI-DEC-001`…`018`)

## What this volume does not authorize

- React components or route files
- CSS or design-system code
- API calls, auth integration, or database access
- Framework selection or production deployment
- Component library implementation (Volume 12)

## Supplementary drafts

Per-area drafts under `docs/12_ui_specifications/UI_*.md` remain **DRAFT_BOOTSTRAP** until reconciled against this master.

## Related volumes

| Volume | Topic |
| --- | --- |
| 10 | API specifications |
| 11 | User interface specifications (this volume) |
| 12 | Component library and design system (next) |

See [`docs/DOCUMENTATION_MASTER_INDEX.md`](../../DOCUMENTATION_MASTER_INDEX.md).
