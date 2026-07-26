# PEOPLE-IS-103 — ENVIRONMENT ARCHITECTURE

**Title:** Environment Architecture  
**Document ID:** `PEOPLE-IS-103-ENVIRONMENT-ARCHITECTURE-1.0`  
**Version:** 1.0  
**Status:** APPROVED  
**Phase:** PHASE 1 — REPOSITORY AND PLATFORM ARCHITECTURE  
**Project Root:** `H:\people`  
**Owner:** People Intake System Program  
**Approval Authority:** Decision Log D-066  
**Created Date:** 2026-07-26  
**Last Updated:** 2026-07-26  
**Governing Documents:** IS-000…005; IS-100; IS-101; IS-102; Catalog 4; Secret Management; Configuration Contract; D-018  
**Dependencies:** IS-102 APPROVED (D-064); ADR-009 OPEN (hosting detail); ADR-004/005/002 OPEN (provider env vars remain named, not valued)  
**Implementation Authorization:** `IMPLEMENTATION NOT AUTHORIZED`

```text
DESIGN COMPLETE
APPROVED FOR DOCUMENTATION GOVERNANCE
APPLICATION IMPLEMENTATION NOT AUTHORIZED
```

---

## 1. Purpose

Define the environment topology for People Intake: Preview, Staging, and Production (plus local development), including configuration boundaries, secret posture, data isolation, deployment evidence separation, and H-drive local-env rules — without authorizing live environment provisioning or secret material.

## 2. Scope

Environment classes; naming; config ownership (MOD-CONFIG); secret vs non-secret separation; `.env.example` rules; local vs remote config; Netlify env injection boundaries; database/storage/auth/job env separation; promotion of config changes; validation at startup; forbidden silent defaults; relationship to IS-105.

## 3. Out of Scope

* Provisioning real Netlify/DB/storage accounts  
* Storing or documenting secret values  
* Accepting open ADRs  
* Creating runtime config loaders in `src/`  
* Authorizing production deployment  

## 4. Governing References

IS-100 §§23, deployment separation; IS-101 ADR-009; Catalog 4; `PEOPLE_INTAKE_SECRET_MANAGEMENT.md`; `PEOPLE_INTAKE_CONFIGURATION_CONTRACT.md`; PEOPLE-PROTOCOL-COMMIT-PUSH-DEPLOY-1.0; D-018.

## 5. Definitions

| Term | Meaning |
| --- | --- |
| Environment | Isolated runtime context with its own config, secrets, and data boundary |
| Local | Developer workstation under `H:\people` |
| Preview | Ephemeral PR/branch deploy context |
| Staging | Persistent pre-production verification context |
| Production | Live constituent-facing context |
| Secret | Credential or key that grants access; never committed |
| Config name | Environment variable **name** safe to document |

## 6. Assumptions

* Dedicated Netlify site preferred (D-018) once authorized — not inherited from unrelated SOSWebsite apps.  
* Providers remain behind adapters (IS-102).  
* Exact provider brands follow accepted ADRs; until then, document **names** only.  

## 7. Functional Requirements

| ID | Description |
| --- | --- |
| REQ-ENV-001 | The system MUST distinguish Local, Preview, Staging, and Production. |
| REQ-ENV-002 | Each remote environment MUST have separate secrets and data boundaries. |
| REQ-ENV-003 | Secret values MUST NOT appear in Git, markdown, fixtures, or logs. |
| REQ-ENV-004 | `.env.example` MAY list names and descriptions only. |
| REQ-ENV-005 | Local `.env` files MUST be gitignored and stored only under project-controlled H-drive paths. |
| REQ-ENV-006 | Production MUST fail safely if required configuration is missing (no silent unsafe defaults). |
| REQ-ENV-007 | Preview success MUST NOT authorize Production release. |
| REQ-ENV-008 | Environment name MUST be explicit in runtime config (`APP_ENV` or equivalent). |
| REQ-ENV-009 | Config keys that appear in Catalog 4 MUST map to documented env/config names without inventing undocumented production keys. |
| REQ-ENV-010 | Cross-environment credential reuse for Production is PROHIBITED. |
| REQ-ENV-011 | Deployment evidence MUST be retained per environment (IS-100 deployment reports). |
| REQ-ENV-012 | Local caches/temp for tooling MUST remain under `H:\people` (ADR-020 / IS-104). |

