# GenRI — short-form video generation project

GenRI is a local desktop project for automated generation of short-form video. The production application combines source media, transitions/effects, subtitles, audio and output validation in a single generation workflow.

This public repository is a **safe demonstration edition**. It contains runnable code, tests and architecture documentation, while the production generation core and private assets remain outside the public repository.

## What the public demo does

The demo creates a deterministic vertical MP4 from synthetic scenes and joins them with FFmpeg transitions. It is intentionally small, but it is fully runnable and demonstrates:

- Python → FFmpeg orchestration;
- vertical-video configuration;
- deterministic scene sequencing;
- transition graph construction;
- input validation;
- automated unit tests;
- reproducible output generation.

## Requirements

- Python 3.10+
- FFmpeg available in `PATH`

No third-party Python packages are required for the public demo.

## Run

```bash
python main.py
```

The default result is written to:

```text
results/genri_demo.mp4
```

Custom example:

```bash
python main.py --resolution 720x1280 --scenes 5 --scene-duration 1.6 --transition-duration 0.3
```

## Tests

```bash
python -m unittest discover -s tests -v
```

## Production project

The production GenRI application includes a desktop GUI and a broader processing pipeline for media preparation, short-form video assembly, transitions/effects, subtitles, audio handling, export and automated output checks.

The production source code, private generation logic, media assets and internal presets are intentionally not published here.

See [`docs/architecture.md`](docs/architecture.md) for the public architecture overview.

## Demonstration frame

A frame captured from a verified local run is included at [`docs/demo_frame.png`](docs/demo_frame.png). Machine-readable FFprobe metadata from that run is included in [`results/demo_metadata.json`](results/demo_metadata.json).

A small verified MP4 produced by the public demo is included at [`docs/genri_demo.mp4`](docs/genri_demo.mp4).
