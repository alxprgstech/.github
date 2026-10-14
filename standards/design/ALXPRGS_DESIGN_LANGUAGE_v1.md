# ALXPRGS Design Language v1

> **Canonical cross-project standard.** This document defines the final shared design language for the entire ALXPRGS infrastructure ecosystem. It is normative where relevant, but it is **not** a claim that any existing project has already implemented every rule. Each project uses a concise, scoped local specification as described in §4.

**Status:** Final specification  
**Target:** All ALXPRGS infrastructure projects, services and interfaces  
**Primary surfaces:** Public websites, applications, dashboards, workspaces, documentation, status pages, settings, operator/developer tools and other relevant human-facing interfaces  
**Design orientation:** Dark-first, light-complete, accessible, performant, motion-aware  
**Audience:** Project owner, collaborators, contributors and implementation agents across ALXPRGS  
**Implementation approach:** Framework-agnostic standard; project-appropriate stack, with React + TypeScript + Tailwind CSS as a recommended option for suitable web apps  
**Identity architecture:** Central ALXPRGS SSO for protected services; no unnecessary duplicate local login systems  
**Quality objective:** Lighthouse 100/100 across all applicable categories; measurable performance, accessibility and security gates  

---

# 1. Identity and design inspiration

ALXPRGS is a family of infrastructure projects and services, not one application or a commercial SaaS template. The same identifiable design language must carry across every applicable ALXPRGS surface without forcing unrelated products into the same screen layout.

The visual language draws selectively from:

**WorkOS** — calm identity flows and interactive technical compositions, where relevant.

**Linear** — useful information density, clear hierarchy, keyboard workflows and restrained application chrome.

**Vercel / Geist** — typography, developer-oriented clarity and reusable design-system discipline.

**Cloudflare** — practical infrastructure operations, semantic theming and subtle, purposeful motion.

These are references, not templates to copy. Do not visually imitate any single product. ALXPRGS must remain recognisably ALXPRGS whether a screen belongs to identity, hosting, monitoring, an internal tool, a public site, a dashboard or a future service.

An API-only, automation-only or headless infrastructure project is still part of ALXPRGS, but it must not be required to invent a user interface merely to satisfy this document. Apply the rules to its actual human-facing surfaces, including documentation, administrative utilities, status pages and any future frontend.

---

# 2. Core design statement

> ALXPRGS is a dark-first, fast, accessible and motion-aware infrastructure design language: calm where people need clarity, dense where operators need control, visually technical without looking like a terminal, and consistent across independently built services.

The system must communicate five qualities:

**Technical.** Built for authentic engineering and real infrastructure, not decorative complexity.

**Calm.** The interface explains a task rather than exposing unnecessary implementation details.

**Alive.** Visible but purposeful responses provide state, continuity and feedback.

**Fast.** Real performance and perceived responsiveness matter more than visual spectacle.

**Coherent.** Applications may differ in purpose and density while still clearly belonging to one ecosystem.

---

# 3. Design principles

## 3.1 Content before chrome

Application content matters more than containers, borders or decoration. Do not place every section inside its own card.

Structure should primarily come from spacing, hierarchy, typography, background levels and alignment. Borders are secondary.

## 3.2 Motion communicates state

Motion communicates state changes, navigation, hierarchy, completion, causality and spatial relationships. It must not exist merely to entertain or slow the user down. Static content and nonvisual projects do not need artificial animation.

## 3.3 Complexity is the system's responsibility

Ordinary users must understand what they can do, what is happening and what to do next without understanding the infrastructure underneath.

Do not make them interpret protocol names, RFC numbers, UUIDs, internal flags, raw errors, event IDs, deployment hashes, queue semantics, cryptographic algorithms, tracing identifiers or implementation terminology in order to perform routine tasks.

Expose technical details contextually when they help developers, administrators or troubleshooting. Complexity is not hidden from the people who actually need it.

## 3.4 Security, privacy and reliability are not negotiable for visual convenience

A redesign must not weaken applicable security and operational controls: identity and access validation, permissions, safe redirects, session handling, request integrity, CSRF protections, origin and input validation, secure storage, secrets handling, data privacy, auditability, destructive-operation safeguards, accessibility, error recovery or reliable service behaviour.

A visual or frontend change must preserve established API contracts, authentication boundaries, authorization checks, data integrity, security requirements and operational invariants. **Server-side enforcement cannot be replaced by UI-only restrictions.**

If a project uses OIDC, PKCE, MFA, WebAuthn, step-up authentication or another security protocol, those controls also remain intact. These are **conditional technical requirements**, not features that every ALXPRGS project must implement independently.

## 3.5 Density depends on context

Public-facing and guided tasks are spacious. Standard applications and settings use moderate density. Operator consoles, administration and data-rich development tools may be intentionally dense.

Shared tokens, typography, components and interaction conventions unite these surfaces; identical layouts do not.

## 3.6 Consistency without unnecessary features

Build only the interface patterns and components useful to the current project or plausibly needed in its near-term scope. Do not add dashboards, authentication forms, complex charts, command palettes, decorative scenes, tables or animations merely because examples appear here.

## 3.7 Quality is a design property

Accessibility, responsiveness, performance, stability, security and Lighthouse outcomes are expected from the beginning. Do not postpone fundamental quality work until after a visual redesign.

---

# 4. Universal standard and project-local adoption

This file is the **canonical, final ALXPRGS design standard**. It is intended to be provided at the very beginning of any new ALXPRGS project, including projects that have no code, UI, routing, tokens or chosen framework yet.

It is **not** a report about an existing codebase, a migration checklist for one frontend, or evidence that any particular project has implemented the rules.

### 4.1 Applicability

Every ALXPRGS project must follow the principles relevant to its actual scope. A web application follows applicable visual, interaction, theme, accessibility and performance rules; a documentation site follows documentation-relevant rules; a headless service follows relevant identity, naming, branding, security and engineering-quality rules **where it has a human-facing surface**. A project does not need to implement irrelevant features just to satisfy the standard.

### 4.2 Required project-start workflow

At project inception, the project owner or implementation agent must:

