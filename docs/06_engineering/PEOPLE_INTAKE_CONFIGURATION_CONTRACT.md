# People Intake — Configuration Contract

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-SECURITY-API-ENGINEERING-DESIGN-1.0

---

## Categories

```text
Application URL
Environment name
Database connectivity
Authentication
Object storage
Claim timeout
Signed URL lifetime
Upload limits
Matching rule version
Background job settings
Canonical contract version
Logging level
Feature flags
```

Exact variable names and numeric values deferred to freeze/ops audit.

---

## Startup Validation

Validate required configuration at startup. Production missing required config → **fail safely**.

### Forbidden Silent Production Defaults

- Local database  
- Public storage  
- Development auth  
- Unrestricted roles  
- Disabled audit  
- Mock canonical service  

---

## Feature Flags (Conceptual)

```text
auto_exact_match_linking
automatic_new_person_promotion
offline_draft_support
heic_conversion
image_view_adjustments
advanced_match_scoring
```

Rules: default high-risk features **off**; environment-aware; server-enforced; audited when changed; documented owner; removal plan after stabilization.

---

## Rate Limiting (Intent)

Apply to: sign-in (as provider supports), upload-intent/complete, signed image access, claim requests, match searches, invitations, admin changes.

Exact numbers deferred; high enough for ops, low enough to deter abuse.

---

## Diagnostics (Admin, Non-Secret)

DB connectivity · storage connectivity · auth configuration health · canonical service status · queue backlog · job failures · promotion failures · claim-expiration health  

Never expose secrets in diagnostics.
