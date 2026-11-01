# Changelog

Meaningful changes to ALXPRGS shared standards, guidance, templates, and workflows are recorded here. This repository currently distributes reviewed snapshots by full commit SHA; no versioned releases have been published.

## [Unreleased]

### Added

- Added a required standard for built-in administrator help in projects with an admin interface, including the `Alt+Shift+Q` overlay, platform fallback, Server/Service groups, verified procedures, and content maintenance. ([admin guide standard](standards/operations/ADMIN_GUIDE_STANDARD.md))
- Added a reusable controlled data-reset security standard for projects that need destructive administrative cleanup, including server-side authorization, staged confirmations, recoverable backups, SSO step-up, idempotency, and failure handling. ([standard](standards/security/CONTROLLED_DATA_RESET.md))
- Added a general operator CLI standard for current and future projects, requiring a safe `self-update` command separate from application deployment. ([operator CLI standard](standards/operations/OPERATOR_CLI.md))
- Shared repository structure and the canonical ALXPRGS design language. ([implementation](https://github.com/alxprgstech/.github/commit/f3c5f958e3145792863c70a509af8b2524b02de2))
- Default contribution and private vulnerability-reporting policies. ([implementation](https://github.com/alxprgstech/.github/commit/4c05e8b21d1b8423ce6c2a869a1ca6cad321d43e))
- Engineering requirements for architecture, isolated testing, independent coverage, safe startup, versioning, and release traceability. ([implementation](https://github.com/alxprgstech/.github/commit/b4a09c6ad3f466ce46a5b59e4d0ece65d58f27b9))
- Security requirements for SSO, secrets, data retention, recovery, external services, and test-only payments. ([implementation](https://github.com/alxprgstech/.github/commit/e415ae561f5d25f323f441f731d3971f5a70a7b1))
- Agent instruction templates with pinned standards and project-specific adoption guidance. ([implementation](https://github.com/alxprgstech/.github/commit/27c328a4db110a1733df51e6aa1d465a8eb0d0c0))
- A scoped project design specification template. ([implementation](https://github.com/alxprgstech/.github/commit/c95fca3847fbc509d914a16dabaa51dd4e07f687))
- Bug and feature issue forms and a pull request template. ([implementation](https://github.com/alxprgstech/.github/commit/e2927be1515d73bf1b39c616341ddae55489e81d))
- A design reviewer profile and configurable reusable Linux quality workflow, with a caller template pinned to its implementation. ([workflow and reviewer](https://github.com/alxprgstech/.github/commit/fc6471722414f46da8212c253e73c8e4c17da712), [caller pin](https://github.com/alxprgstech/.github/commit/27900d962c8c79b82a33772f4e9256ef0d327025))

### Changed

- Updated project instructions, design-spec template, and adoption guidance to apply the administrator guide standard whenever a project has an administrative interface.
- Updated the visual style guide with read-only SSO and MP observations, removing fixed SSO-derived color examples and clarifying that both are optional, distinct references. ([design standard](standards/design/ALXPRGS_DESIGN_LANGUAGE_v1.md))
- Translated all project templates into Russian and aligned design guidance with product-specific visual choices rather than inherited layouts or universal frontend gates. ([templates](templates/))
- Translated the security baseline into Russian while preserving its technical requirements and references. ([standard](standards/security/SECURITY_BASELINE.md))
- Translated the engineering standard into Russian and updated frontend quality guidance to match the visual-style-only design guide. ([standard](standards/engineering/ENGINEERING.md))
- Translated the organization profile README into Russian. ([profile](profile/README.md))
- Translated the design reviewer profile into Russian and aligned its review scope with the visual-style-only design guide. ([profile](agents/design-reviewer.agent.md))
- Переработано руководство по дизайну: оставлены необязательные рекомендации по визуальному стилю, убраны предписания к продукту, сценариям, архитектуре и критериям качества, чтобы SSO, MP и другие сервисы могли сохранять собственные интерфейсы. ([стандарт дизайна](standards/design/ALXPRGS_DESIGN_LANGUAGE_v1.md))
- Clarified changelog and versioning applicability for shared standards, documentation, and templates; introduced this repository's changelog without inventing a released version. ([implementation](https://github.com/alxprgstech/.github/commit/08ca6acb89a06efbfa76a30c719cba62b119c9fc))
- Clarified that the quality wrapper's default configuration does not guarantee the behavior of project-supplied commands or prohibit inherited secrets technically. ([implementation](https://github.com/alxprgstech/.github/commit/08ca6acb89a06efbfa76a30c719cba62b119c9fc))

### Fixed

- Corrected metadata text contrast on canonical theme backgrounds and clarified that Lighthouse Performance has a release gate of at least 95 with a target of 100. ([implementation](https://github.com/alxprgstech/.github/commit/08ca6acb89a06efbfa76a30c719cba62b119c9fc))
- Aligned contribution guidance with issue-form requirements, made local-design-first reading explicit in agent instructions, and closed the organization profile's code block. ([implementation](https://github.com/alxprgstech/.github/commit/08ca6acb89a06efbfa76a30c719cba62b119c9fc))

[Unreleased]: https://github.com/alxprgstech/.github/commits/main
