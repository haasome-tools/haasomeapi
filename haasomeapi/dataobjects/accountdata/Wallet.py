from typing import Dict

from haasomeapi.dataobjects.accountdata.Position import Position


class Wallet:
    """    
    Data Object containing the Wallet

    :ivar coins: Dict[str, float]: Coins in wallet 
    :ivar positions: Dict[str, :class:`~haasomeapi.dataobjects.accountdata.Position`]: Active Positions
    """
    
    coins: Dict[str, float]
    positions: Dict[str, Position]
