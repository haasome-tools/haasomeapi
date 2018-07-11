class ZoneDefinition:
    """ Data Object containing a Zone Definition

    :ivar amount: float:
    :ivar price: float:
    :ivar targetPrice: float:
    :ivar xposureNow: float:
    :ivar takenProfit: float:
    :ivar takenLosses: float:
    :ivar exit: float:
    :ivar feeCosts: float:
    """

    amount: float
    price: float
    targetPrice: float

    exposureNow: float
    takenProfit: float
    takenLosses: float
    exit: float
    feeCosts: float
