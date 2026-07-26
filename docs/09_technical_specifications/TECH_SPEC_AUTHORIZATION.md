# Authorization Specification

**Library volume:** 8 — Technical Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## 1. Purpose

Deny-by-default access control: **role AND record AND state**.

## 2. Roles (V1)

`UPLOADER` · `DATA_ENTRY` · `REVIEWER` · `ADMIN` · `OWNER`

Users may hold multiple roles. Effective permissions = union, still subject to record/state checks.

## 3. Evaluation Order

1. Authenticated?  
2. Approved & enabled?  
3. Role allows operation?  
4. Record ownership / assignment allows?  
5. Resource state allows transition?  
6. Else deny → `ROLE_NOT_ALLOWED` or `RECORD_ACCESS_DENIED`

## 4. Matrix Summary (normative detail in Volume 4 authz matrix)

| Capability | U | DE | R | A | O |
| --- | --- | --- | --- | --- | --- |
| Create batch / upload | ✓ | policy | | ✓ | ✓ |
| Claim entry queue | | ✓ | | ✓ | ✓ |
| Submit page | | ✓ | | ✓ | ✓ |
| Match resolve | | | ✓ | ✓ | ✓ |
| Reassign claim | | | | ✓ | ✓ |
| Manage users | | | | ✓ | ✓ |
| Force complete / reopen | | | | ✓ | ✓ |
| Change security policy | | | | | ✓ |

`PENDING_FREEZE`: Data Entry upload rights marked “Optional by policy” in audit — Owner must lock before coding upload authz for DE.

## 5. Record Rules

- Claimant may edit claimed page draft.  
- Non-claimant cannot mutate draft (except Admin/Owner override with audit).  
- Image access requires page-level authorization + signed URL issuance.  
- Audit search: Admin/Owner (and scoped roles if later approved).

## 6. Server Enforcement

UI may hide controls; **server must enforce**. Never trust client role claims.

## 7. Tests Required

- Each role can perform allowed ops  
- Each role blocked on forbidden ops  
- Cross-user claim mutation denied  
- Override paths audited  

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 4: Authorization matrix
- `contracts/schemas/role-permissions.json`
