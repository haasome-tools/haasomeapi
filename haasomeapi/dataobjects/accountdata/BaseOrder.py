from datetime import datetime


from haasomeapi.enums.EnumOrderType import EnumOrderType
from haasomeapi.enums.EnumOrderStatus import EnumOrderStatus
from haasomeapi.enums.EnumFundMovingPosition import EnumFundMovingPosition

from haasomeapi.dataobjects.marketdata.Market import Market


class BaseOrder:
    """ Data Object containing the Base Order

    :ivar pair: :class:`~haasomeapi.dataobjects.marketdata.Market`: 
    :ivar orderId: str: 
    :ivar orderStatus: :class:`~haasomeapi.enums.EnumOrderStatus`:
    :ivar orderType: :class:`~haasomeapi.enums.EnumOrderType`: 
    :ivar fundMovement: :class:`~haasomeapi.enums.EnumFundMovingPosition`: 
    :ivar price: float: 
    :ivar amount: float: 
    :ivar amountFilled: float: 
    :ivar addedTime: :class:`~datetime`: 
    :ivar unixAddedTime: int: 
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
