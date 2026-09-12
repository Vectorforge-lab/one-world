from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from .config import DemoConfig

# Deliberately simple public palette. The production project uses a different,
# private generation pipeline that is not part of this repository.
SCENE_COLORS = ("0x101820", "0x0057B8", "0x00A878", "0xF4B400", "0x7B2CBF", "0xD7263D")


def ffmpeg_available() -> bool:
    return shutil.which("ffmpeg") is not None


def build_filter_graph(cfg: DemoConfig) -> tuple[list[str], str]:
    """Return lavfi inputs and an xfade filter graph for a synthetic vertical demo."""
    cfg.validate()

    inputs: list[str] = []
    for idx in range(cfg.scene_count):
        color = SCENE_COLORS[idx % len(SCENE_COLORS)]
        source = f"color=c={color}:s={cfg.width}x{cfg.height}:r={cfg.fps}:d={cfg.scene_duration:.3f}"
        inputs += ["-f", "lavfi", "-i", source]

    if cfg.transition_duration == 0:
        # concat is used if transitions are disabled
        streams = "".join(f"[{i}:v]" for i in range(cfg.scene_count))
        graph = f"{streams}concat=n={cfg.scene_count}:v=1:a=0[vout]"
        return inputs, graph

    parts: list[str] = []
    previous = "[0:v]"
    for i in range(1, cfg.scene_count):
        out = f"[v{i}]"
        offset = i * (cfg.scene_duration - cfg.transition_duration)
        parts.append(
            f"{previous}[{i}:v]xfade=transition=fade:duration={cfg.transition_duration:.3f}:offset={offset:.3f}{out}"
        )
        previous = out

    parts.append(f"{previous}format=yuv420p[vout]")
    return inputs, ";".join(parts)


def render_demo(output_path: Path, cfg: DemoConfig) -> Path:
    cfg.validate()
    if not ffmpeg_available():
        raise RuntimeError("FFmpeg was not found in PATH")

    output_path = output_path.resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    inputs, graph = build_filter_graph(cfg)
    cmd = [
        "ffmpeg",
        "-y",
        "-hide_banner",
        "-loglevel",
        "error",
        *inputs,
        "-filter_complex",
        graph,
        "-map",
        "[vout]",
        "-r",
        str(cfg.fps),
        "-c:v",
        "libx264",
        "-preset",
        "veryfast",
        "-crf",
        "23",
        "-movflags",
        "+faststart",
        str(output_path),
    ]
    subprocess.run(cmd, check=True)
    return output_path
