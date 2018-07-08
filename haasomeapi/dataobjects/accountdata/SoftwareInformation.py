from haasomeapi.enums.EnumSoftwareLicence import EnumSoftwareLicence


class SoftwareInformation:
    """    
    Data Object containing the software information

    :ivar isBeta: bool: True if on beta release
    :ivar versionNumber: str: Current software version number.
    :ivar licenceType: :class:`~haasomeapi.enums.EnumSoftwareLicence`: License Type
    """
    
    isBeta: bool
    versionNumber: str
    licenceType: EnumSoftwareLicence
