from __future__ import annotations

import argparse
from pathlib import Path

from genri_demo.config import DemoConfig
from genri_demo.pipeline import render_demo


def parse_resolution(value: str) -> tuple[int, int]:
    try:
        width, height = value.lower().split("x", 1)
        return int(width), int(height)
    except Exception as exc:
        raise argparse.ArgumentTypeError("resolution must look like 720x1280") from exc


def main() -> int:
    parser = argparse.ArgumentParser(
        description="GenRI public demo: generate a short vertical video with deterministic scene transitions."
    )
    parser.add_argument("--output", default="results/genri_demo.mp4", help="output MP4 path")
    parser.add_argument("--resolution", type=parse_resolution, default=(720, 1280), help="WIDTHxHEIGHT")
    parser.add_argument("--scene-duration", type=float, default=1.8)
    parser.add_argument("--transition-duration", type=float, default=0.35)
    parser.add_argument("--scenes", type=int, default=4)
    args = parser.parse_args()

    width, height = args.resolution
    cfg = DemoConfig(
        width=width,
        height=height,
        scene_duration=args.scene_duration,
        transition_duration=args.transition_duration,
        scene_count=args.scenes,
    ).validate()

    out = render_demo(Path(args.output), cfg)
    print(f"Created: {out}")
    print(f"Duration: {cfg.total_duration:.2f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
