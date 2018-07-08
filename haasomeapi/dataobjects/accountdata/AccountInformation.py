from typing import Dict

from haasomeapi.enums.EnumPlatform import EnumPlatform
from haasomeapi.enums.EnumPriceSource import EnumPriceSource


class AccountInformation:
    """ Data Object containing the account information

    :ivar guid: str:
    :ivar name: str: 
    :ivar platformType: :class:`~haasomeapi.enums.EnumPlatform`:
    :ivar connectedPriceSource: :class:`~haasomeapi.enums.EnumPriceSource`:

    :ivar isSimulatedAccount: bool
    :ivar availableOrderTemplates: Dict[str, str]: 
    """
    
    guid: str
    name: str
    platformType: EnumPlatform
    connectedPriceSource: EnumPriceSource

    isSimulatedAccount: bool
    availableOrderTemplates: Dict[str, str]
