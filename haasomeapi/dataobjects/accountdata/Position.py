from typing import Dict

from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.enums.EnumFundPosition import EnumFundPosition


class Position:
    """    
    Data Object containing the Base Order

    :ivar side: :class:`~haasomeapi.enums.EnumFundPosition`: Position Of Trade
    :ivar usedMargin: float: Used Margin
    :ivar amount: float: Amount
    :ivar leverage: float: Leverage
    :ivar priceMarket: :class:`~haasomeapi.dataobjects.marketdata.Market`: Price Market
    :ivar investmentPrice: float: Investment
    :ivar profitLossRatio: float: Profit Loss Ratio
    :ivar profitLossNow: float: Profit Loss Now
    :ivar marginCallPrice: float: Margin Call Price
    :ivar amountLabel: str: Amount Label
    :ivar profitLabel: str: Profit Label
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
