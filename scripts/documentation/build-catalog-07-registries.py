#!/usr/bin/env python3
"""Build Catalog 7 background job foundation registry."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "data" / "documentation"
CAT7 = ROOT / "docs" / "catalogs" / "catalog-07-background-jobs" / "CATALOG_07_BACKGROUND_JOBS.md"

CATEGORIES = [
    "Upload",
    "Storage",
    "Image Processing",
    "Claims",
    "Draft Recovery",
    "Transcription",
    "Normalization",
    "Matching",
    "Promotion",
    "Notification",
    "Reporting",
    "Export",
    "Retention",
    "Audit",
    "Maintenance",
    "Security",
    "System",
]

PRIORITIES = ["LOW", "NORMAL", "HIGH", "CRITICAL"]
CONCURRENCY = ["Single Instance", "Per Resource", "Per Batch", "Per User", "Unlimited"]
RETRIES = [
    "No Retry",
    "Immediate Retry",
    "Exponential Backoff",
    "Manual Retry",
    "Operator Review Required",
]
TRIGGERS = [
    "API Request",
    "State Transition",
    "Scheduled Execution",
    "Queue Availability",
    "Prior Job Completion",
    "Administrator Request",
    "Startup Recovery",
]

SEEDED = [
    ("JOB-UPLOAD-001", "UPLOAD_VERIFICATION"),
    ("JOB-IMAGE-001", "IMAGE_PREVIEW_GENERATION"),
    ("JOB-CLAIM-001", "CLAIM_EXPIRATION_CHECK"),
    ("JOB-DRAFT-001", "DRAFT_RECOVERY_SCAN"),
    ("JOB-NORMALIZATION-001", "ENTRY_NORMALIZATION"),
    ("JOB-MATCH-001", "MATCH_EVALUATION"),
    ("JOB-PROMOTION-001", "PROMOTION_EXECUTION"),
    ("JOB-NOTIFY-001", "NOTIFICATION_DISPATCH"),
    ("JOB-REPORT-001", "REPORT_GENERATION"),
    ("JOB-EXPORT-001", "EXPORT_GENERATION"),
    ("JOB-RETENTION-001", "RETENTION_EXPIRATION"),
    ("JOB-AUDIT-001", "AUDIT_INTEGRITY_CHECK"),
    ("JOB-MAINT-001", "SYSTEM_HEALTH_CHECK"),
]

LOCKED = [
    "No production background job may exist outside this catalog or an approved amendment.",
    "Jobs must never depend on UI state or browser sessions.",
    "Retries must never create duplicate business results.",
    "Jobs that modify canonical data always require idempotency.",
    "Failed jobs never silently disappear.",
    "Priority affects scheduling only and does not bypass authorization.",
    "Jobs execute under service identities, not interactive user sessions.",
    "Dependency failures must be explicit.",
    "Seeded job names in this catalog are authoritative permanent identifiers.",
    "Promotion execution must be idempotent, transactional, and audited.",
    "Configurable timeouts and concurrency use Catalog 4 keys; they do not invent new job types.",
    "Notification dispatch jobs must honor Catalog 6 recipient and privacy rules.",
    "Retention jobs defer classification durations to Catalog 8.",
    "Material job lifecycle events require Catalog 3 audit linkage where required.",
    "Additional job types require catalog amendment under this contract.",
]


def main() -> None:
    text = CAT7.read_text(encoding="utf-8")
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()

    for needle in [
        "PEOPLE-CATALOG-07-BACKGROUND-JOBS-1.0",
        "JOB-PRINCIPLE-001",
        "UPLOAD_VERIFICATION",
        "PROMOTION_EXECUTION",
        "Foundation Scope",
        "PEOPLE-CATALOG-08-DATA-RETENTION-1.0",
    ]:
        if needle not in text:
            raise SystemExit(f"Missing required string: {needle}")

    principles = [f"JOB-PRINCIPLE-{i:03d}" for i in range(1, 11)]
    for p in principles:
        if p not in text:
            raise SystemExit(f"Missing principle {p}")

    for category in CATEGORIES:
        if category not in text:
            raise SystemExit(f"Missing category: {category}")

    for item in PRIORITIES + CONCURRENCY + RETRIES + TRIGGERS:
        if item not in text:
            raise SystemExit(f"Missing catalog value: {item}")

    for job_id, name in SEEDED:
        if job_id not in text or name not in text:
            raise SystemExit(f"Missing job: {job_id} / {name}")

    for decision in LOCKED:
        if decision not in text:
            raise SystemExit(f"Missing locked decision: {decision}")

    found = sorted(set(re.findall(r"JOB-[A-Z]+-\d{3}", text)))
    entry_ids = [i for i in found if not i.startswith("JOB-PRINCIPLE-")]
    # Also filter JOBCAT if any matched - JOBCAT doesn't match JOB-[A-Z]+-\d{3} the same... JOBCAT-001 is JOBCAT not JOB-
    # JOBPRI wouldn't match. Good.
    # JOB-PRINCIPLE filtered. But JOBCAT pattern is different.
    expected = [i for i, _ in SEEDED]
    if sorted(entry_ids) != sorted(expected):
        raise SystemExit(
            f"Job ID mismatch: found={sorted(entry_ids)} expected={sorted(expected)}"
        )

    registry = {
        "documentSetId": "PEOPLE-CATALOG-LIBRARY-1.0",
        "documentId": "PEOPLE-CATALOG-07-BACKGROUND-JOBS-1.0",
        "version": "1.0",
        "status": "DESIGN_COMPLETE_IMPLEMENTATION_NOT_AUTHORIZED",
        "scope": "FOUNDATION_CONTRACT_WITH_SEEDED_JOBS",
        "canonicalPath": str(CAT7.relative_to(ROOT)).replace("\\", "/"),
        "contentSha256": sha,
        "principleCount": 10,
        "principles": principles,
        "categoryCount": len(CATEGORIES),
        "categories": CATEGORIES,
        "priorityCount": len(PRIORITIES),
        "priorities": PRIORITIES,
        "concurrencyPolicyCount": len(CONCURRENCY),
        "concurrencyPolicies": CONCURRENCY,
        "retryPolicyCount": len(RETRIES),
        "retryPolicies": RETRIES,
        "triggerCount": len(TRIGGERS),
        "triggers": TRIGGERS,
        "seededJobCount": len(SEEDED),
        "seededJobs": [{"jobId": jid, "canonicalName": name} for jid, name in SEEDED],
        "lockedDecisionCount": len(LOCKED),
        "lockedDecisions": LOCKED,
        "overallReadinessPercent": 99,
        "nextCatalogId": "PEOPLE-CATALOG-08-DATA-RETENTION-1.0",
        "prohibitions": [
            "No application source code",
            "No worker, queue, or scheduler implementation",
            "No database migrations for job tables",
            "No cron or Netlify scheduled-function wiring",
            "No dependency installation",
            "No inventing undocumented production job names outside this catalog and its approved amendments",
        ],
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "catalog_07_background_jobs_registry.json").write_text(
        json.dumps(registry, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"principles=10 categories={len(CATEGORIES)} seeded={len(SEEDED)} "
        f"locked={len(LOCKED)} sha={sha[:12]}"
    )


if __name__ == "__main__":
    main()
