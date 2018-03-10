# The beginner trader exec - handles the other functionalities inside the trader umbrella
# Highest in the trader modules ranking - as an executive

import os
from binance.client import Client
from transactors.binanceBuyer import BinanceBuyer
from console.display import orderConfirmation

def noobBuyer(client):
    print("Starting Noob Trader ...")
    print("A Noob buys - always buys - blindly buys - always market price.")
    print("To a Noob, everything is bullish, everytime.")
    print("This is an NCASH Noob Buyer \n")

    coinpair = 'NCASHBTC'
    buyer = BinanceBuyer(client)
    qty = 0
    price = ''
    qty = input("How much do you want to buy? : ")
    print("\n")
    price = raw_input("At what price? : ")
    orderConfirmation(coinpair, price, qty, "PURCHASE")
    print("\nBuying ...")

    result = buyer.buy(coinpair, qty, price)

    if (result):
        print("Noob has bought. God bless Noobs.")

    return
