# Requirement Traceability Matrix

**Status:** Phase 0 VERIFIED; IS-100 design-mapped; Catalog 09 foundation seeds TRACE-SEED-001…010; system-wide inventory PARTIAL (amendment-driven)  
**Program:** PEOPLE-IMPLEMENTATION-SPECIFICATION-PROGRAM-1.0

| Requirement ID | Requirement | Source | Entity | Service | API | UI | Job | Permission | State | Error | Audit | Notification | Test | Package | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-GOV-001 | Documentation must precede implementation | IS-000 / Master Program | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Phase 0 review | PKG-0.0 | VERIFIED |
| REQ-GOV-002 | Every specification must use the canonical template | IS-001 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Structural validation | PKG-0.0 | VERIFIED |
| REQ-GOV-003 | Every requirement must have a stable ID | IS-002 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Identifier audit | PKG-0.0 | VERIFIED |
| REQ-GOV-004 | Every implementation-ready requirement must be traceable | IS-003 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Matrix review | PKG-0.0 | VERIFIED |
| REQ-GOV-005 | Blocking decisions must remain visible | IS-004 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Register review | PKG-0.0 | VERIFIED |
| REQ-GOV-006 | Readiness requires objective evidence | IS-005 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Gate review | PKG-0.0 | VERIFIED |
| REQ-GOV-007 | All project work must remain under H:\people | IS-000 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Boundary review | PKG-0.0 | VERIFIED |
| REQ-GOV-008 | Nothing may intentionally write to C:\ | IS-000 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Boundary review | PKG-0.0 | VERIFIED |
| REQ-GOV-009 | Approval does not automatically authorize implementation | IS-000 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Governance review | PKG-0.0 | VERIFIED |
| REQ-GOV-010 | Production secrets must not appear in documentation | IS-000 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Security review | PKG-0.0 | VERIFIED |

| REQ-REPO-001 | All project-controlled artifacts under H:\people | IS-100 / IS-000 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | INVALID_PROJECT_ROOT | N/A | N/A | Root validation test | Future PKG | FULLY_MAPPED |
| REQ-REPO-002 | No intentional C:\ targets in project scripts/config | IS-100 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | FORBIDDEN_WRITE_TARGET | N/A | N/A | Forbidden-target test | Future PKG | FULLY_MAPPED |
| REQ-REPO-003 | Governing docs separate from executable implementation | IS-100 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Index audit | Docs | FULLY_MAPPED |
| REQ-REPO-004 | Each top-level directory has purpose and owner | IS-100 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | UNAPPROVED_TOP_LEVEL_DIRECTORY | N/A | N/A | Ownership validation | Docs | FULLY_MAPPED |
| REQ-REPO-005 | Dependencies follow Presentation→Application→Domain | IS-100 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | FORBIDDEN_DEPENDENCY | N/A | N/A | Import-boundary tests | Future PKG | FULLY_MAPPED |
| REQ-REPO-006 | Modules expose public interfaces only | IS-100 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Deep-import test | Future PKG | FULLY_MAPPED |
| REQ-REPO-007 | Providers behind adapters | IS-100 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Provider replacement test | Future PKG | FULLY_MAPPED |
| REQ-REPO-008 | No real production personal data in Git | IS-100 / Catalog 8 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | SENSITIVE_FILE_DETECTED | N/A | N/A | Sensitive-file scan | Future PKG | FULLY_MAPPED |
| REQ-REPO-009 | No secrets in Git or documentation | IS-100 / Catalog 4&8 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | SECRET_DETECTED | N/A | N/A | Secret scan | Future PKG | FULLY_MAPPED |
| REQ-REPO-010 | Temporary artifacts use approved H-drive paths | IS-100 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | File-location test | Future PKG | FULLY_MAPPED |
| REQ-REPO-011 | Generated artifacts distinguishable from canonical | IS-100 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | GENERATED_FILE_MODIFIED | N/A | N/A | Generated-artifact audit | Future PKG | FULLY_MAPPED |
| REQ-REPO-012 | Migrations in database/migrations with package ID | IS-100 / future IS-305 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Migration validation | Future PKG | PARTIALLY_MAPPED |
| REQ-REPO-013 | System tests use approved test directories | IS-100 / future IS-1100 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Test-path validation | Future PKG | PARTIALLY_MAPPED |
| REQ-REPO-014 | Preview/staging/production distinguishable | IS-100 / future IS-1200 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Environment-separation review | Future PKG | PARTIALLY_MAPPED |
| REQ-REPO-015 | Canonical START_HERE orientation document | IS-100 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | MISSING_DOCUMENT_INDEX | N/A | N/A | Orientation review | Docs | FULLY_MAPPED |
| REQ-REPO-016 | Automated architectural violation checks | IS-100 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Repository-health gate | Future PKG | PARTIALLY_MAPPED |

