# Swift Package Template

The package template for swift library.

## Usage

## Adding `<#swift-package#>` as a Dependency

To use the `<#swift-package#>` plugin in a SwiftPM project, 
add it to the dependencies for your package and your target:

```swift
let package = Package(
  // name, platforms, products, etc.
  dependencies: [
    // other dependencies
    .package(url: "https://github.com/swift-library/<#swift-package#>", from: "0.0.1"),
  ],
  targets: [
    .executableTarget(
      name: "<command-line-tool>",
      dependencies: [
        // other dependencies
        .product(name: "<#swift-package-target#>", package: "<#swift-package#>"),
      ],
      plugins: [
        .plugin(name: "<#swift-package-target#>", package: "<#swift-package#>"),
      ]
    ),
    // other targets
  ]
)
```

### Supported Versions

The most recent versions of <#swift-package#> support Swift 5.8 and newer. The minimum Swift version supported by <#swift-package#> releases are detailed below:

<#swift-package#> | Minimum Swift Version
----------|----------------------
`0.0.1`   | 5.8

<!-- Link references for readme -->

[swift]: https://github.com/apple/swift
