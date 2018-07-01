from typing import Dict

from haasomeapi.enums.EnumCurrencyType import EnumCurrencyType
from haasomeapi.enums.EnumFlashSpreadOptions  import EnumFlashSpreadOptions

from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot
from haasomeapi.dataobjects.custombots.dataobjects.SlotObject import SlotObject


class FlashCrashBot(BaseCustomBot):
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
