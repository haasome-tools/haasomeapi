from haasomeapi.enums.EnumPriceSource import EnumPriceSource


class Market:
    """ Data Object containing market info

    :ivar priceSource: :class:`~haasomeapi.enums.EnumPriceSource`: 
    :ivar primaryCurrency: str:
    :ivar secondaryCurrency: str:
    :ivar contractName: str:
    :ivar displayName: str:
    :ivar shortName: str:
    :ivar amountDecimals: int:
    :ivar riceDecimals: int:
    :ivar minimumTradeAmount: float:
    :ivar minimumTradeVolume: float:
    :ivar tradeFee: float:
    :ivar settlementDate: int:
    """

    priceSource: EnumPriceSource
    primaryCurrency: str
    secondaryCurrency: str
    contractName: str

    displayName: str
    shortName: str

    amountDecimals: int
    priceDecimals: int
    minimumTradeAmount: float
    minimumTradeVolume: float

    tradeFee: float
    settlementDate: int
