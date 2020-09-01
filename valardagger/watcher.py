from __future__ import annotations
import logging
from typing import Sequence
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler, FileSystemEvent


logger = logging.getLogger(__package__)


class EventHandler(PatternMatchingEventHandler):
    def __init__(self, glob: str, max_simultaneous: int):
        super().__init__(patterns=glob, case_sensitive=True)
        self._max_simultaneous = max_simultaneous
        self._waiting = []
        self._active = []
        self._finished = []

    def on_created(self, event: FileSystemEvent):
        path = Path(event.src_path)
        if path.name == ".upload-complete":
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
    def __init__(self, path: Path):
        self.path = path
        self.glob = f"{path}/*/.upload-complete"
        self._handler = EventHandler(self.glob, 2)
        self._observer = Observer()
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
