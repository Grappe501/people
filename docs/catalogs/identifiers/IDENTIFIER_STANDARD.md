# Identifier Standard

**Catalog:** Identifiers  
**Script:** PEOPLE-DOC-FOUNDATION-AND-INVENTORY-1.0  
**Status:** DRAFT foundation (expand in later DOC scripts)

---

## Purpose

Define stable, human-readable identifier families for documentation and specification registries. These identifiers are **not** database primary keys.

## Rules

1. Identifiers are stable once published.  
2. Unique within their registry.  
3. Never reused after retirement.  
4. Independent from UUID/database keys.  
5. Prefer `PEOPLE-` prefix for People Intake controlled registries.

## Families

| Pattern | Use |
| --- | --- |
| `PEOPLE-DOC-####` | Document inventory |
| `PEOPLE-DEC-####` / `OD-B##` / `D-###` | Decisions (legacy D-/OD- IDs remain valid) |
| `PEOPLE-CON-####` / `X-##` | Contradictions (legacy X- IDs remain valid) |
| `PEOPLE-RISK-####` / `R-###` | Risks |
| `PEOPLE-RULE-####` | Domain business rules (Volume 8) |
| `PEOPLE-INV-####` | Invariants (Volume 8) |
| `PEOPLE-ERR-####` | Error catalog entries |
| `PEOPLE-AUDIT-####` | Audit event catalog entries |
| `PEOPLE-SM-####` | State machines |
| `PEOPLE-API-####` | API endpoint specs |
| `PEOPLE-UI-####` | UI screen specs |
| `PEOPLE-COMP-####` | Component specs |
| `PEOPLE-PACKAGE-####` / `PEOPLE-PHASE-##-PACKAGE-##` | Implementation packages |
| `PEOPLE-TERM-####` | Terminology entries |

Exact domain patterns may expand in Volumes 8–13 without breaking this foundation.

## Mapping note

Audit registers currently use `OD-B##`, `X-##`, `F-C##`, `D-###`. Those remain authoritative until a controlled migration maps them to `PEOPLE-*` forms. Do not renumber silently.
