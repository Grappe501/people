# People Intake — Authorization Matrix

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-SECURITY-API-ENGINEERING-DESIGN-1.0

---

## Philosophy

Authorization is server-side, explicit, deny-by-default, action-specific, record-aware, state-aware, and audited for sensitive operations.

Always check both:

```text
Can this role perform this action?
Can this user perform this action on this record in its current state?
```

---

## Roles

UPLOADER · DATA_ENTRY · REVIEWER · ADMIN · OWNER

---

## Batch Actions

| Action | Uploader | Data Entry | Reviewer | Admin | Owner |
| --- | ---: | ---: | ---: | ---: | ---: |
| Create batch | Yes | Optional by policy | No | Yes | Yes |
| Edit draft batch | Own only | No | No | Yes | Yes |
| Upload pages | Own batch | Optional by policy | No | Yes | Yes |
| View own batches | Yes | Limited | Limited | Yes | Yes |
| View all batches | No | Limited queue context | Limited matching context | Yes | Yes |
| Change priority | No | No | No | Yes | Yes |
| Archive batch | No | No | No | Yes | Yes |
| Reopen completed batch | No | No | No | Restricted | Yes |

---

## Page Actions

| Action | Uploader | Data Entry | Reviewer | Admin | Owner |
| --- | ---: | ---: | ---: | ---: | ---: |
| View source image | Own upload context | Claimed/assigned | Matching context | Yes | Yes |
| Replace image | Own unresolved upload | No | Request only | Yes | Yes |
| Claim page | No | Yes | No | Yes | Yes |
| Edit transcription | No | Claimed page | Correction if allowed | Yes | Yes |
| Submit page | No | Claimed page | No | Yes | Yes |
| Release claim | No | Own claim | No | Yes | Yes |
| Force-release claim | No | No | No | Yes | Yes |
| Reassign page | No | No | No | Yes | Yes |
| Complete page | No | No | Matching workflow | Yes | Yes |

---

## Matching Actions

| Action | Uploader | Data Entry | Reviewer | Admin | Owner |
| --- | ---: | ---: | ---: | ---: | ---: |
| View candidate list | No | No | Yes | Yes | Yes |
| Link existing person | No | No | Yes | Yes | Yes |
| Request new person | No | No | Yes | Yes | Yes |
| Reject candidate | No | No | Yes | Yes | Yes |
| Return correction | No | Limited self-receipt | Yes | Yes | Yes |
| Merge canonical people | No | No | No | Restricted separate | Owner-approved separate |

---

## User Management

| Action | Uploader | Data Entry | Reviewer | Admin | Owner |
| --- | ---: | ---: | ---: | ---: | ---: |
| View own account | Yes | Yes | Yes | Yes | Yes |
| Invite operational user | No | No | No | Yes | Yes |
| Assign non-admin role | No | No | No | Yes | Yes |
| Assign admin role | No | No | No | No | Yes |
| Disable user | No | No | No | Yes, non-owner | Yes |
| Change owner | No | No | No | No | Restricted owner process |

---

## Record-Level Rules

- **Uploader:** own images/batches/replacement requests only — no unrelated sheet browsing  
- **Data entry:** claimed page, limited queue metadata, corrections, own recent work — no arbitrary image browse, no candidate people  
- **Reviewer:** entry under review + needed candidate summary — not unrestricted people browse unless separately authorized  
- **Admin:** broader but audited; sensitive image/user actions audited  

---

## Image Access Authorization

```text
Browser requests page image
→ Server verifies session
→ Server verifies role + record access
→ Short-lived signed URL or stream
→ Access may be audited
```

Browser must not construct storage URLs. No public bucket. No dedicated download button for routine roles. Exact signed URL lifetime deferred.
