# People Intake — Migration and Rollback

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-DATA-MATCHING-STORAGE-DESIGN-1.0  
**Migrations authorized:** No

---

## Stance

No migration is authorized in this step.

Future migrations must be:

```text
Additive
Versioned
Reversible where practical
Tested in nonproduction
Backed up
Validated against RedDirt
Separated by domain
```

---

## Pre-Migration Audit (Required)

Before writing migration files:

1. Inspect existing RedDirt and shared-person schemas  
2. Identify current people tables  
3. Identify duplicate contact structures  
4. Identify current IDs and foreign keys  
5. Identify existing consent fields  
6. Identify existing audit patterns  
7. Identify current Postgres extensions  
8. Identify Netlify and hosted-database requirements  
9. Identify schema ownership  
10. Produce a compatibility report  

**No assumed schema.** Conceptual tables in design docs are not proof of existence.

---

## Rollback Package Requirements

Every future migration package must include:

- Forward migration  
- Validation query  
- Backfill plan  
- Rollback or compensating migration  
- Data-preservation plan  
- RedDirt impact statement  
- Downtime assessment  
- Operator gate  

Destructive rollback must not discard intake evidence.

---

## Archive / Soft Delete / Permanent Delete

| Mode | Intent |
| --- | --- |
| Archive | Hide from routine queues; preserve history |
| Soft delete | Unavailable without immediate physical removal |
| Permanent delete | Restricted; retention + authorization; soft-delete first where practical |

People Intake must not directly permanently delete canonical people.

---

## Seed and Test Data

Nonproduction data must be synthetic — never real volunteer sheets as public fixtures.

Synthetic coverage should include: exact email/phone match, household shared contacts, similar names, no contact, unreadable fields, ten-entry page, duplicate image, correction history, new person, conflicting ZIP.

---

## Data Architecture Acceptance Tests

1. One page can contain ten unique entries  
2. Each entry remains independently traceable  
3. One entry may link to an existing person  
4. Another entry on the same page may create a new person  
5. Shared phone does not force a merge  
6. Unknown consent does not overwrite Yes or No  
7. A correction does not erase the original transcription  
8. A new phone does not automatically delete an old phone  
9. Image replacement preserves version history  
10. Duplicate submission does not create duplicate people  
11. Failed promotion can be retried safely  
12. Exact image duplicate can be detected  
13. Every canonical attribute has provenance  
14. Deleted image does not erase audit history  
15. RedDirt remains operational if People Intake is unavailable  
