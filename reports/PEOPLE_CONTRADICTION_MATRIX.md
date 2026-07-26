# People Intake — Contradiction Matrix

**Audit:** PEOPLE-ARCHITECTURE-AUDIT-AND-DESIGN-VALIDATION-1.0  
**Rule:** If two documents can both be “true” and lead to different implementations, record a contradiction.

| ID | Document A | Document B | Conflict | Severity | Resolution required |
| --- | --- | --- | --- | --- | --- |
| X-01 | `PEOPLE_INTAKE_FIELD_DICTIONARY.md` conditions include AMBIGUOUS | `PEOPLE_INTAKE_FORM_BEHAVIOR_SPEC.md` only Not Provided / Unreadable | Operators cannot express Ambiguous in UX | High | Add UX control or remove from V1 data |
| X-02 | Glossary omits Ambiguous | Field dictionary defines AMBIGUOUS | Shared language incomplete | High | Update glossary |
| X-03 | Field dictionary: UNKNOWN may mean unreadable | Separate UNREADABLE field condition | Dual encoding of same reality | High | Validation coupling rules |
| X-04 | Matching workflow: auto-link deferred to data design | Matching engine: deferred to security | Security still deferred | Critical | Lock V1 auto-link policy |
| X-05 | Matching workflow: multiple phones deferred to data | Canonical contract: multiple attributes supported | Workflow text stale vs data lock | Medium | Update matching workflow prose |
| X-06 | `page-state-machine.json` states | Engineering transitions `READY_FOR_ENTRY` / `CLAIMED_FOR_ENTRY` | Dual vocabularies | Critical | Canonical state map |
| X-07 | Master plan page enums (UPLOADING…ARCHIVED) | UX page states (Assigned/In Progress…) | Third vocabulary | Critical | Single map |
| X-08 | Entry state machine lacks promotion pending | Error/API: promotion pending / page not complete | Missing state | High | Add states |
| X-09 | API submit: 1–10 entries unless exception | UX: Mark Page Unreadable / blank with 0 entries | Submit cardinality | High | Formal blank/unreadable submit |
| X-10 | Roles: Reviewer transcription Optional | Authz: Reviewer Claim page No | Ambiguous whether reviewer can enter | Medium | V1: Reviewer cannot transcribe |
| X-11 | Authz: Data Entry create/upload Optional by policy | No written policy document | Undefined capability | High | Default deny + flag |
| X-12 | UX weak-signal draft survival | Security: offline may be deferred | Offline scope | High | Lock V1 online-required submit |
| X-13 | Queue: match claim “later” | Concurrency: match review lock required | Incomplete design | High | Specify match claims |
| X-14 | Controlled promotion locked | Preferred Model A still described in older master plan prose | Historical dual recommendation | Medium | Annotate master plan “superseded by D-032” |
| X-15 | Decision log open list vs freeze expectation of empty opens | Freeze exit criteria | Cannot freeze with open Critical/High | Critical | Close or formally accept |

---

## Non-Contradictions (Clarified as Intentional)

| Topic | Interpretation |
| --- | --- |
| UI Blank vs DB UNKNOWN | Intentional mapping — keep |
| Raw vs normalized | Intentional separation — keep |
| User labels vs internal enums | Allowed **only** with explicit bijection table |
| Model B promotion vs shared DB | Intentional isolation — keep |
