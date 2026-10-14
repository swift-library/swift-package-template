# SPDX-License-Identifier: Apache-2.0 WITH Swift-exception
# Copyright (c) 2026 Xudong Xu

from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]


def check_callers(test, root):
    workflows = root / '.github/workflows'
    ci = (workflows / 'ci.yml').read_text()
    policy = (workflows / 'source-policy.yml').read_text()
    release = (workflows / 'release.yml').read_text()
    for workflow, expected in ((ci, {'opened', 'synchronize', 'reopened'}),
                               (policy, {'opened', 'synchronize', 'reopened', 'edited'})):
        events = re.search(r'types: \[([^\]]+)\]', workflow)[1]
        test.assertEqual({event.strip() for event in events.split(',')}, expected)
        test.assertIn('branches: [master]', workflow)
        test.assertIn('group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}', workflow)
        test.assertIn('cancel-in-progress: true', workflow)
    test.assertNotIn('  policy:', ci)
    test.assertIn('  validate:\n    uses: swift-library/.github/.github/workflows/swift-package-ci.yml@', ci)
    test.assertNotIn('    if:', ci)
    test.assertIn('  policy:\n    uses: swift-library/.github/.github/workflows/policy.yml@', policy)
    test.assertNotIn('  validate:', policy)
    test.assertNotIn('concurrency:', release)
    test.assertIn('    needs: validate', release)
    pins = re.findall(r'swift-library/.github/.github/workflows/[a-z-]+\.yml@([0-9a-f]{40})', ci + policy + release)
    test.assertEqual(len(pins), 4)
    test.assertEqual(len(set(pins)), 1)


class WorkflowTests(unittest.TestCase):
    def test_caller_contract(self):
        check_callers(self, ROOT)


if __name__ == '__main__':
    unittest.main()
