# Module Boundary Validation Rules

**Governed by:** PEOPLE-IS-102-MODULE-BOUNDARY-SPECIFICATION-1.0  
**Use:** Package review checklist now; automated `tools` later (not authorized yet).

## Hard fail rules

| Rule ID | Check | On failure |
| --- | --- | --- |
| VAL-MOD-001 | Import graph contains cycle across modules | REJECT |
| VAL-MOD-002 | Any import path contains another module’s `internal/` | REJECT |
| VAL-MOD-003 | `presentation` imports `infrastructure` repositories or DB client | REJECT |
| VAL-MOD-004 | `presentation` imports provider SDK / `integrations` clients | REJECT |
| VAL-MOD-005 | `domain` imports infrastructure, integrations, presentation, or workers | REJECT |
| VAL-MOD-006 | `workers` contain domain business rules beyond mapping to application calls | REJECT |
| VAL-MOD-007 | SQL/repository write targets a table not owned by the writing module | REJECT |
| VAL-MOD-008 | New `API-*` lacks owning module in ownership matrix | REJECT |
| VAL-MOD-009 | New entity/table lacks owning module | REJECT |
| VAL-MOD-010 | `shared` contains capability-specific business rules | REJECT |
| VAL-MOD-011 | Capability publishes event owned by another capability | REJECT |
| VAL-MOD-012 | Permission check invented outside Catalog 5 keys | REJECT |
| VAL-MOD-013 | Production error code not in Catalog 2 | REJECT |
| VAL-MOD-014 | Implementation package cites module not in IS-102 inventory | REJECT |
| VAL-MOD-015 | Dependency edge used but not ALLOW/P in dependency matrix | REJECT |

## Review evidence required per package

1. Owning module ID  
2. Allowed callers list  
3. Forbidden paths touched (must be none)  
4. Contracts added/changed  
5. Tests owned/mapped  
6. Traceability rows updated  

## Recommended future automation

`tools/repository_guard` / module boundary linter — authorized only by a later implementation package after ADR-020 / tooling ADRs.
