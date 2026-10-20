"""Qt-based transparent overlay window that draws ESP boxes."""
from __future__ import annotations

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QWidget


class OverlayWindow(QWidget):
    def __init__(self, container) -> None:
        super().__init__()
        self._container = container
        self.setWindowTitle("Toxic Commando Trainer")
        self.setWindowFlags(
            Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self._boxes: list[tuple[int, int, int, int]] = []

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)
        self._timer.start(1000 // max(15, container.config_service._config.overlay_fps))

    def set_boxes(self, boxes: list[tuple[int, int, int, int]]) -> None:
        self._boxes = boxes
        self.update()

    def _tick(self) -> None:
        # Snapshot entity positions from the cheat service and rebuild boxes.
        self.update()

    def paintEvent(self, event) -> None:  # noqa: N802 (Qt naming)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, False)
        pen = QPen(QColor(120, 255, 60, 200))
        pen.setWidth(1)
        painter.setPen(pen)
        for x, y, w, h in self._boxes:
            painter.drawRect(x, y, w, h)
        painter.end()