"""Static offset table keyed by game build."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OffsetTable:
    build: str
    player_pawn: int
    entity_list: int
    entity_count: int
    ammo_pool: int

    @classmethod
    def for_build(cls, build: str) -> "OffsetTable":
        table = _TABLES.get(build)
        if table is None:
            raise KeyError(f"no offsets registered for build {build!r}")
        return table


_TABLES: dict[str, OffsetTable] = {
    "1.2.7": OffsetTable(
        build="1.2.7",
        player_pawn=0x0A81C3F0,
        entity_list=0x0B12D4A8,
        entity_count=0x0B12D4B0,
        ammo_pool=0x0A81C4C8,
    ),
    "1.2.6": OffsetTable(
        build="1.2.6",
        player_pawn=0x0A7F1B20,
        entity_list=0x0B0F22D8,
        entity_count=0x0B0F22E0,
        ammo_pool=0x0A7F1BF8,
    ),
}