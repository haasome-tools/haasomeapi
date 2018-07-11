from haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder
from haasomeapi.enums.EnumOrderBotTriggerType import EnumOrderBotTriggerType


class OrderBotPreOrder(BaseOrder):
    """ Data Object containing a Order Bot Pre Order

    :ivar trigger: :class:`~haasomeapi.enums.EnumOrderBotTriggerType`
    :ivar triggerPrice: float:
    :ivar customTemplate: str:
    :ivar dependsOn: str:
    :ivar dependsOnNotExecuted: str:
    """

    trigger: EnumOrderBotTriggerType
    triggerPrice: float
    customTemplate: str
    dependsOn: str
    dependsOnNotExecuted: str
