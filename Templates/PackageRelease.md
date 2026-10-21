# Release

Release status: partly manual. [`Scripts/check`](../../Scripts/check) validates
the package, and the [`Release`](../../.github/workflows/release.yml) workflow
validates and publishes an accepted tag.

Version rules for {{package}}, covering tags, release timing, choosing the
next version and the changelog, are in
[VERSIONING](https://github.com/swift-library/.github/blob/master/VERSIONING.md).
This document records the package's release facts and mechanics and does not
restate those rules. README owns installation and usage.

## Components and Version Sources

| Shipped component | Version meaning | Version source | Mirrors and derived fields | Update and read-only check |
| --- | --- | --- | --- | --- |
| `{{target}}` library | Library version | [`VERSION`](../../VERSION), named by `version_file` in [`.github/release.json`](../../.github/release.json) | [`CHANGELOG.md`](../../CHANGELOG.md) records release notes | The shared validator checks `VERSION` against `CHANGELOG.md` and, during publication, the signed tag |

## Compatibility Surface

Replace this paragraph with what consumers depend on: the public API of the
`{{target}}` library, its observable behavior, and the platform and Swift
floors declared in `Package.swift`.

## Dependencies and Verified Combinations

The package requires Swift 6.0, iOS 15 or macOS 12. `.github/release.json`
selects the shared CI matrix: Swift 6.0 on macOS 15 and Swift 6.3 on macOS 26,
with strict formatting checked separately.

## Derived Metadata and Drift Checks

[`Scripts/check`](../../Scripts/check) checks formatting, Swift tests and a
release build, and accepts compiler-only and format-only scopes.

## Candidate, Acceptance and Publication

Run `Scripts/check` against the accepted source. After tagging, run the
Release workflow with the tag, then resolve the tag from a fresh consumer
package.

## Evidence Reuse and Invalidation

Evidence belongs in `.build/release-validation`.

## Entry Points and Artifact Retention

| Operation | Existing command or explicit manual procedure | Required access |
| --- | --- | --- |
| Version update and check | Update `VERSION` and `CHANGELOG.md` manually; CI runs the shared validator | Repository write access |
| Candidate validation and build | `Scripts/check`; `Scripts/check --compiler-check`; `Scripts/check --format-check` | macOS with Xcode (`xcodebuild`, `xcrun`), Python 3 and Git |
| Status and interrupted-run recovery | Not established. | Not established. |
| Acceptance and publication | Run [`Release`](../../.github/workflows/release.yml) with the accepted tag; it validates the tag and publishes the GitHub release. Then resolve the tag from a fresh consumer package. | Repository write access to run workflows |
| Cleanup | Not established. | Not established. |
