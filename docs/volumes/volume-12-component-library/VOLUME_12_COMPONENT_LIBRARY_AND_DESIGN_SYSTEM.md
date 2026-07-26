# PEOPLE INTAKE SYSTEM

# VOLUME 12 — COMPONENT LIBRARY AND DESIGN SYSTEM

**Document ID**

```text
PEOPLE-VOLUME-12-COMPONENT-LIBRARY-AND-DESIGN-SYSTEM-1.0
```

**Status**

```text
DESIGN COMPLETE — IMPLEMENTATION NOT AUTHORIZED
```

**Project Root**

```text
H:\people
```

**Document Type**

```text
CANONICAL COMPONENT AND VISUAL SYSTEM SPECIFICATION
```

**Build Mode**

```text
DOCUMENTATION ONLY
```

**Prohibited During This Volume**

* No React components
* No JSX or TSX
* No CSS files
* No design-token package
* No Storybook implementation
* No application routes
* No API calls
* No production assets
* No icon package installation
* No font-file installation
* No frontend framework selection
* No build-tool configuration
* No dependency installation

---

# PART I — PURPOSE AND AUTHORITY

## 1. Purpose

Volume 12 defines the reusable component library and visual design system for the People Intake System before implementation begins.

It specifies:

* design principles
* design tokens
* color roles
* typography
* spacing
* sizing
* breakpoints
* borders
* radii
* shadows
* motion
* icons
* layout primitives
* navigation components
* form controls
* data-entry components
* image-viewing components
* queue components
* matching components
* administrative components
* feedback components
* loading components
* empty states
* error states
* dialogs
* accessibility contracts
* responsive behavior
* component states
* test requirements
* composition rules
* implementation boundaries

This volume answers:

> Which reusable interface building blocks must exist, how must they behave, and how must they remain visually and functionally consistent?

---

## 2. Authority

This volume translates Volume 11 into reusable interface contracts.

Volume 12 must remain consistent with Volumes 0 through 11. Where conflict exists, the higher governing rule prevails until a formal amendment is approved.

---

# PART II — DESIGN SYSTEM DOCTRINE

## 3. Product Character

The component system must make People Intake feel trustworthy, calm, civic, practical, modern, serious, human, efficient, understandable, and safe.

It must not feel flashy, playful at inappropriate moments, punitive, hurried, confusing, surveillance-oriented, overly technical, visually noisy, gamified, or intimidating.

---

## 4. Design Principles

### `DESIGN-PRINCIPLE-001 — Clarity Before Decoration`

Visual treatment must improve understanding. Decoration that does not support comprehension, hierarchy, confidence, or usability should be omitted.

### `DESIGN-PRINCIPLE-002 — Accuracy Before Speed`

Components must make uncertainty easy to express. They must never pressure users to guess.

### `DESIGN-PRINCIPLE-003 — State Must Be Visible`

Users must be able to distinguish: available, claimed, saving, saved, submitted, waiting, completed, blocked, failed, archived, read-only.

### `DESIGN-PRINCIPLE-004 — Color Is Supplemental`

Color must never be the sole carrier of meaning.

### `DESIGN-PRINCIPLE-005 — Reuse Before Reinvention`

Equivalent actions and states must use equivalent components.

### `DESIGN-PRINCIPLE-006 — Mobile Is a Primary Surface`

Components must be designed for mobile use from the beginning.

### `DESIGN-PRINCIPLE-007 — Personal Data Requires Restraint`

Components must minimize unnecessary display of personal information.

### `DESIGN-PRINCIPLE-008 — Source and Interpretation Are Distinct`

Source evidence, raw transcription, normalized values, system suggestions, and approved decisions must have distinguishable presentation.

### `DESIGN-PRINCIPLE-009 — History Is Never Hidden`

Revision, provenance, and audit interfaces must make historical context available without overwhelming ordinary workflows.

### `DESIGN-PRINCIPLE-010 — Recovery Must Feel Safe`

Save failures, stale records, expired claims, and interrupted work must use calm recovery patterns.

---

# PART III — DESIGN TOKEN ARCHITECTURE

## 5. Token Layers

### 5.1 Primitive Tokens

Raw values. Examples: `gray-50`, `blue-600`, `space-4`, `radius-md`, `font-size-16`. Primitive tokens should not normally appear directly in application components.

### 5.2 Semantic Tokens

Purpose-based values. Examples: `color-background-page`, `color-text-primary`, `color-status-success`, `space-component-gap`. Components should primarily consume semantic tokens.

### 5.3 Component Tokens

Component-specific values. Examples: `button-primary-background`, `input-border-focus`, `queue-card-padding`, `dialog-max-width`. Component tokens may derive from semantic tokens.

---

## 6. Token Naming Standard

Preferred pattern:

```text
category-role-state-modifier
```

Examples: `color-text-primary`, `color-surface-raised`, `space-layout-section`, `motion-duration-fast`.

Names must describe purpose rather than current visual appearance. Avoid: `dark-blue`, `light-gray-box`, `big-padding`.

---

# PART IV — COLOR SYSTEM

## 7. Color Roles

### Surfaces

```text
color-surface-page
color-surface-panel
color-surface-raised
color-surface-muted
color-surface-disabled
color-surface-selected
color-surface-overlay
```

### Text

```text
color-text-primary
color-text-secondary
color-text-muted
color-text-disabled
color-text-inverse
color-text-link
color-text-danger
color-text-success
color-text-warning
```

### Borders

```text
color-border-default
color-border-muted
color-border-strong
color-border-focus
color-border-danger
color-border-warning
color-border-success
```

### Action

```text
color-action-primary
color-action-primary-hover
color-action-primary-active
color-action-secondary
color-action-danger
color-action-disabled
```

