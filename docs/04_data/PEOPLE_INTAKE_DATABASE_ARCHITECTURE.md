# People Intake — Database Architecture

> **SUPERSEDED AS CANONICAL PERSISTENCE ARCHITECTURE — D-072 / AUDIT-SLICE-003**  
> **Canonical persistence architecture:** `docs/implementation_specs/300_database/PEOPLE-IS-300-DATABASE-ARCHITECTURE.md`.  
> **Domain/entity/field authority:** IS-200 / IS-201 / IS-202.  
> This file remains a **historical conceptual companion**. Table lists here are seeds only — not proof of existence in any shared database. No migrations authorized.

**Status:** draft_complete — **SUPERSEDED (canonical → IS-300)**  
**Version:** 1.0  
**Build:** PEOPLE-DATA-MATCHING-STORAGE-DESIGN-1.0  
**Schema authorized:** No — conceptual only until shared DB audit + Gate G-10 / migrationsAuthorized

---

## Purpose

Define conceptual ownership, table groups, uniqueness, indexing intent, transactions, idempotency, and concurrency for the intake and promotion domains — without writing migrations or Prisma models.

---

## Critical Constraint

> Do not assume any previously discussed conceptual table already exists. The actual shared database must be audited before migrations.

---

## Conceptual Table Groups

### Intake Core

```text
intake_batches
intake_pages
intake_entries
intake_entry_corrections
```

### Queue and Claims

```text
intake_page_claims
intake_page_status_history
```

### Storage

```text
intake_source_images
intake_upload_attempts
intake_image_versions
```

### Matching

```text
intake_match_runs
intake_match_candidates
intake_match_resolutions
```

### Promotion

```text
intake_promotion_requests
intake_promotion_results
```

### Audit and Errors

```text
intake_audit_events
intake_processing_errors
```

### Shared Canonical (names TBD after audit)

```text
people / person_* structures
person preferences / attribute sources
person_merge_history
```

---

## Identifier Design

- UUID (or equivalent) for internal identity
- Human-readable codes for operations (e.g., `PI-2026-0728-00041-P03-R07`)
- Never use email, phone, or name+ZIP as primary key
- Avoid sequential public IDs that expose volume

---

## Uniqueness (Conceptual)

- Page number unique within batch
- Row number unique within page
- One active claim per page
- One final resolution per intake entry
- One active original image version per page
- One active promotion request per resolution version
- Idempotency key unique within operation scope
- Canonical emails/phones are **not** globally unique (household sharing)

---

## Indexing Intent

| Domain | Index targets |
| --- | --- |
| Queue | page status, priority, created time, batch sequence, active claim |
| Matching | normalized email/phone/names/ZIP, match status, candidate person ID |
| Audit | batch, page, entry, person, actor, event type, date |
| Storage | page ID, hash, upload status, storage key |
| Promotion | entry, resolution, status, idempotency key |

Exact indexes after query-plan review (deferred).

---

## Transaction Boundaries

Must be transactional in future implementation:

1. **Submit page** — verify claim, lock version, save entries/conditions, set status, audit, release claim, schedule matching  
2. **Resolve match** — authz, save resolution, candidate status, promotion request, entry status, audit  
3. **Promote new person** — create person/attributes/provenance, promotion result, link entry, audit  
4. **Link existing** — confirm person, provenance, add/reject attributes, promotion result, link, audit  
5. **Replace image** — metadata, version switch, retire prior, page status, audit  

Object storage + Postgres cannot share one DB transaction — require compensation logic.

---

## Idempotency Required For

Batch creation, page registration, image upload completion, page submission, matching-run creation, match resolution, person creation, person linkage, attribute promotion, audit-event creation.

Repeated requests return prior success; no duplicates.

---

## Concurrency

- Atomic page claim
- Optimistic version checks
- Claim expiration
- Draft ownership
- Admin reassignment
- Stale-write rejection
- Match-resolution locking
- Promotion locking
- Duplicate-person creation prevention

No workflow may rely solely on front-end state.

---

## Ownership Summary

| Domain | Owner |
| --- | --- |
| Intake tables | People Intake |
| Canonical people | Shared canonical domain |
| RedDirt operational tables | RedDirt (no People Intake writes) |

---

## Migration Stance

Additive, versioned, reversible where practical, nonproduction-tested, backed up, RedDirt-validated, domain-separated. No migration in this build. See `PEOPLE_INTAKE_MIGRATION_AND_ROLLBACK.md`.