1. Inspect the intended purpose and known constraints of **this specific project**. If no code exists, work from its stated requirements rather than inventing an inherited implementation.
2. Decide which categories are **required now**, **reasonably foreseeable** or **not applicable**: public pages, app shell, data entry, operations, dashboards, identity integration, administration, documentation, responsive UI and so on.
3. Create a short local file, preferably `docs/design/PROJECT_DESIGN.md` (or the project's established equivalent), containing **only the rules, decisions, tokens, patterns and components relevant or reasonably likely to become relevant to this project**. Link back to this canonical standard.
4. Carry forward the non-negotiable baseline wherever applicable: official ALXPRGS identity, coherent semantic design tokens, user-accessible dark/light/system theming for graphical web UIs, accessibility, responsive design, truthful feedback, security boundaries, speed and quality gates.
5. Specify the project's own information architecture, core screen types, interaction density, required component subset, optional visualisation approach, technology choices and documented deviations. Do not copy all 78 sections into the local file or load irrelevant SSO/admin examples into the working context.
6. During implementation, consult **the project-local specification first**, and refer to specific canonical sections only when needed. Update the local specification when the project scope changes; keep it concise.

### 4.3 Scope and precedence

The canonical ALXPRGS standard establishes shared identity and baseline expectations. A project-local document selects relevant implementation guidance; **it cannot silently override mandatory accessibility, security, brand or quality requirements**.

If a constraint makes a shared rule unsuitable, record the rule, technical reason, replacement behaviour, affected surfaces and approval in the project-local document. Never treat absence from the local summary as permission to ignore an applicable rule.

The same canonical document may therefore guide many different projects while each project's active working context stays small.

---

# 5. Brand

## 5.1 Official logo

The existing ALXPRGS logo assets are the canonical brand identity. Use the actual ALXPRGS logo; do not recreate the brand as a letter `A` inside an arbitrary blue square, substitute a text-only imitation or generate an unrelated mark.

Official available assets:

- **BIMI SVG:** https://assets.alxprgs.tech/bimi/logo.svg
- **Full avatar:** https://assets.alxprgs.tech/logo-avatar-full.png
- **Icon avatar:** https://assets.alxprgs.tech/logo-avatar-icon.png
- **PNG logo:** https://assets.alxprgs.tech/logo.png
- **SVG logo:** https://assets.alxprgs.tech/logo.svg

Select the appropriate official format and variant for the actual surface. Prefer the SVG when suitable. If external asset availability would jeopardise critical UI, bundle/cache approved assets according to project deployment policy. The BIMI-specific SVG is not automatically the optimal UI asset.

## 5.2 Logo roles

Use the full mark or wordmark when sufficient horizontal space exists. Use the official icon mark for favicon, collapsed navigation, mobile navigation, compact identity elements, application icons and loading/transition contexts as appropriate.

The logo must not be recoloured, distorted, restyled or covered in arbitrary effects.

## 5.3 Brand colour

Blue remains the primary ALXPRGS interface colour.

Cyan may appear as a secondary visual accent in diagrams, glows and infrastructure visualisations.

Green must not become a competing primary UI colour. It remains primarily semantic: success, healthy state, verified state, active state.

Other colours communicate semantic meaning, not competing product identities.

---

# 6. Themes

Graphical ALXPRGS web interfaces support three user preferences:

- `Dark`
- `Light`
- `System`

Dark is the default visual reference and design priority. Light is a fully supported, accessible theme rather than an afterthought. System follows the user's operating-system preference.

Theme settings should persist appropriately for the product and must not cause a visible startup flash. Where theming has no meaning (for example, a headless service), this section does not require adding a graphical interface.

---

# 7. Colour system

Colours must be exposed through semantic design tokens.

Components must not depend directly on arbitrary palette values.

## Dark theme

| Token | Value | Purpose |
|---|---:|---|
| `canvas` | `#090A0C` | Main application background |
| `surface-1` | `#0F1115` | Primary surfaces |
| `surface-2` | `#14171D` | Raised/interactive surfaces |
| `surface-3` | `#1A1E26` | Strong elevation/selected surfaces |
| `surface-hover` | `#20252E` | Neutral hover |
| `border-subtle` | `#20242C` | Quiet separators |
| `border-default` | `#2A303A` | Controls and visible boundaries |
| `text-primary` | `#F5F7FA` | Main content |
| `text-secondary` | `#B6BEC9` | Secondary copy |
| `text-tertiary` | `#7E8896` | Metadata |
| `brand` | `#3B82F6` | Primary actions |
| `brand-hover` | `#5594F8` | Primary hover |
| `brand-active` | `#2563EB` | Pressed state |
| `accent-cyan` | `#22D3EE` | Decorative technical visualisation |
| `success` | `#22C55E` | Success |
| `warning` | `#F59E0B` | Warning |
| `danger` | `#EF4444` | Failure/destructive |
| `focus` | `#60A5FA` | Keyboard focus |

The primary canvas is almost black, not absolute `#000000`.

Pure black may only be used for isolated deepest layers or media treatment.

---

## Light theme

| Token | Value | Purpose |
|---|---:|---|
| `canvas` | `#F7F8FA` | Main application background |
| `surface-1` | `#FFFFFF` | Primary surfaces |
| `surface-2` | `#F1F3F5` | Secondary surfaces |
| `surface-3` | `#E9EDF2` | Raised/selected surfaces |
| `surface-hover` | `#E7EBF0` | Hover |
| `border-subtle` | `#E2E6EB` | Separators |
| `border-default` | `#CBD2DA` | Controls |
| `text-primary` | `#111318` | Main content |
| `text-secondary` | `#4B5563` | Secondary copy |
| `text-tertiary` | `#77808C` | Metadata |
| `brand` | `#2563EB` | Primary action |
| `brand-hover` | `#1D4ED8` | Primary hover |
| `brand-active` | `#1E40AF` | Pressed |
| `accent-cyan` | `#0891B2` | Decorative accent |
| `success` | `#16A34A` | Success |
| `warning` | `#D97706` | Warning |
| `danger` | `#DC2626` | Failure |
| `focus` | `#2563EB` | Focus |

---

# 8. Typography

## Primary typeface

**Geist Sans**

For web surfaces, self-host with the application. Do not depend on Google Fonts or another third-party runtime font request to render essential text.

## Technical typeface

**Geist Mono**

Use for client IDs, request IDs, scopes, IP addresses, timestamps where technical alignment matters, audit values, recovery codes, hashes, build IDs, command output and code fragments **when those values occur in the current product**.

Do not use monospace merely to make a page look technical.

## Typography scale

| Role | Size | Weight | Line height |
|---|---:|---:|---:|
| Display | 36 px | 600 | 44 px |
| Page title | 28 px | 600 | 36 px |
| Section title | 20 px | 600 | 28 px |
| Card title | 16 px | 600 | 24 px |
| Body | 14 px | 400 | 21 px |
| Body large | 16 px | 400 | 24 px |
| Label | 13 px | 500 | 18 px |
| Metadata | 12 px | 400 | 17 px |
| Mono | 13 px | 400 | 19 px |

Prominent guided-page headings may use 30–36 px depending on viewport. Dense operator interfaces favour 14 px body text. These are default tokens; readable scaling and accessibility take priority over rigid pixels.

---

# 9. Spacing

Use a 4 px base grid.

Canonical spacing values:

`4 / 8 / 12 / 16 / 20 / 24 / 32 / 40 / 48 / 64`

Arbitrary spacing values should be rare.

Focused tasks and guided forms prefer 24–32 px section separation.

Dense operational layouts commonly use 12–20 px.

---

# 10. Shape language

ALXPRGS uses moderately soft geometry.

It must not look either excessively corporate-square or toy-like.

| Token | Radius |
|---|---:|
| `radius-xs` | 6 px |
| `radius-sm` | 8 px |
| `radius-md` | 10 px |
| `radius-lg` | 14 px |
| `radius-xl` | 18 px |
| `radius-full` | 9999 px |

Default controls use approximately 10 px.

Normal cards use 12–14 px.

Large focused task and dialog surfaces may use 14–18 px.

Pills are reserved for elements that genuinely behave like pills:

status, filters, tags and compact segmented controls.

---

# 11. Borders and elevation

Most hierarchy should not rely on heavy borders.

Use subtle 1 px borders.

Elevation should be created through a combination of:

surface colour, border contrast and restrained shadow.

Dark-mode shadows are intentionally subtle.

Avoid large glowing card shadows.

Strong glow is allowed only in decorative visualisations.

---

# 12. Iconography

Functional icons use **Lucide**.

Default stroke weight should remain visually close to Lucide's native appearance.

Common sizes:

16 px for compact actions.

18 px for normal controls.

20 px for navigation.

24 px for larger state indicators.

System glyph characters such as:

`✓`, `✕`, `⚠`, `+`

must not substitute for a proper icon when Lucide contains an appropriate symbol.

Emoji should not be used as functional UI iconography.

The ALXPRGS logo is brand artwork and is not part of the Lucide system.

---

# 13. Motion system

For interactive graphical applications, motion is a first-class design primitive, not a requirement to animate every component.

Recommended durations:

| Motion | Duration |
|---|---:|
| Micro interaction | 100–140 ms |
| Hover/state change | 140–180 ms |
| Normal entrance | 180–240 ms |
| Dialog/layout change | 220–320 ms |
| Large contextual transition | 280–360 ms |

Routine UI transitions should almost never exceed 400 ms.

## Motion character

ALXPRGS motion should feel responsive, smooth, slightly elastic where appropriate and technically precise. Avoid exaggerated bouncing.

## Layout motion

When content height changes, a container should generally resize smoothly if motion does not obstruct interaction.

Example: a task form expands to reveal additional required fields. It should not suddenly jump between heights without context.

## Shared state motion

Use shared-element motion where spatial continuity makes interaction clearer: active navigation indicator, selected tab background, expanding configuration section.

## Success motion

Success should be visible without becoming celebratory marketing. A copy icon may morph to a check; saved settings may receive a subtle confirmation animation. No confetti for routine operations.

---

# 14. Reduced motion

`prefers-reduced-motion` is mandatory for motion-enabled graphical web interfaces.

Reduced-motion mode should remove cursor-following movement, large translation, parallax, nonessential layout travel and repeated decorative motion.

Opacity changes and immediate state replacement may remain where necessary. Essential information cannot depend on animation.


---

# 15. Motion performance

Continuous animation must not behave like a permanently running game renderer.

Interactive backgrounds and complex visualisations must:

- Pause when `document.visibilityState !== "visible"`.
- Reduce complexity on constrained devices.
- Avoid repeated synchronous layout measurement.
- Avoid expensive large-area blur animation.
- Avoid unnecessary React rerender loops in React-based projects.
- Disable or simplify themselves under `prefers-reduced-motion`.
- Defer or omit decorative work if it competes with initial rendering, input responsiveness, battery or Lighthouse quality targets.

Visual quality is not permission to continuously consume significant CPU/GPU resources. Prefer static representations when animations add no meaningful information.

---

# 16. Surface families

ALXPRGS projects may have one or several of these surface families. They are variations of one design language rather than independent themes:

**Public / informational.** Clear, welcoming, low-density landing, documentation, status and explanatory pages.

**Product / task-focused.** Moderate-density applications, settings, forms, account-linked workflows and resource management.

**Operational / developer.** Dense dashboards, control panels, observability, infrastructure operations, administration and internal tools.

**Identity / security.** Dedicated central SSO and sensitive security workflows, implemented only where the service is responsible for them.

Not every project needs every family. Choose only the relevant families in the project's local design specification.

---

# 17. Adaptive page layouts

Layout is selected by **purpose and content**, not a universal sign-in-page template.

Useful layout patterns include:

- **Focused:** one primary task or guided workflow with restrained supporting information.
- **Split:** main task/content on one side, contextual illustration, live preview, help or technical visualisation on the other.
- **Application shell:** navigation plus content area for multi-route services.
- **Dashboard / workspace:** grids, tables and tool panels based on operational density.
- **Document / status:** readable text column, strong semantic hierarchy and meaningful navigation.

Use adaptive layouts that remain usable across narrow, wide and short displays. A split pattern may become a single column; secondary visual material must never displace primary content.

`1024 px` can be a useful **starting point** for desktop split layouts, but switch when the actual content requires it. No service must introduce a decorative split-screen merely to look like SSO.

---

# 18. Contextual technical visualisations

Infrastructure visualisations are **optional** and must be relevant to the current project.

Where useful, they may combine:

- Abstract grid/mesh structure.
- Real or conceptually accurate infrastructure topology.
- Service-to-service relationships or application dependencies.
- Request or event flow signals.
- Subtle animated paths, state indicators and abstract data packets.
- Minimal code/data fragments when they convey meaning.
- Cursor-reactive lighting and restrained blue/cyan glow.

The subject of a visualisation must match the project: for example, a service map for monitoring, deployment topology for hosting, task progression for automation or an identity flow for the SSO project. **Never hardcode an ALXPRGS SSO core node into unrelated projects.**

A composition should suggest real, purposeful infrastructure rather than a marketing hero, cryptocurrency dashboard, hacker terminal, cyberpunk game or generic AI gradient mesh.

A visualisation must never imply live health, network activity, performance, capacity or security states when it uses fabricated data. Label mock/demo states explicitly.

Keep informative views accessible via labels, text or alternate representations. Decorative scenes are not required, and must degrade gracefully or disappear on small and low-power devices.

---

# 19. Page and task hierarchy

Most ALXPRGS pages should have a calm, legible hierarchy. Include **only** the elements appropriate to the task:

1. Official ALXPRGS or product identity where appropriate.
2. Navigation or contextual destination.
3. Clear page heading.
4. Short explanation or current system state.
5. Primary content: information, controls, workflow, data or documentation.
6. Primary action, when one exists.
7. Secondary actions, help and error/recovery affordances.
8. Legal, attribution, contact or footer context where needed.

A standalone public page does not need an operator sidebar. An operational table does not need an authentication illustration. An API-only project does not need a web form.

Pages that require sign-in use central ALXPRGS SSO rather than implementing an unrelated local password form (see §20).

---

# 20. Shared identity and SSO integration

**ALXPRGS SSO is the central identity provider for ALXPRGS services that require user authentication.** Individual services are relying applications, not independent password providers.

- Public resources remain public when the product intends them to be public. **Protected pages or actions must redirect to / initiate the canonical ALXPRGS SSO sign-in flow** through the approved integration, then return safely to the intended destination.
- Do not build separate usernames/passwords, passkeys, MFA enrollment or recovery flows into every service. These belong to the central identity service, unless an explicit architectural decision delegates such functionality.
- Present a clear `Sign in with ALXPRGS` or equivalent action where an explicit sign-in entry point improves comprehension. A seamless authorized redirect is also acceptable when appropriate.
- Respect SSO branding, session boundaries, account state, logout, token lifetimes and authorization. A visual convention never substitutes for real permission checks.
- OIDC/OAuth details, redirects, scopes, PKCE where applicable, callback validation and token handling must follow the canonical SSO contract and the local project's security integration notes; do not duplicate a full SSO protocol specification here.
- A service must not trust unvalidated query parameters for post-login destinations, identity or branding.
- Avoid redirect loops. Provide understandable errors and recovery paths when central SSO is unreachable.

**The central SSO application itself** is the appropriate place for specialised sign-in, passkey, MFA, OTP, recovery and authentication visuals. Its detailed screen/flow requirements belong in its **project-local design and security specifications**, not in every ALXPRGS project's active context.

---

# 21. Identity-aware product UX

Any application that uses identity should communicate the boundary between public, signed-in, signed-out, expired and insufficient-permission states without teaching users the underlying protocols.

Where applicable:

- Offer a clear SSO entry point and current account context.
- Preserve the destination of a legitimate workflow across sign-in when safe.
- Explain expired sessions and access denials in plain language.
- Distinguish `Sign in required` from `You do not have access`.
- Do not display credential/passkey controls inside a relying application; direct the user to the central SSO flow.
- When a sensitive action requires reauthentication, use the approved central identity mechanism rather than asking for credentials inside arbitrary application dialogs.

An app with no private user interaction does not need authentication UI.

---

# 22. Page, workflow and state transitions

Meaningful state changes should animate contextually **where motion is appropriate**:

- List → detail.
- Browse → edit.
- Edit → saved or validation error.
- Start operation → pending → completed or failed.
- Loading → content or empty state.
- Signed-out → central SSO → intended resource.
- Configuration change → revised overview.

Keep a sense of spatial continuity. Do not blink through disconnected screens without explanation, and do not animate a transition when doing so reduces accessibility or responsiveness.

Long-running infrastructure operations require honest progress and final state feedback, not fabricated success animations.

---

# 23. Human-facing technical and security language

Prefer understandable wording in general-purpose UI:

| Prefer | Avoid in ordinary UI unless technically necessary |
|---|---|
| Sign in | OIDC authorization-code exchange |
| Two-factor authentication | Factor-policy implementation metadata |
| Access denied | Raw authorization exception or status codes |
| Service temporarily unavailable | Internal stack trace |
| Recovery code | Implementation identifier |
| Deployment failed | Uninterpreted pipeline event ID |

Developers and operators may need raw protocol terms, IDs, traces and diagnostic payloads. Make them available in explicitly technical contexts, usually with copy/export controls and suitable privacy safeguards.

---

# 24. Forms

Every input must have a programmatic label. Placeholder text does not replace labels.

Default control height: **44 px**. Guided forms may use 44–46 px; compact operator controls may use 36–40 px where appropriate and accessible.

Every form supports consistent default, hover, focus-visible, filled, disabled, loading, invalid and success states where meaningful.

Only build forms needed by the project. A service that authenticates via central SSO does not need to duplicate sign-in credentials.


---

# 25. Passwords and sensitive field controls

When a project **legitimately owns** a password or other secret input, it must offer appropriate usability, privacy and accessibility controls.

Password fields provide visible show/hide actions, clear labels and contextual requirements. Secret/token fields should support masked display, deliberate reveal and copy controls when permitted, without leaking values into logs, URLs or unnecessary telemetry.

Do not expose hashing algorithms or security implementation details to ordinary users merely to fill space.

For ALXPRGS services relying on central SSO, login password/passkey/MFA collection belongs in the SSO frontend, **not duplicated in the relying application's interface**.

---

# 26. Verification codes and structured input

Where a product legitimately accepts OTPs, recovery codes, invitations, verification tokens or similarly structured values, provide a dedicated, accessible pattern rather than treating every code as an unstructured textbox.

Support as appropriate:

- Paste and autofill, including mobile one-time-code autocomplete when applicable.
- Keyboard entry and screen readers.
- Clear invalid/expired feedback.
- A single logical input with optional segmented visual presentation.
- Appropriate masking and privacy protections.

Do not add OTP input to ordinary relying applications when the central SSO owns the verification flow.

---

# 27. Validation

Validation errors belong as close as possible to the affected field.

Serious server/page errors additionally use section alerts.

Do not rely on one generic red banner for all possible validation.

Invalid fields receive:

semantic error association;

visible message;

appropriate `aria-invalid`;

appropriate `aria-describedby`.

---

# 28. Feedback hierarchy

Three feedback levels exist.

## Field feedback

Specific to one value.

## Section/page alert

For errors requiring user attention or affecting the entire current operation.

## Toast

For short-lived confirmation such as:

copied;

session revoked;

settings saved;

application created.

Toasts must not contain information the user needs to preserve or act upon later.

---

# 29. Buttons

Canonical variants:

**Primary** — main action; blue filled.

**Secondary** — neutral elevated/bordered action.

**Ghost** — low-emphasis control.

**Danger** — destructive action; red emphasis.

**Link** — navigation embedded in text.

Buttons must never silently change role based only on colour. Give each button an accessible name, predictable behaviour, visual feedback and a proper disabled/loading state.


---

# 30. Loading

No single loading technique applies everywhere.

Buttons use an inline loading indicator while retaining stable width where practical.

Tables use skeleton rows or structured placeholders.

Large initial areas may use skeletons.

Short local fetches may use subtle progress states.

Avoid blank screens with a centred spinner unless there is genuinely nothing useful to render.

---

# 31. Empty states

Empty states explain what is empty, why that can be expected and what the user can do next.

Example: `No projects yet`, followed by a short explanation and `Create project`, **only when project creation is a feature of that service**.

A genuinely empty table should have a meaningful empty state; an empty `<tbody>` is not an acceptable final design. Do not advertise actions the user is not authorised to take.

---

# 32. Dialogs

Dialogs use accessible headless primitives or a proven equivalent.

Required behaviour: focus trapping; focus restoration; Escape where cancellation is allowed; accessible title and description; background inertness; correct nested-dialog handling; and scrolling on short screens.

No new dialog implementation should manually recreate these mechanisms without exceptional reason. Not every task requires a dialog: prefer a page or inline interaction when that is clearer.


---

# 33. Destructive actions

Browser `alert()` and `confirm()` are not part of ALXPRGS Design Language.

Destructive actions use accessible product dialogs or equally clear context-appropriate confirmation patterns.

Examples, **only where these operations exist**: delete a resource, revoke a token or secret, remove an integration, block a user, delete a deployment, rotate a credential, revoke sessions or permanently erase data.

Extremely destructive actions may require typing an identifier or other deliberate confirmation.

Authorization, audit logging and reauthentication remain separate security controls and must not be confused with confirmation UX.

---

# 34. Sensitive operations and reauthentication

Confirmation UI must identify the actual operation when safe and appropriate.

Avoid generic copy such as only `Confirm operation`.

Prefer contextual text such as `Confirm deleting deployment "staging-api"` or `Confirm rotating the application secret`.

If an operation requires elevated proof of identity, follow the central SSO's approved step-up/reauthentication mechanism and return securely to the operation. Do not invent a second credential system for the individual service.

Never display sensitive operation proof material or secret values unnecessarily.

---

# 35. Product, settings and account-linked surfaces

Use sections rather than excessive nested cards. Select an information architecture appropriate to the project.

Possible categories include:

- Overview or home.
- Projects and resources.
- Activity and history.
- Deployments, jobs, runs or tasks.
- Connections and integrations.
- Configuration and preferences.
- Security and access.
- Usage, limits and health.
- Help and documentation.

**Only introduce categories that the service actually supports.** Shared identity/account lifecycle management remains primarily the responsibility of ALXPRGS SSO; relying applications can link to central account/security settings rather than implementing duplicates.

Security-sensitive actions should visually communicate their relative importance.

---

# 36. Application and operator shells

Use a left sidebar on desktop **when** a multi-section product or operator interface benefits from persistent navigation.

A project may instead use top navigation, a focused task layout, a documentation layout or no application chrome at all.

Possible operator navigation categories include Overview, Resources, Activity, Operations, Integrations, Access, Audit and System. Choose names based on actual product entities, not on a mandatory generic admin menu.

The navigation shell should remain quieter than the primary content and must not compete with operational data.

---

# 37. Sidebar

For applications that use a sidebar, a normal desktop width is approximately `232–248 px`; collapsed width may be `64–72 px`.

Desktop may remember the collapse preference. Mobile uses a drawer/sheet rather than permanently consuming horizontal space.

These dimensions are defaults, not a requirement to add a sidebar to single-page projects, public pages or documentation sites.

---

# 38. Overview pages and dashboards

Overview pages provide genuine situational awareness or useful next actions, rather than decorative analytics.

Choose actual project-specific signals, for example:

- Service/cluster/application health.
- Relevant resource counts.
- Recent activity, incidents or events.
- Pending tasks, running jobs or deployments.
- Usage and quota information.
- Integration/connection status.
- Recent security or administrative events.
- System/build identity.

Charts should exist only where trends or comparisons are genuinely useful. Clearly identify live, delayed, historical, simulated and unavailable data.

Do not add fake analytics simply to make a dashboard appear sophisticated. A small project with no metrics may not need an Overview dashboard at all.

---

# 39. Data tables

For products that need operational tables, support the relevant subset of search, sorting, filters, pagination, sticky headers, column visibility, row actions, keyboard access, loading state, empty state and error state.

Row actions usually live behind an ellipsis menu when secondary; important common actions may remain visible.

Do not add advanced table controls without real data or a user need.


---

# 40. Table density

When operational data tables are used, compact desktop rows should generally be around `40–48 px`.

Information density is intentional for operator tools; large card-like `70–90 px` rows should not become the default.

Conversely, tables for infrequent public tasks should optimise readability rather than chase minimum row height. Touch accessibility and content length may require larger rows.

---

# 41. Responsive tables

Do not force every desktop column onto mobile.

Depending on data, mobile may use:

horizontal scroll;

reduced column set;

expandable details;

compact record cards.

The choice depends on the semantics of each table.

---

# 42. Command palette

For sufficiently complex, keyboard-heavy applications, `Ctrl+K` / `Cmd+K` may open a global command palette.

Depending on actual features it may provide navigation, resource lookup, event lookup, theme control, safe direct actions, creation workflows, account actions and recent commands.

Example commands for a project that supports them:

- `Go to Resources`
- `Find deployment`
- `Create project`
- `Open recent events`
- `Change theme`
- `Sign out`

Do not add a command palette to a tiny one-page site merely for consistency. Destructive commands must still open the proper confirmation UI.

---

# 43. Command palette interaction

Where a command palette is implemented, it should feel extremely fast.

Opening transition is brief. Search responds immediately. Results support keyboard navigation. Recent/common commands may appear before input. Navigation and action categories may be visually separated.

All actions remain authorised server-side and follow the same accessibility and confirmation rules as their normal UI equivalents.

---

# 44. Cards

Cards are not universal containers. Use cards when information is genuinely a discrete object or a useful related group.

Examples: a project resource, active connection, running job, session, security factor or an Overview metric group **if relevant**.

Do not wrap `page → card → section → card → field group → card`.

---

# 45. Navigation and routing

When the service has multiple navigable views, use a real routing model appropriate to its framework. Application state should be representable in URLs where that improves usability, sharing and recovery.

Examples are project-specific: `/projects`, `/projects/:id`, `/activity`, `/settings`, `/admin`, `/docs` — **only if those pages exist**. Do not copy routes from the SSO project into other products.

The browser Back/Forward history must not desynchronise visible UI and URL. Deep links, refreshes, authorisation boundaries, error states and SSO return routes must work correctly.

For React SPAs, prefer a maintained routing solution to manual `pushState`/pathname state synchronisation. Static single-page sites or non-web projects do not need invented routers.

---

# 46. Page transitions

Route transitions are subtle.

Do not animate the entire application off-screen for every navigation.

Preferred techniques:

small opacity;

short translate;

shared active-navigation indicator;

content skeleton where fetching is necessary.

---

# 47. Technical values

Technical identifiers use appropriate dedicated treatments when present, such as project IDs, resource IDs, client IDs, scopes, IP addresses, session IDs, request IDs and build IDs.

Use Geist Mono with a neutral surface and copy action when useful. Long values must wrap, truncate with accessible expansion or provide a dedicated viewer; they must not destroy responsive layouts.

Never display sensitive tokens in full without explicit user intent and appropriate protections.


---

# 48. Copy actions

Copying should have immediate feedback.

Icon state:

Copy → Check.

Text may temporarily become:

`Copied`

No browser alert.

---

# 49. Status

Statuses use language and/or iconography **in addition to colour**. Never encode a meaningful status using colour alone.

Examples: green dot + `Healthy`; yellow indicator + `Pending`; red indicator + `Blocked`.

These are semantic examples, not mandatory statuses for every product. Status must reflect actual backend state.


---

# 50. Glass and blur

Glassmorphism is not a general surface style.

Blur may appear selectively in:

command palette backdrop;

modal backdrop;

floating navigation layer;

selected decorative project-relevant effects.

Normal cards should not all be translucent glass.

---

# 51. Visual effects

Decorative glows may use blue and cyan.

Effects should be soft and spatial.

Avoid:

large rainbow gradients;

permanent neon outlines;

multiple saturated colours competing for attention.

The user should remember the interface rather than the gradient.

---

# 52. Light theme

Light theme preserves the same hierarchy and interaction.

It is not simply an inverted dark palette.

Glows and blur are reduced because they can look excessive against light backgrounds.

Light surfaces rely slightly more on border/elevation contrast.

---

# 53. Theme switching

Theme changes should feel polished and user-controlled.

Provide a visible or readily discoverable **System / Light / Dark** selector on graphical interfaces. The preferred shared placement for public, account and conventional application pages is within a footer or settings/control area that users can consistently find. A command palette may offer an additional path.

When a footer is present, group appearance controls with other utility/contact links where appropriate. On narrow screens, stack the group rather than letting it overlap legal text or cookie notices. Do not force a permanent large footer into fullscreen operational workspaces where it compromises the product; provide an equally accessible alternative.

Keep a text label, keyboard support and a clear focus indicator. A brief global colour transition may be applied when the user directly changes theme.

Do not animate initial theme hydration; avoid theme flash on startup.

---

# 54. Responsive system

Primary layout thresholds may align approximately with:

`640`

`768`

`1024`

`1280`

but components should be responsive to their actual content rather than blindly assuming desktop behaviour.

---

# 55. Mobile and touch layouts

On mobile and other narrow viewports:

- Secondary decoration and complex visualisations disappear or simplify.
- Navigation becomes compact and appropriate for touch.
- Primary content and actions get viewport priority.
- Critical actions remain reachable or predictably scrollable.
- The virtual keyboard must not trap important controls below inaccessible content.
- Tables and dense panels use deliberate responsive strategies, not accidental horizontal overflow.
- Touch targets, zoom and focus remain usable.

SSO login screens follow these same principles within the SSO project; they are not the default layout template for every ALXPRGS service.

---

# 56. Short-height displays

Dialogs and focused task surfaces must be tested on short-height screens.

Every important dialog requires:

viewport-aware max height;

internal scrolling when necessary;

visible action area.

No dialog may render its confirmation buttons below an unreachable viewport boundary.

---

# 57. Accessibility target

Target **WCAG 2.2 AA** for core graphical interfaces. This is a requirement independent of Lighthouse scoring.

Requirements include visible focus, full keyboard operation, semantic labels, correct landmarks, unique page titles, accessible validation, appropriate live announcements, sufficient contrast, reduced-motion support, non-colour status indication and usable touch targets.

Include manual keyboard and assistive-technology checks for critical workflows; a perfect automated Accessibility score is not proof of complete accessibility.

---

# 58. Focus appearance

Keyboard focus must be immediately visible.

Recommended treatment:

2 px brand/focus outline or ring;

small offset where background distinction requires it.

Focus styling must be consistent across primitives.

---

# 59. Page semantics

Each major page should have one meaningful H1.

Avoid nested main landmarks.

Route changes should update:

document title;

meaningful focus target where appropriate.

---

# 60. Performance philosophy

A premium interface must feel fast in real use, not only in screenshots. Design sophistication is never permission for poor runtime behaviour.

Avoid unnecessary dependency weight; constant full-page rerenders; huge unoptimised raster assets; render-blocking scripts; unnecessary hydration; moving large blurred surfaces every frame; layout thrashing; and costly layout-property animations where transforms suffice.

Use progressive loading, sensible caching, lazy loading and robust error handling where appropriate. Optimise essential interactions before decorative effects.

**Near-perfect Lighthouse results are an explicit ALXPRGS engineering target**, not a post-launch stretch goal. See §76 for score objectives, testing procedure and release gates. Score optimisation must never compromise security, actual usability, accessibility or functional correctness.

---

# 61. Asset loading

Official logos and frequently used UI assets should use appropriate caching. Large decorative assets must be optimised and loaded only when needed. Prefer vector formats where suitable and provide properly sized image variants.

Critical content and operations must remain usable if a decorative asset, visualisation, analytics endpoint or third-party resource fails to load. The logo and key typography should not depend unnecessarily on unreliable third-party runtime requests.

Avoid CLS from images, late font swaps and content injected without reserved space. Honour reduced-data or low-performance contexts when practical.

---

# 62. Frontend technical foundation

The design language is **framework-independent at the standard level**. Use the smallest stable technology stack that serves the project. An API-only or infrastructure-only project is not required to install React, Tailwind, routing or animation libraries.

For **new ALXPRGS React web applications**, the recommended baseline is:

- **React + TypeScript** — interactive application foundation and type safety.
- **Tailwind CSS** — real utility generation with semantic theme integration.
- **Radix Primitives or equivalent accessible headless primitives** — interaction-heavy controls.
- **Source-owned shadcn-style components** — architectural foundation, not a substitute for ALXPRGS identity.
- **Motion for React** — coordinated purposeful transitions where needed.
- **Lucide** — functional icons.
- **Geist / Geist Mono** — self-hosted typography.
- **An appropriate maintained router** — only for applications that need client-side routing.

For static sites, documentation, other frontend frameworks or existing products, choose a suitable equivalent and preserve the visual, accessibility and quality rules.

Do not install a dependency merely because it appears in this list. Select stable and compatible versions when implementing; record the chosen project-specific stack in its local design/architecture notes.

---

# 63. Component architecture

Use reusable primitives as actual components rather than repeating near-identical markup across screens.

The **candidate library**, not a mandatory per-project shopping list, includes Button, IconButton, Input, PasswordInput, OTPInput, Checkbox, Radio, Select, Textarea, Label, Field, Alert, Toast, Badge, Card, Dialog, DropdownMenu, Tooltip, Tabs, Popover, CommandPalette, Skeleton, Spinner/Progress, Table foundations and CopyButton.

Build and import **only the components used by the current project** or reasonably needed by its imminent features. PasswordInput and OTPInput normally belong to the central SSO application, not every ALXPRGS service.

Application-specific components build on shared primitives and semantic tokens. Avoid duplicated component frameworks that increase bundles and cognitive load.

---

# 64. Design tokens

Theme values must be defined centrally for each graphical project and remain compatible with the ALXPRGS semantic system.

Token categories may include colour, typography, spacing, radius, shadow/elevation, motion duration, motion easing, z-index, control height and layout widths.

Components consume semantic tokens. Do not duplicate literal design values throughout TSX/CSS, and do not require unused token categories in a headless project.

The canonical palette and scales in §§7–10 are the primary reference. Project-specific semantic extensions are allowed when they preserve recognisable ALXPRGS identity and are documented locally.

---

# 65. Tailwind usage

When Tailwind is used, utilities are implementation tools, not the design system itself.

Repeated semantic patterns must become reusable components or variants. Do not replace undefined handmade utility classes with hundreds of unique unreadable class strings copied between screens.

Use component variants and token conventions. For projects not using Tailwind, implement equivalent semantic tokens and reusable styling patterns rather than adding Tailwind unnecessarily.

---

# 66. Variant management

Reusable components should expose clear variants.

Example Button:

`variant="primary"`

`variant="secondary"`

`variant="ghost"`

`variant="danger"`

`size="sm|md|lg"`

Avoid booleans such as:

`blue`

`rounded`

`big`

`isDangerRed`

that encode presentation inconsistently.

---

# 67. Error architecture

Where relevant, the UI must distinguish:

- Field validation or invalid user input.
- Authentication required or session expired.
- Authorization/access denied.
- Rate limit or quota reached.
- Conflict or invalid resource state.
- Expired or cancelled operation.
- Network failure or offline state.
- Service unavailable or degraded.
- Unexpected internal failure.

Not every HTTP error needs a unique page, but technical failures must map to consistent, meaningful language, correct status representation, useful next actions and correlation identifiers where appropriate.

Do not mask critical failures behind a fake success toast or indefinitely spinning loader. Keep private diagnostics out of ordinary error messages.

---

# 68. Workflow and operation state architecture

Multi-step processes must have explicit, coherent state models even when implemented through routes, reducers, server state or finite-state machines.

Potential states depend on the project: idle, editing, validating, submitting, queued, running, awaiting confirmation, completed, partially completed, failed, cancelled, expired, permission denied or waiting for external service.

The central SSO application additionally models its own sign-in, MFA, recovery, consent and reauthentication states **in its project-local specification**.

Do not scatter incompatible conditional JSX and optimistic assumptions across unrelated components. Handle interruptions, retries and browser refreshes without losing or fabricating critical state.

---

# 69. Progressive disclosure

Ordinary users see simple descriptions and the controls they need. Technical details may appear in expandable sections, inspectors or dedicated diagnostics when useful.

Operators and administrators may require richer metadata, audit trails, traces and configuration. Do not hide operationally important information merely for aesthetic minimalism.

Apply permissions and privacy rules to underlying data, not only to the decision to display an advanced section.

---

# 70. Content tone

Copy is concise, confident, accurate and human. Avoid overly corporate language, exaggerated marketing wording and unnecessary protocol jargon.

Good: `Your changes have been saved.`

Bad: `The system has successfully persisted the configuration mutation transaction.`

Good: `This deployment is running.`

Bad: `The orchestration subsystem reports a nominal state vector.`

Good: `Sign in with ALXPRGS to continue.`

Bad: `Initiate the OAuth 2.0 authorization-code grant workflow.`

Never imply an operation has succeeded before the backend confirms success, and never label placeholder/mock data as live.

---

# 71. Do

- Use dark neutral surfaces as the primary visual reference.
- Use ALXPRGS blue as the primary brand/action colour.
- Use cyan sparingly for relevant technical visuals.
- Use the real official ALXPRGS logo and assets.
- Use meaningful motion to communicate state continuity.
- Choose layout and information density for the task.
- Use reusable components only where they add value.
- Support keyboard, touch, screen readers and reduced motion.
- Use human language and explicit success/error feedback.
- Expose technical detail where it helps operators.
- Integrate protected services with central ALXPRGS SSO.
- Keep project-local guidance short and scope-specific.
- Strive for Lighthouse 100 across all applicable categories and views.

---

# 72. Do not

- Do not make every panel a card.
- Do not use arbitrary gradients everywhere.
- Do not make all controls pills.
- Do not put glass blur on every surface.
- Do not expose raw protocol jargon to ordinary users.
- Do not use browser alerts for product interactions.
- Do not use emoji as functional product icons.
- Do not duplicate component markup across every page.
- Do not let animation delay ordinary interaction or hurt performance.
- Do not weaken security, privacy or authorization in a redesign.
- Do not create fake operational metrics or success states.
- Do not turn ALXPRGS into a generic shadcn demonstration.
- Do not make every new service implement its own login system.
- Do not copy the whole canonical design language into every project's active context.
- Do not introduce unnecessary UI features or frameworks solely to satisfy examples in this document.

---

# 73. Desired end-user feeling

A person using an ALXPRGS service should feel:

- The system is dependable, secure and understandable.
- The task and next action are clear.
- The product is technically sophisticated without being difficult for its own sake.
- Interactions acknowledge input immediately and honestly.
- The interface belongs to a larger, coherent ecosystem.

They should not feel:

- They are filling out an unnecessarily bureaucratic form.
- They are reading raw protocol documentation to complete a routine task.
- They are trapped in a generic admin template.
- Their device is rendering a game instead of executing their action.
- Every ALXPRGS service has a completely different account or identity system.

---

# 74. Desired operator and developer feeling

An operator or developer should feel:

- Information is easy to scan and verify.
- Actions are easy to discover and appropriately guarded.
- Keyboard interactions are fast where useful.
- Critical, reversible and destructive operations are clearly distinguished.
- Technical data and meaningful diagnostics are available without clutter.
- The interface behaves like a serious professional infrastructure tool.

Products without an operator interface need not invent one.

---

# 75. ALXPRGS signature characteristics

An ALXPRGS graphical interface should be recognisable through a coherent combination of:

- Near-black dark canvas with a complete light alternative.
- Authentic ALXPRGS branding and official logo assets.
- ALXPRGS blue identity and selective blue/cyan technical effects.
- Geist typography and balanced mono treatments.
- Moderately soft geometry and quiet surfaces.
- Strong information hierarchy appropriate to the context.
- Fast, purposeful spatial motion where interaction benefits from it.
- Dense but restrained tooling when operations demand it.
- Clear central SSO integration for protected resources.
- Accessible, responsive implementation and exceptionally high real quality.

No one trait alone defines the identity; the combination does. Visual details apply to projects with graphical surfaces, not to headless infrastructure that has no UI.

---

# 76. Lighthouse and continuous quality gates

Lighthouse quality is an **explicit design and engineering acceptance criterion** for ALXPRGS web projects, starting with the first implementation. The goal is **100/100 in every applicable Lighthouse category**, on **mobile and desktop**, for **every representative page type and critical route**.

## 76.1 Target scores

| Lighthouse category | Target | Standard release gate |
|---|---:|---|
| **Performance** | **100 / 100** | Median **≥95 / 100** on representative mobile and desktop runs; investigate every result below 100 and aim for **98–100** |
| **Accessibility** | **100 / 100** | **100 / 100** on representative tested pages, plus manual accessibility verification |
| **Best Practices** | **100 / 100** | **100 / 100**, unless an independently documented tool/platform limitation applies |
| **SEO** | **100 / 100** | **100 / 100** for indexable public pages; **N/A** for intentionally private/nonindexable surfaces |

The target remains 100 even when a release gate allows narrowly bounded fluctuation. A score of 95 is **not** the design goal. Stronger project-specific gates may be set locally.

Score categories and audit availability can change between Lighthouse releases. Use currently supported applicable categories; do not fabricate an SEO requirement for intentionally private routes or mark relevant failed audits N/A simply to obtain a perfect score.

## 76.2 Required testing procedure

1. Test **production-mode builds** under stable, reproducible conditions, with the real application assets, fonts, headers and routing behaviour.
2. Cover representative public pages, app entry points, data-heavy views, forms, error/empty states, mobile and desktop. Where SSO-protected screens matter, authenticate using a safe test account and supported Lighthouse tooling; do not expose test credentials.
3. Perform **at least three runs per tested configuration** and evaluate a representative **median** for noisy performance scores. Investigate single-run failures rather than hiding them behind one favourable result.
4. Automate audits in CI using Lighthouse CI or a maintained equivalent. Make category assertions and regression thresholds explicit in the project-local config; save/report failures so they can be fixed.
5. Run keyboard, focus, touch, screen-reader and high-zoom manual checks. Lighthouse Accessibility 100 is not a WCAG certification.
6. Re-test after changes to dependencies, major routes, branding/assets, animation, network behaviour or shared UI primitives.
7. Track real-user performance and Core Web Vitals where available. Target **LCP ≤2.5 s, INP ≤200 ms and CLS ≤0.1 at the 75th percentile** of page visits, segmented by mobile/desktop. Real user experience takes priority over a lab number.

## 76.3 Non-negotiable behaviour

Do not game scores by disabling functionality, suppressing real content, removing necessary authentication, weakening security headers, blocking assistive technologies, hiding legitimate audits, testing only empty pages or making the production build differ from the audited build.

A temporary exception must record: affected URL/surface, category and score, failed audit, reproducible environment, user impact, reason it cannot yet be fixed, mitigation, owner and revisit date. A release below the standard gate requires explicit project-owner approval. This is an exception, not a permanent relaxation of the canonical target.

For headless APIs, CLIs, jobs and services with no auditable web pages, Lighthouse is **not applicable**. Such projects must still adopt appropriate automated quality checks (tests, static analysis, security and reliability checks), documented locally.

Official references: [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview), [Lighthouse CI configuration](https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/configuration.md), [Core Web Vitals](https://web.dev/articles/vitals/).

---

# 77. Definition of done for a project adopting ALXPRGS Design Language v1

A project conforms to this standard **to the extent applicable to its intended product surface** when:

- The canonical standard was considered at project inception and the concise project-local design specification exists, links to this file and selects only relevant requirements.
- The official logo and recognisable ALXPRGS brand identity are used consistently on the project's human-facing surfaces.
- Shared semantic tokens control applicable dark/light/system themes.
- Only needed reusable components and product patterns are implemented; unused SSO/admin components are not added by default.
- Protected routes correctly integrate with central ALXPRGS SSO without duplicate local sign-in systems.
- Navigation and browser history work correctly where routing exists.
- Loading, success, failure, empty and long-running operation states are deliberately designed and truthful.
- Motion is purposeful, performant and respects reduced-motion preferences.
- Mobile, narrow and short-height interfaces are usable.
- Keyboard, touch and assistive-technology accessibility expectations are met; applicable WCAG 2.2 AA checks are complete.
- Security, privacy, permissions, data integrity and API contracts remain intact.
- Lighthouse reports for applicable web pages meet §76 targets or have explicitly approved, narrowly documented exceptions.
- Relevant automated tests, regression checks and quality gates run in the project's normal workflow.
- No unneeded pseudo-utility styling layer, duplicated component foundation or heavyweight decorative feature is retained merely from a previous project.

Conformance is **project-specific and evidenced by implementation and testing**. The existence or final status of this standard is not proof that any project has finished adopting it.


---

# 78. Final visual and product target

ALXPRGS should not look like a personal pet project attempting to imitate an enterprise product.

Every applicable ALXPRGS interface should look and behave like part of a small, intentionally engineered infrastructure ecosystem that happens to support personal projects, experiments, internal operations and hackathons.

The size of the audience does not determine the quality of the interface. A tool used by one person should be designed with the same care for brand, clarity, security, speed, accessibility and reliability as one used by thousands.

**One design language. Different appropriate products. Minimal project-specific context. No compromised fundamentals.**

