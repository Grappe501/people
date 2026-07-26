# People Intake — Tablet and Desktop Spec

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-WORKFLOW-UX-DESIGN-1.0

---

## Goal

Keep the same workflows as mobile, with denser information and keyboard-efficient transcription on wider screens.

---

## Breakpoint Intent

| Class | Layout bias |
| --- | --- |
| Phone | One-person stack |
| Tablet | Image top or left; compact grid or hybrid |
| Desktop | Image left; ten-row grid right |

Exact CSS breakpoints deferred; behavior contracts are fixed here.

---

## Transcription: Desktop Grid

### Columns

| # | Last | First | Email | Phone | ZIP | Volunteer | Email List | Status |

### Behavior

- Ten available rows
- Blank rows ignored on submit
- Tab moves horizontally
- Enter may move to next row
- Yes/No/Blank keyboard accessible
- Autosave after changes
- Inline row warnings
- Image remains visible beside or above

### Sticky controls

```text
Save Draft · Review Page · Release Page
```

Primary path still ends at Review → Submit Page & Open Next.

---

## Split-Screen Layouts

### Desktop recommended

```text
Left: Source image (viewer controls)
Right: Entry grid
```

### Smaller tablet

```text
Top: Source image
Bottom: Entry grid
```

---

## Capture on Desktop/Tablet

Upload From Device is primary; camera may still be available when hardware allows. Review grid of thumbnails with drag-reorder.

---

## Matching on Desktop

Two- or three-column match workspace:

- Left: source image
- Center: intake entry + reasons
- Right: existing person + other candidates

Conflict table may use true columns:

| Field | Existing | New Intake | Decision |

---

## Admin Desktop

Operational dashboard with metric tiles and tables:

- Batches with priority controls
- Queue with claim holders and ages
- Exceptions
- Users
- Audit search results

---

## Keyboard and Focus

- Visible focus everywhere
- Grid usable without mouse
- Shortcuts may be added later; Tab/Enter/Space must work in Version 1 design intent
- Esc closes full-screen image without losing form draft

---

## Do Not

- Force phone one-at-a-time UI on large screens as the only mode
- Hide the image while typing on desktop
- Require hovering to discover primary actions
