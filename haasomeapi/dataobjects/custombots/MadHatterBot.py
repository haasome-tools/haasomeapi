from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator


class MadHatterBot(BaseCustomBot):
    interval: int

    stopLoss: float
    stopLossPrice: float
    disableAfterStopLoss: bool

    priceChangeToBuy: float
    priceChangeToSell: float
    priceChangeTarget: float

    macd: Indicator
    bbands: Indicator
    rsi: Indicator

    useTwoSIgnals: bool
