from typing import Dict
from typing import List

from haasomeapi.enums.EnumBotType import EnumBotType
from haasomeapi.enums.EnumCoinPosition import EnumCoinPosition
from haasomeapi.enums.EnumFundPosition import EnumFundPosition
from haasomeapi.enums.EnumLimitOrderPriceType import EnumLimitOrderPriceType

from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder
from haasomeapi.dataobjects.tradebot.TradeBotSignals import TradeBotSignals

from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.MessageProfile import MessageProfile


class TradeBot:
    botType: EnumBotType

    guid: str
    name: str
    accountId: str
    activated: bool
    currentTradeAmount: float
    currentFeePercentage: float

    coinsPosition: EnumCoinPosition
    fundsPosition: EnumFundPosition

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

    roi: float
    totalFeeCosts: float
    totalProfits: float

    lastPriceUpdate: float
    contractValue: float
    groupName: str

    botSignals: TradeBotSignals
    messageProfile: MessageProfile

    botLogBook: List[str]

    priceMarket: Market
    leverage: float

    unixSettlementDate: int

    highFrequencyUpdates: bool
    useHiddenOrders: bool

    buyOrderTemplateId: str
    sellOrderTemplateId: str

    enterPositionOrderTemplateId: str
    exitPositionOrderTemplateId: str

    profitLabel: str

    notes: str
    locked: bool
    activatedSince: int
    deactivatedSince: int
    consensusMode: bool

    safeties: Dict[str, Safety]
    indicators: Dict[str, Indicator]
    insurances: Dict[str, Insurance]





