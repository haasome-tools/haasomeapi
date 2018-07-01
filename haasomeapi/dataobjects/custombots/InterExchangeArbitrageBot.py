from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.dataobjects.marketdata.PriceTick import PriceTick
from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot


class InterExchangeArbitrageBot(BaseCustomBot):
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
