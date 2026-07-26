# State Machine Catalog

**Library volume:** Engineering Catalogs  
**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-IMPLEMENTATION-LIBRARY-1.0  
**Implementation authorized:** No — specification only  
**Authority:** Implementation source of truth for this domain. Design volumes remain authoritative for product intent; this volume governs engineering precision. Conflicts → stop → Decision Log.

**Open decisions:** Where audit findings (OD-B*) remain unresolved, fields are marked `PENDING_FREEZE`. Do not invent policy to fill gaps.

---

## Rule

No state exists in code without a documented diagram and transition table here (or linked machine JSON under `contracts/schemas/`).

## Batch

```text
DRAFT → UPLOADING → READY → IN_PROGRESS → NEEDS_ATTENTION → COMPLETED → ARCHIVED
```

## Page

```text
UPLOADING → UPLOADED → IMAGE_REVIEW → READY_FOR_ENTRY → ASSIGNED → IN_PROGRESS
→ ENTRY_COMPLETE → MATCHING → NEEDS_MATCH_REVIEW → NEEDS_CORRECTION → COMPLETED → ARCHIVED
```

Exception branches: upload failure, unreadable, admin reopen/force-complete.

**PENDING_FREEZE:** Unify UX vs engineering vocabulary (audit F-C04).

## Entry

```text
DRAFT → TRANSCRIBED → MATCHING → EXACT_MATCH | POSSIBLE_MATCH | NO_MATCH | CONFLICT
→ LINKED_EXISTING | CREATED_NEW → COMPLETED
```

## Claim

```text
UNCLAIMED → CLAIMED/ACTIVE → EXPIRING_SOON → EXPIRED | RELEASED | REASSIGNED
```

## Promotion

```text
PENDING → SUCCEEDED | FAILED → (retry) PENDING
```

## Job

```text
PENDING → RUNNING → SUCCEEDED | FAILED | DEAD
```

## User

```text
INVITED → ACTIVE → DISABLED
```

## Diagrams

See also Volume 2 state machines mermaid and `contracts/schemas/*-state-machine.json` / `state-transition-registry.json`.

---

## Validation Before Coding

- [ ] Matches Volume 0 Constitution
- [ ] Matches frozen design volumes
- [ ] No `PENDING_FREEZE` leftovers for this slice (or Owner accepted)
- [ ] Corresponding DB / API / UI / package docs updated
- [ ] Tests planned in package exit criteria

## Cross-References

- Volume 2 State machines
- TECH_SPEC_* lifecycle sections
