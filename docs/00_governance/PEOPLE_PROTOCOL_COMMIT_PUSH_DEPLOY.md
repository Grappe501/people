# Standing Commit / Push / Deploy Protocol

**Document ID:** `PEOPLE-PROTOCOL-COMMIT-PUSH-DEPLOY-1.0`  
**Status:** APPROVED STANDING ORDER  
**Decision:** D-065  
**Project root:** `H:\people`  
**Applies to:** Every Burt (Cursor) return after a completed, validated documentation or implementation slice

---

## Distinction

```text
COMMIT AND PUSH
  Required after every completed, validated interaction

NETLIFY DEPLOY
  Required after every interaction once a deployable authorized surface exists

APPLICATION CODE
  Not authorized until Gate G-10 / explicit authorization
```

Documentation-first does **not** mean local-only work. Repository discipline remains mandatory.

---

## Closeout sequence (mandatory)

```text
Write documentation (or authorized implementation)
→ validate
→ update indexes / registers / RTM
→ generate / update completion report
→ commit
→ push to GitHub
→ verify remote commit
→ deploy only when a meaningful authorized Netlify surface exists
```

---

## Standing rules

1. Run all required validators.  
2. Confirm no forbidden implementation artifacts were created (while application code is not authorized).  
3. Update governance records and the completion report.  
4. Commit the complete slice with the governing work-item ID.  
5. Push to the canonical GitHub branch (`master` / approved branch).  
6. Report the commit hash and remote branch.  
7. Verify the remote contains the commit.  
8. Trigger and verify Netlify deployment when a deployable authorized surface exists.  
9. Never treat a local-only change as completed.  
10. Never deploy unauthorized application behavior.  
11. Never invent application code merely to force a Netlify deployment.  

---

## Commit message pattern

```text
docs(<work-item-id-kebab>): <short why>
```

Examples:

```text
docs(people-is-102): approve module boundary architectural rulebook
docs(people-is-103): complete environment architecture specification
```

---

## Required completion evidence

```text
Work item:
<PEOPLE-…-1.0>

Validation:
governance:validate — PASS | FAIL
docs:catalogs:validate — PASS | FAIL | N/A

Forbidden implementation artifacts:
NONE | <list>

Commit:
<full hash>

Branch:
<canonical branch>

Push:
PASS | FAIL

Remote verification:
PASS | FAIL

Netlify:
DEPLOYED AND VERIFIED
or
NOT APPLICABLE — no authorized deployable surface exists

Application implementation:
NOT AUTHORIZED | AUTHORIZED FOR <scope>
```

---

## Netlify applicability (current)

- `.netlify/` local state alone is **not** an authorized deployable documentation site.  
- Absent `netlify.toml` / approved static docs site / authorized app surface → report **NOT APPLICABLE**.  
- When PEOPLE-IS-105 / a docs site package authorizes a deployable surface, Netlify verify becomes mandatory after each push.

---

## Relationship to Cursor Execution Protocol

This standing order extends `docs/08_implementation/PEOPLE_INTAKE_CURSOR_EXECUTION_PROTOCOL.md` End-of-Run requirements. Local-only “done” claims without commit/push/remote verification are **invalid**.
