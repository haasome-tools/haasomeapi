from typing import List

from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot


class ScalperBot(BaseCustomBot):
    minimumTargetChange: float
    maxAllowedReverseChange: float
