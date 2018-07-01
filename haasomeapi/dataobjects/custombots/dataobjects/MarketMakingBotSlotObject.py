from datetime import datetime


class MarketMakingBotSlotObject:
    orderId: str
    price: float
    tempAmount: float
    timeStamp: datetime
    locked: bool
