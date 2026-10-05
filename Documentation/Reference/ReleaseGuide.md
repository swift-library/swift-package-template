# Release Guide

Read the [swift-library versioning standard](https://github.com/swift-library/.github/blob/master/VERSIONING.md)
and the [Versioning and Release policy](../Architecture/VersioningAndRelease.md).
Select VERSION manually and add a nonempty CHANGELOG entry. Run Scripts/check,
validate declared platform behavior, commit the candidate and push it. Verify a
fresh remote consumer before creating the immutable vVERSION tag. Verify its
SemVer installation before dispatching the Release workflow with that existing
tag. Retain compiler, system, SDK, dependency and consumer evidence with the
release. Source corrections after tagging use a new version.
