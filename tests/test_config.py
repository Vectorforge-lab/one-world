import unittest

from genri_demo.config import DemoConfig


class DemoConfigTests(unittest.TestCase):
    def test_total_duration_accounts_for_overlap(self):
        cfg = DemoConfig(scene_count=4, scene_duration=2.0, transition_duration=0.5)
        self.assertAlmostEqual(cfg.total_duration, 6.5)

    def test_rejects_transition_longer_than_scene(self):
        with self.assertRaises(ValueError):
            DemoConfig(scene_duration=1.0, transition_duration=1.0).validate()

    def test_requires_at_least_two_scenes(self):
        with self.assertRaises(ValueError):
            DemoConfig(scene_count=1).validate()


if __name__ == "__main__":
    unittest.main()
