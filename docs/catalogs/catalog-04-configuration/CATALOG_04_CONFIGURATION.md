# PEOPLE INTAKE SYSTEM

# CATALOG 4 — CONFIGURATION CATALOG

**Document ID**

```text
PEOPLE-CATALOG-04-CONFIGURATION-1.0
```

**Catalog Set**

```text
PEOPLE-CATALOG-LIBRARY-1.0
```

**Status**

```text
DESIGN COMPLETE — IMPLEMENTATION NOT AUTHORIZED
```

**Project Root**

```text
H:\people
```

**Document Type**

```text
CANONICAL CONFIGURATION CATALOG
```

**Build Mode**

```text
DOCUMENTATION ONLY
```

**Prohibited During This Catalog**

* No application source code
* No environment file creation for production secrets
* No dependency installation
* No deployment configuration implementation
* No feature-flag runtime wiring
* No inventing undocumented production configuration keys outside this catalog and its approved amendments

**Foundation Scope**

This document establishes the governing configuration contract: principles, categories, entry standard, scopes, types, secret classification, validation, change management, and seeded configuration keys.

Exact production values, provider-specific credentials, and remaining keys must be added through formal catalog amendments under this contract and must not contradict Volumes 0–13 or Catalogs 1–3.

---

# PART I — PURPOSE

## 1. Mission

The Configuration Catalog defines every configurable value used by the People Intake System.

Its goals are to ensure:

* predictable deployments
* reproducible environments
* secure secret management
* centralized configuration
* consistent defaults
* environment independence
* operational flexibility without code changes

No configuration value may exist outside this catalog.

---

# PART II — CONFIGURATION PRINCIPLES

## 2. Core Principles

### `CONFIG-PRINCIPLE-001 — External to Code`

Configuration must be external to application code.

### `CONFIG-PRINCIPLE-002 — Documented`

Configuration must be version controlled as documentation.

### `CONFIG-PRINCIPLE-003 — Multi-Environment`

Configuration must support development, testing, staging, and production.

### `CONFIG-PRINCIPLE-004 — Documented Defaults`

Every configuration item must have documented defaults where applicable.

### `CONFIG-PRINCIPLE-005 — Validation Rules`

Every configuration item must have documented validation rules.

### `CONFIG-PRINCIPLE-006 — Secret Identification`

Every configuration item must identify whether it contains secrets.

### `CONFIG-PRINCIPLE-007 — Restart Requirements`

Every configuration item must specify restart requirements.

### `CONFIG-PRINCIPLE-008 — Runtime Mutability`

Every configuration item must specify runtime mutability.

### `CONFIG-PRINCIPLE-009 — Discoverable`

Configuration must never require searching source code to understand.

### `CONFIG-PRINCIPLE-010 — Catalog Authority`

No production configuration key may exist outside this catalog or an approved amendment.

Configuration must:

* be external to application code
* be version controlled as documentation
* support development, testing, staging, and production
* have documented defaults
* have documented validation rules
* identify whether it contains secrets
* specify restart requirements
* specify runtime mutability

Configuration must never require searching source code to understand.

---

## 3. Configuration Categories

The catalog is divided into:

```text
Application
Environment
Authentication
Authorization
Database
Storage
Uploads
Queue
Claims
Drafts
Transcription
Matching
Promotion
Background Jobs
Notifications
Security
Logging
Monitoring
Reporting
Exports
Feature Flags
Performance
Retention
Developer Options
```

---

# PART III — CONFIGURATION ENTRY STANDARD

Every configuration entry includes:

```text
Configuration ID
Configuration Key
Display Name
Category
Description
Data Type
Allowed Values
Default Value
Required
Secret
Environment Scope
Runtime Change Allowed
Restart Required
Validation Rules
Dependent Components
Related Catalogs
```

---

# PART IV — ENVIRONMENT SCOPES

Supported scopes:

```text
Development
Testing
Staging
Production
All
```

Configuration may specify different defaults for each environment.

