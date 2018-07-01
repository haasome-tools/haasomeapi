from typing import Dict

from haasomeapi.dataobjects.accountdata.Position import Position


class Wallet:
    coins: Dict[str, float]
    positions: Dict[str, Position]
