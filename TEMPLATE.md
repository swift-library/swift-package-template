# Template

New swift-library packages are created from this repository. It is a complete
package that builds, tests and validates as is. It is not versioned; packages
are created from its default branch.

## Creating a package

Create the repository from this template, then replace these values in file
contents and paths:

| Template value | Replace with |
| --- | --- |
| `swift-library/swift-package-template` | the new repository, `owner/name` |
| `swift-package-template` | the package name |
| `SwiftPackageTarget` | the library target name, also its module, directories and type-name prefix |
| `<#year#>` | the current year |
| `<#copyright-holder#>` | the copyright holder |

Remove the template-only paths: `TEMPLATE.md`, `.github/workflows/upstreams.yml`
and `Documentation/Assets/`, the template's own logo. The new package then
completes the author placeholders in its documentation and owns that
documentation; later `swiftpm-docs` rule changes reach it through its own
documentation audits.

## Upstreams

Some of the template's files are produced in other repositories.
`.github/workflows/upstreams.yml` pins each producer by full commit SHA, and
its `upstreams` job fails when a file differs from what that commit produces.

| Files | Producer | Pin in `upstreams.yml` |
| --- | --- | --- |
| `AGENTS.md`, `README.md`, `CONTRIBUTING.md`, `Documentation/README.md`, `Documentation/Architecture/README.md`, `Documentation/Reference/Release.md` | The `minimal` profile of `swiftpm-docs` in swift-library/skills, with the Canonical Artifacts module, the identity values `repo-name` and `package-name`, and the requirements and commands read from `Package.swift` | The `swiftpm-docs` check action's `uses:` commit, which Dependabot moves |
| `LICENSE.txt` | `LICENSE.txt` in swift-library/.github | The `ref` of the organization standard checkout |
| `Documentation/Assets/Logo.svg`, `Documentation/Assets/Logo.png` | The `swift-package-template` entry in the swift-library/.github `DESIGN.md`, rendered by `apple-framework-icon-design` in showxu/skills | The `ref`s of the organization standard and icon generator checkouts |

The job compares the logo's SVG; the PNG is its 1024 px rendering and is
regenerated with it.

The CI, release and source policy workflows call swift-library/github-workflows
at the commit their `uses:` lines name, and that pin is their only declaration.
`.github/swift-package.json` and `.github/release.json` hold the template's own
values in the formats those workflows define. Every other file belongs to the
template, including `Package.swift`, the sources and tests, `NOTICE`,
`CHANGELOG.md`, `VERSION`, `.swift-format`, `.spi.yml`, `.gitignore` and
`.github/dependabot.yml`.

## Adopting an upstream change

An upstream change merges in its own repository. The template adopts it in a
pull request of its own that moves the pin:

1. Move the pin. Dependabot opens that pull request for the `swiftpm-docs`
   action; the checkout `ref`s are moved by hand.
2. When the `upstreams` job reports differences, regenerate the files from the
   pinned commits and commit them on the same branch:
   - Documentation: from a swift-library/skills checkout at the pinned commit,
     run `python3 skills/swiftpm-docs/scripts/export_profile.py --profile minimal --module canonical-artifacts --package-root <template> --output <template> --set repo-name=swift-package-template --set package-name=swift-package-template --force`.
   - License: copy `LICENSE.txt` from swift-library/.github at the pinned commit.
   - Logo: from showxu/skills at the pinned commit, run
     `python3 skills/apple-framework-icon-design/scripts/design_icons.py <DESIGN.md> --out <directory> --name swift-package-template --png`
     with the `DESIGN.md` of the pinned swift-library/.github commit, then copy
     `swift-package-template.svg` and `swift-package-template.png` to
     `Documentation/Assets/Logo.svg` and `Documentation/Assets/Logo.png`.
3. Review the regenerated files with the rest of the pull request.

A change to the requirements or commands in `Package.swift` also changes the
exported `README.md`; regenerate the documentation at the current pin in the
same pull request.
