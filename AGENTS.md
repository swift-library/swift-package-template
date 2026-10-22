# swift-package-template Agent Guide

Read `README.md` first for repository purpose and entry points.
Apply this guide before making changes.

## First-Principles Work

Before changing code, docs, schemas, scripts, templates, examples, governance,
or automation, reduce the task to observable behavior, root cause, invariant,
owner, data flow, and validation.

- Do not silently choose among plausible interpretations. State assumptions,
  surface conflicts, and ask when the decision materially changes the result.
- Deliver the complete requested behavior with bounded design. Do not stop at a
  toy result when production behavior is requested, and do not add abstraction,
  configurability, workflow machinery, or future-facing features unless the
  request, source evidence, or owning invariant requires them.
- Change the owning layer, not the nearest convenient file.
- Keep changes traceable to the request, source evidence, or owning invariant.
- Do not clean up, reformat, rename, or refactor unrelated nearby material
  unless it is required by the request or owning invariant.
- Use the strongest feasible validation for the result. If validation is
  skipped, say what was skipped and why.

Use this check:

1. What behavior is wrong, missing, or at risk?
2. What root cause explains it?
3. What invariant must hold?
4. Which artifact, layer, or workflow owns it?
5. What data or decision flows into that owner?
6. What remains variable, configurable, or case-local?
7. What evidence proves the result beyond one literal case?

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

- Before changing versions, dependencies, packaging or release workflows, read
  `VERSIONING.md`, or the organization VERSIONING the project adopts, for
  version rules and `Documentation/Reference/Release.md` for this repository's release facts and check
  entry points.

- For repository-native documentation placement, read `Documentation/README.md`
  before editing.
- For current canonical structure, read
  `Documentation/Architecture/README.md` and the relevant architecture files.
- For design-in-progress, use `Documentation/Proposals/*` when that subtree is
  present.
- For change history, consult `Documentation/Decisions/*`,
  `Documentation/Migrations/*`, and `Documentation/Archive/*` when those
  subtrees are present.
- For GitHub-facing collaboration files, use `.github/` and root governance
  files.
- Stop and clarify before mixing route instructions into `README` files or
  index text into `AGENTS.md`.

## Authority

- `AGENTS.md` is the agent guide: first-principles guardrails, task
  route, authority boundaries, boundary guardrails, and code review rules.
- `README`-class files index scope and placement.
- `Documentation/Architecture/*` is current truth.
- `Documentation/Proposals/*` is proposal space when that subtree is present.
- `Documentation/Decisions/*`, `Documentation/Migrations/*`, and
  `Documentation/Archive/*` are history when those subtrees are present.
- `.github/*` is GitHub-facing governance.

## Boundary Guardrails

After the owner and invariant are clear, classify concrete values by stability,
variability, and ownership before writing reusable artifacts.

Do not promote context-bound values into reusable artifacts. A value is
context-bound if it depends on the current machine, local workspace, current
input, one fixture, one runtime run, one user-specific path, or temporary
execution state.

Keep shipped documentation focused on current product facts, supported behavior,
and operating guidance. Keep temporary implementation notes, local evidence,
local paths, run-specific artifacts, and historical comparison notes out of
README files, Reference docs, API docs, and bundled user-facing skills. Promote
only accepted decision records into
`Documentation/Decisions/*` and durable transition or cutover records into
`Documentation/Migrations/*`.

Use this decision test:

- If a value changes by input, get it from input, spec, config, parameters, or
  an explicit user decision.
- If a value changes by environment, get it from configuration, runtime state,
  environment variables, or local execution notes.
- If a value belongs only to one example, fixture, or run, keep it there. Do
  not generalize it into reusable docs, schemas, templates, scripts,
  validation rules, or automation.
- If the artifact being edited is not the source of truth for the value, do not
  hardcode it there. Pass it in, derive it, configure it, or link to the
  owning artifact.
- Only stable invariants and values owned by the current artifact may be fixed
  in reusable artifacts.

Classify concrete values before writing:

1. Name the variable parts.
2. Decide which artifact owns each variable.
3. Replace context-bound literals with placeholders, parameters, config keys,
   derived values, or links to the owning artifact.
4. Keep concrete literals only inside the artifact that owns them.

When in doubt, use a placeholder, parameter, configuration key, or repo-owned
source of truth instead of a literal value.

## Code Review Rules

### Compatibility and versioning

- Flag a change to the compatibility surface recorded in
  `Documentation/Reference/Release.md`, such as public API, observable
  behavior or a raised minimum platform or Swift version, without the
  changelog entry and version bump VERSIONING requires. Safe path: record the
  change under the next version with that bump.

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

- Keep Agent Guide and Index separate.
- Keep current truth out of proposal and history subtrees when they are
  present.
- Keep GitHub collaboration configuration out of `Documentation/`.
