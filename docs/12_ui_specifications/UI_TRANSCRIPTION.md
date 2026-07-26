# UI — Transcription Screens

**Library volume:** 11 — UI Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## Data Entry Home
Claim Next primary; secondary My Work / Correction Queue.

## Shared Queue
Read-only list; Claim Next still primary path.

## Page Workspace (critical)
**Layout:** Image pane + entry editor; mobile stacks image top/collapsible.  
**Components:** ImageViewer, EntryEditor, ProgressHeader, StatusBadge, save indicator.  
**Interactions:** Autosave on blur/interval; renew claim; Submit & Open Next.  
**Validation:** Inline field errors; UNKNOWN default for tri-state blanks.  
**Loading:** Skeleton image + form.  
**Empty:** Prompt add person rows up to 10.  
**Error:** Claim lost modal → draft preserved messaging.  
**A11y:** Keyboard between fields; image controls labeled; live region for save status.  
**Mobile:** Large Yes/No/Blank controls; sticky primary action.

## Full-Screen Image Viewer
Zoom/pan/rotate; return to workspace without losing draft.

## Page Review / Submitted
Summary; next claim CTA.

## Correction Queue
Returned pages only.

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
