By submitting a pull request, you represent that you have the right to license
your contribution to swift-library project, and agree by submitting the patch
that your contributions are licensed under the [package
license](LICENSE.txt).

---

Before submitting the pull request, please make sure you have tested your
changes and that they follow the Swift project [guidelines for contributing
code](https://swift-library.github.io/contributing/#contributing-code).


## Development Policy

- Commit subjects must follow Conventional Commits:
  - `feat(scope): summary`
  - `fix: summary`
- Local validation:
  - `git config --local core.hooksPath .githooks`
- CI validation:
  - `.github/workflows/commit-message.yml` enforces commit subject format on PRs.

- Repository type policy: `swift-package`.
- All contributors (human and AI) must respect repository `.swift-format` when editing Swift code.
- Keep formatting consistent before commit.

## Validation and Release

Run Scripts/check-template in this template repository. Generated packages run
Scripts/check. Read Documentation/Architecture/VersioningAndRelease.md before
changing release inputs or requirements. Workflow and dependency updates need
compatibility and CI review.
