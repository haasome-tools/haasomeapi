import json


class CryptoIndexBotIndexSaveObject:
    coin: str
    amount: float

    buyThreshold: float
    sellThreshold: float
    stopLoss: float

