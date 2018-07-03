from haasomeapi.enums.EnumErrorCode import EnumErrorCode

from haasomeapi.apis.TradeApi import TradeApi
from haasomeapi.apis.TradeBotApi import TradeBotApi
from haasomeapi.apis.CustomBotApi import CustomBotApi
from haasomeapi.apis.MarketDataApi import MarketDataApi
from haasomeapi.apis.AccountDataApi import AccountDataApi
from haasomeapi.apis.AdvancedOrderApi import AdvancedOrderApi


class HaasomeClient:

    def __init__(self, connectionstring: str, privatekey: str):
        self.marketDataApi = MarketDataApi(connectionstring, privatekey)
        self.accountDataApi = AccountDataApi(connectionstring, privatekey)
        self.advancedOrderApi = AdvancedOrderApi(connectionstring, privatekey)
        self.customBotApi = CustomBotApi(connectionstring, privatekey)
        self.tradeApi = TradeApi(connectionstring, privatekey)
        self.tradeBotApi = TradeBotApi(connectionstring, privatekey)

    def test_credentials(self):
        result = self.marketDataApi.getEnabledPriceSources()
        return result.ErrorCode == EnumErrorCode.SUCCESS