### Status

```text
color-status-information
color-status-success
color-status-warning
color-status-danger
color-status-neutral
color-status-pending
```

### Evidence Layers

```text
color-evidence-source
color-evidence-raw
color-evidence-normalized
color-evidence-system
color-evidence-approved
color-evidence-conflict
```

---

## 8. Color Accessibility

All text and interactive states must satisfy WCAG 2.2 AA. Required validation includes normal/large text contrast, control boundary contrast, focus indicator contrast, text over status backgrounds, disabled-state legibility, selected-row distinction, and link distinction.

---

## 9. Status Color Rules

Status components must combine text, shape, border, icon where useful, and color.

---

## 10. Prohibited Color Behavior

Do not: use red for ordinary neutral actions; use green to imply consent where consent is unknown; use color alone for unreadable fields; use flashing color for claim expiration; use low-contrast gray for required information; create role-specific color systems that imply hierarchy of human value; use visual urgency where the user is not required to act urgently.

---

# PART V — TYPOGRAPHY

## 11. Typography Principles

Typography must prioritize readability, dense data-entry clarity, clear hierarchy, accessible scale, predictable line length, legible numbers, visible labels, and distinguishable evidence layers.

---

## 12. Font Strategy

Prefer a highly legible sans-serif system: system-native fonts, or an approved web font with strong accessibility and performance. Font files must not be committed casually without licensing and performance review.

---

## 13. Typography Tokens

```text
font-family-interface
font-family-monospace
font-size-caption
font-size-body-small
font-size-body
font-size-body-large
font-size-heading-small
font-size-heading-medium
font-size-heading-large
font-size-display
font-weight-regular
font-weight-medium
font-weight-semibold
font-weight-bold
line-height-tight
line-height-heading
line-height-body
line-height-relaxed
letter-spacing-tight
letter-spacing-normal
letter-spacing-wide
```

---

## 14. Recommended Type Scale

| Role | Approximate Size |
| --- | ---: |
| Caption | 12–13 px |
| Small body | 14 px |
| Standard body | 16 px |
| Large body | 18 px |
| Small heading | 20 px |
| Medium heading | 24 px |
| Large heading | 30–32 px |
| Display | 36–40 px |

The transcription grid must not use text so small that operators strain to compare handwriting and fields.

---

## 15. Numeric Presentation

Use tabular numerals where helpful for row numbers, page numbers, claim times, counts, dates, identifiers, and progress values.

---

## 16. Evidence Typography

Visually distinguish: Source Image; Raw; Normalized; Suggested / System-generated; Approved / Final Resolution. Never use italics alone to distinguish evidence authority.

---

# PART VI — SPACING AND DENSITY

## 17. Spacing Scale

Primitive scale: `0 2 4 6 8 12 16 20 24 32 40 48 64 80`.

Semantic tokens: `space-inline-tight`, `space-inline`, `space-control-gap`, `space-card`, `space-form-row`, `space-section`, `space-layout`, `space-page`.

---

## 18. Density Modes

```text
Comfortable
Compact
```

Comfortable is default for general navigation, batch management, match review, and administration. Compact may be used for transcription grids, audit tables, claims tables, and operational queues. Compact mode must remain accessible and must not reduce touch targets below minimum standards.

---

## 19. Touch Targets

Interactive touch targets should generally be at least:

```text
44 × 44 CSS pixels
```

---

# PART VII — LAYOUT TOKENS

## 20. Container Widths

```text
container-reading
container-form
container-workspace
container-wide
container-full
```

---

## 21. Grid System

Support single-column, two-column split panes, three-panel review layouts, responsive card grids, full-width data tables, and fixed-and-fluid pane combinations.

---

## 22. Responsive Breakpoints

| Breakpoint | Approximate Range |
| --- | ---: |
| Small Mobile | below 375 px |
| Mobile | 375–767 px |
| Tablet | 768–1023 px |
| Desktop | 1024–1439 px |
| Wide Desktop | 1440 px and above |

---

# PART VIII — BORDER, RADIUS, AND ELEVATION

## 23. Border Tokens

```text
border-width-hairline
border-width-default
border-width-strong
border-style-default
```

---

## 24. Radius Tokens

```text
radius-none
radius-small
radius-control
radius-card
radius-panel
radius-dialog
radius-pill
```

Use moderate rounding. Avoid excessive pill-shaped containers for dense information.

---

## 25. Elevation Tokens

```text
shadow-none
shadow-raised
shadow-sticky
shadow-popover
shadow-dialog
```

Do not use heavy shadows for ordinary static cards.

---

# PART IX — MOTION

## 26. Motion Principles

Motion may confirm state change, guide focus, show expansion, communicate progress, and preserve spatial orientation. Motion must not distract from transcription, create urgency, flash, animate large regions unnecessarily, conceal content, or interfere with reduced-motion preferences.

---

## 27. Motion Tokens

```text
motion-duration-instant
motion-duration-fast
motion-duration-standard
motion-duration-slow
motion-easing-standard
motion-easing-enter
motion-easing-exit
```

Conceptual ranges: instant 0–50 ms; fast 100–150 ms; standard 180–250 ms; slow 300–400 ms.

---

## 28. Reduced Motion

When reduced motion is requested: remove nonessential transitions; avoid sliding large panels; avoid animated counters; use immediate or faded state changes; preserve visible status confirmation.

---

# PART X — ICONOGRAPHY

## 29. Icon Principles

Icons must reinforce text, remain recognizable, use consistent stroke or fill style, include accessible names where interactive, and remain secondary to labels in important actions.

---

## 30. Required Icon Concepts

