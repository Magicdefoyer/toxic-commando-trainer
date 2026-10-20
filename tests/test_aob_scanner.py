from cheat_core.aob_scanner import Pattern, find_pattern


def test_find_pattern_exact():
    buf = b"\x00\x11\x22\x33\x44\x55"
    sig = Pattern("test", b"\x22\x33\x44", b"\xFF\xFF\xFF")
    hits = find_pattern(buf, sig)
    assert hits == [2]


def test_find_pattern_wildcard():
    buf = b"\xAA\xBB\xCC\xDD"
    sig = Pattern("w", b"\xAA\x00\xCC", b"\xFF\x00\xFF")
    assert find_pattern(buf, sig) == [0]