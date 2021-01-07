from __future__ import annotations
import logging
from typing import Sequence
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent


logger = logging.getLogger(__package__)


class EventHandler(FileSystemEventHandler):
    def __init__(self, filename: str, max_simultaneous: int):
        self._filename = filename
        self._max_simultaneous = max_simultaneous
        self._waiting = []
        self._active = []
        self._finished = []

    def on_created(self, event: FileSystemEvent):
        path = Path(event.src_path)
        if path.name == self._filename:
            # It's strange, but events get created twice
            if path in self._waiting or path in self._active or path in self._finished:
                return
            self._finished.append(path)
        logger.info(f"Found new upload at {path}")

    @property
    def waiting(self) -> Sequence[Path]:
        return self._waiting

    @property
    def active(self) -> Sequence[Path]:
        return self._active

    @property
    def finished(self) -> Sequence[Path]:
        return self._finished


class Watcher:
    def __init__(self, path: Path, max_simultaneous: int = 2, poll_interval_secs: int = 1):
        """

        Args:
            path: The spool directory
            max_simultaneous: The max number of jobs that can be processed simultaneously
            poll_interval_secs: The number of seconds to wait between polls; must be at least 1 s.
        """
        self.path = path
        self.filename = r".upload-complete"
        self._handler = EventHandler(self.filename, max_simultaneous=max_simultaneous)
        self._observer = Observer(timeout=poll_interval_secs)
        self._observer.schedule(self._handler, str(path), recursive=True)

    def __enter__(self):
        self._observer.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._observer.stop()
        self._observer.join(timeout=2)

    @property
    def waiting(self) -> Sequence[Path]:
        return self._handler.waiting

    @property
    def active(self) -> Sequence[Path]:
        return self._handler.active

    @property
    def finished(self) -> Sequence[Path]:
        return self._handler.finished


__all__ = ["EventHandler", "Watcher"]
