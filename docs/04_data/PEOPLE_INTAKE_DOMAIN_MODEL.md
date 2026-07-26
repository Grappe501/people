# People Intake — Domain Model

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-DATA-MATCHING-STORAGE-DESIGN-1.0  
**Implementation authorized:** No

---

## Governing Principle

> Preserve what was written, record what was typed, normalize what is safe, and never hide how a canonical person was created or changed.

Every important value must remain distinguishable as one of:

```text
Source Evidence
Raw Transcription
Normalized Intake Value
Canonical Person Value
Match Decision
Accepted Person Update
Rejected Person Update
```

These layers must never be silently collapsed.

---

## Core Hierarchy

```text
Intake Batch
  → Intake Page
    → Intake Entry
      → Match Evaluation
        → Canonical Person (via controlled promotion)
```

Supporting concepts:

```text
Source Image
Page Claim
Field Condition
Match Candidate
Match Resolution
Person Attribute
Person Attribute Source / Provenance
Promotion Request / Result
Audit Event
Processing Error
```

---

## Entity Definitions

### Intake Batch

A group of volunteer-sheet pages uploaded together from one source, event, location, collection effort, or field session. Establishes shared context. Contains pages, not canonical people.

### Intake Page

One photographed or uploaded volunteer sheet. Primary queue item; claim unit; image-level source; parent of 0–10 intake entries; image-quality review unit; completes only when all entries resolve.

### Intake Entry

One handwritten person line from a page. Own ID, row number (1–10), transcription, matching status, canonical relationship (after promotion), field conditions, and audit trail.

### Canonical Person

Durable shared identity across the authorized ecosystem. Not the same as an intake entry. Best current representation of an individual assembled from one or more sources.

### Person Attribute

A specific canonical information piece (name, email, phone, ZIP, volunteer preference, email-list preference) with provenance and history — not a silent flat overwrite.

### Match Candidate

An existing canonical person who may correspond to a new intake entry, with signals, conflicts, confidence, rank, explanation, and resolution status.

### Match Resolution

Final determination for an intake entry: `LINK_EXISTING`, `CREATE_NEW`, `DEFER`, `RETURN_FOR_CORRECTION`, `NO_ACTION`.

### Source Image

Private original photograph/upload for one page, plus optional display/thumbnail derivatives.

### Provenance

Where information came from, who entered it, when, which image, what normalization, what match decision, what canonical change, and who approved it.

---

## Data Layer Separation

| Layer | Contents |
| --- | --- |
| Source | Original image, filename, upload metadata, batch context, page order, hash, uploader, collection metadata |
| Transcription | Immutable raw operator values after submit (except formal correction history) |
| Normalization | Safe machine-readable counterparts; no meaning reinterpretation |
| Matching | Candidates, scores, reasons, conflicts, human/auto decisions, linkage |
| Canonical | Durable person + attributes (shared domain via promotion) |
| Audit | Append-only meaningful actions |

---

## Ownership Boundary

**People Intake owns:** batches, pages, entries, images, claims, match candidates/resolutions, corrections, promotion requests/results, intake audit, processing errors.

**Shared canonical domain owns:** people, attributes, preference history, merge history, restrictions, cross-system IDs, canonical provenance links.

**RedDirt owns (People Intake must not write):** missions, tasks, events, email workflows, volunteer assignments, relationship scoring, campaign calendars.

---

## Integration Model (Locked)

**Controlled promotion** (Model B): intake resolves matching, then creates a promotion request; a canonical people service performs create/link/add/retire/reject. People Intake does not rely on RedDirt source imports.

---

## Cross-References

- Database architecture: `PEOPLE_INTAKE_DATABASE_ARCHITECTURE.md`
- ERD: `PEOPLE_INTAKE_ERD.md`
- Field dictionary: `PEOPLE_INTAKE_FIELD_DICTIONARY.md`
- Canonical contract: `PEOPLE_INTAKE_CANONICAL_PERSON_CONTRACT.md`
- Matching: `PEOPLE_INTAKE_MATCHING_ENGINE_SPEC.md`
- Provenance: `PEOPLE_INTAKE_DATA_PROVENANCE.md`
- Storage: `PEOPLE_INTAKE_IMAGE_STORAGE_ARCHITECTURE.md`
