class AdvancedIndexBotIndex:
    """ Data Object containing a Crypto Index Bot Index

    :ivar coin: str:
    :ivar allocatedPercentage: float:
    :ivar lastCalculatedPercentage: float:
    :ivar inVirtualWallet: float:
    :ivar inRealWallet: float:
    :ivar targetAmount: float:
    :ivar inVirtualWalletBase: float:
    :ivar inRealWalletBase: float:
    :ivar targetAmountBase: float:
    :ivar startPrice: float:
    :ivar lastUsedPrice: float:
    :ivar currentPrice: float:
    :ivar buyThreshold: float:
    :ivar buyTarget: float:
    :ivar sellThreshold: float:
    :ivar sellTarget: float:
    :ivar stopLoss: float:
    :ivar stopLossPrice: float:
    :ivar isStopLossActive: bool:
    :ivar trailingStop: float:
    :ivar trailingStopPrice: float:
    :ivar highestRecordPrice: float:
    :ivar isTrailingStopLossActive: bool:
    :ivar isExcluded: bool:
    :ivar openOrderId: str:
    :ivar hasOpenOrder: bool:
    """

    coin: str
    allocatedPercentage: float
    lastCalculatedPercentage: float

    inVirtualWallet: float
    inRealWallet: float
    targetAmount: float

    inVirtualWalletBase: float
    inRealWalletBase: float
    targetAmountBase: float

    startPrice: float
    lastUsedPrice: float
    currentPrice: float

    buyThreshold: float
    buyTarget: float

    sellThreshold: float
    sellTarget: float

    stopLoss: float
    stopLossPrice: float
    isStopLossActive: bool

    trailingStop: float
    trailingStopPrice: float
    highestRecordPrice: float
    isTrailingStopLossActive: bool

    isExcluded: bool

    openOrderId: str

    hasOpenOrder: bool
