from typing import List
from datetime import datetime

from haasomeapi.dataobjects.marketdata.Trade import Trade


class TradeContainer:
    timeStamp: datetime
    unixTimeStamp: int

    lastTrades: List[Trade]
