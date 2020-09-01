from __future__ import annotations

import json
import pickle
from datetime import date, datetime
from pathlib import Path
from typing import Any, Mapping, Optional, Sequence, Union

import tomlkit


class Toml:
    """
    A thin wrapper around a nested dict to make getting values easier.
    Keys must not contain dots (.), which are reserved for splitting of values.
    This class is especially useful for TOML but also works well for JSON and Python dicts.
    Also see ``toml_data``. This has some advantages.
    """

    @classmethod
    def read_toml(cls, path: Union[Path, str]) -> Toml:
        return Toml(tomlkit.loads(Path(path).read_text(encoding="utf8")))

    def __init__(self, x: Mapping[str, Any]) -> None:
        self._x = x

    def sub(self, items: str) -> Toml:
        return Toml(self.get(items, {}))

    def date(self, items: str, default: Optional[bool] = None) -> Optional[date]:
        return self._get_date(self.get(items, default))

    def datetime(self, items: str, default: Optional[bool] = None) -> Optional[datetime]:
        return self._get_datetime(self.get(items, default))

    def bool(self, items: str, default: Optional[bool] = None) -> Optional[bool]:
        return bool(self.get(items, default))

    def int(self, items: str, default: Optional[int] = None) -> Optional[int]:
        return int(self.get(items, default))

    def float(self, items: str, default: Optional[float] = None) -> Optional[float]:
        return float(self.get(items, default))

    def str(self, items: str, default: Optional[str] = None) -> Optional[str]:
        return self.get(items, default)

    def path(self, items: str, default: Optional[Path] = None) -> Optional[Path]:
        return Path(self.get(items, default))

    def list(self, items: str) -> list:
        return self.get(items, [])

    def date_list(self, items: str) -> Sequence[str]:
        return [self._get_date(s) for s in self.get(items, [])]

    def datetime_list(self, items: str) -> Sequence[str]:
        return [self._get_datetime(s) for s in self.get(items, [])]

    def str_list(self, items: str) -> Sequence[str]:
        return [str(s) for s in self.get(items, [])]

    def int_list(self, items: str) -> Sequence[int]:
        return [int(s) for s in self.get(items, [])]

    def float_list(self, items: str) -> Sequence[int]:
        return [float(s) for s in self.get(items, [])]

    def get(self, items: str, default=None):
        at = self._x
        for item in items.split("."):
            at = at[item]
        return self._x.get(items, default)

    def __getitem__(self, items: str):
        at = self._x
        for item in items.split("."):
            at = at[item]
        return at

    def items(self) -> Mapping[str, Any]:
        return dict(self._x)

    def keys(self) -> Sequence[str]:
        return list(self._x.keys())

    def values(self) -> Sequence[Any]:
        return list(self._x.values())

    def __repr__(self):
        return str(self._x)

    def __str__(self):
        return str(self._x)

    def __eq__(self, other):
        return str(self) == str(other)

    def _get_date(self, s):
        if isinstance(s, date):
            return s
        elif isinstance(s, str):
            return tomlkit.date(s)
        else:
            raise TypeError(f"Invalid type ${type(s)} for {s}")

    def _get_datetime(self, s):
        if isinstance(s, datetime):
            return s
        elif isinstance(s, str):
            return tomlkit.datetime(s)
        else:
            raise TypeError(f"Invalid type ${type(s)} for {s}")


__all__ = ["Toml"]
