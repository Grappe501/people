# Database Specification Overview

**Library volume:** 9 — Database Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## Ownership

People Intake owns `intake_*` and local `app_users` / approval tables. Canonical `people*` structures are shared-domain (names TBD after audit).

## Identifier Rules

- UUID primary keys  
- Human-readable operational codes secondary  
- Never email/phone as PK  
- Avoid sequential public IDs exposing volume  

## Uniqueness Checklist

- (batch_id, page_number) unique  
- (page_id, row_number) unique  
- One ACTIVE claim per page (partial unique index)  
- One final resolution per entry version  
- One active original image version per page  
- Idempotency key unique per operation scope  

## Migration Strategy (future)

1. Shared DB compatibility audit report  
2. Additive migrations only  
3. Separate migration credential  
4. Expand/contract for renames  
5. Rollback notes per migration  

## Naming

snake_case tables/columns. Status enums match Engineering Catalog state machines once frozen.

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 3 Database architecture
- Volume 6 audit OD shared DB
