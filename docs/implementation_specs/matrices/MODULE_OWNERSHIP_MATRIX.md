# Module Ownership Matrix

**Governed by:** PEOPLE-IS-102-MODULE-BOUNDARY-SPECIFICATION-1.0  
**Rule:** Exactly one owner per capability artifact class row.

## Capability ownership (primary)

| Module | Owns (business) | Entities / tables (seed) | API family (seed) | Jobs (seed) | Audit focus | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| MOD-USERS | User lifecycle | `app_users` | API-USER-* | — | user admin events | |
| MOD-ROLES | Role assignment | role tables (future) | API-ROLE-* | — | role changes | Catalog 5 roles |
| MOD-PERMISSIONS | Enforcement helpers | — | — | — | denied attempts (as designed) | Keys = Catalog 5 |
| MOD-IDENTITY | Identity binding | identity links (future) | session-related | — | auth bind | Provider via INT |
| MOD-INVITATIONS | Invites | invitation tables (future) | API-INVITE-* | — | invite events | |
| MOD-BATCHES | Batches | `intake_batches` | API-BATCH-* | batch jobs | batch lifecycle | |
| MOD-UPLOADS | Upload + image binaries refs | `intake_source_images` | API upload family | processing jobs | upload events | Private storage adapter |
| MOD-PAGES | Page metadata/sequence | `intake_pages` | API-PAGE-* | — | page events | |
| MOD-QUEUES | Queue projection/order | queue views/tables (future) | API-QUEUE-* | — | — | No claim writes |
| MOD-CLAIMS | Claims | `intake_page_claims` | API-CLAIM-* | claim expiration | CLAIM_* audit | Exclusive hold |
| MOD-DRAFTS | Draft entry state | `intake_entries` (draft) | draft APIs | — | draft events | See ISSUE-MOD-001 |
| MOD-TRANSCRIPTIONS | Transcription workflow | `intake_entries` (submitted) | transcription APIs | — | transcription events | See ISSUE-MOD-001 |
| MOD-NORMALIZATION | Normalize fields | — (pure/domain) | — | — | — | May be domain service |
| MOD-MATCHING | Candidates | `intake_match_candidates` | API-MATCH-* | match jobs | match events | |
| MOD-RESOLUTION | Decisions | `intake_match_resolutions` | resolution APIs | — | resolution events | |
| MOD-PROMOTION | Promotion | `intake_promotion_requests` | API-PROMOTION-* | promotion jobs | promotion events | Canonical INT |
| MOD-NOTIFICATIONS | Notification triggers | — | — | notify jobs | notify audit as required | Catalog 6 names |
| MOD-AUDIT | Audit store/query | `intake_audit_events` | API-AUDIT-* | — | self | Catalog 3 names |
| MOD-REPORTS | Reporting reads | read models | API-REPORT-* | report jobs | — | ISSUE-MOD-002 |
| MOD-EXPORTS | Exports | export artifacts meta | API-EXPORT-* | export jobs | export audit | Classification |
| MOD-RETENTION | Retention orchestration | retention policy links | admin retention APIs | retention jobs | retention audit | Catalog 8 |
| MOD-OPERATIONS | Ops/admin UX/services | — | API-ADMIN-* | ops jobs | admin audit | |
| MOD-CONFIG | Config loading | — | — | — | config change audit | Catalog 4 keys |
| MOD-OBSERVABILITY | Telemetry helpers | — | health endpoints | — | — | No PII |

## Cross-cutting ownership

| Concern | Owner |
| --- | --- |
| Permission key definitions | Catalog 5 (not a code module) |
| Error code definitions | Catalog 2 |
| State machine definitions | Catalog 1 |
| Audit event name definitions | Catalog 3 |
| Notification name definitions | Catalog 6 |
| Job name definitions | Catalog 7 |
| Retention class definitions | Catalog 8 |
| Provider SDKs | MOD-LAYER-INT / MOD-LAYER-INFRA adapters only |
| Shared primitives | MOD-LAYER-SHARED |

## ISSUE-MOD-001 (entries split)

Until amended: draft mutations → MOD-DRAFTS; submit/finalize transcription transitions → MOD-TRANSCRIPTIONS; both coordinate via application ports on shared `intake_entries` with **single-writer rules per state** documented in future IS domain specs. Dual unrestricted writers are forbidden.
