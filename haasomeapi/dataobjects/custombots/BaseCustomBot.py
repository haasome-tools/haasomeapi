from typing import List

from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder

from haasomeapi.enums.EnumCoinPosition import EnumCoinPosition
from haasomeapi.enums.EnumFundPosition import EnumFundPosition
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType


class BaseCustomBot:
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
