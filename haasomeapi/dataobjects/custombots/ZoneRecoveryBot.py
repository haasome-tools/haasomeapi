from typing import List

from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot

from haasomeapi.enums.EnumFundPosition import EnumFundPosition
from haasomeapi.dataobjects.custombots.dataobjects.ZoneDefinition import ZoneDefinition
from haasomeapi.dataobjects.custombots.dataobjects.OpenRecoveryPositionDefinition import OpenRecoveryPositionDefinition


class ZoneRecoveryBot(BaseCustomBot):
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


