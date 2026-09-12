# GenRI architecture overview

GenRI is a local desktop application for building short-form videos from media, audio, subtitle and visual-style inputs.

The production application is organized as a pipeline with the following high-level responsibilities:

1. **Desktop UI and configuration** — project settings, format selection and generation controls.
2. **Media preparation** — inspection and normalization of source assets.
3. **Video assembly** — construction of a short-form sequence from selected media.
4. **Transitions and visual processing** — transition/effect application and format adaptation.
5. **Subtitle stage** — subtitle preparation and rendering.
6. **Audio stage** — voice/music handling and final muxing.
7. **Output validation** — automated checks on generated output and diagnostic logging.
8. **Export** — final MP4 creation and run artifacts.

## Public repository boundary

This repository intentionally contains only a small, independently implemented demonstration pipeline. It proves the development setup, FFmpeg integration, configuration validation, deterministic execution and automated tests without exposing the production generation logic.

The production implementation, private presets, media assets and internal quality-control logic are not included in this public repository.
