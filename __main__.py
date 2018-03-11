# The beginner trader exec - handles the other functionalities inside the trader umbrella
# Highest in the trader modules ranking - as an executive

import os
from binance.client import Client
from transactors.binanceBuyer import BinanceBuyer
from console.display import welcomeMenu
from console.display import showFunds
from executives.noobBuyer import noobBuyer
from executives.noobSeller import noobSeller
from sockets.overallStream import runTradeSocket
from sockets.overallStream import runUserSocket
from sockets.overallStream import closeSocket
from sockets.overallStream import runPriceSocket

# Get access using API token and API secret
client = Client(os.environ['APITOKEN'], os.environ['APISEC'])

def main():
    inp = -1
    while (True):
        welcomeMenu()
        balance = client.get_asset_balance(asset='NCASH')
        showFunds('NCASH', balance["free"], balance["locked"])
        streams = ["ncashbtc@trade", ""]
        runPriceSocket(client)
        runTradeSocket(client, 'NCASHBTC')
        #runUserSocket(client)

        inp = input("\n Your Choice: ")

        if (inp == 1):
            noobBuyer(client)
        if (inp == 2):
            noobSeller(client)
        if (inp == 0):
            closeSocket()
            exit()
        if (inp == -1):
            continue
    return

if __name__ == "__main__" : main();
