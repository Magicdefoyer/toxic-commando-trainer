"""Windows virtual-key helpers used by the hotkey binder."""
from __future__ import annotations

_VK_NAMES = {
    "F1": 0x70,
    "F2": 0x71,
    "F3": 0x72,
    "F4": 0x73,
    "INSERT": 0x2D,
    "HOME": 0x24,
    "VK_XBUTTON2": 0x06,
}


def vk_code(name: str) -> int:
    key = name.upper()
    if key not in _VK_NAMES:
        raise ValueError(f"unknown virtual key: {name}")
    return _VK_NAMES[key]
</｜｜DSML｜｜ parameter>
</｜｜DSML｜｜ invoke>
</｜｜DSML｜｜ calls>