from enum import Enum

class EnumFlashSpreadOptions(Enum):
	Fixed_amount = 0
	PERCENTAGE = 1
	PERCENTAGE_WITH_BOOST = 2
	EXPONENTIAL = 3