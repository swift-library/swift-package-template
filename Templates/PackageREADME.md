<div align="center">

<p align="center">
  <a href="https://github.com/{{repository}}"><img src="Documentation/Assets/Logo.svg" width="160" alt="{{package}} logo"></a>
</p>

<h1 align="center">{{package}}</h1>

<p align="center">
  Describe the outcome your library provides.
</p>

<p align="center">
  <a href="https://github.com/{{repository}}/actions/workflows/ci.yml"><img src="https://github.com/{{repository}}/actions/workflows/ci.yml/badge.svg?branch=master" alt="CI"></a>
  <img src="https://img.shields.io/badge/Swift-6.0%2B-F05138?style=flat" alt="Swift 6.0+">
  <img src="https://img.shields.io/badge/platforms-iOS%2015%2B%20%7C%20macOS%2012%2B-lightgrey?style=flat" alt="Platforms: iOS 15+ | macOS 12+">
  <a href="LICENSE.txt"><img src="https://img.shields.io/badge/license-Apache--2.0-blue?style=flat" alt="License: Apache-2.0 WITH Swift-exception"></a>
</p>

<p align="center">
  <a href="#overview">Overview</a> ·
  <a href="#quick-look">Quick look</a> ·
  <a href="#install">Install</a> ·
  <a href="#usage">Usage</a> ·
  <a href="#requirements">Requirements</a> ·
  <a href="#documentation">Documentation</a> ·
  <a href="#contributing">Contributing</a> ·
  <a href="#license">License</a>
</p>

</div>


## Overview

Add your library implementation in `Sources/{{target}}`. Explain the problem it solves and how it behaves, linking details and limits from Documentation.

## Quick look

```swift
import {{target}}
```

## Install

Add the package dependency and select the `{{target}}` product:

```swift
.package(url: "https://github.com/{{repository}}.git", branch: "master")
```

> [!NOTE]
> No tagged release is published yet. This requirement follows `master`;
> select a next-minor version requirement after the first release.

## Usage

Replace the Quick look with a working example of your public API. Put detailed examples in Documentation and link them here.

## Requirements

- Swift 6.0 or later
- iOS 15 or later, or macOS 12 or later

## Documentation

- [Release](Documentation/Reference/Release.md): release facts and mechanics; version rules are in VERSIONING.
- [Changelog](CHANGELOG.md)

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and run `Scripts/check` before submitting changes.

## License

Apache License 2.0 with the Swift Runtime Library Exception. See [LICENSE.txt](LICENSE.txt) and [NOTICE](NOTICE).
