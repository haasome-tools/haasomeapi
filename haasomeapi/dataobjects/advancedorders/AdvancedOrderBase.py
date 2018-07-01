from typing import List
from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder


class AdvancedOrderBase:
    guid: str
    name: str
    activated: bool

    accountGuid: str
    market: Market
    leverage: float

    amount: float
    correctedAmount: float

    orderDirection: int

    startOrderOnActivation: bool
    startOrderPrice: float
    startTemplateGuid: str

    isPlacingStartOrder: bool
    isTracking: bool

    templateGuid: str

    completedOrders: List[BaseOrder]
