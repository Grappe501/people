# People Intake — Entity Relationship Diagram (Conceptual)

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-DATA-MATCHING-STORAGE-DESIGN-1.0  
**Note:** Conceptual ERD. Final table/column names require shared-database audit.

---

## Hierarchy Diagram

```mermaid
erDiagram
  INTAKE_BATCH ||--o{ INTAKE_PAGE : contains
  INTAKE_PAGE ||--o| INTAKE_SOURCE_IMAGE : has_active_original
  INTAKE_PAGE ||--o{ INTAKE_IMAGE_VERSION : versions
  INTAKE_PAGE ||--o{ INTAKE_ENTRY : has
  INTAKE_PAGE ||--o| INTAKE_PAGE_CLAIM : active_claim
  INTAKE_ENTRY ||--o{ INTAKE_ENTRY_CORRECTION : corrections
  INTAKE_ENTRY ||--o{ INTAKE_MATCH_CANDIDATE : candidates
  INTAKE_ENTRY ||--o| INTAKE_MATCH_RESOLUTION : resolution
  INTAKE_MATCH_RESOLUTION ||--o| INTAKE_PROMOTION_REQUEST : promotes
  INTAKE_PROMOTION_REQUEST ||--o| INTAKE_PROMOTION_RESULT : result
  CANONICAL_PERSON ||--o{ PERSON_ATTRIBUTE : attributes
  PERSON_ATTRIBUTE ||--o{ PERSON_ATTRIBUTE_SOURCE : provenance
  INTAKE_PROMOTION_RESULT }o--|| CANONICAL_PERSON : links_or_creates
  INTAKE_ENTRY }o--o| CANONICAL_PERSON : matched_person
```

---

## Relationship Rules

| From | To | Cardinality | Notes |
| --- | --- | --- | --- |
| Batch | Page | 1:N | Page number unique in batch |
| Page | Entry | 1:0–10 | Blank rows create no entry |
| Page | Active original image | 1:0–1 | Replacement creates new version |
| Entry | Match candidates | 1:N | Ranked |
| Entry | Final resolution | 1:0–1 | One final resolution |
| Resolution | Promotion request | 1:0–1 | Per resolution version |
| Entry | Canonical person | N:0–1 | After successful promotion/link |
| Person | Attributes | 1:N | Multiple emails/phones allowed |
| Attribute | Provenance | 1:N | Mandatory for intake-originated |

---

## Boundary Crossing

People Intake never imports RedDirt code. Crossing into canonical domain occurs only through controlled promotion contracts.

```text
Intake Entry → Match Resolution → Promotion Request → Canonical Person Service → Person + Attributes + Provenance
```

---

## Diagram: Promotion Flow

```mermaid
flowchart LR
  A[Submitted Entry] --> B[Normalize]
  B --> C[Match Run]
  C --> D{Outcome}
  D -->|Exact / Human Link| E[Promotion LINK]
  D -->|No Match / Create| F[Promotion CREATE]
  D -->|Conflict / Possible| G[Human Review]
  G --> E
  G --> F
  G --> H[Return / Defer]
  E --> I[Canonical Domain]
  F --> I
```
