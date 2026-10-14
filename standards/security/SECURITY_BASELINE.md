# ALXPRGS security baseline

This document defines technical security requirements for ALXPRGS projects, applied to their actual functionality and deployment. It complements the [engineering standard](../engineering/ENGINEERING.md). Vulnerability reporting and coordinated disclosure are covered by [SECURITY.md](../../SECURITY.md).

Project documentation must identify applicable controls, configuration, verification, and remaining gaps. A written requirement is not evidence of implementation or production readiness. Do not silently weaken this baseline or claim compliance without verification.

## 1. Identity and access

Protected services integrate with the central [ALXPRGS SSO](https://github.com/alxprgstech/sso) using its documented contracts. Do not add fallback local accounts or duplicate login systems. Public resources do not need artificial authentication.

Deny access to protected resources until the server establishes the required identity and permissions. Enforce authorization for each protected operation and resource, including ownership and administrative scope. Client-side checks and hidden controls do not replace server-side enforcement.

If an SSO dependency needed to establish a new login or validate access is unavailable, reject that operation rather than bypass verification. Existing sessions or locally validated tokens may continue only under the documented SSO contract, with valid trust material, expiry, and required authorization checks; an outage never grants extra access or extends validity.

Validate tokens and authentication responses using maintained libraries and the SSO integration contract. Apply least privilege to service identities, database roles, deployment credentials, and third-party access. Separate application runtime permissions from migrations or administrative operations where applicable.

## 2. Secrets and configuration

- Local development may use a Git-ignored `.env`. Commit only sanitized examples such as `.env.example`, with no working credentials.
- Production secrets must come from protected platform configuration or a secrets store, with access limited to the components and operators that need them.
- Never expose secrets in browser bundles, public configuration endpoints, URLs, logs, error reports, screenshots, test artifacts, or diagnostic output.
- Generate secrets securely, preserve existing values on repeat startup, and document rotation and recovery procedures. Use separate credentials for development, tests, and production.
- Treat a leaked credential as compromised: revoke or rotate it, assess impact, and remove further exposure. Deleting it from the latest file alone is insufficient.

Review CI output and artifacts as potential disclosure surfaces. Untrusted contributions must not receive production credentials or privileged deployment access.

## 3. Transport and production exposure

Production public endpoints must use HTTPS. Verify certificates for outbound HTTPS connections; do not disable verification to work around deployment errors. Local development may use HTTP on loopback under the documented local profile.

Disable debug mode, interactive debuggers, and verbose internal error responses in production. Databases must not be publicly reachable. Restrict administrative endpoints, internal services, and exposed ports to their required audiences.

Document TLS termination, trusted proxy boundaries, and internal connections separately. An internal network is not automatically trusted: restrict access and document whether encryption and service authentication are required for each connection and its data sensitivity.

## 4. Application and data protection

Validate untrusted input at boundaries, use safe database query mechanisms, and encode output appropriately. Apply relevant browser protections, explicit allowed origins, safe redirect validation, and CSRF protection for cookie-authenticated state changes. Configure session cookies for the actual production security model.

Apply bounded request sizes, timeouts, and rate limits to abuse-sensitive operations. Do not expose account existence, stack traces, tokens, or sensitive internal state through errors. Record security-relevant events without logging credentials or unnecessary personal data.

Treat destructive operations and schema migrations explicitly: document impact, required privileges, backup prerequisites, and recovery limitations. Keep test databases and fixtures isolated from real user data. Do not copy production data into ordinary tests or external test services.

## 5. Retention and deletion

Classify persistent records, security/audit records, operational logs, and temporary files. Document ownership and retention rules for each relevant class.

Essential persistent data must not be deleted merely because it is more than 30 days old. Retain it while needed for the service, subject to explicit documented deletion requirements, user deletion workflows, and applicable obligations. This does not authorize retaining all personal data forever.

Operational logs and temporary files older than 30 days may be removed under documented cleanup rules when they are no longer needed for service operation, recovery, incident investigation, or an applicable retention requirement. The 30-day rule is permission for appropriate cleanup, not a blanket expiry for all data or a prohibition on shorter lifetimes for explicitly short-lived secrets and temporary artifacts.

Backup retention is a separate project-specific decision. Do not infer a 30-day backup retention period from log cleanup. Ensure backup expiry and restore procedures respect documented deletion requirements and do not silently resurrect deleted records.

## 6. Backups and recovery

For ordinary services, production recovery requirements are:

| Requirement | Maximum |
| --- | --- |
| Recoverable data loss window (RPO) | 15 minutes |
| Time to restore service after disruption (RTO) | 24 hours |

RPO means the recovered state must be no more than 15 minutes behind the disruption. RTO means restoring a usable, verified service within 24 hours of the disruption, including detection and recovery work. These are required objectives, not claims about current infrastructure.

Choose and document a backup/recovery design capable of meeting both objectives for databases, persistent files, and required configuration. A daily backup alone does not satisfy a 15-minute RPO. Scheduled copies also need to account for completion time and failures; use suitable continuous recovery or sufficiently frequent verified copies as the workload requires.

Keep recoverable copies independent of the primary host or storage failure domain. Protect backups with restricted access and encryption, including recovery keys stored securely and available during an incident. Monitor backup freshness and failures; stale or unreadable copies do not satisfy the requirement.

Before production, demonstrate recovery in an isolated environment with representative data. Verify integrity, application startup, required dependencies, and the measured recovery point and duration. Document the restore procedure, responsible operator, backup schedule and retention, monitoring, and a recurring restore-test schedule. Re-test after material changes to storage, migrations, encryption, or recovery procedures.

The 15-minute data-loss allowance does not automatically apply to financial records or similarly sensitive irreversible transactions. Such functionality requires separately agreed integrity and recovery requirements before any real-world operation.

## 7. External services and privacy

External services are allowed when their purpose, transmitted data, access permissions, environment, and configuration are documented. Existing examples include Sentry, CodeScene, DeepScan, Testmail, and email delivery providers. Evaluate each integration for its actual use; listing a service here does not authorize unrestricted data sharing.

- Code analysis services may receive source code within the agreed repository scope, with appropriately limited access.
- Sentry may receive minimized, sanitized diagnostic events. Exclude passwords, tokens, keys, authorization headers, session contents, and unnecessary personal data. Do not send request bodies or sensitive URLs without deliberate filtering and review.
- Testmail and similar test inboxes receive synthetic test messages and test identities, never actual users' authentication messages or personal data.
- Selected email providers may process the recipient and message content required for real service email. Limit unrelated data and document the chosen transport.

Verify filtering at the sending side and inspect representative sanitized events before enabling an integration. Document how to disable it and what happens if it is unavailable. Optional diagnostics must not prevent core service operation.

### Quotas and telemetry

Use quotas deliberately. Filter expected validation failures, routine health checks, duplicate noise, and irrelevant development events rather than sending every event. Preserve actionable unexpected failures and security-relevant evidence.

Document environment-specific sampling, volume limits, and quota monitoring before enabling telemetry. Start optional tracing and profiling disabled or with a deliberately low, justified sample rate. Do not enable all diagnostics at full volume by default. Avoid unbounded retries and repeated external requests that consume quotas without useful evidence.

Sentry Session Replay must be disabled by default. Enabling it requires a separate privacy review of masking, captured data, access, retention, quota impact, and applicable consent requirements. Masking assumptions must be tested; error-triggered replay must not silently bypass the default-off decision.

Ordinary automated tests use mocks or local substitutes for external providers. Run real email and other quota-consuming integration tests separately and intentionally, with bounded test volumes and explicit prerequisites. Required release tests must still run; quota conservation is not permission to label skipped tests as passed.

## 8. Payments: test mode only

Financial services are not part of the currently intended ecosystem. If a project needs to experiment with payments, use **YooKassa (ЮKassa) test mode only**, with a test shop, separate test credentials, and the provider's supported test data. Do not configure a live shop or accept or transfer real money under this baseline.

YooKassa's [official testing documentation](https://yookassa.ru/developers/payment-acceptance/testing-and-going-live/testing) describes a test mode without actual money transfers and requires test cards rather than real cards. Follow the current provider instructions for the selected integration.

Make test mode explicit in configuration and interfaces. Verify the test shop configuration and the provider's test indicators; reject unexpected live-mode responses. Never collect or store real card credentials in local test flows.

Real payments would require a separate explicit decision and project-specific security, integrity, reconciliation, and recovery requirements. They must not be enabled as a routine configuration change or treated as covered by the ordinary 15-minute loss allowance.

## 9. Verification and incident readiness

Use the engineering standard's required tests, independent coverage gates, dependency auditing, and release evidence. Add meaningful negative tests for applicable access controls, malformed input, secret handling, and trust boundaries. Verify production settings, exposure, backup freshness, recovery evidence, telemetry filtering, and test-only payment safeguards where relevant.

Document how to isolate an affected component, revoke compromised access, preserve necessary evidence, recover service, and contact the responsible operator. Handle public disclosure according to the [security reporting policy](../../SECURITY.md).

Record gaps and exceptions with scope, impact, mitigation, owner, and review date. Releases with an exception require explicit project-owner approval; approval of an exception does not authorize real payments or silently redefine agreed recovery objectives. State what was actually tested and what remains unverified.
