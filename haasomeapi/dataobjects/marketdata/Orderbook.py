from typing import List
from datetime import datetime


from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.dataobjects.marketdata.OrderbookRecord import OrderbookRecord


class Orderbook:
    timeStamp: datetime
    unixLastUpdate: int

    priceMarket: Market
    bid: List[OrderbookRecord]
    ask: List[OrderbookRecord]
