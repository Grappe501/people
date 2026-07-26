# UI — Authentication Screens

**Library volume:** 11 — UI Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## Sign In
**Layout:** Centered form; brand secondary to clarity.  
**Components:** Email/password or magic-link controls per config.  
**States:** Loading · Error (provider) · Success redirect.  
**A11y:** Labels, focus order, error announced.  
**Mobile:** Full width, large tap targets.

## Access Denied
Explain approved-user requirement; no sensitive enumeration.

## Account Disabled
Contact admin message; sign-out control.

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 2 UX docs
- Volume 12 components
