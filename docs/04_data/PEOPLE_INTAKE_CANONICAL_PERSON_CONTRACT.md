# People Intake — Canonical Person Contract

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-DATA-MATCHING-STORAGE-DESIGN-1.0  
**Integration model:** Controlled promotion (locked)

---

## Purpose

Define how People Intake relates to the shared canonical people domain without importing RedDirt application code.

---

## Separation

| Concept | Role |
| --- | --- |
| Intake Entry | Historical source event / transcription |
| Canonical Person | Best current durable identity |
| Person Attribute | Provenance-aware value (possibly multiple per type) |

---

## Canonical Person Core (Minimal)

```text
id
display_first_name
display_last_name
status
created_at
updated_at
merged_into_person_id
archived_at
```

### Person status

```text
ACTIVE | INACTIVE | DUPLICATE | MERGED | ARCHIVED | RESTRICTED
```

---

## Person Attributes

Categories:

```text
NAME | EMAIL | PHONE | ZIP | VOLUNTEER_PREFERENCE | EMAIL_LIST_PREFERENCE
```

Each attribute supports (conceptual):

```text
id, person_id, attribute_type
value_raw, value_normalized
status, is_primary, confidence
source_type, source_reference_id
effective_at, verified_at
created_at, updated_at, retired_at
```

### Why not flat overwrites

A person may have multiple emails/phones, shared household contacts, old and new ZIPs, multiple preference sources, nicknames. New intake must not destroy older valid information.

### Contact sharing flags

```text
PERSONAL | HOUSEHOLD_SHARED | ORGANIZATIONAL | UNKNOWN
```

---

## Controlled Promotion Model

People Intake owns intake-domain records and creates **promotion requests** after match resolution.

Canonical people service performs:

```text
Create new person
Link existing person
Add person attribute
Retire person attribute
Mark attribute primary
Reject conflicting update
```

### Why Model B (promotion) over direct writes

Stronger isolation, easier rollback, safer testing, clearer accountability, lower risk to RedDirt — at the cost of more moving parts and monitoring.

---

## Contract Must Eventually Define

- Stable person ID
- Supported attribute types
- Multiple-value rules
- Primary-value rules
- Provenance requirements
- Update permissions
- Conflict behavior
- Merge boundaries
- Archive behavior
- Cross-application access
- Retry + idempotency

Integration via shared DB contract, shared service contract, versioned API, or approved repository boundary — **never cross-project source imports**.

---

## New Person Creation Gates

Allowed only after:

1. Entry submitted  
2. Normalization complete  
3. Candidate search complete  
4. No acceptable existing person selected  
5. Approved review rule passes  

Must retain provenance to batch, page, entry, image, uploader, transcriber, reviewer/rule, timestamp.

---

## Attribute Update Rules (on link)

| Case | Behavior |
| --- | --- |
| Same normalized value | Confirm source / add provenance; avoid unnecessary duplicates |
| New additional value | May add additional (e.g., second phone); do not auto-delete existing |
| Conflicting value | Keep Existing / Add Additional / Mark Primary / Reject / Defer |
| Preferences | Time-aware; preserve prior; Unknown must not supersede known Yes/No; explicit Yes/No may supersede older per final business rules |

---

## Merge Boundary

Person-to-person merge is **outside** routine intake. Intake may link, create, or flag probable duplicates. It must **not** automatically merge two canonical people.

People Intake must not directly delete canonical people.

---

## Deferred Exact Details

- Exact existing table names after RedDirt/shared audit  
- Exact primary-value rules  
- Exact consent supersession rules  
- Exact merge workflow  
- Exact auto-create vs review for NO_MATCH  

---

## Acceptance Implications

- Shared phone does not force merge  
- Unknown consent does not overwrite Yes/No  
- New phone does not auto-delete old phone  
- Every intake-originated canonical attribute has provenance  
- RedDirt remains operational if People Intake is unavailable  
