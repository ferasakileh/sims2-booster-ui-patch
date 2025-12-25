"""Tests for user-facing option presets (scale/filter labels)."""

import unittest


class PresetsTest(unittest.TestCase):
    """Ensure GUI/CLI preset labels are wired correctly."""

    def test_1080p_medium_preset_exists(self):
        """The 1080p-friendly preset is present and maps to 1.35x."""
        # Importing the GUI module is safe here; we only read its constants.
        from sims2_4k_ui_patcher import LABELS_UI_SCALE  # pylint: disable=import-outside-toplevel

        # Be resilient to minor label text changes: look for any 1080p/FHD preset at 1.35.
        matches = [k for k, v in LABELS_UI_SCALE.items() if v == 1.35 and ("1080p" in k or "FHD" in k)]
        self.assertTrue(matches, "Missing 1080p-friendly (1.35x) scale preset in LABELS_UI_SCALE")
