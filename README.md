# HaasomeApi - Python Library For Haasonline Local API

WARNING: This Library is still in active development and far from a stable production state. Changes and updates will be frequent and the pip package will be updated constantly. Please report any problems has issues and they will be fixed immediatly.

A Python library to access the Local Api on the Haasonline Trading Platform. Its light weight and extremely easy to use designed to follow the same design paradigm has the rest api and the official c# api wrapper. Making it easy to swap between the two libraries and look up endpoints if need be.

* Api Documentation: [Link](https://haasome-tools.github.io/haasomeapi/)
* Quick Start Guide: [Link](https://haasome-tools.github.io/haasomeapi/haasome.guide.quickstart.html)

#### Install Using Pip

```
pip install --no-cache-dir haasomeapi
```

#### Code Example

```
from haasomeapi.HaasomeClient import HaasomeClient

# Connect to the haas client
haasome = HaasomeClient("http://127.0.0.1:9000", "secretkeyhere")

# Get a dict of all enabled accounts
accounts = haasome.accountDataApi.get_enabled_accounts()

# Select the First Guid
accountGuid = accounts.keys[0]

spotBuy = haasome.tradeApi.place_spot_buy_order(accountGuid, "BNB", "BTC", 0.0020852, 20)
```
