from typing import Dict
from typing import List
from datetime import datetime

from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot
from haasomeapi.dataobjects.custombots.dataobjects.CryptoIndexBotIndex import CryptoIndexBotIndex
from haasomeapi.dataobjects.custombots.dataobjects.CryptoIndexBotIndexResult import CryptoIndexBotIndexResult


class CryptoIndexBot(BaseCustomBot):
    """ Data Object containing a Crypto Index bot

    :ivar baseCoin: str:
    :ivar index: List[:class:`~haasomeapi.dataobjects.custombots.dataobjects.CryptoIndexBotIndex`]:
    :ivar totalExtraBuy: float:
    :ivar totalExtraSell: float:
    :ivar individualCoinGrowth: bool:
    :ivar allocateProfits: bool:
    :ivar lastOrderTimeStamp: :class:`~datettime`:
    :ivar mappedIndexes: Dict[str, float]:
    :ivar indexResults: Dict[str, :class:`~haasomeapi.dataobjects.custombots.dataobjects.CryptoIndexBotIndexResult`]:
    """

    baseCoin: str
    index: List[CryptoIndexBotIndex]

    totalExtraBuy: float
    totalExtraSell: float

    individualCoinGrowth: bool
    allocateProfits: bool
    lastOrderTimeStamp: datetime

    mappedIndexes: Dict[str, float]
    indexResults: Dict[str, CryptoIndexBotIndexResult]
