from haasomeapi.apis.ApiBase import ApiBase

from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.dataobjects.marketdata.PriceTick import PriceTick
from haasomeapi.dataobjects.marketdata.Orderbook import Orderbook
from haasomeapi.dataobjects.marketdata.TradeContainer import TradeContainer

from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse


class MarketDataApi(ApiBase):

    def __init__(self, connectionstring: str, privatekey: str):
        ApiBase.__init__(self, connectionstring, privatekey)

    def get_all_price_sources(self):
        response = super()._execute_request("/GetAllPriceSources", {})

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], response["Result"])

    def get_enabled_price_sources(self):
        response = super()._execute_request("/GetEnabledPriceSources", {})

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], response["Result"])

    def get_all_price_markets(self):
        response = super()._execute_request("/GetAllPriceMarkets", {})

        markets = []

        for market in response["Result"]:
            markets.append(super()._from_json(market, Market))

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], markets)

    def get_price_markets(self, pricesource: EnumPriceSource):
        response = super()._execute_request("/GetPriceMarkets", {"priceSourceName": EnumPriceSource(pricesource).name.capitalize()})

        markets = []

        for market in response["Result"]:
            markets.append(super()._from_json(market, Market))

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], markets)

    def get_price_ticker(self, pricesource: EnumPriceSource, primarycoin: str, secondarycoin: str, contractname: str):
        response = super()._execute_request("/GetPriceTicker",
                                            {"priceSourceName": EnumPriceSource(pricesource).name.capitalize(),
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "contractName": contractname})

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], super()._from_json(response["Result"], PriceTick))

    def get_price_ticker_from_market(self, market: Market):
        return self.get_price_ticker(market.priceSource, market.primaryCurrency, market.secondaryCurrency,
                                     market.contractName)

    def get_minute_price_ticker(self, pricesource: EnumPriceSource, primarycoin: str, secondarycoin: str, contractname: str):
        response = super()._execute_request("/GetMinutePriceTicker",
                                            {"priceSourceName": EnumPriceSource(pricesource).name.capitalize(),
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "contractName": contractname})

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], super()._from_json(response["Result"], PriceTick))

    def get_minute_price_ticker_from_market(self, market: Market):
        return self.get_minute_price_ticker(market.priceSource, market.primaryCurrency, market.secondaryCurrency,
                                     market.contractName)

    def get_last_trades(self, pricesource: EnumPriceSource, primarycoin: str, secondarycoin: str, contractname: str):
        response = super()._execute_request("/GetLastTrades",
                                            {"priceSourceName": EnumPriceSource(pricesource).name.capitalize(),
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "contractName": contractname})

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], super()._from_json(response["Result"], TradeContainer))

    def get_last_trades_from_market(self, market: Market):
        return self.get_last_trades(market.priceSource, market.primaryCurrency, market.secondaryCurrency,
                                     market.contractName)

    def get_order_book(self, pricesource: EnumPriceSource, primarycoin: str, secondarycoin: str, contractname: str):
        response = super()._execute_request("/GetOrderbook",
                                            {"priceSourceName": EnumPriceSource(pricesource).name.capitalize(),
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "contractName": contractname})

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], super()._from_json(response["Result"], Orderbook))

    def get_order_book_from_market(self, market: Market):
        return self.get_order_book(market.priceSource, market.primaryCurrency, market.secondaryCurrency,
                                     market.contractName)

    def get_history(self, pricesource: EnumPriceSource, primarycoin: str, secondarycoin: str, contractname: str, interval: int, depth: int):
        response = super()._execute_request("/GetHistory",
                                            {"priceSourceName": EnumPriceSource(pricesource).name.capitalize(),
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "contractName": contractname,
                                             "interval": str(interval),
                                             "depth": str(depth)})

        priceticks = []

        for pricetick in response["Result"]:
            priceticks.append(super()._from_json(pricetick, PriceTick))

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], priceticks)

    def get_history_from_market(self, market: Market, interval: int, depth: int):
        return self.get_history(market.priceSource, market.primaryCurrency, market.secondaryCurrency,
                                     market.contractName, interval, depth)
