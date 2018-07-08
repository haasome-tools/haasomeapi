from haasomeapi.dataobjects.custombots.dataobjects.MarketMakingBotSlotObject import MarketMakingBotSlotObject


class MarketMakingBotSlot:
    """ Data Object containing a Market Making Bot Slot

    :ivar buyOrder: :class:`~haasomeapi.dataobjects.custombots.dataobjects.MarketMakingBotSlotObject`:
    :ivar sellOrder: :class:`~haasomeapi.dataobjects.custombots.dataobjects.MarketMakingBotSlotObject`:
    :ivar offset: float:
    :ivar active: bool:
    """

    buyOrder: MarketMakingBotSlotObject
    sellOrder: MarketMakingBotSlotObject

    offset: float
    active: bool