# People Intake — Governance Preflight Report

**Build ID:** PEOPLE-GOVERNANCE-FOUNDATION-1.0  
**Date and time:** 2026-07-25 (local)  
**Final result:** `PASS_WITH_WARNINGS`

---

## Summary

Preflight completed before governance file creation. Controlled project paths resolve to `H:\people`. Tools required for documentation validation are available.

---

## Path Verification

| Check | Result |
| --- | --- |
| Current working directory | `H:\people` |
| Confirmed target root | `H:\people` |
| H: drive available | Yes |
| `H:\people` directory status | Exists / created as needed |
| TEMP | `H:\people\.tmp` |
| TMP | `H:\people\.tmp` |
| TMPDIR | `H:\people\.tmp` |
| npm_config_cache | `H:\people\.npm-cache` |

---

## Tool Availability

| Tool | Result |
| --- | --- |
| Node.js | v22.18.0 |
| npm | 10.9.3 |
| Git | 2.50.1.windows.1 |
| PowerShell | 7.6.3 |

---

## Controlled Write Categories

Required local directories confirmed or created:

- `H:\people\.tmp`
- `H:\people\.cache`
- `H:\people\.npm-cache`
- `H:\people\.test-output`
- `H:\people\.local-storage`
- `H:\people\.netlify`
- `H:\people\docs`
- `H:\people\develop_notes`
- `H:\people\contracts`
- `H:\people\diagrams`
- `H:\people\scripts`
- `H:\people\reports`

Prohibited implementation directories (`src`, `app`, `prisma`, etc.) were not present and will not be created in this build.

---

## Uncontrolled C-Drive Limitations

Honest limitation: Windows, Cursor, Node, browsers, or authentication tools may independently write application-level files to the user profile on `C:\`. This project aggressively configures controllable paths to `H:\` and will validate controlled project artifacts. It cannot prevent the operating system from writing OS-level files to `C:\`.

No controlled project artifact was intentionally written to `C:\` during preflight.

Secrets, database credentials, and production keys were not inspected.

---

## Final Result

**PASS_WITH_WARNINGS**

Warning: OS and host-application writes outside project control may still touch `C:\`. Project-controlled paths are correctly bound to `H:\people`.