home, capture, upload, image, rotate, zoom, batch, page, row, transcribe, claim, timer, save, saved, warning, error, information, success, review, match, conflict, person, new person, link, history, audit, archive, users, role, search, filter, sort, settings, retry, external system, expand, collapse, more actions.

---

## 31. Icons and Meaning

An icon must not change meaning between components.

---

# PART XI — FOUNDATIONAL LAYOUT COMPONENTS

# 32. `AppShell`

Provide the protected application frame. Contains navigation, top bar, page content, account controls, notification region, skip link, mobile navigation.

States: Default, Navigation Collapsed, Mobile Menu Open, Session Warning, Loading Permissions.

Accessibility: skip-to-content, landmarks, current-navigation indicator, focus containment in mobile menu, Escape closes mobile menu.

---

# 33. `NavigationRail`

Desktop/tablet workspace navigation. Variants: Expanded, Collapsed, Role-Filtered. Active item visible; icons supplemented by labels; tooltips in collapsed mode; nested sections expandable; keyboard navigable.

---

# 34. `MobileNavigation`

Compact mobile workspace navigation. Labels always visible; active state not color-only; no high-risk actions in navigation; supports safe-area insets.

---

# 35. `PageContainer`

Variants: Reading, Form, Workspace, Wide, Full. Consistent horizontal padding; responsive width; safe mobile gutters; no unintended horizontal overflow.

---

# 36. `PageHeader`

Required: title, purpose statement, status, primary action, optional secondary actions, breadcrumbs where applicable. Variants: Standard, Compact, Workspace, Record Detail. Mobile stacks title and actions; keeps primary action and status visible.

---

# 37. `Breadcrumbs`

Identify hierarchy; support direct navigation; collapse on mobile; expose current page semantically; never include raw personal data unnecessarily.

---

# 38. `SectionHeader`

Section title, optional description, count, and action.

---

# 39. `SplitPane`

Variants: Two-Pane, Three-Pane, Adjustable, Fixed Evidence Pane. Minimum usable pane widths; keyboard-accessible resize if adjustable; collapse strategy on smaller screens; no content loss when switching panes.

---

# 40. `StickyActionBar`

Keep primary workflow actions accessible. Respect safe-area insets; not cover content; indicate save state; high-risk action visually separated; logical keyboard focus order.

---

# PART XII — NAVIGATION AND ACTION COMPONENTS

# 41. `Button`

Variants: Primary, Secondary, Tertiary, Danger, Quiet, Link, Icon. Sizes: Small, Medium, Large. States: Default, Hover, Focus, Active, Disabled, Loading.

Rules: one dominant primary per action region; Danger for high-risk; loading prevents duplicate activation; icon-only requires accessible labels; button text describes action.

Good: Submit Page, Claim Page, Retry Promotion. Avoid: OK, Go, Do It, Yes when action is not obvious.

---

# 42. `ButtonGroup`

Variants: Inline, Stacked, Responsive, Confirmation. Primary action position consistent; destructive separated; mobile stacks when needed.

---

# 43. `OverflowMenu`

Never hide the only path to the primary action. Keyboard operable; Escape closes; focus returns to trigger; destructive actions separated; respects permissions.

---

# 44. `Tabs`

Keyboard arrow navigation; selected tab announced; URL state where useful; horizontal scrolling on mobile; count badges optional.

---

# 45. `Pagination`

Current page visible; previous and next; page size where useful; preserve filters; mobile compact variant. Cursor-based pagination may be used where Volume 10 requires it.

---

# PART XIII — FORM COMPONENTS

# 46. `FieldGroup`

Label, optional/required indicators, control, helper text, validation message, character count where needed. Label associated with control; help and error referenced programmatically.

---

# 47. `TextInput`

Variants: Standard, Search, Masked, Read-Only. States: Default, Focus, Filled, Invalid, Disabled, Read-Only, Loading Validation.

Raw transcription inputs must not auto-correct content silently. Placeholder never substitutes for label.

---

# 48. `TextArea`

For operational notes, correction reason, resolution reason, administrative reason. Preserve line breaks; no secret-entry use.

---

# 49. `Select`

Choose one value from a controlled set. Do not use for Yes/No/Unknown, critical field conditions where all choices should remain visible, or destructive confirmation.

---

# 50. `RadioGroup`

Choose one visible option. Preferred for resolution outcomes, quality statuses, review decisions. Group label; keyboard navigation; visible selected state.

---

# 51. `Checkbox`

Independent binary selections. Must not be used for three-state Volunteer or Email List unless implemented as explicit tri-state with visible Unknown.

---

# 52. `DateInput`

Keyboard entry; locale-aware display; machine-stable submission format; clear validation; mobile-friendly.

---

# 53. `NumberInput`

For expected page count, page sequence, bounded priority. Min/max enforcement; no accidental scroll-wheel changes where harmful.

---

# 54. `SearchInput`

Label or accessible name; search icon; clear action; loading state; no hidden automatic submission that disrupts typing.

---

# 55. `FilePicker`

Variants: Single File, Multiple Files, Camera Capture, Drag and Drop. Accepted types and size limits displayed; keyboard accessible; validation per file; does not start irreversible upload without clear behavior.

---

# PART XIV — SPECIALIZED INTAKE CONTROLS

# 56. `PreferenceControl`

Capture YES, NO, UNKNOWN for Volunteer and Email List. All three options visible where space permits. Default: Unknown (or unselected resolving to Unknown). Never default to No. No ambiguous checkbox-only control.

Helper example:

```text
Choose Unknown when the page is blank or unclear.
```

---

# 57. `FieldConditionControl`

Values: Provided, Not Provided, Unreadable, Ambiguous. Corrected usually from revision history. Variants: Compact, Expanded, Review, Read-Only. Selecting Unreadable does not force a guessed value. Status not color-only.

---

