# Terminology Matrix

**Script:** PEOPLE-DOC-FOUNDATION-AND-INVENTORY-1.0  
**Machine:** `data/documentation/terminology_inventory.json`  
**Also:** Volume 0 Article XIV · `PEOPLE_INTAKE_GLOSSARY.md` · `reports/PEOPLE_TERMINOLOGY_MATRIX.md`

## Semantic locks

| Lock | Rule |
| --- | --- |
| UNKNOWN ≠ NO | `UNKNOWN` must never be interpreted as `NO` |
| Page | One captured source sheet image; primary queue unit |
| Entry | Independently tracked person-intake row from a page |
| Canonical Person | Shared trusted identity; intake does not silently own/redefine it |
| Promotion | Controlled link/contribute into canonical domain |
| Claim | Temporary expiring work assignment — not permanent ownership |
| Audit Event | Durable business history — distinct from operational logs |

## Canonical terms

See `terminology_inventory.json` for Term ID, definition, and owning volume (`PEOPLE-TERM-0001` …).

Minimum locked set includes: People Intake, Canonical People Domain, Canonical Person, Batch, Page, Entry, Entry Field, Source Image, Source Evidence, Raw Transcription, Normalized Value, Field Condition, Claim, Queue, Draft, Submission, Match Evaluation, Match Candidate, Match Signal, Match Resolution, Promotion, Person Attribute, Provenance, Audit Event, Background Job, Idempotency Key, Correlation ID, Reviewer, Data Entry User, Uploader, Administrator, Owner, UNKNOWN.

## Open terminology issues

Linked to contradictions/decisions: X-01/X-02/X-03/X-06/X-07 · OD-B03 · OD-B04.
