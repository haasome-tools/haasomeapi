from haasomeapi.dataobjects.advancedorders.AdvancedOrderBase import AdvancedOrderBase


class StopTakeProfitOrder(AdvancedOrderBase):
    """    
    Data Object containing the Advanced Order Base

    :ivar triggerPrice: float: Price to strigger on
    :ivar executionPrice: float: Price to execute the order
    """
    triggerPrice: float
    executionPrice: float