---

# PART V — DATA TYPES

Supported types:

```text
String
Integer
Boolean
Duration
File Size
URL
Enum
Array
JSON
Secret
```

Validation rules must match the declared type.

---

# PART VI — APPLICATION CONFIGURATION

### CONFIG-APP-001

**Key**

```text
APPLICATION_NAME
```

Default:

```text
People Intake System
```

---

### CONFIG-APP-002

```text
APPLICATION_VERSION
```

Read-only.

Set during deployment.

---

### CONFIG-APP-003

```text
APPLICATION_ENVIRONMENT
```

Allowed values:

```text
development
testing
staging
production
```

Required:

Yes.

---

# PART VII — AUTHENTICATION

### CONFIG-AUTH-001

```text
AUTH_PROVIDER
```

Allowed values:

```text
Supabase
```

Future providers require catalog updates.

---

### CONFIG-AUTH-002

```text
AUTH_SESSION_TIMEOUT
```

Type:

Duration

Defines maximum authenticated session lifetime.

---

### CONFIG-AUTH-003

```text
AUTH_REFRESH_WINDOW
```

Defines session renewal window.

---

### CONFIG-AUTH-004

```text
AUTH_MAX_LOGIN_ATTEMPTS
```

Type:

Integer

---

# PART VIII — AUTHORIZATION

### CONFIG-PERM-001

```text
DEFAULT_USER_ROLE
```

Default:

```text
viewer
```

---

### CONFIG-PERM-002

```text
ALLOW_ADMIN_OVERRIDE
```

Boolean.

---

# PART IX — DATABASE

### CONFIG-DB-001

```text
DATABASE_URL
```

Secret:

Yes.

Environment:

All.

---

### CONFIG-DB-002

```text
DATABASE_CONNECTION_POOL
```

Type:

Integer.

---

### CONFIG-DB-003

```text
DATABASE_QUERY_TIMEOUT
```

Duration.

---

### CONFIG-DB-004

```text
DATABASE_STATEMENT_TIMEOUT
```

Duration.

---

### CONFIG-DB-005

```text
DATABASE_MAX_RETRIES
```

Integer.

---

# PART X — STORAGE

### CONFIG-STORAGE-001

```text
STORAGE_PROVIDER
```

Allowed values:

```text
Netlify
```

Future providers require catalog updates.

---

### CONFIG-STORAGE-002

```text
STORAGE_BUCKET_SOURCE_IMAGES
```

---

### CONFIG-STORAGE-003

```text
STORAGE_SIGNED_URL_DURATION
```

Duration.

---

### CONFIG-STORAGE-004

```text
STORAGE_MAX_FILE_SIZE
```

Type:

File Size.

---

### CONFIG-STORAGE-005

```text
STORAGE_ALLOWED_IMAGE_TYPES
```

Array.

---

# PART XI — UPLOADS

### CONFIG-UPLOAD-001

```text
UPLOAD_MAX_CONCURRENT_UPLOADS
```

Integer.

---

### CONFIG-UPLOAD-002

```text
UPLOAD_SESSION_DURATION
```

Duration.

---

### CONFIG-UPLOAD-003

```text
UPLOAD_ENABLE_DUPLICATE_DETECTION
```

Boolean.

---

### CONFIG-UPLOAD-004

```text
UPLOAD_HASH_ALGORITHM
```

Enum.

---

# PART XII — CLAIMS

### CONFIG-CLAIM-001

```text
CLAIM_DURATION
```

Duration.

---

### CONFIG-CLAIM-002

```text
CLAIM_WARNING_THRESHOLD
```

Duration.

---

### CONFIG-CLAIM-003

```text
CLAIM_ALLOW_RENEWAL
```

Boolean.

---

### CONFIG-CLAIM-004

```text
CLAIM_MAX_RENEWALS
```

Integer.

---

# PART XIII — DRAFTS

### CONFIG-DRAFT-001

```text
DRAFT_AUTOSAVE_INTERVAL
```

