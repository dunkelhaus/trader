# The beginner trader exec - handles the other functionalities inside the trader umbrella
# Highest in the trader modules ranking - as an executive

import os
from binance.client import Client
from transactors.binanceSeller import BinanceSeller
from console.display import orderConfirmation

def noobSeller(client):
    print("Starting Noob Trader ...")
    print("A Noob buys - always buys - blindly buys - or panic sells.")
    print("To a Noob, everything is bullish, everytime.")
    print("So if anything goes even a little down, time to sell!")
    print("This is an NCASH Noob Seller \n")

    coinpair = 'NCASHBTC'
    seller = BinanceSeller(client)
    qty = 0
    price = ''
    qty = input("How much do you want to sell?  :")
    print("\n")
    price = raw_input("At what price?")
    orderConfirmation(coinpair, price, qty, "SALE")
    print("\nSelling ...")

    result = seller.sell(coinpair, qty, price)

    if (result):
        print("Noob has panic sold. Poor noob.")

    return
