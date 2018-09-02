from haasomeapi.apis.ApiBase import ApiBase
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse


class TradeApi(ApiBase):
    """ The Trade API Class.
    Gives access to the trade api endpoints

    :param connectionstring: str: Connection String Formatted Ex. http://127.0.0.1:9000
    :param privatekey: str: Private Key Set In The Haas Settings
    """

    def __init__(self, connectionstring: str, privatekey: str):
        ApiBase.__init__(self, connectionstring, privatekey)

    def place_spot_buy_order(self, accountguid: str, primarycoin: str, secondarycoin: str, price: float, amount: float,
                             timeout: int = 0, userguid: str = "", templateguid: str = ""):
        """ Place a spot buy order

        :param accountguid: str: The account guid
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param price: float: Price to place order at
        :param amount: float: Trade Amount
        :param timeout: int:  (Default value = 0) Order Timeout in minutes
        :param userguid: str:  (Default value = "") User guid for order
        :param templateguid: str:  (Default value = "") Order template guid to use
        
        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result str: Template guid
        """

        data = {"accountGuid": accountguid,
                "primaryCoin": primarycoin,
                "secondaryCoin": secondarycoin,
                "price": float(str(price).replace(',', '.')),
                "amount": float(str(amount).replace(',', '.'))}

        if timeout > 0:
            data["timeout"] = str(timeout)

        if userguid:
            data["userGuid"] = userguid

        if templateguid:
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
        """ Place a spot sell order

        :param accountguid: str: The account guid
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param price: float: Price to place order at
        :param amount: float: Trade Amount
        :param timeout: int:  (Default value = 0) Order Timeout in minutes
        :param userguid: str:  (Default value = "") User guid for order
        :param templateguid: str:  (Default value = "") Order template guid to use
        
        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result str: Template guid
        """

        data = {"accountGuid": accountguid,
                "primaryCoin": primarycoin,
                "secondaryCoin": secondarycoin,
                "price": float(str(price).replace(',', '.')),
                "amount": float(str(amount).replace(',', '.'))}

        if timeout > 0:
            data["timeout"] = str(timeout)

        if userguid:
            data["userGuid"] = userguid

        if templateguid:
            data["templateGuid"] = templateguid

        response = super()._execute_request("/PlaceSpotSellOrder", data)

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], response["Result"])
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def place_enter_long_order(self, accountguid: str, primarycoin: str, secondarycoin: str, price: float,
                               amount: float, leverage: float, timeout: int = 0, contractname: str = "", userguid: str = "",
                               templateguid: str = ""):
        """ Place a long order for Leverage/Margin

        :param accountguid: str: The account guid
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param price: float: Price to place order at
        :param amount: float: Trade Amount
        :param leverage: float: Leverage percentage amount
        :param timeout: int:  (Default value = 0) Order Timeout in minutes
        :param contractname: str: (Default value = "") Contract name to use
        :param userguid: str:  (Default value = "") User guid for order
        :param templateguid: str:  (Default value = "") Order template guid to use

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result str: Template guid
        """

        data = {"accountGuid": accountguid,
                "primaryCoin": primarycoin,
                "secondaryCoin": secondarycoin,
                "price": float(str(price).replace(',', '.')),
                "amount": float(str(amount).replace(',', '.')),
                "leverage": float(str(leverage).replace(',', '.'))}

        if timeout > 0:
            data["timeout"] = str(timeout)

        if contractname:
            data["contractName"] = contractname

        if userguid:
            data["userGuid"] = userguid

        if templateguid:
            data["templateGuid"] = templateguid

        response = super()._execute_request("/PlaceLeverageEnterLongOrder", data)

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], response["Result"])
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def place_exit_long_order(self, accountguid: str, primarycoin: str, secondarycoin: str, price: float,
                               amount: float, leverage: float, timeout: int = 0, contractname: str = "", userguid: str = "",
                               templateguid: str = ""):
        """ Place a exit long order for Leverage/Margin

        :param accountguid: str: The account guid
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param price: float: Price to place order at
        :param amount: float: Trade Amount
        :param leverage: float: Leverage percentage amount
        :param timeout: int:  (Default value = 0) Order Timeout in minutes
        :param contractname: str: (Default value = "") Contract name to use
        :param userguid: str:  (Default value = "") User guid for order
        :param templateguid: str:  (Default value = "") Order template guid to use

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result str: Template guid
        """

        data = {"accountGuid": accountguid,
                "primaryCoin": primarycoin,
                "secondaryCoin": secondarycoin,
                "price": float(str(price).replace(',', '.')),
                "amount": float(str(amount).replace(',', '.')),
                "leverage": float(str(leverage).replace(',', '.'))}

        if timeout > 0:
            data["timeout"] = str(timeout)

        if contractname:
            data["contractName"] = contractname

        if userguid:
            data["userGuid"] = userguid

        if templateguid:
            data["templateGuid"] = templateguid

        response = super()._execute_request("/PlaceLeverageExitLongOrder", data)

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], response["Result"])
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def place_enter_short_order(self, accountguid: str, primarycoin: str, secondarycoin: str, price: float,
                               amount: float, leverage: float, timeout: int = 0, contractname: str = "", userguid: str = "",
                               templateguid: str = ""):
        """ Place a short order for Leverage/Margin

        :param accountguid: str: The account guid
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param price: float: Price to place order at
        :param amount: float: Trade Amount
        :param leverage: float: Leverage percentage amount
        :param timeout: int:  (Default value = 0) Order Timeout in minutes
        :param contractname: str: (Default value = "") Contract name to use
        :param userguid: str:  (Default value = "") User guid for order
        :param templateguid: str:  (Default value = "") Order template guid to use

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result str: Template guid
        """

        data = {"accountGuid": accountguid,
                "primaryCoin": primarycoin,
                "secondaryCoin": secondarycoin,
                "price": float(str(price).replace(',', '.')),
                "amount": float(str(amount).replace(',', '.')),
                "leverage": float(str(leverage).replace(',', '.'))}

        if timeout > 0:
            data["timeout"] = str(timeout)

        if contractname:
            data["contractName"] = contractname

        if userguid:
            data["userGuid"] = userguid

        if templateguid:
            data["templateGuid"] = templateguid

        response = super()._execute_request("/PlaceLeverageEnterShortOrder", data)

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], response["Result"])
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def place_exit_short_order(self, accountguid: str, primarycoin: str, secondarycoin: str, price: float,
                               amount: float, leverage: float, timeout: int = 0, contractname: str = "", userguid: str = "",
                               templateguid: str = ""):
        """ Place a exit short order for Leverage/Margin

        :param accountguid: str: The account guid
        :param primarycoin: str: Primary currency Ex. If BNB/BTC then set this to BNB
        :param secondarycoin: str: Secondary currency Ex. If BNB/BTC then set this to BTC
        :param price: float: Price to place order at
        :param amount: float: Trade Amount
        :param leverage: float: Leverage percentage amount
        :param timeout: int:  (Default value = 0) Order Timeout in minutes
        :param contractname: str: (Default value = "") Contract name to use
        :param userguid: str:  (Default value = "") User guid for order
        :param templateguid: str:  (Default value = "") Order template guid to use

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result str: Template guid
        """

        data = {"accountGuid": accountguid,
                "primaryCoin": primarycoin,
                "secondaryCoin": secondarycoin,
                "price": float(str(price).replace(',', '.')),
                "amount": float(str(amount).replace(',', '.')),
                "leverage": float(str(leverage).replace(',', '.'))}

        if timeout > 0:
            data["timeout"] = str(timeout)

        if contractname:
            data["contractName"] = contractname

        if userguid:
            data["userGuid"] = userguid

        if templateguid:
            data["templateGuid"] = templateguid

        response = super()._execute_request("/PlaceLeverageExitShortOrder", data)

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], response["Result"])
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})

    def cancel_order(self, accountguid: str, orderguid: str):
        """ Cancel a pending order

        :param accountguid: str: The account guid
        :param orderguid: str: Order guid to cancel

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result bool: If order cancelled succesfully
        """

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
        """ Cancel a pending template order

        :param templateguid: str: Template order guid

        :returns: :class:`~haasomeapi.dataobjects.util.HaasomeClientResponse`
        :returns: In .result bool: If template cancelled succesfully
        """
        
        response = super()._execute_request("/CancelTemplate",
                                            {"templateGuid": templateguid})

        try:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], bool(response["Result"]))
        except:
            return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                         response["ErrorMessage"], {})