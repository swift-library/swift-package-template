<p align="center">
  <img src="Documentation/Assets/Logo.svg" width="160" alt="swift-package-template logo">
</p>

<h1 align="center">swift-package-template</h1>

<p align="center">
  The swift-library repository template for new Swift packages, with release checks, CI, and maintenance defaults in place.
</p>

<p align="center">
  <a href="https://github.com/swift-library/swift-package-template/actions/workflows/ci.yml"><img src="https://github.com/swift-library/swift-package-template/actions/workflows/ci.yml/badge.svg?branch=master" alt="CI"></a>
  <img src="https://img.shields.io/badge/Swift-6.0%2B-F05138" alt="Swift 6.0+">
  <img src="https://img.shields.io/badge/platforms-iOS%2015%2B%20%7C%20macOS%2012%2B-lightgrey" alt="Platforms: iOS 15+ | macOS 12+">
  <a href="LICENSE.txt"><img src="https://img.shields.io/badge/license-Apache--2.0-blue" alt="License: Apache-2.0 WITH Swift-exception"></a>
</p>

[Overview](#overview) · [Install](#install) · [Quick start](#quick-start) ·
[Usage](#usage) · [Requirements](#requirements) ·
[Documentation](#documentation) · [Contributing](#contributing) ·
[License](#license)

## Overview

swift-package-template creates independently versioned Swift libraries with
strict formatting, shared CI and release validation, and weekly dependency
updates. Its tagged releases version the template and its generation tools.
Create a repository from it and instantiate your package before adding library
implementation; the template itself is not a package dependency.

The generated library and test target require Swift 6.0, iOS 15 or macOS 12.
`VERSION` and `CHANGELOG.md` declare the generated package's first release.
Shared workflows validate version inputs and PR titles, and package checks own
formatting, builds and tests. Organization community defaults apply to new
repositories in swift-library.

## Install

Create a repository from the template's [GitHub page](https://github.com/swift-library/swift-package-template),
or use GitHub CLI:

```sh
gh repo create swift-library/swift-my-library \
  --template swift-library/swift-package-template --public --clone
cd swift-my-library
```

Replace `swift-library` with the account or organization that owns your package.

## Quick start

Generate your package into the ignored build directory, then replace the
tracked template files:

```sh
Scripts/instantiate --output .build/instantiated \
  --package swift-my-library --target MyLibrary \
  --repository swift-library/swift-my-library --copyright "Your Name"
git rm -rq .
cp -R .build/instantiated/. .
git add -A
git commit -m "feat: create swift-my-library"
Scripts/check
```

The generator removes its own template tooling from the generated package.
Replace the README's one-line description and the repository logo, and enable
private vulnerability reporting before publication. Repositories outside
swift-library must select their owner's policy workflow and community defaults.

## Usage

### Instantiation options

All five options are required:

| Option | Meaning |
| --- | --- |
| `--output` | An empty destination outside the source or under its `.build` directory |
| `--package` | Package name using lowercase letters, digits and hyphens, starting with a letter |
| `--target` | Swift identifier for the library product, module and target |
| `--repository` | GitHub `owner/repository` used for links and release configuration |
| `--copyright` | Copyright holder for NOTICE and source headers, paired with the current year |

The generator substitutes package and target identities in tracked text files
and paths, preserves binary assets, and writes package-specific README,
CONTRIBUTING and NOTICE files. It sets version 0.1.0 with an Unreleased changelog
section and initial release notes. Every generated CI command runs
`Scripts/check`. Install snippets use a next-minor requirement for version 0.1.0.

You can also instantiate directly from a clone of a selected template tag.
The destination is an independent package; initialize its Git repository and
commit its source before running the package check.

### Validation

In a generated package:

```sh
Scripts/check
Scripts/check --format-check
Scripts/check --compiler-check
```

The format scope runs strict `swift-format` checks over the manifest, source
and tests. The compiler scope runs Swift tests and a release build. Each scope
records source and toolchain evidence under `.build/release-validation`.
The shared workflows own version, changelog, compiler-declaration and signed-tag
validation.

In this repository, run `Scripts/check-template`, which accepts the same scope
options. It tests instantiation, binary preservation and identity substitution,
then builds and tests a generated package and runs that package's check command.

### Releases

Follow the [shared release procedure](https://github.com/swift-library/.github/blob/master/VERSIONING.md#release-procedure)
and the [template release guide](Documentation/Reference/ReleaseGuide.md).
Generated packages start their own independent release history.

## Requirements

- Swift 6.0 or later
- Generated deployment floors: iOS 15 and macOS 12
- Python 3 and Git for generation and validation
- macOS with Xcode for strict formatting and SDK evidence

CI tests Swift 6.0 on macOS 15 and Swift 6.3 on macOS 26. The maintained system
window covers iOS 18/26/27 and macOS 15/26/27 independently of deployment floors.
GitHub CLI is optional.

## Documentation

- [Versioning and release](Documentation/Architecture/VersioningAndRelease.md):
  the template's compatibility surface and validation requirements.
- [Release guide](Documentation/Reference/ReleaseGuide.md): package-specific acceptance.
- [Organization defaults](https://github.com/swift-library/.github): shared
  workflows, contribution and release standards.
- [Changelog](CHANGELOG.md)

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and run `Scripts/check-template` before
submitting changes. Follow the shared [code of conduct](https://github.com/swift-library/.github/blob/master/CODE_OF_CONDUCT.md).
Report vulnerabilities through [SECURITY.md](SECURITY.md).

## License

Apache License 2.0 with the Swift Runtime Library Exception. See
[LICENSE.txt](LICENSE.txt) and [NOTICE](NOTICE). Generated packages use the same
license and a NOTICE naming their copyright holder.
