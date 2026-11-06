"""The build-launcher workflow must pin Android SDK packages for setup-android.

The workflow used to rely on setup-android defaults, which attempted to install the legacy
`tools` package and failed with "Failed to find package 'tools'". This guard keeps the workflow
on explicit package inputs.
"""
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/build-launcher.yml"


class BuildLauncherWorkflowAndroidPackagesTest(unittest.TestCase):
    def test_setup_android_uses_explicit_packages(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertRegex(
            text,
            re.compile(
                r"- uses: android-actions/setup-android@v3\s+with:\s+packages: "
                r"platforms;android-34 build-tools;34\.0\.0"
            ),
            "build-launcher workflow must pin setup-android packages to platform 34 and build-tools 34.0.0",
        )


if __name__ == "__main__":
    unittest.main()
