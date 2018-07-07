import json

from typing import List
from haasomeapi.apis.ApiBase import ApiBase
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder

from haasomeapi.enums.EnumOrderType import EnumOrderType
from haasomeapi.enums.EnumCurrencyType import EnumCurrencyType
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haasomeapi.enums.EnumMadHatterSafeties import EnumMadHatterSafeties
from haasomeapi.enums.EnumFlashSpreadOptions import EnumFlashSpreadOptions
from haasomeapi.enums.EnumMadHatterIndicators import EnumMadHatterIndicators
from haasomeapi.enums.EnumOrderBotTriggerType import EnumOrderBotTriggerType
from haasomeapi.enums.EnumAccumulationBotStopType import EnumAccumulationBotStopType

from haasomeapi.dataobjects.custombots.EmailBot import EmailBot
from haasomeapi.dataobjects.custombots.OrderBot import OrderBot
from haasomeapi.dataobjects.custombots.ScriptBot import ScriptBot
from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.custombots.FlashCrashBot import FlashCrashBot
from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot
from haasomeapi.dataobjects.custombots.CryptoIndexBot import CryptoIndexBot
from haasomeapi.dataobjects.custombots.AccumulationBot import AccumulationBot
from haasomeapi.dataobjects.custombots.MarketMakingBot import MarketMakingBot
from haasomeapi.dataobjects.custombots.ZoneRecoveryBot import ZoneRecoveryBot
from haasomeapi.dataobjects.custombots.InterExchangeArbitrageBot import InterExchangeArbitrageBot

from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse
from haasomeapi.dataobjects.custombots.dataobjects.EmailBotAction import EmailBotAction
from haasomeapi.dataobjects.custombots.dataobjects.CryptoIndexBotIndexSaveObject import CryptoIndexBotIndexSaveObject


