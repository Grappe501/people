# People Intake — Terminology Matrix

**Audit:** PEOPLE-ARCHITECTURE-AUDIT-AND-DESIGN-VALIDATION-1.0  
**Goal:** One term → one meaning. Prefer UI plain language for users; internal enums for engineering — with explicit mapping.

| Preferred term | Aliases / avoid | Definition | Authoritative doc |
| --- | --- | --- | --- |
| Batch | Intake Batch | Group of pages from one collection upload | Domain model |
| Page | Volunteer Sheet (UI), Intake Page | One image queue work item | Domain model / UX copy |
| Entry | Intake Entry, Person line, Row | One transcribed person from a page | Domain model |
| Person | Canonical Person | Durable shared identity | Canonical contract |
| Attribute | Person Attribute | Provenanced person value | Canonical contract |
| Capture | Upload Sheets | Field photograph/upload workspace | UX architecture |
| Transcribe | Enter Sheets, Data entry | Office transcription workspace | UX architecture |
| Match | Match People, Matching review | Identity resolution workspace | UX architecture |
| Manage | Admin | Oversight workspace | UX architecture |
| Blank (UI) | — | Consent not marked; stores UNKNOWN | Form behavior / copy guide |
| UNKNOWN | — | Consent semantic value | Field dictionary |
| Not Provided | NOT_PROVIDED | Field intentionally empty | Field dictionary |
| Unreadable | UNREADABLE | Writing present but illegible | Field dictionary |
| Ambiguous | AMBIGUOUS | **Unresolved UX exposure** | Field dictionary only today |
| Claim | Assignment | Exclusive edit lock on page/review item | Queue & claiming |
| Promotion | Controlled promotion | Intake → canonical domain handoff | Canonical / integration contracts |
| Exact Match | EXACT | Deterministic rule tier — **auto-action undecided** | Matching engine |
| Possible Match | POSSIBLE | Human review required | Matching engine |
| Conflict | CONFLICT | Incompatible signals | Matching engine |
| Source Image | Original | Private authoritative file | Image storage |
| Display derivative | — | Viewing-only transform | Image storage |
| Audit event | — | Append-only accountability record | Logging and audit |
| Technical log | Log | Ops/debug; no raw PII | Logging and audit |

---

## State Dual-Track (Must Be Unified)

| User-facing label (current UX) | Engineering-ish name (current contracts) | Notes |
| --- | --- | --- |
| Ready for Entry | READY_FOR_ENTRY | Align |
| Assigned | CLAIMED_FOR_ENTRY | Align naming |
| In Progress | ENTRY_IN_PROGRESS | Align |
| Entry Complete | ENTRY_SUBMITTED / READY_FOR_MATCHING | Split if needed |
| Matching | MATCHING_IN_PROGRESS | Align |
| Needs Match Review | NEEDS_MATCH_REVIEW | Align |
| Needs Correction | NEEDS_ENTRY_CORRECTION | Align |
| *(missing)* | PROMOTION_PENDING | **Must add user label** |
| Completed | COMPLETED | Align |

Until a single map is published, treat state names as **High documentation risk**.

---

## Naming Hygiene Rules Going Forward

1. Decision Log wins conflicts after acceptance.  
2. Glossary must list every enum shown to operators or stored.  
3. JSON contracts must not introduce enums absent from field dictionary / state dictionary.  
4. UI copy guide owns operator-visible strings only.