# 58. `RowActivationControl`

Clarify whether a physical page row contains an entry. Labels: Use This Row / Blank Row.

---

# 59. `EntryRow`

Contains row number, field controls, preference controls, field conditions, row status, notes, clear-row action, review flags. Variants: Desktop Grid Row, Tablet Row, Mobile Card, Read-Only Review, Correction. States: Inactive, Active, Saving, Saved, Invalid, Ambiguous, Unreadable, Returned, Submitted, Read-Only. Clear-row requires confirmation when populated.

---

# 60. `EntryGrid`

Organize up to ten row positions. Persistent column labels on desktop; visible row numbers; keyboard navigation; inactive rows visually distinct. Complex ARIA grid must not be used unless keyboard behavior is implemented completely.

---

# 61. `TranscriptionProgress`

Displays rows activated/complete, unreadable/ambiguous fields, unsaved changes.

---

# 62. `SubmissionReviewSummary`

Active entries, unused rows, validation issues, unreadable/ambiguous counts, image version, save state, submission consequence.

---

# PART XV — IMAGE COMPONENTS

# 63. `SourceImageViewer`

Zoom, pan, rotate display, reset, full screen, image-version indicator, loading/missing/access-expired states, privacy notice. Rotation does not alter original. States: Loading, Ready, Zoomed, Rotated, Full Screen, Access Expired, Missing, Corrupt, Replacement Required, Error.

---

# 64. `ImageToolbar`

Zoom in/out, reset, rotate left/right, full screen, version history, report issue. Must not obscure the image.

---

# 65. `ImageThumbnail`

Privacy-safe loading; fixed aspect container; fallback placeholder; no raw permanent URL; status overlay accessible in text.

---

# 66. `ImageQualityControl`

Usable, Blurry, Cropped, Wrong Document, Corrupt, Replacement Required. Short guidance for each state.

---

# 67. `ImageVersionHistory`

Version number, active status, upload time, uploader, replacement relationship, quality state. Original version visibly identified.

---

# PART XVI — QUEUE AND CLAIM COMPONENTS

# 68. `QueueItem`

Work type, record identifier, parent context, safe summary, status, priority, age, claim action. Variants: Card, Table Row, Compact, Mobile. States: Available, Claiming, Claimed By You, Claimed By Another, No Longer Eligible, Blocked, Completed.

---

# 69. `QueueList`

Filtering, sorting, pagination, loading skeletons, empty state, refresh, stale-list warning. Visible availability does not guarantee claim success.

---

# 70. `ClaimButton`

States: Claim Page, Claiming…, Claimed, Unavailable. Loading prevents duplicate activation; calm collision feedback.

---

# 71. `ClaimStatus`

Claimant context, claimed time, expiration, renewal, draft state, ownership.

Examples:

```text
Reserved for you until 4:15 PM
Claimed by another operator
```

---

# 72. `ClaimTimer`

Plain-language time; warning state; extension action; no aggressive animation; accessible announcement before expiration; expiration never presented as loss of saved work.

---

# 73. `ClaimConflictNotice`

```text
This page was just claimed by another user.

Choose another page or refresh the queue.
```

Actions: Claim Next Available; Return to Queue.

---

# PART XVII — SAVE AND RECOVERY COMPONENTS

# 74. `SaveStatus`

States: Saving, Saved, Unsaved Changes, Save Failed, Recovered Draft, Read-Only. Icon plus text; live announcement; no false Saved before durable confirmation.

---

# 75. `RecoveryBanner`

Explain what was recovered, original operator where applicable, what current user may do, how attribution is preserved.

---

# 76. `StaleVersionDialog`

Explanation; latest version; preservation options; reload; compare where supported; cancel. Must not silently discard unsaved work.

---

# 77. `UnsavedChangesGuard`

Stay; Save and Leave; Leave Without Saving. Leave Without Saving is visually secondary or dangerous depending on context.

---

# PART XVIII — STATUS AND FEEDBACK COMPONENTS

# 78. `StatusBadge`

Variants: Neutral, Information, Success, Warning, Danger, Pending, Archived. Short labels; no color-only meaning.

---

# 79. `InlineMessage`

Information, Success, Warning, Error. Icon, title where needed, message, optional action.

---

# 80. `Banner`

Page-level conditions: privacy, recovered draft, stale record, promotion failure, uploads closed, image replacement required. Dismissible only when dismissing does not hide continuing critical condition.

---

# 81. `Toast`

Brief confirmation only. Inappropriate as sole feedback for final match resolution, submission, promotion failure, user suspension, destructive action, or save failure.

---

# 82. `ProgressIndicator`

Determinate, Indeterminate, Step Progress, Background Processing. Text description; no fake precision.

---

# 83. `Skeleton`

Preserve layout during loading for dashboard card, table row, queue card, record header, candidate card, image frame, form. No aggressive animation under reduced motion.

---

# 84. `EmptyState`

Optional illustration/icon; clear title; explanation; primary next action; optional secondary guidance.

---

# 85. `ErrorState`

Plain title; safe explanation; preservation status; recovery action; correlation reference where useful.

---

# PART XIX — CARD AND PANEL COMPONENTS

# 86. `Card`

Variants: Standard, Interactive, Summary, Status, Evidence, Warning. Avoid nesting beyond two levels; interactive cards have clear focus; entire-card click must not conflict with internal controls.

---

# 87. `SummaryCard`

Label, primary value, context, optional trend/status/action. Do not display misleading trends when data is incomplete.

---

# 88. `RecordSummary`

Compact record identity: display ID, title or safe name, parent context, status, date, record type.

---

# 89. `DetailPanel`

Labeled fields, sections, read-only presentation, actions, responsive stacking.

---

