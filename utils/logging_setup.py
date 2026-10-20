"""Shared logging bootstrap for the trainer."""
from __future__ import annotations

import logging
from pathlib import Path


def setup(level: int = logging.INFO) -> None:
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.FileHandler(log_dir / "trainer.log", encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )