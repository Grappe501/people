# People Security / API / Engineering Design Closeout

**Build:** PEOPLE-SECURITY-API-ENGINEERING-DESIGN-1.0  
**Date:** 2026-07-25

## Established

- Auth (approved users, sessions, roles, lifecycle)
- Authorization matrix + record-level image rules
- Threat model and controls
- Secrets, logging vs audit
- Application layering and repositories
- `/api/v1` inventory + contract requirements + examples
- Domain services
- Errors, HTTP guidance, degradation
- Idempotency, concurrency, state transitions
- Validation and upload security
- Configuration + feature flags
- Canonical integration + background jobs
- Security test requirements
- Machine registries (roles, APIs, errors, transitions, services, jobs, checklist)
- Decisions D-034–D-037

## Not Built

Application code, live auth config, DB roles, migrations, buckets, Netlify functions, production env vars.

## Next

```text
PEOPLE-QUALITY-DEPLOYMENT-OPERATIONS-FREEZE-DESIGN-1.0
```
