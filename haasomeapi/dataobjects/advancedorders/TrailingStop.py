from haasomeapi.dataobjects.advancedorders.AdvancedOrderBase import AdvancedOrderBase


class TrailingStop(AdvancedOrderBase):
    """    
    Data Object containing the Advanced Order Base

    :ivar trailingStopPercentage: str: Trailing stop percentage
    :ivar recordedPrice: float: Current recorded price
    """
    trailingStopPercentage: float
    recordedPrice: float
