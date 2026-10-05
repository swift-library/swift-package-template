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
  <img src="https://img.shields.io/badge/platforms-iOS%2018%2B%20%7C%20macOS%2015%2B-lightgrey" alt="Platforms: iOS 18+ | macOS 15+">
  <a href="LICENSE.txt"><img src="https://img.shields.io/badge/license-Apache--2.0-blue" alt="License: Apache-2.0 WITH Swift-exception"></a>
</p>

[Overview](#overview) · [Install](#install) · [Quick start](#quick-start) ·
[Usage](#usage) · [Requirements](#requirements) ·
[Documentation](#documentation) · [Contributing](#contributing) ·
[License](#license)

> [!NOTE]
> swift-package-template is a GitHub repository template, not a package
> dependency. Create a new repository from it instead of adding it to
> `Package.swift`; the template itself has no tagged releases.

## Overview

swift-package-template starts a Swift library with the swift-library
organization's release and maintenance defaults already in place. Create a
repository from it, run `Scripts/instantiate` once to apply your package,
target, and repository names, and the result is an independently versioned
package with strict formatting, release validation, and CI. Like
`swift package init --type library`, it produces a library target and a test
target, and it adds the files a published package needs.

- A library product and test target with iOS 18 and macOS 15 deployment floors
  and Swift tools 6.0.
- `Scripts/instantiate`, which replaces the template's placeholder names in
  file contents and paths.
- `Scripts/check`, which validates version inputs, strict `swift-format`
  formatting, release tooling, tests, and a release build.
- CI, release, and commit-message workflows built on the organization's shared
  workflows, and weekly Dependabot updates for Swift dependencies and GitHub
  Actions.
- `VERSION` and `CHANGELOG.md` release inputs, a versioning and release
  policy, and a release guide.
- Contributing, security, and code of conduct files, and issue and pull
  request templates.

## Install

### Create a repository

On the template's
[GitHub page](https://github.com/swift-library/swift-package-template),
choose **Use this template** > **Create a new repository**, then clone the new
repository. With GitHub CLI, create and clone it in one step:

```bash
gh repo create swift-library/swift-my-library \
  --template swift-library/swift-package-template --public --clone
cd swift-my-library
```

Replace `swift-library` with your own account or organization when the
package lives elsewhere.

### Instantiate the package

The new repository is a copy of the template, with placeholder names such as
`<#swift-package#>`, `<#swift-package-target#>`, and `swift-package-target`.
`Scripts/instantiate` writes a renamed copy of the package to an empty
directory, which must be outside the template source or inside its `.build`
directory. Generate the package under `.build`, then replace the template
files with it:

```bash
Scripts/instantiate --output .build/instantiated \
  --package swift-my-library --target MyLibrary \
  --repository swift-library/swift-my-library --copyright "Your Name"
git rm -rq .
cp -R .build/instantiated/. .
git add -A
```

Git records the source and test directories as renames, and the
template-only files `Scripts/instantiate`, `Scripts/check-template`, and
`Tests/ReleaseTools/test_instantiate.py` are removed.

### Finish setup

Instantiation leaves these steps to you:

1. Add owners to `.github/CODEOWNERS`, which contains only a comment.
2. Replace or remove `Documentation/Assets/Logo.svg`, which is the template's
   logo.
3. Replace the one-line description in the generated `README.md`.
6. Enable private vulnerability reporting in the repository's security
   settings before publishing; `SECURITY.md` sends reporters there.
7. Enable the commit-message hook with
   `git config --local core.hooksPath .githooks`.

## Quick start

Create the repository, instantiate it, and run the package check:

```bash
gh repo create swift-library/swift-my-library \
  --template swift-library/swift-package-template --public --clone
cd swift-my-library

Scripts/instantiate --output .build/instantiated \
  --package swift-my-library --target MyLibrary \
  --repository swift-library/swift-my-library --copyright "Your Name"
git rm -rq .
cp -R .build/instantiated/. .
git add -A

Scripts/check
```

`Scripts/check` validates `VERSION` and `CHANGELOG.md`, lints with
`swift-format --strict`, runs the release tooling tests and `swift test`, and
builds in the release configuration. After the [setup steps](#finish-setup),
commit with a Conventional Commit subject and push:

```bash
git commit -m "feat: create swift-my-library"
git push
```

## Usage

### Instantiate options

All five options are required:

- `--output`: an empty destination directory, outside the template source or
  under its `.build` directory.
- `--package`: the package name, such as `swift-my-library`. It uses lowercase
  letters, digits, and hyphens, starts with a letter, and replaces
  `<#swift-package#>`, `<#swift-package-name#>`, and `swift-package-template`.
- `--target`: the library target and module name, such as `MyLibrary`. It must
  be a Swift identifier, and it replaces `<#swift-package-target#>`,
  `swift-package-target`, and `swift_package_target`, including in directory
  and file names.
- `--repository`: the GitHub `owner/repository`, such as
  `swift-library/swift-my-library`. It replaces `swift-library/<#swift-package#>`
  in links and sets `repository` in `.github/release.json`.
- `--copyright`: the copyright holder that `NOTICE` and the copyright headers
  of the manifest, sources, tests, and scripts name, with the current year.

### Generated files

`Scripts/instantiate` copies every file that Git tracks or would track, except
the template-only `Scripts/instantiate`, `Scripts/check-template`, and
`Tests/ReleaseTools/test_instantiate.py`. It applies the replacements above to
UTF-8 text, replaces each template copyright header with your copyright
holder, and copies other files, such as images, byte for byte. It then writes:

- `README.md`, with install, requirements, maintenance, and license sections
  and a one-line description.
- `CONTRIBUTING.md` for the new package.
- `NOTICE`, with the package name, the current year, and the copyright holder.
- `.github/CODEOWNERS`, with only a comment.
- `.github/release.json`, with the new `repository` and with `check_command`
  and every CI `command` running `Scripts/check`.
- `VERSION` and `CHANGELOG.md` for version 0.1.0.

The generated README's install snippet depends on that first version with
`.upToNextMinor(from: "0.1.0")`.

### Checks

In a generated package, `Scripts/check` runs every check, and two options
select the CI scopes:

```bash
Scripts/check
Scripts/check --format-check
Scripts/check --compiler-check
```

`--format-check` runs `swift-format lint --strict` over `Package.swift`,
`Sources`, and `Tests`. `--compiler-check` runs the release tooling tests,
`swift test`, and a release build with the resolved dependency versions. Every
scope first runs `Scripts/validate-version`, which requires one SemVer version
in `VERSION` and exactly one nonempty matching `CHANGELOG.md` entry, and every
scope records its toolchain, SDK, and results under
`.build/release-validation`.

In this template repository, `Scripts/check-template` accepts the same options.
Its compiler scope first runs `Tests/ReleaseTools/test_instantiate.py`, which
checks binary copies, template residue, and a build and test of a generated
package. It then instantiates a fixture package in a temporary directory,
commits it there, and runs the fixture's `Scripts/check`.

### Releases

Choose the version in `VERSION` and describe it in a `CHANGELOG.md` entry.
During 0.x, compatible fixes increase PATCH, and compatible features and
breaking changes increase MINOR; from 1.0.0, breaking changes increase MAJOR.
The [release guide](Documentation/Reference/ReleaseGuide.md) covers the
sequence: run `Scripts/check`, push the candidate, verify a fresh consumer,
create the `vVERSION` tag, and dispatch the Release workflow with that tag.

### Instantiate without a GitHub template

`Scripts/instantiate` also works from a plain clone of the template. Write the
package to a new directory, make it a repository, and publish it:

```bash
git clone https://github.com/swift-library/swift-package-template.git
swift-package-template/Scripts/instantiate --output swift-my-library \
  --package swift-my-library --target MyLibrary \
  --repository swift-library/swift-my-library --copyright "Your Name"
cd swift-my-library
git init -b master
git add .
git commit -m "feat: create swift-my-library"
Scripts/check
gh repo create swift-library/swift-my-library --public --source . --push
```

`Scripts/check` needs a commit to validate, so run it after the first commit.

## Requirements

- Swift 6.0 or later
- iOS 18 or later, macOS 15 or later

These are the defaults for generated packages. The deployment floors cover the
current system support window of iOS 18, 26, and 27 and macOS 15, 26, and 27,
and the compiler minimum is maintained independently. CI runs Swift 6.0 on
macOS 15 and Swift 6.3 on macOS 26.

`Scripts/instantiate` and `Scripts/check` need Python 3 and Git, and
`Scripts/check` needs macOS with Xcode for `xcrun swift-format` and
`xcodebuild`. GitHub CLI is optional.

## Documentation

- [Versioning and release policy](Documentation/Architecture/VersioningAndRelease.md):
  version authority, compatibility, the system support window, and release
  acceptance.
- [Release guide](Documentation/Reference/ReleaseGuide.md): the steps from a
  candidate to a published release.
- [Organization defaults](https://github.com/swift-library/.github): the
  shared workflows and policies the template adopts.
- [Changelog](CHANGELOG.md)

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and the
[code of conduct](CODE_OF_CONDUCT.md) before opening a pull request, and run
`Scripts/check-template` before submitting changes. `Scripts/instantiate` reads
every file as UTF-8 text, so keep template files text-only. Report
vulnerabilities through the private route in [SECURITY.md](SECURITY.md).

## License

swift-package-template is available under the Apache License 2.0 with the
Swift Runtime Library Exception. See [LICENSE.txt](LICENSE.txt) and
[NOTICE](NOTICE). Packages created from it use the same license, and
instantiation writes a `NOTICE` that names your copyright holder.
