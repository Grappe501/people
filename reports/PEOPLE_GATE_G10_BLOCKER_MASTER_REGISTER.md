# Gate G-10 Blocker Master Register

**Document ID:** `PEOPLE-GATE-G10-BLOCKER-MASTER-REGISTER-1.0`  
**Slice:** `PEOPLE-G10-BLOCKER-REMEDIATION-PACKETS-1.0`  
**Workstream:** `PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0`  
**Last verified commit:** `c1c7c36`  
**Gate status:** REMAIN CLOSED  
**Decisions made by this slice:** NONE

```text
This register prepares decisions. It does not make them.
Accepting ADRs / approving freeze / opening G-10 remains Steve authority.
```

---

## Classification note (FINDING)

| Source | Treatment of ADRs |
| --- | --- |
| Remediation plan §3 | **Minimum BLOCKING_G10:** ADR-001…005, ADR-020 |
| Design freeze exit criteria | All major ADRs must be **accepted** (or Owner-accepted deferral) before freeze APPROVED |
| D-078 readiness | Direct blockers vs CONDITIONAL/DEFERRED for non-minimum ADRs |

**Honest discrepancy:** Freeze blanket criterion makes ADR-006…019 relevant to freeze (hence G-10 via ISSUE-FREEZE-001) even when not in the minimum set. They are classified below as `CONDITIONAL` (Decision Log deferral permitted if freeze exit criteria amended) — **not silently dropped**.

---

## Register

