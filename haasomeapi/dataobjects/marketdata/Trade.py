from datetime import datetime

from haasomeapi.enums.EnumTradeType import EnumTradeType


class Trade:
    timeStamp: datetime
    unixTimeStamp: int

    tradeType: EnumTradeType
    price: float
    amount: float
