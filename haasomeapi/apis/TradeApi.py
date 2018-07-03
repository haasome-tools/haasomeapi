from haasomeapi.apis.ApiBase import ApiBase
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse


class TradeApi(ApiBase):

    def __init__(self, connectionstring: str, privatekey: str):
        ApiBase.__init__(self, connectionstring, privatekey)

    def place_spot_buy_order(self, accountguid: str, primarycoin: str, secondarycoin: str, price: float, amount: float,
                             timeout: int = 0, userguid: str = "", templateguid: str = ""):

        data = {"accountGuid": accountguid,
                "primaryCoin": primarycoin,
                "secondaryCoin": secondarycoin,
                "price": float(str(price).replace(',', '.')),
                "amount": float(str(amount).replace(',', '.'))}

        if timeout > 0:
            data["timeout"] = str(timeout)

        if not userguid:
            data["userGuid"] = userguid

        if not templateguid:
            data["templateGuid"] = templateguid

        response = super()._execute_request("/PlaceSpotBuyOrder", data)

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], response["Result"])
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def place_spot_sell_order(self, accountguid: str, primarycoin: str, secondarycoin: str, price: float, amount: float,
                             timeout: int = 0, userguid: str = "", templateguid: str = ""):

        data = {"accountGuid": accountguid,
                "primaryCoin": primarycoin,
                "secondaryCoin": secondarycoin,
                "price": float(str(price).replace(',', '.')),
                "amount": float(str(amount).replace(',', '.'))}

        if timeout > 0:
            data["timeout"] = str(timeout)

        if not userguid:
            data["userGuid"] = userguid

        if not templateguid:
            data["templateGuid"] = templateguid

        response = super()._execute_request("/PlaceSpotSellOrder", data)

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], response["Result"])
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def place_enter_long_order(self, accountguid: str, primarycoin: str, secondarycoin: str, price: float,
                               amount: float, leverage: float, timeout: int = 0, userguid: str = "",
                               templateguid: str = ""):

        data = {"accountGuid": accountguid,
                "primaryCoin": primarycoin,
                "secondaryCoin": secondarycoin,
                "price": float(str(price).replace(',', '.')),
                "amount": float(str(amount).replace(',', '.')),
                "leverage": float(str(leverage).replace(',', '.'))}

        if timeout > 0:
            data["timeout"] = str(timeout)

        if not userguid:
            data["userGuid"] = userguid

        if not templateguid:
            data["templateGuid"] = templateguid

        response = super()._execute_request("/PlaceLeverageEnterLongOrder", data)

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], response["Result"])
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def place_exit_long_order(self, accountguid: str, primarycoin: str, secondarycoin: str, price: float,
                               amount: float, leverage: float, timeout: int = 0, userguid: str = "",
                               templateguid: str = ""):

        data = {"accountGuid": accountguid,
                "primaryCoin": primarycoin,
                "secondaryCoin": secondarycoin,
                "price": float(str(price).replace(',', '.')),
                "amount": float(str(amount).replace(',', '.')),
                "leverage": float(str(leverage).replace(',', '.'))}

        if timeout > 0:
            data["timeout"] = str(timeout)

        if not userguid:
            data["userGuid"] = userguid

        if not templateguid:
            data["templateGuid"] = templateguid

        response = super()._execute_request("/PlaceLeverageExitLongOrder", data)

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], response["Result"])
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def place_enter_short_order(self, accountguid: str, primarycoin: str, secondarycoin: str, price: float,
                               amount: float, leverage: float, timeout: int = 0, userguid: str = "",
                               templateguid: str = ""):

        data = {"accountGuid": accountguid,
                "primaryCoin": primarycoin,
                "secondaryCoin": secondarycoin,
                "price": float(str(price).replace(',', '.')),
                "amount": float(str(amount).replace(',', '.')),
                "leverage": float(str(leverage).replace(',', '.'))}

        if timeout > 0:
            data["timeout"] = str(timeout)

        if not userguid:
            data["userGuid"] = userguid

        if not templateguid:
            data["templateGuid"] = templateguid

        response = super()._execute_request("/PlaceLeverageEnterShortOrder", data)

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], response["Result"])
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def place_exit_short_order(self, accountguid: str, primarycoin: str, secondarycoin: str, price: float,
                               amount: float, leverage: float, timeout: int = 0, userguid: str = "",
                               templateguid: str = ""):

        data = {"accountGuid": accountguid,
                "primaryCoin": primarycoin,
                "secondaryCoin": secondarycoin,
                "price": float(str(price).replace(',', '.')),
                "amount": float(str(amount).replace(',', '.')),
                "leverage": float(str(leverage).replace(',', '.'))}

        if timeout > 0:
            data["timeout"] = str(timeout)

        if not userguid:
            data["userGuid"] = userguid

        if not templateguid:
            data["templateGuid"] = templateguid

        response = super()._execute_request("/PlaceLeverageExitShortOrder", data)

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], response["Result"])
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def cancel_order(self, accountguid: str, orderguid: str):
        response = super()._execute_request("/CancelOrder",
                                            {"accountGuid": accountguid,
                                             "order": orderguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def cancel_template(self, templateguid: str):
        response = super()._execute_request("/CancelTemplate",
                                            {"templateGuid": templateguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})
