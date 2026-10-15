# ALXPRGS engineering standard

This document defines the shared engineering baseline for ALXPRGS projects. Apply requirements to the project's actual scope: a library does not need a service launcher, and a headless API does not need a frontend or Lighthouse audits.

Project documentation must identify applicable requirements, commands, and evidence. Adoption of this document is not evidence that an existing project already complies. Existing projects must document gaps and their remediation rather than claim unverified conformance. Mandatory requirements must not be silently weakened by local guidance.

## 1. Technology and architecture

- Python is the primary backend language; FastAPI is the default web API framework.
- .NET is an option for workloads with substantial expected load. Explain the workload, performance requirements, and operational tradeoffs before selecting it; do not migrate a working service solely on an assumption about language speed.
- React, Vite, and Tailwind CSS are the default frontend stack.
- Protected services use the central [ALXPRGS SSO](https://github.com/alxprgstech/sso). Use its documented integration contract and SDK where suitable. Do not introduce duplicate local account or login systems. Public services without authentication do not need to add it merely to conform.
- Follow the existing project's architecture and documented contracts. Discuss major architectural changes and new dependencies before implementation, as required by the [contribution guidelines](../../CONTRIBUTING.md).

These preferences guide new development; they do not require every project to contain every layer or force unrelated projects into one architecture.

## 2. Implementation baseline

Keep changes focused and explain the problem they solve. Prefer clear, maintainable code and established project patterns over speculative abstractions.

Validate untrusted input at system boundaries. Enforce authorization on the server; interface visibility is not an access control. Preserve established security and data integrity invariants. Never commit credentials, private keys, production data, or other secrets; provide sanitized configuration examples instead.

Handle failures explicitly, with useful messages and appropriate status codes. Logs must help diagnosis without disclosing secrets or unnecessary personal data. Set appropriate timeouts for external operations and document retry behavior where applicable.

Document public API, configuration, and data-format contracts. Preserve compatibility or explicitly identify the breaking change, affected consumers, migration steps, and required release increment. Database changes must include a migration and a safe upgrade procedure; document recovery limitations and destructive steps before execution.

Update setup, usage, operations, and troubleshooting documentation when behavior changes. Separate implemented behavior, verified behavior, and planned work.

## 3. Dependencies and reproducibility

Reuse existing project capabilities when suitable. Add a dependency when its benefit justifies its maintenance, security, license, and operational costs. Explain the choice; writing everything from scratch is not a goal.

Commit ecosystem-appropriate lock files or equivalent resolved dependency specifications for reproducible application installation. Document supported runtime versions and clean-install commands. Keep dependency updates scoped and review their compatibility and security impact.

Do not ignore applicable dependency audit failures without recording the affected dependency, impact, mitigation, owner, and resolution or review date. A newly introduced unresolved high or critical vulnerability blocks release unless the project owner explicitly accepts a documented exception.

## 4. Testing and coverage

### Required coverage

Backend and frontend must each achieve **at least 75% line coverage and at least 75% branch coverage**, measured independently. A combined average cannot compensate for a failing component. In a backend with separately tested Python and .NET components, report and enforce each component independently.

Configure explicit CI thresholds and retain readable reports. Include all applicable first-party executable source in the denominator, including unimported or untested files. Exclusions must be narrow and documented, such as generated code, vendored code, or nonexecutable declarations. Do not exclude difficult business logic or security paths to raise a score. Pure documentation has no code coverage requirement.

Coverage is a minimum, not proof of correctness. Independently test critical authentication, authorization, token/session handling, validation, and data integrity scenarios, including relevant negative cases, replay, concurrency, and failure behavior. A passing percentage does not excuse an untested critical path.

### Test selection and isolation

- Add meaningful tests for new behavior and regression tests for corrected defects where applicable.
- Use unit tests for isolated logic, integration tests for real boundaries, and end-to-end tests for critical user journeys. Avoid tests that merely repeat implementation details.
- Use pytest for Python projects; use appropriate maintained tools for .NET and frontend projects. Document actual commands locally rather than copying commands from another project without checking them.
- Ordinary tests must not send external emails, charge accounts, or mutate live services. External integration tests run separately with explicit configuration and test identities.
- Database tests must use a dedicated test database with safeguards against production or development data loss. Document required setup and migrations.
- Report skipped external checks and their reasons explicitly. Missing credentials may skip an optional external job, but a skipped job is not evidence of delivery or integration success. If an integration check is required for a release, missing prerequisites block that release.

### Frontend verification

For projects with a frontend, normal checks must include linting, applicable type checking (including test code), unit/component tests, a production build, and dependency auditing. Test critical journeys end to end, including SSO integration where applicable. Document exact commands and prerequisites in the project.

The [ALXPRGS Design Language v1](../design/ALXPRGS_DESIGN_LANGUAGE_v1.md), especially sections 76 and 77, defines mandatory web quality and accessibility requirements. It remains the canonical source for their details:

- Target Lighthouse 100 in every applicable category on representative mobile and desktop surfaces.
- The standard performance release gate is a median of at least 95, with every result below 100 investigated and a continued target of 98–100; applicable Accessibility, Best Practices, and public-page SEO gates are 100, subject to the canonical document's applicability rules and documented limitations.
- Audit production-mode builds, with at least three runs per tested configuration, representative routes and states, and safe access to protected screens.
- Automate audits and regression thresholds in CI. Retain reports and investigate failures.
- Perform manual keyboard, focus, touch, screen-reader, and high-zoom checks. Automated scores do not replace manual accessibility verification.
- Follow the canonical standard for real-user performance, retesting triggers, and narrowly scoped exceptions. Releases below its standard gates require explicit project-owner approval.

Do not weaken security, remove real functionality, or manipulate tested content to improve scores. Lighthouse is not applicable to projects without auditable web pages.

## 5. Cross-platform startup

Every runnable application or service must provide root-level `start.ps1` for PowerShell and `start.sh` for Bash with equivalent supported behavior. Libraries and documentation-only repositories do not need artificial launchers; runnable examples must document how to start them.

Docker Compose is the default local startup method for services. A different method is allowed when the project documents the reason, prerequisites, and equivalent startup behavior. This does not mandate Docker Compose for production hosting.

Both launchers must:

1. Resolve project and configuration paths relative to the script, independent of the caller's current directory.
2. Check required tools, supported versions, runtime availability, and relevant ports before startup; provide actionable errors and nonzero exit status on failure.
3. Guide safe initial configuration. Generate secrets securely when needed, never print them, and never overwrite existing configuration or secrets on repeat runs.
4. Start the documented local environment and verify readiness within a bounded timeout. Do not report success merely because a process was created.
5. Preserve existing databases, users, volumes, and configuration on repeat runs. Keep destructive reset operations separate and require explicit confirmation describing the affected data.
6. Print useful local addresses and next steps without exposing credentials. Default local bindings to loopback unless a documented use case requires otherwise.

Document prerequisites, startup commands, configuration, shutdown, and troubleshooting. Verify first startup and repeat startup on the supported Windows/PowerShell and Unix/Bash environments, or state which verification remains outstanding. Do not claim macOS support solely because a script works on Linux.

## 6. Versioning and build identity

Released software follows [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html). Keep the authoritative product version in a root `VERSION` file, without the tag's `v` prefix. Derive other version fields from it or check their consistency automatically; do not maintain conflicting independent copies.

Repositories distributing shared standards, documentation, and templates must also maintain the changelog required by section 7. Until they introduce versioned releases, reviewed snapshots may be identified by full commit SHA without a `VERSION` file. When publishing their first versioned release, add `VERSION` and apply the same SemVer, matching-tag, immutability, and source-identity requirements to that release and subsequent releases. Merely storing documents does not require inventing a software version.

| Change | Required increment |
| --- | --- |
| Compatible bug fix | PATCH |
| Compatible new capability or deprecation | MINOR |
| Breaking contract change at 1.0.0 or later | MAJOR |
| Breaking contract change before 1.0.0 | MINOR, resetting PATCH |

The pre-1.0 breaking-change rule is an ALXPRGS convention layered on SemVer's initial-development rules. Document compatibility even before 1.0.0. Use valid SemVer prereleases when needed, such as `1.0.0-rc.1`.

Each release must have a matching tag, such as `v1.2.3`, pointing to the exact release commit. The release commit's `VERSION`, changelog heading, release metadata, and product artifact versions must agree. Components with genuinely independent release lifecycles must explicitly document their own version sources and tag namespaces.

Builds must record both the product version and the full source commit SHA in appropriate build metadata so an artifact or deployed service can be traced to its source. Preserve package ecosystem version compatibility when representing metadata. Identify uncommitted local builds as dirty; do not present them as exact reproductions of a clean release commit.

Never move a published release tag or replace an artifact with different contents under the same released version. Corrections require a new version. A normal development commit does not require a version bump; perform the coordinated version change when preparing the release.

## 7. Changelog and commit traceability

Maintain an English root `CHANGELOG.md` following [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Keep `Unreleased` first, followed by releases newest first. Release headings contain the version and an ISO date (`YYYY-MM-DD`). Use the categories `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, and `Security`; omit empty categories.

This requirement includes shared standards, documentation, and template repositories, even before their first versioned release. Record meaningful changes to rules, adoption guidance, and reusable workflows; do not invent release headings for snapshots that have not been released.

Update `Unreleased` in the same pull request or local change series as every meaningful behavior, configuration, dependency, compatibility, security, or operational change. Explain the user or operator impact; a raw commit log is not a changelog. Typo-only and other changes with no meaningful impact may be omitted. Record breaking changes prominently and link migration instructions.

Every meaningful entry must link to the relevant implementation commit or commits in the target repository. Issue and pull request links provide useful context but do not replace final commit links. Links must identify commits that actually contain the described work, not only a documentation edit.

Git commits cannot contain their own final hash. For a new entry, add the implementation commit link in a subsequent documentation or release-preparation commit. Before merging a pull request, links may point to its existing implementation commits; after squash or rebase, update them to the final commits in the target branch in a follow-up commit. Do not invent hashes or repeatedly amend a commit trying to reference itself. All entries included in a release must have finalized links before the release tag is created.

Each release heading must link to the comparison between the preceding and current release tags. `Unreleased` links to the comparison between the latest release tag and the development branch. For the first release, link to its release tag instead of inventing a preceding tag. For a project without any release, an interim `Unreleased` link may point to its development commit history.

Security entries must respect coordinated disclosure: record appropriate impact and remediation when disclosure is authorized, without prematurely exposing exploit details or secrets.

## 8. CI and release acceptance

Projects must document and automate applicable linting, type checks, tests, independent coverage thresholds, builds, dependency audits, and web quality gates. Also check version consistency and changelog structure and traceability before release. Documentation-only projects use relevant documentation and link checks; irrelevant runtime checks are not required.

Failed required checks block release. A skipped, unexecuted, or unavailable required check is not a pass. Record narrowly scoped exceptions with the reason, impact, mitigation, owner, and review date; project-owner approval is required to release with an exception, and canonical design requirements still apply.

Before release, verify:

- Relevant contracts, migrations, SSO boundaries, and critical scenarios are tested.
- Required checks and frontend gates pass, including independent coverage thresholds.
- Launchers and documented setup work on the claimed supported environments.
- `VERSION`, the changelog, final commit links, proposed tag, and artifacts agree.
- Upgrade, configuration, and recovery instructions reflect the release's impact.
- The release can be traced to a clean source commit and its actual validation results.

Applying this standard requires project-specific implementation and evidence. Publishing the standard alone does not install CI checks, change SSO, release software, or deploy services.
