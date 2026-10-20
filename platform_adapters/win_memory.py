"""Thin wrapper around pymem for the Windows target process."""
from __future__ import annotations

import struct


class WinMemoryAdapter:
    def __init__(self, process_name: str) -> None:
        self._process_name = process_name
        self._pm = None
        self._pid: int | None = None

    @property
    def pid(self) -> int | None:
        return self._pid

    def open(self, name: str) -> None:
        import pymem  # local import so tests can stub this module

        self._pm = pymem.Pymem(name)
        self._pid = self._pm.process_id

    def close(self) -> None:
        if self._pm is not None:
            try:
                self._pm.close_process()
            finally:
                self._pm = None
                self._pid = None

    def read_int(self, address: int) -> int:
        assert self._pm is not None, "process not attached"
        return self._pm.read_int(address)

    def write_int(self, address: int, value: int) -> None:
        assert self._pm is not None, "process not attached"
        self._pm.write_int(address, value)

    def read_ptr(self, address: int) -> int:
        assert self._pm is not None, "process not attached"
        return struct.unpack("<Q", self._pm.read_bytes(address, 8))[0]

    def resolve_pointer(self, base: int, chain: list[int]) -> int:
        addr = base
        for offset in chain:
            addr = self.read_ptr(addr) + offset
        return addr