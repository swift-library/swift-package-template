# Release Guide

Follow the [shared release procedure](https://github.com/swift-library/.github/blob/master/VERSIONING.md#release-procedure)
and [template compatibility requirements](../Architecture/VersioningAndRelease.md).

Run `Scripts/check-template` against the accepted source. After tagging, resolve
the remote tag from a fresh consumer and instantiate a package from that tag.
The generated package must pass `Scripts/check` before publication is accepted.
