# SPDX-License-Identifier: Apache-2.0 WITH Swift-exception
# Copyright (c) 2026 Xudong Xu

from datetime import date
import json
from pathlib import Path
import shutil
import struct
import subprocess
import tempfile
import unittest
import zlib

TEMPLATE = Path(__file__).resolve().parents[2]


def png_image():
    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))

    return (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", 1, 1, 8, 6, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(b"\x00\xff\x00\x00\xff"))
        + chunk(b"IEND", b"")
    )


class InstantiateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.directory = tempfile.TemporaryDirectory()
        root = Path(cls.directory.name)
        cls.template = root / "template"
        tracked = subprocess.check_output(["git", "-C", str(TEMPLATE), "ls-files", "-z"]).decode().split("\0")
        for name in filter(None, tracked):
            source = TEMPLATE / name
            if source.is_file():
                destination = cls.template / name
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, destination)
        cls.image = png_image()
        (cls.template / "Documentation/Assets/Icon.png").write_bytes(cls.image)
        subprocess.check_call(["git", "-C", str(cls.template), "init", "-q"])
        cls.package = root / "swift-fixture"
        subprocess.check_call(
            [
                str(cls.template / "Scripts/instantiate"), "--output", str(cls.package),
                "--package", "swift-fixture", "--target", "Fixture",
                "--repository", "fixture/swift-fixture", "--copyright", "Fixture Author",
            ],
            stdout=subprocess.DEVNULL,
        )

    @classmethod
    def tearDownClass(cls):
        cls.directory.cleanup()

    def generated_text_files(self):
        for path in sorted(self.package.rglob("*")):
            if path.is_file() and ".build" not in path.relative_to(self.package).parts:
                try:
                    yield path, path.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    continue

    def test_binary_files_are_copied_byte_for_byte(self):
        self.assertEqual((self.package / "Documentation/Assets/Icon.png").read_bytes(), self.image)

    def test_template_identity_does_not_remain(self):
        for path, text in self.generated_text_files():
            for residue in ("check-template", "swift-package-template", "Xudong Xu", "showxdxu@"):
                self.assertNotIn(residue, text, str(path.relative_to(self.package)))
        self.assertFalse((self.package / "Scripts/instantiate").exists())
        self.assertFalse((self.package / "Tests/ReleaseTools/test_instantiate.py").exists())

    def test_release_configuration_uses_the_package_check(self):
        config = json.loads((self.package / ".github/release.json").read_text())
        self.assertEqual(config["repository"], "fixture/swift-fixture")
        self.assertEqual(config["check_command"], "Scripts/check")
        for entry in config["ci"]["include"]:
            self.assertTrue(entry.get("command", "Scripts/check").startswith("Scripts/check"), entry)

    def test_banners_carry_the_package_copyright(self):
        banner = "Copyright (c) " + str(date.today().year) + " Fixture Author"
        for name in (
            "Package.swift",
            "Sources/Fixture/Fixture.swift",
            "Tests/FixtureTests/FixtureTests.swift",
            "Scripts/check",
            "Scripts/validate-version",
            "Tests/ReleaseTools/test_version.py",
            "NOTICE",
        ):
            self.assertIn(banner, (self.package / name).read_text(), name)

    def test_generated_package_starts_at_its_first_version(self):
        self.assertEqual((self.package / "VERSION").read_text(), "0.1.0\n")
        self.assertIn("## 0.1.0\n", (self.package / "CHANGELOG.md").read_text())

    def test_generated_package_builds_and_tests(self):
        subprocess.check_call(["swift", "build"], cwd=self.package)
        subprocess.check_call(["swift", "test"], cwd=self.package)


if __name__ == "__main__":
    unittest.main()
