# People Intake — Design-Before-Code Protocol

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-GOVERNANCE-FOUNDATION-1.0  
**Authority:** Permanent protocol until superseded by design freeze amendment

---

## Doctrine

> Design every important behavior before implementing it.

The approved design documents and machine-readable contracts govern implementation. The codebase must never become the accidental source of truth.

---

## Design Sequence

```text
Governance
→ Workflow design
→ UX design
→ Domain and database design
→ Security design
→ API and engineering contracts
→ Test and deployment design
→ Design audit
→ Design freeze
→ Implementation
```

---

## Design Stages

| Stage | Name | Application code |
| --- | --- | --- |
| -1 | Governance Foundation | Forbidden |
| 0 | Complete Design | Forbidden |
| Freeze | Design Freeze Gate | Forbidden until approved |
| 1+ | Implementation phases | Authorized only after Gate G-10 |

---

## Prohibited Before Design Freeze

Cursor may not create before design freeze:

- Application routes
- React components
- API handlers
- Database migrations
- Production Prisma schema changes
- Authentication implementation
- Storage implementation
- Deployment functions
- UI code
- Live integrations
- Next.js application scaffolding
- Netlify functions
- Matching-engine implementation
- Image-upload implementation

---

## Permitted Documentation Artifacts Before Freeze

- Markdown documents
- JSON contracts
- JSON schemas
- Diagrams expressed as Mermaid or text
- Validation scripts for documentation
- Empty folder structures when explicitly authorized
- Minimal package metadata needed only for documentation validation

---

## Design Review Standards

Every design document must:

1. State purpose and scope.
2. Cross-reference related governing documents.
3. Use consistent entity, role, and state names.
4. Avoid silent contradiction with higher-authority documents.
5. Mark unresolved decisions explicitly.
6. Separate Version 1 requirements from future-compatible notes.

---

## Cross-Reference Requirements

Documents must align on:

- Entity names (Batch, Page, Intake Entry, Canonical Person)
- Role names (Uploader, Data Entry, Matcher/Reviewer, Administrator, Owner)
- Page and entry state names
- Volunteer / Email List semantics (`YES`, `NO`, `UNKNOWN`)
- Field condition semantics (`PROVIDED`, `NOT_PROVIDED`, `UNREADABLE`)
- H-drive root and prohibited paths
- Design-freeze and implementation gates

---

## Decision Closure Requirements

Blocking decisions must be recorded in the Decision Log with:

- Decision ID
- Status
- Reason
- Alternatives considered
- Consequences
- Related files
- Revisit trigger

Implementation may not invent answers for blocking open decisions.

---

## Design Audit

Before freeze, an audit must check for:

- Contradictions
- Missing states
- Permission gaps
- Data-loss risks
- Race conditions
- UX friction
- Security weaknesses
- RedDirt compatibility
- H-drive compliance
- Unresolved blocking decisions

---

## Design Freeze

Design freeze requires:

- Master build plan complete
- All required design volumes complete or explicitly waived
- Contracts validated
- Audit passed
- Explicit approval recorded

After freeze, implementation follows frozen contracts. Material changes require a controlled design amendment.

---

## Approval Gate

Gate G-9 (Design Freeze) and Gate G-10 (Implementation Authorization) are defined in:

```text
docs/08_implementation/PEOPLE_INTAKE_BUILD_GATES.md
```

No production application code is authorized until Gate G-10 passes.

---

## Implementation Handoff

After freeze, handoff must include:

- Frozen contract set
- File and folder map
- Implementation phase map
- Build gates still in force
- Known risks and non-blocking open questions

---

## Later Design Changes

Post-freeze changes require:

1. Decision Log entry
2. Document and contract updates
3. Cross-reference validation
4. Re-audit of affected areas
5. Explicit re-authorization if the change alters frozen contracts
