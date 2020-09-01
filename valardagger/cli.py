"""
Command-line interface for valar-dagger.
"""

from __future__ import annotations

import logging
from pathlib import Path

import typer

from valardagger.watcher import Watcher


logger = logging.getLogger(__package__)
cli = typer.Typer()


@cli.command()
def start(path: Path) -> None:
    """
    Starts the scheduler.
    """
    with Watcher(path):
        logger.info(f"Started watching at {path}")


if __name__ == "__main__":
    cli()
