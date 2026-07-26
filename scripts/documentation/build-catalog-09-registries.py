#!/usr/bin/env python3
"""Build Catalog 9 traceability foundation registry."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "data" / "documentation"
CAT9 = ROOT / "docs" / "catalogs" / "catalog-09-traceability" / "CATALOG_09_TRACEABILITY.md"

LINK_NODES = [
    "LINK-BUSINESS-RULE",
    "LINK-STATE",
    "LINK-DATABASE",
    "LINK-API",
    "LINK-SCREEN",
    "LINK-COMPONENT",
    "LINK-PERMISSION",
    "LINK-AUDIT",
    "LINK-ERROR",
    "LINK-TEST",
    "LINK-PACKAGE",
    "LINK-JOB",
    "LINK-NOTIFICATION",
    "LINK-RETENTION",
    "LINK-CONFIG",
    "LINK-INTEGRATION",
]

STATUSES = [
    "UNMAPPED",
    "PARTIALLY_MAPPED",
    "FULLY_MAPPED",
    "VERIFIED",
    "BLOCKED",
    "NOT_APPLICABLE",
]

SEEDED = [
    ("TRACE-SEED-001", "REQ-GOV-001", "VERIFIED"),
    ("TRACE-SEED-002", "REQ-GOV-007", "VERIFIED"),
    ("TRACE-SEED-003", "REQ-GOV-008", "VERIFIED"),
    ("TRACE-SEED-004", "REQ-GOV-009", "VERIFIED"),
    ("TRACE-SEED-005", "REQ-GOV-010", "VERIFIED"),
    ("TRACE-SEED-006", "REQ-REPO-001", "FULLY_MAPPED"),
    ("TRACE-SEED-007", "REQ-REPO-005", "FULLY_MAPPED"),
    ("TRACE-SEED-008", "REQ-REPO-015", "FULLY_MAPPED"),
    ("TRACE-SEED-009", "REQ-CLAIM-ACQUIRE", "PARTIALLY_MAPPED"),
    ("TRACE-SEED-010", "REQ-GOV-CATALOG-LOCK", "VERIFIED"),
]

LOCKED = [
    "Traceability is bidirectional.",
    "Stable identifiers are mandatory.",
    "Critical orphans are prohibited for implementation-ready work.",
    "Catalogs 1–8 own operational language; Catalog 9 links them.",
    "Honesty over invented completeness.",
    "Every requirement row requires a source.",
    "Implementation readiness requires mapped tests (or explicit BLOCKED test plan).",
    "Privileged actions require Catalog 5 permissions.",
    "State mutations require Catalog 3 audit decisions or documented exceptions.",
    "Catalog Library remains locked at Catalogs 0–9.",
    "Seeded TRACE-SEED-* rows are authoritative starting points for amendment.",
    "DOC-0 Design Source Map and IS RTM are companions, not substitutes.",
    "`NOT_APPLICABLE` requires a written reason.",
    "Fabricating undocumented production keys to fill matrix cells is prohibited.",
    "Additional matrix rows and full inventories expand only via formal amendment or governed IS updates under this contract.",
]


def main() -> None:
    text = CAT9.read_text(encoding="utf-8")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    CAT9.write_bytes(text.encode("utf-8"))
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()

    for needle in [
        "PEOPLE-CATALOG-09-TRACEABILITY-1.0",
        "TRACE-PRINCIPLE-001",
        "Foundation Scope",
        "TRACE-SEED-001",
        "TRACE-SEED-010",
        "PAGE_CLAIM",
        "CLAIM_ALREADY_HELD",
        "CLAIM_ACQUIRED",
        "PEOPLE-CATALOG-LIBRARY-COMPLETE",
        "PEOPLE-IS-101-TECHNOLOGY-DECISION-SPECIFICATION-1.0",
    ]:
        if needle not in text:
            raise SystemExit(f"Missing required string: {needle}")

    principles = [f"TRACE-PRINCIPLE-{i:03d}" for i in range(1, 11)]
    for p in principles:
        if p not in text:
            raise SystemExit(f"Missing principle {p}")

    for node in LINK_NODES:
        if node not in text:
            raise SystemExit(f"Missing link node: {node}")

    for status in STATUSES:
        if status not in text:
            raise SystemExit(f"Missing status: {status}")

    for rid, req, status in SEEDED:
        if rid not in text or req not in text:
            raise SystemExit(f"Missing seeded row: {rid} / {req}")

    for decision in LOCKED:
        if decision not in text:
            raise SystemExit(f"Missing locked decision: {decision}")

    found = sorted(set(re.findall(r"TRACE-SEED-\d{3}", text)))
    expected = [i for i, _, _ in SEEDED]
    if found != sorted(expected):
        raise SystemExit(f"Seed ID mismatch: found={found} expected={sorted(expected)}")

    registry = {
        "documentSetId": "PEOPLE-CATALOG-LIBRARY-1.0",
        "documentId": "PEOPLE-CATALOG-09-TRACEABILITY-1.0",
        "version": "1.0",
        "status": "DESIGN_COMPLETE_IMPLEMENTATION_NOT_AUTHORIZED",
        "scope": "FOUNDATION_CONTRACT_WITH_SEEDED_MATRIX_ROWS",
        "canonicalPath": str(CAT9.relative_to(ROOT)).replace("\\", "/"),
        "contentSha256": sha,
        "principleCount": 10,
        "principles": principles,
        "linkNodeCount": len(LINK_NODES),
        "linkNodes": LINK_NODES,
        "statusVocabulary": STATUSES,
        "seededRowCount": len(SEEDED),
        "seededRows": [
            {"traceRowId": rid, "requirementId": req, "status": status}
            for rid, req, status in SEEDED
        ],
        "lockedDecisionCount": len(LOCKED),
        "lockedDecisions": LOCKED,
        "overallReadinessPercent": 98,
        "nextCatalogId": "PEOPLE-CATALOG-LIBRARY-COMPLETE",
        "prohibitions": [
            "No application source code",
            "No inventing undocumented production catalog keys to fill matrix cells",
            "No claiming system-wide FULLY_MAPPED or VERIFIED for unseeded domains",
            "No database migrations or runtime enforcement engines",
            "No dependency installation for application scaffolding",
            "No silent contradiction of Volumes 0-13 or Catalogs 0-8",
        ],
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "catalog_09_traceability_registry.json").write_text(
        json.dumps(registry, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    print(
        f"principles=10 nodes={len(LINK_NODES)} seeded={len(SEEDED)} "
        f"locked={len(LOCKED)} sha={sha[:12]}"
    )


if __name__ == "__main__":
    main()
