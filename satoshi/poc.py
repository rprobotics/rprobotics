#!/usr/bin/env python



"""
NOTES:

How will we keep track if the price is on the rise/fall?
Where will we determine if the current price just fell/rose by a large amount. A certain amount of cash should be on hand for events like this, and throw it all in when it does
When this happens we need to keep this trade separate from the others
This script should keep track of multiple trades, and determine the profit for all, so that when something unexpected happens we can continue trading
"""


import os
import pickle

from coinbase.wallet.client import Client


try:
    api_key=os.environ["COINBASE_API_KEY"]
    api_secret=os.environ["COINBASE_SECRET_KEY"]
except KeyError as ke:
    print("Error: add COINBASE_API_KEY and COINBASE_SECRET_KEY as environment variables for authentication")


client = Client(api_key, api_secret)

#btcBuyPrice=client.get_buy_price(currency_pair = 'BTC-USD')
#ethBuyPrice=client.get_buy_price(currency_pair = 'ETH-USD')
#ltcBuyPrice=client.get_buy_price(currency_pair = 'LTC-USD')
#btcSellPrice=client.get_sell_price(currency_pair = 'BTC-USD')
#ltcSellPrice=client.get_sell_price(currency_pair = 'LTC-USD')
#ethSellPrice=client.get_sell_price(currency_pair = 'ETH-USD')
#print(ethBuyPrice['amount'])
#print(ethSellPrice['amount'])

def getCurrentSellPrice(coin):
    if coin == "eth":
        return client.get_sell_price(currency_pair = 'ETH-USD')
    elif coin == "btc":
        client.get_sell_price(currency_pair = 'BTC-USD')
    elif coin == "ltc":
        client.get_sell_price(currency_pair = 'LTC-USD')
    else:
        print("OH NO!!! ERROR!!     D:")

def shouldSell():
    pass

def shouldBuy():
    pass

"""
Calculate whether a trade has the potential to return a profit
If we are looking to sell then we need to determine the difference between when we bought, and the current sell price
The opposite should hold true for a buy
"""
def calculate_profit():        
    pass


def currentPurchasePrice():
    #getCurrentSellPrice(CoinType) + costToTrade + isItWorthIt()
    return 0



