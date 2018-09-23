import datetime

from haasomeapi.apis.ApiBase import ApiBase
from haasomeapi.enums.EnumErrorCode import EnumErrorCode

from haasomeapi.enums.EnumSafety import EnumSafety
from haasomeapi.enums.EnumIndicator import EnumIndicator
from haasomeapi.enums.EnumInsurance import EnumInsurance
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from haasomeapi.enums.EnumFundPosition import EnumFundPosition
from haasomeapi.enums.EnumCoinPosition import EnumCoinPosition
from haasomeapi.enums.EnumPriceChartType import EnumPriceChartType
from haasomeapi.enums.EnumLimitOrderPriceType import EnumLimitOrderPriceType
from haasomeapi.enums.EnumSafetyPositionSignal import EnumSafetyPositionSignal

from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption

from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse


class TradeBotApi(ApiBase):
    """The Trade Bot API Class.
    Gives access to the trade bot api endpoints

    :param connectionstring: str: Connection String Formatted Ex. http://127.0.0.1:9000
    :param privatekey: str: Private Key Set In The Haas Settings
    """

    def __init__(self, connectionstring: str, privatekey: str):
        ApiBase.__init__(self, connectionstring, privatekey)

    def _convert_json_bot_to_trade_bot_object(self, jsonstr: str):
        """ Internal function to easily convert json to Tradebot objet
        :param jsonstr: str: Tradebot in a json string

        :returns: :class:`~haasomeapi.dataobjects.tradebot.TradeBot`
        """

        botinitial = super()._from_json(jsonstr, TradeBot)

        indicators = {}
        safeties = {}
        insurances = {}

        for k, v in botinitial.indicators.items():
            indicatoroptions = []
            indicator = super()._from_json(v, Indicator)
            for indicatoroption in indicator.indicatorInterface:
                indicatoroptions.append(super()._from_json(indicatoroption, IndicatorOption))
            indicator.indicatorInterface = indicatoroptions
            indicators[k] = indicator

        for k, v in botinitial.safeties.items():
            safetyoptions = []
            safety = super()._from_json(v, Safety)
            for safetyoption in safety.safetyInterface:
                safetyoptions.append(super()._from_json(safetyoption, IndicatorOption))
            safety.safetyInterface = safetyoptions
            safeties[k] = safety

        for k, v in botinitial.insurances.items():
            insuranceoptions = []
            insurance = super()._from_json(v, Insurance)
            for insuranceoption in insurance.insuranceInterface:
                insuranceoptions.append(super()._from_json(insuranceoption, IndicatorOption))
            insurance.insuranceInterface = insuranceoptions
            insurances[k] = insurance

        botinitial.indicators = indicators
        botinitial.safeties = safeties
        botinitial.insurances = insurances

        return botinitial

    def get_all_trade_bots(self):
        """ Returns all trade bots created

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result List[:class:`~haasomeapi.dataobjects.tradebot.TradeBot`]
        """

        response = super()._execute_request("/AllTradeBots", {})

        bots = []

        for bot in response["Result"]:

            bots.append(self._convert_json_bot_to_trade_bot_object(bot))

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bots)
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def get_trade_bot(self, botguid: str):
        """ Returns trade bot matching guid

        :param botguid: str: the bot guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = self.get_all_trade_bots()

        if response.errorCode != EnumErrorCode.SUCCESS:
            return HaasomeClientResponse(response.errorCode, response.errorMessage, {})

        for bot in response.result:
            if bot.guid == botguid:
                return HaasomeClientResponse(EnumErrorCode.SUCCESS, "", bot)

        return HaasomeClientResponse(EnumErrorCode.BOT_DOSENOT_EXIT, "Bot Could Not Be Found", {})

    def activate_trade_bot(self, botguid: str):
        """ Activates a trade bot

        :param botguid: str: Trade bot guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result bool: If activation was successful
        """

        response = super()._execute_request("/ActivateTradeBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def deactivate_trade_bot(self, botguid: str):
        """ Deactivates a trade bot

        :param botguid: str: Trade bot guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result bool: If activation was successful
        """

        response = super()._execute_request("/DeactivateBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def new_trade_bot(self, accountguid: str, botname: str, primarycoin: str, secondarycoin: str, contractname: str,
                leverage: float, groupid: str):
        """ Create a new trade bot

        :param accountguid: str: Account guid
        :param botname: str: Name for the new custom bot
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str: Contract name (Optional)
        :param leverage: float: Leverage percentage to use (Optional)
        :param groupid: str: Group id for bot (Optional)

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/NewTradeBot",
                                            {"botName": botname,
                                             "accountGuid": accountguid,
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "contractName": contractname,
                                             "leverage": float(str(leverage).replace(',', '.')),
                                             "groupId": groupid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], TradeBot))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def remove_trade_bot(self, botguid: str):
        """ Removes (deletes) Trade bot

        :param botguid: str: Trade bot guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result bool: If removal was succesfull
        """

        response = super()._execute_request("/RemoveTradeBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def clean_trade_bot(self, botguid: str):
        """ Clears Trade bot history

        :param botguid: str: Custom bot guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/CleanTradeBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def lock_trade_bot(self, botguid: str, lockbot: bool):
        """ Locks a Trade bot

        :param botguid: str: Trade bot guid
        :param lockbot: bool: Lock bot

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result bool: If removal was succesfull
        """

        response = super()._execute_request("/LockTradeBot",  {"botGuid": botguid, "lockBot": str(lockbot).lower()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def backtest_trade_bot(self, botguid: str, minutes: int):
        """ Backtest a Trade bot (Note: This function will will make a request to the exchange so don't call to often)

        :param botguid: str: Custom bot guid
        :param minutestotest: int: Amount of minutes to test in the past

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Tradebot object
        """

        endUnix =  int(datetime.datetime.utcnow().timestamp())
        startUnix = endUnix - (minutes * 60)

        response = super()._execute_request("/BackTestTradeBot",  {"botGuid": botguid,
                                                                   "startUnix": str(startUnix),
                                                                   "endUnix": str(endUnix)})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def backtest_trade_bot_unix_time(self, botguid: str, startUnix: int, endUnix: int):
        """ Backtest a Trade bot (Note: This function will make a request to the exchange so don't call to often)

        :param botguid: str: Custom bot guid
        :param startunix: int: Start time in unix time notation
        :param endunix: int: End time in unix time notation

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade bot object
        """
        response = super()._execute_request("/BackTestTradeBot",  {"botGuid": botguid,
                                                                   "startUnix": str(startUnix),
                                                                   "endUnix": str(endUnix)})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_trade_bot(self, accountguid: str, botguid: str, botname: str, primarycoin: str, secondarycoin: str,
                        contractname: str, leverage: float, groupid: str, useconsensus: bool, copymarketstoelements: bool):
        """ Modify a trade bot

        :param accountguid: str: Account guid
        :param botname: str: Name for the new custom bot
        :param botguid: str: Trade bot guid to modify
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str: Contract name (Optional)
        :param leverage: float: Leverage percentage to use (Optional)
        :param groupid: str: Group id for bot (Optional)
        :param useconsensus: bool: Use consensus mode
        :param copymarketstoelements: bool: Copy markets to elements

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade bot object
        """

        response = super()._execute_request("/SetupSpotBotTradeAmount",  {"botGuid": botguid,
                                                                          "botName": botname,
                                                                          "accountGuid": accountguid,
                                                                          "primaryCoin": primarycoin,
                                                                          "secondaryCoin": secondarycoin,
                                                                          "contractName": contractname,
                                                                          "leverage": float(str(leverage).replace(',', '.')),
                                                                          "groupId": groupid,
                                                                          "useConsensus": str(useconsensus).lower(),
                                                                          "copyMarketToElements": str(copymarketstoelements).lower()})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_spot_bot_trade_amount(self, botguid: str, coinposition: EnumCoinPosition, tradeamount: float,
                                    lastbuyprice: float, lastsellprice: float, buytemplateid: str, selltemplateid: str,
                                    highspeedenabled: bool, allin: bool, ordertimeout: int, templatetimeout: int,
                                    maxtradeamount: bool, limitordertype: EnumLimitOrderPriceType, usehiddenorders: bool, fee: float):
        """ Modify spot trade bot amount

        :param botguid: str: Trade bot guid to modify
        :param coinposition: :class:`~haasomeapi.enums.EnumCoinPosition`: Coin position
        :param tradeamount: float: Trade Amount
        :param lastbuyprice: float: Last buy price
        :param lastsellprice: float: Last sell price
        :param buytemplateid: str: Buy template guid
        :param selltemplateid: str: Sell template guid
        :param highspeedenabled: bool: High speed enabled
        :param allin: bool: All in trades
        :param ordertimeout: int: Order timeout in minutes
        :param templatetimeout: int: Template timeout in minutes
        :param maxtradeamount: bool: Use max trade amount
        :param limitordertype: :class:`~EnumLimitOrderPriceType`: Limit order type
        :param usehiddenorders: bool: Use hidden orders
        :param fee: float: Fee percentage to be used in calculations

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade bot object
        """

        response = super()._execute_request("/SetupSpotBotTradeAmount",  {"botGuid": botguid,
                                                                          "coinPosition": EnumCoinPosition(coinposition).name.capitalize(),
                                                                          "tradeAmount": float(str(tradeamount).replace(',', '.')),
                                                                          "lastBuyPrice": float(str(lastbuyprice).replace(',', '.')),
                                                                          "lastSellPrice": float(str(lastsellprice).replace(',', '.')),
                                                                          "buyTemplateId": buytemplateid,
                                                                          "sellTemplateId": selltemplateid,
                                                                          "highSpeedEnabled": str(highspeedenabled).lower(),
                                                                          "allIn": str(allin).lower(),
                                                                          "orderTimeout": str(ordertimeout),
                                                                          "templateTimeout": templatetimeout,
                                                                          "maxTradeAmount": str(maxtradeamount).lower(),
                                                                          "limitOrderType": EnumLimitOrderPriceType(limitordertype).name.capitalize(),
                                                                          "useHiddenOrders": str(usehiddenorders).lower(),
                                                                          "fee": float(str(fee).replace(',', '.'))})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_leverage_bot_trade_amount(self, botguid: str, coinposition: EnumFundPosition , tradeamount: float,
                                        lastlongprice: float, lastshortprice: float, entertemplateid: str, exittemplateid: str,
                                        highspeedenabled: bool, allin: bool, ordertimeout: int, templatetimeout: int,
                                        maxtradeamount: bool, limitordertype: EnumLimitOrderPriceType, usehiddenorders: bool, fee: float):
        """ Modify leverage/margin trade bot amount

        :param botguid: str: Trade bot guid to modify
        :param coinposition: :class:`~haasomeapi.enums.EnumCoinPosition`: Coin position
        :param tradeamount: float: Trade Amount
        :param lastlongprice: float: Last long price
        :param lastshortprice: float: Last short price
        :param entertemplateid: str: Enter template guid
        :param exittemplateid: str: Exit template guid
        :param highspeedenabled: bool: High speed enabled
        :param allin: bool: All in trades
        :param ordertimeout: int: Order timeout in minutes
        :param templatetimeout: int: Template timeout in minutes
        :param maxtradeamount: bool: Use max trade amount
        :param limitordertype: :class:`~EnumLimitOrderPriceType`: Limit order type
        :param usehiddenorders: bool: Use hidden orders
        :param fee: float: Fee percentage to be used in calculations

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade bot object
        """

        response = super()._execute_request("/SetupLeverageBotTradeAmount", {"botGuid": botguid,
                                                                             "fundsPosition": EnumFundPosition(coinposition).name.capitalize(),
                                                                             "tradeAmount": float(str(tradeamount).replace(',', '.')),
                                                                             "lastLongPrice": float(str(lastlongprice).replace(',', '.')),
                                                                             "lastShortPrice": float(str(lastshortprice).replace(',', '.')),
                                                                             "enterTemplateId": entertemplateid,
                                                                             "exitTemplateId": exittemplateid,
                                                                             "highSpeedEnabled": str(highspeedenabled).lower(),
                                                                             "allIn": str(allin).lower(),
                                                                             "orderTimeout": str(ordertimeout),
                                                                             "templateTimeout": templatetimeout,
                                                                             "maxTradeAmount": str(maxtradeamount).lower(),
                                                                             "limitOrderType": EnumLimitOrderPriceType(limitordertype).name.capitalize(),
                                                                             "useHiddenOrders": str(usehiddenorders).lower(),
                                                                             "fee": float(str(fee).replace(',', '.'))})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def add_safety(self, botguid: str, safetytype: EnumSafety):
        """ Add Safety to trade bot

        :param botguid: str: Trade bot guid to modify
        :param safetytype: :class:`~haasomeapi.enums.EnumSafety`:  Safety type

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/AddSafety",  {"botGuid": botguid,
                                                            "safetyType": EnumSafety(safetytype).name.capitalize()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def add_indicator(self, botguid: str, indicatortype: EnumIndicator):
        """ Add Indicator to trade bot

        :param botguid: str: Trade bot guid to modify
        :param indicatortype: :class:`~haasomeapi.enums.EnumIndicator`:  Indicator type

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/AddIndicator",  {"botGuid": botguid,
                                                               "indicatorType": EnumSafety(indicatortype).name.capitalize()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def add_insurance(self, botguid: str, insurancetype: EnumInsurance):
        """ Add Insurance to trade bot

        :param botguid: str: Trade bot guid to modify
        :param insturancetype: :class:`~haasomeapi.enums.EnumInsurance`:  Insurance type

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/AddInsurance",  {"botGuid": botguid,
                                                               "indicatorType": EnumInsurance(insurancetype).name.capitalize()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def remove_safety(self, botguid: str, elementguid: str):
        """ Remove Safety from trade bot

        :param botguid: str: Trade bot guid to modify
        :param elementguid: str: The element guid to remove

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/RemoveSafety",  {"botGuid": botguid,
                                                               "elementGuid": elementguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def remove_indicator(self, botguid: str, elementguid: str):
        """ Remove Indicator from trade bot

        :param botguid: str: Trade bot guid to modify
        :param elementguid: str: The element guid to remove

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/RemoveIndicator",  {"botGuid": botguid,
                                                                  "elementGuid": elementguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def remove_insurance(self, botguid: str, elementguid: str):
        """ Remove Insurance from trade bot

        :param botguid: str: Trade bot guid to modify
        :param elementguid: str: The element guid to remove

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/RemoveInsurance",  {"botGuid": botguid,
                                                                  "elementGuid": elementguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_indicator(self, botguid: str, elementguid: str, pricesource: EnumPriceSource, primarycoin: str,
                        secondarycoin: str, contractname: str, interval: int, charttype: EnumPriceChartType, delay: int):
        """ Modify trade bot indicator

        :param botguid: str: Trade bot guid to modify
        :param elementguid: str: Element guid to modify
        :param pricesource: :class:`~haasomeapi.enums.EnumPriceSource`: Price Source (Exchange) for indicator to use
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str: Contract name (Optional)
        :param interval: int: Interval in minutes
        :param pricesource: :class:`~haasomeapi.enums.EnumPriceChartType`: Price Chart for indicator to use
        :param delay: int: Delay in minutes

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/SetupTradeBotIndicator",  {"botGuid": botguid,
                                                                         "elementGuid": elementguid,
                                                                         "priceSourceName":EnumPriceSource(pricesource).name.capitalize(),
                                                                         "primaryCoin": primarycoin,
                                                                         "secondaryCoin": secondarycoin,
                                                                         "contractName": contractname,
                                                                         "interval": float(str(interval).replace(',', '.')),
                                                                         "delay": delay,
                                                                         "priceChartType": EnumPriceChartType(charttype).name.capitalize()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_safety(self, botguid: str, elementguid: str, pricesource: EnumPriceSource, primarycoin: str,
                     secondarycoin: str, contractname: str, mappedbuysignal: EnumFundPosition , mappedsellsignal: EnumFundPosition, 
                     validpositionsignal: EnumSafetyPositionSignal):
        """ Modify trade bot safety

        :param botguid: str: Trade bot guid to modify
        :param elementguid: str: Element guid to modify
        :param pricesource: :class:`~haasomeapi.enums.EnumPriceSource`: Price Source (Exchange) for indicator to use
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str: Contract name (Optional)
        :param mappedbuysignal: :class:`~haasomeapi.enums.EnumFundPosition`: Mapped buy signal position
        :param mappedsellsignal: :class:`~haasomeapi.enums.EnumFundPosition`: Mapped sell signal position
        :param validpositionsignal: :class:`~haasomeapi.enums.EnumSafetyPositionSignal`: Mapped Position Signal

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/SetupTradeBotSafety",  {"botGuid": botguid,
                                                                      "elementGuid": elementguid,
                                                                      "priceSourceName":EnumPriceSource(pricesource).name.capitalize(),
                                                                      "primaryCoin": primarycoin,
                                                                      "secondaryCoin": secondarycoin,
                                                                      "contractName": contractname,
                                                                      "mappedBuySignal": EnumFundPosition(mappedbuysignal).name.capitalize(),
                                                                      "mappedSellSignal": EnumFundPosition(mappedsellsignal).name.capitalize(),
                                                                      "validPositionSignal": EnumSafetyPositionSignal(validpositionsignal).value
                                                                      })

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_indicator_spot_signals(self, botguid: str, elementguid: str, usebuysignal: bool, usesellsignal: bool,
                                     reversesignals: bool, standalone: bool):
        """ Modify indicator spot signal

        :param botguid: str: Trade bot guid to modify
        :param elementguid: str: Element guid to modify
        :param usebuysignal: bool: Use buy signal
        :param usesellsignal: bool: Use sell signal
        :param reversesignals: bool: Reverse Signals
        :param standalone: bool: Stand alone

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/SetupTradeBotIndicatorSpotSignals",  {"botGuid": botguid,
                                                                                    "elementGuid": elementguid,
                                                                                    "useBuySignal": str(usebuysignal).lower(),
                                                                                    "useSellSignal": str(usesellsignal).lower(),
                                                                                    "reverseSignals": str(reversesignals).lower(),
                                                                                    "standAlone": str(standalone).lower()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_indicator_leverage_signals(self, botguid: str, elementguid: str, uselongsignals: bool, useshortsignals: bool,
                                         usenopositionsignals: bool, reversesignals: bool, standalone: bool,
                                         mappedbuysignal: EnumFundPosition , mappedsellsignal: EnumFundPosition):
        """ Modify indicator leverage signals

        :param botguid: str: Trade bot guid to modify
        :param elementguid: str: Element guid to modify
        :param uselongsignals: bool: Use long signals
        :param useshortsignals: bool: Use short signals
        :param usenopositionsignals: bool: Use no position signals
        :param reversesignals: bool: Reverse signals
        :param standalone: bool: Stand alone
        :param mappedbuysignal: :class:`~haasomeapi.enums.EnumFundPosition`: Mapped buy signal position
        :param mappedsellsignal: :class:`~haasomeapi.enums.EnumFundPosition`: Mapped sell signal position

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/SetupTradeBotIndicatorLeverageSignals",  {"botGuid": botguid,
                                                                                        "elementGuid": elementguid,
                                                                                        "useLongSignals": str(uselongsignals).lower(),
                                                                                        "useShortSignals": str(useshortsignals).lower(),
                                                                                        "useNoPositionSignals": str(usenopositionsignals).lower(),
                                                                                        "reverseSignals": str(reversesignals).lower(),
                                                                                        "standAlone": str(standalone).lower(),
                                                                                        "mappedLongSignal": EnumFundPosition(mappedbuysignal).name.capitalize(),
                                                                                        "mappedShortSignal": EnumFundPosition(mappedsellsignal).name.capitalize()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def edit_bot_indicator_settings(self, botguid: str, elementguid: str, fieldno: int, value: any):
        """ Edit trade bot indicator setting

        :param botguid: str: Trade bot guid to modify
        :param elementguid: str: Element guid to modify
        :param fieldno: int: Field Number to modify
        :param value: any: Value for field

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/EditTradeBotIndicatorSetting",  {"botGuid": botguid,
                                                                               "elementGuid": elementguid,
                                                                               "fieldNo": fieldno,
                                                                               "value": value})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def edit_bot_safety_settings(self, botguid: str, elementguid: str, fieldno: int, value: any):
        """ Edit trade bot safety setting

        :param botguid: str: Trade bot guid to modify
        :param elementguid: str: Element guid to modify
        :param fieldno: int: Field Number to modify
        :param value: any: Value for field

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/EditTradeBotSafetySetting",  {"botGuid": botguid,
                                                                            "elementGuid": elementguid,
                                                                            "fieldNo": fieldno,
                                                                            "value": value})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def edit_bot_insurance_settings(self, botguid: str, elementguid: str, fieldno: int, value: any):
        """ Edit trade bot insurance setting

        :param botguid: str: Trade bot guid to modify
        :param elementguid: str: Element guid to modify
        :param fieldno: int: Field Number to modify
        :param value: any: Value for field

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/EditTradeBotInsuranceSetting",  {"botGuid": botguid,
                                                                               "elementGuid": elementguid,
                                                                               "fieldNo": fieldno,
                                                                               "value": value})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def switch_coin_positions(self, botguid: str, position: EnumCoinPosition):
        """ Switch trade bots coin position (Spot Market)

        :param botguid: str: Trade bot guid to modify
        :param position: :class:`~haasomeapi.enums.EnumFundPosition`: Coin position to change to

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/SwitchTradeBotCoinPositions",  {"botGuid": botguid,
                                                                              "position": EnumCoinPosition(position).name.capitalize()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def switch_bot_funds_position(self, botguid: str, position: EnumFundPosition):
        """ Switch trade bots funds position (Leverage/Margin Market)

        :param botguid: str: Trade bot guid to modify
        :param position: :class:`~haasomeapi.enums.EnumFundPosition`: Fund position to change to

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/SwitchTradeBotFundsPositions",  {"botGuid": botguid,
                                                                               "fundsPosition": EnumFundPosition(position).name.capitalize()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def switch_bot_coin_position_with_order(self, botguid: str, templateguid: str):
        """ Switch trade bot coin poisiton with order (Spot Market)

        :param botguid: str: Trade bot guid to modify
        :param templateguid: str: Order template guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/SwitchTradeBotCoinPositionsWithOrder",  {"botGuid": botguid,
                                                                                       "templateGuid": templateguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def switch_bot_funds_position_with_order(self, botguid: str, templateguid: str, targetposition: EnumFundPosition ):
        """ Switch trade bot coin poisiton with order (Leverage/Margin Market)

        :param botguid: str: Trade bot guid to modify
        :param templateguid: str: Order template guid
        :param targetposition: :class:`~haasomeapi.enums.EnumFundPosition`: Fund position to change to

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/SwitchTradeBotFundsPositionsWithOrder",  {"botGuid": botguid,
                                                                                        "templateGuid": templateguid,
                                                                                        "fundsPosition": EnumFundPosition(targetposition).name.capitalize()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def clone_trade_bot(self, accountguid: str, botguid: str, botname: str, primarycoin: str, secondarycoin: str,
                        contractname: str, leverage: float, copysafeties: bool, copyindicators: bool, copyinsurances: bool,
                        copyparameters: bool, copymarkettoelements: bool):
        """ Clone Trade Bot

        :param accountguid: str: Account guid
        :param botguid: str: Trade bot guid to modify
        :param botname: str: Name for the new custom bot
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str: Contract name (Optional)
        :param leverage: float: Leverage percentage to use (Optional)
        :param copysafeties: bool:  Copy Safeties
        :param copyindicators: bool: Copy indicators
        :param copyinsurances: bool:  Copy insurances
        :param copyparameters: bool:  Copy parameters
        :param copymarkettoelements: bool: Copy market to elements

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/CloneTradeBot",  {"botGuid": botguid,
                                                                "botName": botname,
                                                                "accountGuid": accountguid,
                                                                "primaryCoin": primarycoin,
                                                                "secondaryCoin": secondarycoin,
                                                                "contractName": contractname,
                                                                "leverage": float(str(leverage).replace(',', '.')),
                                                                "copySafeties": str(copysafeties).lower(),
                                                                "copyIndicators": str(copyindicators).lower(),
                                                                "copyInsurances": str(copyinsurances).lower(),
                                                                "copyParameters": str(copyparameters).lower(),
                                                                "copyMarketToElements": str(copymarkettoelements).lower()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def clone_indicator(self, botguid: str, elementguid: str, tobotguid: str):
        """ Clone Indicator

        :param botguid: str: Trade bot guid to copy from
        :param elementguid: str: Element Guid to copy
        :param tobotguid: str: Trade bot guid to copy to

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/CloneIndicator",  {"botGuid": botguid,
                                                                 "elementGuid": elementguid,
                                                                 "toBotGuid": tobotguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def clone_safety(self, botguid: str, elementguid: str, tobotguid: str):
        """ Clone Safety

        :param botguid: str: Trade bot guid to copy from
        :param elementguid: str: Element Guid to copy
        :param tobotguid: str: Trade bot guid to copy to

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/CloneSafety",  {"botGuid": botguid,
                                                              "elementGuid": elementguid,
                                                              "toBotGuid": tobotguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def clone_insurance(self, botguid: str, elementguid: str, tobotguid: str):
        """ Clone Insurance

        :param botguid: str: Trade bot guid to copy from
        :param elementguid: str: Element Guid to copy
        :param tobotguid: str: Trade bot guid to copy to

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.tradebot.TradeBot`: Trade Bot
        """

        response = super()._execute_request("/CloneInsurance",  {"botGuid": botguid,
                                                                 "elementGuid": elementguid,
                                                                 "toBotGuid": tobotguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})
