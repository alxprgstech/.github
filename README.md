# ALXPRGS shared standards and GitHub defaults

This repository contains shared standards, contributor guidance, and reusable resources for [alxprgstech](https://github.com/alxprgstech), the organization behind [alxprgs.tech](https://alxprgs.tech).

Use it to find the common rules for contributing, report security issues privately, and adopt relevant standards in a project.

## Start here

- Read the [contribution guidelines](CONTRIBUTING.md) before opening an issue or pull request.
- Report vulnerabilities using the private contact in the [security policy](SECURITY.md).
- Use the [ALXPRGS Design Language v1](standards/design/ALXPRGS_DESIGN_LANGUAGE_v1.md) for applicable human-facing surfaces. Follow its guidance on selecting requirements for each project's scope.
- Follow the [engineering standard](standards/engineering/ENGINEERING.md) for development, testing, startup, versioning, and changelog requirements.
- Apply the [security baseline](standards/security/SECURITY_BASELINE.md) for access controls, secrets, production configuration, data recovery, and external integrations.
- Read the target project's own documentation for setup, commands, and project-specific requirements.

## Repository layout

| Path | Purpose | Current status |
| --- | --- | --- |
| `profile/README.md` | Public organization profile on GitHub | Existing profile content |
| `standards/design/ALXPRGS_DESIGN_LANGUAGE_v1.md` | Shared design standard | Written |
| `standards/engineering/ENGINEERING.md` | Shared engineering guidance | Written |
| `standards/security/SECURITY_BASELINE.md` | Shared technical security requirements | Written |
| `templates/` | Project guidance templates for contributors and coding agents | Agent instructions and project design template written |
| `agents/` | Reusable agent definitions | Placeholder |
| `CONTRIBUTING.md` | Default contribution guidelines | Written |
| `SECURITY.md` | Default vulnerability reporting policy | Written |
| `.github/ISSUE_TEMPLATE/` | Default issue forms | Placeholders |
| `.github/PULL_REQUEST_TEMPLATE.md` | Default pull request template | Placeholder |
| `.github/workflows/` | Reusable GitHub Actions workflows | Placeholder |
| `workflow-templates/` | Organization workflow templates | Placeholders |

Placeholder files reserve the intended structure. They do not yet provide usable forms, workflows, agent instructions, or enforceable standards.

## How to use these resources

### GitHub community defaults

GitHub can use this public `.github` repository's supported community files, including `CONTRIBUTING.md` and `SECURITY.md`, for organization repositories that do not provide their own corresponding files. A project's own files take precedence. These defaults are displayed by GitHub; they are not copied into each project's checkout.

Issue templates have a separate override rule: if a project defines its own issue templates or issue template configuration, GitHub does not use the organization's default issue template directory for that project.

The root README describes this shared repository. The separate [`profile/README.md`](profile/README.md) provides the organization's public profile.

### Standards and templates

GitHub does not automatically distribute or enforce the contents of `standards/`, `templates/`, or `agents/`. Adopt relevant written guidance explicitly and document project-specific choices in the target repository. Do not treat empty placeholders as implemented policies.

### Adopting agent instructions

1. Copy [`templates/AGENTS.md`](templates/AGENTS.md) to the target repository root as `AGENTS.md` and [`templates/copilot-instructions.md`](templates/copilot-instructions.md) to `.github/copilot-instructions.md`. Merge with existing instructions rather than overwriting project knowledge.
2. Select a reviewed full commit SHA of this repository. Copy the design, engineering, and security standards from that commit into the target's `docs/standards/`, preserving their `design/`, `engineering/`, and `security/` subdirectories, basenames, and contents. This preserves links between standards.
3. Record the upstream repository, full SHA, original source paths, immutable source links, and adoption date in `docs/standards/SOURCE.md`. In this adopted layout, adapt links to `../../SECURITY.md` and `../../CONTRIBUTING.md` to `../../../SECURITY.md` and `../../../CONTRIBUTING.md`, respectively, and provide those project root policies. Record these reporting/contribution link adaptations in `SOURCE.md`; preserve all standard requirements. Verify other links when adopting a newer snapshot.
4. Replace the project-context checklist in the adopted `AGENTS.md` with verified commands, working directories, prerequisites, contracts, applicability decisions, and known gaps. Remove adoption comments. Do not invent commands or claim checks were run merely because the template lists them.
5. Review both instruction files together for consistency. Update pinned standards deliberately in a separate scoped change; offline agents use the committed snapshots.

These templates express the desired working rules. Instruction support and automatic discovery vary by agent and execution environment; they do not change platform permissions or guarantee that a hosted agent permits custom branch names. See the [Codex AGENTS.md guide](https://learn.chatgpt.com/docs/agent-configuration/agents-md) and [GitHub Copilot instruction documentation](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions).

### Adopting the project design specification

Copy [`templates/PROJECT_DESIGN.md`](templates/PROJECT_DESIGN.md) to `docs/design/PROJECT_DESIGN.md` or the project's established equivalent. Use the pinned design standard from the snapshot layout above, replace prompts with actual product decisions, and remove unused sections. The shared design language already defines the visual direction; the local specification selects relevant screens, journeys, layouts, components, and verification. For a project without a graphical interface, retain only the brief applicability statement described in the template.

Reusable workflows must be explicitly called by another workflow. Organization workflow templates are starting points that users add to individual repositories; changes to a template do not automatically update existing copies. The current workflow files are empty and are not ready for use.

## Maintaining this repository

Changes to shared policies can affect contributors across the organization. Explain their purpose, scope, and compatibility with project-specific guidance in the pull request. Keep links accurate and distinguish usable resources from planned content.

This repository does not grant a shared license to other projects. Check each project's own license before reusing its code or other materials.

## GitHub documentation

- [Default community health files](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)
- [Organization profile README](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile)
- [Reusing workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows)
- [Creating workflow templates](https://docs.github.com/en/actions/how-tos/reuse-automations/create-workflow-templates)
