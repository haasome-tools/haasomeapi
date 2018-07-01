from typing import List

from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot
from haasomeapi.dataobjects.custombots.dataobjects.OrderBotPreOrder import OrderBotPreOrder


class OrderBot(BaseCustomBot):
    preOrders: List[OrderBotPreOrder]