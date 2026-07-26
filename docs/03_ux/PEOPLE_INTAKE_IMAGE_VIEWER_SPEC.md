# People Intake — Image Viewer Spec

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-WORKFLOW-UX-DESIGN-1.0

---

## Purpose

Let operators read difficult handwriting quickly without altering the stored original image.

---

## Required Controls

```text
Zoom In
Zoom Out
Rotate Left
Rotate Right
Full Screen
Reset View
```

---

## Touch / Pointer Behavior

- Pinch to zoom
- Drag to pan
- Double-tap to zoom
- Maintain position while entering nearby fields
- Return to same zoom/pan after leaving a field or closing fullscreen

---

## Viewing Aids (Display-Only)

```text
Increase Contrast
Increase Brightness
```

These affect viewing only unless the user explicitly saves an edited derivative in a future authorized feature. Version 1 stores and preserves the original.

---

## Full Screen

- Immersive viewing
- Easy close
- Does not discard draft
- Autosave before entering fullscreen

---

## Capture Review Viewer

During upload review, rotation/reorder/replace apply to the page image that will be uploaded. After upload, operator rotation in transcription is viewing-oriented unless an authorized replace workflow is used.

---

## Security / Privacy

- Images load via temporary signed URLs only
- No public permanent URLs
- Expired URL → refresh through authorized path
- Do not log image bytes or signed URLs

---

## Accessibility

- Controls labeled for screen readers
- Keyboard operable zoom/rotate/fullscreen/reset
- Do not rely on color alone for load/error state
- Announce load failures

---

## Performance

- Progressive preview acceptable
- Form remains usable while full-resolution finishes loading
- Prefer display derivative when available; original remains authoritative evidence
