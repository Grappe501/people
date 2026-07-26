# People Intake — Open Decisions Register

**Audit:** PEOPLE-ARCHITECTURE-AUDIT-AND-DESIGN-VALIDATION-1.0  
**Freeze expectation:** Empty of blocking items  
**Current status:** **NOT EMPTY — freeze blocked**

---

## Blocking (must close before freeze)

| Decision ID | Question | Options | Proposed default for V1 | Owner |
| --- | --- | --- | --- | --- |
| OD-B01 | May EXACT matches auto-link without human? | Always review / Auto-link E-rules / Flag-gated | **Always review in V1**; flag `auto_exact_match_linking` default off | Owner + Reviewer |
| OD-B02 | Does NO_MATCH auto-create person? | Always human Create / Auto-create / Flag-gated | **Human Create New** | Owner + Reviewer |
| OD-B03 | Canonical state dictionary mapping? | Publish map now | **Publish before freeze** | Eng lead |
| OD-B04 | Include AMBIGUOUS in V1 UX? | Add control / Remove from V1 data | **Add to UX** or remove from data—pick one | UX + Data |
| OD-B05 | Shared DB compatibility outcome? | Audit report | **Required read-only audit** | Owner |
| OD-B06 | Data Entry batch/upload capability? | Deny / Allow / Flag | **Deny by default** | Admin/Owner |
| OD-B07 | V1 offline scope? | Full offline / Brief buffer / Online-only submit | **Brief local buffer; online submit required** | Security + UX |
| OD-B08 | Match review claim model? | Mirror page claims | **Mirror page claims with TTL** | Eng lead |
| OD-B09 | Blank/unreadable page submit with 0 entries? | Allowed with reason | **Allowed with required reason codes** | Eng + UX |
| OD-B10 | Interim image retention? | Indefinite / N days / Hold-only | **Retain until policy signed; no auto-delete in V1** | Owner |
| OD-B11 | Preference supersession? | Timestamp wins / Manual only | **Newer explicit YES/NO supersedes; UNKNOWN never supersedes** | Data lead |
| OD-B12 | Quality/ops/freeze docs complete? | Complete package | **Must exist** | Owner |

---

## Non-blocking (may remain open through early implementation planning, not coding of affected areas)

| Decision ID | Question | Notes |
| --- | --- | --- |
| OD-N01 | Exact storage provider | Required before upload implementation wave |
| OD-N02 | Exact signed URL TTL / claim TTL numbers | 30 min claim recommended; finalize in config |
| OD-N03 | Exact upload size / rate limits | Set during quality package |
| OD-N04 | Exact match score formula | Ranking aid only if reasons shown |
| OD-N05 | Exact CSP / session timeout | Security hardening wave |
| OD-N06 | Background job host | Netlify/functions/worker choice |
| OD-N07 | Prisma/table names | After shared DB audit |
| OD-N08 | Monitoring vendor | Ops package |

---

## Formally Accepted Residual Risks

| ID | Acceptance |
| --- | --- |
| OD-A01 | OS/profile may write to `C:\` outside project control |
| OD-A02 | Browser “Save image as” cannot be fully prevented; mitigate with least privilege + audit |

---

## Note

This register **fails** the freeze exit criterion “Open Decisions Register expected to be empty.” Emptiness applies to **blocking** decisions after remediation—not to all future numeric tunables.
