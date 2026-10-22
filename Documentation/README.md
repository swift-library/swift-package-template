# Documentation

- [Release](Reference/Release.md): release facts and mechanics; version rules are in VERSIONING.

This directory indexes repository-native documentation for `swift-package-template`.

## Areas

- `Architecture/`: current truth for repository documentation structure
- `Proposals/`: design-in-progress and open alternatives when needed
- `Decisions/`: decision records and rationale when needed
- `Migrations/`: transition and cutover records when needed
- `Archive/`: retired or superseded material kept for record when needed
- `Reference/`: supporting reference material and examples when needed

Target-level API documentation belongs with the SwiftPM target it documents,
normally under `Sources/<Target>/<Target>.docc/`. Link to those catalogs from
this index when present, but do not move them under `Documentation/` by default.

## Placement Rules

- Put only current canonical guidance in `Architecture/`.
- Put unresolved changes and alternatives in `Proposals/` when that subtree is
  present.
- Put historical records in `Decisions/`, `Migrations/`, and `Archive/` when
  those subtrees are present.
- Put supporting reference material in `Reference/` when that subtree is
  present.
- Keep DocC catalogs with their SwiftPM targets; treat `.doccarchive`
  directories as generated output unless this repository explicitly governs
  checked-in documentation archives.
- Keep GitHub-facing governance in `.github/`, not here.
