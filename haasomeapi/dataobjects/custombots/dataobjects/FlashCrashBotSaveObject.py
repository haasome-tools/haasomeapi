from haasomeapi.dataobjects.marketdata.Market import Market

from haasomeapi.enums.EnumCurrencyType import EnumCurrencyType
from haasomeapi.enums.EnumFlashSpreadOptions import EnumFlashSpreadOptions


class FlashCrashBotSaveObject:
    botName: str
    botGuid: str
    accountId: str
    fee: float
    priceMarket: Market

    basePrice: float
    priceSpreadType: EnumFlashSpreadOptions
    priceSpread: float
    percentageBoost: float
    minPercentage: float
    maxPercentage: float

    accountType: EnumCurrencyType
    amountSpread: float
    buyAmount: float
    sellAmount: float
    refillDelay: int

    safetyEnabled: bool
    safetyTriggerLevel: float
    safetyMoveInOut: bool

    followTheTrend: bool
    followTheTrendChannelRange: int
    followTheTrendChannelOffset: int
    followTheTrendTimeout: int