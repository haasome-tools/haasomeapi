from haasomeapi.apis.ApiBase import ApiBase
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse


class TradeApi(ApiBase):

    def __init__(self, connectionstring: str, privatekey: str):
        ApiBase.__init__(self, connectionstring, privatekey)

    def place_spot_buy_order(self, accountguid: str, primarycoin: str, secondarycoin: str, price: float, amount: float):
        response = super()._execute_request("/PlaceSpotBuyOrder",
                                            {"accountGuid": accountguid,
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "price": float(str(price).replace(',', '.')),
                                             "amount": float(str(amount).replace(',', '.'))})
        print(response)
        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], response["Result"])

    def place_spot_sell_order(self, accountguid: str, primarycoin: str, secondarycoin: str, price: float, amount: float):
        response = super()._execute_request("/PlaceSpotSellOrder",
                                            {"accountGuid": accountguid,
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "price": float(str(price).replace(',', '.')),
                                             "amount": float(str(amount).replace(',', '.'))})
        print(response)
        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], response["Result"])

    def place_enter_long_order(self, accountguid: str, primarycoin: str, secondarycoin: str, price: float, amount: float, leverage: float):
        response = super()._execute_request("/PlaceLeverageEnterLongOrder",
                                            {"accountGuid": accountguid,
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "price": float(str(price).replace(',', '.')),
                                             "amount": float(str(amount).replace(',', '.')),
                                             "leverage": float(str(leverage).replace(',', '.'))})

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], response["Result"])

    def place_exit_long_order(self, accountguid: str, primarycoin: str, secondarycoin: str, price: float, amount: float, leverage: float):
        response = super()._execute_request("/PlaceLeverageExitLongOrder",
                                            {"accountGuid": accountguid,
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "price": float(str(price).replace(',', '.')),
                                             "amount": float(str(amount).replace(',', '.')),
                                             "leverage": float(str(leverage).replace(',', '.'))})

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], response["Result"])

    def place_enter_short_order(self, accountguid: str, primarycoin: str, secondarycoin: str, price: float, amount: float, leverage: float):
        response = super()._execute_request("/PlaceLeverageEnterShortOrder",
                                            {"accountGuid": accountguid,
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "price": float(str(price).replace(',', '.')),
                                             "amount": float(str(amount).replace(',', '.')),
                                             "leverage": float(str(leverage).replace(',', '.'))})

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], response["Result"])

    def place_exit_short_order(self, accountguid: str, primarycoin: str, secondarycoin: str, price: float, amount: float, leverage: float):
        response = super()._execute_request("/PlaceLeverageExitShortOrder",
                                            {"accountGuid": accountguid,
                                             "primaryCoin": primarycoin,
                                             "secondaryCoin": secondarycoin,
                                             "price": float(str(price).replace(',', '.')),
                                             "amount": float(str(amount).replace(',', '.')),
                                             "leverage": float(str(leverage).replace(',', '.'))})

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], response["Result"])

    def cancel_order(self, accountguid: str, orderguid: str):
        response = super()._execute_request("/CancelOrder",
                                            {"accountGuid": accountguid,
                                             "order": orderguid})

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], response["Result"])

    def cancel_template(self, templateguid: str):
        response = super()._execute_request("/CancelTemplate",
                                            {"templateGuid": templateguid})

        return HaasomeClientResponse(EnumErrorCode(int(response["ErrorCode"])),
                                     response["ErrorMessage"], response["Result"])