# People Intake — Risk Register

**Audit:** PEOPLE-ARCHITECTURE-AUDIT-AND-DESIGN-VALIDATION-1.0  
**Owner default:** Project Owner / Design lead  
**Freeze rule:** No Critical or unresolved High at freeze

| Risk ID | Description | Sev | Likelihood | Impact | Owner | Mitigation | Status | Target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-001 | Implement without quality/ops/freeze docs | Critical | High | Uncontrolled build, missed tests/ops | Owner | Complete DOC-044–060 package | Open | Before freeze |
| R-002 | Silent false person merges via invented auto-link | Critical | Medium | Trust destruction, PII corruption | Reviewer lead | Lock V1 auto-link=off or explicit rules | Open | Before freeze |
| R-003 | Promotion redesign after coding due to unknown RedDirt schema | Critical | High | Rework, delay | Owner | Shared DB compatibility audit | Open | Before freeze |
| R-004 | State machine mismatch causes stuck pages | Critical | High | Queue deadlock, data inconsistency | Eng lead | Canonical state dictionary | Open | Before freeze |
| R-005 | Ambiguous field not in UX leads to wrong NOT_PROVIDED | High | Medium | Bad matching/consent | UX lead | Align AMBIGUOUS | Open | Before freeze |
| R-006 | Consent UNKNOWN vs UNREADABLE conflict | High | Medium | Bad preference history | Data lead | Validation coupling | Open | Before freeze |
| R-007 | Zero-entry submit rejected incorrectly | High | Medium | Unreadable pages stuck | Eng lead | Blank/unreadable submit contract | Open | Before freeze |
| R-008 | Dual match reviewers collide | High | Medium | Duplicate resolutions | Eng lead | Match claim model | Open | Before freeze |
| R-009 | Wrong storage provider choice late | High | Medium | Upload/security rework | Eng lead | Provider decision | Open | Before impl wave 2 |
| R-010 | Lifecycle deletes evidence | High | Low | Irreversible loss | Owner | Retention policy + legal hold | Open | Before any lifecycle job |
| R-011 | Data Entry gains unintended upload rights | High | Medium | Scope creep / PII sprawl | Admin | Default deny optional capabilities | Open | Before freeze |
| R-012 | Auto-create people on NO_MATCH floods duplicates | High | Medium | Canonical pollution | Reviewer lead | Human confirm CREATE_NEW in V1 | Open | Before freeze |
| R-013 | Preference Yes overwritten by Unknown | High | Low | Consent corruption | Data lead | Supersession rules | Open | Before freeze |
| R-014 | Offline draft PII on shared phones | High | Medium | Privacy incident | Security | V1 online submit + clear sync UI | Open | Before freeze |
| R-015 | Pages marked complete while promotion pending | High | Medium | False operational metrics | Eng lead | Promotion-pending state in UX | Open | Before freeze |
| R-016 | No incident runbook when image leaks | High | Medium | Slow response | Ops | Incident doc in ops package | Open | Before freeze |
| R-017 | Household phone auto-link (if rules weak) | High | Medium | Spouse/family false merge | Matching | Shared flag blocks independent identity | Partially mitigated in design | Verify in rules lock |
| R-018 | Orphan objects if storage/DB diverge | Medium | Medium | Cost + privacy residue | Eng lead | Compensation + cleanup jobs | Designed, not detailed | Quality package |
| R-019 | Stale browser overwrite | Medium | Medium | Lost work / corruption | Eng lead | Claim+version (designed) | Mitigated in design | Prove in tests |
| R-020 | Admin force-complete abuse | Medium | Low | Evidence skip | Owner | Reason + audit required | Open | Before freeze |
| R-021 | Terminology drift across docs | Medium | High | Implementer errors | Docs lead | Terminology matrix + glossary update | Open | Remediation |
| R-022 | Scale to 100k pages without index plan | Medium | Medium | Slow queues | Eng lead | Index strategy after schema audit | Open | Pre-migration |
| R-023 | OCR/AI later incompatible with raw immutability | Low | Low | Future rework | Owner | Keep raw immutable (good) | Accept | — |
| R-024 | H-drive OS writes to C:\ | Low | High | Policy noise | All | Honest limitation + validators | Accept | Ongoing |

---

## Status Legend

- **Open** — must be addressed for freeze (Critical/High) or tracked  
- **Partially mitigated** — design intent present; needs lock/test  
- **Mitigated in design** — controls documented; proof deferred to tests  
- **Accept** — known residual risk with justification  
