from typing import List
from datetime import datetime

from haasomeapi.enums.EnumSlotType import EnumSlotType


class SlotObject:
    orderId: str
    price: float
    amount: float
    inUse: bool
    activeSlot: bool

    type: EnumSlotType
    waitingForExecuting: bool
    lockTimeStamp: datetime
    orderIds: List[str]