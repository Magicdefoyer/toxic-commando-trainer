"""Array-of-bytes pattern scanner — used to re-derive offsets after patches."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Pattern:
    name: str
    signature: bytes
    mask: bytes  # 0xFF = must match, 0x00 = wildcard

    def __len__(self) -> int:
        return len(self.signature)


def find_pattern(buffer: bytes, pattern: Pattern) -> list[int]:
    hits: list[int] = []
    n = len(pattern)
    if n == 0 or n > len(buffer):
        return hits
    for i in range(len(buffer) - n + 1):
        ok = True
        for j in range(n):
            if pattern.mask[j] and buffer[i + j] != pattern.signature[j]:
                ok = False
                break
        if ok:
            hits.append(i)
    return hits