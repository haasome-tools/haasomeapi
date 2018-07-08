from datetime import datetime


from haasomeapi.enums.EnumOrderType import EnumOrderType
from haasomeapi.enums.EnumOrderStatus import EnumOrderStatus
from haasomeapi.enums.EnumFundMovingPosition import EnumFundMovingPosition

from haasomeapi.dataobjects.marketdata.Market import Market


class BaseOrder:
    """    
    Data Object containing the Base Order

    :ivar pair: :class:`~haasomeapi.dataobjects.marketdata.Market`: Market Information
    :ivar orderId: str: Order Id
    :ivar orderStatus: :class:`~haasomeapi.enums.EnumOrderStatus`: Order Status
    :ivar orderType: :class:`~haasomeapi.enums.EnumOrderType`: Order Type
    :ivar fundMovement: :class:`~haasomeapi.enums.EnumFundMovingPosition`: Leverage Position
    :ivar price: float: Price Of Order
    :ivar amount: float: Amount In Order
    :ivar amountFilled: float: Amount Filled
    :ivar addedTime: :class:`~datetime`: Time Added In Datetime
    :ivar unixAddedTime: int: Time Added In Unix
    """
    
    pair: Market
    orderId: str
    orderStatus: EnumOrderStatus

    orderType: EnumOrderType
    fundMovement: EnumFundMovingPosition

    price: float
    amount: float
    amountFilled: float

    addedTime: datetime
    unixAddedTime: int
