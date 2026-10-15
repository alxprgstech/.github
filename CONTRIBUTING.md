# Contributing to ALXPRGS

Useful contributions are welcome from everyone: bug fixes, documentation improvements, new capabilities, and changes that make projects easier to use or maintain.

Explain the problem your contribution solves. Changes made only for the sake of changing something, including cosmetic churn without a clear benefit, are unlikely to be accepted. Maintainers decide whether a contribution fits the project.

These are the default guidelines for repositories in [alxprgstech](https://github.com/alxprgstech). Follow a repository's own contribution guidelines when provided. Read its README, development instructions, and applicable standards before making changes.

## Before you start

- Search existing issues and pull requests to avoid duplicate work.
- Open an issue before starting a large change, adding a dependency, or changing architecture. Describe the problem, proposed approach, and expected benefit so maintainers can discuss the direction with you.
- Small, focused fixes and documentation improvements can go directly to a pull request.
- For vulnerabilities, follow the [security policy](https://github.com/alxprgstech/.github/blob/main/SECURITY.md). Do not disclose sensitive details in public issues or pull requests.

## Reporting bugs and requesting features

Use the relevant project's issue tracker and its issue forms when available.

For a bug, include a problem description, reproduction steps, expected and actual behavior, and the affected release version or full commit SHA. Include relevant sanitized logs, or explicitly explain why logs are not produced or accessible. Environment details are optional; include them when relevant. A minimal sanitized example is helpful where applicable.

For a feature, describe the problem or use case, who benefits, and why existing behavior is insufficient. A proposed solution and alternatives considered are optional.

Never include passwords, tokens, private keys, personal data, or other confidential information in reports, screenshots, logs, or example files.

## Branch names

Use an English branch name in the form `<type>/<short-description>`. Use lowercase words separated by hyphens in the description.

| Prefix | Use |
| --- | --- |
| `bug/` | Fixing a reproducible software bug |
| `fix/` | Other corrections, such as configuration or integration fixes |
| `new/` | Adding a new capability |
| `docs/` | Documentation changes |
| `refactor/` | Restructuring code without intentionally changing behavior |
| `chore/` | Maintenance and tooling |

Examples: `bug/login-redirect`, `new/export-settings`, `docs/setup-guide`.

## Preparing a pull request

1. Fork the repository if you do not have write access, then create a branch using the naming convention above.
2. Follow the project's setup instructions and existing implementation patterns. Keep the change focused; avoid unrelated reformatting, renaming, or dependency updates.
3. Add or update meaningful tests when behavior changes. Update documentation when users or maintainers need new instructions.
4. Run the checks documented by the project and review your diff for unintended changes and sensitive data.
5. Open a pull request against the project's default branch unless its documentation or maintainers specify another target. Use a draft pull request if work is still in progress.

Use a clear English title and description. Explain what problem is solved, what changes, and how you verified the result. Link a related issue when one exists; an issue is not required for every small fix. For interface changes, include useful screenshots or a recording. Call out breaking changes, migrations, new dependencies, and operational impact when relevant.

Report the checks you ran and their results. If a relevant check could not be run, say which one and why. Do not claim unperformed checks passed.

Write clear commit messages that describe the change. Conventional Commits are welcome but are not required by these shared guidelines.

## Review

Respond to review feedback and keep discussion constructive and focused on the work. Be prepared to explain the benefit of a change or adjust its scope. Opening an issue or pull request does not guarantee acceptance or a response within a fixed time.

Check the target repository's license and any contribution terms before submitting code or other material. Do not contribute material you are not entitled to share.
