from typing import NamedTuple
from enum import Enum


class Move(NamedTuple):
    row: int
    col: int


class Symbol(Enum):
    X = "X"
    O = "O"
    EMPTY = " "
