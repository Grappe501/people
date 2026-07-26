# People Workflow + UX Design Closeout

**Build:** PEOPLE-WORKFLOW-UX-DESIGN-1.0  
**Date:** 2026-07-25

---

## What This Build Established

Complete operating behavior for every role before database/API design:

- User roles and provisional permission matrix
- Capture / transcription / matching / exception workflows
- Shared queue and claiming (atomic, renewable, expiring)
- Conceptual batch/page/entry state machines
- UX architecture and 44-screen inventory
- Mobile vs tablet/desktop transcription layouts
- Image viewer, form behavior, accessibility, copy
- UX acceptance tests and 30 critical edge cases
- Locked UX decisions D-021–D-028
- Explicit deferrals for data/storage/engineering

---

## Intentionally Unbuilt

- Domain model / ERD / field dictionary
- Canonical person contract details
- Match-score formulas and auto-link rules
- Storage provider selection
- API/service contracts
- Application code
- Database migrations

---

## Gates Advanced

- Gate G-3 (Workflow Design): targeted complete for draft package
- Gate G-4 (UX Design): targeted complete for draft package
- Gate G-10: still closed

---

## Recommended Next Build

```text
PEOPLE-DATA-MATCHING-STORAGE-DESIGN-1.0
```

Still design-only.
