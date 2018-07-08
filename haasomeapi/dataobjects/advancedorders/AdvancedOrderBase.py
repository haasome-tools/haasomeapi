from typing import List
from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder


class AdvancedOrderBase:
    """ Data Object containing the Advanced Order Base

    :ivar guid: str:
    :ivar name: str: 
    :ivar activated: bool: 
    :ivar accountGuid: str: 
    :ivar market: :class:`~haasomeapi.dataobjects.marketdata.Market`: 
    :ivar leverage: float:
    :ivar amount: float:
    :ivar correctedAmount: float: 
    :ivar orderDirection: int: 
    :ivar startOrderOnActivation: bool: 
    :ivar startOrderPrice: float: 
    :ivar startTemplateGuid: bool: 
    :ivar isPlacingStartOrder: bool: 
    :ivar isTracking: bool: 
    :ivar templateGuid: str: 
    :ivar completedOrders: List[:class:`~haasomeapi.dataobjects.accountdata.BaseOrder`]: 
    """

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
