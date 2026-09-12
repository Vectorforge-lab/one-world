import unittest

from genri_demo.config import DemoConfig
from genri_demo.pipeline import build_filter_graph


class PipelineTests(unittest.TestCase):
    def test_filter_graph_contains_expected_xfades(self):
        cfg = DemoConfig(scene_count=4)
        inputs, graph = build_filter_graph(cfg)
        self.assertEqual(inputs.count("-i"), 4)
        self.assertEqual(graph.count("xfade="), 3)
        self.assertIn("[vout]", graph)

    def test_zero_transition_uses_concat(self):
        cfg = DemoConfig(scene_count=3, transition_duration=0)
        _, graph = build_filter_graph(cfg)
        self.assertIn("concat=n=3", graph)


if __name__ == "__main__":
    unittest.main()
