from datetime import datetime

from haasomeapi.enums.EnumTradeType import EnumTradeType


class Trade:
    """ Data Object containing trade information
    
    :ivar timeStamp: :class:`~datetime`:
    :ivar unixTimeStamp: int:
    :ivar tradeType: :class:`~haasomeapi.enums.EnumTradeType`:
    :ivar price: float:
    :ivar amount: float:
    """

    timeStamp: datetime
    unixTimeStamp: int

    tradeType: EnumTradeType
    price: float
    amount: float
