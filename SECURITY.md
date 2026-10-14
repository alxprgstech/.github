# Security policy

This is the default security reporting policy for projects in [alxprgstech](https://github.com/alxprgstech). If a project provides its own security policy, follow that policy for project-specific contacts, scope, and supported versions.

## Supported projects and versions

Currently, vulnerability reports concerning all ALXPRGS projects and released versions are accepted for review. A project's own `SECURITY.md` may specify a narrower support scope.

Accepting a report for review does not guarantee a backport, a fix for every affected version, or indefinite maintenance. The available resolution may be an upgrade, a configuration change, or another mitigation. No fixed response or remediation time is guaranteed.

## Report a vulnerability privately

Email **[alxprgs@gmail.com](mailto:alxprgs@gmail.com)** with a subject such as `Security report: <project> — <short summary>`.

GitHub Private Vulnerability Reporting is not currently enabled. Use email for private reports under this policy.

Do not open a public issue or pull request containing vulnerability details, exploit instructions, or exposed credentials. Ordinary bugs without a security impact can be reported through the affected project's issue tracker.

Include enough information to assess and reproduce the issue safely:

- The affected repository or service, version or commit, and relevant configuration.
- A description of the vulnerability and its potential impact.
- Reproduction steps or a minimal proof of concept, including any required access or prerequisites.
- Sanitized evidence, such as logs, screenshots, or a proposed fix, if available.
- How to contact you and whether you would like public credit if an advisory is published.

Do not send live credentials, private keys, unnecessary personal data, or copies of other users' data. If you find an exposed secret, identify its location and the affected service without repeating the secret in the report.

## Handling and disclosure

Reports are reviewed to understand impact, reproduce the issue where practical, and determine an appropriate fix or mitigation. Maintainers may request additional details and coordinate disclosure with the reporter.

Keep vulnerability details private while a resolution and disclosure are being coordinated. Agree on publication timing with the maintainer rather than assuming a fixed deadline. Where appropriate, a GitHub Security Advisory or project release notes may communicate the affected versions, impact, and resolution.

This policy does not establish a bug bounty or promise a financial reward.

## Research boundaries

Use local environments or systems you own or have explicit permission to test. This reporting policy does not authorize testing of deployed services or third-party infrastructure.

Avoid accessing other people's data, disrupting availability, social engineering, or modifying or deleting data. If you encounter sensitive information unexpectedly, stop accessing it and report the minimum information needed to identify the issue privately.
