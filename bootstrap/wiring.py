"""Dependency wiring / container."""
from __future__ import annotations

from dataclasses import dataclass

from services.cheat_service import CheatService
from services.config_service import ConfigService
from services.process_service import ProcessService
from platform_adapters.win_memory import WinMemoryAdapter
from cheat_core.offsets import OffsetTable


@dataclass
class Container:
    config_service: ConfigService
    process_service: ProcessService
    memory: WinMemoryAdapter
    offsets: OffsetTable
    cheat_service: CheatService


def build_container() -> Container:
    config = ConfigService.load_default()
    memory = WinMemoryAdapter(process_name=config.process_name)
    offsets = OffsetTable.for_build(config.game_build)
    process = ProcessService(memory=memory, expected_name=config.process_name)
    cheats = CheatService(memory=memory, offsets=offsets)
    return Container(
        config_service=config,
        process_service=process,
        memory=memory,
        offsets=offsets,
        cheat_service=cheats,
    )