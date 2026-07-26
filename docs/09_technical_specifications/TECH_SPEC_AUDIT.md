# Audit Specification

**Library volume:** 8 — Technical Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## 1. Purpose

Append-only, attributable history of meaningful actions.

## 2. Event Shape

who · what · when · where (requestId, IP hash if approved) · subject refs (batch/page/entry/person) · why (optional) · result

No raw PII dumps, secrets, or signed URLs in audit payloads. Store references + redacted summaries.

## 3. Write Rules

- High-risk ops require successful audit write before commit completes (or compensating policy).  
- Audit is append-only in normal operations.  
- Failures escalate severity CRITICAL when privileged action cannot be audited.

## 4. Query

Admin/Owner search by actor, type, date, batch/page/entry. Paginated.

## 5. Retention

Per privacy/retention design (`PENDING_FREEZE` retention provider decisions).

## 6. Catalog

Normative event names live in Engineering Catalog — Event Catalog.

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 4 Logging and audit
- EVENT_CATALOG.md
