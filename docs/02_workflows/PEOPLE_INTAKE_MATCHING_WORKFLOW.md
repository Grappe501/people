# People Intake — Matching Workflow

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-WORKFLOW-UX-DESIGN-1.0  
**Workspace:** MATCH  
**Primary role:** Matching Reviewer

---

## Purpose

Define post-transcription matching behavior and the human review experience for uncertain people.

---

## Principle

Matching must not interrupt data entry.

```text
Transcribed entry
→ Normalize
→ Search existing people
→ Rank candidates
→ Assign resolution status
```

---

## Outcomes Per Entry

| Outcome | Meaning | Human required? |
| --- | --- | --- |
| Exact Match | Strong identity signal under approved rules | Only if rules require confirmation; auto-link details deferred |
| Possible Match | Plausible but uncertain | Yes |
| No Match | No credible existing person | Creation timing deferred to data design |
| Conflict | Contradictory or ambiguous multi-person signals | Yes |
| Needs Correction | Transcription appears wrong or incomplete for matching | Return to entry |

---

## Exact Match (Conceptual)

May auto-link only under approved rules, for example:

- Exact normalized email
- Compatible name
- No conflicting person identity

Exact auto-link policy is deferred to `PEOPLE-DATA-MATCHING-STORAGE-DESIGN-1.0`.

---

## Possible Match → Human Queue

Reviewer opens unresolved work via:

```text
Review Next Match
```

---

## Match Workspace

### Source information

- Source image
- Batch, page, row
- Uploader, transcriber

### New intake entry

- Raw values
- Normalized values
- Field conditions (Provided / Not Provided / Unreadable)

### Suggested existing person

- Existing values
- Prior sources (when authorized)
- Last updated
- Match reasons

### Other candidates

Ranked alternatives.

### Example explanation

```text
Why this may be the same person

Exact email match
Exact phone match
Last name matches
ZIP matches
```

---

## Reviewer Actions

```text
Link to Existing Person
Create New Person
Choose Different Match
Return for Correction
Defer
```

---

## Field Conflict Review

When new intake differs from existing data, reviewer decides per field within later-approved rules:

| Field | Existing | New Intake | Decision options (conceptual) |
| --- | --- | --- | --- |
| Phone | … | … | Keep Existing / Accept New / Keep Both* |
| ZIP | … | … | Keep Existing / Accept New |

\*Whether multiple active phones/emails are allowed is deferred to data architecture.

---

## Evidence Preservation (Non-Negotiable)

Regardless of decision:

- Raw intake remains unchanged
- Source image remains linked
- Match decision is stored separately
- Existing person history remains available

---

## Reviewer Home Metrics

```text
Possible Matches: 18
Conflicts: 4
Needs Correction: 3
Completed Today: 27
```

---

## After Resolution

Entry moves toward Completed. Page completes only when every valid entry is resolved and no unresolved conflicts/corrections remain for that page.

---

## Success Criteria

A reviewer can open a possible match, understand reasons, compare values, link or create, resolve conflicts, and complete the entry.
