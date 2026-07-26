# Matching Specification

**Library volume:** 8 — Technical Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## 1. Purpose

Find candidate canonical people; score; require human review for uncertain identity.

## 2. Principles (Constitution)

- Prefer temporary duplicates over false merges.  
- Household shared contacts do not independently prove identity.  
- AI may assist ranking; humans decide irreversible identity (`PENDING_FREEZE` auto-link).

## 3. Pipeline

1. Normalize entry fields.  
2. Search candidates (email, phone, name+ZIP, etc. per matching engine design).  
3. Score + tier: EXACT | POSSIBLE | CONFLICT | NONE.  
4. Persist candidates + explanations.  
5. Auto path only if frozen policy allows; else queue for review.  
6. Resolution → promotion request when needed.

## 4. Resolution Options

`LINK_EXISTING` · `CREATE_NEW` · `DEFER` · `RETURN_FOR_CORRECTION` · `NO_ACTION`

## 5. Invariants

- One final resolution per entry version.  
- Conflict never auto-merged.  
- Ranking explanations stored for audit.  
- Stable sort for equal scores (personId tie-break).

## 6. Degradation

If canonical domain unavailable: pause candidate lookup / final resolutions needing canonical; preserve transcription.

## 7. Audit

`MatchRunStarted` `MatchCandidatesGenerated` `MatchResolved` `MatchDeferred` `MatchReturnedForCorrection`

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 3 Matching engine
- Volume 9 match tables
- OD-B exact-match lock
