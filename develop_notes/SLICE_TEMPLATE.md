# Slice Template (Copy Per Implementation Slice)

Use after Gate G-10. Paste into develop note or PR body.

```markdown
## Objective

## Scope

## Out of Scope

## Files Expected

## Validation Commands

```powershell
$env:TEMP="H:\people\.tmp"
$env:TMP="H:\people\.tmp"
$env:TMPDIR="H:\people\.tmp"
$env:npm_config_cache="H:\people\.npm-cache"
npm run drive:validate
# then lint / typecheck / test as established in Phase 0
```

## Manual Tests

## Rollback Plan

## Documentation Updates

## Exit Criteria
```
