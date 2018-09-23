from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator

from haasomeapi.enums.EnumFundPosition import EnumFundPosition
from haasomeapi.enums.EnumBotTradeAmount import EnumBotTradeAmount

class MadHatterBot(BaseCustomBot):
    """ Data Object containing a Mad Hatter Bot

    :ivar interval: int:
    :ivar stopLoss: float:
    :ivar stopLossPrice: float:
    :ivar disableAfterStopLoss: bool:
    :ivar priceChangeToBuy: float:
    :ivar priceChangeToSell: float:
    :ivar priceChangeTarget: float:
    :ivar macd: :class:`~haasomeapi.dataobjects.custombots.dataobjects.Indicator`:
    :ivar bbands: :class:`~haasomeapi.dataobjects.custombots.dataobjects.Indicator`:
    :ivar rsi: :class:`~haasomeapi.dataobjects.custombots.dataobjects.Indicator`:
    :ivar mappedBuySignal: :class:`~haasomeapi.enums.EnumFundPosition`:
    :ivar mappedSellSignal: :class:`~haasomeapi.enums.EnumFundPosition`:
    :ivar useTwoSIgnals: bool:
    """

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

    mappedBuySignal: EnumFundPosition
    mappedSellSignal: EnumFundPosition
