"""
.. module:: haasomeapi
    :platform: any
    :synopsis: Core Haasonline Module For Local Api 
 
.. moduleauthor:: Raynaldo Rivera <royal.r4stl1n@gmail.com>
"""

from haasomeapi.enums.EnumErrorCode import EnumErrorCode

from haasomeapi.apis.TradeApi import TradeApi
from haasomeapi.apis.TradeBotApi import TradeBotApi
from haasomeapi.apis.CustomBotApi import CustomBotApi
from haasomeapi.apis.MarketDataApi import MarketDataApi
from haasomeapi.apis.AccountDataApi import AccountDataApi
from haasomeapi.apis.AdvancedOrderApi import AdvancedOrderApi


class HaasomeClient:
    """ The Core Haasome Client Class.
    Gives access to the main api modules to interact with the haasonline local api

    :param connectionstring: str: Connection String Formatted Ex. http://127.0.0.1:9000
    :param privatekey: str: Private Key Set In The Haas Settings
    """

    def __init__(self, connectionstring: str, privatekey: str):
        """A simple initialization method.
 
        :param connectionstring: str: Connection String Formatted http://<ip:port> asdfasdf
        :param privatekey: str: Private Key Set In The Haas Settings 
        """
        self.marketDataApi = MarketDataApi(connectionstring, privatekey)
        self.accountDataApi = AccountDataApi(connectionstring, privatekey)
        self.advancedOrderApi = AdvancedOrderApi(connectionstring, privatekey)
        self.customBotApi = CustomBotApi(connectionstring, privatekey)
        self.tradeApi = TradeApi(connectionstring, privatekey)
        self.tradeBotApi = TradeBotApi(connectionstring, privatekey)

    def test_credentials(self):
        """
        Verifies that the supplied credentials work and a valid connection to the
        Haasonline Local Api is made.

        :return :class:`~haasomeapi.enums.EnumErrorCode`
        """
        result = self.accountDataApi.get_all_wallets()
        return result

