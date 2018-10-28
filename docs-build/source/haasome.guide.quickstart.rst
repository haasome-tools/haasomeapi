Quick Start Guide 
=================


In this guide we will cover some core functionality of the api to get you up and running. 
This guide is going to assume you have already enabled the LocalAPI functionality of your 
Haasonline instance. If not you can find the instructions at https://wiki.haasonline.com/Local_API_Server

Requirments
-----------

- python 3.6+
- virtualenv
- Haasonline Trading Platform 3.1.14+

Setting Up Our Enviornment
--------------------------

First thing we are going to want to do is setup a virtual environment to use for our project. First we will create a folder and then from within the folder create a virtual environment. 

>>> From our favorite terminal on mac,linux, or windows
virtualenv --python=python3 .env

Then we will need to change our environment to the generated one

>>> On Windows We Do
.env/Scripts/activate.bat

>>> On linux/mac we do
source .env/bin/activate

After we have setup our environment we want to install the haasomeapi dependency

>>> In our terminal we do
pip install haasomeapi

Connecting To The Haasonline Local Interface
--------------------------------------------

Now that we have the library and environment setup we want to go ahead and create a file called main.py and save it.
We are going to assume you setup the local api ip to 127.0.0.1 and the port to 9000. 

Inside the file lets add the following lines ignoring the three ">"

>>>
from haasomeapi.HaasomeClient import HaasomeClient
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.enums.EnumOrderType import EnumOrderType
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haasomeapi.enums.EnumBotTradeAmount import EnumBotTradeAmount
haasomeClient = HaasomeClient("http://127.0.0.1:9000", "secretkeyhere")

What we are doing here is importing our api library and then creating a initial connection to the local api. We can verify the connection and credentials are entered correctly by writing the following code under the three we have previously added. This will verify that the secret key we have supplied is correct. If a exception is thrown then we know the ip and port are not set correctly.

>>>
try:
    testCredsResult = haasomeClient.test_credentials()
    if testCredsResult.errorCode == EnumErrorCode.SUCCESS:
        print("Connection Succesfull and Secret Is Correct")
    else:
        print("Connection Failed but Ip and Port are correct")
