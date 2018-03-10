# The beginner trader exec - handles the other functionalities inside the trader umbrella
# Highest in the trader modules ranking - as an executive

import os
from binance.client import Client
from transactors.binanceBuyer import BinanceBuyer
from console.display import welcomeMenu
from executives.noobBuyer import noobBuyer
from executives.noobSeller import noobSeller

# Get access using API token and API secret
client = Client(os.environ['APITOKEN'], os.environ['APISEC'])

def main():
    inp = -1
    while (inp != 0):
        welcomeMenu()
        inp = input("\n Your Choice: ")

        if (inp == 1):
            noobBuyer(client)
        if (inp == 2):
            noobSeller(client)
        if (inp == 0):
            exit()
        if (inp == -1):
            continue
    return

if __name__ == "__main__" : main();
