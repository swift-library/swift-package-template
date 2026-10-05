# Changelog

## 0.1.0

- `Scripts/instantiate` creates an independent Swift package from the template.
  It applies the package, target and repository names, puts the copyright
  holder in `NOTICE` and every copyright header, copies binary files unchanged,
  and writes the README, CONTRIBUTING, CODEOWNERS, `VERSION` and `CHANGELOG.md`
  for version 0.1.0.
- Generated packages include `Scripts/check` with format and compiler scopes,
  `Scripts/validate-version`, the shared CI and Release workflows, and a
  `.github/release.json` whose commands run `Scripts/check`.
- `Scripts/check-template` tests instantiation, then runs the full check of a
  generated package.
- Generated packages default to iOS 18 and macOS 15 deployment floors and Swift
  tools 6.0, under Apache License 2.0 with the Swift Runtime Library Exception.
