import enum
from enum import Enum

class SavingThrow(Enum):
    Fortitude = enum.auto()
    Reflex = enum.auto()
    Will = enum.auto()

# Values to test main.py
Fortitude = 3
Reflex = 2
Will = 1