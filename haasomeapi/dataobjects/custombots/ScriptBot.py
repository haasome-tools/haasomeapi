from typing import Dict
from typing import List

from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot

from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from haasomeapi.dataobjects.custombots.dataobjects.ScriptBotOrder import ScriptBotOrder


class ScriptBot(BaseCustomBot):
    openOrders = Dict[str, ScriptBotOrder]

    finishedOrder = List[str]
    cancelledOrders = List[str]
    availableScript = Dict[str, str]

    scriptId: str
    fullScriptName: str

    botSettings: List[IndicatorOption]
    scriptStatusOk: bool
    localScriptPath: str

    lastLongBuyPrice: float
    lastShortBuyPrice: float
    lastLongSellPrice: float
    lastShortSellPrice: float
