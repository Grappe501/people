# People Intake — Matching Engine Spec

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-DATA-MATCHING-STORAGE-DESIGN-1.0

---

## Philosophy

Matching must be conservative, explainable, repeatable, provenance-aware, human-reviewable, and resistant to household false positives.

> A false duplicate is more dangerous than a temporary duplicate.

Matching occurs **after** transcription. It must not interrupt typing.

---

## Pipeline

```text
Submitted entry
→ Normalize
→ Search candidates
→ Rank + explain
→ Assign confidence tier
→ Auto-prepare exact/no-match paths per approved rules
→ Human review for possible/conflict/high-confidence (unless later authorized)
→ Match resolution
→ Promotion request
```

---

## Signal Classes

### Strong

- Exact normalized email  
- Exact normalized phone + compatible name  
- Exact email + compatible last name  
- Exact phone + matching ZIP + compatible name  

### Moderate

- Exact first + last + ZIP  
- Similar first + exact last + phone  
- Exact last + email similarity  
- Exact name + prior source relationship  

### Weak (never auto-link)

- Same last name only  
- Same ZIP only  
- Same first name only  
- Name similarity without contact match  
- Shared event/county only  

### Negative / conflict

- Different strong emails  
- Different strong phones  
- Substantially different full names  
- Known shared household contact  
- Multiple equally strong candidates  
- Conflicting person history  

---

## Confidence Tiers

```text
EXACT
HIGH_CONFIDENCE
POSSIBLE
LOW_CONFIDENCE
NO_MATCH
CONFLICT
```

| Tier | Meaning |
| --- | --- |
| EXACT | Meets approved deterministic rule |
| HIGH_CONFIDENCE | Strong but review unless later authorized |
| POSSIBLE | Human should compare |
| LOW_CONFIDENCE | Context only; not recommended as likely |
| NO_MATCH | No reasonable candidate |
| CONFLICT | Incompatible directions |

---

## Automatic Boundaries

**May:** normalize, search, rank, explain, detect exact deterministic matches, mark no-candidate, create review tasks, prepare promotion requests.

**Must not:** merge people, link ambiguous household phones, link shared emails without corroboration, replace conflicting canonical values, delete existing values, promote unreadable data, treat name similarity alone as identity.

---

## Exact Match Rules (Versioned)

Each rule:

```text
rule_id, version, description
required_signals, disqualifying_signals
resolution_action, human_review_required, effective_date
```

### Potential initial rules

**E-1:** Exact normalized email + compatible first or last name + no conflicting identity signal  

**E-2:** Exact normalized phone + exact last name + compatible first name + no known shared-phone flag  

**E-3:** Exact normalized email and phone + no conflicting identity signal  

Final auto-link authorization deferred to security/engineering design.

---

## Household Contact Protection

Attributes may be marked PERSONAL / HOUSEHOLD_SHARED / ORGANIZATIONAL / UNKNOWN.

When shared: cannot independently establish identity; may support discovery; reviewer needs additional evidence.

---

## Same-Page Duplicates

Warn on same email/phone or same name+ZIP twice on one page. Operator: Keep Both / Edit / Remove. Never silent remove.

---

## Cross-Batch Duplicate Images

SHA-256 (or equivalent) content hash. Detect exact duplicates across batches. User/admin decides keep. Perceptual duplicates not required in V1.

---

## Match Candidate Record

```text
id, intake_entry_id, candidate_person_id
rank, confidence_tier, score, match_rule_version
positive_signals, negative_signals, conflicting_fields
explanation, status, created_at, resolved_at
```

Candidate status: SUGGESTED, SELECTED, REJECTED, SUPERSEDED, EXPIRED  

Score is a ranking aid, not identity truth — always show reasons.

---

## Match Resolution Record

```text
id, intake_entry_id, resolution_type
resolved_person_id, created_person_id
resolution_reason, selected_candidate_id
resolved_by_user_id, resolution_method, rule_version, created_at
```

Resolution type: LINK_EXISTING, CREATE_NEW, RETURN_FOR_CORRECTION, DEFER, NO_ACTION  
Method: HUMAN, APPROVED_EXACT_RULE, ADMINISTRATIVE, SYSTEM_RECOVERY  

---

## Intake Correction vs Canonical Update

1. **Intake correction** fixes transcription of paper (append-only history).  
2. **Canonical update** decides whether corrected values update the person (separate decision).
