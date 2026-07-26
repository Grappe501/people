# People Data / Matching / Storage Design Closeout

**Build:** PEOPLE-DATA-MATCHING-STORAGE-DESIGN-1.0  
**Date:** 2026-07-25

---

## Established

- Domain hierarchy and layer separation
- Controlled promotion into canonical people (Model B)
- Field conditions + consent semantics
- Matching philosophy, signals, tiers, household protection
- Provenance and append-only audit/corrections
- Private object storage with original/display/thumbnail
- Ownership boundaries vs RedDirt
- Migration/rollback principles and pre-audit gate
- Conceptual JSON contracts for core entities
- Locked decisions D-029–D-033

---

## Not Built (Correctly)

- Prisma models / SQL migrations / live tables
- Storage buckets
- API routes / application code
- Shared DB inspection (required before migrations)
- Exact auto-link / score / retention numbers

---

## Next Build

```text
PEOPLE-SECURITY-API-ENGINEERING-DESIGN-1.0
```
