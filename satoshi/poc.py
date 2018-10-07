#!/usr/bin/env python



"""
NOTES:

How will we keep track if the price is on the rise/fall?
Where will we determine if the current price just fell/rose by a large amount. A certain amount of cash should be on hand for events like this, and throw it all in when it does
When this happens we need to keep this trade separate from the others
This script should keep track of multiple trades, and determine the profit for all, so that when something unexpected happens we can continue trading
"""


import os
import sys
import time
import datetime
import pickle

from coinbase.wallet.client import Client


try:
    api_key=os.environ["COINBASE_API_KEY"]
    api_secret=os.environ["COINBASE_SECRET_KEY"]
except KeyError as ke:
    print("Error: add COINBASE_API_KEY and COINBASE_SECRET_KEY as environment variables for authentication")
    sys.exit()

client = Client(api_key, api_secret)

def currentPurchasePrice():
    #getCurrentSellPrice(CoinType) + costToTrade + isItWorthIt()
    return 0


class BTC():
    coin = 'btc'
    currency_pair = ''
    if_hodl = False
    trade_id = 0
    price_at_purchase = 0.0
    coin_prices = []
    
    def __init__(self):
        self.next = None
        self.prev = None
        
    def init(self):
        self.currency_pair = self.getCurrencyPair()
        self.trade_id = self.getTradeId()

    def getTradeId(self):
        return self.prev.trade_id + 1

    def calculateProfit(self):                
        profit = self.price_at_purchase - float(self.getSell()['amount'])
        print(profit)
        return profit

    def shouldSell(self):
        pass

    def shouldBuy(self):
        pass

    def getBuy(self):
        buy = client.get_buy_price(currency_pair = self.currency_pair)
        return buy

    def getSell(self):
        sell = client.get_sell_price(currency_pair = self.currency_pair)        
        return sell

    def getCurrencyPair(self):
        if self.coin == 'eth':
            return 'ETH-USD'
        elif self.coin == 'btc':
            return 'BTC-USD'
        elif self.coin == 'ltc':
            return  'LTC-USD'
        else:
            print('OH NO!!! ERROR!!     D:')

    def getCurrentSellPrice(self):
        return client.get_sell_price(currency_pair = self.currency_pair)
    
    def makePurchase(self):
        if self.if_hodl:
            self.next = BTC()
            self.next.prev = self
            self.next.price_at_purchase = float(self.getBuy()['amount'])
            self.next.if_hodl = True
        else:
            self.price_at_purchase = float(self.getBuy()['amount'])
            self.if_hodl = True
    
    def makeSell(self):
        self.if_hodl = False
        
    
    
class ETH(BTC):
    def __init__(self):
        self.coin = 'eth'

class LTC(BTC):
    def __init__(self):
        self.coin = 'ltc'



if __name__ == '__main__':
    tmp_counter = 0
    btc = BTC()
    btc.init()
    ltc = LTC()
    ltc.init()
    eth = ETH()
    eth.init()
    seeds = [btc, ltc, eth]

    while True:
        #btc.coin_prices.append(float(btc.getBuy()['amount']))
        #ltc.coin_prices.append(float(ltc.getBuy()['amount']))
        #eth.coin_prices.append(float(eth.getBuy()['amount']))
        
        ## save often
        #if tmp_counter == 3:
        if tmp_counter == 2:
            if not os.path.exists('data/'):
                print('making data dir')
                os.mkdir('data')
            for i in seeds:
                data_file = 'data/{0}.data'.format(i.coin)
                if os.path.exists(data_file):
                    os.rename(data_file, '{0}.{1}'.format(data_file, datetime.date.today()))
                    print(ltc.currency_pair)
            
                data = open(data_file, 'wb')
                pickle.dump(btc, data)
                data.close()

            tmp_counter = 0            
            sys.exit()

        tmp_counter+=1
        #time.sleep(300)
        time.sleep(1)
