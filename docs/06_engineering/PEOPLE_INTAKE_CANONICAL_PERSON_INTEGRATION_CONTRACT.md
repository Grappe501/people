# People Intake — Canonical Person Integration Contract

**Status:** draft_complete  
**Version:** 1.0  
**Contract version intent:** `canonical-people-contract/v1`  
**Build:** PEOPLE-SECURITY-API-ENGINEERING-DESIGN-1.0

---

## Boundary

People Intake communicates with the canonical people domain through a **versioned controlled contract**.

Breaking changes require a new contract version.

No RedDirt source imports. No writes to RedDirt operational tables.

Preferred transports (choose later): stored procedure · dedicated service · restricted DB function · versioned internal API. Avoid unrestricted direct writes to all canonical tables.

---

## Conceptual Operations

```text
findCandidates
getPersonSummary
createPersonFromIntake
linkIntakeToPerson
addPersonAttribute
recordPreference
attachProvenance
checkIdempotency
getPromotionResult
```

---

## Promotion Request (Required Fields)

```text
promotionRequestId
idempotencyKey
intakeEntryId
resolutionType
targetPersonId
approvedAttributes
rejectedAttributes
preferenceEvents
provenance
requestedBy
requestedAt
contractVersion
```

---

## Promotion Response (Required Fields)

```text
promotionRequestId
status
personId
createdAttributeIds
existingAttributeIds
rejectedUpdates
warnings
completedAt
contractVersion
```

---

## Failure Isolation

If promotion fails:

- Intake resolution remains preserved  
- Entry → promotion pending/failed  
- Page does **not** falsely become completed  
- Retry is safe  
- RedDirt unaffected  
- Operator sees actionable status  

Browsers do not call raw canonical mutation endpoints; they go through match resolution → promotion request services.

Machine schemas: existing `promotion-request.schema.json` / `promotion-result.schema.json` plus this contract doc.
