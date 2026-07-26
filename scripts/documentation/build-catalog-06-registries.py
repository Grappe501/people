#!/usr/bin/env python3
"""Build Catalog 6 notification foundation registry."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "data" / "documentation"
CAT6 = ROOT / "docs" / "catalogs" / "catalog-06-notifications" / "CATALOG_06_NOTIFICATIONS.md"

CHANNELS = ["IN_APP", "EMAIL", "SMS (future)", "PUSH (future)", "WEBHOOK (future)"]
PRIORITIES = ["LOW", "NORMAL", "HIGH", "CRITICAL"]
RECIPIENTS = [
    "Individual User",
    "Assigned Worker",
    "Reviewer",
    "Administrator",
    "Owner",
    "System Account",
]
EXPIRATION = [
    "Never Expires",
    "Expires After Duration",
    "Expires On State Change",
    "Expires On Acknowledgment",
]

SEEDED = [
    ("NOTIFY-QUEUE-001", "WORK_AVAILABLE"),
    ("NOTIFY-CLAIM-001", "CLAIM_EXPIRING"),
    ("NOTIFY-CLAIM-002", "CLAIM_EXPIRED"),
    ("NOTIFY-DRAFT-001", "DRAFT_RECOVERABLE"),
    ("NOTIFY-PAGE-001", "TRANSCRIPTION_RETURNED"),
    ("NOTIFY-MATCH-001", "MATCH_REQUIRES_REVIEW"),
    ("NOTIFY-PROMOTION-001", "PROMOTION_FAILED"),
    ("NOTIFY-CONFIG-001", "SYSTEM_CONFIGURATION_CHANGED"),
    ("NOTIFY-SECURITY-001", "SECURITY_EVENT"),
]

LOCKED = [
    "No production notification type may exist outside this catalog or an approved amendment.",
    "Recipients are determined by business rules, not client input.",
    "Priority never replaces authorization.",
    "Notifications must never expose confidential information to unauthorized recipients.",
    "Security notifications are generally not deduplicated.",
    "Reading a notification does not necessarily acknowledge it.",
    "Future channels (SMS, PUSH, WEBHOOK) require formal catalog amendment before production use.",
    "Acknowledgment-required notifications must be auditable where required.",
    "Seeded notification names in this catalog are authoritative permanent identifiers.",
    "Notifications must remain accessible without relying solely on color for priority.",
    "Deduplication must not suppress SECURITY_EVENT by default.",
    "Configuration-change and security notifications require acknowledgment.",
    "Notification delivery failures must not silently alter business state.",
    "Exact channel enablement may be environment-specific but must use cataloged notification types.",
    "Additional notification types require catalog amendment under this contract.",
]


def main() -> None:
    text = CAT6.read_text(encoding="utf-8")
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()

    for needle in [
        "PEOPLE-CATALOG-06-NOTIFICATIONS-1.0",
        "NOTIFY-PRINCIPLE-001",
        "WORK_AVAILABLE",
        "SECURITY_EVENT",
        "Foundation Scope",
        "PEOPLE-CATALOG-07-BACKGROUND-JOBS-1.0",
    ]:
        if needle not in text:
            raise SystemExit(f"Missing required string: {needle}")

    principles = [f"NOTIFY-PRINCIPLE-{i:03d}" for i in range(1, 11)]
    for p in principles:
        if p not in text:
            raise SystemExit(f"Missing principle {p}")

    for channel in CHANNELS:
        if channel not in text:
            raise SystemExit(f"Missing channel: {channel}")

    for priority in PRIORITIES:
        if priority not in text:
            raise SystemExit(f"Missing priority: {priority}")

    for recipient in RECIPIENTS:
        if recipient not in text:
            raise SystemExit(f"Missing recipient type: {recipient}")

    for expire in EXPIRATION:
        if expire not in text:
            raise SystemExit(f"Missing expiration behavior: {expire}")

    for nid, name in SEEDED:
        if nid not in text or name not in text:
            raise SystemExit(f"Missing notification: {nid} / {name}")

    for decision in LOCKED:
        if decision not in text:
            raise SystemExit(f"Missing locked decision: {decision}")

    found = sorted(set(re.findall(r"NOTIFY-[A-Z]+-\d{3}", text)))
    expected = [i for i, _ in SEEDED]
    # Exclude principles NOTIFY-PRINCIPLE-* which also match pattern if PRINCIPLE counted
    entry_ids = [i for i in found if not i.startswith("NOTIFY-PRINCIPLE-")]
    if sorted(entry_ids) != sorted(expected):
        raise SystemExit(
            f"Notification ID mismatch: found={sorted(entry_ids)} expected={sorted(expected)}"
        )

    registry = {
        "documentSetId": "PEOPLE-CATALOG-LIBRARY-1.0",
        "documentId": "PEOPLE-CATALOG-06-NOTIFICATIONS-1.0",
        "version": "1.0",
        "status": "DESIGN_COMPLETE_IMPLEMENTATION_NOT_AUTHORIZED",
        "scope": "FOUNDATION_CONTRACT_WITH_SEEDED_NOTIFICATIONS",
        "canonicalPath": str(CAT6.relative_to(ROOT)).replace("\\", "/"),
        "contentSha256": sha,
        "principleCount": 10,
        "principles": principles,
        "channelCount": len(CHANNELS),
        "channels": CHANNELS,
        "priorityCount": len(PRIORITIES),
        "priorities": PRIORITIES,
        "recipientTypeCount": len(RECIPIENTS),
        "recipientTypes": RECIPIENTS,
        "expirationPolicyCount": len(EXPIRATION),
        "expirationPolicies": EXPIRATION,
        "seededNotificationCount": len(SEEDED),
        "seededNotifications": [
            {"notificationId": nid, "canonicalName": name} for nid, name in SEEDED
        ],
        "lockedDecisionCount": len(LOCKED),
        "lockedDecisions": LOCKED,
        "overallReadinessPercent": 98,
        "nextCatalogId": "PEOPLE-CATALOG-07-BACKGROUND-JOBS-1.0",
        "prohibitions": [
            "No application source code",
            "No email, SMS, push, or webhook delivery implementation",
            "No notification persistence or queue workers",
            "No UI notification components",
            "No dependency installation",
            "No inventing undocumented production notification names outside this catalog and its approved amendments",
        ],
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "catalog_06_notifications_registry.json").write_text(
        json.dumps(registry, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"principles=10 channels={len(CHANNELS)} priorities={len(PRIORITIES)} "
        f"recipients={len(RECIPIENTS)} seeded={len(SEEDED)} locked={len(LOCKED)} "
        f"sha={sha[:12]}"
    )


if __name__ == "__main__":
    main()
