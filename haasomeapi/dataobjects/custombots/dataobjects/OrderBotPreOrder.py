from haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder
from haasomeapi.enums.EnumOrderBotTriggerType import EnumOrderBotTriggerType


class OrderBotPreOrder(BaseOrder):
    trigger: EnumOrderBotTriggerType
    triggerPrice: float
    customTemplate: str
    dependsOn: str
    dependsOnNotExecuted: str
