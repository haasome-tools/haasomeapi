class CryptoIndexBotIndex:
    """ Data Object containing a Crypto Index Bot Index

    :ivar coin: str:
    :ivar amount: float:
    :ivar startPrice: float:
    :ivar conversionRate: float:
    :ivar buyThreshold: float:
    :ivar sellThreshold: float:
    :ivar needsReBalancing: bool:
    :ivar hasOpenOrder: bool:
    :ivar isStopLossActive: bool:
    :ivar stopLoss: float:
    """

    coin: str
    amount: float
    startPrice: float
    conversionRate: float

    buyThreshold: float
    sellThreshold: float

    needsReBalancing: bool
    hasOpenOrder: bool

    isStopLossActive: bool
    stopLoss: float
