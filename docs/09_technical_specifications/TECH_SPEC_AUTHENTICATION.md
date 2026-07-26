# Authentication Specification

**Library volume:** 8 — Technical Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## 1. Purpose

Establish verified identity for every request. Approved users only. No public signup in V1.

## 2. Provider

**Designed:** Supabase Auth (email magic link / password per Owner config).  
**Adapter rule:** Auth provider is swappable behind an AuthPort interface; app code never calls provider SDKs outside the auth adapter.

## 3. Session Model

| Concern | Rule |
| --- | --- |
| Session transport | HTTP-only secure cookie (preferred) or approved bearer for server routes |
| Server trust | Browser tokens are untrusted; validate session server-side every request |
| Idle timeout | Configurable; default per security design |
| Absolute timeout | Configurable |
| Concurrent sessions | Allowed unless Owner policy restricts |
| Sign-out | Invalidate server session; clear client cookie |

## 4. Approved-User Gate

After provider authentication succeeds:

1. Resolve local `app_user` / approved-user record by auth subject ID / email.  
2. If missing → `ACCESS_NOT_APPROVED` (Access Denied screen).  
3. If `disabled` → `ACCOUNT_DISABLED`.  
4. Else attach `userId`, `roles[]`, `displayName` to request context.

## 5. Routes

| Path | Auth required | Notes |
| --- | --- | --- |
| Sign-in handling | No (bootstrap) | Provider callback only |
| All `/api/v1/*` | Yes | Except documented health if any |
| All app workspaces | Yes | |

## 6. Invariants

- Individual accounts only (no shared passwords).  
- Disabled users lose access immediately on next request.  
- Failed auth never reveals whether email exists when policy requires uniformity.  
- Auth events audited: sign-in success/failure (no secrets), sign-out, disable/enable.

## 7. Failure Modes

| Condition | Code | UX |
| --- | --- | --- |
| No session | AUTH_REQUIRED | Redirect sign-in |
| Not approved | ACCESS_NOT_APPROVED | Access Denied |
| Disabled | ACCOUNT_DISABLED | Account Disabled |
| Provider down | DEPENDENCY_UNAVAILABLE | Degraded message |

## 8. Tests Required

- Unauthenticated API → 401  
- Unapproved user → denied  
- Disabled user → denied  
- Approved user with valid session → 200 on `GET /session`  
- Sign-out clears subsequent access  

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 4: Auth architecture
- Volume 10: Session endpoints
- Volume 9: `app_users` table (conceptual)
