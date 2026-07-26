# People Intake — Queue and Claiming

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-WORKFLOW-UX-DESIGN-1.0  
**Governs:** Shared queue, priority, atomic claims, expiration, release, reassignment

---

## Purpose

Define how pages move through a multi-user queue without two people editing the same page at once.

---

## Primary Work Item

The **Page** is the queue unit.

Each page:

- Belongs to one batch
- Has one source image
- May contain up to ten entries
- Has one queue status
- May be claimed by one user at a time
- Keeps complete history

---

## Queue Categories (User-Facing)

```text
Uploading
Ready for Entry
In Entry
Ready for Matching
Needs Match Review
Needs Entry Correction
Completed
Archived
```

---

## Data Entry Queue Screen

Show batch, page, source, waiting time, priority, status, assigned to.

Default worker action remains:

```text
Claim Next Page
```

Manual selection only when needed.

---

## Priority

```text
Normal · High · Urgent
```

Administrators may change priority. Workers cannot raise their own batch priority.

Claim selection order:

1. Highest-priority batch
2. Oldest ready page
3. Lowest page sequence within batch

---

## Aging

Pages waiting too long show:

```text
Waiting 3 days
```

Administrators can sort by oldest waiting.

---

## Atomic Claim

Only one successful claim per page.

If two users press Claim Next Page simultaneously, each receives a different page (or a clear “no pages available” if the queue empties).

### Claim metadata

- User
- Claimed time
- Last activity
- Expiration time
- Claim version
- Draft identity

---

## Claim Renewal

Renew on:

- Typing
- Saving
- Meaningful image interaction
- Returning from background
- Explicit continue working

Recommended inactivity window:

```text
30 minutes
```

### Warning

```text
Your page will be released in 5 minutes.
Continue Working
```

---

## Expired Claim

On expire:

1. Preserve draft
2. Return page to queue
3. Mark prior draft recoverable
4. Block old session from overwriting newer work

### If still unclaimed

```text
Reclaim Page
```

### If claimed by someone else

```text
This page is now being entered by another user.
Your saved draft has been preserved for administrator review.
```

---

## Manual Release

```text
Save & Release Page
```

Page returns to Ready for Entry (or appropriate prior ready state). Draft preserved.

---

## Administrator Reassignment

Admin may:

- Release a claim
- Reassign a page
- Preserve existing draft
- Record a reason
- Notify current user in-app

---

## Offline / Weak Signal Interaction

Brief disconnect: local draft may continue; submission waits for reconnect; claim must be reconciled before final save.

If another user received the page while offline, original user must not overwrite newer work.

---

## Matching Queue

Separate from entry queue. Reviewers use Review Next Match against Needs Match Review / Conflicts inventories. Claiming model for match items will follow the same one-active-editor principle; exact match-claim mechanics may be detailed further in data/security design without changing this UX intent.
