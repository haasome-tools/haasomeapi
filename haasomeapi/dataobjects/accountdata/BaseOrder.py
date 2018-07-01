from datetime import datetime


from haasomeapi.enums.EnumOrderType import EnumOrderType
from haasomeapi.enums.EnumOrderStatus import EnumOrderStatus
from haasomeapi.enums.EnumFundMovingPosition import EnumFundMovingPosition

from haasomeapi.dataobjects.marketdata.Market import Market


class BaseOrder:
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
