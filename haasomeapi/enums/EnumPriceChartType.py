from enum import Enum

class EnumPriceChartType(Enum):
	CANDLESTICK = 0
	CANDLESTICK_HLC = 1
	HEIKIN_ASHI = 2
	OHLC = 3
	HLC = 4
	LINE = 5
	MOUNTAIN = 6
	REDBLACK = 7
	SPREAD = 8