from typing import List

from haasomeapi.enums.EnumBotTradeResult import EnumBotTradeResult
from haasomeapi.enums.EnumFundMovingPosition import EnumFundMovingPosition

from haasomeapi.dataobjects.custombots.dataobjects.EnumBotActionMessage import EmailBotActionMessage


class EmailBotAction:
    """ Data Object containing a Email Bot Action

    :ivar guid: str:
    :ivar providerGuid: str:
    :ivar templateGuid: str:
    :ivar messages: List[:class:`~haasomeapi.dataobjects.custombots.dataobjects.EnumBotActionMessage`]:
    :ivar timeoutInSeconds: int = 65:
    :ivar spotAction: :class:`~haasomeapi.enums.EnumBotTradeResult`:
    :ivar leverageAction: :class:`~haasomeapi.enums.EnumFundMovingPosition`:
    """

    guid: str
    providerGuid: str
    templateGuid: str
    messages: List[EmailBotActionMessage]

    timeoutInSeconds: int = 65

    spotAction: EnumBotTradeResult
    leverageAction: EnumFundMovingPosition