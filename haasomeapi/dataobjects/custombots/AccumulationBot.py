from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot

from haasomeapi.enums.EnumOrderType import EnumOrderType
from haasomeapi.enums.EnumAccumulationBotStopType import EnumAccumulationBotStopType


class AccumulationBot(BaseCustomBot):
    """ Data Object containing a Accumlation Bot

    :ivar amountDecimals: int:
    :ivar priceDecimals: int:
    :ivar nextOrderTime: int:
    :ivar orderType: :class:`~haasomeapi.enums.EnumOrderType`:
    :ivar accumulatedSoFar: float:
    :ivar stopType: :class:`~haasomeapi.enums.EnumAccumulationBotStopType`:
    :ivar stopTypeValue: float:
    :ivar randomOrderTimeX: int:
    :ivar randomOrderTimeY: int:
    :ivar randomOrderSizeX: int:
    :ivar randomOrderSizeY: int:
    :ivar triggerOnPrice: bool:
    :ivar triggerWhenHigher: bool:
    :ivar triggerValue: float:
    """

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

