from typing import Dict

from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.enums.EnumFundPosition import EnumFundPosition


class Position:
    """ Data Object containing the Base Order

    :ivar side: :class:`~haasomeapi.enums.EnumFundPosition`: 
    :ivar usedMargin: float: 
    :ivar amount: float:
    :ivar leverage: float: 
    :ivar priceMarket: :class:`~haasomeapi.dataobjects.marketdata.Market`:
    :ivar investmentPrice: float: 
    :ivar profitLossRatio: float: 
    :ivar profitLossNow: float: 
    :ivar marginCallPrice: float: 
    :ivar amountLabel: str:
    :ivar profitLabel: str:
    """
    
    side: EnumFundPosition
    usedMargin: float
    amount: float
    leverage: float
    priceMarket: Market
    investmentPrice: float
    profitLossRatio: float
    profitLossNow: float
    marginCallPrice: float
    amountLabel: str
    profitLabel: str