class CustomBotApi(ApiBase):
    """ The Custom Bot API Class.
    Gives access to the Custom Bot api endpoints

    :param connectionstring: str: Connection String Formatted Ex. http://127.0.0.1:9000
    :param privatekey: str: Private Key Set In The Haas Settings
    """

    def __init__(self, connectionstring: str, privatekey: str):
        ApiBase.__init__(self, connectionstring, privatekey)

    def _convert_json_bot_to_custom_bot_object(self, jsonstr: str):
        """ Internal function to easily convert json strings to BaseCustomBot objects
        :param jsonstr: str: 

        :returns: :class:`~haasomeapi.dataobjects.custombots.BaseCustomBot`
        """

        botinitial = super()._from_json(jsonstr, BaseCustomBot)

        orders = []

        for corder in botinitial.completedOrders:
            orders.append(super()._from_json(corder, BaseOrder))

        botinitial.completedOrders = orders

        return botinitial

    def _convert_json_bot_to_custom_bot_specific(self, bottype: EnumCustomBotType, jsonstr: str):
        """ Internal function to easily convert json strings to specific custom bot objects
        :param bottype: :class:`~haasomeapi.enums.EnumCustomBotType`
        :param jsonstr: str: 
        :returns: any: Returns a Class Instance of bottype specified
        """

        botinitial = None

        if bottype == EnumCustomBotType.BASE_CUSTOM_BOT:
            botinitial = super()._from_json(jsonstr, BaseCustomBot)
        if bottype == EnumCustomBotType.MARKET_MAKING_BOT:
            botinitial = super()._from_json(jsonstr, MarketMakingBot)
        if bottype == EnumCustomBotType.PING_PONG_BOT:
            botinitial = super()._from_json(jsonstr, BaseCustomBot)
        if bottype == EnumCustomBotType.SCALPER_BOT:
            botinitial = super()._from_json(jsonstr, ScalperBot)
        if bottype == EnumCustomBotType.ORDER_BOT:
            botinitial = super()._from_json(jsonstr, OrderBot)
        if bottype == EnumCustomBotType.FLASH_CRASH_BOT:
            botinitial = super()._from_json(jsonstr, FlashCrashBot)
        if bottype == EnumCustomBotType.INTER_EXCHANGE_ARBITRAGE_BOT:
            botinitial = super()._from_json(jsonstr, InterExchangeArbitrageBot)
        if bottype == EnumCustomBotType.INTELLIBOT_ALICE_BOT:
            botinitial = super()._from_json(jsonstr, BaseCustomBot)
        if bottype == EnumCustomBotType.ZONE_RECOVERY_BOT:
            botinitial = super()._from_json(jsonstr, ZoneRecoveryBot)
        if bottype == EnumCustomBotType.ACCUMULATION_BOT:
            botinitial = super()._from_json(jsonstr, AccumulationBot)
        if bottype == EnumCustomBotType.TREND_LINES_BOT:
            botinitial = super()._from_json(jsonstr, BaseCustomBot)
        if bottype == EnumCustomBotType.MAD_HATTER_BOT:
            botinitial = super()._from_json(jsonstr, MadHatterBot)
        if bottype == EnumCustomBotType.SCRIPT_BOT:
            botinitial = super()._from_json(jsonstr, ScriptBot)
        if bottype == EnumCustomBotType.CRYPTO_INDEX_BOT:
            botinitial = super()._from_json(jsonstr, CryptoIndexBot)
        if bottype == EnumCustomBotType.HAAS_SCRIPT_BOT:
            botinitial = super()._from_json(jsonstr, ScriptBot)
        if bottype == EnumCustomBotType.EMAIL_BOT:
            botinitial = super()._from_json(jsonstr, EmailBot)

        orders = []

        for corder in botinitial.completedOrders:
            orders.append(super()._from_json(corder, BaseOrder))

        botinitial.completedOrders = orders

        return botinitial

    def _convert_index_list_to_json(self, index: List[CryptoIndexBotIndexSaveObject]):
        """ Internal fucntion to converts a CryptoIndexBotIndexSaveObject list to a json string

        :param index: List[CryptoIndexBotIndexSaveObject]: 

        :returns: str: Json string representation of specified list
        """
        index_fixed = []

        for i in index:
            index_fixed.append({"coin": i.coin, "amount": i.amount, "buyThreshold": i.buyThreshold,
                                "sellThreshold": i.sellThreshold, "stopLoss": i.stopLoss})

        return json.dumps(index_fixed, sort_keys=True)

    def _convert_emails_list_to_json(self, actions: List[EmailBotAction]):
        """ Internal fucntion to converts a EmailBotAction list to a json string

        :param actions: List[EmailBotAction]: 

        :returns: str: Json string representation of the specified list

        """

        actions_fixed = []

        for i in actions:
            messages_tmp = []
            for m in i.messages:
                messages_tmp.append({"message": m.message, "lastReceivedTime": m.lastReceivedTime})

            actions_fixed.append({"guid": i.guid, "providedGuid": i.providerGuid, "messages": messages_tmp,
                                  "timeoutInSeconds": i.timeoutInSeconds, "spotAction": i.spotAction,
                                  "leverageAction": i.leverageAction})

        return json.dumps(actions_fixed, sort_keys=True)



    def get_all_custom_bots(self):
        """ Returns all custom bots created

        :returns: List[:class:`~haasomeapi.dataobjects.custombots.BaseCustomBot`]
        """
        response = super()._execute_request("/AllCustomBots", {})

        bots = []

        for bot in response["Result"]:

            bots.append(self._convert_json_bot_to_custom_bot_object(bot))

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bots)
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def get_custom_bot(self,  botguid: str, bottype: EnumCustomBotType):
        """ Returns custom bot matching bot guid

        :param botguid: str: the bot 
        :param bottype: :class:`~haasomeapi.enums.EnumCustomBotType`: Type of bot to return 

        :returns: any: Specified bottype object

        """

        response = super()._execute_request("/GetCustomBot", {"botGuid": botguid})


        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(bottype, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def activate_custom_bot(self, botguid: str, withextra: bool):
        """ Activates a custom bot

        :param botguid: str: Bot guid
        :param withextra: bool: with extra

        :returns: bool: If activation was successful

        """
        response = super()._execute_request("/ActivateCustomBot",  {"botGuid": botguid, "extra": str(withextra).lower()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def deactivate_custom_bot(self, botguid: str, withextra: bool):
        """ Deactivates a custom bot

        :param botguid: str: Bot guid
        :param withextra: bool: with extra

        :returns: bool: If deactivation was successful

        """
        response = super()._execute_request("/DeactivateCustomBot",  {"botGuid": botguid, "extra": str(withextra).lower()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def new_custom_bot(self, accountguid: str, bottype: EnumCustomBotType, botname: str, primarycoin: str,
                       secondarycoin: str, contractname: str):
        """ Create a new custom bot

        :param accountguid: str: Account guid
        :param bottype: :class:`~haasomeapi.enums.EnumCustomBotType`: The bottype to create 
        :param botname: str: Name for the new custom bot
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str: Contract name (Optional)

        :returns: any: Specified bot type object

        """

        response = super()._execute_request("/GetCustomBot", {"botType": EnumCustomBotType(bottype).name.capitalize(),
                                                              "botName": botname,
                                                              "accountGuid": accountguid,
                                                              "primaryCoin": primarycoin,
                                                              "secondaryCoin": secondarycoin,
                                                              "contractName": contractname})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(bottype, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def new_custom_bot_from_market(self, accountguid: str, bottype: EnumCustomBotType, botname: str, market: Market):
        """ Create a new custom bot from market object

        :param accountguid: str: Account guid
        :param bottype: :class:`~haasomeapi.enums.EnumCustomBotType`: The bottype to create 
        :param botname: str: Name for the new custom bot
        :parama market: :class:`~haasomeapi.dataobjects.marketdata.Market`: Market object to use

        :returns: any: Specified bot type object

        """

        response = super()._execute_request("/GetCustomBot", {"botType": EnumCustomBotType(bottype).name.capitalize(),
                                                              "botName": botname,
                                                              "accountGuid": accountguid,
                                                              "primaryCoin": market.primaryCurrency,
                                                              "secondaryCoin": market.secondaryCurrency,
                                                              "contractName": market.contractName})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(bottype, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def remove_custom_bot(self, botguid: str):
        """

        :param botguid: str: 

        """
        response = super()._execute_request("/RemoveCustomBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def clear_custom_bot(self, botguid: str):
        """

        :param botguid: str: 

        """
        response = super()._execute_request("/ClearCustomBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.BASE_CUSTOM_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def clear_custom_bot_specific(self, bottype: EnumCustomBotType, botguid: str):
        """

        :param bottype: EnumCustomBotType: 
        :param botguid: str: 

        """
        response = super()._execute_request("/ClearCustomBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(bottype, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def backtest_custom_bot(self, botguid: str, minutestotest: int):
        """

        :param botguid: str: 
        :param minutestotest: int: 

        """
        response = super()._execute_request("/BacktestCustomBot",  {"botGuid": botguid, "minutesToTest": minutestotest})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.BASE_CUSTOM_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def backtest_custom_bot_unix_time(self, botguid: str, startunix: int, endunix: int):
        """

        :param botguid: str: 
        :param startunix: int: 
        :param endunix: int: 

        """
        response = super()._execute_request("/BacktestCustomBot",  {"botGuid": botguid, "startUnix": startunix,
                                                                    "endunix": endunix})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.BASE_CUSTOM_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def backtest_custom_bot_on_market(self, accountguid: str, botguid: str, minutestotest: int, primarycoin: str,
                                      secondarycoin: str, contractname: str):
        """

        :param accountguid: str: 
        :param botguid: str: 
        :param minutestotest: int: 
        :param primarycoin: str: 
        :param secondarycoin: str: 
        :param contractname: str: 

        """

        response = super()._execute_request("/BacktestCustomBot",  {"botGuid": botguid,
                                                                    "minutesToTest": minutestotest,
                                                                    "accountGuid": accountguid,
                                                                    "primaryCoin": primarycoin,
                                                                    "secondaryCoin": secondarycoin,
                                                                    "contractName": contractname})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.BASE_CUSTOM_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def clone_custom_bot(self, accountguid: str, bottype: EnumCustomBotType, botguid: str, botname: str, 
                         primarycoin: str,secondarycoin: str, contractname: str, leverage: float):
        """

        :param accountguid: str: 
        :param bottype: EnumCustomBotType: 
        :param botguid: str: 
        :param botname: str: 
        :param primarycoin: str: 
        :param secondarycoin: str: 
        :param contractname: str: 
        :param leverage: float: 

        """

        response = super()._execute_request("/CloneCustomBot",  {"botGuid": botguid,
                                                                 "botName": botname,
                                                                 "accountGuid": accountguid,
                                                                 "primaryCoin": primarycoin,
                                                                 "secondaryCoin": secondarycoin,
                                                                 "contractName": contractname,
                                                                 "leverage": float(str(leverage).replace(',', '.'))})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(bottype, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def clone_custom_bot_simple(self, accountguid: str, botguid: str, botname: str):
        """

        :param accountguid: str: 
        :param botguid: str: 
        :param botname: str: 

        """

        response = super()._execute_request("/CloneCustomBotSimple",  {"botGuid": botguid,
                                                                 "botName": botname,
                                                                 "accountGuid": accountguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.BASE_CUSTOM_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_accumulation_bot(self, accountguid: str, botguid: str, botname: str, primarycoin: str, secondarycoin: str,
                               stoptype: EnumAccumulationBotStopType, stoptypevalue: float, randomordersizex: float,
                               randomordersizey: float, randomordertimex: int, randomordertimey: int,
                               direction: EnumOrderType, triggeronprice: bool, triggerwhenhigher: bool, triggervalue: float):
        """

        :param accountguid: str: 
        :param botguid: str: 
        :param botname: str: 
        :param primarycoin: str: 
        :param secondarycoin: str: 
        :param stoptype: EnumAccumulationBotStopType: 
        :param stoptypevalue: float: 
        :param randomordersizex: float: 
        :param randomordersizey: float: 
        :param randomordertimex: int: 
        :param randomordertimey: int: 
        :param direction: EnumOrderType: 
        :param triggeronprice: bool: 
        :param triggerwhenhigher: bool: 
        :param triggervalue: float: 

        """

        response = super()._execute_request("/SetupAccumulationBot",  {"botGuid": botguid,
                                                                       "botName": botname,
                                                                       "accountGuid": accountguid,
                                                                       "primaryCoin": primarycoin,
                                                                       "secondaryCoin": secondarycoin,
                                                                       "stopType": EnumAccumulationBotStopType(stoptype).name.capitalize(),
                                                                       "stopTypeValue": float(str(stoptypevalue).replace(',', '.')),
                                                                       "randomOrderSizeX": float(str(randomordersizex).replace(',', '.')),
                                                                       "randomOrderSizeY": float(str(randomordersizey).replace(',', '.')),
                                                                       "randomOrderTimeX": randomordertimex,
                                                                       "randomOrderTimeY": randomordertimey,
                                                                       "direction": EnumOrderType(direction).name.capitalize(),
                                                                       "triggerOnPrice": str(triggeronprice).lower(),
                                                                       "triggerWhenHigher": str(triggerwhenhigher).lower(),
                                                                       "triggerValue": float(str(triggervalue).replace(',', '.'))})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.ACCUMULATION_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_crypto_index_bot(self, accountguid: str, botguid: str, botname: str, templateguid: str, basecoin: str,
                               totalIndexValue: float, individualgrowth: bool, allocateprofits: bool, index: List[CryptoIndexBotIndexSaveObject] ):
        """

        :param accountguid: str: 
        :param botguid: str: 
        :param botname: str: 
        :param templateguid: str: 
        :param basecoin: str: 
        :param totalIndexValue: float: 
        :param individualgrowth: bool: 
        :param allocateprofits: bool: 
        :param index: List[CryptoIndexBotIndexSaveObject]: 

        """

        response = super()._execute_request("/SetupCryptoIndexBot",  {"botGuid": botguid,
                                                                      "botName": botname,
                                                                      "accountGuid": accountguid,
                                                                      "templateGuid": templateguid,
                                                                      "baseCoin": basecoin,
                                                                      "totalIndexValue": float(str(totalIndexValue).replace(',', '.')),
                                                                      "individualGrowth": str(individualgrowth).lower(),
                                                                      "allocateProfits": str(allocateprofits).lower(),
                                                                      "index": self._convert_index_list_to_json(index)})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.CRYPTO_INDEX_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_email_bot(self, accountguid: str, botguid: str, botname: str, primarycoin: str, secondarycoin: str,
                        contractname: str, leverage: float, tradeamount: float, fee: float, templateguid: str,
                        position: str, actions: List[EmailBotAction], stoploss: float, minchangetobuy: float,
                        minchangetosell: float):
        """

        :param accountguid: str: 
        :param botguid: str: 
        :param botname: str: 
        :param primarycoin: str: 
        :param secondarycoin: str: 
        :param contractname: str: 
        :param leverage: float: 
        :param tradeamount: float: 
        :param fee: float: 
        :param templateguid: str: 
        :param position: str: 
        :param actions: List[EmailBotAction]: 
        :param stoploss: float: 
        :param minchangetobuy: float: 
        :param minchangetosell: float: 

        """

        response = super()._execute_request("/SetupEmailBot",  {"botGuid": botguid,
                                                                "botName": botname,
                                                                "accountGuid": accountguid,
                                                                "primaryCoin": primarycoin,
                                                                "secondaryCoin": secondarycoin,
                                                                "contractName": contractname,
                                                                "leverage": float(str(leverage).replace(',', '.')),
                                                                "tradeAmount": float(str(tradeamount).replace(',', '.')),
                                                                "fee": float(str(fee).replace(',', '.')),
                                                                "templateGuid": templateguid,
                                                                "position": position,
                                                                "emails": self._convert_emails_list_to_json(actions),
                                                                "stopLoss": float(str(stoploss).replace(',', '.')),
                                                                "minChangeToBuy": float(str(minchangetobuy).replace(',', '.')),
                                                                "minChangeToSell": float(str(minchangetosell).replace(',', '.'))})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.EMAIL_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_flash_crash_bot(self, accountguid: str, botguid: str, botname: str, primarycoin: str, secondarycoin: str,
                              fee: float, baseprice: float,  priceSpreadType: EnumFlashSpreadOptions, pricespread: float,
                              percentageboost: float, minpercentage: float, maxpercentage: float, amounttype: EnumCurrencyType,
                              amountspread: float, buyamount: float, sellamount: float, refilldelay: int, safetyenabled: bool,
                              safetytriggerlevel: float, safetymoveinout: bool, followthetrend: bool, followthetrendchannelrange: int,
                              followthetrendchanneloffset: int, followthetrendtimeout: int):
        """

        :param accountguid: str: 
        :param botguid: str: 
        :param botname: str: 
        :param primarycoin: str: 
        :param secondarycoin: str: 
        :param fee: float: 
        :param baseprice: float: 
        :param priceSpreadType: EnumFlashSpreadOptions: 
        :param pricespread: float: 
        :param percentageboost: float: 
        :param minpercentage: float: 
        :param maxpercentage: float: 
        :param amounttype: EnumCurrencyType: 
        :param amountspread: float: 
        :param buyamount: float: 
        :param sellamount: float: 
        :param refilldelay: int: 
        :param safetyenabled: bool: 
        :param safetytriggerlevel: float: 
        :param safetymoveinout: bool: 
        :param followthetrend: bool: 
        :param followthetrendchannelrange: int: 
        :param followthetrendchanneloffset: int: 
        :param followthetrendtimeout: int: 

        """

        response = super()._execute_request("/SetupFlashCrashBot",  {"botGuid": botguid,
                                                                     "botName": botname,
                                                                     "accountGuid": accountguid,
                                                                     "primaryCoin": primarycoin,
                                                                     "secondaryCoin": secondarycoin,
                                                                     "fee": float(str(fee).replace(',', '.')),
                                                                     "basePrice": float(str(baseprice).replace(',', '.')),
                                                                     "priceSpreadType": EnumFlashSpreadOptions(priceSpreadType).name.capitalize(),
                                                                     "priceSpread": float(str(pricespread).replace(',', '.')),
                                                                     "percentageBoost": float(str(percentageboost).replace(',', '.')),
                                                                     "minPercentage": float(str(minpercentage).replace(',', '.')),
                                                                     "maxPercentage": float(str(maxpercentage).replace(',', '.')),
                                                                     "amountType": EnumCurrencyType(amounttype).name.capitalize(),
                                                                     "amountSpread": float(str(amountspread).replace(',', '.')),
                                                                     "buyAmount": float(str(buyamount).replace(',', '.')),
                                                                     "sellAmount":  float(str(sellamount).replace(',', '.')),
                                                                     "refillDelay": refilldelay,
                                                                     "safetyEnabled": str(safetyenabled).lower(),
                                                                     "safetyTriggerLevel": safetytriggerlevel,
                                                                     "safetyMoveInOut": str(safetymoveinout).lower(),
                                                                     "fttEnabled": str(followthetrend).lower(),
                                                                     "fttRange": followthetrendchannelrange,
                                                                     "fttOffset": followthetrendchanneloffset,
                                                                     "fttTimeout": followthetrendtimeout
                                                                     })
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.FLASH_CRASH_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_inter_exchange_arbitrage_bot(self, accountguid: str, botguid: str, botname: str, primarycoin: str, secondarycoin: str,
                                           accountguid2: str, primarycoin2: str, secondarycoin2: str, tradeamount: float,
                                           triggerlevel: float, templateguid: str, maxamount: float, maxtrades: int):
        """

        :param accountguid: str: 
        :param botguid: str: 
        :param botname: str: 
        :param primarycoin: str: 
        :param secondarycoin: str: 
        :param accountguid2: str: 
        :param primarycoin2: str: 
        :param secondarycoin2: str: 
        :param tradeamount: float: 
        :param triggerlevel: float: 
        :param templateguid: str: 
        :param maxamount: float: 
        :param maxtrades: int: 

        """

        response = super()._execute_request("/SetupInterExchangeArbitrageBot",  {"botGuid": botguid,
                                                                                 "botName": botname,
                                                                                 "accountGuid": accountguid,
                                                                                 "primaryCoin": primarycoin,
                                                                                 "secondaryCoin": secondarycoin,
                                                                                 "accountGuid2": accountguid2,
                                                                                 "primaryCoin2": primarycoin2,
                                                                                 "secondaryCoin2": secondarycoin2,
                                                                                 "tradeAmount": float(str(tradeamount).replace(',', '.')),
                                                                                 "triggerLevel": float(str(triggerlevel).replace(',', '.')),
                                                                                 "templateGuid": templateguid,
                                                                                 "maxAmount": float(str(maxamount).replace(',', '.')),
                                                                                 "maxTrades": maxtrades})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.INTER_EXCHANGE_ARBITRAGE_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_intellibot_alice(self, accountguid: str, botguid: str, botname: str, primarycoin: str, secondarycoin: str,
                               contractname: str, leverage: float, tradeamount: float, fee: float):
        """

        :param accountguid: str: 
        :param botguid: str: 
        :param botname: str: 
        :param primarycoin: str: 
        :param secondarycoin: str: 
        :param contractname: str: 
        :param leverage: float: 
        :param tradeamount: float: 
        :param fee: float: 

        """

        response = super()._execute_request("/SetupIntellibotAlice",  {"botGuid": botguid,
                                                                       "botName": botname,
                                                                       "accountGuid": accountguid,
                                                                       "primaryCoin": primarycoin,
                                                                       "secondaryCoin": secondarycoin,
                                                                       "contractName": contractname,
                                                                       "leverage": float(str(leverage).replace(',', '.')),
                                                                       "tradeAmount": float(str(tradeamount).replace(',', '.')),
                                                                       "fee": float(str(fee).replace(',', '.'))})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.BASE_CUSTOM_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_market_making_bot(self, accountguid: str, botguid: str, botname: str, primarycoin: str, secondarycoin: str,
                                tradeamount: float, fee: float, offset: float, resettimeout: int, usedsecondorder: bool,
                                secondoffset: float):
        """

        :param accountguid: str: 
        :param botguid: str: 
        :param botname: str: 
        :param primarycoin: str: 
        :param secondarycoin: str: 
        :param tradeamount: float: 
        :param fee: float: 
        :param offset: float: 
        :param resettimeout: int: 
        :param usedsecondorder: bool: 
        :param secondoffset: float: 

        """

        response = super()._execute_request("/SetupMarketMakingBot",  {"botGuid": botguid,
                                                                       "botName": botname,
                                                                       "accountGuid": accountguid,
                                                                       "primaryCoin": primarycoin,
                                                                       "secondaryCoin": secondarycoin,
                                                                       "tradeAmount": float(str(tradeamount).replace(',', '.')),
                                                                       "fee": float(str(fee).replace(',', '.')),
                                                                       "priceOffset": float(str(offset).replace(',', '.')),
                                                                       "resetTimer": resettimeout,
                                                                       "useSecondOrder": str(usedsecondorder).lower(),
                                                                       "secondOrderPriceOffset": float(str(secondoffset).replace(',', '.'))})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.MARKET_MAKING_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_mad_hatter_bot(self, accountguid: str, botguid: str, botname: str, primarycoin: str, secondarycoin: str,
                             templateguid: str, position: str, fee: float, tradeamount: float, useconsensus: bool,
                             disableafterstoploss: bool, interval: int, includeincompleteinterval: bool):
        """

        :param accountguid: str: 
        :param botguid: str: 
        :param botname: str: 
        :param primarycoin: str: 
        :param secondarycoin: str: 
        :param templateguid: str: 
        :param position: str: 
        :param fee: float: 
        :param tradeamount: float: 
        :param useconsensus: bool: 
        :param disableafterstoploss: bool: 
        :param interval: int: 
        :param includeincompleteinterval: bool: 

        """

        response = super()._execute_request("/SetupMadHatterBot",  {"botGuid": botguid,
                                                                    "botName": botname,
                                                                    "accountGuid": accountguid,
                                                                    "primaryCoin": primarycoin,
                                                                    "secondaryCoin": secondarycoin,
                                                                    "tradeAmount": float(str(tradeamount).replace(',', '.')),
                                                                    "fee": float(str(fee).replace(',', '.')),
                                                                    "templateGuid": templateguid,
                                                                    "position": position,
                                                                    "useTwoSignals": str(useconsensus).lower(),
                                                                    "disableAfterStopLoss": str(disableafterstoploss).lower(),
                                                                    "interval": interval,
                                                                    "includeIncompleteInterval": str(includeincompleteinterval).lower()})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.MAD_HATTER_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_order_bot(self, accountguid: str, botguid: str, botname: str, primarycoin: str, secondarycoin: str):
        """

        :param accountguid: str: 
        :param botguid: str: 
        :param botname: str: 
        :param primarycoin: str: 
        :param secondarycoin: str: 

        """

        response = super()._execute_request("/SetupOrderBot",  {"botGuid": botguid,
                                                                    "botName": botname,
                                                                    "accountGuid": accountguid,
                                                                    "primaryCoin": primarycoin,
                                                                    "secondaryCoin": secondarycoin})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.ORDER_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_ping_pong_bot(self, accountguid: str, botguid: str, botname: str, primarycoin: str, secondarycoin: str,
                            contractbame: str, leverage: float, tradeamount: float, position: str, fee: float):
        """

        :param accountguid: str: 
        :param botguid: str: 
        :param botname: str: 
        :param primarycoin: str: 
        :param secondarycoin: str: 
        :param contractbame: str: 
        :param leverage: float: 
        :param tradeamount: float: 
        :param position: str: 
        :param fee: float: 

        """

        response = super()._execute_request("/SetupPingPongBot",  {"botGuid": botguid,
                                                                    "botName": botname,
                                                                    "accountGuid": accountguid,
                                                                    "primaryCoin": primarycoin,
                                                                    "secondaryCoin": secondarycoin,
                                                                    "contractName": contractbame,
                                                                    "leverage": float(str(leverage).replace(',', '.')),
                                                                    "tradeAmount": float(str(tradeamount).replace(',', '.')),
                                                                    "fee": float(str(fee).replace(',', '.')),
                                                                    "position": position})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.PING_PONG_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_scalper_bot(self, accountguid: str, botguid: str, botname: str, primarycoin: str, secondarycoin: str,
                          templateguid :str, contractbame: str, leverage: float, tradeamount: float, targetpercentage: float,
                          safetythreshold: float, position: str, fee: float):
        """

        :param accountguid: str: 
        :param botguid: str: 
        :param botname: str: 
        :param primarycoin: str: 
        :param secondarycoin: str: 
        :param templateguid :str: 
        :param contractbame: str: 
        :param leverage: float: 
        :param tradeamount: float: 
        :param targetpercentage: float: 
        :param safetythreshold: float: 
        :param position: str: 
        :param fee: float: 

        """

        response = super()._execute_request("/SetupScalpingBot",  {"botGuid": botguid,
                                                                   "botName": botname,
                                                                   "accountGuid": accountguid,
                                                                   "primaryCoin": primarycoin,
                                                                   "secondaryCoin": secondarycoin,
                                                                   "templateGuid": templateguid,
                                                                   "contractName": contractbame,
                                                                   "leverage": float(str(leverage).replace(',', '.')),
                                                                   "tradeAmount": float(str(tradeamount).replace(',', '.')),
                                                                   "targetPercentage": float(str(targetpercentage).replace(',', '.')),
                                                                   "safetyThreshold": float(str(safetythreshold).replace(',', '.')),
                                                                   "fee": float(str(fee).replace(',', '.')),
                                                                   "position": position})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.SCALPER_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_script_bot(self, accountguid: str, botguid: str, botname: str, primarycoin: str, secondarycoin: str,
                         templateguid :str, contractbame: str, leverage: float, tradeamount: float, fee: float,
                         position: str, scriptid: str):
        """

        :param accountguid: str: 
        :param botguid: str: 
        :param botname: str: 
        :param primarycoin: str: 
        :param secondarycoin: str: 
        :param templateguid :str: 
        :param contractbame: str: 
        :param leverage: float: 
        :param tradeamount: float: 
        :param fee: float: 
        :param position: str: 
        :param scriptid: str: 

        """

        response = super()._execute_request("/SetupScriptBot",  {"botGuid": botguid,
                                                                 "botName": botname,
                                                                 "accountGuid": accountguid,
                                                                 "primaryCoin": primarycoin,
                                                                 "secondaryCoin": secondarycoin,
                                                                 "templateGuid": templateguid,
                                                                 "contractName": contractbame,
                                                                 "leverage": float(str(leverage).replace(',', '.')),
                                                                 "tradeAmount": float(str(tradeamount).replace(',', '.')),
                                                                 "fee": float(str(fee).replace(',', '.')),
                                                                 "position": position,
                                                                 "scriptId": scriptid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.SCRIPT_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_zone_recovery_bot(self, accountguid: str, botguid: str, botname: str, primarycoin: str, secondarycoin: str,
                                contractname: str, leverage: float, tradeamount: float, maxtradeamount: float,
                                factorlong: float, factorshort: float, targetprofit: float, zone: float):
        """

        :param accountguid: str: 
        :param botguid: str: 
        :param botname: str: 
        :param primarycoin: str: 
        :param secondarycoin: str: 
        :param contractname: str: 
        :param leverage: float: 
        :param tradeamount: float: 
        :param maxtradeamount: float: 
        :param factorlong: float: 
        :param factorshort: float: 
        :param targetprofit: float: 
        :param zone: float: 

        """

        response = super()._execute_request("/SetupZoneRecoveryBot",  {"botGuid": botguid,
                                                                       "botName": botname,
                                                                       "accountGuid": accountguid,
                                                                       "primaryCoin": primarycoin,
                                                                       "secondaryCoin": secondarycoin,
                                                                       "contractName": contractname,
                                                                       "leverage": float(str(leverage).replace(',', '.')),
                                                                       "tradeAmount": float(str(tradeamount).replace(',', '.')),
                                                                       "maxTradeAmount": float(str(maxtradeamount).replace(',', '.')),
                                                                       "factorLong":  float(str(factorlong).replace(',', '.')),
                                                                       "factorShort":  float(str(factorshort).replace(',', '.')),
                                                                       "targetProfit":  float(str(targetprofit).replace(',', '.')),
                                                                       "zone":  float(str(zone).replace(',', '.'))})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.ZONE_RECOVERY_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def flash_crash_bot_quck_start(self, botguid: str):
        """

        :param botguid: str: 

        """
        response = super()._execute_request("/QuickStartFlashCrashBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def flash_crash_bot_quick_start_all(self, botguid: str):
        """

        :param botguid: str: 

        """
        response = super()._execute_request("/QuickStartAllFlashCrashBots",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def flash_crash_bot_live_edit(self, botguid: str, isbuyorder: bool, addorder: bool):
        """

        :param botguid: str: 
        :param isbuyorder: bool: 
        :param addorder: bool: 

        """
        response = super()._execute_request("/LiveOrderEditFlashCrashBot",  {"botGuid": botguid,
                                                                             "isBuyOrder": str(isbuyorder).lower(),
                                                                             "addOrder": str(addorder).lower()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.FLASH_CRASH_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def flash_crash_bot_add_buy_order(self, botguid: str):
        """

        :param botguid: str: 

        """
        return self.flash_crash_bot_live_edit(botguid, True, True)

    def flash_crash_bot_remove_buy_order(self, botguid: str):
        """

        :param botguid: str: 

        """
        return self.flash_crash_bot_live_edit(botguid, True, False)

    def flash_crash_bot_add_sell_order(self, botguid: str):
        """

        :param botguid: str: 

        """
        return self.flash_crash_bot_live_edit(botguid, False, True)

    def flash_crash_bot_remove_sell_order(self, botguid: str):
        """

        :param botguid: str: 

        """
        return self.flash_crash_bot_live_edit(botguid, False, False)

    def set_mad_hatter_indicator_parameter(self, botguid: str, type: EnumMadHatterIndicators, fieldNo: int, value: any):
        """

        :param botguid: str: 
        :param type: EnumMadHatterIndicators: 
        :param fieldNo: int: 
        :param value: any: 

        """

        response = super()._execute_request("/MadHatterSetIndicatorParameter",  {"botGuid": botguid,
                                                                                 "type": EnumMadHatterIndicators(type).name.capitalize(),
                                                                                 "fieldNo": fieldNo,
                                                                                 "value": value})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.MAD_HATTER_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def set_mad_hatter_safety_parameter(self, botguid: str, type: EnumMadHatterSafeties, value: any):
        """

        :param botguid: str: 
        :param type: EnumMadHatterSafeties: 
        :param value: any: 

        """

        response = super()._execute_request("/MadHatterSetSafetyParameter",  {"botGuid": botguid,
                                                                              "type": EnumMadHatterSafeties(type).name.capitalize(),
                                                                              "value": value})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.MAD_HATTER_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def flip_accumulation_bot(self, botguid: str):
        """

        :param botguid: str: 

        """
        response = super()._execute_request("/FlipAccumulationBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def add_order_bot_order(self, botguid: str, dependson: str, dependsonnotexecuted: str, amount: float, price: float,
                            triggerprice: float, templateguid: str,  direction: EnumOrderType, triggertype: EnumOrderBotTriggerType,):
        """

        :param botguid: str: 
        :param dependson: str: 
        :param dependsonnotexecuted: str: 
        :param amount: float: 
        :param price: float: 
        :param triggerprice: float: 
        :param templateguid: str: 
        :param direction: EnumOrderType: 
        :param triggertype: EnumOrderBotTriggerType: 

        """

        response = super()._execute_request("/OrderBotAddOrder", {"botGuid": botguid,
                                                                  "dependsOn": dependson,
                                                                  "dependsOnNotExecuted": dependsonnotexecuted,
                                                                  "amount": float(str(amount).replace(',', '.')),
                                                                  "price": float(str(price).replace(',', '.')),
                                                                  "triggerPrice": float(str(triggerprice).replace(',', '.')),
                                                                  "orderTemplate": templateguid,
                                                                  "orderType": EnumOrderType(direction).name.capitalize(),
                                                                  "triggerType": EnumOrderBotTriggerType(triggertype).name.capitalize()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])), response["ErrorMessage"],
                                         self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.ORDER_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def edit_order_bot_order(self, botguid: str, dependson: str, dependsonnotexecuted: str, amount: float, price: float,
                            triggerprice: float, templateguid: str,  direction: EnumOrderType, triggertype: EnumOrderBotTriggerType,):
        """

        :param botguid: str: 
        :param dependson: str: 
        :param dependsonnotexecuted: str: 
        :param amount: float: 
        :param price: float: 
        :param triggerprice: float: 
        :param templateguid: str: 
        :param direction: EnumOrderType: 
        :param triggertype: EnumOrderBotTriggerType: 

        """

        response = super()._execute_request("/OrderBotEditOrder", {"botGuid": botguid,
                                                                   "dependsOn": dependson,
                                                                   "dependsOnNotExecuted": dependsonnotexecuted,
                                                                   "amount": float(str(amount).replace(',', '.')),
                                                                   "price": float(str(price).replace(',', '.')),
                                                                   "triggerPrice": float(str(triggerprice).replace(',', '.')),
                                                                   "orderTemplate": templateguid,
                                                                   "orderType": EnumOrderType(direction).name.capitalize(),
                                                                   "triggerType": EnumOrderBotTriggerType(triggertype).name.capitalize()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])), response["ErrorMessage"],
                                         self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.ORDER_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def reset_order_bot_order(self, botguid: str, orderguid: str):
        """

        :param botguid: str: 
        :param orderguid: str: 

        """

        response = super()._execute_request("/OrderBotResetOrder", {"botGuid": botguid,
                                                                    "orderGuid": orderguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])), response["ErrorMessage"],
                                         self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.ORDER_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def remove_order_bot_order(self, botguid: str, orderguid: str):
        """

        :param botguid: str: 
        :param orderguid: str: 

        """

        response = super()._execute_request("/OrderBotRemoveOrder", {"botGuid": botguid,
                                                                     "orderGuid": orderguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])), response["ErrorMessage"],
                                         self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.ORDER_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def remove_all_order_bot_order(self, botguid: str):
        """

        :param botguid: str: 

        """

        response = super()._execute_request("/OrderBotRemoveAllOrders", {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])), response["ErrorMessage"],
                                         self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.ORDER_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_script_bot_parameters(self, botguid: str, fieldno: int, value: any):
        """

        :param botguid: str: 
        :param fieldno: int: 
        :param value: any: 

        """

        response = super()._execute_request("/OrderBotResetOrder", {"botGuid": botguid,
                                                                    "fieldNo": fieldno,
                                                                    "value": value})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])), response["ErrorMessage"],
                                         self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.SCRIPT_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})
            