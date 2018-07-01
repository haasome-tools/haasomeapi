from typing import List

from haasomeapi.enums.EnumBotTradeResult import EnumBotTradeResult
from haasomeapi.enums.EnumFundMovingPosition import EnumFundMovingPosition

from haasomeapi.dataobjects.custombots.dataobjects.EnumBotActionMessage import EmailBotActionMessage


class EmailBotAction:
    guid: str
    providerGuid: str
    messages: List[EmailBotActionMessage]

    timeoutInSeconds: int = 65

    spotAction: EnumBotTradeResult
    leverageAction: EnumFundMovingPosition