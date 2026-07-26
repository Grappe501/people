#!/usr/bin/env python3
"""Build Catalog 4 configuration foundation registry."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "data" / "documentation"
CAT4 = ROOT / "docs" / "catalogs" / "catalog-04-configuration" / "CATALOG_04_CONFIGURATION.md"

CATEGORIES = [
    "Application",
    "Environment",
    "Authentication",
    "Authorization",
    "Database",
    "Storage",
    "Uploads",
    "Queue",
    "Claims",
    "Drafts",
    "Transcription",
    "Matching",
    "Promotion",
    "Background Jobs",
    "Notifications",
    "Security",
    "Logging",
    "Monitoring",
    "Reporting",
    "Exports",
    "Feature Flags",
    "Performance",
    "Retention",
    "Developer Options",
]

# Seeded CONFIG-* entries with keys in document order
SEEDED = [
    ("CONFIG-APP-001", "APPLICATION_NAME"),
    ("CONFIG-APP-002", "APPLICATION_VERSION"),
    ("CONFIG-APP-003", "APPLICATION_ENVIRONMENT"),
    ("CONFIG-AUTH-001", "AUTH_PROVIDER"),
    ("CONFIG-AUTH-002", "AUTH_SESSION_TIMEOUT"),
    ("CONFIG-AUTH-003", "AUTH_REFRESH_WINDOW"),
    ("CONFIG-AUTH-004", "AUTH_MAX_LOGIN_ATTEMPTS"),
    ("CONFIG-PERM-001", "DEFAULT_USER_ROLE"),
    ("CONFIG-PERM-002", "ALLOW_ADMIN_OVERRIDE"),
    ("CONFIG-DB-001", "DATABASE_URL"),
    ("CONFIG-DB-002", "DATABASE_CONNECTION_POOL"),
    ("CONFIG-DB-003", "DATABASE_QUERY_TIMEOUT"),
    ("CONFIG-DB-004", "DATABASE_STATEMENT_TIMEOUT"),
    ("CONFIG-DB-005", "DATABASE_MAX_RETRIES"),
    ("CONFIG-STORAGE-001", "STORAGE_PROVIDER"),
    ("CONFIG-STORAGE-002", "STORAGE_BUCKET_SOURCE_IMAGES"),
    ("CONFIG-STORAGE-003", "STORAGE_SIGNED_URL_DURATION"),
    ("CONFIG-STORAGE-004", "STORAGE_MAX_FILE_SIZE"),
    ("CONFIG-STORAGE-005", "STORAGE_ALLOWED_IMAGE_TYPES"),
    ("CONFIG-UPLOAD-001", "UPLOAD_MAX_CONCURRENT_UPLOADS"),
    ("CONFIG-UPLOAD-002", "UPLOAD_SESSION_DURATION"),
    ("CONFIG-UPLOAD-003", "UPLOAD_ENABLE_DUPLICATE_DETECTION"),
    ("CONFIG-UPLOAD-004", "UPLOAD_HASH_ALGORITHM"),
    ("CONFIG-CLAIM-001", "CLAIM_DURATION"),
    ("CONFIG-CLAIM-002", "CLAIM_WARNING_THRESHOLD"),
    ("CONFIG-CLAIM-003", "CLAIM_ALLOW_RENEWAL"),
    ("CONFIG-CLAIM-004", "CLAIM_MAX_RENEWALS"),
    ("CONFIG-DRAFT-001", "DRAFT_AUTOSAVE_INTERVAL"),
    ("CONFIG-DRAFT-002", "DRAFT_RETENTION_PERIOD"),
    ("CONFIG-DRAFT-003", "DRAFT_LOCAL_RECOVERY_ENABLED"),
    ("CONFIG-MATCH-001", "MATCH_CONFIDENCE_THRESHOLD"),
    ("CONFIG-MATCH-002", "MATCH_MAX_CANDIDATES"),
    ("CONFIG-MATCH-003", "MATCH_REQUIRE_REVIEW_BELOW_THRESHOLD"),
    ("CONFIG-PROMOTION-001", "PROMOTION_MAX_RETRIES"),
    ("CONFIG-PROMOTION-002", "PROMOTION_RETRY_DELAY"),
    ("CONFIG-PROMOTION-003", "PROMOTION_REQUIRE_IDEMPOTENCY"),
    ("CONFIG-JOB-001", "JOB_MAX_ATTEMPTS"),
    ("CONFIG-JOB-002", "JOB_TIMEOUT"),
    ("CONFIG-JOB-003", "JOB_CONCURRENCY"),
    ("CONFIG-JOB-004", "JOB_BACKOFF_STRATEGY"),
    ("CONFIG-NOTIFY-001", "NOTIFICATION_EXPIRATION"),
    ("CONFIG-NOTIFY-002", "ENABLE_IN_APP_NOTIFICATIONS"),
    ("CONFIG-NOTIFY-003", "ENABLE_EMAIL_NOTIFICATIONS"),
    ("CONFIG-SECURITY-001", "ENABLE_CSRF_PROTECTION"),
    ("CONFIG-SECURITY-002", "ENABLE_RATE_LIMITING"),
    ("CONFIG-SECURITY-003", "MAX_REQUEST_SIZE"),
    ("CONFIG-SECURITY-004", "ENABLE_CONTENT_SECURITY_POLICY"),
    ("CONFIG-SECURITY-005", "ENABLE_SECURITY_HEADERS"),
    ("CONFIG-LOG-001", "LOG_LEVEL"),
    ("CONFIG-LOG-002", "LOG_RETENTION_DAYS"),
    ("CONFIG-LOG-003", "LOG_PII_REDACTION"),
    ("CONFIG-MONITOR-001", "ENABLE_HEALTH_ENDPOINT"),
    ("CONFIG-MONITOR-002", "HEALTH_CHECK_INTERVAL"),
    ("CONFIG-MONITOR-003", "ALERT_THRESHOLD_ERROR_RATE"),
    ("CONFIG-REPORT-001", "REPORT_MAX_ROWS"),
    ("CONFIG-REPORT-002", "REPORT_DEFAULT_PAGE_SIZE"),
    ("CONFIG-EXPORT-001", "EXPORT_MAX_ROWS"),
    ("CONFIG-EXPORT-002", "EXPORT_LINK_EXPIRATION"),
    ("CONFIG-EXPORT-003", "EXPORT_MAX_DOWNLOADS"),
]

FEATURE_FLAGS = [
    "FEATURE_ADVANCED_MATCHING",
    "FEATURE_BACKGROUND_PROMOTION",
    "FEATURE_BULK_EXPORT",
    "FEATURE_OPERATOR_DASHBOARD",
]

LOCKED = [
    "No production configuration key may exist outside this catalog or an approved amendment",
    "Configuration is external to application code",
    "Secrets never appear in logs, client bundles, or API responses",
    "Required secrets missing at startup fail startup",
    "Invalid enum values fail startup",
    "Unsupported providers fail startup",
    "Feature flags are temporary and must have removal targets",
    "Performance tuning must not alter business rules",
    "Retention durations are governed by the Data Retention Catalog",
    "AUTH_PROVIDER additions require catalog updates",
    "STORAGE_PROVIDER additions require catalog updates",
    "High-risk configuration changes require audit events",
    "Seeded configuration keys in this catalog are authoritative",
    "Exact production values may be environment-specific but must use cataloged keys",
    "Configuration must never require searching source code to understand",
]


def main() -> None:
    text = CAT4.read_text(encoding="utf-8")
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()

    for needle in [
        "PEOPLE-CATALOG-04-CONFIGURATION-1.0",
        "CONFIG-PRINCIPLE-001",
        "CONFIG-APP-001",
        "DATABASE_URL",
        "CLAIM_DURATION",
        "PEOPLE-CATALOG-05-PERMISSIONS-1.0",
        "Foundation Scope",
    ]:
        if needle not in text:
            raise SystemExit(f"Missing required string: {needle}")

    principles = [f"CONFIG-PRINCIPLE-{i:03d}" for i in range(1, 11)]
    for p in principles:
        if p not in text:
            raise SystemExit(f"Missing principle {p}")

    for category in CATEGORIES:
        if category not in text:
            raise SystemExit(f"Missing category: {category}")

    for config_id, key in SEEDED:
        if config_id not in text or key not in text:
            raise SystemExit(f"Missing config entry: {config_id} / {key}")

    for flag in FEATURE_FLAGS:
        if flag not in text:
            raise SystemExit(f"Missing feature flag example: {flag}")

    for decision in LOCKED:
        if decision not in text:
            raise SystemExit(f"Missing locked decision: {decision}")

    found_ids = sorted(set(re.findall(r"CONFIG-[A-Z]+-\d{3}", text)))
    entry_ids = [i for i in found_ids if not i.startswith("CONFIG-PRINCIPLE-")]
    expected_ids = [i for i, _ in SEEDED]
    if sorted(entry_ids) != sorted(expected_ids):
        raise SystemExit(
            f"Config ID mismatch: found={len(entry_ids)} expected={len(expected_ids)}"
        )

    registry = {
        "documentSetId": "PEOPLE-CATALOG-LIBRARY-1.0",
        "documentId": "PEOPLE-CATALOG-04-CONFIGURATION-1.0",
        "version": "1.0",
        "status": "DESIGN_COMPLETE_IMPLEMENTATION_NOT_AUTHORIZED",
        "scope": "FOUNDATION_CONTRACT_WITH_SEEDED_KEYS",
        "canonicalPath": str(CAT4.relative_to(ROOT)).replace("\\", "/"),
        "contentSha256": sha,
        "principleCount": 10,
        "principles": principles,
        "categoryCount": len(CATEGORIES),
        "categories": CATEGORIES,
        "seededConfigCount": len(SEEDED),
        "seededConfigs": [
            {"configId": cid, "configurationKey": key} for cid, key in SEEDED
        ],
        "featureFlagExamples": FEATURE_FLAGS,
        "lockedDecisionCount": len(LOCKED),
        "lockedDecisions": LOCKED,
        "overallReadinessPercent": 99,
        "nextCatalogId": "PEOPLE-CATALOG-05-PERMISSIONS-1.0",
        "prohibitions": [
            "No application source code",
            "No environment file creation for production secrets",
            "No dependency installation",
            "No deployment configuration implementation",
            "No feature-flag runtime wiring",
            "No inventing undocumented production configuration keys outside this catalog and its approved amendments",
        ],
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "catalog_04_configuration_registry.json").write_text(
        json.dumps(registry, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"principles=10 categories={len(CATEGORIES)} seeded={len(SEEDED)} "
        f"flags={len(FEATURE_FLAGS)} locked={len(LOCKED)} sha={sha[:12]}"
    )


if __name__ == "__main__":
    main()
