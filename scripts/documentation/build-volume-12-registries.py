#!/usr/bin/env python3
"""Extract Volume 12 component inventory and write registries."""
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
    / "volume-12-component-library"
    / "VOLUME_12_COMPONENT_LIBRARY_AND_DESIGN_SYSTEM.md"
)
OUT_DIR = ROOT / "data" / "documentation"

CATEGORIES = {
    "Shell and Layout": [
        "AppShell", "NavigationRail", "MobileNavigation", "PageContainer",
        "PageHeader", "SectionHeader", "Breadcrumbs", "SplitPane", "StickyActionBar",
    ],
    "Actions": ["Button", "ButtonGroup", "OverflowMenu", "Tabs", "Pagination"],
    "Forms": [
        "FieldGroup", "TextInput", "TextArea", "Select", "RadioGroup", "Checkbox",
        "DateInput", "NumberInput", "SearchInput", "FilePicker",
    ],
    "Intake": [
        "PreferenceControl", "FieldConditionControl", "RowActivationControl",
        "EntryRow", "EntryGrid", "TranscriptionProgress", "SubmissionReviewSummary",
    ],
    "Images": [
        "SourceImageViewer", "ImageToolbar", "ImageThumbnail",
        "ImageQualityControl", "ImageVersionHistory",
    ],
    "Queue and Claims": [
        "QueueItem", "QueueList", "ClaimButton", "ClaimStatus",
        "ClaimTimer", "ClaimConflictNotice",
    ],
    "Save and Recovery": [
        "SaveStatus", "RecoveryBanner", "StaleVersionDialog", "UnsavedChangesGuard",
    ],
    "Feedback": [
        "StatusBadge", "InlineMessage", "Banner", "Toast",
        "ProgressIndicator", "Skeleton", "EmptyState", "ErrorState",
    ],
    "Data Display": [
        "Card", "SummaryCard", "RecordSummary", "DetailPanel", "DataTable",
        "ResponsiveRecordList", "FilterBar", "SortControl", "Timeline",
    ],
    "Matching": [
        "EvidenceComparison", "CandidateCard", "ConfidenceIndicator", "MatchSignal",
        "SignalGroup", "ConflictAlert", "ResolutionPanel", "ResolutionConfirmationDialog",
    ],
    "Promotion": ["PromotionStatus", "AttemptTimeline", "RetryAction"],
    "Users and Roles": ["UserStatus", "RoleBadge", "RoleEditor", "UserActionPanel"],
    "Administration": [
        "OperationalHealthCard", "AlertCard", "ErrorDetailPanel",
        "AuditEventRow", "AuditEventDetail",
    ],
    "Overlays": ["Dialog", "ConfirmationDialog", "Drawer", "Popover"],
    "Help": ["HelpText", "Tooltip", "DefinitionPopover", "FirstUseGuide"],
}


def main() -> None:
    text = VOL_PATH.read_text(encoding="utf-8")
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()

    principles = sorted(set(re.findall(r"DESIGN-PRINCIPLE-\d{3}", text)))
    required_principles = [f"DESIGN-PRINCIPLE-{i:03d}" for i in range(1, 11)]
    for p in required_principles:
        if p not in principles:
            raise SystemExit(f"Missing principle {p}")

    deferred = sorted(set(re.findall(r"COMP-DEC-\d{3}", text)))
    required_dec = [f"COMP-DEC-{i:03d}" for i in range(1, 26)]
    for d in required_dec:
        if d not in deferred:
            raise SystemExit(f"Missing deferred decision {d}")

    components = []
    for category, names in CATEGORIES.items():
        for name in names:
            if f"`{name}`" not in text and name not in text:
                raise SystemExit(f"Component missing: {name}")
            components.append({"componentName": name, "category": category})

    registry = {
        "documentId": "PEOPLE-VOLUME-12-COMPONENT-LIBRARY-AND-DESIGN-SYSTEM-1.0",
        "version": "1.0",
        "status": "DESIGN_COMPLETE_IMPLEMENTATION_NOT_AUTHORIZED",
        "canonicalPath": str(VOL_PATH.relative_to(ROOT)).replace("\\", "/"),
        "contentSha256": sha,
        "principles": required_principles,
        "lockedDecisionCount": 50,
        "deferredDecisions": required_dec,
        "componentCount": len(components),
        "components": components,
        "accessibilityTarget": "WCAG 2.2 AA",
        "prohibitions": [
            "No React components",
            "No JSX or TSX",
            "No CSS files",
            "No design-token package",
            "No Storybook implementation",
            "No application routes",
            "No API calls",
            "No production assets",
            "No icon package installation",
            "No font-file installation",
            "No frontend framework selection",
            "No build-tool configuration",
            "No dependency installation",
        ],
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "volume_12_component_registry.json").write_text(
        json.dumps(registry, indent=2) + "\n", encoding="utf-8"
    )
    print(f"components={len(components)} deferred={len(required_dec)} sha={sha[:12]}")


if __name__ == "__main__":
    main()
