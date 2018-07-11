from typing import List
from haasomeapi.enums.EnumInsurance import EnumInsurance

from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption


class Insurance:
    """ Data Object containing a Insurance

    :ivar guid: str:
    :ivar insuranceType: :class:`~haasomeapi.enums.EnumInsurance`:
    :ivar insuranceTypeShortName: str:
    :ivar insuranceTypeFullName: str:
    :ivar agreeToTrade: bool:
    :ivar insuranceName: str:
    :ivar insuranceInterface: List[:class:`~aasomeapi.dataobjects.custombots.dataobjects.IndicatorOption`]:
    """

    guid: str
    insuranceType: EnumInsurance

    insuranceTypeShortName: str
    insuranceTypeFullName: str

    agreeToTrade: bool
    insuranceName: str

    insuranceInterface: List[IndicatorOption]
