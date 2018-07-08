from typing import Dict

from haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder


class OrderContainer:
    """ Data Object containing the Base Order

    :ivar exchangeOrderList: Dict[str, :class:`~haasomeapi.dataobjects.accountdata.BaseOrder`]:
    :ivar marginOrderList: Dict[str, :class:`~haasomeapi.dataobjects.accountdata.BaseOrder`]:
    :ivar leverageOrderList: Dict[str, :class:`~haasomeapi.dataobjects.accountdata.BaseOrder`]: 
    """
    
    exchangeOrderList: Dict[str, BaseOrder]
    marginOrderList: Dict[str, BaseOrder]
    leverageOrderList: Dict[str, BaseOrder]
