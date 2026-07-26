#!/usr/bin/env python3
"""Extract Volume 9 table/principle/decision IDs and write registries."""
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
    / "volume-09-database-specifications"
    / "VOLUME_09_DATABASE_SPECIFICATIONS.md"
)
OUT_DIR = ROOT / "data" / "documentation"

CANONICAL_TABLES = [
    "application_users",
    "user_roles",
    "user_role_history",
    "user_access_events",
    "intake_batches",
    "intake_batch_status_history",
    "intake_pages",
    "intake_page_status_history",
    "intake_entries",
    "entry_submission_revisions",
    "intake_entry_fields",
    "entry_field_revision_history",
    "storage_objects",
    "source_images",
    "image_access_events",
    "upload_sessions",
    "upload_attempts",
    "work_queue_items",
    "work_claims",
    "claim_history",
    "page_drafts",
    "page_draft_revisions",
    "normalization_runs",
    "normalized_entry_fields",
    "match_evaluations",
    "match_candidates",
    "match_signals",
    "match_evaluation_warnings",
    "match_resolutions",
    "duplicate_entry_links",
    "resolution_status_history",
    "promotion_requests",
    "promotion_attempts",
    "canonical_person_links",
    "canonical_attribute_contributions",
    "provenance_records",
    "provenance_links",
    "audit_events",
    "background_jobs",
    "background_job_attempts",
    "processing_errors",
    "operator_alerts",
    "idempotency_records",
    "application_configuration",
]

OPTIONAL_TABLES = {
    "user_access_events",
    "image_access_events",
    "entry_field_revision_history",
    "resolution_status_history",
    "provenance_links",
    "application_configuration",
}

APPEND_ONLY = [
    "user_role_history",
    "user_access_events",
    "intake_batch_status_history",
    "intake_page_status_history",
    "upload_attempts",
    "claim_history",
    "page_draft_revisions",
    "entry_submission_revisions",
    "match_signals",
    "match_resolutions",
    "promotion_attempts",
    "canonical_attribute_contributions",
    "provenance_records",
    "audit_events",
    "background_job_attempts",
]

FAMILIES = [
    ("Identity and Access", ["application_users", "user_roles", "user_role_history", "user_access_events"]),
    ("Intake", ["intake_batches", "intake_batch_status_history", "intake_pages", "intake_page_status_history", "intake_entries", "entry_submission_revisions", "intake_entry_fields", "entry_field_revision_history"]),
    ("Images and Uploads", ["storage_objects", "source_images", "image_access_events", "upload_sessions", "upload_attempts"]),
    ("Queue and Claims", ["work_queue_items", "work_claims", "claim_history"]),
    ("Drafts", ["page_drafts", "page_draft_revisions"]),
    ("Normalization", ["normalization_runs", "normalized_entry_fields"]),
    ("Matching", ["match_evaluations", "match_candidates", "match_signals", "match_evaluation_warnings", "match_resolutions", "duplicate_entry_links", "resolution_status_history"]),
    ("Canonical Integration", ["promotion_requests", "promotion_attempts", "canonical_person_links", "canonical_attribute_contributions"]),
    ("Provenance and Audit", ["provenance_records", "provenance_links", "audit_events"]),
    ("Operations", ["background_jobs", "background_job_attempts", "processing_errors", "operator_alerts", "idempotency_records", "application_configuration"]),
]


def main() -> None:
    text = VOL_PATH.read_text(encoding="utf-8")
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()

    principles = sorted(set(re.findall(r"DB-PRINCIPLE-\d{3}", text)))
    decisions = sorted(set(re.findall(r"DB-DEC-\d{3}", text)))

    missing = [t for t in CANONICAL_TABLES if f"`{t}`" not in text and t not in text]
    if missing:
        raise SystemExit(f"Tables missing from Volume 9 text: {missing}")

    required_principles = [f"DB-PRINCIPLE-{i:03d}" for i in range(1, 11)]
    for p in required_principles:
        if p not in principles:
            raise SystemExit(f"Missing principle {p}")

    required_dec = [f"DB-DEC-{i:03d}" for i in range(1, 16)]
    for d in required_dec:
        if d not in decisions:
            raise SystemExit(f"Missing deferred decision {d}")

    table_rows = []
    for name in CANONICAL_TABLES:
        table_rows.append(
            {
                "tableName": name,
                "optional": name in OPTIONAL_TABLES,
                "appendOnly": name in APPEND_ONLY,
                "mentioned": name in text,
            }
        )

    families = [
        {"family": fam, "tables": tables} for fam, tables in FAMILIES
    ]

    table_registry = {
        "documentId": "PEOPLE-VOLUME-09-DATABASE-SPECIFICATIONS-1.0",
        "version": "1.0",
        "status": "DESIGN_COMPLETE_PENDING_CROSS_VOLUME_VALIDATION",
        "canonicalPath": str(VOL_PATH.relative_to(ROOT)).replace("\\", "/"),
        "contentSha256": sha,
        "principles": required_principles,
        "deferredDecisions": required_dec,
        "lockedDecisionCount": 40,
        "tableCount": len(CANONICAL_TABLES),
        "appendOnlyCount": len(APPEND_ONLY),
        "tables": table_rows,
        "families": families,
        "prohibitions": [
            "No SQL migrations",
            "No Prisma schema",
            "No ORM models",
            "No database provisioning",
            "No live database connection",
            "No production credentials",
            "No schema deployment",
            "No seed execution",
            "No destructive data operations",
        ],
    }

    decision_registry = {
        "documentId": "PEOPLE-VOLUME-09-DATABASE-SPECIFICATIONS-1.0",
        "contentSha256": sha,
        "principles": required_principles,
        "deferredDecisions": required_dec,
        "lockedDecisionCount": 40,
        "appendOnlyTables": APPEND_ONLY,
        "canonicalTables": CANONICAL_TABLES,
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "volume_09_table_registry.json").write_text(
        json.dumps(table_registry, indent=2) + "\n", encoding="utf-8"
    )
    (OUT_DIR / "volume_09_decision_registry.json").write_text(
        json.dumps(decision_registry, indent=2) + "\n", encoding="utf-8"
    )
    print(f"tables={len(CANONICAL_TABLES)} principles={len(principles)} deferred={len(decisions)} sha={sha[:12]}")


if __name__ == "__main__":
    main()
