# People Intake — Scope and Boundaries

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-GOVERNANCE-FOUNDATION-1.0

---

## Purpose

Define what People Intake includes, excludes, and how it relates to RedDirt and other systems.

---

## In-Scope Functions (Version 1 Design Target)

- Secure sign-in
- Role-based access
- Mobile image capture
- Multi-image upload
- Intake batch creation
- Shared page queue
- Page claiming
- Page transcription (up to ten entries per page)
- Draft autosave
- Page-level submission
- Entry normalization
- Exact duplicate detection
- Possible-match generation
- Human matching review
- Canonical person creation or linkage
- Private image storage
- Audit history
- Batch progress
- Queue metrics
- Recent activity
- Administrative reassignment
- Image quality review
- Data validation
- Error recovery
- Mobile, tablet, and desktop layouts
- Netlify deployment
- Database connectivity
- Operational documentation

---

## Out-of-Scope Functions (Version 1)

- Handwriting OCR
- AI transcription
- Email sending
- Text messaging
- Volunteer scheduling
- Event management
- Canvassing tools
- Donor management
- Relationship scoring
- Public intake forms
- Native iOS or Android applications
- Public image URLs
- Automatic uncertain merges
- Marketing automation
- Full CRM dashboards
- Voter-file matching
- Household modeling
- Address enrichment
- External data purchases

---

## Application Boundaries

| Boundary | Rule |
| --- | --- |
| Project root | `H:\people` only |
| Application identity | Separate from RedDirt |
| Repository | Dedicated GitHub repository preferred |
| Deployment | Dedicated Netlify site preferred |
| Code sharing | No direct RedDirt code imports |
| Contracts | Shared database contracts, not shared application modules |

---

## Database Boundaries

- Same hosted Postgres environment / connectivity conventions as RedDirt
- Separate application credentials
- Least-privilege permissions
- Additive schema changes preferred
- No destructive schema changes without explicit approval
- Intake-domain tables owned by People Intake design
- Canonical people integration chosen and documented before implementation

---

## Storage Boundaries

- Source images in private object storage
- Postgres stores metadata and storage keys, not image blobs as the primary strategy
- Signed temporary viewing URLs only
- No public permanent image URLs
- Development and production storage separation

---

## RedDirt Relationship

```text
One hosted Postgres database environment
Two applications
Separate application credentials
Shared canonical people records (via approved contract)
```

People Intake may:

- Create intake batches, pages, and entries
- Upload and link source images
- Create or update people through approved matching flows
- Record volunteer and email-list preferences
- Read only records needed for duplicate detection and authorized review

People Intake must not automatically receive unrestricted access to every campaign, donor, mission, calendar, or administrative table in RedDirt.

---

## Cross-Project Dependency Rules

- People Intake may reference RedDirt conventions and shared database contracts.
- People Intake must not edit files under `H:\SOSWebsite` during People Intake builds unless explicitly authorized in a separate build script.
- RedDirt must not be modified as a side effect of People Intake governance or design builds.

---

## Prohibited Cross-Lane Imports

- No importing RedDirt UI, campaign, donor, or scheduling modules into People Intake.
- No copying production secrets between projects into documentation.
- No shared writable public buckets for volunteer images.

---

## No-Send Rules

Version 1 must not send:

- Email
- SMS / text messages
- Push outreach
- Automated campaign communications

---

## No-Public-Image Rules

Source images must never:

- Appear in public routes
- Be indexed publicly
- Be placed in a public repository
- Be logged as base64
- Be exposed through permanent unsigned URLs
- Be cached in public CDN paths without authorization

---

## No-OCR Rules

Version 1 must not include handwriting OCR or AI transcription as a required path. Manual transcription is the designed operating mode.

---

## No-Automatic-Merge Rules

The system may assist with matching and may auto-link only approved exact-match categories. It must not:

- Silently merge uncertain people
- Invent missing data
- Interpret unmarked fields as `NO`
- Replace raw transcription with normalized values as the only retained evidence
- Delete source evidence automatically

---

## No-Production-Change Rules During Design

Until design freeze and implementation authorization:

- No production database changes
- No production migrations
- No production deployments of application code
- No production secret inspection for convenience
- No live storage bucket mutation for application features

---

## Future-Compatible Areas (Not Version 1 Commitments)

- PWA offline support
- Address fields
- County and precinct enrichment
- Organization affiliations
- Event linkage
- Volunteer skills and availability
- Source campaigns
- QR batch labels
- AI-assisted quality review
- RedDirt relationship integration expansion
- External form imports
- Bulk spreadsheet imports
- Retention schedules
- Consent-history expansion
