from typing import Dict
from typing import List
from datetime import datetime

from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot
from haasomeapi.dataobjects.custombots.dataobjects.AdvancedIndexBotIndex import AdvancedIndexBotIndex

from haasomeapi.enums.EnumAdvancedIndexBotRebalanceType import EnumAdvancedIndexBotRebalanceType


class AdvancedIndexBot(BaseCustomBot):
    """ Data Object containing a Advanced Index bot

    :ivar baseCoin: str:
    :ivar index: List[:class:`~haasomeapi.dataobjects.custombots.dataobjects.AdvancedIndexBotIndex`]:
    :ivar totalExtraBuy: float:
    :ivar totalExtraSell: float:
    :ivar individualCoinGrowth: bool:
    :ivar allocateProfits: bool:
    :ivar lastOrderTimeStamp: :class:`~datettime`:
    :ivar mappedIndexes: Dict[str, float]:
    :ivar indexResults: Dict[str, :class:`~haasomeapi.dataobjects.custombots.dataobjects.AdvancedIndexBotIndex`]:
    """

    baseCoin: str
    index: List[AdvancedIndexBotIndex]

    totalExtraBuy: float
    totalExtraSell: float

    rebalanceType: EnumAdvancedIndexBotRebalanceType
    rebalanceInterval: int
    rebalanceTimestamp: datetime
    rebalanceUnix: float

    allocateProfits: bool
    lastOrderTimestamp: datetime
    preserveBaseIndexPercentage: bool

    mappedIndexes: Dict[str, float]
    indexResults: Dict[str, AdvancedIndexBotIndex]
