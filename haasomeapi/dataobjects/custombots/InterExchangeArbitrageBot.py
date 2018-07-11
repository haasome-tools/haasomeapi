from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.dataobjects.marketdata.PriceTick import PriceTick
from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot


class InterExchangeArbitrageBot(BaseCustomBot):
    """ Data Object containing a Inter Exchange Arbitrage Bot

    :ivar currentFeePercentage2: float:
    :ivar accountId2: str:
    :ivar priceMarket2: :class:`~haasomeapi.dataobjects.marketdata.Market`:
    :ivar triggerLevel: float:
    :ivar mainAccountIsBought: bool:
    :ivar lastTick: :class:`~haasomeapi.dataobjects.marketdata.PriceTick`:
    :ivar lastTick2: :class:`~haasomeapi.dataobjects.marketdata.PriceTick`:
    :ivar priceDecimals1: int:
    :ivar priceDecimals2: int:
    :ivar openOrderIdMain: str:
    :ivar openOrderIdSecondary: str:
    :ivar totalTradesSoFar: float:
    :ivar maxTradeAmount: float:
    :ivar maxTradesPerDay: int:
    """

    currentFeePercentage2: float
    accountId2: str

    priceMarket2: Market

    triggerLevel: float
    mainAccountIsBought: bool

    lastTick: PriceTick
    lastTick2: PriceTick

    priceDecimals1: int
    priceDecimals2: int

    openOrderIdMain: str
    openOrderIdSecondary: str

    totalTradesSoFar: float
    maxTradeAmount: float

    maxTradesPerDay: int
