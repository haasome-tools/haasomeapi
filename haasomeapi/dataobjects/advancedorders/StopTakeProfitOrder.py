from haasomeapi.dataobjects.advancedorders.AdvancedOrderBase import AdvancedOrderBase


class StopTakeProfitOrder(AdvancedOrderBase):
    triggerPrice: float
    executionPrice: float
