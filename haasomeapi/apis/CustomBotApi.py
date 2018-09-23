import json

from typing import List
from haasomeapi.apis.ApiBase import ApiBase
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder

from haasomeapi.enums.EnumOrderType import EnumOrderType
from haasomeapi.enums.EnumCurrencyType import EnumCurrencyType
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haasomeapi.enums.EnumBotTradeAmount import EnumBotTradeAmount
from haasomeapi.enums.EnumMadHatterSafeties import EnumMadHatterSafeties
from haasomeapi.enums.EnumFlashSpreadOptions import EnumFlashSpreadOptions
from haasomeapi.enums.EnumMadHatterIndicators import EnumMadHatterIndicators
from haasomeapi.enums.EnumOrderBotTriggerType import EnumOrderBotTriggerType
from haasomeapi.enums.EnumAccumulationBotStopType import EnumAccumulationBotStopType
from haasomeapi.enums.EnumAdvancedIndexBotRebalanceType import EnumAdvancedIndexBotRebalanceType

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
from haasomeapi.dataobjects.custombots.dataobjects.AdvancedIndexBotIndexSaveObject import AdvancedIndexBotIndexSaveObject


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

        botinitial.priceMarket = super()._from_json(botinitial.priceMarket, Market)

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

        botinitial.priceMarket = super()._from_json(botinitial.priceMarket, Market)

        return botinitial

    def _convert_index_to_json(self, index: CryptoIndexBotIndexSaveObject):

        index = {
            "coin": index.coin, 
            "amount": index.amount,
            "buyThreshold": index.buyThreshold,
            "sellThreshold": index.sellThreshold, 
            "stopLoss": index.stopLoss
        }

        return json.dumps(index,sort_key=True)

    def _convert_advanced_index_to_json(self, index: AdvancedIndexBotIndexSaveObject):
        
        index = {
            "coin": index.coin, 
            "allocatedPercentage": index.allocatedPercentage, 
            "buyThreshold": index.buyThreshold,
            "sellThreshold": index.sellThreshold, 
            "stopLoss": index.stopLoss, 
            "trailingStop": index.trailingStop
        }

        return json.dumps(index,sort_key=True)

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

    def _convert_advanced_index_list_to_json(self, index: List[AdvancedIndexBotIndexSaveObject]):
        """ Internal fucntion to converts a CryptoIndexBotIndexSaveObject list to a json string

        :param index: List[CryptoIndexBotIndexSaveObject]: 

        :returns: str: Json string representation of specified list
        """

        index_fixed = []

        for i in index:
            index_fixed.append({"coin": i.coin, "allocatedPercentage": i.allocatedPercentage, "buyThreshold": i.buyThreshold,
                    "sellThreshold": i.sellThreshold, "stopLoss": i.stopLoss, "trailingStop": i.trailingStop})

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


    def _safe_custom_bot_type_enum_name_convert(self, bottype: EnumCustomBotType):
        """ Internal fucntion to converts a haasomeapi enum name to the correct haasonline enum name

        :param bottype: :class:`~haasomeapi.enums.EnumCustomBotType`: Enum Bot Type To Convert

        :returns: str: Correct Name for enum
        """
        
        botname = ""

        if bottype == EnumCustomBotType.MARKET_MAKING_BOT:
            botname = "MarketMakingBot"
        if bottype == EnumCustomBotType.PING_PONG_BOT:
            botname = "PingPongBot"
        if bottype == EnumCustomBotType.SCALPER_BOT:
            botname = "ScalperBot"
        if bottype == EnumCustomBotType.ORDER_BOT:
            botname = "OrderBot"
        if bottype == EnumCustomBotType.FLASH_CRASH_BOT:
            botname = "FlashCrashBot"
        if bottype == EnumCustomBotType.INTER_EXCHANGE_ARBITRAGE_BOT:
            botname = "InterExchangeArbitrage"
        if bottype == EnumCustomBotType.INTELLIBOT_ALICE_BOT:
            botname = "IntellibotAlice"
        if bottype == EnumCustomBotType.ZONE_RECOVERY_BOT:
            botname = "ZoneRecoveryBot"
        if bottype == EnumCustomBotType.ACCUMULATION_BOT:
            botname = "AccumulationBot"
        if bottype == EnumCustomBotType.TREND_LINES_BOT:
            botname = "TrendLinesBot"
        if bottype == EnumCustomBotType.MAD_HATTER_BOT:
            botname = "MadHatterBot"
        if bottype == EnumCustomBotType.SCRIPT_BOT:
            botname ="ScriptBot"
        if bottype == EnumCustomBotType.CRYPTO_INDEX_BOT:
            botname = "CryptoIndexBot"
        if bottype == EnumCustomBotType.HAAS_SCRIPT_BOT:
            botname = "HaasScriptBot"
        if bottype == EnumCustomBotType.EMAIL_BOT:
            botname = "EmailBot"

        return botname

    def _safe_mad_hatter_safety_enum_name_convert(self, enumMHSafety: EnumMadHatterSafeties):

        enumstr = ""

        if enumMHSafety == EnumMadHatterSafeties.PRICE_CHANGE_TO_BUY:
            enumstr = "PriceChangeToBuy"
        if enumMHSafety == EnumMadHatterSafeties.PRICE_CHANGE_TO_SELL:
            enumstr = "PriceChangeToSell"
        if enumMHSafety == EnumMadHatterSafeties.STOP_LOSS:
            enumstr = "StopLoss"

        return enumstr

    def get_all_custom_bots(self):
        """ Returns all custom bots created

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result List[:class:`~haasomeapi.dataobjects.custombots.BaseCustomBot`]
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

        :param botguid: str: Custom bot guid
        :param bottype: :class:`~haasomeapi.enums.EnumCustomBotType`: Type of bot to return 

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result any: Specified bottype object
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

        :param botguid: str: Custm bot guid
        :param withextra: bool: with extra

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result bool: If activation was successful
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

        :param botguid: str: Custm bot guid
        :param withextra: bool: with extra
        
        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: Int .result bool: If deactivation was successful
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

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result any: Specified bot type object
        """

        response = super()._execute_request("/NewCustomBot", {"botType": self._safe_custom_bot_type_enum_name_convert(EnumCustomBotType(bottype)),
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

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result any: Specified bot type object
        """

        response = super()._execute_request("/NewCustomBot", {"botType": self._safe_custom_bot_type_enum_name_convert(EnumCustomBotType(bottype)),
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
        """ Removes (deletes) custom bot

        :param botguid: str: Custom bot guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result bool: If removal was succesfull
        """

        response = super()._execute_request("/RemoveCustomBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def clear_custom_bot(self, botguid: str):
        """ Clears custom bots history and returns a BaseCustomBot object

        :param botguid: str: Custom bot guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.BaseCustomBot`: BaseCustomBot of the bot that was cleared
        """

        response = super()._execute_request("/ClearCustomBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.BASE_CUSTOM_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def clear_custom_bot_specific(self, botguid: str, bottype: EnumCustomBotType):
        """ Clears custom bots history and returns the specific custombot object

        :param botguid: str: Custom bot guid
        :param bottype: :class:`~haasomeapi.enums.EnumCustomBotType`: Custom bot type to return

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result any: Specified custom bot object 
        """

        response = super()._execute_request("/ClearCustomBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(bottype, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def backtest_custom_bot(self, botguid: str, minutestotest: int):
        """ Backtest a custom bot (Note: This function will will make a request to the exchange so don't call to often)

        :param botguid: str: Custom bot guid
        :param minutestotest: int: Amount of minutes to test in the past
        
        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.BaseCustomBot`: BaseCustomBot of the bot that was backtested
        """

        response = super()._execute_request("/BacktestCustomBot",  {"botGuid": botguid, "minutesToTest": minutestotest})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.BASE_CUSTOM_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def backtest_custom_bot_unix_time(self, botguid: str, startunix: int, endunix: int):
        """ Backtest a custom bot (Note: This function will make a request to the exchange so don't call to often)

        :param botguid: str: Custom bot guid
        :param startunix: int: Start time in unix time notation
        :param endunix: int: End time in unix time notation

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.BaseCustomBot`: BaseCustomBot of the bot that was backtested
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
        """ Backtest a custom bot on specified market place (Note: This function does not call the exchange can use has often as you want.)

        :param accountguid: str: Account guid
        :param botguid: str: Custom bot guid
        :param minutestotest: int: Amount of minutes to test in the past
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str: Contract name (Optional)

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.BaseCustomBot`: BaseCustomBot of the bot that was backtested
        """

        response = super()._execute_request("/BacktestCustomBotOnMarket",  {"botGuid": botguid,
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

    def clone_custom_bot(self, accountguid: str, botguid: str, bottype: EnumCustomBotType,botname: str, 
                         primarycoin: str,secondarycoin: str, contractname: str, leverage: float):
        """ Clone a custom bot

        :param accountguid: str: Account guid
        :param botguid: str: Custom bot guid
        :param bottype: :class:`~haasomeapi.enums.EnumCustomBotType`: The bottype to create 
        :param botname: str: Name for the new custom bot
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str: Contract name (Optional)
        :param leverage: float: Leverage percentage to use (Optional)

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result any: Specified bot type object
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
        """ Clone a custom bot simplefied

        :param accountguid: str: Account guid
        :param botguid: str: Custom bot guid to clone
        :param botname: str: Name for the new custom bot

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.BaseCustomBot`: BaseCustomBot of the bot that was backtested
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
        """ Modify a Accumulation bot

        :param accountguid: str: Account guid
        :param botguid: str: Custom bot guid
        :param botname: str: Name for the new custom bot
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param stoptype: :class:`~haasomeapi.enums.EnumAccumulationBotStopType`:  The stop type
        :param stoptypevalue: float:  Stop value associated with stop type
        :param randomordersizex: float: Random order size start
        :param randomordersizey: float: Random order size end
        :param randomordertimex: int: Random order time in seconds start
        :param randomordertimey: int: Random order time in seconds stop
        :param direction: :class:`~haasomeapi.enums.EnumOrderType`: Order direction (buy/sell) 
        :param triggeronprice: bool: Trigger on a specific price 
        :param triggerwhenhigher: bool: Trigger when marker price is higher than trigger price
        :param triggervalue: float: Trigger price

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.AccumulationBot`: Accumulation bot object
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
        """ Modify a Crypto Index bot

        :param accountguid: str: Account guid
        :param botguid: str: Custom bot guid
        :param botname: str: Name for the new custom bot 
        :param templateguid: str: Order template to use GUID
        :param basecoin: str: The base currency for the index bot Ex. BTC
        :param totalIndexValue: float: Total value the index should be using.
        :param individualgrowth: bool: Use the individual growth algorithm
        :param allocateprofits: bool: Perform allocation of profits
        :param index: List[:class:`~haasomeapi.dataobjects.custombots.dataobjects.CryptoIndexBotIndexSaveObject`]: List of :class:`~haasomeapi.dataobjects.custombots.dataobjects.CryptoIndexBotIndexSaveObject` to construct the index.

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.CryptoIndexBot`: Crypto Index bot object
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

    def setup_advanced_index_bot(self, accountguid: str, botguid: str, botname: str, templateguid: str, basecoin: str,
                               totalIndexValue: float, rebalanceInterval: int, rebalanceType: EnumAdvancedIndexBotRebalanceType, 
                               allocateProfits: bool, preserveBaseIndexPrecentage:bool, index: List[AdvancedIndexBotIndexSaveObject] ):
        """ Modify a Crypto Index bot

        :param accountguid: str: Account guid
        :param botguid: str: Custom bot guid
        :param botname: str: Name for the new custom bot 
        :param templateguid: str: Order template to use GUID
        :param basecoin: str: The base currency for the index bot Ex. BTC
        :param totalIndexValue: float: Total value the index should be using.
        :param rebalanceInterval: int: How often to rebalance
        :param allocateprofits: bool: Perform allocation of profits
        :param preserveBaseIndexPercentage: bool: Ensure index perecentage never dips below start percentage
        :param index: List[:class:`~haasomeapi.dataobjects.custombots.dataobjects.AdvancedIndexBotIndexSaveObject`]: List of :class:`~haasomeapi.dataobjects.custombots.dataobjects.AdvancedIndexBotIndexSaveObject` to construct the index.

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.AdvancedIndexBot`: Crypto Index bot object
        """

        response = super()._execute_request("/SetupAdvancedIndexBot",  {"botGuid": botguid,
                                                                      "botName": botname,
                                                                      "accountGuid": accountguid,
                                                                      "templateGuid": templateguid,
                                                                      "baseCoin": basecoin,
                                                                      "totalIndexValue": float(str(totalIndexValue).replace(',', '.')),
                                                                      "rebalanceInterval": rebalanceInterval,
                                                                      "rebalanceType": EnumAdvancedIndexBotRebalanceType(rebalanceType).value,
                                                                      "allocateProfits": str(allocateProfits).lower(),
                                                                      "preserveBaseIndexPercentage": str(preserveBaseIndexPercentage).lower(),
                                                                      "index": self._convert_index_list_to_json(index)})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.ADVANCED_INDEX_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_email_bot(self, accountguid: str, botguid: str, botname: str, primarycoin: str, secondarycoin: str,
                        contractname: str, leverage: float, amountType: EnumBotTradeAmount, tradeamount: float, fee: float, templateguid: str,
                        position: str, actions: List[EmailBotAction], stoploss: float, minchangetobuy: float,
                        minchangetosell: float):
        """ Modify a Email bot

        :param accountguid: str: Account guid
        :param botguid: str: Custom bot guid
        :param botname: str: Name for the new custom bot
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str: Contract name (Optional)
        :param leverage: float: Leverage percentage to use (Optional)
        :param amountType: :class:`~haasomeapi.enums.EnumBotTradeAmount` Trade amount type

        :param tradeamount: float: Trade amount for the bot to use
        :param fee: float: Fee percentage to be used in calculations
        :param templateguid: str: Order template to be used GUID
        :param position: str: Position bot should start in EX. For BNB/BTC if you have no BNB set to BTC
        :param actions: List[:class:`~haasomeapi.dataobjects.custombots.dataobjects.EmailBotAction`]: List of :class:`~haasomeapi.dataobjects.custombots.dataobjects.EmailBotAction` to build the email bot from 
        :param stoploss: float: Stop loss percentage
        :param minchangetobuy: float: Min Change To Buy insurance setting
        :param minchangetosell: float: Min Change To Sell Insurance setting

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.EmailBot`: Email bot object
        """

        response = super()._execute_request("/SetupEmailBot",  {"botGuid": botguid,
                                                                "botName": botname,
                                                                "accountGuid": accountguid,
                                                                "primaryCoin": primarycoin,
                                                                "secondaryCoin": secondarycoin,
                                                                "contractName": contractname,
                                                                "leverage": float(str(leverage).replace(',', '.')),
                                                                "tradeAmountType": str(EnumBotTradeAmount(amountType).value),
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
        """ Modify a Flash Crash bot

        :param accountguid: str: Account guid
        :param botguid: str: Custom bot guid
        :param botname: str: Name for the new custom bot
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param fee: float: Fee percentage to be used in calculations
        :param baseprice: float: Base price for FCB to start at
        :param priceSpreadType: :class:`~haasomeapi.enums.EnumFlashSpreadOptions`: FCB Spread Type 
        :param pricespread: float: Price spread value
        :param percentageboost: float: Percentage boost value to be set with PercentageBoost spread type.
        :param minpercentage: float: Min Percentage value to be used with percentage spread type
        :param maxpercentage: float: Max Percentage value to be used with percentage spread type
        :param amounttype: :class:`~haasomeapi.enums.EnumCurrencyType`: Currency type 
        :param amountspread: float: Current amount spread value
        :param buyamount: float: Number of buy orders
        :param sellamount: float: Number of sell orders
        :param refilldelay: int: Refill order delay in minutes
        :param safetyenabled: bool: Enable the safety
        :param safetytriggerlevel: float: Price value saftey should activate
        :param safetymoveinout: bool: Safety move in out value
        :param followthetrend: bool: Activate follow the trend
        :param followthetrendchannelrange: int: Follow the trend channel range
        :param followthetrendchanneloffset: int: Follow the trend channel offset
        :param followthetrendtimeout: int:  Follow the trend timeout value

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.FlashCrashBot`: Flash Crash bot object
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
        """ Modify Inter Exchange Arbitrage bot
        :param accountguid: str: Account guid
        :param botguid: str: Custom bot guid
        :param botname: str: Name for the new custom bot
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param accountguid2: str: Seoncdary Account Guid
        :param primarycoin2: str: Primary currency of the second account Ex. If BNB/BTC then set this to BNB
        :param secondarycoin2: str: Secondary currency of the second account Ex. If BNB/BTC then set this to BTC
        :param tradeamount: float: Trade amount to use
        :param triggerlevel: float: Trigger level for trades in percentage
        :param templateguid: str: Order template to use Guid
        :param maxamount: float: Max amount to trade a day
        :param maxtrades: int: Max trades to execute a day

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.InterExchangeArbitrageBot`: Inter Exchange Arbitrage bot object
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
                               contractname: str, leverage: float, amountType: EnumBotTradeAmount, tradeamount: float, fee: float):
        """ Modify Intelli Bot Alice bot

        :param accountguid: str: Account guid
        :param botguid: str: Custom bot guid
        :param botname: str: Name for the new custom bot
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str: Contract name (Optional)
        :param leverage: float: Leverage percentage to use (Optional)
        :param amountType: :class:`~haasomeapi.enums.EnumBotTradeAmount` Trade amount type
        :param tradeamount: float: Trade amount to use
        :param fee: float: Fee percentage to be used in calculations

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.BaseCustomBot`: BaseCustomBot Object
        """

        response = super()._execute_request("/SetupIntellibotAlice",  {"botGuid": botguid,
                                                                       "botName": botname,
                                                                       "accountGuid": accountguid,
                                                                       "primaryCoin": primarycoin,
                                                                       "secondaryCoin": secondarycoin,
                                                                       "contractName": contractname,
                                                                       "leverage": float(str(leverage).replace(',', '.')),
                                                                       "tradeAmountType": str(EnumBotTradeAmount(amountType).value),
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
        """ Modify Market Making bot

        :param accountguid: str: Account guid
        :param botguid: str: Custom bot guid
        :param botname: str: Name for the new custom bot
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param tradeamount: float: Trade amount to use
        :param fee: float: Fee percentage to be used in calculations
        :param offset: float: First order offset value 
        :param resettimeout: int: Reset timeout in minutes
        :param usedsecondorder: bool: Use a second order
        :param secondoffset: float: Second order offset

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.MarketMakingBot`: Market Making bot object
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
                             templateguid: str, position: str, fee: float, amountType: EnumBotTradeAmount, 
                             tradeamount: float, useconsensus: bool, disableafterstoploss: bool, interval: int, includeincompleteinterval: bool):
        """ Modify Mad Hatter bot

        :param accountguid: str: Account guid
        :param botguid: str: Custom bot guid
        :param botname: str: Name for the new custom bot
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param templateguid: str: Order template to use Guid
        :param position: str: Position bot should start in EX. For BNB/BTC if you have no BNB set to BTC
        :param fee: float: Fee percentage to be used in calculations
        :param amountType: :class:`~haasomeapi.enums.EnumBotTradeAmount` Trade amount type
        :param tradeamount: float: Trade amount to use
        :param useconsensus: bool: Enable Consensus Mode
        :param disableafterstoploss: bool: Disable bot after stop loss
        :param interval: int: Price Ticker Minute Interval. Ex. 1,2,3,,5,15,30, etc
        :param includeincompleteinterval: bool: Allow a incomplete price ticker

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.MadHatterBot`: Mad Hatter bot object
        """

        response = super()._execute_request("/SetupMadHatterBot",  {"botGuid": botguid,
                                                                    "botName": botname,
                                                                    "accountGuid": accountguid,
                                                                    "primaryCoin": primarycoin,
                                                                    "secondaryCoin": secondarycoin,
                                                                    "tradeAmountType": str(EnumBotTradeAmount(amountType).value),
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
        """ Modify Order bot

        :param accountguid: str: Account guid
        :param botguid: str: Custom bot guid
        :param botname: str: Name for the new custom bot
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        
        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.OrderBot`: Order bot object
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
                            contractbame: str, leverage: float, amountType: EnumBotTradeAmount, tradeamount: float, position: str, fee: float):
        """ Modify Ping Pong bot

        :param accountguid: str: Account guid
        :param botguid: str: Custom bot guid
        :param botname: str: Name for the new custom bot
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str: Contract name (Optional)
        :param leverage: float: Leverage percentage to use (Optional)
        :param amountType: :class:`~haasomeapi.enums.EnumBotTradeAmount` Trade amount type
        :param tradeamount: float: Trade amount to use
        :param position: str: Position bot should start in EX. For BNB/BTC if you have no BNB set to BTC
        :param fee: float: Fee percentage to be used in calculations

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.BaseCustomBot`: Ping Pong is just a BaseCustomBot - BaseCustomBot object
        """

        response = super()._execute_request("/SetupPingPongBot",  {"botGuid": botguid,
                                                                    "botName": botname,
                                                                    "accountGuid": accountguid,
                                                                    "primaryCoin": primarycoin,
                                                                    "secondaryCoin": secondarycoin,
                                                                    "contractName": contractbame,
                                                                    "leverage": float(str(leverage).replace(',', '.')),
                                                                    "tradeAmountType": str(EnumBotTradeAmount(amountType).value),
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
                          templateguid :str, contractname: str, leverage: float, amountType: EnumBotTradeAmount,
                          tradeamount: float, position: str, fee: float , targetpercentage: float, safetythreshold: float):
        """ Modify Scalper bot

        :param accountguid: str: Account guid
        :param botguid: str: Custom bot guid
        :param botname: str: Name for the new custom bot
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param templateguid: str: Order template to use Guid
        :param contractname: str: Contract name (Optional)
        :param leverage: float: Leverage percentage to use (Optional)
        :param amountType: :class:`~haasomeapi.enums.EnumBotTradeAmount` Trade amount type
        :param tradeamount: float: Trade amount to use
        :param position: str: Position bot should start in EX. For BNB/BTC if you have no BNB set to BTC
        :param fee: float: Fee percentage to be used in calculations
        :param targetpercentage: float: 
        :param safetythreshold: float: 

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.ScalperBot`: Scalper bot object
        """

        response = super()._execute_request("/SetupScalpingBot",  {"botGuid": botguid,
                                                                   "botName": botname,
                                                                   "accountGuid": accountguid,
                                                                   "primaryCoin": primarycoin,
                                                                   "secondaryCoin": secondarycoin,
                                                                   "templateGuid": templateguid,
                                                                   "contractName": contractname,
                                                                   "leverage": float(str(leverage).replace(',', '.')),
                                                                   "tradeAmountType": str(EnumBotTradeAmount(amountType).value),
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
                         templateguid :str, contractbame: str, leverage: float, tradeamount: float, position: str, 
                         fee: float,scriptid: str):
        """ Modify Script bot

        :param accountguid: str: Account guid
        :param botguid: str: Custom bot guid
        :param botname: str: Name for the new custom bot
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
       
        :param templateguid :str: Order template to use Guid
        :param contractbame: str: Contract name (Optional)
        :param leverage: float: Leverage percentage to use (Optional)
        :param tradeamount: float: Trade amount to use
        :param position: str: Position bot should start in EX. For BNB/BTC if you have no BNB set to BTC
        :param fee: float: Fee percentage to be used in calculations
        :param scriptid: str: Script Id for bot to use

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.ScriptBot`: Script Bot Object
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
        """ Modify zone_recovery_bot

        :param accountguid: str: Account guid
        :param botguid: str: Custom bot guid
        :param botname: str: Name for the new custom bot
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str: Contract name (Optional)
        :param leverage: float: Leverage percentage to use (Optional)
        :param tradeamount: float: Trade amount to use
        :param maxtradeamount: float: Max Trade amount 
        :param factorlong: float: Factor long value
        :param factorshort: float: Factor short value
        :param targetprofit: float: Target profit percentage
        :param zone: float: Zone value

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.ZoneRecoveryBot`: Zone Recovery bot object
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
        """ Flash crash quick start (Do not replace orders)
        
        :param botguid: str: Custom bot guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result bool: If quick start was successful
        """

        response = super()._execute_request("/QuickStartFlashCrashBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def flash_crash_bot_quick_start_all(self, botguid: str):
        """ Flash crash quick start (Replace orders missing)

        :param botguid: str: Custom bot guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result bool: If quick start was successful
        """

        response = super()._execute_request("/QuickStartAllFlashCrashBots",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def flash_crash_bot_live_edit(self, botguid: str, isbuyorder: bool, addorder: bool):
        """ Add a order to a running flash crash

        :param botguid: str: Custom bot guid
        :param isbuyorder: bool: Is the order to add a buy order
        :param addorder: bool: Should we be adding the order or removing one

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.FlashCrashBot`: Flash Crash bot object
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
        """ Quick call to add a buy order to a running flash crash_bot

        :param botguid: str: Custom bot guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.FlashCrashBot`: Flash Crash bot object
        """

        return self.flash_crash_bot_live_edit(botguid, True, True)

    def flash_crash_bot_remove_buy_order(self, botguid: str):
        """ Quick call to remove a buy order to a running flash crash_bot

        :param botguid: str: Custom bot guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.FlashCrashBot`: Flash Crash bot object
        """

        return self.flash_crash_bot_live_edit(botguid, True, False)

    def flash_crash_bot_add_sell_order(self, botguid: str):
        """ Quick call to add a sell order to a running flash crash_bot

        :param botguid: str: Custom bot guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.FlashCrashBot`: Flash Crash bot object
        """

        return self.flash_crash_bot_live_edit(botguid, False, True)

    def flash_crash_bot_remove_sell_order(self, botguid: str):
        """ Quick call to remove a sell order to a running flash crash_bot

        :param botguid: str: Custom bot guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.FlashCrashBot`: Flash Crash bot object
        """

        return self.flash_crash_bot_live_edit(botguid, False, False)

    def set_mad_hatter_indicator_parameter(self, botguid: str, type: EnumMadHatterIndicators, fieldNo: int, value: any):
        """ Modify Mad Hatter Indicator Parameter

        :param botguid: str: Custom bot guid
        :param type: :class:`~haasomeapi.enums.EnumMadHatterIndicators`: Indicator type to modify 
        :param fieldNo: int: Field to modify 
        :param value: any: Value for the field

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.MadHatterBot`: Mad Hatter bot object
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
        """ Modify Mad hatter Safety Parameter

        :param botguid: str: Custom Bot guid
        :param type: :class:`~haasomeapi.enums.EnumMadHatterSafeties`: Safety Type to modify 
        :param value: any: Safety Value

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.MadHatterBot`: Mad Hatter bot object
        """

        response = super()._execute_request("/MadHatterSetSafetyParameter",  {"botGuid": botguid,
                                                                              "type": self._safe_mad_hatter_safety_enum_name_convert(type),
                                                                              "value": value})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.MAD_HATTER_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def flip_accumulation_bot(self, botguid: str):
        """ Flip Accumulation bot from buy to sold or sold to buy

        :param botguid: str: Custom bot guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result bool: If flip was successful
        """

        response = super()._execute_request("/FlipAccumulationBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def add_order_bot_order(self, botguid: str, dependson: str, dependsonnotexecuted: str, amount: float, price: float,
                            triggerprice: float, templateguid: str,  direction: EnumOrderType, triggertype: EnumOrderBotTriggerType):
        """ Add a order to a order bot

        :param botguid: str: Custom bot guid
        :param dependson: str: Order template guid this order depends on
        :param dependsonnotexecuted: str: Order guid this depends on to not be executed.
        :param amount: float: Trade amount to use
        :param price: float: Price for the order
        :param triggerprice: float: Trigger price for the order
        :param templateguid: str: Order template for order to use guid
        :param direction: :class:`~haasomeapi.enums.EnumOrderType`: Order direction (Buy/Sell)
        :param triggertype: :class:`~haasomeapi.enums.EnumOrderBotTriggerType`: Trigger type

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.OrderBot`: Order bot object 
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

    def edit_order_bot_order(self, botguid: str, orderguid: str, dependson: str, dependsonnotexecuted: str, amount: float, price: float,
                            triggerprice: float, templateguid: str,  direction: EnumOrderType, triggertype: EnumOrderBotTriggerType,):
        """ Edit a order on a order bot

        :param botguid: str: Custom bot guid
        :param orderguid: str: Guid of order to edit
        :param dependson: str: Order template guid this order depends on
        :param dependsonnotexecuted: str: Order guid this depends on to not be executed.
        :param amount: float: Trade amount to use
        :param price: float: Price for the order
        :param triggerprice: float: Trigger price for the order
        :param templateguid: str: Order template for order to use guid
        :param direction: :class:`~haasomeapi.enums.EnumOrderType`: Order direction (Buy/Sell)
        :param triggertype: :class:`~haasomeapi.enums.EnumOrderBotTriggerType`: Trigger type

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.OrderBot`: Order bot object 
        """

        response = super()._execute_request("/OrderBotEditOrder", {"botGuid": botguid,
                                                                   "orderGuid": orderguid,
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
        """ Reset a order on a order bot

        :param botguid: str: Custom bot guid
        :param orderguid: str: Order guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.OrderBot`: Order bot object 
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
        """ Remove (delete) a order on a order bot

        :param botguid: str: Custom bot guid
        :param orderguid: str: Order guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.OrderBot`: Order bot object 
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
        """ Removes all orders from order bot

        :param botguid: str: Custom bot guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.OrderBot`: Order bot object 
        """

        response = super()._execute_request("/OrderBotRemoveAllOrders", {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])), response["ErrorMessage"],
                                         self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.ORDER_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_script_bot_parameters(self, botguid: str, fieldno: int, value: any):
        """ Modify script bot parameters

        :param botguid: str: Custom bot guid
        :param fieldno: int: Field Number to modify
        :param value: any: Value for field
    
        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.ScriptBot`: Script bot object 
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

    def add_crypto_index_bot_index(self, botguid: str, index: CryptoIndexBotIndexSaveObject, realocatebalance: bool, raisebalance: bool):
        """ Addes a index to preexiting crypto index bot
        :param botguid: str: Custom bot guid
        :param index: :class:`~haasomeapi.dataobjects.custombots.dataobjects.CryptoIndexBotIndexSaveObject` Index to add
        :param reallocatebalance: bool: reallocate current index balance
        :param raisebalance: bool: increase current index balance
    
        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.CryptoIndexBot`: Crypto Index bot object 
        """

        response = super()._execute_request("/CryptoIndexBotAddIndex",{"botGuid": botguid,
                                                                      "index": self._convert_index_to_json(index),
                                                                      "raiseBalance": str(raisebalance).lower(),
                                                                      "realocateBalance": str(realocatebalance).lower(),
                                                                      })
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.CRYPTO_INDEX_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def remove_crypto_index_bot_index(self, botguid: str, coin: str, lowerbalance: bool):
        """ Removes a index from preexiting crypto index bot
        :param botguid: str: Custom bot guid
        :param coin: std: Coin to remove from index
        :param lowerbalance: bool: Reduce the index balance
    
        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.CryptoIndexBot`: Crypto Index bot object 
        """

        response = super()._execute_request("/CryptoIndexBotRemoveIndex",{"botGuid": botguid,
                                                                          "coin": coin,
                                                                          "lowerBalance": str(lowerbalance).lower(),
                                                                          })
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.CRYPTO_INDEX_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def add_advanced_index_bot_index(self, botguid: str, index: AdvancedIndexBotIndexSaveObject, realocatebalance: bool, raisebalance: bool):
        """ Addes a index to preexiting advanced index bot
        :param botguid: str: Custom bot guid
        :param index: :class:`~haasomeapi.dataobjects.custombots.dataobjects.AdvancedIndexBotIndexSaveObject` Index to add
        :param reallocatebalance: bool: reallocate current index balance
        :param raisebalance: bool: increase current index balance
    
        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.AdvancedIndexBot`: Crypto Index bot object 
        """

        response = super()._execute_request("/AdvancedIndexBotAddIndex",{"botGuid": botguid,
                                                                      "index": self._convert_advanced_index_to_json(index),
                                                                      "raiseBalance": str(raisebalance).lower(),
                                                                      "realocateBalance": str(realocatebalance).lower(),
                                                                      })
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.ADVANCED_INDEX_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})


    def remove_advanced_index_bot_index(self, botguid: str, coin: str, lowerbalance: bool):
        """ Removes a index from preexiting advanced index bot
        :param botguid: str: Custom bot guid
        :param coin: std: Coin to remove from index
        :param lowerbalance: bool: Reduce the index balance
    
        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.AdvancedIndexBot`: Crypto Index bot object 
        """

        response = super()._execute_request("/AdvancedIndexBotRemoveIndex",{"botGuid": botguid,
                                                                            "coin": coin,
                                                                            "lowerBalance": str(lowerbalance).lower(),
                                                                            })
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.ADVANCED_INDEX_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def include_advanced_index_bot_index(self, botguid: str, coin: str):
        """ Includes a excluded index from the advanced index bot
        :param botguid: str: Custom bot guid
        :param coin: std: Coin to include from index
    
        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.AdvancedIndexBot`: Crypto Index bot object 
        """

        response = super()._execute_request("/AdvancedIndexBotIncludeIndex",{"botGuid": botguid,
                                                                             "coin": coin,
                                                                             })
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.ADVANCED_INDEX_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def rebalance_advanced_index_bot_index(self, botguid: str):
        """ Rebalance a advanced index bot
        :param botguid: str: Custom bot guid
    
        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.custombots.AdvancedIndexBot`: Crypto Index bot object 
        """

        response = super()._execute_request("/AdvancedIndexBotRebalanceBot",{"botGuid": botguid})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.ADVANCED_INDEX_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})