from haasomeapi.dataobjects.advancedorders.AdvancedOrderBase import AdvancedOrderBase


class TrailingStop(AdvancedOrderBase):
    """ Data Object containing the Advanced Order Base

    :ivar trailingStopPercentage: str: 
    :ivar recordedPrice: float:
    """
    
    trailingStopPercentage: float
    recordedPrice: float
