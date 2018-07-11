from typing import List

from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot
from haasomeapi.dataobjects.custombots.dataobjects.OrderBotPreOrder import OrderBotPreOrder


class OrderBot(BaseCustomBot):
    """ Data Object containing a Order Bot

    :ivar preOrders: List[:class:`~haasomeapi.dataobjects.custombots.dataobjects.OrderBotPreOrder`]:
    """

    preOrders: List[OrderBotPreOrder]