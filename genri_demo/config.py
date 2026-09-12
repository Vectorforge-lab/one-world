from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DemoConfig:
    width: int = 720
    height: int = 1280
    fps: int = 30
    scene_duration: float = 1.8
    transition_duration: float = 0.35
    scene_count: int = 4

    def validate(self) -> "DemoConfig":
        if self.width <= 0 or self.height <= 0:
            raise ValueError("width and height must be positive")
        if self.fps <= 0:
            raise ValueError("fps must be positive")
        if self.scene_count < 2:
            raise ValueError("scene_count must be at least 2")
        if self.scene_duration <= 0:
            raise ValueError("scene_duration must be positive")
        if not 0 <= self.transition_duration < self.scene_duration:
            raise ValueError("transition_duration must be >= 0 and smaller than scene_duration")
        return self

    @property
    def total_duration(self) -> float:
        # Every xfade overlaps two neighbouring scenes.
        return self.scene_count * self.scene_duration - (self.scene_count - 1) * self.transition_duration
