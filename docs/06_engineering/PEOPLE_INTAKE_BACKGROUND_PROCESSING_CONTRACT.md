# People Intake — Background Processing Contract

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-SECURITY-API-ENGINEERING-DESIGN-1.0

---

## Candidate Background Operations

- Image derivative creation  
- Image hash validation  
- Matching candidate generation  
- Promotion execution  
- Retry processing  
- Orphan-storage cleanup  
- Claim expiration  
- Retention evaluation  

Exact worker hosting deferred.

---

## Job Record (Conceptual)

```text
id, job_type, target_type, target_id
status, attempt_count, max_attempts, next_attempt_at
locked_by, locked_at, last_error_code
created_at, updated_at, completed_at
```

### Status

```text
PENDING | RUNNING | RETRY_WAIT | SUCCEEDED | FAILED | CANCELLED
```

### Requirements

Idempotent · retryable · lockable · observable · audited when sensitive · safe after restart.

---

## Completeness Rule

A page must **not** appear complete while required promotion work remains pending.

---

## Worker Security

- Authenticate to required services  
- Least-privilege credentials  
- Lock jobs  
- Sanitize errors  
- No PII in logs  
- Respect idempotency and environment boundaries  
- Audit sensitive promotion outcomes  

Machine schema: `contracts/schemas/background-job.schema.json`
