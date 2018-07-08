from typing import List
from datetime import datetime

from haasomeapi.enums.EnumSlotType import EnumSlotType


class SlotObject:
    """ Data Object containing a Slot Object

    :ivar orderId: str:
    :ivar price: float:
    :ivar amount: float:
    :ivar inUse: bool:
    :ivar activeSlot: bool:
    :ivar type: :class:`~haasomeapi.enums.EnumSlotType`:
    :ivar waitingForExecuting: bool:
    :ivar lockTimeStamp: :class:`~datetime`:
    :ivar orderIds: List[str]:
    """

    orderId: str
    price: float
    amount: float
    inUse: bool
    activeSlot: bool

    type: EnumSlotType
    waitingForExecuting: bool
    lockTimeStamp: datetime
    orderIds: List[str]