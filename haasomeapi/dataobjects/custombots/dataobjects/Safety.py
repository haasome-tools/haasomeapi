from typing import List

from haasomeapi.enums.EnumSafety import EnumSafety
from haasomeapi.enums.EnumFundPosition import EnumFundPosition
from haasomeapi.enums.EnumBotTradeResult import EnumBotTradeResult

from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption


class Safety:
    """ Data Object containing a Safety

    :ivar guid: str:
    :ivar safetyType: :class:`~haasomeapi.enums.EnumSafety`:
    :ivar safetyName: str:
    :ivar safetyTypeShortName: str:
    :ivar safetyTypeFullName: str:
    :ivar priceMarket: :class:`~haasomeapi.dataobjects.marketdata.Market`:
    :ivar buySellResult: :class:`~haasomeapi.enums.EnumBotTradeResult`:
    :ivar shortLongResult: :class:`~haasomeapi.enums.EnumFundPosition`:
    :ivar mapBuySignal: :class:`~haasomeapi.enums.EnumFundPosition`:
    :ivar mapSellSignal: :class:`~haasomeapi.enums.EnumFundPosition`:
    :ivar safetyInterface: List[:class:`~haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption`]:
    """

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
