# The beginner trader exec - handles the other functionalities inside the trader umbrella
# Highest in the trader modules ranking - as an executive

import os
from binance.client import Client
from transactors.binanceBuyer import BinanceBuyer

# Get access using API token and API secret
client = Client(os.environ['APITOKEN'], os.environ['APISEC'])

def main():
    print("Starting Noob Trader ...")
    print("A Noob buys - always buys - blindly buys - always market price.")
    print("To a Noob, everything is bullish, everytime.")
    print("This is an NCASH Noob")
    coinpair = 'NCASHBTC'

    buyer = BinanceBuyer(client)
    result = buyer.buy(coinpair, 50)

    if (result):
        print("Noob has bought. God bless Noobs.")

    return

if __name__ == "__main__" : main();
