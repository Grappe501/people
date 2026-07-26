# People Intake — UX Architecture

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-WORKFLOW-UX-DESIGN-1.0

---

## Product Shape

People Intake is three focused workspaces plus administration:

```text
CAPTURE · TRANSCRIBE · MATCH · MANAGE
```

Operating chain:

```text
Capture pages → Shared queue → Transcribe page → Normalize/evaluate → Match review → Link or create → Complete page → Update batch
```

---

## Experience Principles

1. **One clear job per screen**
2. **Next action always obvious** (dominant primary button)
3. **Routine work requires few decisions** (system handles ordering, claims, autosave, next page)
4. **Never hide save status**
5. **Preserve work before navigation**
6. **Plain language only**

### Preferred words

```text
Volunteer Sheet · Page · Person · Possible Match · Needs Review
```

### Avoid in UI

```text
Entity · Record Instance · Canonical Resolution · Candidate Object
```

---

## Navigation Model

Role-specific top navigation (mobile ≤5 visible destinations via bottom/menu).

See `PEOPLE_INTAKE_USER_ROLES.md` for per-role nav lists.

---

## Authentication Entry

### Sign-in

```text
People Intake
Secure volunteer-sheet entry

Continue with Google

Only approved users may access this system.
```

No public signup.

### First login

Brief welcome + role explanation (< 1 minute).

### Returning user

Role home. Unfinished work first when present.

---

## Screen Inventory (44)

### Authentication

1. Sign In  
2. Access Denied  
3. Account Disabled  

### Capture

4. Uploader Home  
5. New Batch  
6. Camera Capture  
7. Select Images  
8. Review Images  
9. Upload Progress  
10. Upload Complete  
11. My Batches  
12. Batch Detail  

### Transcription

13. Data Entry Home  
14. Shared Queue  
15. Page Workspace  
16. Full-Screen Image Viewer  
17. Mobile Person Entry  
18. Desktop Entry Grid  
19. Page Review  
20. Page Submitted  
21. My Work  
22. Correction Queue  

### Matching

23. Reviewer Home  
24. Match Queue  
25. Match Workspace  
26. Field Conflict Review  
27. Create New Person Review  
28. Match Complete  
29. Deferred Review  

### Administration

30. Admin Overview  
31. Batch Management  
32. Queue Management  
33. Claim Detail  
34. Exception Queue  
35. User Management  
36. Audit Search  
37. Audit Detail  
38. Settings  

### Shared

39. Help  
40. Notifications  
41. Account  
42. Session Expired  
43. Offline State  
44. General Error  

Detailed layouts: mobile and tablet/desktop specs.

---

## Notifications (Version 1)

In-app only. Examples: upload finished, correction returned, claim expiring, page reassigned, batch complete. No email/SMS in Version 1.

---

## Help

Contextual short help per workspace (capture readability, unreadable fields, match decisions). Training mode may use non-PII samples only — never public production sheets.

---

## Performance Experience Targets (qualitative)

- Fast home load
- Immediate open after claim
- Progressive image preview
- Form usable while image finishes
- Autosave does not interrupt typing
- Retry only failed uploads
- Queue refresh keeps position

Numeric thresholds deferred.

---

## Cross-References

- Capture: `PEOPLE_INTAKE_CAPTURE_WORKFLOW.md`
- Transcription: `PEOPLE_INTAKE_TRANSCRIPTION_WORKFLOW.md`
- Matching: `PEOPLE_INTAKE_MATCHING_WORKFLOW.md`
- Queue/claims: `PEOPLE_INTAKE_QUEUE_AND_CLAIMING.md`
- Exceptions: `PEOPLE_INTAKE_EXCEPTION_WORKFLOWS.md`
- Copy: `PEOPLE_INTAKE_CONTENT_AND_COPY_GUIDE.md`
- A11y: `PEOPLE_INTAKE_ACCESSIBILITY_SPEC.md`
