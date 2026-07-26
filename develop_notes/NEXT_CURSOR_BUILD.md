# Next Cursor Build

## Primary

```text
PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0
```

Phase 3 (IS-300…305) documentation is complete. Focus: Critical ADR/issue remediation, design-freeze readiness, Gate G-10 evaluation inputs.

## Explicit non-goals

```text
Do NOT open Gate G-10 in this lane by implication.
Do NOT create migrations, SQL, Prisma, or application code.
Do NOT treat Phase 3 complete as implementation authorization.
```

## Standing locks

* Migration implements approved design — never creates it (IS-305)  
* Read models project truth / disposable (IS-304)  
* DB may enforce / must not invent (IS-303)  
* Relationships = governed business concepts (IS-302)  

## Mode

```text
DOCUMENTATION_AND_SPECIFICATION_ONLY
```

Gate G-10: **CLOSED**  
`migrationsAuthorized`: **false**
