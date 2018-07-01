from typing import List

from haasomeapi.dataobjects.marketdata.Market import Market

from haasomeapi.enums.EnumIndicator import EnumIndicator
from haasomeapi.enums.EnumFundPosition import EnumFundPosition
from haasomeapi.enums.EnumPriceChartType import EnumPriceChartType
from haasomeapi.enums.EnumBotTradeResult import EnumBotTradeResult

from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption


class Indicator:
    guid: str
    indicatorType: EnumIndicator

    indicatorName: str
    indicatorInterface: List[IndicatorOption]

    indicatorTypeShortName: str
    indicatorTypeFullName: str

    priceMarket: Market
    chartType: EnumPriceChartType
    timer: int
    deviation: int

    useBuySignals: bool
    useSellSignals: bool
    useLongSignals: bool
    useNoPositionSignals: bool
    useShortSignals: bool

    reverseSignals: bool
    standAlone: bool

    buySellResult: EnumBotTradeResult
    shortLongResult: EnumFundPosition

    mappedLongSignal: EnumFundPosition
    mappedShortSignal: EnumFundPosition
