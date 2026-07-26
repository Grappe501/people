#!/usr/bin/env python3
"""Extract Volume 13 platform standards inventory and write registries."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOL_PATH = (
    ROOT
    / "docs"
    / "volumes"
    / "volume-13-platform-standards"
    / "VOLUME_13_CANONICAL_PLATFORM_STANDARDS.md"
)
OUT_DIR = ROOT / "data" / "documentation"

STANDARD_AREAS = [
    "Repository Standards",
    "Configuration",
    "Architecture",
    "Authentication",
    "Authorization",
    "Data Protection",
    "Database Governance",
    "API Governance",
    "UI Governance",
    "Security",
    "Testing",
    "Deployment",
    "Documentation",
    "Implementation Governance",
]

LOCKED_DECISIONS = [
    "Documentation-first development",
    "Business rules belong in the domain layer",
    "Authentication and authorization remain separate concerns",
    "Original source images are immutable",
    "Audit history is append-only",
    "Canonical identity ownership remains outside People Intake",
    "APIs are contract-driven",
    "Database changes require migrations",
    "Components are reused rather than duplicated",
    "Accessibility is mandatory",
    "Responsive design is mandatory",
    "Server-side authorization is required",
    "Secrets never enter source control",
    "Idempotent operations remain idempotent",
    "High-risk actions remain auditable",
    "Documentation stays synchronized with implementation",
    "All project-controlled artifacts remain under the approved project workspace",
    "Every implementation package must end with validation and documentation updates",
]

NEXT_DOCUMENTS = [
    {
        "documentId": "PEOPLE-STATE-MACHINE-CATALOG-1.0",
        "title": "State Machine Catalog",
        "sequence": 1,
    },
    {
        "documentId": "PEOPLE-ERROR-CATALOG-1.0",
        "title": "Error Catalog",
        "sequence": 2,
    },
    {
        "documentId": "PEOPLE-AUDIT-EVENT-CATALOG-1.0",
        "title": "Audit Event Catalog",
        "sequence": 3,
    },
    {
        "documentId": "PEOPLE-CONFIGURATION-CATALOG-1.0",
        "title": "Configuration Catalog",
        "sequence": 4,
    },
    {
        "documentId": "PEOPLE-CROSS-VOLUME-TRACEABILITY-MATRIX-1.0",
        "title": "Cross-Volume Traceability Matrix",
        "sequence": 5,
    },
    {
        "documentId": "PEOPLE-IMPLEMENTATION-PACKAGE-LIBRARY-1.0",
        "title": "Implementation Package Library",
        "sequence": 6,
    },
]


def main() -> None:
    text = VOL_PATH.read_text(encoding="utf-8")
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()

    for area in STANDARD_AREAS:
        if area not in text:
            raise SystemExit(f"Missing standard area: {area}")

    for decision in LOCKED_DECISIONS:
        if decision not in text:
            raise SystemExit(f"Missing locked decision: {decision}")

    for doc in NEXT_DOCUMENTS:
        if doc["title"] not in text:
            raise SystemExit(f"Missing next document title: {doc['title']}")

    required = [
        "PEOPLE-VOLUME-13-CANONICAL-PLATFORM-STANDARDS-1.0",
        "PEOPLE-STATE-MACHINE-CATALOG-1.0",
        "H:\\people",
        "No application source code",
    ]
    for needle in required:
        if needle not in text:
            raise SystemExit(f"Missing required string: {needle}")

    registry = {
        "documentId": "PEOPLE-VOLUME-13-CANONICAL-PLATFORM-STANDARDS-1.0",
        "version": "1.0",
        "status": "DESIGN_COMPLETE_IMPLEMENTATION_NOT_AUTHORIZED",
        "canonicalPath": str(VOL_PATH.relative_to(ROOT)).replace("\\", "/"),
        "contentSha256": sha,
        "projectRoot": "H:\\people",
        "lockedDecisionCount": len(LOCKED_DECISIONS),
        "lockedDecisions": LOCKED_DECISIONS,
        "standardAreaCount": len(STANDARD_AREAS),
        "standardAreas": STANDARD_AREAS,
        "nextGoverningDocuments": NEXT_DOCUMENTS,
        "overallReadinessPercent": 100,
        "prohibitions": [
            "No application source code under src/",
            "No API handlers or route implementations",
            "No database migrations or ORM models",
            "No React, JSX, TSX, or CSS implementation",
            "No dependency installation for runtime application stacks",
            "No production deployment",
            "No secrets committed to the repository",
        ],
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "volume_13_platform_registry.json").write_text(
        json.dumps(registry, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"areas={len(STANDARD_AREAS)} locked={len(LOCKED_DECISIONS)} "
        f"next={len(NEXT_DOCUMENTS)} sha={sha[:12]}"
    )


if __name__ == "__main__":
    main()