## 8. Nonfunctional Requirements

| ID | Description |
| --- | --- |
| NFR-ENV-SEC-001 | Least privilege per environment. |
| NFR-ENV-OPS-001 | Operators can identify which environment a log/metric belongs to. |
| NFR-ENV-REL-001 | Staging must be able to run migration/verification dry-runs without touching Production data. |

## 9. Architecture

### 9.1 Environment classes

| Class | Purpose | Data | Secrets | Deploy trigger |
| --- | --- | --- | --- | --- |
| Local | Developer documentation/tooling and future app dev | Synthetic / local only | Developer-local only | N/A |
| Preview | PR/branch verification | Non-production; disposable | Preview-scoped | PR / branch (when authorized) |
| Staging | Pre-prod acceptance | Non-production persistent | Staging-scoped | Manual/approved pipeline |
| Production | Live operations | Production | Production-scoped | Explicit authorization only |

### 9.2 Logical topology

```text
Local (H:\people)
  ├─ .env (gitignored)
  ├─ local/  tmp/  logs/  .npm-cache
  └─ docs + contracts (canonical)

GitHub (source of truth)
  └─ branch / PR

Netlify (when authorized)
  ├─ Preview context
  ├─ Staging context (if configured)
  └─ Production context

Provider backends (when ADRs accepted)
  ├─ Database instances per env
  ├─ Auth projects/tenants per env
  ├─ Object storage buckets per env
  └─ Job/runtime resources per env
```

### 9.3 Configuration ownership

* MOD-CONFIG owns typed loading and startup validation (IS-102).  
* Catalog 4 owns configuration **key language**.  
* Presentation MUST NOT read raw provider secrets.  
* Integrations/infrastructure adapters receive secrets only via environment injection.  

### 9.4 Secret vs non-secret

| May commit | Must not commit |
| --- | --- |
| Variable names | API keys, tokens, passwords |
| Descriptions / purpose | Connection strings with credentials |
| Safe placeholders (`REPLACE_ME`) | Real JWTs, private keys |
| Non-secret feature defaults | Production URLs with embedded secrets |
| `.env.example` | `.env`, `.env.local`, `.env.production` |

### 9.5 Required config name categories (names only)

```text
APP_ENV                    # local | preview | staging | production
APP_BASE_URL
DATABASE_URL               # secret
AUTH_PROVIDER              # aligns Catalog 4 seed language
AUTH_*                     # provider-specific secret names TBD after ADR-004
STORAGE_PROVIDER
STORAGE_*                  # secrets TBD after ADR-005 — private buckets only for intake images
JOB_RUNTIME_*              # TBD after ADR-006
NOTIFICATION_*             # TBD after ADR-007
LOG_LEVEL
FEATURE_*                  # Catalog 4 flags
```

Exact final name list expands with Catalog 4 amendments and accepted ADRs — do not invent production values here.

### 9.6 Forbidden silent production defaults

Production MUST NOT silently default to:

* Local database  
* Public storage for intake images  
* Development authentication bypass  
* Unrestricted roles  
* Disabled audit  
* Shared secrets with Preview/Staging  

### 9.7 Local H-drive rules

* Project root: `H:\people`  
* Local env files only under repo (ignored) or `local/`  
* TEMP/TMP/npm/framework caches → H-drive paths (IS-104 / ADR-020)  
* No intentional C:\ project writes  

### 9.8 Netlify boundary

