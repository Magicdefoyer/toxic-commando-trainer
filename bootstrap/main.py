"""Entry point — wires services together and starts the overlay."""
from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from bootstrap.wiring import build_container
from overlay_core.overlay_window import OverlayWindow


def main() -> int:
    app = QApplication(sys.argv)
    container = build_container()

    # Attempt to attach to the running game process before showing UI.
    attached = container.process_service.attach()
    if not attached:
        print("[trainer] John Carpenter's Toxic Commando not found — running in idle mode")

    window = OverlayWindow(container)
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())