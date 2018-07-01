from datetime import datetime


class PriceTick:
    timeStamp: datetime
    unixTimeStamp: int

    open: float
    highValue: float
    lowValue: float
    close: float
    volume: float

    currentBuyValue: float
    currentSellValue: float
