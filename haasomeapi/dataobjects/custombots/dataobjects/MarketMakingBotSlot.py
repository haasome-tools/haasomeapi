from haasomeapi.dataobjects.custombots.dataobjects.MarketMakingBotSlotObject import MarketMakingBotSlotObject


class MarketMakingBotSlot:
    buyOrder: MarketMakingBotSlotObject
    sellOrder: MarketMakingBotSlotObject

    offset: float
    active: bool