# Promotion Specification

**Library volume:** 8 — Technical Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## 1. Purpose

Controlled bridge from intake resolution to canonical people domain (Model B).

## 2. Flow

Match resolution → `PromotionRequest` → Canonical service → `PromotionResult` → update entry/page status.

Browsers never call raw canonical mutation APIs.

## 3. Request Payload (conceptual)

entryId, resolutionId, action (CREATE|LINK|UPDATE_ATTRIBUTES), attribute decisions, idempotencyKey, actorId, provenance bundle.

## 4. Invariants

- Idempotent retry safe.  
- Provenance required for every promoted value.  
- Page not falsely marked complete while promotion pending.  
- No RedDirt operational table writes.  
- No routine automatic merges.

## 5. Failure

Canonical unavailable → keep resolution; mark promotion pending/retryable; user-safe message.

## 6. Audit

`PromotionRequested` `PromotionSucceeded` `PromotionFailed` `PromotionRetried`

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 3 Canonical person contract
- Volume 4/6 engineering integration contract
