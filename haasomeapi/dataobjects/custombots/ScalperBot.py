from typing import List

from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot


class ScalperBot(BaseCustomBot):
    """ Data Object containing a Scalper Bot
    
    :ivar minimumTargetChange: float:
    :ivar maxAllowedReverseChange: float:
    """
    
    minimumTargetChange: float
    maxAllowedReverseChange: float
