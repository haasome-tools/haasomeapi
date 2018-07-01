from typing import List
from haasomeapi.enums.EnumInsurances import EnumInsurances

from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption


class Insurance:
    guid: str
    insuranceType: EnumInsurances

    insuranceTypeShortName: str
    insuranceTypeFullName: str

    agreeToTrade: bool
    insuranceName: str

    insuranceInterface: List[IndicatorOption]
