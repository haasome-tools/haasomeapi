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

    def __init__(self, connectionstring: str, privatekey: str):
        ApiBase.__init__(self, connectionstring, privatekey)

    def _convert_json_bot_to_custom_bot_object(self, jsonstr: str):

        botinitial = super()._from_json(jsonstr, BaseCustomBot)

        orders = []

        for corder in botinitial.completedOrders:
            orders.append(super()._from_json(corder, BaseOrder))

        botinitial.completedOrders = orders

        return botinitial

    def _convert_json_bot_to_custom_bot_specific(self, bottype: EnumCustomBotType, jsonstr: str):

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
        index_fixed = []

        for i in index:
            index_fixed.append({"coin": i.coin, "amount": i.amount, "buyThreshold": i.buyThreshold,
                                "sellThreshold": i.sellThreshold, "stopLoss": i.stopLoss})

        return json.dumps(index_fixed, sort_keys=True)

    def _convert_emails_list_to_json(self, actions: List[EmailBotAction]):

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

    def get_custom_bot(self, bottype: EnumCustomBotType, botguid: str):

        response = super()._execute_request("/GetCustomBot", {"botGuid": botguid})


        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(bottype, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def activate_custom_bot(self, botguid: str, withextra: bool):
        response = super()._execute_request("/ActivateCustomBot",  {"botGuid": botguid, "extra": str(withextra).lower()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def deactivate_custom_bot(self, botguid: str, withextra: bool):
        response = super()._execute_request("/DeactivateCustomBot",  {"botGuid": botguid, "extra": str(withextra).lower()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def new_custom_bot(self, bottype: EnumCustomBotType, botname: str, accountguid: str, primarycoin: str,
                       secondarycoin: str, contractname: str):

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

    def new_custom_bot_from_market(self, bottype: EnumCustomBotType, botname: str, accountguid: str, market: Market):

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
        response = super()._execute_request("/RemoveCustomBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def clear_custom_bot(self, botguid: str):
        response = super()._execute_request("/ClearCustomBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.BASE_CUSTOM_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def clear_custom_bot_specific(self, bottype: EnumCustomBotType, botguid: str):
        response = super()._execute_request("/ClearCustomBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(bottype, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def backtest_custom_bot(self, botguid: str, minutestotest: int):
        response = super()._execute_request("/BacktestCustomBot",  {"botGuid": botguid, "minutesToTest": minutestotest})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.BASE_CUSTOM_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def backtest_custom_bot_unix_time(self, botguid: str, startunix: int, endunix: int):
        response = super()._execute_request("/BacktestCustomBot",  {"botGuid": botguid, "startUnix": startunix,
                                                                    "endunix": endunix})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.BASE_CUSTOM_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def backtest_custom_bot_on_market(self, botguid: str, minutestotest: int, accountguid: str, primarycoin: str,
                                      secondarycoin: str, contractname: str):

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

    def clone_custom_bot(self, bottype: EnumCustomBotType, botguid: str, botname: str, accountguid: str,
                         primarycoin: str,secondarycoin: str, contractname: str, leverage: float):

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

    def clone_custom_bot_simple(self, botguid: str, botname: str, accountguid: str):

        response = super()._execute_request("/CloneCustomBotSimple",  {"botGuid": botguid,
                                                                 "botName": botname,
                                                                 "accountGuid": accountguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.BASE_CUSTOM_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_accumulation_bot(self, botguid: str, botname: str, accountguid: str, primarycoin: str, secondarycoin: str,
                               stoptype: EnumAccumulationBotStopType, stoptypevalue: float, randomordersizex: float,
                               randomordersizey: float, randomordertimex: int, randomordertimey: int,
                               direction: EnumOrderType, triggeronprice: bool, triggerwhenhigher: bool, triggervalue: float):

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

    def setup_crypto_index_bot(self, botguid: str, botname: str, accountguid: str, templateguid: str, basecoin: str,
                               totalIndexValue: float, individualgrowth: bool, allocateprofits: bool, index: List[CryptoIndexBotIndexSaveObject] ):

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

    def setup_email_bot(self, botguid: str, botname: str, accountguid: str, primarycoin: str, secondarycoin: str,
                        contractname: str, leverage: float, tradeamount: float, fee: float, templateguid: str,
                        position: str, actions: List[EmailBotAction], stoploss: float, minchangetobuy: float,
                        minchangetosell: float):

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

    def setup_flash_crash_bot(self, botguid: str, botname: str, accountguid: str, primarycoin: str, secondarycoin: str,
                              fee: float, baseprice: float,  priceSpreadType: EnumFlashSpreadOptions, pricespread: float,
                              percentageboost: float, minpercentage: float, maxpercentage: float, amounttype: EnumCurrencyType,
                              amountspread: float, buyamount: float, sellamount: float, refilldelay: int, safetyenabled: bool,
                              safetytriggerlevel: float, safetymoveinout: bool, followthetrend: bool, followthetrendchannelrange: int,
                              followthetrendchanneloffset: int, followthetrendtimeout: int):

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

    def setup_inter_exchange_arbitrage_bot(self, botguid: str, botname: str, accountguid: str, primarycoin: str, secondarycoin: str,
                                           accountguid2: str, primarycoin2: str, secondarycoin2: str, tradeamount: float,
                                           triggerlevel: float, templateguid: str, maxamount: float, maxtrades: int):

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

    def setup_intellibot_alice(self, botguid: str, botname: str, accountguid: str, primarycoin: str, secondarycoin: str,
                               contractname: str, leverage: float, tradeamount: float, fee: float):

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

    def setup_market_making_bot(self, botguid: str, botname: str, accountguid: str, primarycoin: str, secondarycoin: str,
                                tradeamount: float, fee: float, offset: float, resettimeout: int, usedsecondorder: bool,
                                secondoffset: float):

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

    def setup_mad_hatter_bot(self, botguid: str, botname: str, accountguid: str, primarycoin: str, secondarycoin: str,
                             templateguid: str, position: str, fee: float, tradeamount: float, useconsensus: bool,
                             disableafterstoploss: bool, interval: int, includeincompleteinterval: bool):

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

    def setup_order_bot(self, botguid: str, botname: str, accountguid: str, primarycoin: str, secondarycoin: str):

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

    def setup_ping_pong_bot(self, botguid: str, botname: str, accountguid: str, primarycoin: str, secondarycoin: str,
                            contractbame: str, leverage: float, tradeamount: float, position: str, fee: float):

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

    def setup_scalper_bot(self, botguid: str, botname: str, accountguid: str, primarycoin: str, secondarycoin: str,
                          templateguid :str, contractbame: str, leverage: float, tradeamount: float, targetpercentage: float,
                          safetythreshold: float, position: str, fee: float):

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

    def setup_script_bot(self, botguid: str, botname: str, accountguid: str, primarycoin: str, secondarycoin: str,
                         templateguid :str, contractbame: str, leverage: float, tradeamount: float, fee: float,
                         position: str, scriptid: str):

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

    def setup_zone_recovery_bot(self, botguid: str, botname: str, accountguid: str, primarycoin: str, secondarycoin: str,
                                contractname: str, leverage: float, tradeamount: float, maxtradeamount: float,
                                factorlong: float, factorshort: float, targetprofit: float, zone: float):

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
        response = super()._execute_request("/QuickStartFlashCrashBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def flash_crash_bot_quick_start_all(self, botguid: str):
        response = super()._execute_request("/QuickStartAllFlashCrashBots",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def flash_crash_bot_live_edit(self, botguid: str, isbuyorder: bool, addorder: bool):
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
        return self.flash_crash_bot_live_edit(botguid, True, True)

    def flash_crash_bot_remove_buy_order(self, botguid: str):
        return self.flash_crash_bot_live_edit(botguid, True, False)

    def flash_crash_bot_add_sell_order(self, botguid: str):
        return self.flash_crash_bot_live_edit(botguid, False, True)

    def flash_crash_bot_remove_sell_order(self, botguid: str):
        return self.flash_crash_bot_live_edit(botguid, False, False)

    def set_mad_hatter_indicator_parameter(self, botguid: str, type: EnumMadHatterIndicators, fieldNo: int, value: any):

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
        response = super()._execute_request("/FlipAccumulationBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def add_order_bot_order(self, botguid: str, dependson: str, dependsonnotexecuted: str, amount: float, price: float,
                            triggerprice: float, templateguid: str,  direction: EnumOrderType, triggertype: EnumOrderBotTriggerType,):

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

        response = super()._execute_request("/OrderBotResetOrder", {"botGuid": botguid,
                                                                    "orderGuid": orderguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])), response["ErrorMessage"],
                                         self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.ORDER_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def remove_order_bot_order(self, botguid: str, orderguid: str):

        response = super()._execute_request("/OrderBotRemoveOrder", {"botGuid": botguid,
                                                                     "orderGuid": orderguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])), response["ErrorMessage"],
                                         self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.ORDER_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def remove_all_order_bot_order(self, botguid: str):

        response = super()._execute_request("/OrderBotRemoveAllOrders", {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])), response["ErrorMessage"],
                                         self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.ORDER_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_script_bot_parameters(self, botguid: str, fieldno: int, value: any):

        response = super()._execute_request("/OrderBotResetOrder", {"botGuid": botguid,
                                                                    "fieldNo": fieldno,
                                                                    "value": value})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])), response["ErrorMessage"],
                                         self._convert_json_bot_to_custom_bot_specific(EnumCustomBotType.SCRIPT_BOT, response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})