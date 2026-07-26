# UI — Capture Screens

**Library volume:** 11 — UI Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## Uploader Home
Primary CTA: New Batch. List recent batches + status badges.

## New Batch
Metadata fields; continue to camera/select.

## Camera Capture / Select Images
Mobile-first; multi-image; review before upload.

## Review Images
Reorder/remove; confirm.

## Upload Progress / Complete
Per-page progress; retry failed pages; never fake success.

## My Batches / Batch Detail
Progress header; page list; link to detail.

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
