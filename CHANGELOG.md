# Changelog

Meaningful changes to ALXPRGS shared standards, guidance, templates, and workflows are recorded here. This repository currently distributes reviewed snapshots by full commit SHA; no versioned releases have been published.

## [Unreleased]

### Added

- Shared repository structure and the canonical ALXPRGS design language. ([implementation](https://github.com/alxprgstech/.github/commit/f3c5f958e3145792863c70a509af8b2524b02de2))
- Default contribution and private vulnerability-reporting policies. ([implementation](https://github.com/alxprgstech/.github/commit/4c05e8b21d1b8423ce6c2a869a1ca6cad321d43e))
- Engineering requirements for architecture, isolated testing, independent coverage, safe startup, versioning, and release traceability. ([implementation](https://github.com/alxprgstech/.github/commit/b4a09c6ad3f466ce46a5b59e4d0ece65d58f27b9))
- Security requirements for SSO, secrets, data retention, recovery, external services, and test-only payments. ([implementation](https://github.com/alxprgstech/.github/commit/e415ae561f5d25f323f441f731d3971f5a70a7b1))
- Agent instruction templates with pinned standards and project-specific adoption guidance. ([implementation](https://github.com/alxprgstech/.github/commit/27c328a4db110a1733df51e6aa1d465a8eb0d0c0))
- A scoped project design specification template. ([implementation](https://github.com/alxprgstech/.github/commit/c95fca3847fbc509d914a16dabaa51dd4e07f687))
- Bug and feature issue forms and a pull request template. ([implementation](https://github.com/alxprgstech/.github/commit/e2927be1515d73bf1b39c616341ddae55489e81d))
- A design reviewer profile and configurable reusable Linux quality workflow, with a caller template pinned to its implementation. ([workflow and reviewer](https://github.com/alxprgstech/.github/commit/fc6471722414f46da8212c253e73c8e4c17da712), [caller pin](https://github.com/alxprgstech/.github/commit/27900d962c8c79b82a33772f4e9256ef0d327025))

### Changed

- Clarified changelog and versioning applicability for shared standards, documentation, and templates; introduced this repository's changelog without inventing a released version.
- Clarified that the quality wrapper's default configuration does not guarantee the behavior of project-supplied commands or prohibit inherited secrets technically.

### Fixed

- Corrected metadata text contrast on canonical theme backgrounds and clarified that Lighthouse Performance has a release gate of at least 95 with a target of 100.
- Aligned contribution guidance with issue-form requirements, made local-design-first reading explicit in agent instructions, and closed the organization profile's code block.

[Unreleased]: https://github.com/alxprgstech/.github/commits/main
