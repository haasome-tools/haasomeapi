from dateutil import parser

from haasomeapi.apis.ApiBase import ApiBase

from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.dataobjects.marketdata.PriceTick import PriceTick
from haasomeapi.dataobjects.marketdata.Orderbook import Orderbook
from haasomeapi.dataobjects.marketdata.TradeContainer import TradeContainer

from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse


class MarketDataApi(ApiBase):
    """ The Market Data API Class.
    Gives access to the market data endpoints

    :param connectionstring: str: Connection String Formatted Ex. http://127.0.0.1:9000
    :param privatekey: str: Private Key Set In The Haas Settings
    """

    def __init__(self, connectionstring: str, privatekey: str):
        ApiBase.__init__(self, connectionstring, privatekey)

    def get_all_price_sources(self):
        """ Returns all avalible price sources

        
        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result List[str] of all the prices sources
        """

        response = super()._execute_request("/GetAllPriceSources", {})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], response["Result"])
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def get_enabled_price_sources(self):
        """ Returns all enabled price sources

        
        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result List[str] of all the enabled sources
        """
        response = super()._execute_request("/GetEnabledPriceSources", {})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], response["Result"])
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def get_all_price_markets(self):
        """ Returns all  markets

        
        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result List[:class:`~haasomeapi.dataobjects.marketdata.Market`] of markets
        """
        response = super()._execute_request("/GetAllPriceMarkets", {})

        markets = []

        for market in response["Result"]:
            markets.append(super()._from_json(market, Market))

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], markets)
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def get_price_markets(self, pricesource: EnumPriceSource):
        """ Returns markets for specified price source

        :param pricesource: :class:`~haasomeapi.enums.EnumPriceSource`: Price Source (Exchange) 

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result List[:class:`~haasomeapi.dataobjects.marketdata.Market`] of markets
        """

        response = super()._execute_request("/GetPriceMarkets", {"priceSourceName": EnumPriceSource(pricesource).name.capitalize()})

        markets = []

        for market in response["Result"]:
            markets.append(super()._from_json(market, Market))

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], markets)
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def get_price_ticker(self, pricesource: EnumPriceSource, primarycoin: str, secondarycoin: str, contractname: str):
        """ Returns the current price tick object

        :param pricesource: :class:`~haasomeapi.enums.EnumPriceSource`: Price Source (Exchange) to get ticker from 
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str:  Contract Name (Optional)

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.marketdata.PriceTick`: Price Tick object
        """

        response = super()._execute_request("/GetPriceTicker",
                                            {"priceSourceName": EnumPriceSource(pricesource).name.capitalize(),
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "contractName": contractname})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], PriceTick))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def get_price_ticker_from_market(self, market: Market):
        """ Returns the current price tick object from a market object

        :param market: :class:`~haasomeapi.dataobjects.marketdata.Market`: Market object to use

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.marketdata.PriceTick`: Price Tick object
        """

        return self.get_price_ticker(market.priceSource, market.primaryCurrency, market.secondaryCurrency,
                                     market.contractName)

    def get_minute_price_ticker(self, pricesource: EnumPriceSource, primarycoin: str, secondarycoin: str, contractname: str):
        """ Returns a minute price ticker

        :param pricesource: :class:`~haasomeapi.enums.EnumPriceSource`: Price Source (Exchange) to get ticker from 
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str:  Contract Name (Optional)

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.marketdata.PriceTick`: Price Tick object
        """

        response = super()._execute_request("/GetMinutePriceTicker",
                                            {"priceSourceName": EnumPriceSource(pricesource).name.capitalize(),
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "contractName": contractname})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], PriceTick))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def get_minute_price_ticker_from_market(self, market: Market):
        """ Returns a minute price ticker using a market object

        :param market: :class:`~haasomeapi.dataobjects.marketdata.Market`: Market object to use

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.marketdata.PriceTick`: Price Tick object
        """

        return self.get_minute_price_ticker(market.priceSource, market.primaryCurrency, market.secondaryCurrency,
                                     market.contractName)

    def get_last_trades(self, pricesource: EnumPriceSource, primarycoin: str, secondarycoin: str, contractname: str):
        """ Returns trade history for the specified market

        :param pricesource: :class:`~haasomeapi.enums.EnumPriceSource`: Price Source (Exchange) to get ticker from 
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str:  Contract Name (Optional)

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.marketdata.TradeContainer`: Trade Container object
        """

        response = super()._execute_request("/GetLastTrades",
                                            {"priceSourceName": EnumPriceSource(pricesource).name.capitalize(),
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "contractName": contractname})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], TradeContainer))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def get_last_trades_from_market(self, market: Market):
        """ Returns trade history for the specified market using a market object

        :param market: :class:`~haasomeapi.dataobjects.marketdata.Market`: Market object to use

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.marketdata.TradeContainer`: Trade Container object
        """

        return self.get_last_trades(market.priceSource, market.primaryCurrency, market.secondaryCurrency,
                                     market.contractName)

    def get_order_book(self, pricesource: EnumPriceSource, primarycoin: str, secondarycoin: str, contractname: str):
        """ Returns the current order book for specified market

        :param pricesource: :class:`~haasomeapi.enums.EnumPriceSource`: Price Source (Exchange) to get ticker from 
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str:  Contract Name (Optional)

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.marketdata.Orderbook`: Orderbook object
        """
    
        response = super()._execute_request("/GetOrderbook",
                                            {"priceSourceName": EnumPriceSource(pricesource).name.capitalize(),
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "contractName": contractname})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], Orderbook))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def get_order_book_from_market(self, market: Market):
        """ Returns the current order book for specified market using a market object

        :param market: :class:`~haasomeapi.dataobjects.marketdata.Market`: Market object to use

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.marketdata.Orderbook`: Orderbook object
        """

        return self.get_order_book(market.priceSource, market.primaryCurrency, market.secondaryCurrency,
                                     market.contractName)

    def get_history(self, pricesource: EnumPriceSource, primarycoin: str, secondarycoin: str, contractname: str, interval: int, depth: int):
        """ Get price history from price servers

        :param pricesource: :class:`~haasomeapi.enums.EnumPriceSource`: Price Source (Exchange) to get ticker from 
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str:  Contract Name (Optional)
        :param interval: int: The candle interval value Ex. 1,2,3,5,15,30,etc (In minutes)
        :param depth: int: The depth or how many candles to get

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result List[:class:`~haasomeapi.dataobjects.marketdata.PriceTick`]: List of Price Tick objects
        """

        response = super()._execute_request("/GetHistory",
                                            {"priceSourceName": EnumPriceSource(pricesource).name.capitalize(),
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "contractName": contractname,
                                             "interval": str(interval),
                                             "depth": str(depth)})

        priceticks = []

        try:
            for pricetick in response["Result"]:
                priceTickModel = super()._from_json(pricetick, PriceTick)
                priceTickModel.timeStamp = parser.parse(priceTickModel.timeStamp)
                priceticks.append(priceTickModel)

            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], priceticks)
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def get_history_from_market(self, market: Market, interval: int, depth: int):
        """ Get price history from price servers using market object

        :param market: :class:`~haasomeapi.dataobjects.marketdata.Market`: Market object to use
        :param interval: int: The candle interval value Ex. 1,2,3,5,15,30,etc (In minutes)
        :param depth: int: The depth or how many candles to get

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result List[:class:`~haasomeapi.dataobjects.marketdata.PriceTick`]: List of Price Tick objects
        """
        return self.get_history(market.priceSource, market.primaryCurrency, market.secondaryCurrency,
                                     market.contractName, interval, depth)
