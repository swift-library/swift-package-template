# Release

Release status: partly manual;
[`Scripts/check-template`](../../Scripts/check-template) validates generated
packages, and publication acceptance requires resolving the remote tag from a
fresh consumer and running the generated package's `Scripts/check`.

Version rules for swift-package-template, covering tags, release timing, choosing
the next version and the changelog, are in
[VERSIONING](https://github.com/swift-library/.github/blob/master/VERSIONING.md).
This document records the repository's release facts and mechanics and does not
restate those rules.

## Components and Version Sources

| Shipped component | Version meaning | Version source | Mirrors and derived fields | Update and read-only check |
| --- | --- | --- | --- | --- |
| swift-package-template | Template release | `VERSION`, named by `version_file` in [`.github/release.json`](../../.github/release.json) | `CHANGELOG.md` records its behavior. | Not established. |

Generated packages start at version 0.1.0 and release independently.

## Compatibility Surface

The template owns generated package structure, instantiation options,
validation commands and default compiler and platform requirements.
`Scripts/instantiate` creates a library and test target with the selected names.

## Dependencies and Verified Combinations

`.github/release.json` selects the shared CI matrix.

Generated packages require Swift 6.0, iOS 15 or macOS 12. The maintained system
window covers iOS 18/26/27 and macOS 15/26/27. CI tests Swift 6.0 on macOS 15
and Swift 6.3 on macOS 26, with strict formatting checked separately.

## Derived Metadata and Drift Checks

`Scripts/check-template` tests instantiation, binary asset preservation,
identity substitution and compilation of a generated package. It then runs
the generated package's `Scripts/check`, which checks formatting, Swift tests
and a release build. Each command accepts compiler-only and format-only scopes.

## Candidate, Acceptance and Publication

Run `Scripts/check-template` against the accepted source. After tagging, resolve
the remote tag from a fresh consumer and instantiate a package from that tag.
The generated package must pass `Scripts/check` before publication is accepted.

## Evidence Reuse and Invalidation

Evidence belongs in `.build/release-validation`.

## Entry Points and Artifact Retention

| Operation | Existing command or explicit manual procedure | Required access |
| --- | --- | --- |
| Version update and check | Not established. | Not established. |
| Candidate validation and build | `Scripts/check-template`; `Scripts/check-template --compiler-check`; `Scripts/check-template --format-check` | Not established. |
| Status and interrupted-run recovery | Not established. | Not established. |
| Acceptance and publication | Run [`Release`](../../.github/workflows/release.yml) with the accepted tag; it validates the tag and publishes the GitHub release. Resolve the remote tag from a fresh consumer, instantiate a package from that tag and run the generated package's `Scripts/check`. | Repository write access to run workflows |
| Cleanup | Not established. | Not established. |
