# Component: ImageViewer

**Library volume:** 12 — Component Library  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## Props
`imageAccessUrl | fetcher`, `rotation`, `initialZoom`, `onRotate`, `onError`, `alt`

## Behavior
Pan/zoom/rotate; does not persist rotations to original without replace-image flow; handles expired signed URL via refresh callback.

## Accessibility
Keyboard zoom/pan shortcuts documented; focusable controls; alt text required.

## Events
`onReady` `onError` `onRotateRequest`

## Styling
Full-bleed within pane; no decorative overlay badges on image (Constitution UX).

## Tests
Rotate; expired URL refresh; keyboard operability.

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 11 UI specs
- Volume 2 Accessibility spec
