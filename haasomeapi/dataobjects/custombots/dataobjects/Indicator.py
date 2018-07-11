from typing import List

from haasomeapi.dataobjects.marketdata.Market import Market

from haasomeapi.enums.EnumIndicator import EnumIndicator
from haasomeapi.enums.EnumFundPosition import EnumFundPosition
from haasomeapi.enums.EnumPriceChartType import EnumPriceChartType
from haasomeapi.enums.EnumBotTradeResult import EnumBotTradeResult

from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption


class Indicator:
    """ Data Object containing a Indicator

    :ivar guid: str:
    :ivar indicatorType: :class:`~haasomeapi.enums.EnumIndicator`:
    :ivar indicatorName: str:
    :ivar indicatorInterface: List[:class:`~haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption`]:
    :ivar indicatorTypeShortName: str:
    :ivar indicatorTypeFullName: str:
    :ivar priceMarket: Market:
    :ivar chartType: :class:`~haasomeapi.enums.EnumPriceChartType`:
    :ivar timer: int:
    :ivar deviation: int:
    :ivar useBuySignals: bool:
    :ivar useSellSignals: bool:
    :ivar useLongSignals: bool:
    :ivar useNoPositionSignals: bool:
    :ivar useShortSignals: bool:
    :ivar reverseSignals: bool:
    :ivar standAlone: bool:
    :ivar buySellResult: :class:`~haasomeapi.enums.EnumBotTradeResult`:
    :ivar shortLongResult: :class:`~haasomeapi.enums.EnumFundPosition`:
    :ivar mappedLongSignal: :class:`~haasomeapi.enums.EnumFundPosition`:
    :ivar mappedShortSignal: :class:`~haasomeapi.enums.EnumFundPosition`:
    """

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