| Blocker ID | Source | Title | Classification | Current status | Decision owner | Evidence owner | Required decision | Required evidence | Dependencies | Resolution path | Waiver permitted | Waiver authority | Current recommendation | G-10 effect | MG effect | Traceability | Last verified commit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BLK-ADR-001 | ADR-001 | Application Framework | BLOCKING_G10 | OPEN/PROPOSED | Steve | Burt/Ernie packet | Accept/reject/revise ADR-001 | Decision Log entry | ADR-020 for caches | Steve decision pass | No for G-10 open | Steve | Accept Next.js+React+TS | Blocks freeze/G-10 | Scaffolding | IS-101; ISSUE-PLATFORM-001; packet | c1c7c36 |
| BLK-ADR-002 | ADR-002 | Database Provider | BLOCKING_G10 | OPEN/PROPOSED | Steve | Burt/Ernie | Accept hosted PG (+brand?) | Decision Log | ISSUE-DATABASE-001; ISSUE-DBA-001 | Steve then DBA audit | No | Steve | Accept hosted PostgreSQL | Blocks G-10 | BLOCKING_MG | IS-101; packet | c1c7c36 |
| BLK-ADR-003 | ADR-003 | ORM / Data Access | BLOCKING_G10 | OPEN/PROPOSED | Steve | Burt/Ernie | Accept Prisma-behind-adapters or alternate | Decision Log | ADR-002 | Steve | No | Steve | Accept Prisma+adapters | Blocks G-10 | BLOCKING_MG | IS-101; packet | c1c7c36 |
| BLK-ADR-004 | ADR-004 | Authentication Provider | BLOCKING_G10 | OPEN/PROPOSED | Steve | Burt/Ernie | Provider **and** method | Decision Log; Cat 4 amend if needed | ISSUE-AUTH-001 | Steve | No | Steve | Accept Supabase Auth + choose method | Blocks G-10 | Auth packages | IS-101; packet | c1c7c36 |
| BLK-ADR-005 | ADR-005 | Object Storage | BLOCKING_G10 | OPEN/PROPOSED | Steve | Burt/Ernie | Private storage vs public Netlify assets | Decision Log; Cat 4 | ISSUE-STORAGE-001 | Steve | Yes conditional (non-upload core only) | Steve | Accept private adapter | Blocks G-10 | Upload/image MG | IS-101; packet | c1c7c36 |
| BLK-ADR-006 | ADR-006 | Background Jobs | CONDITIONAL | OPEN/PROPOSED | Steve | Burt/Ernie | Accept/defer past MG core | Decision Log | ISSUE-JOBS-001 | Steve | Yes with DL | Steve | Defer past first MG core | Freeze unless deferred | Phase 7 | IS-101; packet | c1c7c36 |
| BLK-ADR-007 | ADR-007 | Notifications | CONDITIONAL | OPEN/PROPOSED | Steve | Burt/Ernie | Accept/defer | Decision Log | ISSUE-NOTIFY-001 | Steve | Yes | Steve | Defer | Freeze unless deferred | Notify pkgs | packet | c1c7c36 |
| BLK-ADR-008 | ADR-008 | API Style | CONDITIONAL | OPEN/PROPOSED | Steve | Burt/Ernie | Accept REST /api/v1 | Decision Log | — | Steve | Yes | Steve | Accept | Freeze unless deferred | API pkgs | packet | c1c7c36 |
| BLK-ADR-009 | ADR-009 | Hosting | CONDITIONAL | OPEN/PROPOSED | Steve | Burt/Ernie | Affirm D-018 Netlify site | Decision Log | D-018 | Steve | Yes | Steve | Accept IS-105 posture | Freeze unless deferred | Deploy | packet | c1c7c36 |
| BLK-ADR-010 | ADR-010 | Schema Validation | CONDITIONAL | OPEN/PROPOSED | Steve | Burt/Ernie | Zod/Ajv pick | Decision Log | — | Steve | Yes | Steve | Accept Zod and/or Ajv | Freeze unless deferred | App validation | packet | c1c7c36 |
| BLK-ADR-011 | ADR-011 | Test Framework | CONDITIONAL | OPEN/PROPOSED | Steve | Burt/Ernie | Vitest+Playwright | Decision Log | — | Steve | Yes | Steve | Accept | Freeze unless deferred | Tests | packet | c1c7c36 |
| BLK-ADR-012 | ADR-012 | Observability | CONDITIONAL | OPEN/PROPOSED | Steve | Burt/Ernie | Logs+OTel posture | Decision Log | — | Steve | Yes | Steve | Defer vendor | Freeze unless deferred | Ops | packet | c1c7c36 |
| BLK-ADR-013 | ADR-013 | Audit Storage | CONDITIONAL | OPEN/PROPOSED | Steve | Burt/Ernie | Postgres audit tables | Decision Log | ADR-002 | Steve | Limited | Steve | Accept PG audit tables | Freeze / MG audit | BLOCKING_MG audit | IS-303; packet | c1c7c36 |
| BLK-ADR-014 | ADR-014 | Idempotency | CONDITIONAL | OPEN/PROPOSED | Steve | Burt/Ernie | Keys+constraints | Decision Log | IS-303 | Steve | Yes | Steve | Accept | Freeze unless deferred | Promo MG | packet | c1c7c36 |
| BLK-ADR-015 | ADR-015 | Optimistic Concurrency | CONDITIONAL | OPEN/PROPOSED | Steve | Burt/Ernie | Version columns | Decision Log | IS-303 | Steve | Yes | Steve | Accept | Freeze unless deferred | Mutable LTs | packet | c1c7c36 |
| BLK-ADR-016 | ADR-016 | Canonical Person Boundary | CONDITIONAL | OPEN/PROPOSED | Steve | Burt/Ernie | Soft-ref + DTO boundary | Decision Log; contract | ISSUE-CANONICAL-001 | Steve | Yes for core soft-ref | Steve | Accept soft-ref default | Promo blocked if unresolved | Promotion MG | packet | c1c7c36 |
| BLK-ADR-017 | ADR-017 | Retention Enforcement | DEFERRED | OPEN/PROPOSED | Steve | Burt/Ernie | Pattern vs durations | Decision Log | ISSUE-RETENTION-001 | Steve | Yes durations | Steve | Accept pattern; defer durations | Launch | Retention jobs | Cat 08; packet | c1c7c36 |
| BLK-ADR-018 | ADR-018 | Feature Flags | CONDITIONAL | OPEN/PROPOSED | Steve | Burt/Ernie | Cat 4 first | Decision Log | — | Steve | Yes | Steve | Accept Cat 4 | Freeze unless deferred | Config | packet | c1c7c36 |
| BLK-ADR-019 | ADR-019 | AI / Human Review | CONDITIONAL | OPEN/PROPOSED | Steve | Burt/Ernie | Assistive+human required | Decision Log | — | Steve | Yes | Steve | Accept | Freeze unless deferred | Optional AI | packet | c1c7c36 |
| BLK-ADR-020 | ADR-020 | H-Drive Enforcement | BLOCKING_G10 | OPEN/PROPOSED | Steve | Burt/Ernie | Accept IS-104 guard+redirects | Decision Log | ISSUE-HDRIVE-001 | Steve | No for tooling auth | Steve | Accept IS-104 posture | Blocks G-10 tooling | Scaffolding | IS-104; packet | c1c7c36 |
| BLK-ISS-AUTH-001 | ISSUE-AUTH-001 | Auth method conflict | BLOCKING_G10 | OPEN | Steve | Burt | Resolve with ADR-004 | Method choice in DL | ADR-004 | Via ADR-004 packet | No | Steve | Resolve in ADR-004 | Blocks G-10 | Auth | Open-issue register | c1c7c36 |
| BLK-ISS-STORAGE-001 | ISSUE-STORAGE-001 | Storage / Cat 4 conflict | BLOCKING_G10 | OPEN | Steve | Burt | Resolve with ADR-005 | Cat 4 amendment | ADR-005 | Via ADR-005 | Conditional | Steve | Private storage | Blocks G-10 | Upload | register | c1c7c36 |
| BLK-ISS-PLATFORM-001 | ISSUE-PLATFORM-001 | Framework not accepted | BLOCKING_G10 | OPEN | Steve | Burt | ADR-001 accept | DL | ADR-001 | Via ADR-001 | No | Steve | Accept ADR-001 | Blocks G-10 | Scaffold | register | c1c7c36 |
| BLK-ISS-DATABASE-001 | ISSUE-DATABASE-001 | DB provider not selected | BLOCKING_G10 / BLOCKING_MG | OPEN | Steve | Burt | ADR-002/003 | DL | ADR-002/003; DBA-001 | Via ADRs + DBA plan | No | Steve | Accept PG+Prisma path | Blocks G-10/MG | First MG | register | c1c7c36 |
| BLK-ISS-JOBS-001 | ISSUE-JOBS-001 | Job runtime | CONDITIONAL | OPEN | Steve | Burt | ADR-006 | DL | ADR-006 | Defer OK with DL | Yes | Steve | Defer past MG core | Conditional | Phase 7 | register | c1c7c36 |
| BLK-ISS-CANONICAL-001 | ISSUE-CANONICAL-001 | Canonical contract | CONDITIONAL / BLOCKING_PACKAGE | OPEN | Steve | Ernie/Burt | Contract precision | Contract draft | ADR-016 | Soft-ref meantime | Yes for core | Steve | Soft-ref; contract before promo | Conditional | Promo MG | register | c1c7c36 |
| BLK-ISS-RETENTION-001 | ISSUE-RETENTION-001 | Retention durations | DEFERRED | OPEN | Steve | Policy | Durations | Policy approval | ADR-017; Cat 08 | Launch | Yes | Steve | Defer to launch | Not G-10 direct | Launch | register | c1c7c36 |
| BLK-ISS-HDRIVE-001 | ISSUE-HDRIVE-001 | H-drive guard | BLOCKING_G10 | OPEN | Steve | Burt | ADR-020 | DL | ADR-020 | Via ADR-020 | No | Steve | Accept ADR-020 | Blocks tooling | Scaffold | register | c1c7c36 |
| BLK-ISS-FREEZE-001 | ISSUE-FREEZE-001 | Design freeze blocked | BLOCKING_G10 | OPEN | Steve | Burt/Ernie | Approve freeze after blockers | Freeze report APPROVED | ADRs; Critical issues | Remediation queue | No | Steve | Remediations first | Direct G-10 block | All MG | freeze report | c1c7c36 |
| BLK-ISS-AUDIT-001 | ISSUE-AUDIT-001 | Field-dict vs Cat 01 | MITIGATED | MITIGATED | Ernie/Steve | Burt | Freeze review retain | Banners present | Cat 01; IS-202 | Retain until freeze | N/A | — | Retain mitigated | Freeze review | Enum honesty | register | c1c7c36 |
| BLK-ISS-DBA-001 | ISSUE-DBA-001 | Shared DB audit | BLOCKING_MG | OPEN | Steve (outcome) | Burt plan / auditor | Complete read-only audit | Audit report | ADR-002 | Execute plan later | No for migrationsAuthorized | Steve | Plan ready; execute later | Blocks migrationsAuthorized | First apply | DBA plan | c1c7c36 |
| BLK-FRZ-DENIED | Freeze report | Design freeze DENIED | BLOCKING_G10 | DENIED | Steve | Burt/Ernie | Approve when exit criteria pass | Delta report | All above | Freeze delta | No | Steve | Remediations | Direct | All | freeze delta | c1c7c36 |
| BLK-FLAG-APP | active-build | applicationCodeAuthorized=false | BLOCKING_G10 | false | Steve via G-10 | Burt verify | Set true only after G-10+authz | Gate decision | G-10 OPEN | After G-10 | No | Steve | Keep false | Direct | Impl | active-build.json | c1c7c36 |
| BLK-FLAG-DB | active-build | databaseChangesAuthorized=false | BLOCKING_G10 | false | Steve via G-10 | Burt | Set true only when authorized | Gate decision | G-10 | After G-10 | No | Steve | Keep false | Direct | Schema | active-build | c1c7c36 |
| BLK-FLAG-MIG | active-build | migrationsAuthorized=false | BLOCKING_MG | false | Steve via G-10 | Burt | Set true only when authorized | Gate+DBA | ISSUE-DBA-001 | After G-10+DBA | No | Steve | Keep false | Direct MG | MG apply | active-build | c1c7c36 |

---

## Packet links (ADR)

All packets under `reports/adr_decision_packets/ADR-NNN-DECISION-PACKET.md` (001–020).