# PART XX — TABLE COMPONENTS

# 90. `DataTable`

Semantic headers; sorting where approved; filtering; row selection; pagination; loading/empty; row actions; keyboard navigation; responsive alternative. Personal values masked where required. No horizontal scrolling for ordinary mobile use when card conversion is practical.

---

# 91. `ResponsiveRecordList`

Mobile alternative: primary identity, status, key metadata, one primary action, overflow menu.

---

# 92. `FilterBar`

Search, status/date/user filters, clear filters, result count. Mobile may use filter sheet or drawer.

---

# 93. `SortControl`

Only approved sortable fields. Unknown sorting never silently accepted.

---

# PART XXI — MATCHING COMPONENTS

# 94. `EvidenceComparison`

For each field: Field, Raw Value, Field Condition, Normalized Value, Warnings. Raw remains visually primary; normalized labeled as derived; unreadable/ambiguous remain visible; no system output styled as human approval.

---

# 95. `CandidateCard`

Safe canonical identity summary; confidence class; supporting/conflicting/weak signals; data freshness; selection control; detail expansion. States: Default, Hovered, Focused, Selected, Conflict, Unavailable, Previously Rejected. Selection does not finalize. Numeric scores secondary to explanations.

---

# 96. `ConfidenceIndicator`

Exact, High, Possible, Low, No Match, Conflict. Never alone authorize a merge. Conflict visually distinct from low confidence.

---

# 97. `MatchSignal`

Direction: Supports, Weakens, Conflicts, Neutral. Plain-language description; strength; source field. Example: Email matches exactly.

---

# 98. `SignalGroup`

Supporting; Conflicting; Additional Context. Conflict group appears before supporting when strong conflict exists.

---

# 99. `ConflictAlert`

State what conflicts, why it matters, what reviewer should do, what system will not do automatically.

---

# 100. `ResolutionPanel`

Outcome selection; selected candidate; reason; warning summary; downstream consequence; finalize action. States: No Selection, Candidate Selected, Create New Selected, More Information Selected, Conflict Escalation, Ready to Finalize, Saving, Finalized, Stale.

---

# 101. `ResolutionConfirmationDialog`

Selected outcome; selected person where applicable; evidence summary; conflicts; reason; downstream action; history-preservation statement; confirm and cancel.

---

# PART XXII — PROMOTION COMPONENTS

# 102. `PromotionStatus`

Operation type; state; attempts; canonical result; retry eligibility; provenance status. States: Pending, Running, Succeeded, Retry Needed, Failed, Needs Review, Cancelled.

---

# 103. `AttemptTimeline`

Attempt number, start/completion, outcome, safe error, retry timing, provider reference where approved.

---

# 104. `RetryAction`

Explain idempotency protection; show eligibility; distinguish automated vs manual retry; confirm high-risk; disable while attempt running.

---

# PART XXIII — USER AND ROLE COMPONENTS

# 105. `UserStatus`

Invited, Active, Suspended, Disabled, Revoked. Explanatory help for administrators.

---

# 106. `RoleBadge`

Uploader, Data Entry, Reviewer, Administrator, Owner. Role colors must not imply personal rank or value.

---

# 107. `RoleEditor`

Current roles visible; grant/revoke separated; expiration where supported; confirmation for elevated roles; reason for revocation.

---

# 108. `UserActionPanel`

Activate, suspend, restore, disable, revoke, inspect claims, inspect audit. High-risk actions use confirmation dialogs.

---

# PART XXIV — ADMINISTRATIVE COMPONENTS

# 109. `OperationalHealthCard`

One system area: queue, uploads, matching, promotions, background jobs, alerts. Current state, count, severity, last update, action.

---

# 110. `AlertCard`

Severity, title, safe summary, affected record, first/last detected, occurrence count, recommended action, status, actions. Acknowledgment and resolution remain separate.

---

# 111. `ErrorDetailPanel`

Error code, category, severity, subject, operation, retryability, occurrences, safe operator summary, resolution history. Never secrets or unrestricted provider payloads.

---

# 112. `AuditEventRow`

Event name, actor, subject, result, occurred time, correlation.

---

# 113. `AuditEventDetail`

Event metadata, actor, subject, object, result, reason, occurred/recorded time, safe structured payload, correlation links. Read-only.

---

# 114. `Timeline`

Chronological order clearly stated; current effective event identifiable; accessible list semantics; not color-only.

---

# PART XXV — DIALOGS, DRAWERS, AND POPOVERS

# 115. `Dialog`

Sizes: Small, Medium, Large, Full-Screen Mobile. Clear title; focus containment; Escape where safe; focus return; labeled close; primary and cancel; no nested dialogs except exceptional approved cases.

---

# 116. `ConfirmationDialog`

Risk levels: Medium, High, Destructive. Must state action, consequence, history behavior, reversibility, affected record, required reason where applicable.

---

# 117. `Drawer`

Filters, secondary detail, candidate information, navigation, help. Must not hide unsaved work state.

---

# 118. `Popover`

Short explanations, secondary controls, date selection, compact menus. Not for critical long-form workflow content.

---

# PART XXVI — HELP COMPONENTS

# 119. `HelpText`

Short persistent guidance near a control.

---

# 120. `Tooltip`

Available by keyboard; remain readable; not contain essential instructions unavailable elsewhere; avoid exposing personal information.

---

# 121. `DefinitionPopover`

Terms such as Claim, Unknown, Ambiguous, Canonical Person, Promotion, Provenance.

---

# 122. `FirstUseGuide`

Short; dismissible; available again; role-aware; no forced multi-step tour during urgent work; does not obscure source data.

---

# PART XXVII — COMPONENT STATE STANDARD

# 123. Universal Interactive States

