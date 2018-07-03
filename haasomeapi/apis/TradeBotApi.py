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

from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption

from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse


class TradeBotApi(ApiBase):

    def __init__(self, connectionstring: str, privatekey: str):
        ApiBase.__init__(self, connectionstring, privatekey)

    def _convert_json_bot_to_trade_bot_object(self, jsonstr: str):
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
            insurances[k] = safety

        botinitial.indicators = indicators
        botinitial.safeties = safeties
        botinitial.insurances = insurances

        return botinitial

    def get_all_trade_bots(self):
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

        response = self.get_all_bots()

        if response.errorCode != EnumErrorCode.SUCCESS:
            return HaasomeClientResponse(response.errorCode, response.errorMessage, {})

        for bot in response.result:
            if bot.guid == botguid:
                return HaasomeClientResponse(EnumErrorCode.SUCCESS, "", bot)

        return HaasomeClientResponse(EnumErrorCode.BOT_DOSENOT_EXIT, "Bot Could Not Be Found", {})

    def activate_trade_bot(self, botguid: str):
        response = super()._execute_request("/ActivateTradeBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def deactivate_trade_bot(self, botguid: str):
        response = super()._execute_request("/DeactivateBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def new_trade_bot(self, accountguid: str, botname: str, primarycoin: str, secondarycoin: str, contractname: str,
                leverage: float, groupid: str):

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
        response = super()._execute_request("/RemoveTradeBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def clean_trade_bot(self, botguid: str):
        response = super()._execute_request("/CleanTradeBot",  {"botGuid": botguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def lock_trade_bot(self, botguid: str, lockbot: bool):
        response = super()._execute_request("/LockTradeBot",  {"botGuid": botguid, "lockBot": str(lockbot).lower()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def backtest_trade_bot(self, botguid: str, minutes: int):

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
        response = super()._execute_request("/BackTestTradeBot",  {"botGuid": botguid,
                                                                   "startUnix": str(startUnix),
                                                                   "endUnix": str(endUnix)})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_trade_bot(self, botguid: str, botname: str, accountguid: str, primarycoin: str, secondarycoin: str,
                        contractname: str, leverage: float, groupid: str, useconsensus: bool, copymarketstoelements: bool):

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
        response = super()._execute_request("/AddSafety",  {"botGuid": botguid,
                                                            "safetyType": EnumSafety(safetytype).name.capitalize()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def add_indicator(self, botguid: str, indicatortype: EnumIndicator):
        response = super()._execute_request("/AddIndicator",  {"botGuid": botguid,
                                                               "indicatorType": EnumSafety(indicatortype).name.capitalize()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def add_insurance(self, botguid: str, insurancetype: EnumInsurance):
        response = super()._execute_request("/AddInsurance",  {"botGuid": botguid,
                                                               "indicatorType": EnumInsurance(insurancetype).name.capitalize()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def remove_safety(self, botguid: str, elementguid: str):
        response = super()._execute_request("/RemoveSafety",  {"botGuid": botguid,
                                                               "elementGuid": elementguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def remove_indicator(self, botguid: str, elementguid: str):
        response = super()._execute_request("/RemoveIndicator",  {"botGuid": botguid,
                                                                  "elementGuid": elementguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def remove_insurance(self, botguid: str, elementguid: str):
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
                     secondarycoin: str, contractname: str, mappedbuysignal: EnumFundPosition , mappedsellsignal: EnumFundPosition ):
        response = super()._execute_request("/SetupTradeBotSafety",  {"botGuid": botguid,
                                                                      "elementGuid": elementguid,
                                                                      "priceSourceName":EnumPriceSource(pricesource).name.capitalize(),
                                                                      "primaryCoin": primarycoin,
                                                                      "secondaryCoin": secondarycoin,
                                                                      "contractName": contractname,
                                                                      "mappedBuySignal": EnumFundPosition(mappedbuysignal).name.capitalize(),
                                                                      "mappedSellSignal": EnumFundPosition(mappedsellsignal).name.capitalize()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_indicator_spot_signals(self, botguid: str, elementguid: str, usebuysignal: bool, usesellsignal: bool,
                                     reversesignals: bool, standalone: bool):
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
        response = super()._execute_request("/SwitchTradeBotCoinPositions",  {"botGuid": botguid,
                                                                              "position": EnumCoinPosition(position).name.capitalize()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def switch_bot_funds_position(self, botguid: str, position: EnumFundPosition):
        response = super()._execute_request("/SwitchTradeBotFundsPositions",  {"botGuid": botguid,
                                                                               "fundsPosition": EnumFundPosition(position).name.capitalize()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def switch_bot_coin_position_with_order(self, botguid: str, templateguid: str):
        response = super()._execute_request("/SwitchTradeBotCoinPositionsWithOrder",  {"botGuid": botguid,
                                                                                       "templateGuid": templateguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def switch_bot_funds_position_with_order(self, botguid: str, templateguid: str, targetposition: EnumFundPosition ):
        response = super()._execute_request("/SwitchTradeBotFundsPositionsWithOrder",  {"botGuid": botguid,
                                                                                        "templateGuid": templateguid,
                                                                                        "fundsPosition": EnumFundPosition(targetposition).name.capitalize()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def clone_trade_bot(self, botguid: str, botname: str, accountguid: str, primarycoin: str, secondarycoin: str,
                        contractname: str, leverage: float, copysafeties: bool, copyindicators: bool, copyinsurances: bool,
                        copyparameters: bool, copymarkettoelements: bool):

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
        response = super()._execute_request("/CloneInsurance",  {"botGuid": botguid,
                                                                 "elementGuid": elementguid,
                                                                 "toBotGuid": tobotguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], self._convert_json_bot_to_trade_bot_object(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})