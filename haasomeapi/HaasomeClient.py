from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.apis.AccountDataApi import AccountDataApi


class HaasomeClient:

    def __init__(self, connectionstring: str, privatekey: str):
        #self.marketDataApi = MarketDataApi(connectionstring, privatekey)
        self.accountDataApi = AccountDataApi(connectionstring, privatekey)
        #self.customBotApi = CustomBotApi(connectionstring, privatekey)
        #self.tradeApi = TradeApi(connectionstring, privatekey)
        #self.tradeBotApi = TradeBotApi(connectionstring, privatekey)

    #def test_credentials(self):
        #result = MarketDataApi.getEnabledPriceSources()
        #return result.ErrorCode == EnumErrorCode.SUCCESS

