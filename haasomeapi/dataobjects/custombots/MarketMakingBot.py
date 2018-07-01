from haasomeapi.dataobjects.marketdata.PriceTick import PriceTick
from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot

from haasomeapi.dataobjects.custombots.dataobjects.MarketMakingBotSlot import MarketMakingBotSlot


class MarketMakingBot(BaseCustomBot):
    tradeAmount: float
    customFee: float

    firstOrder: MarketMakingBotSlot
    secondOrder: MarketMakingBotSlot

    firstOffset: float
    secondOffset: float

    useSecondOrder: bool
    resetTimeout: int

    lastTick: PriceTick
