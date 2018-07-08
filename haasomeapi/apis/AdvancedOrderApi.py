from haasomeapi.apis.ApiBase import ApiBase

from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.enums.EnumOrderType import EnumOrderType
from haasomeapi.dataobjects.advancedorders.StopTakeProfitOrder import StopTakeProfitOrder
from haasomeapi.dataobjects.advancedorders.TrailingStop import TrailingStop
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse
from haasomeapi.dataobjects.advancedorders.AdvancedOrderBase import AdvancedOrderBase


class AdvancedOrderApi(ApiBase):
    """ The Advanced Order API Class.
    Gives access to the advanced order endpoints

    :param connectionstring: str: Connection String Formatted Ex. http://127.0.0.1:9000
    :param privatekey: str: Private Key Set In The Haas Settings
    """

    def __init__(self, connectionstring: str, privatekey: str):
        ApiBase.__init__(self, connectionstring, privatekey)

    def get_advanced_orders(self):
        """ Retrieves the current created advanced orders

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result Dict[:class:`~haasomeapi.dataobjects.advancedorders.AdvancedOrderBase`]
        """

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
        """ Activates an advanced order

        :param guid: str: advanced order guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.advancedorders.AdvancedOrderBase`   
        """

        response = super()._execute_request("/ActivateAdvancedOrder", {"guid": guid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], AdvancedOrderBase))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def deactivate_advanced_order(self, guid: str):
        """ Deactivates an advanced order

        :param guid: str: advanced order guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~haasomeapi.dataobjects.advancedorders.AdvancedOrderBase`
        """

        response = super()._execute_request("/DeactivateAdvancedOrder", {"guid": guid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], AdvancedOrderBase))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def remove_advanced_order(self, guid: str):
        """ Removes (deletes) advanced order

        :param guid: str: advanced order guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result bool if success
        """

        response = super()._execute_request("/RemoveAdvancedOrder", {"guid": guid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def add_stop_order(self, accountguid: str, name: str, primarycoin: str, secondarycoin: str,
                       direction: EnumOrderType, executingtemplateguid: str, triggerprice: float, executionprice: float,
                       amount: float, startorderonactivation: bool, startorderprice: float, starttemplateguid: str,
                       activate: bool):
        """ 
        Create a stop order for a spot market

        :param accountguid: str: The account guid
        :param name: str: Name of the advanced order
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param direction: EnumOrderType: Order Direction (Buy / Sell)  
        :param executingtemplateguid: str: Executing Template To Use
        :param triggerprice: float:  Trigger price to execute the stop
        :param executionprice: float: Price for the order to be placed at
        :param amount: float: Trade Amount
        :param startorderonactivation: bool: Start the adavnced order only on activation 
        :param startorderprice: float: What price to start the order
        :param starttemplateguid: str: The template guid to use for the order
        :param activate: bool: Activate the order.

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~from haasomeapi.dataobjects.advancedorders.StopTakeProfitOrder`
        """

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

    def add_stop_order_leverage(self, accountguid: str, name: str, primarycoin: str, secondarycoin: str,
                                contractname: str, leverage: float, direction: EnumOrderType,
                                executingtemplateguid: str, triggerprice: float, executionprice: float,
                                amount: float, startorderonactivation: bool, startorderprice: float,
                                starttemplateguid: str, activate: bool):
        """ Create a stop order for a leverage/margin market

        :param accountguid: str: The account guid
        :param name: str: Name of the advanced order
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str: Name of the contract (Options)
        :param leverage: float:  Leverage percentage
        :param direction: EnumOrderType: Order Direction (Long/Short)
        :param executingtemplateguid: str: Executing Template To Use
        :param triggerprice: float:  Trigger price to execute the stop
        :param executionprice: float: Price for the order to be placed at
        :param amount: float: Trade Amount
        :param startorderonactivation: bool: Start the adavnced order only on activation 
        :param startorderprice: float: What price to start the order
        :param starttemplateguid: str: The template guid to use for the order
        :param activate: bool: Activate the order.

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~from haasomeapi.dataobjects.advancedorders.StopTakeProfitOrder`
        """

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

    def add_take_profit_order(self, accountguid: str, name: str,  primarycoin: str, secondarycoin: str,
                              direction: EnumOrderType, executingtemplateguid: str, triggerprice: float, executionprice: float,
                              amount: float, startorderonactivation: bool, startorderprice: float, starttemplateguid: str,
                              activate: bool):
        """ Createa take profit order for a spot market

        :param accountguid: str: The account guid
        :param name: str: Name of the advanced order
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param direction: EnumOrderType: Order Direction (Buy / Sell)  
        :param executingtemplateguid: str: Executing Template To Use
        :param triggerprice: float:  Trigger price to execute the stop
        :param executionprice: float: Price for the order to be placed at
        :param amount: float: Trade Amount
        :param startorderonactivation: bool: Start the adavnced order only on activation 
        :param startorderprice: float: What price to start the order
        :param starttemplateguid: str: The template guid to use for the order
        :param activate: bool: Activate the order.

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~from haasomeapi.dataobjects.advancedorders.StopTakeProfitOrder`
        """

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
        """ Create a take profit order for a leverage/margin market

        :param accountguid: str: The account guid
        :param name: str: Name of the advanced order
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str: Name of the contract (Options)
        :param leverage: float:  Leverage percentage
        :param direction: EnumOrderType: Order Direction (Long/Short)
        :param executingtemplateguid: str: Executing Template To Use
        :param triggerprice: float:  Trigger price to execute the stop
        :param executionprice: float: Price for the order to be placed at
        :param amount: float: Trade Amount
        :param startorderonactivation: bool: Start the adavnced order only on activation 
        :param startorderprice: float: What price to start the order
        :param starttemplateguid: str: The template guid to use for the order
        :param activate: bool: Activate the order.

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~from haasomeapi.dataobjects.advancedorders.StopTakeProfitOrder`
        """

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

    def add_trailing_stop_order(self, accountguid: str, name: str,  primarycoin: str, secondarycoin: str,
                              direction: EnumOrderType, executingtemplateguid: str, trailingstoppercentage: float,
                              amount: float, startorderonactivation: bool, startorderprice: float, starttemplateguid: str,
                              activate: bool):
        """ Create a trailing stop order for a spot market

        :param accountguid: str: The account guid
        :param name: str: Name of the advanced order
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param direction: EnumOrderType: Order Direction (Buy / Sell)  
        :param executingtemplateguid: str: Executing Template To Use
        :param trailingstoppercentage: float: Percentage for trailing top to follow
        :param amount: float: Trade Amount
        :param startorderonactivation: bool: Start the adavnced order only on activation 
        :param startorderprice: float: What price to start the order
        :param starttemplateguid: str: The template guid to use for the order
        :param activate: bool: Activate the order.

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~from haasomeapi.dataobjects.advancedorders.StopTakeProfitOrder`
        """

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
                                         response["ErrorMessage"], super()._from_json(response["Result"], TrailingStop))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def add_trailing_stop_leverage(self, accountguid: str, name: str, primarycoin: str, secondarycoin: str,
                                   contractname: str, leverage: float, direction: EnumOrderType, executingtemplateguid: str,
                                   trailingstoppercentage: float, amount: float, startorderonactivation: bool,
                                   startorderprice: float, starttemplateguid: str, activate: bool):
        """ Create trailing stop order for a leverage/margin market

        :param accountguid: str: The account guid
        :param name: str: Name of the advanced order
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str: Name of the contract (Options)
        :param leverage: float:  Leverage percentage
        :param direction: EnumOrderType: Order Direction (Long/Short)
        :param executingtemplateguid: str: Executing Template To Use
        :param trailingstoppercentage: float: Percentage for trailing top to follow
        :param amount: float: Trade Amount
        :param startorderonactivation: bool: Start the adavnced order only on activation 
        :param startorderprice: float: What price to start the order
        :param starttemplateguid: str: The template guid to use for the order
        :param activate: bool: Activate the order.

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~from haasomeapi.dataobjects.advancedorders.StopTakeProfitOrder`
        """

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
                                         response["ErrorMessage"], super()._from_json(response["Result"], TrailingStop))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_stop_order(self, accountguid: str, orderguid: str, name: str, primarycoin: str, secondarycoin: str,
                         direction: EnumOrderType, executingtemplateguid: str, triggerprice: float,
                         executionprice: float,
                         amount: float, startorderonactivation: bool, startorderprice: float, starttemplateguid: str,
                         activate: bool):
        """ Modify a stop order for a spot market

        :param accountguid: str: The account guid
        :param orderguid: str: The advanced order guid to modify
        :param name: str: Name of the advanced order
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param direction: EnumOrderType: Order Direction (Buy / Sell)  
        :param executingtemplateguid: str: Executing Template To Use
        :param triggerprice: float:  Trigger price to execute the stop
        :param executionprice: float: Price for the order to be placed at
        :param amount: float: Trade Amount
        :param startorderonactivation: bool: Start the adavnced order only on activation 
        :param startorderprice: float: What price to start the order
        :param starttemplateguid: str: The template guid to use for the order
        :param activate: bool: Activate the order.

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~from haasomeapi.dataobjects.advancedorders.StopTakeProfitOrder`
        """

        response = super()._execute_request("/AddStopOrder",
                                            {"guid": orderguid,
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

    def setup_stop_order_leverage(self, accountguid: str, orderguid: str, name: str, primarycoin: str, secondarycoin: str,
                                  contractname: str, leverage: float, direction: EnumOrderType,
                                  executingtemplateguid: str, triggerprice: float, executionprice: float,
                                  amount: float, startorderonactivation: bool, startorderprice: float,
                                  starttemplateguid: str, activate: bool):
        """ Modify a stop order for a leverage/margin market

        :param accountguid: str: The account guid
        :param orderguid: str: The advanced order guid to modify
        :param name: str: Name of the advanced order
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str: Name of the contract (Options)
        :param leverage: float:  Leverage percentage
        :param direction: EnumOrderType: Order Direction (Long/Short)
        :param executingtemplateguid: str: Executing Template To Use
        :param triggerprice: float:  Trigger price to execute the stop
        :param executionprice: float: Price for the order to be placed at
        :param amount: float: Trade Amount
        :param startorderonactivation: bool: Start the adavnced order only on activation
        :param startorderprice: float: What price to start the order
        :param starttemplateguid: str: The template guid to use for the order
        :param activate: bool: Activate the order.

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~from haasomeapi.dataobjects.advancedorders.StopTakeProfitOrder`
        """
        response = super()._execute_request("/AddStopOrder",
                                             {"guid": orderguid,
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

    def setup_take_profit_order(self, accountguid: str, orderguid: str, name: str, primarycoin: str, secondarycoin: str,
                              direction: EnumOrderType, executingtemplateguid: str, triggerprice: float, executionprice: float,
                              amount: float, startorderonactivation: bool, startorderprice: float, starttemplateguid: str,
                              activate: bool):
        """ Modify take profit order for a spot market

        :param accountguid: str: The account guid
        :param orderguid: str: The advanced order guid to modify
        :param name: str: Name of the advanced order
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param direction: EnumOrderType: Order Direction (Buy / Sell)  
        :param executingtemplateguid: str: Executing Template To Use
        :param triggerprice: float:  Trigger price to execute the stop
        :param executionprice: float: Price for the order to be placed at
        :param amount: float: Trade Amount
        :param startorderonactivation: bool: Start the adavnced order only on activation 
        :param startorderprice: float: What price to start the order
        :param starttemplateguid: str: The template guid to use for the order
        :param activate: bool: Activate the order.

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~from haasomeapi.dataobjects.advancedorders.StopTakeProfitOrder`

        """

        response = super()._execute_request("/AddTakeProfitOrder",
                                             {"guid": orderguid,
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

    def setup_take_profit_order_leverage(self, accountguid: str, orderguid: str, name: str, primarycoin: str, secondarycoin: str,
                                         contractname: str, leverage: float, direction: EnumOrderType,
                                         executingtemplateguid: str, triggerprice: float, executionprice: float,
                                         amount: float, startorderonactivation: bool, startorderprice: float,
                                         starttemplateguid: str, activate: bool):
        """ Modify a take profit order for a leverage/margin market

        :param accountguid: str: The account guid
        :param orderguid: str: The advanced order guid to modify
        :param name: str: Name of the advanced order
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str: Name of the contract (Options)
        :param leverage: float:  Leverage percentage
        :param direction: EnumOrderType: Order Direction (Long/Short)
        :param executingtemplateguid: str: Executing Template To Use
        :param triggerprice: float:  Trigger price to execute the stop
        :param executionprice: float: Price for the order to be placed at
        :param amount: float: Trade Amount
        :param startorderonactivation: bool: Start the adavnced order only on activation 
        :param startorderprice: float: What price to start the order
        :param starttemplateguid: str: The template guid to use for the order
        :param activate: bool: Activate the order.

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~from haasomeapi.dataobjects.advancedorders.StopTakeProfitOrder`
        """

        response = super()._execute_request("/AddTakeProfitOrder",
                                            {"guid": orderguid,
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

    def setup_trailing_stop_order(self, accountguid: str, orderguid: str, name: str, primarycoin: str, secondarycoin: str,
                              direction: EnumOrderType, executingtemplateguid: str, trailingstoppercentage: float,
                              amount: float, startorderonactivation: bool, startorderprice: float, starttemplateguid: str,
                              activate: bool):
        """ Modify a trailing stop order for a spot market

        :param accountguid: str: The account guid
        :param orderguid: str: The advanced order guid to modify
        :param name: str: Name of the advanced order
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param direction: EnumOrderType: Order Direction (Buy / Sell)  
        :param executingtemplateguid: str: Executing Template To Use
        :param trailingstoppercentage: float: Percentage for trailing top to follow
        :param amount: float: Trade Amount
        :param startorderonactivation: bool: Start the adavnced order only on activation 
        :param startorderprice: float: What price to start the order
        :param starttemplateguid: str: The template guid to use for the order
        :param activate: bool: Activate the order.

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~from haasomeapi.dataobjects.advancedorders.StopTakeProfitOrder`
        """

        response = super()._execute_request("/AddTrailingStopOrder",
                                             {"guid": orderguid,
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
                                         response["ErrorMessage"], super()._from_json(response["Result"], TrailingStop))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def setup_trailing_stop_leverage(self, accountguid: str, orderguid: str, name: str, primarycoin: str, secondarycoin: str,
                                   contractname: str, leverage: float, direction: EnumOrderType, executingtemplateguid: str,
                                   trailingstoppercentage: float, amount: float, startorderonactivation: bool,
                                   startorderprice: float, starttemplateguid: str, activate: bool):
        """ Modify trailing stop order for a leverage/margin market

        :param accountguid: str: The account guid
        :param orderguid: str: The advanced order guid to modify
        :param name: str: Name of the advanced order
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param contractname: str: Name of the contract (Options)
        :param leverage: float:  Leverage percentage
        :param direction: EnumOrderType: Order Direction (Long/Short)
        :param executingtemplateguid: str: Executing Template To Use
        :param trailingstoppercentage: float: Percentage for trailing top to follow
        :param amount: float: Trade Amount
        :param startorderonactivation: bool: Start the adavnced order only on activation 
        :param startorderprice: float: What price to start the order
        :param starttemplateguid: str: The template guid to use for the order
        :param activate: bool: Activate the order.

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result :class:`~from haasomeapi.dataobjects.advancedorders.StopTakeProfitOrder`
        """

        response = super()._execute_request("/AddTrailingStopOrder",
                                             {"guid": orderguid,
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
                                         response["ErrorMessage"], super()._from_json(response["Result"], TrailingStop))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})
