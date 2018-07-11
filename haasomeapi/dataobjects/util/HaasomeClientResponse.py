from haasomeapi.enums.EnumErrorCode import EnumErrorCode


class HaasomeClientResponse:
    """ Standard Haas API Response Object
    Contains the Haas Local API Response

    :param errorCode: :class:`~haasomeapi.enums.EnumErrorCode`: Error Code Returned if any
    :param errorMessage: str: Error message returned from the server if any
    :param result: any: Can contain anything so check functiona definition
    """

    def __init__(self, errorcode: EnumErrorCode, errormessage: str, result):
        self.errorCode: EnumErrorCode = errorcode
        self.errorMessage: str = errormessage
        self.result = result
