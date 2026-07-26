# Canonical Platform Standards

**Library volume:** 13 — Canonical Platform Standards  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## Purpose

Define shared platform expectations for People Intake, RedDirt, Relationship Command Center, ContactListSOS, Arkansas Civic University, and future apps.

These standards extend Volume 0 Article II (Universal Engineering Constitution).

## 1. Canonical Person Standards

- Single canonical identity domain.  
- Apps contribute via controlled promotion / approved write APIs.  
- Apps consume via read contracts.  
- No silent merges; merge is an explicit privileged workflow.  
- Attributes carry provenance.

## 2. Shared Identity Standards

- External auth subjects map to per-app or shared identity records as designed.  
- Individual accounts; disablement honored across session validation.  
- Roles are app-scoped unless a shared permissions model is explicitly adopted.

## 3. Common Audit Model

- Append-only events with who/what/when/subject refs.  
- Redacted payloads; no secrets/signed URLs.  
- High-risk actions require durable audit.

## 4. Shared Attachment Model

- Private object storage; metadata in DB.  
- Temporary authorized access.  
- Originals preserved across replacements.

## 5. Shared Notification Model (future)

- Notifications are explicit product features, not side effects of random writes.  
- V1 People Intake does not send email/SMS.  
- Future shared notifier must be opt-in per app with audit.

## 6. Shared Organization Model (future)

- Organizations/tenants defined once if multi-org appears.  
- People Intake V1 may be single-org operationally; do not hard-code assumptions that block org_id later.

## 7. Shared Permissions Model

- Deny by default.  
- Server-side enforcement.  
- Matrix documented per app; shared verbs preferred (`read`, `write`, `admin`, `promote`).

## 8. Shared Event Model

- Past-tense catalog names (`PageClaimed`).  
- Stable event types; additive evolution.  
- Consumers must tolerate unknown future event types.

## 9. Shared API Conventions

- Versioned HTTP (`/api/v1`).  
- Standard envelope.  
- Idempotency keys on mutating critical paths.  
- Consistent error codes where domain-overlap exists.

## 10. Shared UI Conventions

- Plain language; recovery-first errors.  
- Accessibility baseline (keyboard, labels, non-color-only status).  
- Do not expose internal enum names to routine users.

## 11. Shared Testing Standards

- Authz denial tests mandatory.  
- Concurrency tests for claims/idempotency where applicable.  
- No production deploy without automated regression for critical paths.

## Adoption Rule

New apps should link this Volume 13 in their constitution/README and document deviations via Decision Log.

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 0 Article II
- Canonical person contracts
