from typing import Dict

from haasomeapi.enums.EnumCurrencyType import EnumCurrencyType
from haasomeapi.enums.EnumFlashSpreadOptions import EnumFlashSpreadOptions

from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot
from haasomeapi.dataobjects.custombots.dataobjects.SlotObject import SlotObject


class FlashCrashBot(BaseCustomBot):
    """ Data Object containing a Flash Crash Bot

    :ivar slots: Dict[int, :class:`~haasomeapi.dataobjects.custombots.dataobjects.SlotObject`]:
    :ivar baseKey: int:
    :ivar totalBuyAmount: float:
    :ivar totalSellAmount: float:
    :ivar basePrice: float:
    :ivar isStopping: bool:
    :ivar priceSpreadType: :class:`~haasomeapi.enums.EnumFlashSpreadOptions`:
    :ivar priceSpread: float:
    :ivar percentageBoost: float:
    :ivar amountSpread: float:
    :ivar amountDecimals: int:
    :ivar priceDecimals: int:
    :ivar amountType: EnumCurrencyType:
    :ivar amountSpreadType: :class:`~haasomeapi.enums.EnumFlashSpreadOptions`:
    :ivar refillDelay: int:
    :ivar minPercentage: float:
    :ivar maxPercentage: float:
    :ivar quickRestartPossible: bool:
    :ivar followTheTrend: bool:
    :ivar followTheTrendTimeout: int:
    :ivar followTheTrendChannelRange: int:
    :ivar followTheTrendChannelRange: int:
    :ivar followTheTrendChannelOffset: int:
    :ivar safetyEnabled: bool:
    :ivar safetyTriggerLevel: float:
    :ivar safetyMoveInOut: bool:
    :ivar safetyMoveInOutTarget: float:
    """

    slots: Dict[int, SlotObject]
    baseKey: int

    totalBuyAmount: float
    totalSellAmount: float

    basePrice: float
    isStopping: bool

    priceSpreadType: EnumFlashSpreadOptions
    priceSpread: float
    percentageBoost: float

    amountSpread: float
    amountDecimals: int
    priceDecimals: int

    amountType: EnumCurrencyType
    amountSpreadType: EnumFlashSpreadOptions
    refillDelay: int

    minPercentage: float
    maxPercentage: float

    quickRestartPossible: bool

    followTheTrend: bool
    followTheTrendTimeout: int
    followTheTrendChannelRange: int
    followTheTrendChannelRange: int
    followTheTrendChannelOffset: int

    safetyEnabled: bool
    safetyTriggerLevel: float

    safetyMoveInOut: bool
    safetyMoveInOutTarget: float
