# Configuration Catalog

**Library volume:** Engineering Catalogs  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## Rule

Nothing undocumented. Secrets never in git.

## Environment variables (conceptual names)

| Name | Purpose | Secret |
| --- | --- | --- |
| DATABASE_URL | App DB (least privilege) | yes |
| DATABASE_MIGRATE_URL | Migrations only | yes |
| AUTH_SUPABASE_URL | Auth provider | no |
| AUTH_SUPABASE_ANON_KEY | Public anon if required | careful |
| AUTH_SUPABASE_SERVICE_ROLE | Server only | yes |
| STORAGE_ENDPOINT / keys | Private object storage | yes |
| STORAGE_BUCKET_SOURCE | Source images bucket | no |
| SIGNED_URL_TTL_SECONDS | Image access TTL | no |
| CLAIM_TTL_SECONDS | Default 1800 | no |
| CLAIM_RENEW_WINDOW_SECONDS | Renew policy | no |
| NETLIFY / site keys | Deploy | yes |
| LOG_LEVEL | Logging | no |
| FEATURE_* | Flags below | no |

## Feature flags (V1 intent)

| Flag | Default | Notes |
| --- | --- | --- |
| FEATURE_EXACT_MATCH_AUTOLINK | false | PENDING_FREEZE |
| FEATURE_DATA_ENTRY_UPLOAD | false | PENDING_FREEZE policy |
| FEATURE_MATCH_CLAIM | false | PENDING_FREEZE |
| FEATURE_OFFLINE_DRAFT | false | PENDING_FREEZE V1 offline |

## Runtime settings

Max upload bytes · MIME allowlist · rate limits · session timeouts · job retry limits.

Document actual names in `.env.example` at Phase 0 — still no production secrets in repo.

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 4 Configuration contract
