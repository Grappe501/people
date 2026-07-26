#!/usr/bin/env python3
"""Build Catalog 5 permissions foundation registry."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "data" / "documentation"
CAT5 = ROOT / "docs" / "catalogs" / "catalog-05-permissions" / "CATALOG_05_PERMISSIONS.md"

ROLES = [
    ("ROLE-001", "Owner"),
    ("ROLE-002", "Administrator"),
    ("ROLE-003", "Reviewer"),
    ("ROLE-004", "Data Entry"),
    ("ROLE-005", "Uploader"),
    ("ROLE-006", "Viewer"),
    ("ROLE-007", "System"),
]

RESOURCES = [
    "Users",
    "Roles",
    "Batches",
    "Pages",
    "Entries",
    "Claims",
    "Drafts",
    "Uploads",
    "Images",
    "Queues",
    "Matches",
    "Resolutions",
    "Promotions",
    "Exports",
    "Reports",
    "Configuration",
    "Audit",
    "Background Jobs",
]

ACTIONS = [
    "READ",
    "CREATE",
    "UPDATE",
    "DELETE",
    "CLAIM",
    "RELEASE",
    "SUBMIT",
    "APPROVE",
    "RETURN",
    "MATCH",
    "RESOLVE",
    "PROMOTE",
    "EXPORT",
    "ARCHIVE",
    "RESTORE",
    "CONFIGURE",
]

SCOPES = [
    "Own Resource",
    "Assigned Work",
    "Department",
    "Organization",
    "Entire System",
]

PERMISSIONS = [
    ("PERM-USER-001", "USER_READ"),
    ("PERM-USER-002", "USER_CREATE"),
    ("PERM-USER-003", "USER_UPDATE"),
    ("PERM-USER-004", "USER_DISABLE"),
    ("PERM-ROLE-001", "ROLE_ASSIGN"),
    ("PERM-BATCH-001", "BATCH_CREATE"),
    ("PERM-BATCH-002", "BATCH_COMPLETE"),
    ("PERM-PAGE-001", "PAGE_UPLOAD"),
    ("PERM-PAGE-002", "PAGE_REPLACE_IMAGE"),
    ("PERM-PAGE-003", "PAGE_CLAIM"),
    ("PERM-PAGE-004", "PAGE_SUBMIT"),
    ("PERM-MATCH-001", "MATCH_REVIEW"),
    ("PERM-MATCH-002", "MATCH_FINALIZE"),
    ("PERM-PROMOTION-001", "PROMOTION_APPROVE"),
    ("PERM-EXPORT-001", "EXPORT_RUN"),
    ("PERM-CONFIG-001", "CONFIGURATION_EDIT"),
    ("PERM-AUDIT-001", "AUDIT_VIEW"),
    ("PERM-SYSTEM-001", "SYSTEM_JOB_EXECUTE"),
]

SOD = [
    ("SOD-001", "Submit and Approve"),
    ("SOD-002", "Match Resolve and Dual Review"),
    ("SOD-003", "Self Elevation"),
]

LOCKED = [
    "Authorization is server enforced.",
    "Roles grant permissions.",
    "Permissions apply to resources.",
    "Resources have scopes.",
    "States may block otherwise valid permissions.",
    "Hidden UI never grants authorization.",
    "Owners cannot be accidentally removed.",
    "Audit history is always protected.",
    "Administrative overrides are auditable.",
    "Separation of duties is enforced for protected workflows.",
    "Version 1 roles are a closed set unless formally amended.",
    "Permission keys are permanent identifiers.",
    "System never authenticates through interactive login.",
    "Delegation never exceeds the delegator's authority.",
    "Additional roles, permission keys, and matrix grants require catalog amendment.",
]


def main() -> None:
    text = CAT5.read_text(encoding="utf-8")
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()

    for needle in [
        "PEOPLE-CATALOG-05-PERMISSIONS-1.0",
        "AUTHZ-PRINCIPLE-001",
        "ROLE-001",
        "PERM-USER-001",
        "USER_READ",
        "SOD-001",
        "Foundation Scope",
        "PEOPLE-CATALOG-06-NOTIFICATIONS-1.0",
    ]:
        if needle not in text:
            raise SystemExit(f"Missing required string: {needle}")

    principles = [f"AUTHZ-PRINCIPLE-{i:03d}" for i in range(1, 11)]
    for p in principles:
        if p not in text:
            raise SystemExit(f"Missing principle {p}")

    for role_id, role_key in ROLES:
        if role_id not in text or role_key not in text:
            raise SystemExit(f"Missing role: {role_id} / {role_key}")

    for resource in RESOURCES:
        if resource not in text:
            raise SystemExit(f"Missing resource type: {resource}")

    for action in ACTIONS:
        if action not in text:
            raise SystemExit(f"Missing action: {action}")

    for scope in SCOPES:
        if scope not in text:
            raise SystemExit(f"Missing scope: {scope}")

    for perm_id, key in PERMISSIONS:
        if perm_id not in text or key not in text:
            raise SystemExit(f"Missing permission: {perm_id} / {key}")

    for sod_id, label in SOD:
        if sod_id not in text or label not in text:
            raise SystemExit(f"Missing SoD: {sod_id}")

    for decision in LOCKED:
        if decision not in text:
            raise SystemExit(f"Missing locked decision: {decision}")

    found_perms = sorted(set(re.findall(r"PERM-[A-Z]+-\d{3}", text)))
    expected_perms = [i for i, _ in PERMISSIONS]
    if sorted(found_perms) != sorted(expected_perms):
        raise SystemExit(
            f"Permission ID mismatch: found={len(found_perms)} expected={len(expected_perms)}"
        )

    registry = {
        "documentSetId": "PEOPLE-CATALOG-LIBRARY-1.0",
        "documentId": "PEOPLE-CATALOG-05-PERMISSIONS-1.0",
        "version": "1.0",
        "status": "DESIGN_COMPLETE_IMPLEMENTATION_NOT_AUTHORIZED",
        "scope": "FOUNDATION_CONTRACT_WITH_SEEDED_PERMISSIONS",
        "canonicalPath": str(CAT5.relative_to(ROOT)).replace("\\", "/"),
        "contentSha256": sha,
        "principleCount": 10,
        "principles": principles,
        "roleCount": len(ROLES),
        "roles": [{"roleId": rid, "roleKey": key} for rid, key in ROLES],
        "resourceTypeCount": len(RESOURCES),
        "resourceTypes": RESOURCES,
        "actionCount": len(ACTIONS),
        "actions": ACTIONS,
        "scopeCount": len(SCOPES),
        "scopes": SCOPES,
        "seededPermissionCount": len(PERMISSIONS),
        "seededPermissions": [
            {"permissionId": pid, "permissionKey": key} for pid, key in PERMISSIONS
        ],
        "sodRuleCount": len(SOD),
        "sodRules": [{"sodId": sid, "label": label} for sid, label in SOD],
        "lockedDecisionCount": len(LOCKED),
        "lockedDecisions": LOCKED,
        "overallReadinessPercent": 99,
        "nextCatalogId": "PEOPLE-CATALOG-06-NOTIFICATIONS-1.0",
        "prohibitions": [
            "No application source code",
            "No authentication or authorization middleware implementation",
            "No RLS policy SQL or migrations",
            "No role-assignment UI or handlers",
            "No dependency installation",
            "No inventing undocumented production roles, permission keys, or matrix grants outside this catalog and its approved amendments",
        ],
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "catalog_05_permissions_registry.json").write_text(
        json.dumps(registry, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"principles=10 roles={len(ROLES)} resources={len(RESOURCES)} "
        f"actions={len(ACTIONS)} scopes={len(SCOPES)} perms={len(PERMISSIONS)} "
        f"sod={len(SOD)} locked={len(LOCKED)} sha={sha[:12]}"
    )


if __name__ == "__main__":
    main()
