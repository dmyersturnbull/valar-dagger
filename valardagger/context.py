import os
from pathlib import Path

import valarpy
from valardagger.toml import Toml


class Context:
    def __init__(self):
        path = os.environ.get("VALARDAGGER_CONFIG", Path("/etc", "valardagger.toml"))
        self.config = Toml.read_toml(path)
        self.valar = valarpy.Valar()
        self.model = None

    def __enter__(self):
        self.valar.open()
        self.model = valarpy.new_model()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.valar.close()

    @classmethod
    def archive_path(cls, subission_hash: str) -> Path:
        pass
