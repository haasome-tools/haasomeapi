from typing import Dict

from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.enums.EnumFundPosition import EnumFundPosition


class Position:
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
