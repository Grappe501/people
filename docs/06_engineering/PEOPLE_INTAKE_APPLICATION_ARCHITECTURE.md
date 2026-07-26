# People Intake — Application Architecture

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-SECURITY-API-ENGINEERING-DESIGN-1.0  
**Code authorized:** No

---

## Stack Alignment (Intent)

Next.js · TypeScript · React · Prisma · hosted Postgres · Supabase Auth · private object storage · Netlify · server API routes/functions · schema validation  

Exact package versions deferred.

---

## Trust Model Recap

Browser untrusted → Server enforces everything sensitive → Intake DB / private storage / canonical domain via controlled contracts → RedDirt external.

---

## Layering

```text
UI (role workspaces)
→ Versioned HTTP API /api/v1
→ Domain services
→ Repositories / persistence boundaries
→ Intake DB + Object storage + Canonical people contract
→ Audit + Jobs + Error recovery
```

---

## Repository Boundaries

```text
BatchRepository, PageRepository, ClaimRepository
EntryRepository, MatchingRepository, PromotionRepository
ImageRepository, AuditRepository, UserRepository
```

Rules:

- UI does not query DB directly  
- Browser does not import server repositories  
- Matching does not bypass promotion  
- Promotion does not modify intake evidence  
- RedDirt code is not imported  

---

## Domain Services

See `PEOPLE_INTAKE_SERVICE_CONTRACTS.md` for Auth, Authz, Batch, Upload, Queue, Draft, Transcription, Matching, Match Review, Promotion, Image Access, Audit, Error/Recovery.

---

## Browser Security (Intent)

Secure/HttpOnly/SameSite cookies · CSRF where needed · CSP · referrer policy · frame restrictions · MIME sniffing protection · secure transport · sanitized redirects  

Exact headers deferred to implementation planning.

---

## Offline Draft Security

Local drafts may contain PII: minimize; tie to user+page; avoid permanent unencrypted storage where possible; clear on complete/logout when safe; revalidate claim before sync; document device-sharing risk. Full offline may be deferred if too complex for V1.