* Env vars injected per Netlify context when authorized.  
* `.netlify/` is local-only, non-canonical (IS-100).  
* Netlify MUST NOT be treated as source of truth for schemas, docs, or migration state.  
* Dedicated site / dedicated secrets (D-018).  
* Until an authorized deployable surface exists, Netlify deploy is **NOT APPLICABLE** under the commit/push protocol.  

### 9.9 Promotion of configuration

```text
Docs / Catalog 4 amendment
→ Staging verification
→ Production change with approval + evidence
```

Preview may test config shape but cannot alone authorize Production secret changes.

## 10–13. Data / Interface / State / Permission

NOT_APPLICABLE for runtime entities beyond config keys. Permissions to change Production secrets are operational (ops role) — not Catalog 5 page permissions.

## 14. Error and Recovery

Missing required Production config → fail closed. Mis-pointed env (e.g. Staging using Production DB URL) → treat as CRITICAL incident; rotate secrets; record ISSUE/ADR as needed.

## 15–17. Audit / Notification / Jobs

Material Production config/secret rotations SHOULD produce operational audit evidence. Job runtime env isolated per ADR-006.

## 18–19. Security / Retention

Secret management doc remains authoritative. Env-specific backups/retention follow Catalog 8 when data exists.

## 20. Observability

Every log line/metric SHOULD carry environment label. No secrets in logs.

## 21. Testing

Future tests: fail-closed missing config; reject production unsafe defaults; ensure `.env` not packed into artifacts; Preview/Staging/Production config schema validation.

## 22. Acceptance Criteria

| ID | Criterion |
| --- | --- |
| AC-ENV-001 | Four environment classes documented with separate secret/data rules |
| AC-ENV-002 | Secret exclusion rules explicit |
| AC-ENV-003 | `.env.example` policy explicit |
| AC-ENV-004 | Preview ≠ Production authorization |
| AC-ENV-005 | Forbidden silent production defaults listed |
| AC-ENV-006 | H-drive local rules stated |
| AC-ENV-007 | Netlify applicability for deploy protocol stated |
| AC-ENV-008 | No secret values in this document |

## 23. Open Decisions

| ID | Status |
| --- | --- |
| ADR-002/004/005/006/007/009 | OPEN — env var brands finalize with ADR acceptance |
| ISSUE-REPO-002 | OPEN — exact ignore/cache env vars with framework ADR |
| Staging as separate Netlify site vs context | DEFER to IS-105 |

## 24. Risks

| ID | Risk | Mitigation |
| --- | --- | --- |
| RISK-ENV-001 | Secret committed accidentally | gitignore + secret scan + protocol |
| RISK-ENV-002 | Cross-env credential reuse | REQ-ENV-010 |
| RISK-ENV-003 | Preview treated as prod auth | REQ-ENV-007 |
| RISK-ENV-004 | Catalog 4 Netlify storage seed vs private images | IS-101 contradiction; private buckets only |

## 25. Dependencies

IS-100…102; Catalog 4; secret management; IS-104/105 for depth; open ADRs for provider env specifics.

## 26. Traceability

| Requirement | Status |
| --- | --- |
| REQ-ENV-001…012 | FULLY_MAPPED (design) |
| REQ-REPO-014 | FULLY_MAPPED |
| REQ-GOV-010 | VERIFIED (no secrets herein) |

## 27. Implementation Boundary

**Authorized:** this documentation.  
**Forbidden:** creating real env secrets, Netlify production config with live keys, application config loaders, provider provisioning.

## 28. Revision History

| Version | Date | Change | Approval |
| --- | --- | --- | --- |
| 1.0 | 2026-07-26 | Initial environment architecture | D-066 |

## Next

```text
PEOPLE-IS-104-H-DRIVE-WORKSPACE-PROTOCOL-1.0
```

## Final status

```text
PEOPLE-IS-103 ENVIRONMENT ARCHITECTURE: APPROVED (DOCUMENTATION)
APPLICATION IMPLEMENTATION: NOT AUTHORIZED
```
