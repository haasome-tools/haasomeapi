from typing import List

from haasomeapi.enums.EnumSafety import EnumSafety
from haasomeapi.enums.EnumFundPosition import EnumFundPosition
from haasomeapi.enums.EnumBotTradeResult import EnumBotTradeResult

from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption


class Safety:
    guid: str
    safetyType: EnumSafety

    safetyName: str
    safetyTypeShortName: str
    safetyTypeFullName: str

    priceMarket: Market

    buySellResult: EnumBotTradeResult
    shortLongResult: EnumFundPosition

    mapBuySignal: EnumFundPosition
    mapSellSignal: EnumFundPosition

    safetyInterface: List[IndicatorOption]
