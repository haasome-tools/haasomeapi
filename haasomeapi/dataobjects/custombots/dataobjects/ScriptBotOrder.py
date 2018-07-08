from haasomeapi.enums.EnumOrderType import EnumOrderType
from haasomeapi.enums.EnumFundMovingPosition import EnumFundMovingPosition


class ScriptBotOrder:
    """ Data Object containing a Script Bot Order

    :ivar guid: str:
    :ivar price: float:
    :ivar amount: float:
    :ivar orderType: :class:`~haasomeapi.enums.EnumOrderType`:
    :ivar fundMovement: :class:`~haasomeapi.enums.EnumFundMovingPosition`:
    """

    guid: str
    price: float
    amount: float

    orderType: EnumOrderType
    fundMovement: EnumFundMovingPosition
