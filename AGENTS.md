# swift-package-template Agent Guide

Read `README.md` first for repository purpose, package surface, and entry
points.

## First-Principles Work

- Name the behavior, root cause, invariant, owner, data flow, and validation
  before changing reusable files.
- Change the owning artifact, not the nearest convenient file.
- Keep concrete values in the artifact that owns them.
- Validate Swift package changes with package-local build or test checks.

## Canonical Artifacts

- Treat conversation, review feedback, plans, and intermediate attempts as
  editing input. Recompute the complete accepted result before finalizing.
- Active artifacts depend only on that result and their repository role, not
  on the editing path. Apply this to code, symbols, files, wrappers, branches,
  configuration, schemas, defaults, generated sources, scripts, templates,
  automation, comments, DocC, diagrams, tests, fixtures, snapshots, examples,
  and normative docs.
- If an intermediate result is `A + B` and the accepted result is `A`, express
  `A` directly. Remove `B` and its residual surface rather than retaining names
  such as `AOnly` or `AWithoutB`, or prose such as "B was removed."
- Normalize by semantic identity and artifact role, not by token. A rejected
  current capability does not invalidate a distinct historical fact,
  migration, ownership record, or safety boundary that uses the same term.
- Keep a negative constraint only when excluding `B` is independently required
  by a current compatibility, safety, or ownership invariant.
- A disabled B flag, skipped B test, dead B branch, retained B fixture, or
  "do not add B" rule is residue when it exists only because B was attempted;
  disabled state alone is not an invariant.
- Keep change history only in commits, pull requests, changelogs, release
  records, migrations, archives, or accepted decision records with durable
  value. Do not create a history artifact merely to preserve a correction.
- Preserve role-owned facts unless separate evidence changes them; do not
  rewrite history or ownership merely to make a rejected term disappear.
- Leave an already-correct history, migration, provenance, ownership, or safety
  artifact unchanged when the task does not change its facts. Do not polish or
  restate it merely because it is relevant to the current edit.
- Comments explain non-obvious current semantics and invariants, not the
  sequence of edits.
- Before handoff, verify that a new agent with no editing conversation can
  derive the complete current behavior, boundaries, and operating guidance
  without mentally subtracting a rejected concept.

## Task Route

Read the organization's
[VERSIONING.md](https://github.com/swift-library/.github/blob/master/VERSIONING.md)
and Documentation/Architecture/VersioningAndRelease.md before changing
versions, requirements, dependencies or release workflows.

- Use `README.md` as the package entry point.
- Use `Package.swift` for package graph, products, targets, and dependencies.
- Keep source changes under `Sources/` and tests under `Tests/`.
- For GitHub-facing collaboration files, use `.github/` and root governance
  files when present.

## Authority

- `AGENTS.md` is the agent guide for package work, including its code review
  rules.
- `README.md` is the user-facing package manual and index.
- `Package.swift` owns SwiftPM package structure.
- Source and test files own implementation behavior.

## Boundary Guardrails

- Do not promote machine-local paths, one-run state, or fixture-only values into
  reusable docs, scripts, templates, or automation.
- If a value changes by input or environment, pass it in, configure it, derive
  it, or link to the owning artifact.

## Code Review Rules

### Compatibility and versioning

- Flag a change to public API or observable behavior, including a raised
  minimum platform or Swift version, without the change record and version
  bump `Documentation/Architecture/VersioningAndRelease.md` requires. Safe
  path: record the change under the next version with that bump.

### Claims

- Flag README, DocC, or release-note statements that the code and tests do
  not support: capabilities that do not exist, existing behavior described as
  new, or platforms CI does not build. Safe path: describe what the code
  shows.

### Public documentation

- Flag a new public symbol without a documentation comment, and public prose
  that compares the package with other projects or describes internal
  process. Safe path: document the symbol, and describe only this package's
  own behavior.

### Tests

- Flag a behavior change without a test that would fail before the change.
  Safe path: add the test beside the existing suite for that behavior.

## Operating Notes

- Keep this guide compact. Put durable user-facing explanations in `README.md`
  or focused docs.
