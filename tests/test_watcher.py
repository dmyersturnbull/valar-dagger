import random
import string
import time

import pytest

from valardagger.watcher import Watcher, EventHandler

from . import new_tmp_dir


class TestWatcher:
    def test_run_1(self):
        self._run_run(n=1)

    def test_run_0(self):
        self._run_run(n=0)

    def _run_run(self, n: int, interval_s: int = 1):
        with new_tmp_dir() as tmpdir:
            with Watcher(tmpdir, poll_interval_secs=interval_s) as watcher:
                path = watcher.path / "testit" / ".upload-complete"
                path.parent.mkdir(parents=True, exist_ok=True)
                for i, h in enumerate([self._rand_hash() for _ in range(n)]):
                    assert len(watcher.finished) == i
                    path.touch()
                    time.sleep(2 * interval_s)
                    assert len(watcher.finished) == i + 1
            assert len(watcher.finished) == n

    def _rand_hash(self) -> str:
        return "".join(random.choices(string.ascii_lowercase + string.digits, k=12))


if __name__ == "__main__":
    pytest.main()
