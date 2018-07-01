class CryptoIndexBotIndex:
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
