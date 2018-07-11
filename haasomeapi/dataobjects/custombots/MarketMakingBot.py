from haasomeapi.dataobjects.marketdata.PriceTick import PriceTick
from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot

from haasomeapi.dataobjects.custombots.dataobjects.MarketMakingBotSlot import MarketMakingBotSlot


class MarketMakingBot(BaseCustomBot):
    """ Data Object containin a Market Making Bot

    :ivar tradeAmount: float:
    :ivar customFee: float:
    :ivar firstOrder: :class:`~haasomeapi.dataobjects.custombots.dataobjects.MarketMakingBotSlot`:
    :ivar secondOrder: :class:`~haasomeapi.dataobjects.custombots.dataobjects.MarketMakingBotSlot`:
    :ivar firstOffset: float:
    :ivar secondOffset: float:
    :ivar useSecondOrder: bool:
    :ivar resetTimeout: int:
    :ivar lastTick: :class:`~haasomeapi.dataobjects.marketdata.PriceTick`:
    """

    tradeAmount: float
    customFee: float

    firstOrder: MarketMakingBotSlot
    secondOrder: MarketMakingBotSlot

    firstOffset: float
    secondOffset: float

    useSecondOrder: bool
    resetTimeout: int

    lastTick: PriceTick
