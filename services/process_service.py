"""Attach / detach lifecycle for the game process."""
from __future__ import annotations

import logging

from platform_adapters.win_memory import WinMemoryAdapter

log = logging.getLogger(__name__)


class ProcessService:
    def __init__(self, memory: WinMemoryAdapter, expected_name: str) -> None:
        self._memory = memory
        self._expected_name = expected_name
        self._attached = False

    @property
    def attached(self) -> bool:
        return self._attached

    def attach(self) -> bool:
        try:
            self._memory.open(self._expected_name)
            self._attached = True
            log.info("attached to %s (pid=%s)", self._expected_name, self._memory.pid)
            return True
        except Exception as exc:  # noqa: BLE001
            log.warning("attach failed: %s", exc)
            self._attached = False
            return False

    def detach(self) -> None:
        if self._attached:
            self._memory.close()
            self._attached = False
            log.info("detached from game process")