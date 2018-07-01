from haasomeapi.enums.EnumOrderType import EnumOrderType
from haasomeapi.enums.EnumFundMovingPosition import EnumFundMovingPosition


class ScriptBotOrder:
    guid: str
    price: float
    amount: float

    orderType: EnumOrderType
    fundMovement: EnumFundMovingPosition