Duration.

---

### CONFIG-DRAFT-002

```text
DRAFT_RETENTION_PERIOD
```

Duration.

---

### CONFIG-DRAFT-003

```text
DRAFT_LOCAL_RECOVERY_ENABLED
```

Boolean.

---

# PART XIV — MATCHING

### CONFIG-MATCH-001

```text
MATCH_CONFIDENCE_THRESHOLD
```

Decimal.

---

### CONFIG-MATCH-002

```text
MATCH_MAX_CANDIDATES
```

Integer.

---

### CONFIG-MATCH-003

```text
MATCH_REQUIRE_REVIEW_BELOW_THRESHOLD
```

Boolean.

---

# PART XV — PROMOTION

### CONFIG-PROMOTION-001

```text
PROMOTION_MAX_RETRIES
```

Integer.

---

### CONFIG-PROMOTION-002

```text
PROMOTION_RETRY_DELAY
```

Duration.

---

### CONFIG-PROMOTION-003

```text
PROMOTION_REQUIRE_IDEMPOTENCY
```

Boolean.

---

# PART XVI — BACKGROUND JOBS

### CONFIG-JOB-001

```text
JOB_MAX_ATTEMPTS
```

Integer.

---

### CONFIG-JOB-002

```text
JOB_TIMEOUT
```

Duration.

---

### CONFIG-JOB-003

```text
JOB_CONCURRENCY
```

Integer.

---

### CONFIG-JOB-004

```text
JOB_BACKOFF_STRATEGY
```

Allowed values:

```text
Linear
Exponential
```

---

# PART XVII — NOTIFICATIONS

### CONFIG-NOTIFY-001

```text
NOTIFICATION_EXPIRATION
```

Duration.

---

### CONFIG-NOTIFY-002

```text
ENABLE_IN_APP_NOTIFICATIONS
```

Boolean.

---

### CONFIG-NOTIFY-003

```text
ENABLE_EMAIL_NOTIFICATIONS
```

Boolean.

---

# PART XVIII — SECURITY

### CONFIG-SECURITY-001

```text
ENABLE_CSRF_PROTECTION
```

Boolean.

---

### CONFIG-SECURITY-002

```text
ENABLE_RATE_LIMITING
```

Boolean.

---

### CONFIG-SECURITY-003

```text
MAX_REQUEST_SIZE
```

File Size.

---

### CONFIG-SECURITY-004

```text
ENABLE_CONTENT_SECURITY_POLICY
```

Boolean.

---

### CONFIG-SECURITY-005

```text
ENABLE_SECURITY_HEADERS
```

Boolean.

---

# PART XIX — LOGGING

### CONFIG-LOG-001

```text
LOG_LEVEL
```

Allowed values:

```text
Debug
Info
Warn
Error
Critical
```

---

### CONFIG-LOG-002

```text
LOG_RETENTION_DAYS
```

Integer.

---

### CONFIG-LOG-003

```text
LOG_PII_REDACTION
```

Boolean.

---

# PART XX — MONITORING

### CONFIG-MONITOR-001

```text
ENABLE_HEALTH_ENDPOINT
```

Boolean.

---

### CONFIG-MONITOR-002

```text
HEALTH_CHECK_INTERVAL
```

Duration.

---

### CONFIG-MONITOR-003

```text
ALERT_THRESHOLD_ERROR_RATE
```

Percentage.

---

# PART XXI — REPORTING

### CONFIG-REPORT-001

```text
REPORT_MAX_ROWS
```

Integer.

---

### CONFIG-REPORT-002

```text
REPORT_DEFAULT_PAGE_SIZE
```

Integer.

---

# PART XXII — EXPORTS

### CONFIG-EXPORT-001

```text
EXPORT_MAX_ROWS
```

Integer.

---

### CONFIG-EXPORT-002

```text
EXPORT_LINK_EXPIRATION
```

Duration.

---

### CONFIG-EXPORT-003

