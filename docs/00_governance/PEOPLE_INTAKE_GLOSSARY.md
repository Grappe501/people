# People Intake — Glossary

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-GOVERNANCE-FOUNDATION-1.0

---

## Batch

A collection of photographed pages uploaded together, usually with shared source metadata (event, county, city, collection date, collected by).

## Page

One photographed volunteer sheet. The primary queue work item. Contains one source image and up to ten intake entries.

## Intake Entry

One handwritten person line transcribed from a page. Each entry has its own unique identity even when submitted with other entries from the same page.

## Canonical Person

The shared individual identity used by RedDirt and other authorized systems. Distinct from the raw intake transcription.

## Capture

The workflow in which a field user photographs or uploads volunteer sheets into a batch and shared queue.

## Transcription

The workflow in which an office user reads a page image and manually enters every visible person.

## Matching

The workflow that determines whether an intake entry corresponds to an existing canonical person or should create a new person.

## Match Candidate

A scored possible relationship between an intake entry and an existing canonical person, including reasons and confidence tier.

## Exact Match

A high-certainty match signal (for example exact normalized email or phone under approved rules) that may support automatic linking when explicitly authorized by matching rules.

## Possible Match

An uncertain candidate that requires human review before linking or creating a person.

## Conflict

A match situation with contradictory evidence (for example same email with substantially different names) that must not be auto-merged.

## Claim

An atomic lock granting one user exclusive editing rights to a page for transcription or authorized work.

## Claim Expiration

The time after which an inactive claim returns the page to the queue. Recommended default: 30 minutes, renewable on activity.

## Queue

The shared multi-user work list of pages moving through upload, entry, matching, review, and completion stages.

## Raw Value

Exactly what the operator transcribed from the sheet (for example `phone_raw`).

## Normalized Value

A cleaned comparison form of a value (for example lowercase email or digits-only phone) used for matching and operations without discarding the raw value.

## Provenance

The full trail linking a person attribute or decision to batch, page, entry, image, uploader, transcriber, reviewer, and timestamps.

## Audit Event

An append-only record of a meaningful system or user action.

## Source Image

The original uploaded photograph or scan of a volunteer sheet, stored privately and linked to the page.

## Object Storage

Private file storage for source images (and optional viewing derivatives), distinct from Postgres row storage.

## Design Freeze

The gate after which design contracts are considered authoritative for implementation until formally amended.

## Design Gate

A named checkpoint that must pass before progressing to a later design or implementation stage.

## Implementation Gate

The authorization gate that permits creation of application code (Gate G-10).

## Unknown

For Volunteer and Email List: the paper did not clearly indicate Yes or No. Stored as `UNKNOWN`. Must never silently become `NO`.

## Unreadable

Writing appears to be present but cannot be read confidently. Distinct from blank / not provided.

## Not Provided

The field was left empty on the sheet by choice or omission, not because handwriting was illegible.
