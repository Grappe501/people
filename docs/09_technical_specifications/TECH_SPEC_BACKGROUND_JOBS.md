# Background Jobs Specification

**Library volume:** 8 — Technical Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## 1. Purpose

Reliable async work: matching runs, claim expiry, promotion retry, derivative generation, notifications (if any — V1 limited).

## 2. Job Record

jobId, type, payload ref, status (PENDING|RUNNING|SUCCEEDED|FAILED|DEAD), attempts, nextRunAt, lastError code, idempotencyKey.

## 3. Types (V1 intent)

| Type | Trigger |
| --- | --- |
| MATCH_EVALUATE_PAGE / ENTRY | After submit |
| CLAIM_EXPIRE | Scheduler |
| PROMOTION_RETRY | Failed promotion |
| IMAGE_DERIVATIVE | After upload |
| BATCH_PROGRESS_RECOMPUTE | Optional |

## 4. Rules

- Idempotent handlers.  
- Exponential backoff.  
- Dead-letter after N attempts → exception queue + alert.  
- Never lose transcription because a job failed.

## 5. Observability

Admin visibility into failing jobs; no PII in logs.

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 4 Background processing contract
- Volume 9 job table (if used)
