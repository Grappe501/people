# Open Decisions Register (Documentation Program Mirror)

**Canonical audit register:** `reports/PEOPLE_OPEN_DECISIONS_REGISTER.md`  
**Script:** PEOPLE-DOC-FOUNDATION-AND-INVENTORY-1.0  

This file mirrors blocking decisions for the documentation sequence. Do not invent resolutions.

## Blocking (freeze + precise specs)

| ID | Topic | Spec impact |
| --- | --- | --- |
| OD-B01 | Exact-match auto-link | MATCH-RULE / API resolve |
| OD-B02 | NO_MATCH auto-create | PROMOTION / matching |
| OD-B03 | Canonical state dictionary | All state machines |
| OD-B04 | AMBIGUOUS in UX | Entry / field condition |
| OD-B05 | Shared DB audit | Volume 9 migrations gate |
| OD-B06 | Data Entry upload | Authz / capture |
| OD-B07 | Offline V1 | Draft / config |
| OD-B08 | Match claim model | Claim / queue |
| OD-B09 | 0-entry blank/unreadable submit | Page submit API |
| OD-B10 | Image retention | Storage / retention |
| OD-B11 | Preference supersession | Canonical attributes |
| OD-B12 | Quality/ops docs | Volume 5 |

## Documentation program decisions (proposed, not approved)

| ID | Proposal | Status |
| --- | --- | --- |
| OD-D01 | Retain `docs/00_*`…`docs/16_*` as equivalent to `docs/volumes/*` pointers | **proposed / adopted for DOC-0** |
| OD-D02 | Count bootstrap specs as DRAFT_BOOTSTRAP until DOC-1…6 formalization | **proposed / adopted for DOC-0** |

Mark new discoveries in `reports/PEOPLE_OPEN_DECISIONS_REGISTER.md` as well.
