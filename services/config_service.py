"""Loads trainer config (hotkeys, feature toggles, process name)."""
from __future__ import annotations

import json
from pathlib import Path

from pydantic import BaseModel, Field


class TrainerConfig(BaseModel):
    process_name: str = "ToxicCommando-Win64-Shipping.exe"
    game_build: str = "1.2.7"
    toggle_key: str = "INSERT"
    aimbot_key: str = "VK_XBUTTON2"
    esp_enabled_default: bool = False
    godmode_enabled_default: bool = False
    overlay_fps: int = Field(default=60, ge=15, le=240)


class ConfigService:
    def __init__(self, config: TrainerConfig, path: Path | None = None) -> None:
        self._config = config
        self._path = path

    @property
    def process_name(self) -> str:
        return self._config.process_name

    @property
    def game_build(self) -> str:
        return self._config.game_build

    @classmethod
    def load_default(cls) -> "ConfigService":
        path = Path("config/trainer.default.json")
        if path.exists():
            data = json.loads(path.read_text(encoding="utf-8"))
            return cls(TrainerConfig(**data), path)
        return cls(TrainerConfig())