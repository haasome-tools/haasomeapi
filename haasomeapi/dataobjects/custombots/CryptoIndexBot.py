from typing import Dict
from typing import List
from datetime import datetime

from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot
from haasomeapi.dataobjects.custombots.dataobjects.CryptoIndexBotIndex import CryptoIndexBotIndex
from haasomeapi.dataobjects.custombots.dataobjects.CryptoIndexBotIndexResult import CryptoIndexBotIndexResult


class CryptoIndexBot(BaseCustomBot):
    baseCoin: str
    index: List[CryptoIndexBotIndex]

    totalExtraBuy: float
    totalExtraSell: float

    individualCoinGrowth: bool
    allocateProfits: bool
    lastOrderTimeStamp: datetime

    mappedIndexes: Dict[str, float]
    indexResults: Dict[str, CryptoIndexBotIndexResult]
