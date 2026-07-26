# UI — Matching Screens

**Library volume:** 11 — UI Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## Reviewer Home / Match Queue
Claim next match work.

## Match Workspace
Entry summary + candidates ranked + ImageViewer.  
Actions: Link · Create New · Defer · Return correction.  
Conflict UI forces explicit field decisions.

## Field Conflict Review / Create New Person Review
Confirm attributes before promotion request.

## Match Complete / Deferred Review
Clear next step.

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 2 UX docs
- Volume 12 components
