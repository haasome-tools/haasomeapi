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
    """ Data Object cotaining a trade bots information

    :ivar botType: :class:`~haasomeapi.enums.EnumBotType`:
    :ivar guid: str:
    :ivar name: str:
    :ivar accountId: str:
    :ivar activated: bool:
    :ivar currentTradeAmount: float:
    :ivar currentFeePercentage: float:
    :ivar coinsPosition: :class:`~haasomeapi.enums.EnumCoinPosition`:
    :ivar fundsPosition: :class:`~haasomeapi.enums.EnumFundPosition`:
    :ivar lastBuyPrice: float:
    :ivar lastSellPrice: float:
    :ivar lastLongPrice: float:
    :ivar lastShortPrice: float:
    :ivar adjustAmountDown: bool:
    :ivar limitOrderType: :class:`~haasomeapi.enums.haasomeapi.enums.EnumLimitOrderPriceType`:
    :ivar openOrderTimeout: int:
    :ivar templateTimeout: int:
    :ivar goAllIn: bool:
    :ivar issuedOrders: List[str]:
    :ivar completedOrders: List[:class:`~haasomeapi.dataobjects.accountdata.BaseOrder`]:
    :ivar roi: float:
    :ivar totalFeeCosts: float:
    :ivar totalProfits: float:
    :ivar lastPriceUpdate: float:
    :ivar contractValue: float:
    :ivar groupName: str:
    :ivar botSignals: :class:`~haasomeapi.dataobjects.tradebot.TradeBotSignals`:
    :ivar messageProfile: :class:`~haasomeapi.dataobjects.custombots.dataobjects.MessageProfile`:
    :ivar botLogBook: List[str]:
    :ivar priceMarket: :class:`~haasomeapi.dataobjects.marketdata.Market`:
    :ivar leverage: float:
    :ivar unixSettlementDate: int:
    :ivar highFrequencyUpdates: bool:
    :ivar useHiddenOrders: bool:
    :ivar buyOrderTemplateId: str:
    :ivar sellOrderTemplateId: str:
    :ivar enterPositionOrderTemplateId: str:
    :ivar exitPositionOrderTemplateId: str:
    :ivar profitLabel: str:
    :ivar notes: str:
    :ivar locked: bool:
    :ivar activatedSince: int:
    :ivar deactivatedSince: int:
    :ivar consensusMode: bool:
    :ivar safeties: Dict[str, :class:`~haasomeapi.dataobjects.custombots.dataobjects.Safety`]:
    :ivar indicators: Dict[str, :class:`~haasomeapi.dataobjects.custombots.dataobjects.Indicator`]:
    :ivar insurances: Dict[str, :class:`~haasomeapi.dataobjects.custombots.dataobjects.Insurance`]:
    """

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





