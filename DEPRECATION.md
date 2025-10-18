# Deprecation Notice

Status: DEPRECATED
Date: 2025-10-18

## Summary
This repository is deprecated and is no longer maintained. Use this project at your own risk. This document explains why it's deprecated, recommended alternatives, migration steps, and the deprecation timeline.

## Why deprecated
- Reason(s): The project is no longer actively maintained by the author. (Update this section with more specific reasons if desired — e.g., upstream API changes or security concerns.)

## Recommended alternatives
- If you need dynamic DNS for Google Cloud DNS, consider using actively maintained tools or scripts that support the current Google Cloud DNS API.
- Example alternatives:
  - Cloud DNS official tools / automation (check Google Cloud documentation)
  - Well-maintained DDNS projects on GitHub (search for "Google Cloud DNS DDNS")

## Migration guidance
1. Stop using this repository for new deployments.
2. If you currently run it:
   - Inspect your configuration and credentials.
   - Identify an alternative listed above and read their migration docs.
3. Example steps (high level):
   - Export current DNS records as needed.
   - Replace cron/automation with the replacement project's recommended workflow.
   - Test in a staging environment before switching production.

## Timeline
- 2025-10-18 — Repository marked as deprecated and NOTICE added.
- (Optional) 2026-01-01 — Repository will be archived if no maintenance is resumed.

## Contact
If you need help migrating or have questions, open an issue or contact the maintainer: jcruse03

## If you are a package owner (npm/PyPI/etc.)
- npm: run `npm deprecate <package>@<version> "This package is deprecated — use <replacement>"`
- PyPI: publish a new release with a deprecation note in the long_description and consider updating classifiers (no direct deprecate command).

## Security
If this project contains unresolved security issues, please raise them (or use the GitHub Security Advisories) so they can be addressed separately.

Thank you for using the project. We recommend moving to the alternatives above for better maintenance and security.
