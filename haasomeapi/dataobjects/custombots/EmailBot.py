from typing import List

from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot
from haasomeapi.dataobjects.custombots.dataobjects.EmailBotAction import EmailBotAction


class EmailBot(BaseCustomBot):
    actions: List[EmailBotAction]
    stopLoss: float
    stopLossPrice: float

    priceChangeToBuy: float

    priceChangeToSell: float
    priceChangeTarget: float

    maximumLossOnPosition: float
    minimumProfitOnPosition: float
