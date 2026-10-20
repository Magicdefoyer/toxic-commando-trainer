# Security Policy

## Scope
This project is an offline trainer for **John Carpenter's Toxic Commando**. Attack surface considered:

- The overlay injector (`overlay-core/injector.py`)
- The memory reader/writer adapter (`platform-adapters/win_memory.py`)
- The remote config loader (`services/config_service.py`)

## Reporting
If you find a vulnerability (e.g. arbitrary code execution via a crafted config file, or an overlay injection path that could be hijacked), open a private security advisory or email the maintainers listed in `pyproject.toml`.

Do **not** open public issues for exploit-class bugs.

## Anti-cheat note
This tool is intended for **single-player / offline sessions only**. Using it online is against the game's ToS and is not supported. Do not file security reports about "getting banned" — that is expected behavior.