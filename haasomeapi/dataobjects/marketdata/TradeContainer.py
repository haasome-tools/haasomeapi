from typing import List
from datetime import datetime

from haasomeapi.dataobjects.marketdata.Trade import Trade


class TradeContainer:
    """ Data object containing Trades
    
    :ivar timeStamp: :class:`~datetime`:
    :ivar unixTimeStamp: int:
    :ivar lastTrades: List[`~haasomeapi.dataobjects.marketdata.Trade`]:
    """

    timeStamp: datetime
    unixTimeStamp: int

    lastTrades: List[Trade]
