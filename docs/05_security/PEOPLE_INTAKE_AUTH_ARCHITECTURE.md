# People Intake — Auth Architecture

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-SECURITY-API-ENGINEERING-DESIGN-1.0  
**Implementation authorized:** No

---

## Governing Principle

> Every action must be authenticated, authorized, traceable, minimal, and recoverable.

Security must not depend on hidden buttons, front-end guards alone, obscure URLs, client-supplied roles, browser state, or permanent image URLs.

---

## Provider

Use the existing ecosystem pattern: **Supabase Auth with Google OAuth**, unless a later compatibility audit requires a different approved provider.

Exact project/redirect/session timeout values are deferred.

---

## Approved Users Only

No public signup.

Access requires all of:

1. Successful Google authentication  
2. Email or user ID in approved-user registry  
3. Account active  
4. Valid assigned role  
5. No access restriction  

### Unapproved sign-in

Show `Access Not Approved`. Do not reveal user lists, roles, admin identities, or whether another email is approved.

---

## User Lifecycle States

```text
INVITED → ACTIVE → SUSPENDED | DISABLED | REVOKED
```

### First sign-in

1. Verify approved identity  
2. Create/activate local application-user record  
3. Apply assigned role  
4. Audit sign-in  
5. Role-specific onboarding  
6. Accept operating/privacy notice when approved  

---

## Application User (Conceptual)

```text
id, auth_provider_user_id, email, display_name
status, primary_role
created_at, activated_at, last_sign_in_at
disabled_at, disabled_by_user_id, disable_reason
```

Optional future: additional_roles, organization/county/batch scope. Version 1 stays simple.

---

## Roles

```text
UPLOADER | DATA_ENTRY | REVIEWER | ADMIN | OWNER
```

Ordinarily one primary role. Multi-role allowed only if authorization clarity is preserved. **No shared accounts.**

---

## Session Requirements

- Secure cookie handling  
- Server-side session verification  
- Refresh  
- Explicit sign-out  
- Account disablement honored promptly  
- Role changes take effect promptly  
- Expiration per approved inactivity / provider session  

Exact timeout deferred.

---

## Session vs Claim

A valid login does **not** automatically preserve a page claim.

On session expiry: preserve draft where possible; re-auth for final writes; revalidate claim; old client cannot overwrite new work.

On disable: stop new actions ASAP; release/review claims; preserve drafts; audit.
