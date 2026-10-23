// swift-tools-version: 6.3
// SPDX-License-Identifier: Apache-2.0 WITH Swift-exception
// Copyright (c) <#year#> <#copyright-holder#>

// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
  name: "swift-package-template",
  platforms: [.iOS(.v18), .macOS(.v15)],
  products: [
    // Products define the executables and libraries a package produces, making them visible to other packages.
    .library(
      name: "SwiftPackageTarget",
      targets: ["SwiftPackageTarget"])
  ],
  targets: [
    // Targets are the basic building blocks of a package, defining a module or a test suite.
    // Targets can depend on other targets in this package and products from dependencies.
    .target(
      name: "SwiftPackageTarget"),
    .testTarget(
      name: "SwiftPackageTargetTests",
      dependencies: ["SwiftPackageTarget"]),
  ]
)
