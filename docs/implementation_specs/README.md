# Implementation Specifications

**Program:** PEOPLE-IMPLEMENTATION-SPECIFICATION-PROGRAM-1.0  
**Phase 0:** COMPLETE (D-060)  
**Latest IS:** PEOPLE-IS-103 APPROVED (D-066)  
**Standing protocol:** PEOPLE-PROTOCOL-COMMIT-PUSH-DEPLOY-1.0 (D-065)  
**Status:** DOCUMENTATION GOVERNANCE APPROVED — APPLICATION IMPLEMENTATION NOT AUTHORIZED  
**Project root:** `H:\people`

## Purpose

Translate approved Volumes and Catalogs into precise engineering specifications. Documentation before implementation. Approval ≠ coding authorization.

## Document hierarchy

Master Build → Volumes → Catalogs 00–09 → Protocols → ADRs → IS specs → PKG-* → Application (blocked) → Verification → Runbooks

## Directory map

| Path | Role |
| --- | --- |
| `000_program/` | Phase 0 IS-000…005 |
| `100_platform/` | Phase 1 platform specs (IS-100…) |
| `200_domain/` … `1400_authorization/` | Future phases |
| `matrices/` | Traceability matrices |
| `decisions/` | Decision + open-issue registers |
| `reports/` | Progress + phase completion |
| `templates/` | Spec templates |

## How to add a specification

1. Copy `templates/IMPLEMENTATION_SPECIFICATION_TEMPLATE.md`  
2. Assign PEOPLE-IS-* ID per PEOPLE-IS-002  
3. Map requirements into the traceability matrix  
4. Record open issues / ADRs  
5. Advance readiness via PEOPLE-IS-005 gates  

## Current next-ready documents

1. `PEOPLE-IS-104-H-DRIVE-WORKSPACE-PROTOCOL-1.0`  

IS-103 **APPROVED** (D-066). Commit/push protocol restored (D-065).  

## Implementation prohibition

No application source, migrations, Netlify functions, UI, live providers, production secrets, or deployments until Gate G-10 / explicit authorization. See `START_HERE.md` and PEOPLE-IS-100 §27.
