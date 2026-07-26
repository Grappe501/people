# API — Session & Users

**Library volume:** 10 — API Specifications  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

### GET /api/v1/session
**Op:** getSession · Roles: any authenticated · Returns session user + roles · Errors: AUTH_REQUIRED · Audit: none (or SessionChecked if required)

### GET /api/v1/me
**Op:** getMe · Profile fields · Errors: AUTH_REQUIRED

### POST /api/v1/sign-out
**Op:** signOut · Clears session · Audit: UserSignedOut

### GET /api/v1/users
**Op:** listUsers · Roles: ADMIN, OWNER · Paginated

### POST /api/v1/users/invite
**Op:** inviteUser · Roles: ADMIN, OWNER · Body: email, roles · Audit: UserInvited · Idempotency: yes

### PATCH /api/v1/users/{userId}
**Op:** updateUser · Roles: ADMIN, OWNER · Audit: UserUpdated

### POST /api/v1/users/{userId}/disable | enable
**Op:** disableUser / enableUser · Roles: ADMIN, OWNER · Audit: UserDisabled / UserEnabled

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- API_CONVENTIONS.md
- api-endpoint-registry.json
