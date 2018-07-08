from haasomeapi.dataobjects.marketdata.Market import Market

from haasomeapi.enums.EnumCurrencyType import EnumCurrencyType
from haasomeapi.enums.EnumFlashSpreadOptions import EnumFlashSpreadOptions


class FlashCrashBotSaveObject:
    """ Data Object containing a Falsh Crash Bot Save Object

    :ivar botName: str:
    :ivar botGuid: str:
    :ivar accountId: str:
    :ivar fee: float:
    :ivar priceMarket: :class:`~haasomeapi.dataobjects.marketdata.Market`:
    :ivar basePrice: float:
    :ivar priceSpreadType: :class:`~haasomeapi.enums.EnumFlashSpreadOptions`:
    :ivar priceSpread: float:
    :ivar percentageBoost: float:
    :ivar minPercentage: float:
    :ivar maxPercentage: float:
    :ivar accountType: :class:`~haasomeapi.enums.EnumCurrencyType`:
    :ivar amountSpread: float:
    :ivar buyAmount: float:
    :ivar sellAmount: float:
    :ivar refillDelay: int:
    :ivar safetyEnabled: bool:
    :ivar safetyTriggerLevel: float:
    :ivar safetyMoveInOut: bool:
    :ivar followTheTrend: bool:
    :ivar followTheTrendChannelRange: int:
    :ivar followTheTrendChannelOffset: int:
    :ivar followTheTrendTimeout: int:
    """

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