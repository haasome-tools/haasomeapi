from haasomeapi.dataobjects.advancedorders.AdvancedOrderBase import AdvancedOrderBase


class TrailingStop(AdvancedOrderBase):
    trailingStopPercentage: float
    recordedPrice: float
