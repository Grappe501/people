#!/usr/bin/env python3
"""Extract Volume 11 screen inventory and write registries."""
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
    / "volume-11-ui-specifications"
    / "VOLUME_11_USER_INTERFACE_SPECIFICATIONS.md"
)
OUT_DIR = ROOT / "data" / "documentation"

WORKSPACES = ["Capture", "Transcribe", "Match", "Manage"]

SCREEN_GROUPS = {
    "Public or Pre-Access": [
        "Sign In",
        "Access Pending",
        "Access Suspended",
        "Access Revoked",
        "Session Expired",
    ],
    "Home": ["Role-Aware Home", "My Recent Work", "Notifications"],
    "Capture": [
        "Capture Dashboard",
        "Batch List",
        "Create Batch",
        "Batch Detail",
        "Upload Pages",
        "Upload Progress",
        "Page Preparation",
        "Image Replacement",
    ],
    "Transcribe": [
        "Transcribe Dashboard",
        "Shared Queue",
        "My Active Work",
        "Transcription Workspace",
        "Draft Recovery",
        "Submission Review",
        "Submission Success",
        "Submitted Work",
        "Returned Corrections",
    ],
    "Review": [
        "Transcription Review Queue",
        "Transcription Review Screen",
        "Correction Request",
    ],
    "Match": [
        "Match Dashboard",
        "Match Review Queue",
        "Match Review Screen",
        "Candidate Detail",
        "Resolution Confirmation",
        "Resolution Detail",
        "Promotion List",
        "Promotion Detail",
        "Promotion Retry",
    ],
    "Manage": [
        "Manage Dashboard",
        "User List",
        "Invite User",
        "User Detail",
        "Role Management",
        "Claims Management",
        "Batch Operations",
        "Error and Alert Center",
        "Error Detail",
        "Alert Detail",
        "Background Job Detail",
        "Audit Explorer",
        "Audit Event Detail",
        "Reports",
        "Export Confirmation",
        "Configuration View",
    ],
    "Shared": [
        "Global Search",
        "Record Not Found",
        "Access Denied",
        "System Error",
        "Offline or Connection Lost",
        "Maintenance Notice",
    ],
}


def main() -> None:
    text = VOL_PATH.read_text(encoding="utf-8")
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()

    for ws in WORKSPACES:
        if ws not in text:
            raise SystemExit(f"Missing workspace: {ws}")

    deferred = sorted(set(re.findall(r"UI-DEC-\d{3}", text)))
    required_dec = [f"UI-DEC-{i:03d}" for i in range(1, 19)]
    for d in required_dec:
        if d not in deferred:
            raise SystemExit(f"Missing deferred decision {d}")

    screens = []
    for group, names in SCREEN_GROUPS.items():
        for name in names:
            if name not in text:
                raise SystemExit(f"Screen missing from volume text: {name}")
            screens.append({"screenName": name, "group": group})

    registry = {
        "documentId": "PEOPLE-VOLUME-11-USER-INTERFACE-SPECIFICATIONS-1.0",
        "version": "1.0",
        "status": "DESIGN_COMPLETE_IMPLEMENTATION_NOT_AUTHORIZED",
        "canonicalPath": str(VOL_PATH.relative_to(ROOT)).replace("\\", "/"),
        "contentSha256": sha,
        "workspaces": WORKSPACES,
        "lockedDecisionCount": 40,
        "deferredDecisions": required_dec,
        "screenCount": len(screens),
        "screens": screens,
        "accessibilityTarget": "WCAG 2.2 AA",
        "prohibitions": [
            "No React components",
            "No route files",
            "No CSS",
            "No design-system code",
            "No image-upload implementation",
            "No API calls",
            "No authentication integration",
            "No database access",
            "No production analytics",
            "No deployment configuration",
            "No framework selection",
        ],
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "volume_11_screen_registry.json").write_text(
        json.dumps(registry, indent=2) + "\n", encoding="utf-8"
    )
    print(f"screens={len(screens)} deferred={len(required_dec)} sha={sha[:12]}")


if __name__ == "__main__":
    main()
