# Offset Reference

All offsets in `cheat_core/offsets.py` are verified against specific game builds
of **John Carpenter's Toxic Commando**.

| Build  | PlayerPawn  | EntityList  | EntityCount | AmmoPool    |
|--------|-------------|-------------|-------------|-------------|
| 1.2.7  | 0x0A81C3F0  | 0x0B12D4A8  | 0x0B12D4B0  | 0x0A81C4C8  |
| 1.2.6  | 0x0A7F1B20  | 0x0B0F22D8  | 0x0B0F22E0  | 0x0A7F1BF8  |

## Re-deriving after a patch
1. Dump the `.text` section from the shipping exe.
2. Run `cheat_core/aob_scanner.py` against the dump with the saved signatures in `docs/signatures/`.
3. Update the pointer chain in `cheat_core/offsets.py` and bump `game_build` in `config/trainer.default.json`.