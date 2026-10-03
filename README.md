# Swift Package Template

Create an independently versioned Swift library with the swift-library release
and maintenance defaults.

```sh
Scripts/instantiate --output ../MyLibrary --package swift-my-library \
  --target MyLibrary --repository swift-library/swift-my-library \
  --copyright "Your Name"
```

The destination must be empty. The command sets the package/module names,
repository identity, contributor ownership and initial release inputs. Develop
and run `Scripts/check` inside the generated repository. Enable its private
vulnerability reporting before publishing.

The default deployment floors are iOS 18 and macOS 15, covering the current
three-generation system window. Swift tools 6.0 is the compiler minimum.
Compiler requirements and system support are maintained independently.

- [Version and maintenance policy](Documentation/Architecture/VersioningAndRelease.md)
- [Release guide](Documentation/Reference/ReleaseGuide.md)
- [Organization defaults](https://github.com/swift-library/.github)
- [Contributing](CONTRIBUTING.md)

New libraries use Apache License 2.0 with the Swift Runtime Library Exception
(`Apache-2.0 WITH Swift-exception`). See [LICENSE.txt](LICENSE.txt) and [NOTICE](NOTICE).
