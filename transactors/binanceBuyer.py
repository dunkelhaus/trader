# This is a buyer for the Binance Cryptocurrency Exchange
# Advisors ask buyers to buy.

import os
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException

class BinanceBuyer():
    def __init__(self, client):
        self.client = client

    """
    NAME: buy(coinpair, qty, target)    "Buyer"
    PARAMS: coinpair - A string pairing of the coins of the form 'LTCBTC'
                    target - The limit price to buy at
                    qty - An Integer containing the number of coins to buy
    RETURNS: void
    PURPOSE: This method places a buy order on the passed-in coin pair,
                    of the type "Market". Identified by the single parameter coinpair.
    """
    def buy(self, coinpair, qty, target=None):
        # Get market depth
        depth = self.client.get_order_book(symbol=coinpair)
        if target is None:
            # Place buy order
            try:
                order = self.client.create_order(symbol=coinpair, side=self.client.SIDE_BUY, type=self.client.ORDER_TYPE_MARKET,
                                                        quantity=qty)
            except BinanceAPIException as e:
                print("Error is: ")
                print(e)
                print("Noob failed to buy. Dumbfuck.")
                return False
        else:
            try:
                # Place buy order
                order = self.client.create_order(symbol=coinpair, side=self.client.SIDE_BUY, type=self.client.ORDER_TYPE_LIMIT,
                                                            timeInForce=self.client.TIME_IN_FORCE_GTC, quantity=qty,
                                                            price=target)
            except BinanceAPIException as e:
                print("Error is: ")
                print(e)
                print("Noob failed to buy. Dumbfuck.")
                return False

        return True
