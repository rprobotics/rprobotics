#!/usr/bin/env python

import os

from coinbase.wallet.client import Client


try:
    api_key=os.environ["COINBASE_API_KEY"]
    api_secret=os.environ["COINBASE_SECRET_KEY"]
except KeyError as ke:
    print("Error: add COINBASE_API_KEY and COINBASE_SECRET_KEY as environment variables for authentication")


client = Client(api_key, api_secret)


