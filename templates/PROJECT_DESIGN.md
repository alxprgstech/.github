# Project design specification

<!-- Adoption: copy to docs/design/PROJECT_DESIGN.md or the project's established equivalent. Replace the prompts with verified project decisions, remove unused sections and these adoption instructions, and keep the result concise. Paths below assume the documented docs/standards/ snapshot layout. -->

The visual language is defined by the project's pinned `docs/standards/design/ALXPRGS_DESIGN_LANGUAGE_v1.md`, with provenance in `docs/standards/SOURCE.md`. Apply that standard; do not reopen its established brand, typography, color, theme, motion, or component principles as a new visual-direction exercise. This document specifies their application to this product, not a replacement design system.

Use the local specification first during implementation and consult relevant canonical sections as needed. Missing details here do not waive applicable canonical requirements. Keep this file current when product scope changes, and distinguish intended behavior from implemented and verified behavior.

## 1. Product and applicability

- **Purpose and users:** State the problem, intended users, and primary tasks.
- **Surfaces:** Identify what is required now, reasonably foreseeable, and not applicable. Include only actual product needs; do not add dashboards, administration, login screens, or other features solely because the canonical standard discusses them.
- **Known constraints:** Record relevant existing architecture, framework, devices, and integration contracts from verified project facts.

**Projects without a graphical interface:** Keep only a brief statement of purpose and the absence of a graphical interface. Remove sections 2–5 and record a deviation only if one actually exists. No screen, theme, component, responsive-layout, or Lighthouse specification is required. Relevant engineering and security requirements still apply, and any actual documentation or CLI surface follows applicable canonical guidance without inventing a frontend. Revisit applicability if a graphical surface is later introduced.

## 2. User journeys and navigation

List only the core journeys and screens needed now. For each, record:

- The user's goal, entry point or route, and successful outcome.
- Required data and actions, navigation and browser-history behavior where relevant.
- Public or protected access and any role or ownership boundaries. Protected resources use central ALXPRGS SSO; this document does not invent a separate local login system.

Ask focused requirements questions when the product behavior remains unclear after inspecting the task and project. Do not ask the owner to choose a new visual language already settled by the canonical standard. Routine details within established rules can be resolved during implementation.

## 3. Layout and component application

Describe the information hierarchy, appropriate interaction density, and relevant screen layouts. Select the smallest useful component subset from the established system and project implementation; avoid importing unrelated SSO or administrative patterns.

Record where official assets, semantic tokens, and existing components live, or where they will be implemented if this is a new project. Document project-specific mapping decisions without copying the entire canonical palette or token catalogue.

Graphical web interfaces must retain the applicable canonical baseline: official ALXPRGS identity, semantic tokens, dark/light/system theme selection, accessible interaction, responsive layouts, and purposeful reduced-motion-aware behavior. State how the project's real layouts work on narrow and short viewports, including dense content where present.

## 4. States and interaction

For relevant journeys and components, define loading, success, empty, validation, failure, access-denied, and long-running states. Include recovery actions, disabled states, confirmation of destructive operations, and unsaved-change behavior only where needed.

Keep feedback truthful. Identify mock data explicitly and never imply that fabricated health, activity, or metrics are live. Preserve server-side security boundaries and avoid exposing secrets or unnecessary implementation details.

## 5. Verification and evidence

Select representative routes, states, mobile/desktop configurations, and critical journeys for this project. Record the exact verification commands, prerequisites, and report locations, or link to the project's maintained testing document rather than duplicating it.

Apply canonical sections 76 and 77 for production-mode Lighthouse audits, at least three runs per tested configuration, category release gates, manual accessibility checks, and applicable real-user performance targets. Follow the engineering standard for frontend checks, critical end-to-end journeys, and independent coverage requirements. Do not replace these requirements with a weaker local checklist.

Record the tested commit/build and results separately from planned checks. Include keyboard/focus, touch, screen-reader, high-zoom, responsive layouts, themes, and reduced-motion verification as applicable. A written specification or automated accessibility score alone is not proof of conformance.

## 6. Deviations, if any

Remove this section if there are no deviations. Otherwise record the canonical rule, technical reason, replacement behavior, affected surfaces, impact and mitigation, and explicit owner approval. For release-gate exceptions, include the owner and revisit date plus the evidence required by the canonical standard. Do not silently redefine mandatory rules or label an applicable failing requirement as not applicable.
