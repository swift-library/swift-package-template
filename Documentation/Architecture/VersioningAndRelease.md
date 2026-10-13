# Versioning and Release

This repository follows the [shared release standard](https://github.com/swift-library/.github/blob/master/VERSIONING.md).
`VERSION` declares the template release, `CHANGELOG.md` records its behavior,
and `.github/release.json` selects the shared CI matrix.

## Compatibility surface

The template owns generated package structure, instantiation options,
validation commands and default compiler and platform requirements.
`Scripts/instantiate` creates a library and test target with the selected names.
Generated packages start at version 0.1.0 and release independently.

## Requirements and validation

Generated packages require Swift 6.0, iOS 15 or macOS 12. The maintained system
window covers iOS 18/26/27 and macOS 15/26/27. CI tests Swift 6.0 on macOS 15
and Swift 6.3 on macOS 26, with strict formatting checked separately.

`Scripts/check-template` tests instantiation, binary asset preservation,
identity substitution and compilation of a generated package. It then runs
the generated package's `Scripts/check`, which checks formatting, Swift tests
and a release build. Each command accepts compiler-only and format-only scopes.
Evidence belongs in `.build/release-validation`.
