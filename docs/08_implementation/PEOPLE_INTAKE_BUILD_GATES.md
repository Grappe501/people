# People Intake — Build Gates

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-GOVERNANCE-FOUNDATION-1.0

---

## Gate G-1: Workspace Safety

Requires:

- Root is `H:\people`
- Controlled temp paths use `H:\people`
- Controlled npm cache uses `H:\people`
- No project artifact is intentionally created on `C:\`

Validation: `npm run drive:validate`

---

## Gate G-2: Governance Completeness

Requires:

- Master plan
- Product charter
- Scope
- H-drive protocol
- Design-before-code protocol
- Source-of-truth registry
- Decision log
- Glossary
- Cursor protocol
- Build gates
- Progress ledger

Validation: `npm run governance:validate`

**Status after PEOPLE-GOVERNANCE-FOUNDATION-1.0:** targeted for PASS

---

## Gate G-3: Workflow Design

Future gate requiring:

- Capture workflow
- Transcription workflow
- Matching workflow
- Queue and claims
- State machines
- Exception workflows
- User roles document

---

## Gate G-4: UX Design

Future gate requiring:

- Mobile screen specification
- Tablet and desktop specification
- Image viewer
- Ten-entry form behavior
- Accessibility
- Content guide
- UX architecture

---

## Gate G-5: Data and Storage Design

Future gate requiring:

- Domain model
- ERD
- Database architecture
- Field dictionary
- Canonical-person contract
- Matching specification
- Storage architecture
- Migration strategy
- Provenance

---

## Gate G-6: Security and Engineering Design

Future gate requiring:

- Authentication
- Authorization
- Threat model
- API contracts
- Service contracts
- Error contract
- Concurrency
- Idempotency
- Secret management
- Logging and audit

---

## Gate G-7: Quality and Operations Design

Future gate requiring:

- Test plan
- Test cases
- Deployment plan
- Runbooks
- Operator manual
- Incident recovery
- Launch checklist

---

## Gate G-8: Design Audit

Requires:

- Cross-document audit
- Contract validation
- Contradiction resolution
- No blocking open decisions
- Security review
- UX friction review
- Data-loss review

---

## Gate G-9: Design Freeze

Requires explicit approval before implementation.

Produces:

- Design freeze report
- Frozen contracts
- Implementation handoff

---

## Gate G-10: Implementation Authorization

Only this gate authorizes creation of application code (`src/`, routes, components, Prisma migrations, auth/storage implementations, Netlify functions).

Until G-10 passes:

```text
applicationCodeAuthorized = false
```
