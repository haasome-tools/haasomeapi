from enum import Enum

class EnumSafety(Enum):
    CLOSE_BEFORE_SETTLEMENT = 0
    CLOSE_POSITION_WITH_LOSS = 14
    CLOSE_POSITION_WITH_PROFIT = 15

    DEACTIVATE_BOT_AFTER_BUY = 12
    DEACTIVATE_BOT_AFTER_SELL = 13
    DEAVTIVATE_BOT_AFTER_X_TRADES = 18
    DEAVTIVATE_BOT_AFTER_X_IDLE_MINUTES = 21
    DEAVTIVATE_BOT_AFTER_X_ACTIVE_MINUTES = 22
    
    TOT = 20

    FORCE_TO_BOUGHT_LONG = 7
    FORCE_TO_SOLD_SHORT = 8

    PRICE_PUMP = 16
    PRICE_DUMP = 17

    ROOF_IN_DYNAMIC = 1
    ROOF_IN_FIXED = 2
    ROOF_OUT_DYNAMIC = 3
    ROOF_OUT_FIXED = 4
    RESET_BUY_PRICE = 10
    RESET_SELL_PRICE = 11

    STOP_LOSS_FIXED = 5
    STOP_LOSS_DYNAMIC = 6

    SCRIPT_SAFETY = 9

    HAAS_SCRIPT_SAFETY = 19