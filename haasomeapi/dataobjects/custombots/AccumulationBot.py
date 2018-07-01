from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot

from haasomeapi.enums.EnumOrderType import EnumOrderType
from haasomeapi.enums.EnumAccumulationBotStopType import EnumAccumulationBotStopType


class AccumulationBot(BaseCustomBot):
    amountDecimals: int
    priceDecimals: int

    nextOrderTime: int

    orderType: EnumOrderType
    accumulatedSoFar: float
    stopType: EnumAccumulationBotStopType
    stopTypeValue: float

    randomOrderTimeX: int
    randomOrderTimeY: int

    randomOrderSizeX: int
    randomOrderSizeY: int

    triggerOnPrice: bool
    triggerWhenHigher: bool
    triggerValue: float

