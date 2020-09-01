import time

import pytest

from valardagger.watcher import Watcher, EventHandler

from . import new_tmp_dir


class TestWatcher:
    def test_run(self):
        with new_tmp_dir() as tmpdir:
            with Watcher(tmpdir) as watcher:
                path = watcher.path/"testit"/".upload-complete"
                path.parent.mkdir(parents=True)
                path.touch()
                time.sleep(1)
                assert len(watcher.finished) == 1


if __name__ == "__main__":
    pytest.main()