Default, Hover, Focus, Active, Disabled, Loading, Error. Where applicable: Selected, Expanded, Read-Only, Success, Warning, Stale.

---

# 124. Disabled-State Rule

Communicate why disabled when not obvious. Do not use disabled controls as a substitute for explaining permissions.

---

# 125. Read-Only State

Read-only is not the same as disabled. Remain legible; permit text selection where safe; show history access; explain why editing unavailable; avoid appearing broken.

---

# PART XXVIII — COMPOSITION RULES

# 126. Transcription Screen Composition

```text
AppShell
└── PageContainer: Full
    ├── PageHeader
    ├── RecoveryBanner
    ├── SplitPane
    │   ├── SourceImageViewer
    │   └── EntryGrid
    │       └── EntryRow × 10
    └── StickyActionBar
        ├── SaveStatus
        ├── ClaimStatus
        └── ButtonGroup
```

---

# 127. Match Screen Composition

```text
AppShell
└── PageContainer: Full
    ├── PageHeader
    ├── ConflictAlert
    ├── SplitPane: Three-Pane
    │   ├── EvidenceComparison
    │   ├── CandidateList
    │   │   └── CandidateCard
    │   │       └── SignalGroup
    │   └── ResolutionPanel
    └── StickyActionBar
```

---

# 128. Administrative Screen Composition

```text
AppShell
└── PageContainer: Workspace
    ├── PageHeader
    ├── SummaryCard Grid
    ├── FilterBar
    ├── DataTable
    └── Pagination
```

---

# PART XXIX — RESPONSIVE COMPONENT BEHAVIOR

# 129. Responsive Transformation Rules

Tables → ResponsiveRecordList on mobile. Split panes → adjustable/tabbed on tablet; stacked on mobile. Dialogs → full-screen or bottom-sheet on mobile. Actions → StickyActionBar plus overflow on mobile.

---

# 130. Small-Mobile Behavior

Preserve field readability; stack controls; avoid two-column forms; full-width buttons where appropriate; preserve source-image access; prevent horizontal form overflow.

---

# PART XXX — ACCESSIBILITY CONTRACTS

# 131. Component Accessibility Requirements

Every component must document: semantic element, accessible name, keyboard, focus, announcement, error, disabled/read-only, touch target, contrast, reduced-motion where applicable.

---

# 132. Focus Indicator

Visible on all interactive elements; not removed; surrounds actionable area; distinct from selected state.

---

# 133. Live Regions

Use carefully for save-state, upload completion, claim status, validation summary, background completion, retry result. Avoid announcing every keystroke or autosave attempt.

---

# 134. Error Summary

Identify error count; link to affected controls; receive focus on failed submission; preserve field-level errors.

---

# 135. Modal Accessibility

Initial focus; trap focus; accessible title; restore focus; Escape where safe; prevent background interaction. High-risk confirmations may require explicit action rather than outside-click dismissal.

---

# PART XXXI — PRIVACY CONTRACTS

# 136. Personal Data Display

Minimum required personal data. Queue cards may mask email/phone. Audit list should avoid copying raw values. Error banners prefer record IDs. Notifications avoid full PII.

---

# 137. Copy-to-Clipboard

Role-restricted where needed; clearly identify copied content; audit where policy requires; confirmation without exposing value in a toast.

---

# 138. Sensitive Screen Protection

Consider no-cache headers, inactivity protection, privacy notices, minimized browser-title PII, safe URL paths, no analytics capture of content, no permanent image URLs.

---

# PART XXXII — COMPONENT DOCUMENTATION TEMPLATE

# 139. Required Component Specification

```text
Component ID
Component Name
Purpose
Domain Ownership
Used On
Variants
Properties
Content Rules
States
Default Behavior
Responsive Behavior
Keyboard Behavior
Screen-Reader Behavior
Focus Behavior
Validation Behavior
Error Behavior
Privacy Rules
Audit Impact
Analytics Rules
Dependencies
Composition Examples
Acceptance Tests
Traceability
```

---

# PART XXXIII — COMPONENT REGISTRY

# 140. Canonical Component Categories

## Foundations

```text
Design Tokens
Typography
Color
Spacing
Layout
Motion
Iconography
```

## Shell and Layout

```text
AppShell
NavigationRail
MobileNavigation
PageContainer
PageHeader
SectionHeader
Breadcrumbs
SplitPane
StickyActionBar
```

## Actions

```text
Button
ButtonGroup
OverflowMenu
Tabs
Pagination
```

## Forms

```text
FieldGroup
TextInput
TextArea
Select
RadioGroup
Checkbox
DateInput
NumberInput
SearchInput
FilePicker
```

## Intake

```text
PreferenceControl
FieldConditionControl
RowActivationControl
EntryRow
EntryGrid
TranscriptionProgress
SubmissionReviewSummary
```

## Images

```text
SourceImageViewer
ImageToolbar
ImageThumbnail
ImageQualityControl
ImageVersionHistory
```

## Queue and Claims

```text
QueueItem
QueueList
ClaimButton
ClaimStatus
ClaimTimer
ClaimConflictNotice
```

## Save and Recovery

```text
SaveStatus
RecoveryBanner
StaleVersionDialog
UnsavedChangesGuard
```

## Feedback

```text
StatusBadge
InlineMessage
Banner
Toast
ProgressIndicator
Skeleton
EmptyState
ErrorState
```

## Data Display

```text
Card
SummaryCard
RecordSummary
DetailPanel
DataTable
ResponsiveRecordList
FilterBar
SortControl
Timeline
```

## Matching

```text
EvidenceComparison
CandidateCard
ConfidenceIndicator
MatchSignal
SignalGroup
ConflictAlert
ResolutionPanel
ResolutionConfirmationDialog
```

