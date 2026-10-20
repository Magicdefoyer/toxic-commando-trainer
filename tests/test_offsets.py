from cheat_core.offsets import OffsetTable


def test_known_build_returns_table():
    table = OffsetTable.for_build("1.2.7")
    assert table.player_pawn == 0x0A81C3F0
    assert table.build == "1.2.7"


def test_unknown_build_raises():
    import pytest

    with pytest.raises(KeyError):
        OffsetTable.for_build("0.0.0")