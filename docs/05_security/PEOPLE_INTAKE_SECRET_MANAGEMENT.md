# People Intake — Secret Management

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-SECURITY-API-ENGINEERING-DESIGN-1.0  
**Live secrets authorized:** No

---

## Secret Types (Future)

- Database URL / direct migration URL  
- Supabase URL / publishable key / server key if approved  
- OAuth credentials  
- Storage credentials  
- Canonical-service credentials  
- Internal signing secrets  

---

## Rules

1. Never commit secrets  
2. Never store secrets in Markdown  
3. Never print secrets in logs  
4. Never expose server secrets to browser bundles  
5. Separate secrets by environment  
6. Rotate after suspected exposure  
7. Document variable **names**, not values  
8. Least-privilege credentials  

---

## Environment Files

Local `.env.local` only after implementation begins.

Governance may keep `.env.example` with path/names only — no credentials, no DB URLs with secrets, no Supabase keys.

---

## Credential Separation

| Credential | Use |
| --- | --- |
| Runtime app role | Least privilege for intake + approved canonical ops |
| Migration role | Schema changes only; **not** used by running app |
| Storage admin | Lifecycle/admin — never given to routine users |
| Canonical service | Controlled contract calls |

---

## Production Startup

Missing required production configuration → fail safely. No silent fallback to local DB, public storage, development auth, unrestricted roles, disabled audit, or mock canonical service.
