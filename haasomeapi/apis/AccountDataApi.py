from haasomeapi.apis.ApiBase import ApiBase

from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.enums.EnumOrderStatus import EnumOrderStatus
from haasomeapi.dataobjects.accountdata.Wallet import Wallet
from haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder
from haasomeapi.dataobjects.accountdata.OrderContainer import OrderContainer
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse


class AccountDataApi(ApiBase):

    def __init__(self, connectionstring: str, privatekey: str):
        ApiBase.__init__(self, connectionstring, privatekey)

    def get_enabled_accounts(self):

        response = super()._execute_request("/GetEnabledAccounts", {})

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], response["Result"])

    def get_all_wallets(self):

        accounts = self.get_enabled_accounts()

        if accounts.errorCode != EnumErrorCode.SUCCESS:
            return HaasomeClientResponse(accounts.errorCode, accounts.errorMessage, {})

        results = {}

        for key, value in accounts.result.items():
            wallet = self.get_wallet(key)
            results[key] = wallet.result

        return HaasomeClientResponse(EnumErrorCode.SUCCESS, "", results)

    def get_wallet(self, accountguid: str):

        response = super()._execute_request("/GetWallet", {"accountGuid": accountguid})

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], super()._from_json(response["Result"], Wallet))

    def get_all_open_orders(self):

        accounts = self.get_enabled_accounts()

        if accounts.errorCode != EnumErrorCode.SUCCESS:
            return HaasomeClientResponse(accounts.errorCode, accounts.errorMessage, {})

        results = {}

        for key, value in accounts.result.items():
            openorders = self.get_open_orders(key)
            results[key] = openorders.result

        return HaasomeClientResponse(EnumErrorCode.SUCCESS, "", results)

    def get_open_orders(self, accountguid: str):

        response = super()._execute_request("/GetOpenOrders", {"accountGuid": accountguid})

        order_container = super()._from_json(response["Result"], OrderContainer)

        exchangeorderlist = {}
        marginorderlist = {}
        leverageorderlist = {}

        for orderstr, order in order_container.exchangeOrderList.items():
            exchangeorderlist[orderstr] = super()._from_json(order, BaseOrder)

        for orderstr, order in order_container.marginOrderList.items():
            marginorderlist[orderstr] = super()._from_json(order, BaseOrder)

        for orderstr, order in order_container.leverageOrderList.items():
            leverageorderlist[orderstr] = super()._from_json(order, BaseOrder)

        order_container.exchangeOrderList = exchangeorderlist
        order_container.marginOrderList = marginorderlist
        order_container.leverageOrderList = leverageorderlist

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], order_container)

    def get_template_status(self, templateguid: str):

        response = super()._execute_request("/GetTemplateStatus", {"templateGuid": templateguid})

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], EnumOrderStatus(int(response["Result"])))
