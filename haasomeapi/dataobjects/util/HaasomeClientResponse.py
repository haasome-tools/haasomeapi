from haasomeapi.enums.EnumErrorCode import EnumErrorCode


class HaasomeClientResponse:

    def __init__(self, errorcode: EnumErrorCode, errormessage: str, result):
        self.errorCode: EnumErrorCode = errorcode
        self.errorMessage: str = errormessage
        self.result = result
