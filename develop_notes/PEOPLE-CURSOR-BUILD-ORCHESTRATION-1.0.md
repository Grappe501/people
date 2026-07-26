# Develop Note — PEOPLE-CURSOR-BUILD-ORCHESTRATION-1.0

## Objective

Produce the Master Cursor Build Orchestration playbook and Volume 0 Project Constitution so implementation (when authorized) has an execution control plane.

## Scope

- Orchestration document (phases 0–12, gates, Git/Netlify, slices, RCs)
- Project Constitution (non-negotiable rules)
- Implementation phase map + living ledger
- Governance updates reflecting dormant coding status

## Out of Scope

- Application code
- Design freeze approval
- Resolving audit Critical findings
- Step 5 quality/ops document package

## Prerequisite honesty

Step 5B text assumes Steps 1–5 complete and audit passed. **Those prerequisites are not met.** Orchestration is written with an explicit hard gate so Phase 0 cannot start until freeze is APPROVED.

## Exit Criteria

- [x] Orchestration doc written under `docs/08_implementation/`
- [x] Constitution written under `docs/00_governance/`
- [x] Ledger initialized
- [x] Next build remains remediation (not Phase 0 code)
- [x] `applicationCodeAuthorized` remains false
