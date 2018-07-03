from haasomeapi.apis.ApiBase import ApiBase

from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.enums.EnumOrderType import EnumOrderType
from haasomeapi.dataobjects.advancedorders.StopTakeProfitOrder import StopTakeProfitOrder
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse
from haasomeapi.dataobjects.advancedorders.AdvancedOrderBase import AdvancedOrderBase


class AdvancedOrderApi(ApiBase):

    def __init__(self, connectionstring: str, privatekey: str):
        ApiBase.__init__(self, connectionstring, privatekey)

    def get_advanced_orders(self):
        response = super()._execute_request("/GetAdvancedOrders", {})

        advancedorders = {}

        for key, value in response["Result"].items():
            advancedorders[key] = super()._from_json(value, AdvancedOrderBase)

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], advancedorders)
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def activate_advanced_order(self, guid: str):

        response = super()._execute_request("/ActivateAdvancedOrder", {"guid": guid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], AdvancedOrderBase))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def deactivate_advanced_order(self, guid: str):

        response = super()._execute_request("/DeactivateAdvancedOrder", {"guid": guid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], AdvancedOrderBase))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def remove_advanced_order(self, guid: str):

        response = super()._execute_request("/RemoveAdvancedOrder", {"guid": guid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def add_stop_order(self, name: str, accountguid: str, primarycoin: str, secondarycoin: str,
                       direction: EnumOrderType, executingtemplateguid: str, triggerprice: float, executionprice: float,
                       amount: float, startorderonactivation: bool, startorderprice: float, starttemplateguid: str,
                       activate: bool):

        response = super()._execute_request("/AddStopOrder",
                                             {"name": name,
                                              "accountGuid": accountguid,
                                              "primaryCoin": primarycoin,
                                              "secondaryCoin": secondarycoin,
                                              "leverage": "0",
                                              "orderDirection": EnumOrderType(direction).name.capitalize(),
                                              "executingTemplateGuid": executingtemplateguid,
                                              "triggerPrice": float(str(triggerprice).replace(',', '.')),
                                              "executionPrice": float(str(executionprice).replace(',', '.')),
                                              "amount": float(str(amount).replace(',', '.')),
                                              "startOrderOnActivation": str(startorderonactivation).lower(),
                                              "startOrderPrice": float(str(startorderprice).replace(',', '.')),
                                              "startTemplateGuid": starttemplateguid,
                                              "activate": str(activate).lower()})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], StopTakeProfitOrder))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def add_stop_order_leverage(self, name: str, accountguid: str, primarycoin: str, secondarycoin: str,
                                contractname: str, leverage: float, direction: EnumOrderType,
                                executingtemplateguid: str, triggerprice: float, executionprice: float,
                                amount: float, startorderonactivation: bool, startorderprice: float,
                                starttemplateguid: str, activate: bool):

        response = super()._execute_request("/AddStopOrder",
                                            {"name": name,
                                             "accountGuid": accountguid,
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "contractname": contractname,
                                             "leverage": float(str(leverage).replace(',', '.')),
                                             "orderDirection": EnumOrderType(direction).name.capitalize(),
                                             "executingTemplateGuid": executingtemplateguid,
                                             "triggerPrice": float(str(triggerprice).replace(',', '.')),
                                             "executionPrice": float(str(executionprice).replace(',', '.')),
                                             "amount": float(str(amount).replace(',', '.')),
                                             "startOrderOnActivation": str(startorderonactivation).lower(),
                                             "startOrderPrice": float(str(startorderprice).replace(',', '.')),
                                             "startTemplateGuid": starttemplateguid,
                                             "activate": str(activate).lower()})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], StopTakeProfitOrder))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def add_take_profit_order(self, name: str, accountguid: str, primarycoin: str, secondarycoin: str,
                              direction: EnumOrderType, executingtemplateguid: str, triggerprice: float, executionprice: float,
                              amount: float, startorderonactivation: bool, startorderprice: float, starttemplateguid: str,
                              activate: bool):

        response = super()._execute_request("/AddTakeProfitOrder",
                                             {"name": name,
                                              "accountGuid": accountguid,
                                              "primaryCoin": primarycoin,
                                              "secondaryCoin": secondarycoin,
                                              "leverage": "0",
                                              "orderDirection": EnumOrderType(direction).name.capitalize(),
                                              "executingTemplateGuid": executingtemplateguid,
                                              "triggerPrice": float(str(triggerprice).replace(',', '.')),
                                              "executionPrice": float(str(executionprice).replace(',', '.')),
                                              "amount": float(str(amount).replace(',', '.')),
                                              "startOrderOnActivation": str(startorderonactivation).lower(),
                                              "startOrderPrice": float(str(startorderprice).replace(',', '.')),
                                              "startTemplateGuid": starttemplateguid,
                                              "activate": str(activate).lower()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], StopTakeProfitOrder))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def add_take_profit_order_leverage(self, name: str, accountguid: str, primarycoin: str, secondarycoin: str,
                                       contractname: str, leverage: float, direction: EnumOrderType,
                                       executingtemplateguid: str, triggerprice: float, executionprice: float,
                                       amount: float, startorderonactivation: bool, startorderprice: float,
                                       starttemplateguid: str, activate: bool):

        response = super()._execute_request("/AddTakeProfitOrder",
                                            {"name": name,
                                             "accountGuid": accountguid,
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "contractname": contractname,
                                             "leverage": float(str(leverage).replace(',', '.')),
                                             "orderDirection": EnumOrderType(direction).name.capitalize(),
                                             "executingTemplateGuid": executingtemplateguid,
                                             "triggerPrice": float(str(triggerprice).replace(',', '.')),
                                             "executionPrice": float(str(executionprice).replace(',', '.')),
                                             "amount": float(str(amount).replace(',', '.')),
                                             "startOrderOnActivation": str(startorderonactivation).lower(),
                                             "startOrderPrice": float(str(startorderprice).replace(',', '.')),
                                             "startTemplateGuid": starttemplateguid,
                                             "activate": str(activate).lower()})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], StopTakeProfitOrder))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def add_trailing_stop_order(self, name: str, accountguid: str, primarycoin: str, secondarycoin: str,
                              direction: EnumOrderType, executingtemplateguid: str, trailingstoppercentage: float,
                              amount: float, startorderonactivation: bool, startorderprice: float, starttemplateguid: str,
                              activate: bool):

        response = super()._execute_request("/AddTrailingStopOrder",
                                             {"name": name,
                                              "accountGuid": accountguid,
                                              "primaryCoin": primarycoin,
                                              "secondaryCoin": secondarycoin,
                                              "leverage": "0",
                                              "orderDirection": EnumOrderType(direction).name.capitalize(),
                                              "executingTemplateGuid": executingtemplateguid,
                                              "trailingStopPercentage": float(str(trailingstoppercentage).replace(',', '.')),
                                              "amount": float(str(amount).replace(',', '.')),
                                              "startOrderOnActivation": str(startorderonactivation).lower(),
                                              "startOrderPrice": float(str(startorderprice).replace(',', '.')),
                                              "startTemplateGuid": starttemplateguid,
                                              "activate": str(activate).lower()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], StopTakeProfitOrder))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def add_trailing_stop_leverage(self, name: str, accountguid: str, primarycoin: str, secondarycoin: str,
                                   contractname: str, leverage: float, direction: EnumOrderType, executingtemplateguid: str,
                                   trailingstoppercentage: float, amount: float, startorderonactivation: bool,
                                   startorderprice: float, starttemplateguid: str, activate: bool):

        response = super()._execute_request("/AddTrailingStopOrder",
                                             {"name": name,
                                              "accountGuid": accountguid,
                                              "primaryCoin": primarycoin,
                                              "secondaryCoin": secondarycoin,
                                              "contractName": contractname,
                                              "leverage": float(str(leverage).replace(',', '.')),
                                              "orderDirection": EnumOrderType(direction).name.capitalize(),
                                              "executingTemplateGuid": executingtemplateguid,
                                              "trailingStopPercentage": float(str(trailingstoppercentage).replace(',', '.')),
                                              "amount": float(str(amount).replace(',', '.')),
                                              "startOrderOnActivation": str(startorderonactivation).lower(),
                                              "startOrderPrice": float(str(startorderprice).replace(',', '.')),
                                              "startTemplateGuid": starttemplateguid,
                                              "activate": str(activate).lower()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], StopTakeProfitOrder))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_stop_order(self, guid: str, name: str, accountguid: str, primarycoin: str, secondarycoin: str,
                         direction: EnumOrderType, executingtemplateguid: str, triggerprice: float,
                         executionprice: float,
                         amount: float, startorderonactivation: bool, startorderprice: float, starttemplateguid: str,
                         activate: bool):

        response = super()._execute_request("/AddStopOrder",
                                            {"guid": guid,
                                             "name": name,
                                             "accountGuid": accountguid,
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "leverage": "0",
                                             "orderDirection": EnumOrderType(direction).name.capitalize(),
                                             "executingTemplateGuid": executingtemplateguid,
                                             "triggerPrice": float(str(triggerprice).replace(',', '.')),
                                             "executionPrice": float(str(executionprice).replace(',', '.')),
                                             "amount": float(str(amount).replace(',', '.')),
                                             "startOrderOnActivation": str(startorderonactivation).lower(),
                                             "startOrderPrice": float(str(startorderprice).replace(',', '.')),
                                             "startTemplateGuid": starttemplateguid,
                                             "activate": str(activate).lower()})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"],
                                         super()._from_json(response["Result"], StopTakeProfitOrder))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_stop_order_leverage(self, guid: str, name: str, accountguid: str, primarycoin: str, secondarycoin: str,
                                  contractname: str, leverage: float, direction: EnumOrderType,
                                  executingtemplateguid: str, triggerprice: float, executionprice: float,
                                  amount: float, startorderonactivation: bool, startorderprice: float,
                                  starttemplateguid: str, activate: bool):

        response = super()._execute_request("/AddStopOrder",
                                            {"guid": guid,
                                             "name": name,
                                             "accountGuid": accountguid,
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "contractname": contractname,
                                             "leverage": float(str(leverage).replace(',', '.')),
                                             "orderDirection": EnumOrderType(direction).name.capitalize(),
                                             "executingTemplateGuid": executingtemplateguid,
                                             "triggerPrice": float(str(triggerprice).replace(',', '.')),
                                             "executionPrice": float(str(executionprice).replace(',', '.')),
                                             "amount": float(str(amount).replace(',', '.')),
                                             "startOrderOnActivation": str(startorderonactivation).lower(),
                                             "startOrderPrice": float(str(startorderprice).replace(',', '.')),
                                             "startTemplateGuid": starttemplateguid,
                                             "activate": str(activate).lower()})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"],
                                         super()._from_json(response["Result"], StopTakeProfitOrder))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_take_profit_order(self, guid: str, name: str, accountguid: str, primarycoin: str, secondarycoin: str,
                              direction: EnumOrderType, executingtemplateguid: str, triggerprice: float, executionprice: float,
                              amount: float, startorderonactivation: bool, startorderprice: float, starttemplateguid: str,
                              activate: bool):

        response = super()._execute_request("/AddTakeProfitOrder",
                                             {"guid": guid,
                                              "name": name,
                                              "accountGuid": accountguid,
                                              "primaryCoin": primarycoin,
                                              "secondaryCoin": secondarycoin,
                                              "leverage": "0",
                                              "orderDirection": EnumOrderType(direction).name.capitalize(),
                                              "executingTemplateGuid": executingtemplateguid,
                                              "triggerPrice": float(str(triggerprice).replace(',', '.')),
                                              "executionPrice": float(str(executionprice).replace(',', '.')),
                                              "amount": float(str(amount).replace(',', '.')),
                                              "startOrderOnActivation": str(startorderonactivation).lower(),
                                              "startOrderPrice": float(str(startorderprice).replace(',', '.')),
                                              "startTemplateGuid": starttemplateguid,
                                              "activate": str(activate).lower()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], StopTakeProfitOrder))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_take_profit_order_leverage(self, guid: str, name: str, accountguid: str, primarycoin: str, secondarycoin: str,
                                         contractname: str, leverage: float, direction: EnumOrderType,
                                         executingtemplateguid: str, triggerprice: float, executionprice: float,
                                         amount: float, startorderonactivation: bool, startorderprice: float,
                                         starttemplateguid: str, activate: bool):

        response = super()._execute_request("/AddTakeProfitOrder",
                                            {"guid": guid,
                                             "name": name,
                                             "accountGuid": accountguid,
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "contractname": contractname,
                                             "leverage": float(str(leverage).replace(',', '.')),
                                             "orderDirection": EnumOrderType(direction).name.capitalize(),
                                             "executingTemplateGuid": executingtemplateguid,
                                             "triggerPrice": float(str(triggerprice).replace(',', '.')),
                                             "executionPrice": float(str(executionprice).replace(',', '.')),
                                             "amount": float(str(amount).replace(',', '.')),
                                             "startOrderOnActivation": str(startorderonactivation).lower(),
                                             "startOrderPrice": float(str(startorderprice).replace(',', '.')),
                                             "startTemplateGuid": starttemplateguid,
                                             "activate": str(activate).lower()})
        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], StopTakeProfitOrder))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_trailing_stop_order(self, guid: str, name: str, accountguid: str, primarycoin: str, secondarycoin: str,
                              direction: EnumOrderType, executingtemplateguid: str, trailingstoppercentage: float,
                              amount: float, startorderonactivation: bool, startorderprice: float, starttemplateguid: str,
                              activate: bool):

        response = super()._execute_request("/AddTrailingStopOrder",
                                             {"guid": guid,
                                              "name": name,
                                              "accountGuid": accountguid,
                                              "primaryCoin": primarycoin,
                                              "secondaryCoin": secondarycoin,
                                              "leverage": "0",
                                              "orderDirection": EnumOrderType(direction).name.capitalize(),
                                              "executingTemplateGuid": executingtemplateguid,
                                              "trailingStopPercentage": float(str(trailingstoppercentage).replace(',', '.')),
                                              "amount": float(str(amount).replace(',', '.')),
                                              "startOrderOnActivation": str(startorderonactivation).lower(),
                                              "startOrderPrice": float(str(startorderprice).replace(',', '.')),
                                              "startTemplateGuid": starttemplateguid,
                                              "activate": str(activate).lower()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], StopTakeProfitOrder))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_trailing_stop_leverage(self, guid: str, name: str, accountguid: str, primarycoin: str, secondarycoin: str,
                                   contractname: str, leverage: float, direction: EnumOrderType, executingtemplateguid: str,
                                   trailingstoppercentage: float, amount: float, startorderonactivation: bool,
                                   startorderprice: float, starttemplateguid: str, activate: bool):

        response = super()._execute_request("/AddTrailingStopOrder",
                                             {"guid": guid,
                                              "name": name,
                                              "accountGuid": accountguid,
                                              "primaryCoin": primarycoin,
                                              "secondaryCoin": secondarycoin,
                                              "contractName": contractname,
                                              "leverage": float(str(leverage).replace(',', '.')),
                                              "orderDirection": EnumOrderType(direction).name.capitalize(),
                                              "executingTemplateGuid": executingtemplateguid,
                                              "trailingStopPercentage": float(str(trailingstoppercentage).replace(',', '.')),
                                              "amount": float(str(amount).replace(',', '.')),
                                              "startOrderOnActivation": str(startorderonactivation).lower(),
                                              "startOrderPrice": float(str(startorderprice).replace(',', '.')),
                                              "startTemplateGuid": starttemplateguid,
                                              "activate": str(activate).lower()})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], StopTakeProfitOrder))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})