## Promotion

```text
PromotionStatus
AttemptTimeline
RetryAction
```

## Users and Roles

```text
UserStatus
RoleBadge
RoleEditor
UserActionPanel
```

## Administration

```text
OperationalHealthCard
AlertCard
ErrorDetailPanel
AuditEventRow
AuditEventDetail
```

## Overlays

```text
Dialog
ConfirmationDialog
Drawer
Popover
```

## Help

```text
HelpText
Tooltip
DefinitionPopover
FirstUseGuide
```

---

# PART XXXIV — COMPONENT TESTING

# 141. Required Test Categories

Rendering, variants, states, keyboard, focus, accessible name, validation, error, disabled, read-only, responsive, content overflow, reduced motion, high contrast, privacy masking, event handling, duplicate activation prevention.

---

# 142. Visual Regression Testing

Default, focus, error, loading, mobile, desktop, long content, high zoom, reduced motion where visible.

---

# 143. Accessibility Testing

Automated checks, keyboard-only, screen-reader, zoom/reflow, contrast, touch-target, error recovery, time-limit. Automated checks do not replace manual testing.

---

# 144. Component Acceptance Criteria

All required variants exist; states documented; keyboard and focus work; responsive works; accessibility checks pass; privacy respected; loading and error states exist; no business rule hidden solely in visual presentation; traceability recorded.

---

# PART XXXV — STORY AND PROTOTYPE REQUIREMENTS

# 145. Isolated Component Preview

Permit inspection of every component, variant, state, mobile/desktop widths, long/error/loading content, accessibility notes. Exact tool deferred.

---

# 146. Required Workflow Prototypes

1. Create Batch
2. Upload Pages
3. Prepare Page
4. Claim Page
5. Transcribe Page
6. Recover Draft
7. Submit Page
8. Review Transcription
9. Review Match
10. Finalize Resolution
11. Retry Promotion
12. Suspend User
13. Release Claim
14. Resolve Alert

---

# PART XXXVI — CONTENT STANDARD

# 147. Button Labels

Use verbs. Good: Create Batch, Upload Pages, Claim Page, Save Draft, Submit Page, Finalize Match, Retry Promotion, Suspend User. Avoid vague: Continue, Confirm, OK, Process unless context is unmistakable.

---

# 148. Status Labels

Use consistent case. Recommended: Ready for Transcription, Waiting for Review, Needs Image Replacement, Retry Needed. Avoid exposing database enum formatting.

---

# 149. Helper Text

Explain purpose; prevent errors; remain concise; avoid legalistic language; avoid blaming the user.

---

# 150. Error Language

Prefer: We could not save this draft. / This page changed while you were working. Avoid: You entered invalid data. / User error.

---

# PART XXXVII — DESIGN SYSTEM GOVERNANCE

# 151. Adding a New Component

Only when existing component cannot support the need; distinct semantic purpose; accessibility and responsive defined; states defined; duplication reviewed; traceability documented.

---

# 152. Modifying a Component

Document reason, affected screens/variants, accessibility impact, backward compatibility, migration, visual-regression impact.

---

# 153. Component Deprecation

Requires replacement, migration guidance, usage inventory, removal timeline, compatibility period, documentation update.

---

# 154. Token Changes

Evaluate across whole application. A token must not be repurposed silently.

---

# PART XXXVIII — LOCKED COMPONENT DECISIONS

# 155. Locked Decisions

1. Components consume semantic tokens rather than scattered raw values.
2. Primitive, semantic, and component tokens remain distinct.
3. The interface targets WCAG 2.2 AA.
4. Color is never the sole carrier of meaning.
5. Mobile is a first-class design surface.
6. Core touch targets are approximately 44 by 44 CSS pixels or larger.
7. Raw and normalized values use distinguishable presentation.
8. System suggestions are labeled as system-generated.
9. Approved decisions are visually distinct from suggestions.
10. Source images use a dedicated private viewer.
11. Image rotation does not alter the original.
12. Volunteer and Email List use a three-value Preference Control.
13. Preference Control includes Yes, No, and Unknown.
14. Unknown is never silently converted to No.
15. Field conditions have a dedicated control.
16. Unreadable and Ambiguous are visible choices.
17. The Entry Grid supports up to ten row positions.
18. Blank rows remain inactive rather than becoming empty entries.
19. Entry rows convert to mobile cards or another mobile-appropriate structure.
20. Autosave state uses a persistent Save Status component.
21. Claim status and expiration use dedicated components.
22. Claim expiration avoids panic-inducing animation.
23. Queue visibility does not guarantee claim success.
24. Candidate selection does not finalize identity.
25. Candidate Cards explain supporting and conflicting signals.
26. Numeric match scores remain secondary.
27. Strong conflicts use a persistent Conflict Alert.
28. Final resolution uses a Resolution Confirmation Dialog.
29. Promotion retries explain duplicate protection.
30. High-risk administrative actions use explicit confirmation.
31. Read-only is visually distinct from disabled.
32. Disabled controls explain why when needed.
33. Important outcomes do not rely only on temporary toasts.
34. Tables have mobile alternatives.
35. Dialogs manage focus and restore it.
36. Loading states preserve layout.
37. Empty states explain what happens next.
38. Error states explain whether work was preserved.
39. Personal data is minimized in compact components.
40. Raw personal data is prohibited from analytics.
41. Component documentation is required.
42. Component state coverage is required.
43. Keyboard testing is required.
44. Screen-reader testing is required.
45. Visual-regression testing is required.
46. Components must support long content and high zoom.
47. Reduced-motion support is required.
48. New components require governance review.
49. Token names describe purpose, not appearance.
50. The component system prioritizes calm, accurate work over visual spectacle.

---

