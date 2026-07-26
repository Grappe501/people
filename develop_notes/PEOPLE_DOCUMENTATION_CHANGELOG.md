# Documentation Changelog

## PEOPLE-DOC-FOUNDATION-AND-INVENTORY-1.0

**Date:** 2026-07-25  

**Summary:**  
Established the canonical documentation structure, inventoried existing People Intake design artifacts, created terminology and source maps, created validation infrastructure, initialized documentation governance registers, aligned inventory schema to DOC-0 Cursor-ready format (`PEOPLE-DOC-####`, hashes, enums), and preserved approved Volumes 0–7 without silent rewrite.

**Files Created (representative):**  
- `data/documentation/document_inventory.json`  
- `data/documentation/terminology_inventory.json`  
- `data/documentation/design_source_map.json`  
- `contracts/documentation/document_inventory.schema.json`  
- `scripts/documentation/build-doc-0-foundation.mjs`  
- `scripts/documentation/validate-documentation-inventory.mjs`  
- `docs/README.md`  
- `docs/DOCUMENTATION_MASTER_INDEX.md`  
- `docs/volumes/volume-*/README.md`  
- `docs/catalogs/terminology/TERMINOLOGY_MATRIX.md`  
- `docs/catalogs/identifiers/IDENTIFIER_STANDARD.md`  
- `docs/traceability/DESIGN_SOURCE_MAP.md`  
- `develop_notes/PEOPLE_DOCUMENTATION_*`  
- Prior session bootstrap Volumes 8–13 / EC / IP under `docs/09_*`…`docs/16_*` (DRAFT)  
- Volume 0 constitution and related governance updates from prior builds in this working tree  

**Files Moved:**  
None (unsafe for history/links; mapped in place)

**Files Modified:**  
`README.md`, `package.json`, `contracts/governance/active-build.json`, governance validators, selected governance docs  

**Documents Classified:**  
See inventory `status_counts`

**Contradictions Found:**  
15 tracked (4 Critical, 8 High, 3 Medium)

**Open Decisions Found:**  
12 blocking (OD-B01–OD-B12) + nonblocking list in reports

**Validation:**  
`npm run docs:foundation:validate` — see latest Cursor report
