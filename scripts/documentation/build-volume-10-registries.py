#!/usr/bin/env python3
"""Extract Volume 10 endpoint inventory and write registries."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOL_PATH = (
    ROOT
    / "docs"
    / "volumes"
    / "volume-10-api-specifications"
    / "VOLUME_10_API_SPECIFICATIONS.md"
)
OUT_DIR = ROOT / "data" / "documentation"

# Explicit Owner inventory (method, path, group, notes)
ENDPOINTS = [
    ("GET", "/api/v1/session", "authentication", {"auth": True}),
    ("POST", "/api/v1/session/logout", "authentication", {"auth": True, "idempotent": True}),
    ("GET", "/api/v1/users/me", "users", {"auth": True}),
    ("GET", "/api/v1/users", "users", {"auth": True, "roles": ["ADMIN", "OWNER"], "paginated": True}),
    ("POST", "/api/v1/users", "users", {"auth": True, "roles": ["ADMIN", "OWNER"], "audit": True}),
    ("PATCH", "/api/v1/users/{id}", "users", {"auth": True, "concurrency": True, "audit": True}),
    ("GET", "/api/v1/users/{id}/roles", "roles", {"auth": True}),
    ("POST", "/api/v1/users/{id}/roles", "roles", {"auth": True, "audit": True}),
    ("DELETE", "/api/v1/users/{id}/roles/{role}", "roles", {"auth": True, "audit": True}),
    ("GET", "/api/v1/batches", "batches", {"auth": True, "paginated": True}),
    ("POST", "/api/v1/batches", "batches", {"auth": True, "audit": True, "idempotent": False}),
    ("GET", "/api/v1/batches/{id}", "batches", {"auth": True}),
    ("PATCH", "/api/v1/batches/{id}", "batches", {"auth": True, "concurrency": True}),
    ("GET", "/api/v1/pages/{id}", "pages", {"auth": True}),
    ("POST", "/api/v1/pages", "pages", {"auth": True}),
    ("PATCH", "/api/v1/pages/{id}", "pages", {"auth": True}),
    ("POST", "/api/v1/uploads", "images", {"auth": True}),
    ("POST", "/api/v1/uploads/{id}/complete", "images", {"auth": True, "idempotent": True}),
    ("GET", "/api/v1/images/{id}", "images", {"auth": True}),
    ("POST", "/api/v1/images/{id}/replace", "images", {"auth": True}),
    ("GET", "/api/v1/queue", "queue", {"auth": True, "paginated": True}),
    ("POST", "/api/v1/queue/{id}/claim", "queue", {"auth": True, "audit": True}),
    ("POST", "/api/v1/claims/{id}/renew", "queue", {"auth": True}),
    ("POST", "/api/v1/claims/{id}/release", "queue", {"auth": True, "audit": True}),
    ("GET", "/api/v1/drafts/{pageId}", "drafts", {"auth": True}),
    ("PUT", "/api/v1/drafts/{pageId}", "drafts", {"auth": True, "concurrency": True}),
    ("POST", "/api/v1/drafts/{pageId}/recover", "drafts", {"auth": True, "audit": True}),
    ("POST", "/api/v1/pages/{id}/submit", "transcription", {"auth": True, "idempotent": True, "audit": True}),
    ("GET", "/api/v1/entries/{id}", "transcription", {"auth": True}),
    ("GET", "/api/v1/entries/{id}/history", "transcription", {"auth": True}),
    ("POST", "/api/v1/entries/{id}/evaluate", "matching", {"auth": True}),
    ("GET", "/api/v1/match-evaluations/{id}", "matching", {"auth": True}),
    ("GET", "/api/v1/match-candidates/{id}", "matching", {"auth": True}),
    ("POST", "/api/v1/match-resolutions", "resolution", {"auth": True, "roles": ["REVIEWER"], "audit": True}),
    ("GET", "/api/v1/match-resolutions/{id}", "resolution", {"auth": True}),
    ("POST", "/api/v1/promotions", "promotion", {"auth": True, "idempotent": True, "audit": True}),
    ("GET", "/api/v1/promotions/{id}", "promotion", {"auth": True}),
    ("POST", "/api/v1/promotions/{id}/retry", "promotion", {"auth": True}),
    ("GET", "/api/v1/reports/batches", "reporting", {"auth": True}),
    ("GET", "/api/v1/reports/queue", "reporting", {"auth": True}),
    ("GET", "/api/v1/reports/errors", "reporting", {"auth": True}),
    ("GET", "/api/v1/reports/operators", "reporting", {"auth": True}),
    ("GET", "/api/v1/audit", "audit", {"auth": True, "roles": ["ADMIN"]}),
    ("GET", "/api/v1/audit/{id}", "audit", {"auth": True, "roles": ["ADMIN"]}),
]

ERROR_CODES = [
    "AUTH_REQUIRED",
    "ACCESS_DENIED",
    "VALIDATION_FAILED",
    "CLAIM_ALREADY_HELD",
    "CLAIM_EXPIRED",
    "STALE_VERSION",
    "NOT_FOUND",
    "UPLOAD_FAILED",
    "MATCH_CONFLICT",
    "PROMOTION_FAILED",
    "IDEMPOTENCY_CONFLICT",
    "RATE_LIMITED",
    "SYSTEM_ERROR",
]


def main() -> None:
    text = VOL_PATH.read_text(encoding="utf-8")
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()

    principles = sorted(set(re.findall(r"API-PRINCIPLE-\d{3}", text)))
    required_principles = [f"API-PRINCIPLE-{i:03d}" for i in range(1, 6)]
    for p in required_principles:
        if p not in principles:
            raise SystemExit(f"Missing principle {p}")

    for method, path, _group, _meta in ENDPOINTS:
        heading = f"## {method} {path}"
        if heading not in text and f"{method} {path}" not in text:
            raise SystemExit(f"Endpoint missing from volume text: {method} {path}")

    for code in ERROR_CODES:
        if code not in text:
            raise SystemExit(f"Error code missing: {code}")

    endpoint_rows = []
    for method, path, group, meta in ENDPOINTS:
        endpoint_rows.append(
            {
                "method": method,
                "path": path,
                "group": group,
                "requiresAuth": bool(meta.get("auth", True)),
                "idempotent": meta.get("idempotent"),
                "requiresConcurrency": bool(meta.get("concurrency", False)),
                "auditRequired": bool(meta.get("audit", False)),
                "roles": meta.get("roles", []),
                "paginated": bool(meta.get("paginated", False)),
            }
        )

    registry = {
        "documentId": "PEOPLE-VOLUME-10-API-SPECIFICATIONS-1.0",
        "version": "1.0",
        "status": "DESIGN_COMPLETE_IMPLEMENTATION_NOT_AUTHORIZED",
        "canonicalPath": str(VOL_PATH.relative_to(ROOT)).replace("\\", "/"),
        "contentSha256": sha,
        "apiPrefix": "/api/v1/",
        "principles": required_principles,
        "lockedDecisionCount": 20,
        "endpointCount": len(endpoint_rows),
        "endpoints": endpoint_rows,
        "errorCodes": ERROR_CODES,
        "prohibitions": [
            "No route handlers",
            "No framework code",
            "No controller logic",
            "No ORM code",
            "No SQL",
            "No SDK implementation",
            "No HTTP library choice",
            "No production deployment",
        ],
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "volume_10_endpoint_registry.json").write_text(
        json.dumps(registry, indent=2) + "\n", encoding="utf-8"
    )
    print(f"endpoints={len(endpoint_rows)} principles={len(principles)} sha={sha[:12]}")


if __name__ == "__main__":
    main()
