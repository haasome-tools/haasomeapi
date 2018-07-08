from typing import List
from datetime import datetime


from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.dataobjects.marketdata.OrderbookRecord import OrderbookRecord


class Orderbook:
    """ Data Object containing the orderbook

    :ivar timeStamp: datetime:
    :ivar unixLastUpdate: int:
    :ivar priceMarket: :class:`~haasomeapi.dataobjects.marketdata.Market`:
    :ivar bid: List[:class:`~haasomeapi.dataobjects.marketdata.OrderbookRecord`]:
    :ivar ask: List[:class:`~haasomeapi.dataobjects.marketdata.OrderbookRecord`]:
    """

    timeStamp: datetime
    unixLastUpdate: int

    priceMarket: Market
    bid: List[OrderbookRecord]
    ask: List[OrderbookRecord]
