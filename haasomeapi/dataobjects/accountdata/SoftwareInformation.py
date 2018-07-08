from haasomeapi.enums.EnumSoftwareLicence import EnumSoftwareLicence


class SoftwareInformation:
    """ Data Object containing the software information

    :ivar isBeta: bool:
    :ivar versionNumber: str: 
    :ivar licenceType: :class:`~haasomeapi.enums.EnumSoftwareLicence`:
    """
    
    isBeta: bool
    versionNumber: str
    licenceType: EnumSoftwareLicence
