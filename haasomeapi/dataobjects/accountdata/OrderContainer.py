from typing import Dict

from haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder


class OrderContainer:
    exchangeOrderList: Dict[str, BaseOrder]
    marginOrderList: Dict[str, BaseOrder]
    leverageOrderList: Dict[str, BaseOrder]
