#!/usr/bin/env python3
"""Build Catalog 0 master registry and Catalog 1 state-machine registries."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "data" / "documentation"

CAT0 = ROOT / "docs" / "catalogs" / "catalog-00-master-registry" / "CATALOG_00_MASTER_REGISTRY.md"
CAT1 = ROOT / "docs" / "catalogs" / "catalog-01-state-machines" / "CATALOG_01_STATE_MACHINES.md"

CATALOG_SET = [
    {
        "catalogId": "PEOPLE-CATALOG-00-MASTER-REGISTRY-1.0",
        "sequence": 0,
        "title": "Master Catalog Registry",
        "status": "DESIGN_COMPLETE",
    },
    {
        "catalogId": "PEOPLE-CATALOG-01-STATE-MACHINES-1.0",
        "sequence": 1,
        "title": "State Machine Catalog",
        "status": "DESIGN_COMPLETE",
    },
    {
        "catalogId": "PEOPLE-CATALOG-02-ERRORS-1.0",
        "sequence": 2,
        "title": "Error Catalog",
        "status": "DESIGN_COMPLETE",
    },
    {
        "catalogId": "PEOPLE-CATALOG-03-AUDIT-EVENTS-1.0",
        "sequence": 3,
        "title": "Audit Event Catalog",
        "status": "DESIGN_COMPLETE",
    },
    {
        "catalogId": "PEOPLE-CATALOG-04-CONFIGURATION-1.0",
        "sequence": 4,
        "title": "Configuration Catalog",
        "status": "DESIGN_COMPLETE",
    },
    {
        "catalogId": "PEOPLE-CATALOG-05-PERMISSIONS-1.0",
        "sequence": 5,
        "title": "Permission and Authorization Catalog",
        "status": "DESIGN_COMPLETE",
    },
    {
        "catalogId": "PEOPLE-CATALOG-06-NOTIFICATIONS-1.0",
        "sequence": 6,
        "title": "Notification Catalog",
        "status": "DESIGN_COMPLETE",
    },
    {
        "catalogId": "PEOPLE-CATALOG-07-BACKGROUND-JOBS-1.0",
        "sequence": 7,
        "title": "Background Job Catalog",
        "status": "DESIGN_COMPLETE",
    },
    {
        "catalogId": "PEOPLE-CATALOG-08-DATA-RETENTION-1.0",
        "sequence": 8,
        "title": "Data Classification and Retention Catalog",
        "status": "DESIGN_COMPLETE",
    },
    {
        "catalogId": "PEOPLE-CATALOG-09-TRACEABILITY-1.0",
        "sequence": 9,
        "title": "Cross-Volume Traceability Matrix",
        "status": "DESIGN_COMPLETE",
    },
]

MACHINES = [
    ("STATE-USER-001", "Application User Lifecycle"),
    ("STATE-ROLE-001", "Role Grant Lifecycle"),
    ("STATE-BATCH-001", "Intake Batch Lifecycle"),
    ("STATE-PAGE-001", "Intake Page Lifecycle"),
    ("STATE-IMAGE-QUALITY-001", "Image Quality Lifecycle"),
    ("STATE-STORAGE-001", "Storage Object Lifecycle"),
    ("STATE-UPLOAD-001", "Upload Lifecycle"),
    ("STATE-QUEUE-001", "Queue Item Lifecycle"),
    ("STATE-CLAIM-001", "Work Claim Lifecycle"),
    ("STATE-DRAFT-001", "Draft Lifecycle"),
    ("STATE-ENTRY-001", "Intake Entry Lifecycle"),
    ("STATE-NORMALIZATION-001", "Normalization Run Lifecycle"),
    ("STATE-MATCH-EVAL-001", "Match Evaluation Lifecycle"),
    ("STATE-MATCH-RESOLUTION-001", "Match Resolution Workflow"),
    ("STATE-PROMOTION-001", "Promotion Request Lifecycle"),
    ("STATE-CANONICAL-LINK-001", "Canonical Person Link Lifecycle"),
    ("STATE-JOB-001", "Background Job Lifecycle"),
    ("STATE-ERROR-001", "Processing Error Lifecycle"),
    ("STATE-ALERT-001", "Alert Lifecycle"),
    ("STATE-IDEMPOTENCY-001", "Idempotency Record Lifecycle"),
    ("STATE-NOTIFICATION-001", "In-App Notification Lifecycle"),
    ("STATE-EXPORT-001", "Data Export Lifecycle"),
    ("STATE-ARCHIVE-001", "Archival Lifecycle"),
]

LOCKED = [
    "State transitions are server-enforced",
    "Every state uses a cataloged canonical key",
    "State history is preserved",
    "State transitions are concurrency-protected",
    "UI labels may differ from machine keys but not from their meaning",
    "Claim expiration does not erase drafts",
    "Source-image replacement does not erase original images",
    "Submission creates an immutable revision",
    "Corrections create new revisions",
    "Match evaluations are immutable after completion",
    "Match resolutions are versioned",
    "Candidate selection is not finalization",
    "Promotions are independently stateful from resolutions",
    "Promotion retries reuse idempotency identity",
    "Canonical links retain history",
    "Acknowledgment is not resolution",
    "Read notification is not acknowledgment",
    "Archive is not deletion",
    "Legal hold blocks destruction",
    "Terminal failure cannot be displayed as success",
    "No state transition may silently skip audit when audit is required",
    "No undocumented state may appear in production",
]


def sha_of(path: Path) -> str:
    return hashlib.sha256(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()


def main() -> None:
    text0 = CAT0.read_text(encoding="utf-8")
    text1 = CAT1.read_text(encoding="utf-8")

    for item in CATALOG_SET:
        if item["catalogId"] not in text0:
            raise SystemExit(f"Catalog 0 missing inventory id: {item['catalogId']}")

    machines = []
    for machine_id, title in MACHINES:
        if machine_id not in text1:
            raise SystemExit(f"Catalog 1 missing machine: {machine_id}")
        machines.append({"machineId": machine_id, "title": title})

    for decision in LOCKED:
        if decision not in text1:
            raise SystemExit(f"Missing locked decision: {decision}")

    deferred = sorted(set(re.findall(r"STATE-DEC-\d{3}", text1)))
    required_dec = [f"STATE-DEC-{i:03d}" for i in range(1, 11)]
    for d in required_dec:
        if d not in deferred:
            raise SystemExit(f"Missing deferred decision {d}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    master = {
        "documentSetId": "PEOPLE-CATALOG-LIBRARY-1.0",
        "documentId": "PEOPLE-CATALOG-00-MASTER-REGISTRY-1.0",
        "version": "1.0",
        "status": "DESIGN_COMPLETE_IMPLEMENTATION_NOT_AUTHORIZED",
        "canonicalPath": str(CAT0.relative_to(ROOT)).replace("\\", "/"),
        "contentSha256": sha_of(CAT0),
        "catalogCount": len(CATALOG_SET),
        "catalogs": CATALOG_SET,
        "nextCatalogId": "PEOPLE-CATALOG-LIBRARY-COMPLETE",
        "prohibitions": [
            "No application source code",
            "No API handlers or route implementations",
            "No database migrations or ORM models",
            "No React, JSX, TSX, or CSS implementation",
            "No undocumented enum, status, error, permission, audit, config, or job values in production code",
        ],
    }

    state_reg = {
        "documentSetId": "PEOPLE-CATALOG-LIBRARY-1.0",
        "documentId": "PEOPLE-CATALOG-01-STATE-MACHINES-1.0",
        "version": "1.0",
        "status": "DESIGN_COMPLETE_IMPLEMENTATION_NOT_AUTHORIZED",
        "canonicalPath": str(CAT1.relative_to(ROOT)).replace("\\", "/"),
        "contentSha256": sha_of(CAT1),
        "machineCount": len(machines),
        "machines": machines,
        "lockedDecisionCount": len(LOCKED),
        "lockedDecisions": LOCKED,
        "deferredDecisions": required_dec,
        "overallReadinessPercent": 99,
        "nextCatalogId": "PEOPLE-CATALOG-02-ERRORS-1.0",
    }

    (OUT_DIR / "catalog_00_master_registry.json").write_text(
        json.dumps(master, indent=2) + "\n", encoding="utf-8"
    )
    (OUT_DIR / "catalog_01_state_machine_registry.json").write_text(
        json.dumps(state_reg, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"catalogs={len(CATALOG_SET)} machines={len(machines)} "
        f"locked={len(LOCKED)} deferred={len(required_dec)}"
    )


if __name__ == "__main__":
    main()
