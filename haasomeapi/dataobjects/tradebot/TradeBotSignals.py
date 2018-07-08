from datetime import datetime

from haasomeapi.enums.EnumFundPosition import EnumFundPosition
from haasomeapi.enums.EnumBotTradeResult import EnumBotTradeResult


class TradeBotSignals:
    """ Data Object containing a trade bot signals

    :ivar priceSourceConnected: bool:
    :ivar accountConnected: bool:
    :ivar tradeAmountOk: bool:
    :ivar openOrdersOk: bool:
    :ivar isBenchmark: bool:
    :ivar isSafetySignalNow: bool:
    :ivar maxLongAmount: float:
    :ivar maxNoPositionAmount: float:
    :ivar maxShortAmount: float:
    :ivar maxBuyAmount: float:
    :ivar maxSellAmount: float:
    :ivar botBuySellSignal: int = 50:
    :ivar botLongShortSignal: int = 50:
    :ivar lastPoolMoment: :class:`~datettime`:
    :ivar unixLastPoolMoment: int:
    :ivar buySellResult: :class:`~haasomeapi.enums.EnumBotTradeResult`:
    :ivar longShortResult: :class:`~haasomeapi.enums.EnumFundPosition`:
    """

    priceSourceConnected: bool

    accountConnected: bool
    tradeAmountOk: bool
    openOrdersOk: bool
    isBenchmark: bool
    isSafetySignalNow: bool

    maxLongAmount: float
    maxNoPositionAmount: float
    maxShortAmount: float

    maxBuyAmount: float
    maxSellAmount: float

    botBuySellSignal: int = 50
    botLongShortSignal: int = 50

    lastPoolMoment: datetime
    unixLastPoolMoment: int

    buySellResult: EnumBotTradeResult
    longShortResult: EnumFundPosition
