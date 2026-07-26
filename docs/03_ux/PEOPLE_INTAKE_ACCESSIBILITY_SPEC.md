# People Intake — Accessibility Spec

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-WORKFLOW-UX-DESIGN-1.0

---

## Required Support

- Keyboard-only entry (including desktop grid)
- Screen readers
- Large touch targets
- Visible focus states
- High contrast
- Text zoom
- Reduced motion
- Error summaries
- Accessible image controls
- Accessible Yes/No/Blank controls
- Status announcements (save, claim, upload)
- Portrait and landscape layouts

---

## Form Controls

- Every input has a persistent visible label
- Yes/No/Blank are distinct buttons or radiogroup — not color-only toggles
- Field options (Not Provided / Unreadable) are reachable by keyboard and announced
- Warnings associated with fields via accessible descriptions
- Page review provides an error/warning summary before submit

---

## Image Viewer

- Control names announced (Zoom In, Rotate Left, Full Screen, etc.)
- Fullscreen can be closed with keyboard
- Loading and failure states announced
- Do not convey status by color alone

---

## Queue and Claims

- Claim status and assignee announced
- Expiration warnings announced with time remaining and Continue Working action
- Live regions for Saving/Saved/Offline without stealing focus mid-keystroke excessively

---

## Matching

- Match reasons available as text, not icon-only
- Conflict decisions labeled per field
- Candidate lists navigable by keyboard

---

## Motion

Respect reduced-motion preferences: avoid non-essential animation; keep status changes clear without relying on motion.

---

## Testing Intent

Include screen-reader smoke paths for: claim page, enter one person, review/submit, open match, link/create. Full thresholds deferred to quality design.
