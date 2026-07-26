# People Intake — Product Charter

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-GOVERNANCE-FOUNDATION-1.0

---

## Product Name

**People Intake**

Internal purpose statement:

> A secure, mobile-first paper-to-database entry queue for creating and updating canonical people records.

---

## Problem Statement

Campaigns and civic organizations collect valuable contact information on handwritten volunteer sheets, but the information often remains trapped on paper, becomes difficult to trace, or is inconsistently entered into multiple systems.

People Intake creates a reliable bridge between paper volunteer forms and the shared people database used by RedDirt and other authorized systems.

---

## User Groups

| Group | Primary job |
| --- | --- |
| Uploader | Capture and upload volunteer sheets |
| Data Entry Operator | Transcribe up to ten people per page |
| Matcher / Reviewer | Resolve uncertain person matches |
| Administrator | Manage queue exceptions, users, and operations |
| Owner | Govern configuration, access, and policy |

---

## Primary Use Case

1. Field staff photograph volunteer sign-up sheets and upload them as a batch.
2. Office staff claim pages from a shared queue.
3. Each page is transcribed into up to ten unique intake entries.
4. Matching links entries to existing canonical people or creates new people.
5. Source images, raw transcription, and audit history are preserved.

---

## Product Promise

Authorized users can move handwritten volunteer contacts into the shared people database quickly, safely, and with full provenance — without turning People Intake into a campaign platform.

---

## Core Workflow

```text
Capture the page → Transcribe every entry → Match each person → Preserve the evidence
```

Operating loop:

```text
Capture → Queue → View → Enter → Submit → Match → Complete
```

---

## Product Principles

1. The **page** is the primary work unit.
2. Each handwritten line is a unique intake entry.
3. Capture, transcription, and matching are separate jobs.
4. Fewest practical decisions and taps at each stage.
5. Evidence and auditability over convenience merges.
6. Least privilege relative to RedDirt and shared data.

---

## Trust Principles

- Do not invent missing data.
- Do not treat unmarked Yes/No fields as No.
- Do not silently merge uncertain people.
- Do not discard raw transcription.
- Do not expose source images publicly.
- Do not send email or texts from Version 1.

---

## Experience Principles

- Mobile-first for capture and transcription.
- Large touch targets and clear Yes / No / Blank controls.
- Shared multi-user queue with atomic claims.
- Autosave and resume after interruption.
- Role-appropriate home screens only.

---

## Success Measures

- Field user can upload a multi-page batch from a phone.
- Office user can claim, enter, and submit pages continuously.
- Reviewer can resolve possible matches without losing provenance.
- Canonical people become available to authorized systems.
- Original images remain private and linked.

---

## Non-Goals

People Intake is not:

- A volunteer management system
- A canvassing tool
- A CRM dashboard
- An OCR product
- A messaging platform
- A public form host

---

## Version 1 Boundaries

See `PEOPLE_INTAKE_SCOPE_AND_BOUNDARIES.md`.

Version 1 focuses on:

- Capture
- Shared queue
- Ten-entry transcription
- Matching review
- Provenance
- Private storage
- Shared canonical people connectivity

---

## Future Expansion Principles

Future features must:

1. Preserve the Capture / Transcribe / Match separation.
2. Remain additive to provenance and audit.
3. Avoid collapsing People Intake into RedDirt.
4. Pass design review before implementation.
5. Respect H-drive and least-privilege protocols.
