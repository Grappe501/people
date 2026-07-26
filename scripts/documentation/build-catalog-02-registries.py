#!/usr/bin/env python3
"""Build Catalog 2 error registry and refresh Catalog 0 inventory status."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "data" / "documentation"
CAT2 = ROOT / "docs" / "catalogs" / "catalog-02-errors" / "CATALOG_02_ERRORS.md"

LOCKED = [
    "Production errors use cataloged stable codes",
    "User messages never expose secrets or stack traces",
    "Every significant error includes a correlation ID",
    "Validation errors preserve user input",
    "Claim expiration preserves drafts",
    "Draft save failure must not clear visible entries",
    "Normalization failure never changes raw transcription",
    "Match failure preserves prior evaluations",
    "Resolution failure preserves finalized history",
    "Promotion failure preserves the approved resolution",
    "Canonical uncertainty blocks unsafe retry",
    "Idempotency-result uncertainty requires operator review",
    "Audit failure rolls back any action requiring atomic audit",
    "Acknowledging an error does not resolve it",
    "A read notification does not resolve an error",
    "Retry guidance appears only when retry is safe",
    "Technical failures remain distinct from valid business conditions",
    "Queue empty is not treated as a system failure",
    "Claim collision is not treated as a system failure",
    "Unknown data is never converted to No because of an error",
    "Personal information is minimized in logs",
    "Source images are never logged",
    "Alerts are created according to catalog policy",
    "Critical integrity errors cannot be shown as success",
    "Error handling must be tested",
    "The UI must tell users whether their work was preserved",
    "Unsupported machine values are rejected",
    "Repeated errors follow deduplication policy",
    "Security errors always use safe, minimal user messages",
    "No undocumented production error code is allowed",
]

FAMILIES_START = "# PART LI — ERROR REGISTRY"
FAMILIES_END = "# PART LII — LOCKED ERROR DECISIONS"


def sha_of(path: Path) -> str:
    return hashlib.sha256(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()


def extract_family_codes(text: str) -> list[str]:
    start = text.find(FAMILIES_START)
    end = text.find(FAMILIES_END)
    if start < 0 or end < 0 or end <= start:
        raise SystemExit("Could not locate Part LI family registry section")
    section = text[start:end]
    codes = re.findall(r"^([A-Z][A-Z0-9_]+)$", section, flags=re.M)
    # de-dupe preserving order
    seen = set()
    out = []
    for c in codes:
        if c in seen:
            continue
        seen.add(c)
        out.append(c)
    return out


def main() -> None:
    text = CAT2.read_text(encoding="utf-8")
    for needle in [
        "PEOPLE-CATALOG-02-ERRORS-1.0",
        "ERROR-PRINCIPLE-001",
        "ERROR-AUTH-001",
        "CLAIM_ALREADY_HELD",
        "PROMOTION_IDEMPOTENCY_MISSING",
        "ERROR-DEC-012",
        "PEOPLE-CATALOG-03-AUDIT-EVENTS-1.0",
        "No undocumented production error code",
    ]:
        if needle not in text:
            raise SystemExit(f"Missing required string: {needle}")

    all_ids = sorted(set(re.findall(r"ERROR-[A-Z]+-\d{3}", text)))
    entry_ids = [i for i in all_ids if not i.startswith("ERROR-PRINCIPLE-") and not i.startswith("ERROR-DEC-")]
    if len(entry_ids) != 154:
        raise SystemExit(f"Expected 154 error entry IDs, found {len(entry_ids)}")

    principles = [f"ERROR-PRINCIPLE-{i:03d}" for i in range(1, 11)]
    for p in principles:
        if p not in text:
            raise SystemExit(f"Missing principle {p}")

    deferred = [f"ERROR-DEC-{i:03d}" for i in range(1, 13)]
    for d in deferred:
        if d not in text:
            raise SystemExit(f"Missing deferred {d}")

    for decision in LOCKED:
        if decision not in text:
            raise SystemExit(f"Missing locked decision: {decision}")

    codes = extract_family_codes(text)
    if len(codes) != 154:
        raise SystemExit(f"Expected 154 family codes, found {len(codes)}")

    registry = {
        "documentSetId": "PEOPLE-CATALOG-LIBRARY-1.0",
        "documentId": "PEOPLE-CATALOG-02-ERRORS-1.0",
        "version": "1.0",
        "status": "DESIGN_COMPLETE_IMPLEMENTATION_NOT_AUTHORIZED",
        "canonicalPath": str(CAT2.relative_to(ROOT)).replace("\\", "/"),
        "contentSha256": sha_of(CAT2),
        "principleCount": 10,
        "principles": principles,
        "errorEntryCount": len(entry_ids),
        "errorEntryIds": entry_ids,
        "canonicalCodeCount": len(codes),
        "canonicalCodes": codes,
        "lockedDecisionCount": 30,
        "lockedDecisions": LOCKED,
        "deferredDecisions": deferred,
        "overallReadinessPercent": 99,
        "nextCatalogId": "PEOPLE-CATALOG-03-AUDIT-EVENTS-1.0",
        "prohibitions": [
            "No error classes",
            "No route handlers",
            "No logging implementation",
            "No alerting implementation",
            "No database migrations",
            "No API middleware",
            "No monitoring configuration",
            "No UI components",
            "No retry workers",
            "No dependency installation",
            "No production error messages",
        ],
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "catalog_02_error_registry.json").write_text(
        json.dumps(registry, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"entries={len(entry_ids)} codes={len(codes)} "
        f"principles=10 deferred=12 locked=30 sha={registry['contentSha256'][:12]}"
    )


if __name__ == "__main__":
    main()
