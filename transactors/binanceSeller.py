# This implements a seller for the Binance Cryptocurrency Exchange
# Uses the python binance API wrapper to implement selling
# Sold by command from advisors.

import os
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException

class BinanceSeller():
    def __init__(self, client):
        self.client = client

    """
    NAME: sell(coinpair, qty, target)    "Seller"
    PARAMS: coinpair - A string pairing of the coins of the form 'LTCBTC'
                    target - The limit price to buy at
                    qty - An Integer containing the number of coins to buy
    RETURNS: void
    PURPOSE: This method places a sell order on the passed-in coin pair,
                    of the type based on whether parameter 'target' is provided.
                    Identified by the single parameter coinpair.
    """
    def sell(self, coinpair, qty, target=None):
        # Get market depth
        depth = self.client.get_order_book(symbol=coinpair)

        if target is None:
            try:
                # Place buy order
                order = self.client.create_order(symbol=coinpair, side=self.client.SIDE_SELL, type=self.client.ORDER_TYPE_MARKET,
                                                        quantity=qty)
            except BinanceAPIException as e:
                print("Error is: ")
                print(e)
                print("Noob failed to buy. Dumbfuck.")
                return False
        else:
            try:
                # Place buy order
                order = self.client.create_order(symbol=coinpair, side=self.client.SIDE_SELL, type=self.client.ORDER_TYPE_LIMIT,
                                                            timeInForce=self.client.TIME_IN_FORCE_GTC, quantity=qty,
                                                            price=target)
            except BinanceAPIException as e:
                print("Error is: ")
                print(e)
                print("Noob failed to buy. Dumbfuck.")
                return False

        return True
