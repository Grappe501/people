# Entry Specification

**Library volume:** 8 — Technical Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## 1. Purpose

One handwritten person line; unique identity; ≤10 per page.

## 2. Fields (conceptual)

Raw + normalized pairs for: first/last name, phone, email, ZIP, volunteer (YES/NO/UNKNOWN), email list (YES/NO/UNKNOWN), notes, rowNumber 1–10, field conditions (BLANK/UNREADABLE/etc.).

## 3. Draft vs Submitted

- Draft: mutable under active claim; autosaved.  
- Submitted: raw values treated as evidence; corrections via correction history, not silent overwrite.

## 4. Invariants

- `UNKNOWN ≠ NO`.  
- Blank UI → UNKNOWN for tri-state fields.  
- Unreadable ≠ blank.  
- Row numbers unique per page.  
- Max 10 entries.

## 5. Normalization

Deterministic rules (lowercase email, digits phone, trim names). Never invent missing data.

## 6. Lifecycle

Draft → Transcribed → Matching → (Exact/Possible/No/Conflict) → Linked/Created → Completed (+ correction branches).

`PENDING_FREEZE`: exact-match auto-link policy; 0-entry unreadable submit vs API 1–10.

## 7. Audit

`EntryDraftSaved` `EntrySubmitted` `EntryCorrected` `EntryMatchStatusChanged`

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 3 Field dictionary
- Volume 9 `intake_entries`
