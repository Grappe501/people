# People Intake — Service Contracts

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-SECURITY-API-ENGINEERING-DESIGN-1.0

---

## Authentication Service

Resolve session/user; confirm account status; provide trusted user context.

## Authorization Service

Evaluate action + record scope + state; produce denial codes; support audit.

## Batch Service

Create/update allowed metadata; progress; complete upload; archive/reopen under authz.

## Upload Service

Validate intent; safe storage key; signed upload; confirm; metadata verify; derivative jobs; hash duplicate detect; replacement.

## Page Queue Service

Next page by priority/age; atomic claim; renew; release; expire; reassign.

## Draft Service

Save/retrieve draft; validate claim + version; reconciliation metadata.

## Transcription Service

Validate ≤10 entries; preserve raw; normalize; submit transactionally; audit; schedule matching.

## Matching Service

Search/rank/explain; versioned rules; conflicts; review work; **never merge people**.

## Match Review Service

Claim review item; validate authority; save resolution; promotion request; return correction; defer.

## Promotion Service

Canonical contract calls; recheck identity; create/link; attributes; provenance; result; safe retry; prevent duplicates.

## Image Access Service

Authorize; signed URL or stream; hide storage implementation; audit when required.

## Audit Service

Append-only events; sanitize metadata; authorized search; prevent routine mutation.

## Error and Recovery Service

Record retryable failures; classify severity; schedule retry; operator action; resolve incidents.

---

## Machine Registry

`contracts/schemas/service-registry.json`
