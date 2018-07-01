from datetime import datetime

from haasomeapi.enums.EnumFundPosition import EnumFundPosition
from haasomeapi.enums.EnumBotTradeResult import EnumBotTradeResult


class TradeBotSignals:
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
