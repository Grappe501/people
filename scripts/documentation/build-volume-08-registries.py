#!/usr/bin/env python3
"""Extract Volume 8 rule/invariant IDs and write machine-readable registries."""
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
    / "volume-08-technical-specifications"
    / "VOLUME_08_TECHNICAL_DOMAIN_SPECIFICATIONS.md"
)
OUT_DIR = ROOT / "data" / "documentation"

DOMAINS = [
    ("AUTH", "Authentication"),
    ("USER", "User Access and Approval"),
    ("AUTHZ", "Authorization"),
    ("BATCH", "Batch"),
    ("PAGE", "Page"),
    ("IMAGE", "Source Image"),
    ("UPLOAD", "Upload"),
    ("QUEUE", "Shared Work Queue"),
    ("CLAIM", "Claim"),
    ("DRAFT", "Draft"),
    ("TRANSCRIPTION", "Transcription"),
    ("FIELD", "Field Condition"),
    ("NORMALIZE", "Normalization"),
    ("SUBMIT", "Entry Submission"),
    ("MATCH", "Matching"),
    ("CANDIDATE", "Match Candidate"),
    ("RESOLUTION", "Match Resolution"),
    ("PROMOTION", "Canonical Promotion"),
    ("ATTRIBUTE", "Person Attribute Contribution"),
    ("PROVENANCE", "Provenance"),
    ("AUDIT", "Audit"),
    ("JOB", "Background Job"),
    ("ALERT", "Operator Alert"),
    ("SEARCH", "Search"),
    ("ADMIN", "Administration"),
    ("REPORT", "Reporting"),
    ("RETENTION", "Retention and Archival"),
    ("RECOVERY", "Error Recovery"),
]

REQUIRED_GLOBAL_INVARIANTS = [f"PEOPLE-INV-{i:03d}" for i in range(1, 16)]


def main() -> None:
    text = VOL_PATH.read_text(encoding="utf-8")
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
    ids = sorted(set(re.findall(r"([A-Z][A-Z0-9]+-(?:RULE|INV)-\d{3})", text)))
    rules = [i for i in ids if "-RULE-" in i]
    invs = [i for i in ids if "-INV-" in i]
    people_inv = [i for i in invs if i.startswith("PEOPLE-INV-")]

    missing = [i for i in REQUIRED_GLOBAL_INVARIANTS if i not in people_inv]
    if missing:
        raise SystemExit(f"Missing required global invariants: {missing}")

    domain_rows = []
    for prefix, name in DOMAINS:
        domain_rows.append(
            {
                "domainId": f"DOMAIN-{prefix}",
                "name": name,
                "rulePrefix": prefix,
                "rules": [r for r in rules if r.startswith(f"{prefix}-RULE-")],
                "invariants": [i for i in invs if i.startswith(f"{prefix}-INV-")],
            }
        )

    domain_registry = {
        "documentId": "PEOPLE-VOLUME-08-TECHNICAL-DOMAIN-SPECIFICATIONS-1.0",
        "version": "1.0",
        "status": "DESIGN_COMPLETE_PENDING_CROSS_VOLUME_FREEZE",
        "canonicalPath": str(VOL_PATH.relative_to(ROOT)).replace("\\", "/"),
        "contentSha256": sha,
        "globalInvariants": REQUIRED_GLOBAL_INVARIANTS,
        "domains": domain_rows,
        "ruleCount": len(rules),
        "invariantCount": len(invs),
        "lockedDecisionCount": 40,
    }

    rule_registry = {
        "documentId": "PEOPLE-VOLUME-08-TECHNICAL-DOMAIN-SPECIFICATIONS-1.0",
        "contentSha256": sha,
        "rules": rules,
        "invariants": invs,
        "globalInvariants": REQUIRED_GLOBAL_INVARIANTS,
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "volume_08_domain_registry.json").write_text(
        json.dumps(domain_registry, indent=2) + "\n", encoding="utf-8"
    )
    (OUT_DIR / "volume_08_rule_registry.json").write_text(
        json.dumps(rule_registry, indent=2) + "\n", encoding="utf-8"
    )
    print(f"rules={len(rules)} invariants={len(invs)} sha={sha[:12]}")


if __name__ == "__main__":
    main()
