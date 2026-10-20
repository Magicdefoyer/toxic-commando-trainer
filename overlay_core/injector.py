"""Minimal overlay injector — currently spawns the Qt overlay as a child process."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def launch_overlay() -> subprocess.Popen:
    script = Path(__file__).with_name("overlay_window.py")
    return subprocess.Popen([sys.executable, "-m", "bootstrap.main"], close_fds=True)


def is_overlay_running(proc: subprocess.Popen | None) -> bool:
    return proc is not None and proc.poll() is None