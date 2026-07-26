# Blocking ADR Decision Packet Index

**Slice:** PEOPLE-G10-BLOCKER-REMEDIATION-PACKETS-1.0  
**Status:** PROPOSED FOR STEVE DECISION (none accepted)  
**Verified commit:** `c1c7c36`  
**Gate:** REMAIN CLOSED

```text
Selecting an ADR option does NOT open Gate G-10.
Opening G-10 does NOT authorize implementation.
```

## Recommended Steve decision order

1. ADR-001 Framework  
2. ADR-020 H-Drive enforcement (tooling)  
3. ADR-002 Database provider  
4. ADR-003 ORM  
5. ADR-004 Auth provider **+ method**  
6. ADR-005 Object storage  
7. Then CONDITIONAL ADRs: defer-with-Decision-Log or accept (006–019) before freeze approval  

## Index

| ADR | Title | State | Why it matters | Blocks G-10? | Blocks first MG-*? | Recommended action | If accept | If reject | If defer | Follow-up | Dependencies | Packet |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ADR-001 | Application Framework | OPEN/PROPOSED | ISSUE-PLATFORM-001 | YES (direct) | Scaffolding yes; DDL no | Accept Next.js+React+TS | Locks framework | New evaluation | Blocks freeze | ISSUE-PLATFORM-001 close path | ADR-020 | [packet](adr_decision_packets/ADR-001-DECISION-PACKET.md) |
| ADR-002 | Database Provider | OPEN/PROPOSED | ISSUE-DATABASE-001 | YES | YES | Accept hosted PostgreSQL | Enables MG planning | New engine eval | Blocks MG | Brand TBD OK if stated | ISSUE-DBA-001 | [packet](adr_decision_packets/ADR-002-DECISION-PACKET.md) |
| ADR-003 | ORM / Data Access | OPEN/PROPOSED | MG translation | YES | YES | Accept Prisma+adapters | Locks access layer | Alternate ORM | Blocks MG clarity | Adapter rule in packages | ADR-002 | [packet](adr_decision_packets/ADR-003-DECISION-PACKET.md) |
| ADR-004 | Authentication | OPEN/PROPOSED | ISSUE-AUTH-001 method | YES | Auth packages | Accept Supabase Auth **+ method** | Clears auth blocker | New provider | Weak if method open | Cat 4 amend | ISSUE-AUTH-001 | [packet](adr_decision_packets/ADR-004-DECISION-PACKET.md) |
| ADR-005 | Object Storage | OPEN/PROPOSED | ISSUE-STORAGE-001 | YES | Upload/image | Accept private adapter | Clears storage | Conflict remains | Conditional waiver only | Cat 4 amend | ISSUE-STORAGE-001 | [packet](adr_decision_packets/ADR-005-DECISION-PACKET.md) |
| ADR-006 | Background Jobs | OPEN/PROPOSED | ISSUE-JOBS-001 | CONDITIONAL | Phase 7 | Defer past first MG core w/ DL | Locks jobs early | — | OK with DL | Vendor later | ISSUE-JOBS-001 | [packet](adr_decision_packets/ADR-006-DECISION-PACKET.md) |
| ADR-007 | Notifications | OPEN/PROPOSED | ISSUE-NOTIFY-001 | CONDITIONAL | Notify pkgs | Defer | — | — | OK | Vendor later | ISSUE-NOTIFY-001 | [packet](adr_decision_packets/ADR-007-DECISION-PACKET.md) |
| ADR-008 | API Style | OPEN/PROPOSED | API shape | CONDITIONAL | API pkgs | Accept REST /api/v1 | Locks API | Revise | Freeze impact | Contracts | — | [packet](adr_decision_packets/ADR-008-DECISION-PACKET.md) |
| ADR-009 | Hosting | OPEN/PROPOSED | D-018 | CONDITIONAL | Deploy | Affirm Netlify site + externals | Aligns IS-105 | Revise | OK | — | D-018 | [packet](adr_decision_packets/ADR-009-DECISION-PACKET.md) |
| ADR-010 | Schema Validation | OPEN/PROPOSED | Toolchain | CONDITIONAL | App validation | Accept Zod and/or Ajv | Locks validators | Revise | OK | — | — | [packet](adr_decision_packets/ADR-010-DECISION-PACKET.md) |
| ADR-011 | Test Framework | OPEN/PROPOSED | Tests | CONDITIONAL | Test pkgs | Accept Vitest+Playwright | Locks tests | Alternate | OK | — | — | [packet](adr_decision_packets/ADR-011-DECISION-PACKET.md) |
| ADR-012 | Observability | OPEN/PROPOSED | Telemetry | CONDITIONAL | Ops | Accept logs+OTel; vendor TBD | Posture | — | OK | Vendor later | — | [packet](adr_decision_packets/ADR-012-DECISION-PACKET.md) |
| ADR-013 | Audit Storage | OPEN/PROPOSED | Cat 03 / CON-APP-AUDIT | CONDITIONAL | Audit MG | Accept PG audit tables | Aligns IS-303 | Alternate | Weak for audit MG | — | ADR-002 | [packet](adr_decision_packets/ADR-013-DECISION-PACKET.md) |
| ADR-014 | Idempotency | OPEN/PROPOSED | CON-UNQ-PROMO | CONDITIONAL | Promo MG | Accept | Aligns IS-303 | Revise | OK | — | — | [packet](adr_decision_packets/ADR-014-DECISION-PACKET.md) |
| ADR-015 | Optimistic Concurrency | OPEN/PROPOSED | CON-CONC-OPT-LOCK | CONDITIONAL | Mutable LTs | Accept | Aligns IS-303 | Revise | OK | — | — | [packet](adr_decision_packets/ADR-015-DECISION-PACKET.md) |
| ADR-016 | Canonical Boundary | OPEN/PROPOSED | ISSUE-CANONICAL-001 | CONDITIONAL | Promo | Accept soft-ref+DTO | Core OK | Hard FK now | Contract later | ISSUE-CANONICAL-001 | — | [packet](adr_decision_packets/ADR-016-DECISION-PACKET.md) |
| ADR-017 | Retention | OPEN/PROPOSED | ISSUE-RETENTION-001 | DEFERRED durations | Retention jobs | Accept pattern; defer durations | Pattern locked | — | Durations launch | ISSUE-RETENTION-001 | Cat 08 | [packet](adr_decision_packets/ADR-017-DECISION-PACKET.md) |
| ADR-018 | Feature Flags | OPEN/PROPOSED | Cat 4 | CONDITIONAL | Config | Accept Cat 4 first | — | SaaS | OK | — | — | [packet](adr_decision_packets/ADR-018-DECISION-PACKET.md) |
| ADR-019 | AI / Human Review | OPEN/PROPOSED | Human finalize | CONDITIONAL | Optional AI | Accept assistive+human | Safety | Forbid AI | OK | — | — | [packet](adr_decision_packets/ADR-019-DECISION-PACKET.md) |
| ADR-020 | H-Drive Enforcement | OPEN/PROPOSED | ISSUE-HDRIVE-001 | YES (tooling) | Scaffold/install | Accept IS-104 guard | Enables tooling path | Revise | Blocks installs | ISSUE-HDRIVE-001 | IS-104 | [packet](adr_decision_packets/ADR-020-DECISION-PACKET.md) |

**Steve dashboard:** `reports/PEOPLE_STEVE_G10_DECISION_DASHBOARD.md`
