from typing import List

from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot

from haasomeapi.enums.EnumFundPosition import EnumFundPosition
from haasomeapi.dataobjects.custombots.dataobjects.ZoneDefinition import ZoneDefinition
from haasomeapi.dataobjects.custombots.dataobjects.OpenRecoveryPositionDefinition import OpenRecoveryPositionDefinition


class ZoneRecoveryBot(BaseCustomBot):
    """ Data Object containing a Zone Recovery Bot

    :ivar factorShort: float:
    :ivar factorLong: float:
    :ivar zoneFactor: float:
    :ivar targetPercentage: float:
    :ivar tradeAmount: float:
    :ivar maxTradeAmount: float:
    :ivar triggerLevel: float:
    :ivar useMarketOrders: bool:
    :ivar roundAmount: bool:
    :ivar basePrice: float:
    :ivar firstAction: :class:`~haasomeapi.enums.EnumFundPosition`:
    :ivar calculatedZones: List[:class:`~haasomeapi.dataobjects.custombots.dataobjects.ZoneDefinition`]
    :ivar takeLongPrice: float
    :ivar goLongPrice: float
    :ivar goShortPrice: float
    :ivar takeShortPrice: float
    :ivar takenPositions: List[:class:`~haasomeapi.dataobjects.custombots.dataobjects.OpenRecoveryPositionDefinition`]
    """

    factorShort: float
    factorLong: float
    zoneFactor: float
    targetPercentage: float
    tradeAmount: float
    maxTradeAmount: float

    triggerLevel: float
    useMarketOrders: bool
    roundAmount: bool

    basePrice: float
    firstAction: EnumFundPosition

    calculatedZones: List[ZoneDefinition]
    takeLongPrice: float
    goLongPrice: float
    goShortPrice: float
    takeShortPrice: float
    takenPositions: List[OpenRecoveryPositionDefinition]


