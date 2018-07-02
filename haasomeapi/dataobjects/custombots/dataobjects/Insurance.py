from typing import List
from haasomeapi.enums.EnumInsurance import EnumInsurance

from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption


class Insurance:
    guid: str
    insuranceType: EnumInsurance

    insuranceTypeShortName: str
    insuranceTypeFullName: str

    agreeToTrade: bool
    insuranceName: str

    insuranceInterface: List[IndicatorOption]
