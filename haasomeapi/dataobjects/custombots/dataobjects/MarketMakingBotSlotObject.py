from datetime import datetime


class MarketMakingBotSlotObject:
    """ Data Object containing a Market Making Bot Slot Object

    :ivar orderId: str:
    :ivar price: float:
    :ivar tempAmount: float:
    :ivar timeStamp: :class:`~datettime`:
    :ivar locked: bool:
    """

    orderId: str
    price: float
    tempAmount: float
    timeStamp: datetime
    locked: bool
