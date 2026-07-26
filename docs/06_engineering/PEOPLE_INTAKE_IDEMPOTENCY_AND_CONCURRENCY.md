# People Intake — Idempotency and Concurrency

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-SECURITY-API-ENGINEERING-DESIGN-1.0

---

## Idempotency Required For

Batch creation · page creation · upload completion · page submission · match resolution · promotion request · person creation · attribute addition · image replacement

### Key Record (Conceptual)

```text
key, operation, actor, request fingerprint
status, result reference, created_at, expires_at
```

### Behavior

| Case | Result |
| --- | --- |
| Same key + same request | Return original result |
| Same key + different request | Reject as conflict (`IDEMPOTENCY_CONFLICT`) |

Scope by operation, authenticated user/trusted service, and target record where applicable.

---

## Optimistic Concurrency

Mutable records carry version (or equivalent). Writes include expected version. Mismatch → `STALE_WRITE`.

---

## Pessimistic Locking

Use for: claim next page · resolve match · create/promote person when duplicate risk exists.

### Claim-Next Sequence

1. Select eligible page (priority + age)  
2. Lock selection  
3. Confirm no active claim  
4. Create claim  
5. Update page state  
6. Commit  
7. Return page  

Two simultaneous users must not receive the same page.

### Match Review

One reviewer resolves an entry at a time.

### Admin Override

Invalidate prior claim version · preserve draft · record reason · prevent stale browser writes.

---

## State Transition Contract

No arbitrary status assignment. Every transition defines:

```text
Current state · Requested action · Allowed roles
Required conditions · Resulting state · Side effects
Audit event · Failure codes · Recovery path
```

Examples:

```text
READY_FOR_ENTRY + CLAIM_PAGE → CLAIMED_FOR_ENTRY
ENTRY_IN_PROGRESS + SUBMIT_PAGE → READY_FOR_MATCHING
NEEDS_ENTRY_CORRECTION + RESUBMIT_CORRECTION → READY_FOR_MATCHING
```

Invalid transitions rejected.

Machine registry: `contracts/schemas/state-transition-registry.json`
