# Usage guide

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

## Instantiation options

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

To instantiate from a selected template release, clone its tag:

```sh
git clone --branch v0.1.1 --depth 1 https://github.com/swift-library/swift-package-template.git
cd swift-package-template
```

The destination is an independent package; initialize its Git repository and
commit its source before running the package check.

## Validation

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

## Releases

Follow the [shared release procedure](https://github.com/swift-library/.github/blob/master/VERSIONING.md#release-procedure)
and the [template release guide](../../Documentation/Reference/ReleaseGuide.md).
Generated packages start their own independent release history.
