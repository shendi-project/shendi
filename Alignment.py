import enum
from enum import Enum

class Alignment(Enum):
    LawfulGood = enum.auto()
    NeutralGood = enum.auto()
    ChaoticGood = enum.auto()
    LawfulNeutral = enum.auto()
    TrueNeutral = enum.auto()
    ChaoticNeutral = enum.auto()
    LawfulEvil = enum.auto()
    NeutralEvil = enum.auto()
    ChaoticEvil = enum.auto()
