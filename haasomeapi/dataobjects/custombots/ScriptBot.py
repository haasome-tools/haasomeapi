from typing import Dict
from typing import List

from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot

from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from haasomeapi.dataobjects.custombots.dataobjects.ScriptBotOrder import ScriptBotOrder


class ScriptBot(BaseCustomBot):
    """ Data Object containing a Script Bot

    :ivar openOrders = Dict[str, :class:`~haasomeapi.dataobjects.custombots.dataobjects.ScriptBotOrder`]:
    :ivar finishedOrder = List[str]:
    :ivar cancelledOrders = List[str]:
    :ivar availableScript = Dict[str, str]:
    :ivar scriptId: str:
    :ivar fullScriptName: str:
    :ivar botSettings: List[:class:`~haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption`]:
    :ivar scriptStatusOk: bool:
    :ivar localScriptPath: str:
    :ivar lastLongBuyPrice: float:
    :ivar lastShortBuyPrice: float:
    :ivar lastLongSellPrice: float:
    :ivar lastShortSellPrice: float:
    """

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