| REQ-MOD-001 | Every business capability has exactly one owning module | IS-102 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | OWNERSHIP_CONFLICT | N/A | N/A | Ownership matrix review | Future PKG | FULLY_MAPPED |
| REQ-MOD-003 | Dependencies follow approved layer and module direction | IS-102 / IS-100 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | FORBIDDEN_DEPENDENCY | N/A | N/A | Import-boundary tests | Future PKG | FULLY_MAPPED |
| REQ-MOD-005 | UI must not bypass application services | IS-102 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | UI_BYPASS_SERVICE | N/A | N/A | Boundary validation | Future PKG | FULLY_MAPPED |
| REQ-MOD-008 | Each API endpoint belongs to exactly one module | IS-102 | N/A | N/A | API-* | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Ownership matrix | Future PKG | FULLY_MAPPED |
| REQ-MOD-009 | Each durable entity/table has exactly one owner | IS-102 | ENTITY-* | N/A | N/A | N/A | N/A | N/A | N/A | FOREIGN_TABLE_WRITE | N/A | N/A | Ownership matrix | Future PKG | FULLY_MAPPED |

| REQ-HDRIVE-001 | Canonical project root is H:\people | IS-104 / IS-100 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | INVALID_PROJECT_ROOT | N/A | N/A | drive:validate | Future guard PKG | FULLY_MAPPED |
| REQ-HDRIVE-003 | No intentional project-controlled writes to C:\ | IS-104 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | FORBIDDEN_WRITE_TARGET | N/A | N/A | drive:validate | Future guard PKG | FULLY_MAPPED |
| REQ-HDRIVE-010 | Unavoidable external C:\ writes distinguished from violations | IS-104 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Boundary review | Docs | FULLY_MAPPED |

| REQ-GHN-001 | Single governing GitHub repository | IS-105 / IS-100 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Remote topology review | Docs | FULLY_MAPPED |
| REQ-GHN-003 | Canonical integration branch Decision-Log recognized | IS-105 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Branch policy review | Docs | FULLY_MAPPED |
| REQ-GHN-009 | Dedicated Netlify site; no unrelated secret inheritance | IS-105 / D-018 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Hosting boundary review | Future deploy PKG | FULLY_MAPPED |
| REQ-GHN-011 | Preview success must not authorize Production | IS-105 / IS-103 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Promotion review | Future deploy PKG | FULLY_MAPPED |
| REQ-GHN-013 | Every authorized deploy records provenance | IS-105 / IS-103 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Deploy evidence review | Future deploy PKG | FULLY_MAPPED |
| REQ-GHN-016 | Netlify N/A until authorized deployable surface | IS-105 / D-065 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Closeout review | Docs | FULLY_MAPPED |
| REQ-GHN-017 | Burt executes closeout within governance | IS-105 / D-065 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Protocol review | Docs | FULLY_MAPPED |

| REQ-DOM-001 | Distinguishable data layers preserved | IS-200 / D-030 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Domain review | Future PKG | FULLY_MAPPED |
| REQ-DOM-002 | Batch/Page/Entry/Canonical Person separate | IS-200 / D-029 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Domain review | Future PKG | FULLY_MAPPED |
| REQ-DOM-004 | Exactly one owning module per concept | IS-200 / IS-102 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | OWNERSHIP_CONFLICT | N/A | N/A | Ownership matrix | Future PKG | FULLY_MAPPED |
| REQ-DOM-006 | Catalog 01 is state authority | IS-200 / Cat 01 | N/A | N/A | N/A | N/A | N/A | N/A | STATE-* | N/A | N/A | N/A | State review | Future PKG | FULLY_MAPPED |
| REQ-DOM-011 | Match Resolution ≠ Promotion | IS-200 / Vol 8 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Boundary review | Future PKG | FULLY_MAPPED |
| REQ-DOM-014 | Canonical identity outside intake ownership | IS-200 / D-032 | Canonical Person | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Integration review | Future PKG | FULLY_MAPPED |
| REQ-DOM-019 | Packages cite owning domain concept before code | IS-200 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Package gate | Future PKG | FULLY_MAPPED |

| REQ-ENT-001 | Every admitted entity has complete questionnaire card | IS-201 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Entity encyclopedia review | Docs | FULLY_MAPPED |
| REQ-ENT-002 | Lifecycles cite Catalog 01 only | IS-201 / Cat 01 | N/A | N/A | N/A | N/A | N/A | N/A | STATE-* | N/A | N/A | N/A | State review | Future PKG | FULLY_MAPPED |
| REQ-ENT-003 | Match Resolution must not write canonical persons | IS-201 / IS-200 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Boundary tests | Future PKG | FULLY_MAPPED |
| REQ-ENT-004 | Promotion must not redefine match outcomes | IS-201 / IS-200 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Boundary tests | Future PKG | FULLY_MAPPED |
| REQ-ENT-005 | New entities require IS/ADR amendment | IS-201 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Admission gate | Docs | FULLY_MAPPED |

Do not invent catalog keys to fill future rows. Use `PENDING` or `NOT_APPLICABLE` with rationale. Catalog Library is locked at 0–9.
