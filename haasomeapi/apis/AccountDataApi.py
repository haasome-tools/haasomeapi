from haasomeapi.apis.ApiBase import ApiBase

from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.enums.EnumOrderStatus import EnumOrderStatus
from haasomeapi.dataobjects.accountdata.Wallet import Wallet
from haasomeapi.dataobjects.accountdata.BaseOrder import BaseOrder
from haasomeapi.dataobjects.accountdata.OrderContainer import OrderContainer
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse

from haasomeapi.dataobjects.accountdata.AccountInformation import AccountInformation
from haasomeapi.dataobjects.accountdata.SoftwareInformation import SoftwareInformation


class AccountDataApi(ApiBase):

    def __init__(self, connectionstring: str, privatekey: str):
        ApiBase.__init__(self, connectionstring, privatekey)

    def get_software_details(self):
        response = super()._execute_request("/GetSoftwareDetails", {})

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], super()._from_json(response["Result"], SoftwareInformation))

    def get_enabled_accounts(self):

        response = super()._execute_request("/GetEnabledAccounts", {})

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], response["Result"])

    def get_all_account_details(self):

        response = super()._execute_request("/GetAllAccountDetails", {})

        accounts = {}

        for key, value in response["Result"].items():
            accounts[key] = (super()._from_json(value, AccountInformation))

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], accounts)
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def get_account_details(self, accountguid: str):
        response = super()._execute_request("/GetAccountDetails",  {"accountGuid": accountguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], AccountInformation))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def simulated_account_clear_wallet(self, accountguid: str):
        response = super()._execute_request("/SimulatedAccountClearWallet",  {"accountGuid": accountguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], Wallet))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def simulated_account_add_or_adjust_coin_amount(self, accountguid: str, coin: str, amount: float):
        response = super()._execute_request("/SimulatedAccountAddOrAdjustCoinAmount",  {"accountGuid": accountguid,
                                                                                        "coin": coin,
                                                                                        "amount": float(str(amount).replace(',', '.'))})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], Wallet))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def get_order_templates(self):
        response = super()._execute_request("/GetOrderTemplates",  {})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], response["Result"])
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def get_all_wallets(self):

        accounts = self.get_enabled_accounts()

        if accounts.errorCode != EnumErrorCode.SUCCESS:
            return HaasomeClientResponse(accounts.errorCode, accounts.errorMessage, {})

        results = {}

        for key, value in accounts.result.items():
            wallet = self.get_wallet(key)
            results[key] = wallet.result

        try:
            return HaasomeClientResponse(EnumErrorCode.SUCCESS, "", results)
        except:
            return HaasomeClientResponse(EnumErrorCode.FAILURE, "", {})

    def get_wallet(self, accountguid: str):

        response = super()._execute_request("/GetWallet", {"accountGuid": accountguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], super()._from_json(response["Result"], Wallet))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def get_all_open_orders(self):

        accounts = self.get_enabled_accounts()

        if accounts.errorCode != EnumErrorCode.SUCCESS:
            return HaasomeClientResponse(accounts.errorCode, accounts.errorMessage, {})

        results = {}

        for key, value in accounts.result.items():
            openorders = self.get_open_orders(key)
            results[key] = openorders.result

        try:
            return HaasomeClientResponse(EnumErrorCode.SUCCESS, "", results)
        except:
            return HaasomeClientResponse(EnumErrorCode.FAILURE, "", {})

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

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], order_container)
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def get_template_status(self, templateguid: str):

        response = super()._execute_request("/GetTemplateStatus", {"templateGuid": templateguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], EnumOrderStatus(int(response["Result"])))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})