# PART XXXIX — DEFERRED DESIGN DECISIONS

# 156. Open Decisions

### `COMP-DEC-001`

Exact frontend component framework.

### `COMP-DEC-002`

Exact CSS architecture.

### `COMP-DEC-003`

Exact design-token storage format.

### `COMP-DEC-004`

Exact primitive color values.

### `COMP-DEC-005`

Exact font family.

### `COMP-DEC-006`

Exact typography values.

### `COMP-DEC-007`

Exact spacing values after prototype validation.

### `COMP-DEC-008`

Exact responsive breakpoints.

### `COMP-DEC-009`

Exact border radii.

### `COMP-DEC-010`

Exact shadow values.

### `COMP-DEC-011`

Exact icon library.

### `COMP-DEC-012`

Exact isolated component-preview tool.

### `COMP-DEC-013`

Whether the app supports comfortable and compact density at launch.

### `COMP-DEC-014`

Whether users may choose density preference.

### `COMP-DEC-015`

Whether dark mode is included in Version 1.

### `COMP-DEC-016`

Whether the transcription split pane is user-resizable.

### `COMP-DEC-017`

Whether Entry Grid uses semantic table or ARIA grid behavior.

### `COMP-DEC-018`

Exact mobile image-and-entry switching pattern.

### `COMP-DEC-019`

Exact Candidate Card expansion behavior.

### `COMP-DEC-020`

Exact audit payload viewer format.

### `COMP-DEC-021`

Whether report charts are included at launch.

### `COMP-DEC-022`

Exact status icon set.

### `COMP-DEC-023`

Exact animation durations.

### `COMP-DEC-024`

Exact handling of browser high-contrast modes.

### `COMP-DEC-025`

Whether component documentation is generated, hand-maintained, or hybrid.

These decisions must be resolved through Volume 13, implementation packages, and prototype review rather than improvised during coding.

---

# PART XL — TRACEABILITY REQUIREMENTS

# 157. Component-to-Screen Traceability

Every component must identify the screens where it is used.

---

# 158. Component-to-Domain Traceability

Examples:

```text
ClaimTimer → Claim Domain → CLAIM-RULE-003 → CLAIM-RULE-006
CandidateCard → Matching Domain → MATCH-RULE-001 → MATCH-RULE-002 → MATCH-RULE-008
SaveStatus → Draft Domain → DRAFT-RULE-004 → DRAFT-RULE-006
```

---

# 159. Component-to-API Traceability

Examples:

```text
ClaimButton → POST /api/v1/queue/{id}/claim
RetryAction → POST /api/v1/promotions/{id}/retry
RoleEditor → POST /api/v1/users/{id}/roles → DELETE /api/v1/users/{id}/roles/{role}
```

---

# PART XLI — VALIDATION REQUIREMENTS

# 160. Design-System Validation

Before implementation begins, prove every major screen has required reusable components; every business state has visual representation; every mutation has an action component; every high-risk mutation has confirmation; every draft workflow has save state; every claim workflow has claim state; every personal-data surface has privacy rules; loading/empty/error states have components; every desktop table has mobile behavior; every component has accessibility and responsive behavior, tests, and traceability.

---

# 161. Design-System Anti-Drift Review

Regularly check for duplicate button styles, status badges, inconsistent spacing/dialogs/queue cards, raw color values, unexplained icon-only actions, inconsistent preference/field-condition/error language, inaccessible one-offs, screens bypassing the component library.

---

# PART XLII — VOLUME 12 READINESS

# 162. Completion Checklist

Volume 12 is complete when design doctrine, token architecture, color/typography/spacing/responsive/motion roles, foundational/form/intake/image/queue/save/matching/promotion/admin components, dialogs and feedback, accessibility and privacy contracts, testing and governance rules, locked and deferred decisions, and traceability requirements are defined.

---

# 163. Readiness Score

| Area | Readiness |
| --- | ---: |
| Design doctrine | 100% |
| Token architecture | 100% |
| Color roles | 98% |
| Typography roles | 98% |
| Spacing and density | 98% |
| Responsive structure | 99% |
| Motion | 98% |
| Layout components | 100% |
| Navigation components | 100% |
| Form components | 100% |
| Intake controls | 100% |
| Image components | 100% |
| Queue and claim components | 100% |
| Save and recovery | 100% |
| Feedback components | 100% |
| Matching components | 100% |
| Promotion components | 100% |
| Administrative components | 99% |
| Accessibility contracts | 100% |
| Privacy contracts | 100% |
| Component testing | 100% |
| Governance | 100% |
| Traceability | 98% |

**Overall Volume 12 Design Readiness**

```text
99%
```

---

# 164. Next Governing Build

The next documentation build is:

```text
PEOPLE-VOLUME-13-CANONICAL-PLATFORM-STANDARDS-1.0
```

Volume 13 will define shared engineering and integration rules across the entire application. No application code should be written during Volume 13.

The next build is **Volume 13 — Canonical Platform Standards**. That volume will unify database, API, UI, and component rules into one engineering doctrine so Cursor cannot improvise project structure, security boundaries, dependencies, environment handling, or integration patterns during implementation.

---

## Document Control

| Field | Value |
| --- | --- |
| Canonical path | `docs/volumes/volume-12-component-library/VOLUME_12_COMPONENT_LIBRARY_AND_DESIGN_SYSTEM.md` |
| Legacy pointer | `docs/13_component_library/VOLUME_12_COMPONENT_LIBRARY_AND_DESIGN_SYSTEM.md` |
| Encoding | UTF-8 |
| Status | DESIGN COMPLETE — IMPLEMENTATION NOT AUTHORIZED |
| Build mode | DOCUMENTATION ONLY — no React, CSS, Storybook, or tokens package |
