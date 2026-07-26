#!/usr/bin/env python3
"""Build Catalog 8 data retention foundation registry."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "data" / "documentation"
CAT8 = ROOT / "docs" / "catalogs" / "catalog-08-data-retention" / "CATALOG_08_DATA_RETENTION.md"

CLASSIFICATIONS = [
    "PUBLIC",
    "INTERNAL",
    "CONFIDENTIAL",
    "RESTRICTED",
    "SYSTEM_SECRET",
]

DOMAINS = [
    "Users",
    "Roles",
    "Authentication",
    "Audit",
    "Configuration",
    "Uploads",
    "Images",
    "Batches",
    "Pages",
    "Claims",
    "Drafts",
    "Transcription",
    "Normalization",
    "Matching",
    "Resolution",
    "Promotion",
    "Reports",
    "Exports",
    "Notifications",
    "Jobs",
    "Logs",
    "System Metadata",
]

STATES = [
    "ACTIVE",
    "ARCHIVED",
    "LEGAL_HOLD",
    "PENDING_DESTRUCTION",
    "DESTROYED",
]

SEEDED = [
    ("RETAIN-AUDIT-001", "Audit Records"),
    ("RETAIN-DRAFT-001", "Drafts"),
    ("RETAIN-IMAGE-001", "Uploaded Images"),
    ("RETAIN-SECRET-001", "Authentication Secrets"),
]

LOCKED = [
    "No persistent data may exist without a documented lifecycle.",
    "Information is classified before durable storage.",
    "Retention policies are deterministic and consistently enforced.",
    "Legal hold prohibits destruction and suspends retention timers.",
    "Destruction must be irreversible when required by policy.",
    "Not all destroyed data is recoverable.",
    "Archived data remains protected according to its classification.",
    "Existing data must not silently change lifecycle rules.",
    "SYSTEM_SECRET data is not archived into ordinary archival stores.",
    "Seeded retention examples in this catalog are authoritative starting points for amendment.",
    "Exact durations may use Catalog 4 keys but must map to cataloged retention entries.",
    "Classification does not grant access; Catalog 5 remains authoritative for authorization.",
    "Completed retention destruction cannot be overridden administratively.",
    "Material lifecycle events require Catalog 3 audit linkage where required.",
    "Additional classification levels and retention rules require catalog amendment under this contract.",
]


def main() -> None:
    text = CAT8.read_text(encoding="utf-8")
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()

    for needle in [
        "PEOPLE-CATALOG-08-DATA-RETENTION-1.0",
        "RETAIN-PRINCIPLE-001",
        "SYSTEM_SECRET",
        "LEGAL_HOLD",
        "RETAIN-AUDIT-001",
        "Foundation Scope",
        "PEOPLE-CATALOG-09-TRACEABILITY-1.0",
    ]:
        if needle not in text:
            raise SystemExit(f"Missing required string: {needle}")

    principles = [f"RETAIN-PRINCIPLE-{i:03d}" for i in range(1, 11)]
    for p in principles:
        if p not in text:
            raise SystemExit(f"Missing principle {p}")

    for classification in CLASSIFICATIONS:
        if classification not in text:
            raise SystemExit(f"Missing classification: {classification}")

    for domain in DOMAINS:
        if domain not in text:
            raise SystemExit(f"Missing domain: {domain}")

    for state in STATES:
        if state not in text:
            raise SystemExit(f"Missing retention state: {state}")

    for rid, label in SEEDED:
        if rid not in text or label not in text:
            raise SystemExit(f"Missing retention example: {rid} / {label}")

    for decision in LOCKED:
        if decision not in text:
            raise SystemExit(f"Missing locked decision: {decision}")

    found = sorted(set(re.findall(r"RETAIN-[A-Z]+-\d{3}", text)))
    entry_ids = [i for i in found if not i.startswith("RETAIN-PRINCIPLE-")]
    expected = [i for i, _ in SEEDED]
    if sorted(entry_ids) != sorted(expected):
        raise SystemExit(
            f"Retention ID mismatch: found={sorted(entry_ids)} expected={sorted(expected)}"
        )

    registry = {
        "documentSetId": "PEOPLE-CATALOG-LIBRARY-1.0",
        "documentId": "PEOPLE-CATALOG-08-DATA-RETENTION-1.0",
        "version": "1.0",
        "status": "DESIGN_COMPLETE_IMPLEMENTATION_NOT_AUTHORIZED",
        "scope": "FOUNDATION_CONTRACT_WITH_SEEDED_RETENTION_RULES",
        "canonicalPath": str(CAT8.relative_to(ROOT)).replace("\\", "/"),
        "contentSha256": sha,
        "principleCount": 10,
        "principles": principles,
        "classificationCount": len(CLASSIFICATIONS),
        "classifications": CLASSIFICATIONS,
        "domainCount": len(DOMAINS),
        "domains": DOMAINS,
        "retentionStateCount": len(STATES),
        "retentionStates": STATES,
        "seededRetentionCount": len(SEEDED),
        "seededRetentionRules": [
            {"retentionId": rid, "label": label} for rid, label in SEEDED
        ],
        "lockedDecisionCount": len(LOCKED),
        "lockedDecisions": LOCKED,
        "overallReadinessPercent": 99,
        "nextCatalogId": "PEOPLE-CATALOG-09-TRACEABILITY-1.0",
        "prohibitions": [
            "No application source code",
            "No archival or destruction workers",
            "No database migrations for retention tables",
            "No production data deletion",
            "No dependency installation",
            "No inventing undocumented production retention rules or classification levels outside this catalog and its approved amendments",
        ],
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "catalog_08_data_retention_registry.json").write_text(
        json.dumps(registry, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"principles=10 classifications={len(CLASSIFICATIONS)} domains={len(DOMAINS)} "
        f"states={len(STATES)} seeded={len(SEEDED)} locked={len(LOCKED)} sha={sha[:12]}"
    )


if __name__ == "__main__":
    main()
