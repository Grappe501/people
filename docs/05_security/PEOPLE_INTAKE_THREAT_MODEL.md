# People Intake — Threat Model

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-SECURITY-API-ENGINEERING-DESIGN-1.0

---

## Objectives

| Objective | Protect against |
| --- | --- |
| Confidentiality | Unauthorized access to PII, images, matches, audit |
| Integrity | Unauthorized changes, silent overwrites, duplicates, stale writes, unapproved merges, role escalation |
| Availability | Recoverability under storage/DB/job/claim/deployment failures |
| Accountability | Who/what/when/why for meaningful actions |

---

## Trust Boundaries

| Boundary | Trust |
| --- | --- |
| User device / browser | **Untrusted** |
| People Intake server | Enforces authz, validation, claims, audit, signed access, orchestration |
| Intake DB domain | Intake-owned records |
| Private object storage | Original/display/thumbnail; not public |
| Canonical people domain | Higher-trust shared identity spine |
| RedDirt | External app; shared people infrastructure only; no code imports; no operational table writes |

Browser may display authorized data, collect input, hold temporary drafts, request uploads/actions. Browser must **not** determine permissions, assign roles, approve matches, generate canonical IDs, confirm claim ownership, create signed access without server approval, decide idempotency, or decide exact auto-link.

---

## Threats and Controls

| Threat | Controls |
| --- | --- |
| Unauthorized Google user | Approved registry; account status; deny-by-default; access-denied audit |
| Role escalation | Server-loaded roles; no trusted client role; owner-only admin assign; audit |
| Insecure direct object reference | Record-level authz; non-guessable IDs; workflow checks; no direct object-store access |
| Source image leakage | Private bucket; signed access; no permanent client URLs; no public cache |
| Duplicate person creation | Idempotency; locks; candidate recheck; promotion uniqueness; canonical enforcement |
| Stale page overwrite | Claim verify; version check; STALE_WRITE; preserve draft without overwrite |
| Malicious upload | MIME/ext/size; decode verify; re-encode derivative; quarantine; safe keys |
| Secret exposure | Server-only env; scanning; sanitized errors; gitignore; no secrets in docs; env separation |
| Audit tampering | Append-only; restricted write; no routine update/delete; DB permissions |
| Excessive data access | Record scope; role views; sensitive access audit; limited search; no unrestricted export |
| Cross-application damage | Separate repo/deploy/DB role; controlled canonical contract; no RedDirt imports |
| Request forgery / replay | Secure cookies; CSRF where needed; SameSite; idempotency; nonce/timestamp where needed |

---

## Incident Triggers

- Private image becomes public  
- Unauthorized PII access  
- Secrets in logs/repo  
- Canonical duplication at scale  
- Audit altered/unavailable  
- Writes to unrelated production tables  
- Storage deletes active source evidence  
- Role escalation  
- Repeated promotion failures blocking backlog  

Incident procedures deferred to quality/ops freeze design.
