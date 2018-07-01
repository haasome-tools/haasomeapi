from typing import List

from haasomeapi.enums.EnumBotType import EnumBotType
from haasomeapi.enums.EnumCoinPosition import EnumCoinPosition
from haasomeapi.enums.EnumFundPosition import EnumFundPosition
from haasomeapi.enums.EnumLimitOrderPriceType import EnumLimitOrderPriceType

from haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder


class TradeBot:
    botType: EnumBotType

    guid: str
    name: str
    accountId: str
    activated: bool
    currentTradeAmount: float
    currentFeePercentage: float

    coinPosition: EnumCoinPosition
    fundPosition: EnumFundPosition

    lastBuyPrice: float
    lastSellPrice: float

    lastLongPrice: float
    lastShortPrice: float

    adjustAmountDown: bool
    limitOrderType: EnumLimitOrderPriceType

    openOrderTimeout: int
    templateTimeout: int
    goAllIn: bool

    issuedOrders: List[str]
    completedOrders: List[BaseOrder]



