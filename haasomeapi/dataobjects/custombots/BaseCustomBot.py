from typing import List

from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder

from haasomeapi.enums.EnumCoinPosition import EnumCoinPosition
from haasomeapi.enums.EnumFundPosition import EnumFundPosition
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haasomeapi.enums.EnumBotTradeAmount import EnumBotTradeAmount


class BaseCustomBot:
    """ Data Object containing the Base Custom Bot 

    :ivar botType: :class:`~haasomeapi.enums.EnumCustomBotType`:
    :ivar isBackTesting: bool:
    :ivar guid: str:
    :ivar name: str:
    :ivar accountId: str:
    :ivar priceMarket: :class:`~haasomeapi.dataobjects.marketdata.Market`:
    :ivar leverage: float:
    :ivar coinPosition: :class:`~haasomeapi.enums.EnumCoinPosition`:
    :ivar fundPosition: :class:`~haasomeapi.enums.EnumFundPosition`:
    :ivar currentTradeAmount: float:
    :ivar correctedTradeAmount: float:
    :ivar amountType: :class:`~haasomeapi.enums.EnumBotTradeAmount`:
    :ivar lastBuyPrice: float:
    :ivar lastSellPrice: float:
    :ivar currentFeePercentage: float:
    :ivar settlementDate: int:
    :ivar profitLabel: str:
    :ivar activated: bool:
    :ivar activatedSince: int:
    :ivar deactivatedSince: int:
    :ivar statusPriceSourceOk: bool:
    :ivar statusAccountOk: bool:
    :ivar openOrdersOk: bool:
    :ivar walletOk: bool:
    :ivar openOrderId: str:
    :ivar totalFeeCosts: float:
    :ivar totalProfits: float:
    :ivar roi: float:
    :ivar lastPriceUpdate: float:
    :ivar contractValue: float:
    :ivar lastUpdateTime: int:
    :ivar groupName: str:
    :ivar notes: str:
    :ivar customTemplate: str:
    :ivar botLogBook: List[str]:
    :ivar completedOrders: List[:class:`~haasomeapi.dataobjects.accountdata.BaseOrder`]:
    """

    botType: EnumCustomBotType
    isBackTesting: bool
    guid: str
    name: str
    accountId: str
    priceMarket: Market
    leverage: float

    coinPosition: EnumCoinPosition
    fundPosition: EnumFundPosition

    currentTradeAmount: float
    correctedTradeAmount: float
    amountType: EnumBotTradeAmount

    lastBuyPrice: float
    lastSellPrice: float

    currentFeePercentage: float
    settlementDate: int
    profitLabel: str
    activated: bool
    activatedSince: int
    deactivatedSince: int
    statusPriceSourceOk: bool
    statusAccountOk: bool
    openOrdersOk: bool
    walletOk: bool

    openOrderId: str
    totalFeeCosts: float
    totalProfits: float
    roi: float

    lastPriceUpdate: float
    contractValue: float
    lastUpdateTime: int

    groupName: str
    notes: str

    customTemplate: str

    botLogBook: List[str]
    completedOrders: List[BaseOrder]
