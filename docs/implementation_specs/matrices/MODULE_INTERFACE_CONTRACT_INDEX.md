# Module Interface Contract Index

**Governed by:** PEOPLE-IS-102-MODULE-BOUNDARY-SPECIFICATION-1.0  
**Status:** Foundation index — detailed payloads expand via IS phases / amendments  
**Rule:** Consumers use these contracts only; never internals.

## Contract classes

| Class | Location | Owner |
| --- | --- | --- |
| Provider-neutral system contracts | `contracts/**` | Platform + capability authors |
| Module ports / DTOs | `<module>/contracts` (logical) | Owning module |
| API fragments | `contracts/api` | Owning API module |
| Events | `contracts/events` | Publishing module |
| Jobs | `contracts/jobs` | Job-owning module |
| Errors/permissions/states | catalogs + `contracts/*` | Catalog authority |

## Seed port contracts (logical IDs)

| Contract ID | Module | Purpose | Status |
| --- | --- | --- | --- |
| CONTRACT-USERS-COMMANDS | MOD-USERS | Create/disable/update user | PLANNED |
| CONTRACT-USERS-QUERIES | MOD-USERS | User read models | PLANNED |
| CONTRACT-BATCHES-COMMANDS | MOD-BATCHES | Batch lifecycle commands | PLANNED |
| CONTRACT-PAGES-QUERIES | MOD-PAGES | Page read model | PLANNED |
| CONTRACT-UPLOADS-COMMANDS | MOD-UPLOADS | Initiate/complete upload | PLANNED |
| CONTRACT-CLAIMS-COMMANDS | MOD-CLAIMS | Acquire/release/heartbeat/expire | PLANNED |
| CONTRACT-CLAIMS-EVENTS | MOD-CLAIMS | Claim acquired/released/expired | PLANNED |
| CONTRACT-DRAFTS-COMMANDS | MOD-DRAFTS | Save draft entry | PLANNED |
| CONTRACT-TRANSCRIPTIONS-COMMANDS | MOD-TRANSCRIPTIONS | Submit/finalize transcription | PLANNED |
| CONTRACT-MATCHING-COMMANDS | MOD-MATCHING | Generate/refresh candidates | PLANNED |
| CONTRACT-MATCHING-QUERIES | MOD-MATCHING | List candidates | PLANNED |
| CONTRACT-RESOLUTION-COMMANDS | MOD-RESOLUTION | Record match decision | PLANNED |
| CONTRACT-PROMOTION-COMMANDS | MOD-PROMOTION | Request/approve/execute promotion | PLANNED |
| CONTRACT-PROMOTION-CANONICAL | MOD-PROMOTION + INT | Canonical person DTO port | BLOCKED (ISSUE-CANONICAL-001) |
| CONTRACT-AUDIT-WRITE | MOD-AUDIT | Append audit event | PLANNED |
| CONTRACT-AUDIT-QUERY | MOD-AUDIT | Query audit trail | PLANNED |
| CONTRACT-NOTIFY-DISPATCH | MOD-NOTIFICATIONS + INT | Dispatch Catalog 6 notification | PLANNED |
| CONTRACT-RETENTION-ENFORCE | MOD-RETENTION | Evaluate/enforce retention actions | PLANNED |
| CONTRACT-PERMISSIONS-CHECK | MOD-PERMISSIONS | Check Catalog 5 key | PLANNED |
| CONTRACT-CONFIG-READ | MOD-CONFIG | Read typed config | PLANNED |

## Compatibility

* Additive fields preferred.  
* Breaking changes require CHANGE-* + consumer list.  
* `PLANNED` means specification placeholder — **not** implemented code.  
* `BLOCKED` cannot be implemented until listed issue/ADR resolves.

## Index maintenance

Every implementation package that introduces a public method, event, or DTO MUST add or update a row here before coding authorization for that package.
