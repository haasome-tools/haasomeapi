from typing import List
from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder


class AdvancedOrderBase:
    """    
    Data Object containing the Advanced Order Base

    :ivar guid: str: Order Guid
    :ivar name: str: Name of the order
    :ivar activated: bool: Is Activated
    :ivar accountGuid: str: Account Guid
    :ivar market: :class:`~haasomeapi.dataobjects.marketdata.Market`: Market associated with order
    :ivar leverage: float: Leverage percentage of order
    :ivar amount: float: Amount In Order
    :ivar correctedAmount: float: Corrected amount for exchange
    :ivar orderDirection: int: Order Direction
    :ivar startOrderOnActivation: bool: Start order on activation
    :ivar startOrderPrice: float: Price to start the order on
    :ivar startTemplateGuid: bool: Start order template guid
    :ivar isPlacingStartOrder: bool: Place start order
    :ivar isTracking: bool: Tracking order
    :ivar templateGuid: str: Order template guid
    :ivar completedOrders: List[:class:`~haasomeapi.dataobjects.accountdata.BaseOrder`]: List of completed orders
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