except:
    print("Connection Failed - Check Ip and Port)

The HaasomeClientResponse Class
-------------------------------
Before we continue we need to understand that unlike normal libraries the functions in this library do not return their objects directly. Instead they all return a HaasomeClientResponse. This class contains the following definition. But whats most important is the errorcode field and the result field. The result can be any class so make sure to handle it according to what the documentation says the function returns

>>>
class HaasomeClientResponse:
    """ Standard Haas API Response Object
    Contains the Haas Local API Response
    :param errorCode: :class:`~haasomeapi.enums.EnumErrorCode`: Error Code Returned if any
    :param errorMessage: str: Error message returned from the server if any
    :param result: any: Can contain anything so check functiona definition
    """
    def __init__(self, errorcode: EnumErrorCode, errormessage: str, result):
        self.errorCode: EnumErrorCode = errorcode
        self.errorMessage: str = errormessage
        self.result = result

Getting Available Accounts and Using One
----------------------------------------
Now what we need to do is get a list of all the activated accounts and select which one to use. For simplicity sake we are just going to use whatever the first one in the list is returned. We can achieve this by doing the following

>>>
# Get a dict of all enabled accounts
accounts = haasomeClient.accountDataApi.get_enabled_accounts()
# Display our current accounts
print (accounts.result)
# Select the First Guid
accountGuid = accounts.keys[0]


Executing A Simple Spot Trade
-----------------------------
Now lets go ahead and execute a simple buy and sell order on binance (We are assuming the accountguid we have selected is a binance account). The format for the parameters are (ACCOUNT_GUID, PRIMARY_COIN, SECONDARY_COIN, PRICE,AMOUNT). These functions will return a template guid. Its important to note that in Haasonline orders have a parent class called "Template" so all orders are actually templates. 

>>>
# Place a spot buy order
spotBuy = haasomeClient.tradeApi.place_spot_buy_order(accountGuid, "BNB", "BTC", 0.0020852, 20)
# Place a spot sell order
spotSell = haasomeClient.tradeApi.place_spot_sell_order(accountguid, "BNB", "BTC", 0.0020852, 20)

Checking Our Order Status
-------------------------
We have created our basic orders but now we need to check the status of the order. There are a few ways we can go about this. First we can just get a list of all open orders on all accounts, or check open orders status. 

>>>
# Get All Open Orders
allOrders = haasome.accountDataApi.get_all_open_orders()
# Get Open Orders From account
orders = haasome.accountDataApi.get_open_orders(accountguid)
# Get the order status specifically
orderStatus = haasome.accountDataApi.get_template_status(spotBuy.result)
# Then we check to see if the order is completed
if orderStatus.result == EnumOrderStatus.COMPLETED:
    print("Order Completed")

Creating A Scalper Bot
----------------------
The final part of this quick start guide is going to show you how to create and backtest a basic scalper bot and backtest it. First things first we need to create the scalper bot to do so we call the function new_custom_bot from the customBotApi. The format for the parameters are (ACCOUNT_GUID, BOT_TYPE, BOT_NAME, PRIMARY_CURRENCY, SECONDARY_CURRENCY, CONTRACT_NAME(Optional))

>>>
newScalper = haasomeClient.customBotApi.new_custom_bot(accountGuid, EnumCustomBotType.SCALPER_BOT,"SuperCoolTutorialBot", "BNB", "BTC", "")

Configure The New Scalper Bot
-----------------------------
Now that we have a new scalper bot created we will want to configure it this can be done using the setup_scalper_bot function in the customBotApi. The format for the function is (ACCOUNT_GUID, BOT_GUID, BOT_NAME, PRIMARY_CURRENCY, SECONDARY_CURRENCY, TEMPLATE_GUID, CONTRACT_NAME, LEVERAGE, AMOUNT_TYPE, TRADE_AMOUNT, POSITION, FEE, TARGET_PERCENTAGE, SAFETY_THRESHOLD)

>>>
newScalperEdited = haasomeClient.customBotApi.setup_scalper_bot(accountGuid, newScalper.result.guid, newScalper.result.name, newScalper.result.primaryCurrency, newScalper.result.secondaryCurrency, "LOCKEDLIMITORDERGUID", "", 0.0, EnumBotTradeAmount.STATIC, 100, "BTC", 0.1, 1.0, 1.0)

Activate The Scalper Bot
------------------------
Now all that is left to do is activate our scalper bot we can do that easily with the activate_custom_bot function in the customBotApi. The format for the function is (BOT_GUID, WITH_EXTRA)


>>>
isActivated = haasomeClient.customBotApi.activate_custom_bot(newScalper.result.guid, False)

Get Status Of Bot
-----------------
After the bot is running we will occasionally want to get the status of the bot, what its current ROI is etc. To do this we simply request a new bot object which will contain all this information for the local api we do this by calling the get_custom_bot function in the customBotApi. The format for this function is (BOT_GUID, BOT_TYPE)

>>>
newBotInfo = haasomeClient.customBotApi.get_custom_bot(newScalper.result.guid, EnumCustomBotType.SCALPER_BOT)

Deactivate The Bot
------------------
Finally we want to deactivate the bot using the deactivate_custom_bot function in the customBotApi. The format for the function is (BOT_GUID, WITH_EXTRA)

>>>
isDeactivated = haasomeClient.customBotApi.activate_custom_bot(newScalper.result.guid, False)

Final Remarks
-------------
Hopefully this is enough to get you up and running with the haasomeapi to control your Haasonline Trade Platform. The HaasomeApi is fully featured and implements all endpoints currently available with the haasonline local api. There is much more we can do with the api and you can find all of this in the documentation.
