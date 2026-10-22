<div align="center">

<p align="center">
  <a href="https://github.com/swift-library/swift-package-template"><img src="Documentation/Assets/Logo.svg" width="160" alt="swift-package-template logo"></a>
</p>

<h1 align="center">swift-package-template</h1>

<p align="center">
  Start a named Swift package with one command and shared CI and release checks.
</p>

<p align="center">
  <a href="https://github.com/swift-library/swift-package-template/actions/workflows/ci.yml"><img src="https://github.com/swift-library/swift-package-template/actions/workflows/ci.yml/badge.svg?branch=master" alt="CI"></a>
  <img src="https://img.shields.io/badge/Swift-6.0%2B-F05138?style=flat" alt="Swift 6.0+">
  <img src="https://img.shields.io/badge/platforms-iOS%2015%2B%20%7C%20macOS%2012%2B-lightgrey?style=flat" alt="Platforms: iOS 15+ | macOS 12+">
  <a href="LICENSE.txt"><img src="https://img.shields.io/badge/license-Apache--2.0-blue?style=flat" alt="License: Apache-2.0 WITH Swift-exception"></a>
</p>

<p align="center">
  <a href="#overview">Overview</a> ·
  <a href="#quick-look">Quick look</a> ·
  <a href="#install">Install</a> ·
  <a href="#usage">Usage</a> ·
  <a href="#requirements">Requirements</a> ·
  <a href="#documentation">Documentation</a> ·
  <a href="#contributing">Contributing</a> ·
  <a href="#license">License</a>
</p>

</div>

## Overview

Choose the package, module, and repository names once, then build on a generated library and test target. Instantiation replaces identities in paths and tracked text, preserves binary assets, and removes the template tooling; the [usage guide](Documentation/Reference/Usage.md) covers setup and validation.

## Quick look

```sh
Scripts/instantiate --output .build/instantiated \
  --package swift-my-library --target MyLibrary \
  --repository swift-library/swift-my-library --copyright "Your Name"
```

## Install

Create a repository from the template's [GitHub page](https://github.com/swift-library/swift-package-template),
or use GitHub CLI:

```sh
gh repo create swift-library/swift-my-library \
  --template swift-library/swift-package-template --public --clone
cd swift-my-library
```

Replace `swift-library` with the account or organization that owns your package.

## Usage

Create a repository from this template, instantiate it with your identities, and replace the tracked template files with the output. The [usage guide](Documentation/Reference/Usage.md) covers the replacement commands, every option, and validation of the generated package.

## Requirements

- Swift 6.0 or later
- Generated deployment floors: iOS 15 and macOS 12
- Python 3 and Git for generation and validation
- macOS with Xcode for strict formatting and SDK evidence

CI tests Swift 6.0 on macOS 15 and Swift 6.3 on macOS 26. The maintained system
window covers iOS 18/26/27 and macOS 15/26/27 independently of deployment floors.
GitHub CLI is optional.

## Documentation

- [Usage guide](Documentation/Reference/Usage.md): examples, behavior, and limits.
- [Release](Documentation/Reference/Release.md): release facts and mechanics; version rules are in VERSIONING.
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
