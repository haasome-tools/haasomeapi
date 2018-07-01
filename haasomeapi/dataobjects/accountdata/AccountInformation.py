from typing import Dict

from haasomeapi.enums.EnumPlatform import EnumPlatform
from haasomeapi.enums.EnumPriceSource import EnumPriceSource


class AccountInformation:
    guid: str
    name: str
    platformType: EnumPlatform
    connectedPriceSource: EnumPriceSource

    isSimulatedAccount: bool
    availableOrderTemplates: Dict[str, str]
