# Implementation Specifications

**Program:** PEOPLE-IMPLEMENTATION-SPECIFICATION-PROGRAM-1.0  
**Phase 0:** COMPLETE (D-060)  
**Phase 1 platform:** COMPLETE (IS-100…105; D-068)  
**Latest IS:** PEOPLE-IS-105 APPROVED (D-068)  
**Standing protocol:** PEOPLE-PROTOCOL-COMMIT-PUSH-DEPLOY-1.0 (D-065)  
**H-drive standard:** PEOPLE-IS-104 + `PEOPLE_INTAKE_H_DRIVE_PROTOCOL.md`  
**GitHub/Netlify model:** PEOPLE-IS-105  
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
| `100_platform/` | Phase 1 platform specs (IS-100…105) |
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

1. `PEOPLE-IS-200-DOMAIN-MODEL-1.0`  
2. Parallel: `PEOPLE-AUDIT-REMEDIATION-AND-QUALITY-OPS-FREEZE-1.0`

IS-105 **APPROVED** (D-068). Phase 1 platform documentation complete.

## Implementation prohibition

No application source, migrations, Netlify functions, UI, live providers, production secrets, GitHub Actions workflows, `netlify.toml`, or deployments until Gate G-10 / explicit authorization. See `START_HERE.md`, PEOPLE-IS-100 §27, and PEOPLE-IS-105 §27.
