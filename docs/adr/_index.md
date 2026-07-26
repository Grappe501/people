# Architectural Decision Records — Index

**Status:** Queue only — individual ADRs are **OPEN / PROPOSED**  
**Authority:** PEOPLE-IS-101-TECHNOLOGY-DECISION-SPECIFICATION-1.0 (D-063)  
**Project root:** `H:\people`

Evaluations and recommendations live in:

```text
docs/implementation_specs/100_platform/PEOPLE-IS-101-TECHNOLOGY-DECISION-SPECIFICATION.md
```

Full ADR markdown acceptances are created when the Decision Log accepts each ADR. Until then, **do not** treat recommendations as approved technology locks for implementation packages.

| ADR | Topic | Recommendation (summary) | Status |
| --- | --- | --- | --- |
| ADR-001 | Application Framework | Next.js + React + TypeScript | OPEN / PROPOSED |
| ADR-002 | Database Provider | Hosted PostgreSQL (brand TBD) | OPEN / PROPOSED |
| ADR-003 | ORM / Data Access | Prisma behind adapters | OPEN / PROPOSED |
| ADR-004 | Authentication Provider | Supabase Auth; **method unresolved** | OPEN / PROPOSED |
| ADR-005 | Object Storage | Private object storage adapter; not public Netlify assets | OPEN / PROPOSED |
| ADR-006 | Background Job Runtime | Dedicated queue/worker; Netlify alone insufficient | OPEN / PROPOSED |
| ADR-007 | Notification Provider | Email behind adapter; vendor TBD | OPEN / PROPOSED |
| ADR-008 | API Style / Versioning | Versioned REST JSON `/api/v1` | OPEN / PROPOSED |
| ADR-009 | Hosting / Deployment | Dedicated Netlify site (D-018) + external backends as needed | OPEN / PROPOSED |
| ADR-010 | Schema Validation | Zod and/or Ajv; contracts authoritative | OPEN / PROPOSED |
| ADR-011 | Test Framework | Vitest + Playwright class toolchain | OPEN / PROPOSED |
| ADR-012 | Observability | Structured logs; OTel-friendly exporter TBD | OPEN / PROPOSED |
| ADR-013 | Audit Storage | Postgres audit tables primary | OPEN / PROPOSED |
| ADR-014 | Idempotency | Keys + unique constraints + app checks | OPEN / PROPOSED |
| ADR-015 | Optimistic Concurrency | Version columns → STALE_VERSION | OPEN / PROPOSED |
| ADR-016 | Canonical Person Boundary | Anti-corruption integration DTOs | OPEN / PROPOSED |
| ADR-017 | Retention Enforcement | Policy metadata + scheduled jobs | OPEN / PROPOSED |
| ADR-018 | Feature Flags | Catalog 4 flags first | OPEN / PROPOSED |
| ADR-019 | AI / Human Review | Assistive only; human review required | OPEN / PROPOSED |
| ADR-020 | H-Drive Enforcement | Repository guard + cache redirects (IS-104) | OPEN / PROPOSED |

```text
APPLICATION IMPLEMENTATION: NOT AUTHORIZED
```
