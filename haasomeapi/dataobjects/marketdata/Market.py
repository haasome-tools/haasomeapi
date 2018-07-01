from haasomeapi.enums.EnumPriceSource import EnumPriceSource


class Market:
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
