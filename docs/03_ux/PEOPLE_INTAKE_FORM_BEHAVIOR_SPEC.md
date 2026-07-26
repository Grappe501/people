# People Intake — Form Behavior Spec

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-WORKFLOW-UX-DESIGN-1.0

---

## Field Order (Locked)

```text
Last Name
First Name
Email
Phone
ZIP Code
Volunteer
Email List
```

Matches hard-copy Last, First orientation.

---

## Last Name

- First focus field on new person
- Preserve punctuation
- Trim leading/trailing spaces
- Allow apostrophes and hyphens
- Do not require perfect capitalization

## First Name

- Preserve middle initials if written
- Do not force splitting into extra fields
- Allow incomplete/unclear names

## Email

- Email keyboard on mobile
- Store raw
- Normalize lowercase for matching later
- Warn on likely format issues
- Allow submit with warning

## Phone

- Telephone keyboard
- Visual formatting (e.g., 5015551212 → (501) 555-1212)
- Store raw
- Normalize digits later
- Allow incomplete with warning

## ZIP Code

- Number keyboard
- Five digits primary; leave room for ZIP+4 later
- Warn rather than block

---

## Volunteer / Email List

Three visible choices — never an unlabeled switch:

```text
Yes | No | Blank
```

Blank means `UNKNOWN` in data semantics. Never silent-convert to No.

---

## Missing vs Unreadable

Each field supports options:

```text
Not Provided
Unreadable
```

A blank field alone does not automatically explain why the value is absent; operators should use the field-options control when the distinction matters.

---

## Person / Page Limits

- 0–10 people per page
- Blank unused rows ignored
- No eleventh person
- At least one entry required unless page explicitly marked blank/unusable/unreadable
- Within-page duplicate warning (non-blocking)

---

## Mobile Save Person

```text
Save Person & Continue
```

Saves, collapses summary, opens next, focuses Last Name, keeps image view state.

## Desktop Grid Save

Autosave after meaningful changes; sticky Save Draft available; Review before submit.

---

## Review Warnings (Non-Blocking)

```text
Email may be incomplete
Phone has fewer than 10 digits
ZIP may be incomplete
Volunteer response is blank
Possible duplicate on this page
Unreadable field
```

## Blocking Errors

- More than ten entries
- Corrupted draft
- Claim lost / reassigned
- Missing required internal identifiers

---

## Submission Primary Action

```text
Submit Page & Open Next
```

Also: Return to Entry; Submit Page & Return to Queue.
