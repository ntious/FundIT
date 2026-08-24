# Security Policy

## Supported Version

Security fixes are applied to the current `main` branch. Historical tags and
student forks are not maintained unless explicitly stated.

## System and Scope

FundIT is an educational repository containing introductory Python programs,
Binder materials, and a disposable PostgreSQL/Adminer environment for
Codespaces. Covered components include executable source code, container and
development-environment configuration, automation, and dependency manifests.

The repository is not a production service and must not process real
credentials, regulated data, grades, or personally identifiable information.

## Reporting a Vulnerability

Use GitHub's private vulnerability reporting feature under **Security →
Advisories → Report a vulnerability**. Do not disclose a suspected
vulnerability in a public issue.

Include the affected path, practical impact, reproduction conditions, and a
suggested mitigation when available. Do not include real secrets or student
data.

## Threat Model and Trust Boundaries

Potentially untrusted inputs include command-line input, file paths, CSV
content, SQL entered by students, dependency updates, and pull-request
content. Important boundaries include the host filesystem, Binder or
Codespaces environment, container network, generated database credentials,
and GitHub Actions.

## Security Invariants

- Secrets and reusable passwords must never be committed.
- PostgreSQL and administrative interfaces must remain loopback-only or
  privately forwarded.
- User-controlled values must not cause command injection, unsafe evaluation,
  or filesystem access outside an explicitly selected location.
- Classroom SQL must remain confined to the user's disposable lab database.
- Automation must use least privilege and immutable third-party action
  references.

## Reportable Findings and Severity Context

Report command execution, path traversal, credential exposure, unintended
network exposure, container escape, authorization bypass, destructive file
operations outside the selected scope, and practical CI or dependency
compromise.

Severity depends on realistic reachability and impact beyond the user's own
deliberate operation of a disposable lab.

## Out of Scope

Ordinary teaching errors, formatting problems, and expected effects of
student-supplied SQL inside the student's own disposable database are not
security findings unless they cross a documented boundary.

## Known Limitations

Binder, Codespaces, Docker, PostgreSQL, and Adminer provide external security
controls and must be kept updated. The examples are designed for education,
not production deployment.
