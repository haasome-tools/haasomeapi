from haasomeapi.dataobjects.advancedorders.AdvancedOrderBase import AdvancedOrderBase


class StopTakeProfitOrder(AdvancedOrderBase):
    """ Data Object containing the Advanced Order Base

    :ivar triggerPrice: float: 
    :ivar executionPrice: float: 
    """
    triggerPrice: float
    executionPrice: float
