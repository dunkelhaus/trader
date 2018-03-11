# Implements an overall trade stream
# Socket pushes trade history

from binance.client import Client
from binance.websockets import BinanceSocketManager
import time

socketManager = None
current_milli_time = lambda: int(round(time.time() * 1000))
start = current_milli_time()

def getSocketManager(client):
    global socketManager;
    socketManager = BinanceSocketManager(client)
    return BinanceSocketManager(client)

def closeSocket():
    print("Closing socket ...")
    socketManager.close()
    print("Socket closed.")

def tradeSocketCallback(msg):
    print("{} of {} at price {} at time {}".format(msg['q'], msg['s'], msg['p'], msg['T']))
    # print(msg)

    return

def runTradeSocket(client, coin):
    socketManager = BinanceSocketManager(client)
    conn_key = socketManager.start_trade_socket(coin, tradeSocketCallback)
    print("========== Trade Feed ============")

    socketManager.start()

    return

def userSocketCallback(msg):
    # print("{} of {} at price {} at time {}".format(msg['q'], msg['s'], msg['p'], msg['T']))
    print(msg)

    return

def runUserSocket(client):
    socketManager = getSocketManager(client)
    conn_key = socketManager.start_user_socket(userSocketCallback)
    print("========== User Data Feed ============")

    socketManager.start()

    return

def multiplexSocketCallback(msg):
    # print("{} of {} at price {} at time {}".format(msg['q'], msg['s'], msg['p'], msg['T']))
    print(msg)

    return

def runMultiplexSocket(client, streams, symbol):
    socketManager = BinanceSocketManager(client)
    conn_key = socketManager.start_user_socket(streams, userSocketCallback)
    print("========== Multiplex Data Feed ============")

    socketManager.start()

    return

def priceSocketCallback(msg):
    global start
    diff = current_milli_time() - start
    interval = 120000
    if diff > interval:
        print("============= Universal Price Update ===============")
        for i in msg:
            print("Binance Feed:  {}  Open: {} High: {} Low: {} Close: {} Volume: {}".format(i['s'], i['q'], i['o'], i['h'], i['l'], i['c'], i['v']))
        #print(msg)
        print ("Price update complete. Next update in 2:00 minutes.")
        start = current_milli_time()

    return

def runPriceSocket(client):
    socketManager = getSocketManager(client)
    conn_key = socketManager.start_miniticker_socket(priceSocketCallback, 1000)
    print("Price Socket Activated.")

    socketManager.start()

    return
