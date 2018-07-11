from typing import List

from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot
from haasomeapi.dataobjects.custombots.dataobjects.EmailBotAction import EmailBotAction


class EmailBot(BaseCustomBot):
    """ Data Object containing a Email Bot

    :ivar actions: List[:class:`~haasomeapi.dataobjects.custombots.dataobjects.EmailBotAction`]:
    :ivar stopLoss: float:
    :ivar stopLossPrice: float:
    :ivar priceChangeToBuy: float:
    :ivar priceChangeToSell: float:
    :ivar priceChangeTarget: float:
    :ivar maximumLossOnPosition: float:
    :ivar minimumProfitOnPosition: float:
    """

    actions: List[EmailBotAction]
    stopLoss: float
    stopLossPrice: float

    priceChangeToBuy: float

    priceChangeToSell: float
    priceChangeTarget: float

    maximumLossOnPosition: float
    minimumProfitOnPosition: float
