from __future__ import annotations
import typing

from src.containers import UserSet, UserDict, UserList

if typing.TYPE_CHECKING:
    from src.users import User
    from typing import FrozenSet, Tuple

__all__ = ["GameState"]

class PregameState:
    def __init__(self):
        pass

class GameState:
    def __init__(self):
        self._rolestats = set()

    def get_role_stats(self) -> FrozenSet[FrozenSet[Tuple[str, int]]]:
        return frozenset(self._rolestats)

    def set_role_stats(self, value) -> None:
        self._rolestats.clear()
        self._rolestats.update(value)

    def del_role_stats(self) -> None:
        self._rolestats.clear()

    ROLE_STATS = property(get_role_stats, set_role_stats, del_role_stats, "Manipulate and return the current valid role sets")


