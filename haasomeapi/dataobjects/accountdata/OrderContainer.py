from typing import Dict

from haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder


class OrderContainer:
    """    
    Data Object containing the Base Order

    :ivar exchangeOrderList: Dict[str, :class:`~haasomeapi.dataobjects.accountdata.BaseOrder`]: Spot Order List
    :ivar marginOrderList: Dict[str, :class:`~haasomeapi.dataobjects.accountdata.BaseOrder`]: Margin Order List
    :ivar leverageOrderList: Dict[str, :class:`~haasomeapi.dataobjects.accountdata.BaseOrder`]: Leverage Order List
    """
    
    exchangeOrderList: Dict[str, BaseOrder]
    marginOrderList: Dict[str, BaseOrder]
    leverageOrderList: Dict[str, BaseOrder]
