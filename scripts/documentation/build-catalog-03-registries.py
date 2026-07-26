#!/usr/bin/env python3
"""Build Catalog 3 audit-event foundation registry."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "data" / "documentation"
CAT3 = ROOT / "docs" / "catalogs" / "catalog-03-audit-events" / "CATALOG_03_AUDIT_EVENTS.md"

DOMAINS = [
    "AUTHENTICATION",
    "USER_MANAGEMENT",
    "ROLE_MANAGEMENT",
    "BATCH",
    "PAGE",
    "UPLOAD",
    "IMAGE",
    "QUEUE",
    "CLAIM",
    "DRAFT",
    "TRANSCRIPTION",
    "MATCHING",
    "RESOLUTION",
    "PROMOTION",
    "CANONICAL_INTEGRATION",
    "BACKGROUND_JOBS",
    "REPORTING",
    "EXPORT",
    "CONFIGURATION",
    "SECURITY",
    "AUDIT",
    "SYSTEM",
]

SEEDED_EVENTS = [
    {"eventId": "AUDIT-USER-001", "canonicalName": "USER_INVITED", "domain": "USER_MANAGEMENT"},
    {"eventId": "AUDIT-CLAIM-001", "canonicalName": "CLAIM_ACQUIRED", "domain": "CLAIM"},
    {"eventId": "AUDIT-PAGE-001", "canonicalName": "PAGE_SUBMITTED", "domain": "PAGE"},
    {"eventId": "AUDIT-MATCH-001", "canonicalName": "MATCH_RESOLUTION_FINALIZED", "domain": "RESOLUTION"},
    {"eventId": "AUDIT-PROMOTION-001", "canonicalName": "PROMOTION_SUCCEEDED", "domain": "PROMOTION"},
    {"eventId": "AUDIT-SECURITY-001", "canonicalName": "SECURITY_ACCESS_DENIED", "domain": "SECURITY"},
]

LOCKED = [
    "Audit records are append-only",
    "Released canonical event names are permanent",
    "Every significant auditable action requires a cataloged event",
    "Audit is for accountability and investigation, not primary business logic",
    "Every event carries a correlation identifier",
    "Every event is attributed to a human or system actor",
    "Secrets and tokens never appear in audit payloads",
    "Full source images never appear in audit payloads",
    "Metadata prefers references over copies of personal data",
    "Event types are versioned",
    "Privacy classification is required on each event definition",
    "Retention class is assigned via the Retention Catalog",
    "Seeded example events in this catalog are authoritative",
    "Additional events require formal catalog amendment under this contract",
    "No audit implementation may invent undocumented production event names",
]


def main() -> None:
    text = CAT3.read_text(encoding="utf-8")
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()

    for needle in [
        "PEOPLE-CATALOG-03-AUDIT-EVENTS-1.0",
        "AUDIT-PRINCIPLE-001",
        "PEOPLE-CATALOG-04-CONFIGURATION-1.0",
        "Foundation Scope",
    ]:
        if needle not in text:
            raise SystemExit(f"Missing required string: {needle}")

    principles = [f"AUDIT-PRINCIPLE-{i:03d}" for i in range(1, 11)]
    for p in principles:
        if p not in text:
            raise SystemExit(f"Missing principle {p}")

    for domain in DOMAINS:
        if domain not in text:
            raise SystemExit(f"Missing domain: {domain}")

    for event in SEEDED_EVENTS:
        if event["eventId"] not in text or event["canonicalName"] not in text:
            raise SystemExit(f"Missing seeded event: {event}")

    for decision in LOCKED:
        if decision not in text:
            raise SystemExit(f"Missing locked decision: {decision}")

    registry = {
        "documentSetId": "PEOPLE-CATALOG-LIBRARY-1.0",
        "documentId": "PEOPLE-CATALOG-03-AUDIT-EVENTS-1.0",
        "version": "1.0",
        "status": "DESIGN_COMPLETE_IMPLEMENTATION_NOT_AUTHORIZED",
        "scope": "FOUNDATION_CONTRACT_WITH_SEEDED_EVENTS",
        "canonicalPath": str(CAT3.relative_to(ROOT)).replace("\\", "/"),
        "contentSha256": sha,
        "principleCount": 10,
        "principles": principles,
        "domainCount": len(DOMAINS),
        "domains": DOMAINS,
        "seededEventCount": len(SEEDED_EVENTS),
        "seededEvents": SEEDED_EVENTS,
        "lockedDecisionCount": len(LOCKED),
        "lockedDecisions": LOCKED,
        "overallReadinessPercent": 98,
        "nextCatalogId": "PEOPLE-CATALOG-04-CONFIGURATION-1.0",
        "prohibitions": [
            "No audit persistence implementation",
            "No database migrations",
            "No API handlers or middleware",
            "No logging or alerting implementation",
            "No UI components",
            "No dependency installation",
            "No production audit payloads",
            "No inventing undocumented production event names outside this catalog and its approved amendments",
        ],
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "catalog_03_audit_event_registry.json").write_text(
        json.dumps(registry, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"principles=10 domains={len(DOMAINS)} seeded={len(SEEDED_EVENTS)} "
        f"locked={len(LOCKED)} sha={sha[:12]}"
    )


if __name__ == "__main__":
    main()
