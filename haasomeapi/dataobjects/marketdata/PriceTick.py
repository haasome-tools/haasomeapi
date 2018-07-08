from datetime import datetime


class PriceTick:
    """ Data Object containing Price Tick information

    :ivar timeStamp: datetime:
    :ivar unixTimeStamp: int:
    :ivar open: float:
    :ivar highValue: float:
    :ivar lowValue: float:
    :ivar close: float:
    :ivar volume: float:
    :ivar currentBuyValue: float:
    :ivar currentSellValue: float:
    """

    timeStamp: datetime
    unixTimeStamp: int

    open: float
    highValue: float
    lowValue: float
    close: float
    volume: float

    currentBuyValue: float
    currentSellValue: float
