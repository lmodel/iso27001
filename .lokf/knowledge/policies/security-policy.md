---
type: Policy
id: https://w3id.org/lmodel/iso27001/knowledge/policies/security-policy
genre: reference
title: Security policy
description: How to report a vulnerability (GitHub's private vulnerability reporting), which release receives fixes (the latest), what executes in the repository and what holds each surface, the ruleset on `main`, and the two repository settings that are not yet in force.
resource: SECURITY.md
sources:
  - id: security.md
    resource: SECURITY.md
    title: every section
  - id: dependabot.yml
    resource: .github/dependabot.yml
    title: the five update entries
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# Security policy

`SECURITY.md` asks for a vulnerability to be reported through GitHub's private vulnerability reporting, not in a public issue. It says that one person maintains the repository, so a first reply takes days and there is no bounty. It also says that only the latest release receives fixes.[^security.md]

The repository releases the schema, the Python models generated from it, and the adapt copy as a release asset. Nothing is published to PyPI, and nothing released holds text of ISO/IEC 27001. The upstream watch streams ISO's dataset and writes only its report. The overlay scripts read YAML with `yaml.safe_load`, the merge writes only under `tmp/`, and `.gitignore` keeps a licence holder's overlay out of every commit.

The policy's table of surfaces names each workflow and what holds it:

- the pull request checks run read-only;
- the release job runs only on a push to `main`, in the `release` Environment;
- the website's deploy job alone holds the Pages scopes;
- the upstream watch writes only issues;
- the librarian's agent runs without a write token.

Every workflow declares `permissions: {}` at the top, pins its actions to commit hashes and runs harden-runner in audit mode. Dependabot keeps the pins, the package's lock, the sidecar's lock, the website's npm packages and the release tools' npm lock current, each monthly.[^dependabot.yml] The policy says that a ruleset on `main` blocks deletion and force-pushes and keeps the history linear. It names two settings not yet in force: required reviewers on the `release` Environment, and secret scanning with push protection.

The policy leaves out ISO/IEC 27001 itself, LinkML, a compromised runner or harness, and whether the knowledge bundle is true.

[^security.md]: SECURITY.md, every section
[^dependabot.yml]: .github/dependabot.yml, the five entries
