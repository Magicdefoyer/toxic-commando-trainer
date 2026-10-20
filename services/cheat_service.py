"""High-level cheat operations — thin, delegates to memory + offsets."""
from __future__ import annotations

from cheat_core.offsets import OffsetTable
from platform_adapters.win_memory import WinMemoryAdapter


class CheatService:
    def __init__(self, memory: WinMemoryAdapter, offsets: OffsetTable) -> None:
        self._memory = memory
        self._offsets = offsets
        self._godmode = False
        self._esp = False

    def set_godmode(self, enabled: bool) -> None:
        # Writes the health-lock flag in the player pawn struct.
        addr = self._memory.resolve_pointer(self._offsets.player_pawn, [0x38, 0x2A0])
        self._memory.write_int(addr, 1 if enabled else 0)
        self._godmode = enabled

    def set_esp(self, enabled: bool) -> None:
        self._esp = enabled
        # ESP is read-only — the overlay renders boxes from tracked entities.

    def is_godmode(self) -> bool:
        return self._godmode

    def is_esp_enabled(self) -> bool:
        return self._esp