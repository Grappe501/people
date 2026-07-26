# People Intake — Data Design Validation Checklist

**Build:** PEOPLE-DATA-MATCHING-STORAGE-DESIGN-1.0

- [x] Domain hierarchy final (Batch → Page → Entry → Match → Person)
- [x] Intake vs canonical separation defined
- [x] Raw vs normalized rules defined
- [x] Field-condition semantics final
- [x] Consent semantics final (YES/NO/UNKNOWN)
- [x] Canonical-person architecture defined
- [x] Controlled promotion selected
- [x] Matching philosophy + signals + tiers defined
- [x] Household contact protection defined
- [x] Provenance mandatory
- [x] Audit structure defined
- [x] Source-image architecture defined
- [x] Private temporary access defined
- [x] Image replace/delete defined
- [x] Retention states defined
- [x] DB ownership boundaries defined
- [x] Transaction + idempotency needs defined
- [x] Migration/rollback principles defined
- [x] Deferred items explicitly listed
- [x] No schema, migration, or application code written

Machine validators: see `PEOPLE_GOVERNANCE_VALIDATION_REPORT.md` and `PEOPLE_H_DRIVE_VALIDATION_REPORT.md`.
