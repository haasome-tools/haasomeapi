from typing import Dict

from haasomeapi.enums.EnumPlatform import EnumPlatform
from haasomeapi.enums.EnumPriceSource import EnumPriceSource


class AccountInformation:
    """    
    Data Object containing the account information

    :ivar guid: str: Account guid
    :ivar name: str: Account name
    :ivar platformType: :class:`~haasomeapi.enums.EnumPlatform`: Platform
    :ivar connectedPriceSource: :class:`~haasomeapi.enums.EnumPriceSource`: Connected Price Source

    :ivar isSimulatedAccount: bool: Is a simulated account
    :ivar availableOrderTemplates: Dict[str, str]: Available order templates
    """
    
    guid: str
    name: str
    platformType: EnumPlatform
    connectedPriceSource: EnumPriceSource

    isSimulatedAccount: bool
    availableOrderTemplates: Dict[str, str]