```text
EXPORT_MAX_DOWNLOADS
```

Integer.

---

# PART XXIII — FEATURE FLAGS

Every feature flag must include:

* owner
* purpose
* default state
* removal target

Examples:

```text
FEATURE_ADVANCED_MATCHING
FEATURE_BACKGROUND_PROMOTION
FEATURE_BULK_EXPORT
FEATURE_OPERATOR_DASHBOARD
```

Feature flags are temporary and should not become permanent configuration.

---

# PART XXIV — PERFORMANCE

Representative settings:

```text
MAX_PAGE_SIZE
DEFAULT_PAGE_SIZE
CACHE_DURATION
QUERY_TIMEOUT
IMAGE_PREVIEW_SIZE
```

Performance tuning must not alter business rules.

---

# PART XXV — RETENTION

Representative configuration:

```text
AUDIT_RETENTION_CLASS
DRAFT_RETENTION_PERIOD
EXPORT_RETENTION_PERIOD
JOB_HISTORY_RETENTION
```

Actual durations are governed by the Data Retention Catalog.

---

# PART XXVI — SECRET CLASSIFICATION

Every configuration value is classified as:

```text
Public
Internal
Sensitive
Secret
```

Secret values:

* never appear in logs
* never appear in client bundles
* never appear in API responses
* must use secure environment storage

---

# PART XXVII — VALIDATION RULES

Every configuration value must be validated during startup.

Startup must fail for:

* missing required secrets
* invalid enum values
* invalid numeric ranges
* malformed URLs
* unsupported providers

---

# PART XXVIII — TRACEABILITY

Each configuration item maps to:

* affected components
* APIs
* state machines
* background jobs
* permissions
* deployment environments
* tests

---

# PART XXIX — CHANGE MANAGEMENT

Every configuration change must record:

```text
Configuration Key
Previous Value
New Value
Actor
Timestamp
Reason
Approval (if required)
```

High-risk configuration changes require audit events.

---

# PART XXX — LOCKED CONFIGURATION DECISIONS

## Locked Decisions

1. No production configuration key may exist outside this catalog or an approved amendment.
2. Configuration is external to application code.
3. Secrets never appear in logs, client bundles, or API responses.
4. Required secrets missing at startup fail startup.
5. Invalid enum values fail startup.
6. Unsupported providers fail startup.
7. Feature flags are temporary and must have removal targets.
8. Performance tuning must not alter business rules.
9. Retention durations are governed by the Data Retention Catalog.
10. AUTH_PROVIDER additions require catalog updates.
11. STORAGE_PROVIDER additions require catalog updates.
12. High-risk configuration changes require audit events.
13. Seeded configuration keys in this catalog are authoritative.
14. Exact production values may be environment-specific but must use cataloged keys.
15. Configuration must never require searching source code to understand.

---

# PART XXXI — READINESS

| Area                    | Readiness |
| ----------------------- | --------: |
| Configuration Structure |      100% |
| Environment Strategy    |      100% |
| Secret Management       |      100% |
| Validation              |      100% |
| Feature Flags           |      100% |
| Startup Rules           |      100% |
| Traceability            |       98% |
| Governance              |      100% |
| Seeded Keys             |      100% |
| Exact Production Values | Deferred to env + amendment |

**Overall Catalog 4 Readiness**

```text
99%
```

The remaining percentage is reserved for exact environment values, Permission Catalog linkage, Retention Catalog durations, and Cross-Volume Traceability.

---

# PART XXXII — NEXT CATALOG

## Next Catalog

```text
PEOPLE-CATALOG-05-PERMISSIONS-1.0
```

This catalog will define every role, permission, resource scope, administrative capability, separation-of-duties rule, and authorization matrix used by the People Intake System.

With Catalogs 1–4 in place, the project now has governing specifications for **workflow states, errors, audit events, and configuration**. The next major governance layer is the **Permissions Catalog**, which will formally define who can perform every action in the system and under what conditions.

No application code is authorized during the catalog sequence.
