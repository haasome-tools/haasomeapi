from enum import Enum

class EnumSafetyPositionSignal(Enum):
    ANY = 0
    BUY_LONG = 1
    SELL_SHORT = 2
    NO_POSITION = 3
