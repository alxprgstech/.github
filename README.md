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
| `agents/` | Reusable agent definitions | Design reviewer written |
| `CONTRIBUTING.md` | Default contribution guidelines | Written |
| `SECURITY.md` | Default vulnerability reporting policy | Written |
| `CHANGELOG.md` | History of meaningful standards, guidance, and workflow changes | Written |
| `.github/ISSUE_TEMPLATE/` | Default issue forms | Bug report and feature request forms written |
| `.github/PULL_REQUEST_TEMPLATE.md` | Default pull request template | Written |
| `.github/workflows/` | Reusable GitHub Actions workflows | Configurable Linux quality workflow written |
| `workflow-templates/` | Organization workflow templates | Quality caller and catalog metadata written |

All planned files now contain content. Templates still require project-specific adoption and validation; their presence alone does not implement checks in another repository.

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

For design work, read the project's local design specification first, then consult the relevant sections of the pinned canonical standard. Do not load the entire design standard into the active context by default. The local summary does not waive applicable canonical requirements.

These templates express the desired working rules. Instruction support and automatic discovery vary by agent and execution environment; they do not change platform permissions or guarantee that a hosted agent permits custom branch names. See the [Codex AGENTS.md guide](https://learn.chatgpt.com/docs/agent-configuration/agents-md) and [GitHub Copilot instruction documentation](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions).

### Adopting the project design specification

Copy [`templates/PROJECT_DESIGN.md`](templates/PROJECT_DESIGN.md) to `docs/design/PROJECT_DESIGN.md` or the project's established equivalent. Use the pinned design standard from the snapshot layout above, replace prompts with actual product decisions, and remove unused sections. The shared design language already defines the visual direction; the local specification selects relevant screens, journeys, layouts, components, and verification. For a project without a graphical interface, retain only the brief applicability statement described in the template.

### Using the design reviewer

[`agents/design-reviewer.agent.md`](agents/design-reviewer.agent.md) is an organization custom-agent profile; for project-local adoption, copy it to `.github/agents/design-reviewer.agent.md`. It reviews against pinned standards without making fixes. Its tool list allows reading, searching, and configured Playwright browser tools, with no shell or editing tools. Provide an already running safe test interface for browser review. Browser tools and automatic organization-agent availability depend on the host; unsupported tools are not a guarantee of runtime inspection. See [GitHub custom agent configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration).

### Connecting quality checks

The [reusable workflow](.github/workflows/reusable-quality.yml) is a Linux execution wrapper, not a universal implementation of every standard. It checks out the caller's event revision (the merge revision for ordinary pull requests), disables persisted checkout credentials, optionally sets up explicitly selected Python/Node versions, and runs mandatory setup and quality commands from the repository root. Actions are pinned to full commits. The supplied caller passes no external secrets, repository-token permissions are read-only, and the wrapper contains no release or deployment steps of its own. It executes project-supplied commands, so it does not technically prevent those commands from making external changes or receiving secrets through caller inputs. The absence of declared secret inputs does not reject `secrets: inherit`; callers must not add it to this quality template.

To adopt the [caller template](workflow-templates/quality.yml):

1. Ensure the pinned shared workflow commit is available on GitHub. Local-only commits cannot be fetched by Actions; this repository must be published separately under explicit authorization before another repository can use the new workflow.
2. Add the template through GitHub's Actions catalog, or copy it to the target project's `.github/workflows/quality.yml`. When copying manually, replace `$default-branch` with the actual default branch. Retain the reviewed full upstream SHA, updating it deliberately.
3. Create project-owned `scripts/ci/install.sh` and `scripts/ci/quality.sh`, or replace the inputs with equivalent explicit commands. Set required runtime versions. For .NET or other tools, the setup script must provision and verify the required version reproducibly. Missing scripts or failed commands fail the job; do not replace them with no-ops.
4. The quality command must enforce all applicable project gates: lint/type checks, tests, independent backend/frontend line and branch coverage of at least 75%, builds, dependency/security audits, and relevant version/changelog checks. Frontend projects also need canonical Lighthouse gates and critical browser journeys. Document commands, prerequisites, applicability, and manual checks in the target project. The wrapper cannot prove that an arbitrary command actually enforces these gates; review its implementation.
5. Set up isolated databases and service dependencies explicitly in project scripts, or use dedicated project jobs where that is clearer. Services, configuration, and runtime state in a separate caller job are not automatically shared with this job. Never point test commands at production data.
6. Keep Windows launcher regressions, real email/other quota-consuming external tests, and release workflows separate. SSO's existing specialized jobs must not be removed merely because a generic wrapper exists. A release workflow must validate and test its exact release commit; this template's normal PR/push run is not proof about another SHA.
7. Review required status checks and repository protections during adoption; these files do not configure them. Keep untrusted PR execution on isolated GitHub-hosted runners without secrets. Do not use this command interface with privileged `pull_request_target`, inherited production secrets, or untrusted self-hosted runners.

The wrapper runs only when called. Its supplied caller runs on pull requests targeting the default branch, pushes to that branch, and manual dispatch. Newer runs cancel superseded work for the same PR/ref. Ordinary checks do not invoke external email services; telemetry flag defaults are defensive hints, and each project's own configuration must actually keep external effects off. No artifacts are uploaded automatically, avoiding accidental publication of sensitive logs; projects may add explicit sanitized reports where needed. Verify a real Actions run after publishing and adopting before treating the integration as proven.

Reusable workflows must be explicitly called by another workflow. Organization workflow templates are starting points that users add to individual repositories; changes to a template do not automatically update existing copies.

## Maintaining this repository

Changes to shared policies can affect contributors across the organization. Explain their purpose, scope, and compatibility with project-specific guidance in the pull request. Keep links accurate and distinguish usable resources from planned content.

Maintain the English root [CHANGELOG.md](CHANGELOG.md) for meaningful changes to standards, instructions, templates, and workflows, with links to the implementation commits. This repository currently identifies reviewed standards snapshots by full commit SHA and has no versioned releases. A root `VERSION` file is required when introducing a versioned release, together with the engineering standard's SemVer and matching-tag rules. Do not invent release versions for the existing unreleased history.

This repository does not grant a shared license to other projects. Check each project's own license before reusing its code or other materials.

## GitHub documentation

- [Default community health files](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)
- [Organization profile README](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile)
- [Reusing workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows)
- [Creating workflow templates](https://docs.github.com/en/actions/how-tos/reuse-automations/create-workflow-templates)
